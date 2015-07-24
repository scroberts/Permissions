#!/usr/bin/env python3

# external modules
import pprint
import json

# my modules
import DCC
import get_url_word
import config as cf

FDRP2_coll = 'Collection-10071'
# FDRP2_coll = 'Document-21380'

sys_eng_read = 'Group-325'
ext_panel = 'Group-574'
int_panel = 'Group-576'
obs_panel = 'Group-577'

def print_check_perms(perm):
    read_okay = False
    print("[",perm["handle"],"]:\t","perms = ",sep="",end="")
    if "Search" in perm.keys():
        print("[Search]", end="")
    if "Read" in perm.keys():
        print("[Read]", end="")
        read_okay = True
    if "Write" in perm.keys():
       print("[Write]", end="")
    if "Manage" in perm.keys():
        print("[Manage]", end="")
    print(", \"",perm['name'],"\"",sep="")
    return read_okay

# Login to DCC
s = DCC.login(cf.dcc_url + cf.dcc_login)

#DCC.get_collections_in_collection(s, FDRP2_coll)
doclist = DCC.get_files_in_collection(s, FDRP2_coll)

for doc in doclist:
    dom = DCC.dom_prop_find(s, doc)
    fd = DCC.read_dcc_doc_data(dom)
    
    print("\n\n*** Document Entry", fd['dccnum'], "***\n")
    print("DCC Document Number/Name: ", fd['dccnum'],", \"",fd['dccname'],"\"",sep="")
    print("TMT Document Number: ", fd['tmtnum'])
    print("https://docushare.tmt.org/docushare/dsweb/ServicesLib/" + fd['dccnum'] + "/view")
        
    all_perms_okay = False
    ext_perms_okay = False
    int_perms_okay = False
    obs_perms_okay = False
    
    for perm in sorted(fd["permissions"], key = lambda x: x["handle"]):
        if perm["handle"] == sys_eng_read:
            all_perms_okay = print_check_perms(perm)
        if perm["handle"] == ext_panel:
            ext_perms_okay = print_check_perms(perm)
        if perm["handle"] == int_panel:
            int_perms_okay = print_check_perms(perm)
        if perm["handle"] == obs_panel:
            obs_perms_okay = print_check_perms(perm)
            
    if all_perms_okay or (ext_perms_okay and int_perms_okay and obs_perms_okay):
        print("Review panel can access this document")
    else:
        print("!!! PERMISSIONS PROBLEM - Panel cannot access this document !!!")
