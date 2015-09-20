#!/usr/bin/env python3

# external modules

# my modules
import DCC
import Config as CF
import Tree
import FileSys
import PERM_DEFS
import Match
import PERM
import MyUtil


def main():
    # Login to DCC
    s = DCC.login(CF.dcc_url + CF.dcc_login) 
    
    #****** SET Flag for asking about changes ******
#     ask_flag = False
    ask_flag = True
    
    #****** Choose SET ******
#     set = PERM_DEFS.SET_M1CS_PDR
#     set = PERM_DEFS.SET_REMOVE_STR_MANAGERS
#     set = PERM_DEFS.SET_SE_READERSHIP    
#     set = PERM_DEFS.SET_IRIS_REMOVEUSERS_1
#     set = PERM_DEFS.SET_IRIS_REMOVE_MATTHIAS_MANAGE_FALSE
    set = PERM_DEFS.SET_IRIS_REMOVE_ISBRUCKER
    
    #****** Choose Collection ******
#     m1cs_pdr_root = 'Collection-10725'
#     m1cs_pdr_presentation = 'Collection-10821'
#     handle = m1cs_pdr_presentation

#     config_control = 'Collection-8277'
#     handle = config_control

    IRIS_science = 'Collection-7542'
    handle = IRIS_science
    
    #******!!!  Run !!! ******
#     print(set)
    PERM.check_perms(s, set, handle, 'Tree_' + handle, Ask = ask_flag)

if __name__ == '__main__':
    print("Running module test code for",__file__)
    
    main()