#!/usr/bin/env python3

# external modules

# my modules
import PERM
import DCC
import Config as CF
import MyUtil

# Define the top level collection or document to check
target = 'Collection-10725'
# target = 'Collection-10259'

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
pg_user = 'User-27'     # Paul Gillett

check_user = pg_user

permissions = [{check_user : ''}]

# Now call the checkPerms function
[passList,failList] = PERM.checkPerms(target, permissions)

print('Pass List:', passList)
print('Fail List:', failList)

# Login to DCC
s = DCC.login(CF.dcc_url + CF.dcc_login)

for handle in passList:
    print('\n\n')
    if 'Document' in handle:
        fd = DCC.prop_get(s, handle, InfoSet = 'DocBasic', Print = True)
        perm = DCC.prop_get(s, handle, InfoSet = 'Perms', Print = True)
        perm = MyUtil.remove_dict_from_list(perm,'handle', check_user)
        print('After: ')
        DCC.print_perms(perm)
    elif 'Collection' in handle:
        fd = DCC.prop_get(s, handle, InfoSet = 'CollData', Print = True)
        perm = DCC.prop_get(s, handle, InfoSet = 'Perms', Print = True)
#         DCC.print_coll_data(fd)
#         perm = fd['permissions']
        fd = MyUtil.remove_dict_from_list(perm,'handle', check_user)
        print('After: ')
        DCC.print_perms(perm)

    else:
        print('Not Document or Collection')

    if MyUtil.get_yn('Change Permissions (Y/N)?'):
        print('Changing permissions...')
        DCC.set_permissions(s, handle, perm)