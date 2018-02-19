__author__ = 'zelalem'

################################################################################
# Licensed under LGPL. See <docs/LICENSE.txt> or <http://opensource.org/licenses/LGPL-3.0>
################################################################################
'''
Created on 31.03.2014

@author: Tonio
'''

'''
time structure class.
The structure attribute is the most important.
structure is a dictionary. The keys are IDs and their values are tuples.
These tuples each contain a time object and a set of its relations to others.
'''


class TimeStructure():
    def __init__(self, taleName, text):
        self.taleName = taleName
        self.structure = dict()
        self.idCounter = 0
        self.tale = text

    def reprStruct(self):
        for i in self.structure:
            print i, self.structure[i]