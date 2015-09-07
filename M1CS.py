#!/usr/bin/env python3

# external modules

# my modules
import PERM

# Define the top level collection or document to check
target = 'Collection-10725'

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
ext_panel = 'Group-639'
int_panel = 'Group-640'
obs_panel = 'Group-641'

jpl_m1cs = 'Group-96'
tel_controls = 'Group-465'
tmt_se = 'Group-103'
sw_in = 'Group-454'
ear_in = 'Group-219'

amanda = 'User-1054'
amanda_test = 'User-1086'
nancy = 'User-1191'
site = 'User-2'

# permissions = [{sys_eng_read : 'R'},{ext_panel : 'R', int_panel : 'RW', obs_panel : 'R'}]
permissions = [{jpl_m1cs : 'RW', tel_controls : 'RW', tmt_se : 'RW', sw_in : 'R', ear_in : 'R'}]
# permissions = [{amanda : ''}, {amanda_test : ''}, {nancy : ''}, {site : ''}]

# Now call the checkPerms function
PERM.checkPerms(target, permissions)