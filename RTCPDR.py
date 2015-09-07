#!/usr/bin/env python3

# external modules

# my modules
import PERM

# Define the top level collection or document to check
target = 'Collection-10045'

# Define a list data structure of users or groups in sets that are
# acceptable if they have read permission to the collections and files
# The with the following logic: 
#
#   All contents of sets must be acceptable in an AND case (i.e. every
#       member of a set must have read access to be acceptable) 
#
#   Permissions will be acceptable if any set is acceptable in an OR
#     	sense (i.e. if one set meets the criteria then the the
#     	permissions are considered okay)

sys_eng_read = 'Group-325'
ext_panel = 'Group-644'
int_panel = 'Group-646'
obs_panel = 'Group-647'

permissions = [{sys_eng_read : 'R'},{ext_panel : 'R', int_panel : 'RW', obs_panel : 'R'}]

# Now call the checkPerms function
PERM.checkPerms(target, permissions)