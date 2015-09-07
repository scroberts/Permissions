#!/usr/bin/env python3

# external modules

# my modules
import PERM
import DCC
import Config as CF
import myutil

# Define the top level collection or document to check
target = 'Collection-10725'
target = 'Collection-10259'

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

acm_user = 'User-1054'  # Amanda Cuetto-Moll
ks_user = 'User-138'    # Kei Szeto
tc_user = 'User-1165'   # Tomas Chylek

permissions = [{ks_user : ''}]

# Now call the checkPerms function
[passList,failList] = PERM.checkPerms(target, permissions)

print('Pass List:', passList)
print('Fail List:', failList)

# passList = ['Collection-10731', 'Collection-10887', 'Collection-10749', 'Collection-10748', 'Collection-10746', 'Collection-10743', 'Document-49004', 'Document-48445','Document-48876', 'Document-48389', 'Document-47885', 'Document-48330']

# Login to DCC
s = DCC.login(CF.dcc_url + CF.dcc_login)

for handle in passList:
    print('\n\n')
    if 'Document' in handle:
        fd = DCC.prop_get(s, handle, InfoSet = 'DocBasic')
        DCC.print_doc_basic(fd)
        perm = DCC.prop_get(s, handle, InfoSet = 'Perms')
        perm = myutil.remove_dict_from_list(perm,'handle', ks_user)
        print('After: ')
        DCC.print_perm(perm)
    elif 'Collection' in handle:
        fd = DCC.prop_get(s, handle, InfoSet = 'CollData')
        DCC.print_coll_data(fd)
        perm = fd['permissions']
        fd = myutil.remove_dict_from_list(perm,'handle', ks_user)
        print('After: ')
        DCC.print_perm(perm)

    else:
        print('Not Document or Collection')

    if myutil.get_yn('Change Permissions (Y/N)?'):
        print('Changing permissions...')
        DCC.set_permissions(s, handle, perm)