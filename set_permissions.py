#!/usr/bin/env python3

# external modules

# my modules
import DCC
import Config as CF
import Tree
import FileSys
import PERM_DEFS as PD
import Match
import PERM
import MyUtil


def main():
    # Login to DCC
    s = DCC.login(CF.dcc_url + CF.dcc_login) 
    
    #****** SET Flag for asking about changes ******
    ask_flag = MyUtil.get_yn('Ask about changes to files ***  BE CAREFUL !!! *** (Y/N)? ')
    print()
        
    #****** Choose SET ******
    
    ### Safe to run without checking ###
#     set = PD.SET_REMOVE_RO_IF_SE_READERSHIP 
#     set =  PD.SET_REMOVE_STR_MANAGERS 
#     set = PD.SET_REMOVE_INACTIVE
    set = PD.SET_PUBLISHED
  
    ### Don't Run without checking ###
#     set = PD.SET_PERM_NRTCPDR
#     set = PD.SET_M1CS_PDR
#     set = PD.SET_REMOVE_STR_MANAGERS
#     set = PD.SET_SE_READERSHIP    
#     set = PD.SET_IRIS_REMOVE_MATTHIAS_MANAGE_FALSE
#     set = PD.SET_IRIS_REMOVE_ISBRUCKER
#     set = PD.SET_REPLACE_IRIS_EAR_WITH_ALL
#     set = PD.SET_REMOVE_STR_MANAGERS
#     set = PD.SET_REMOVE_UNNEEDED

### IRIS Manager Set with removal of group membership
#     set = PD.SET_IRIS_TEAM
#     ghs = PERM.get_group_handles(s,PD.grp_IRIS_MANAGE)
#     for gh in ghs:
#         PD.SET_ADD_IRIS_MANAGER['PermAct'].append(PD.remove_user(gh))
#     print(PD.SET_ADD_IRIS_MANAGER['PermAct'])

### IRIS Team Set with removal of group members
#     set = PD.SET_IRIS_TEAM   
#     ghs = PERM.get_group_handles(s,PD.grp_IRIS_team)
#     for gh in ghs:
#         PD.SET_IRIS_TEAM['PermAct'].append(PD.remove_user_ifperms(gh, PD.manage_false)) 
#     print(PD.SET_IRIS_TEAM['PermAct'])


### M1S Team Set with removal of optics group members
#     set = PD.SET_M1S_Suijian
#      
#     PD.remove_user_if_group(s, set, PD.grp_optics, PD.manage_false)
#     PD.remove_user_if_group(s, set, PD.grp_niaotEAR, PD.WM_false)
#  
#     print(PD.SET_M1S_Suijian['PermAct'])        

### CRYO Team Set with removal of optics group members
#     set = PD.SET_EMPTY
#      
#     PD.remove_user_if_group(s, set, PD.grp_CryoTeam, PD.manage_false)
#     PD.remove_user_if_group(s, set, PD.grp_CryoManager,PD.read_true)
#  
#     print(PD.SET_EMPTY['PermAct'])      
        
    #****** Choose Collection ******
#     m1cs_pdr_root = 'Collection-10725'
#     m1cs_pdr_presentation = 'Collection-10821'
#     handle = m1cs_pdr_presentation

#     config_control = 'Collection-8277'
#     handle = config_control

    IRIS_science = 'Collection-7542'
    IRIS = 'Collection-2463'
    Change_control = 'Collection-399'
    SE_access_handling = 'Collection-2949'
    SE_interface_control = 'Collection-195'
    SE_budgets = 'Collection-309'
    Published = 'Collection-8277'
    IRIS_LPDR = 'Collection-11161'
    NRTC_PDR = 'Collection-10045'
    M1S_suijian_coll = 'Collection-5678'
    CRYO_coll = 'Collection-9141'
    LGSF_IOE = 'Collection-4956'
    ENC_Construction_Phase = 'Collection-10598'
    
    Test = 'Document-27819'
    
#     set = PD.SET_ENC_CONSTRUCTION
#     set = PD.SET_REMOVE_RO_IF_SE_READERSHIP
#     handle = ENC_Construction_Phase
#     handle =  Test
    handle = Published
    
    #******!!!  Run !!! ******
#     print(set)
    tr = Tree.return_tree(s, handle, 'Tree_' + handle)
    handles = Tree.get_flat_tree(tr)
    PERM.check_perms(s, set, handles, Ask = ask_flag)

if __name__ == '__main__':
    print("Running module test code for",__file__)
    
    main()