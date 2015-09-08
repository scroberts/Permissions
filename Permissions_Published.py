#!/usr/bin/env python3

# my modules
import DCC
import Config as CF
import Tree
import PERM

collhandle = 'Collection-8279'
collhandle = 'Collection-9895'
collhandle = 'Collection-8288'
collhandle = 'Collection-8711'
collhandle = 'Collection-9908'
collhandle = 'Collection-9889'

actions = [ {'Criteria' : {'HandlePattern' : 'User-', 'Read' : True, 'Write' : False, 'Manage' : False}, 'Action' : 'Remove'},
            {'Criteria' : {'HandlePattern' : 'Group-', 'Read' : True, 'Write' : False, 'Manage' : False}, 'Exclude' : ['Group-325', 'Group-4'], 'Action' : 'Remove'},
            {'Criteria' : {'Read' : False, 'Write' : False, 'Manage' : False} ,'Exclude':['Group-4'], 'Action' : 'Remove'},
            {'Criteria' : {'Read' : False, 'Write' : True, 'Manage' : False} ,'Exclude':['Group-4'], 'Action' : 'Remove'},
            {'Criteria' : {'Read' : False, 'Write' : False, 'Manage' : True} ,'Exclude':['Group-4'], 'Action' : 'Remove'},
            {'Criteria' : {'HandleMatches' : 'Group-4'}, 'Action' : 'Remove'},
            {'Criteria' : {'HandleMatches' : 'Group-536'}, 'Action' : 'Remove'},
            {'Criteria' : {'HandleMatches' : 'User-1083'}, 'Action' : 'Remove'},
            {'Criteria' : {'HandleMatches' : 'User-21'}, 'Action' : 'Remove'},
            {'Criteria' : {'HandleMatches' : 'User-2'}, 'Action' : 'Remove'},
            {'Criteria' : {'HandleMatches' : 'User-1087'}, 'Action' : 'Remove'},
            {'Criteria' : {'HandleMatches' : 'User-120'}, 'Action' : 'Remove'},
            {'Criteria' : {'HandleMatches' : 'User-1165'}, 'Action' : 'Remove'},
            {'Criteria' : {'HandleMatches' : 'User-383'}, 'Action' : 'Remove'},
            {'Criteria' : {'Absent' : 'Group-325'}, 'Action' : 'Add', 'Handle': 'Group-325', 'Perms' : {'Read':True}},
            {'Criteria' : {'Absent' : 'Group-103'}, 'Action' : 'Add', 'Handle': 'Group-103', 'Perms' : {'Read':True, 'Write':True}}]

# Login to DCC
s = DCC.login(CF.dcc_url + CF.dcc_login)

tree = Tree.get_tree(s, collhandle)
Tree.print_tree(s,tree)
flatTree = Tree.flat_tree(tree, 'root', [])

for handle in flatTree:
    PERM.fixPerm(s,handle, actions)
