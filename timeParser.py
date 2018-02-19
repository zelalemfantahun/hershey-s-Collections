__author__ = 'zelalem'

################################################################################
# Licensed under LGPL. See <docs/LICENSE.txt> or <http://opensource.org/licenses/LGPL-3.0>
################################################################################
'''
Created on 02.04.2014

@author: Tonio
'''

"""
TimeParser class. Instantiated without arguments.
The main method is "parse". It calls the other methods and returns a timeStructure object.
"""

import re
import sys
from os import getcwd
from timeStructure import TimeStructure
import timeObjects as to
import os

class TimeParser():
    def __init__(self):

        """
        Regular expressions for dialogue recognition during creation of surface structure.
        Used by the method "surfaceStructure".
        """

        # ## Surface Structure tokens
        # sentence without direct speech
        self.ss1 = r'[A-Z][^?.!"]*[?.!]\s'
        # direct speech phase
        self.ss2 = r'[^?.!"]*\"[^"]*[?!.]\'?\"\s'
        # direct speech followed by narration
        self.ss3 = r'\"[^"]*\",?\s?[a-z][^?.!"]*[?.!]\s'
        # direct speech phase interrupted by narration
        self.ss4 = r'\"[^"]*\"\s[^?.!"]+\"[^\"]*\"\s'
        # complex sentence
        self.ss5 = r'[^?.!"]*\"[^?.!"]*\"\s[a-z][^?.!"]*[?.!]\s'
        # All together make up the surface structure:
        self.ssTokens = self.ss3 + '|' + self.ss2 + '|' + self.ss1 + '|' + self.ss4 + '|' + self.ss5
        # For Testing
        self.ssTokensTest = self.ss2 + '|' + self.ss3 + '|' + self.ss1 + '|' + self.ss4 + '|' + self.ss5


        """
        Regular expressions for the filtering of time relations.
        Used by the methods "startingPoint" and "deepStructure".
        """

        # ## Unfixed Time
        self.ds1 = re.compile(r'(Now )?(o|O)ne day,?(.*)')
        self.ds2 = re.compile(r'In olden times,?( when wishing still did some good)?,?(.*)')
        self.ds3 = re.compile(r'Once,?(.*)')

        # ## Simultaneousness
        self.ds4 = re.compile(r'Just then,?(.*)')

        # ## Sequencial Relations
        # right after (explicitly mentioned in the text)
        self.ds5 = re.compile(r'Then,?(.*)')
        self.ds6 = re.compile(r'After this,?(.*)')
        # later
        self.ds7 = re.compile(r'Before long,?(.*)')
        # next morning
        self.ds8 = re.compile(r'The next morning,?(.*)')
        self.ds9 = re.compile(r'And so it went on until the morning, when,?(.*)')
        self.ds10 = re.compile(r'By daybreak,?(.*)')
        # next day
        self.ds11 = re.compile(r'The next day,?(.*)')
        self.ds12 = re.compile(r'On the second day,?(.*)')
        self.ds13 = re.compile(r'On the third day,?(.*)')
        # a year after
        self.ds14 = re.compile(r'A year after,?(.*)')

        # ## groups with the int values indicating the desired group inside the regular expression
        self.unfixed = ([(self.ds1, 3), (self.ds2, 2), (self.ds3, 1)], 'unfixed')
        self.simultaneous = ([(self.ds4, 1)], 'simultaneous')
        self.explicitAfter = ([(self.ds5, 1), (self.ds6, 1)], 'explicit after')
        self.later = ([(self.ds7, 1)], 'later')
        self.nextMorning = ([(self.ds8, 1), (self.ds9, 1), (self.ds10, 1)], 'next morning')
        self.nextDay = ([(self.ds11, 1), (self.ds12, 1), (self.ds13, 1)], 'next day')
        self.yearAfter = ([(self.ds14, 1)], 'a year after')
        # list of the groups
        self.dsRelations = [self.unfixed, self.simultaneous, self.explicitAfter, self.later, self.nextMorning, self.nextDay, self.yearAfter]


    """
    parse takes a tale name, creates a corresponding time structure object and calls the other methods.
    Returns a filled & completed time structure object for the given tale.

    Possible tale names at this time:
    The-Swan-Geese.txt, The Bremen Town Musicians.txt, The-Frog-King.txt, Rumpelstiltskin.txt
    """

    def parse(self, taleName):
        projectDir = r'SoPro13Python.*'
        dataDir = r'SoPro13Python'+os.sep +'data'+os.sep + taleName #new
        # dataDir = r'SoPro13Python\data\\' + taleName               #old
        directory = re.sub(projectDir, dataDir, getcwd())
        redundantSpace = r'[\s\n]+'
        try:
            with open(directory, 'r') as f:
                struct = TimeStructure(taleName, re.sub(redundantSpace, ' ', ''.join([line for line in f])))
        except IOError:
            sys.exit(1)
        return self.relationInference(self.deepStructure(self.startingPoint(self.surfaceStructure(struct))))


    """
    surfaceStructure is called by parse. It takes an empty time structure and filles it with time objects of the type 'ss' (surface structure).
    Returns the filled time structure object.
    """

    def surfaceStructure(self, struct):
        for token in [sent.lstrip() for sent in re.findall(self.ssTokens, struct.tale)]:
            struct.idCounter += 1
            struct.structure[struct.idCounter] = (to.timeObject(struct.idCounter, token, 'ss'), set())
        return struct


    """
    startingPoint takes a structure filled with time objects of a surface structure.
    Returns the structure with the beginning of the tale turned in into an oriantation point unfixed in time (before narration of course).
    """

    def startingPoint(self, struct):
        for (regex, desiredGroup) in self.unfixed[0]:
            match = re.search(regex, struct.structure[1][0].text)
            if match:
                struct.structure[1] = (to.timeObject(1, struct.structure[1][0].text, 'ds'), {('unfixed', 0)})
                # struct.structure[1] = (to.timeObject(1, match.group(desiredGroup).lstrip(), 'ds'), {('unfixed', 0)})
                return struct
        struct.structure[1] = (to.timeObject(1, struct.structure[1][0].text, 'ds'), {('unfixed', 0)})
        return struct


    """
    deepStructure takes a surface structure with a starting point and parses the structure for certain time adverbs (relations).
    Returns a deep structure containing relations between time objects. The necessary regular expressions are defined in the __init__ method.
    """

    def deepStructureHelp(self, struct, key, regexList, text, relation):
        for (regex, desiredGroup) in regexList:
            match = re.search(regex, text)
            if match:
                # struct.structure[key] = (to.timeObject(key, match.group(desiredGroup).lstrip(), 'ds'), {(relation, key-1)})
                struct.structure[key] = (to.timeObject(key, text, 'ds'), {(relation, key - 1)})
                return (struct, True)
        return (struct, False)

    def deepStructure(self, struct):
        for (key, value) in struct.structure.items()[1:]:
            relationMatch = False
            text = value[0].text
            for (regexList, relation) in self.dsRelations:
                (struct, relationMatch) = self.deepStructureHelp(struct, key, regexList, text, relation)
                if relationMatch:
                    break
            if relationMatch == False:
                struct.structure[key] = (to.timeObject(key, struct.structure[key][0].text, 'ds'), {('default after', key - 1)})
        return struct


    """
    relationInference fills in the counterparts of symmetrical relations.
    Returns the complete structure.
    """

    def relationInference(self, struct):
        for (key, value) in struct.structure.items()[1:]:
            sharedRelations = set()
            for (relation, target) in value[1]:
                if relation == 'simultaneous':
                    struct.structure[target][1].add(('simultaneous', key))
                    for sharedRelation in struct.structure.copy()[target][1]:
                        sharedRelations.add(sharedRelation)
            for (relation, target) in sharedRelations:
                if target != key:
                    struct.structure[key][1].add((relation, target))
        return struct