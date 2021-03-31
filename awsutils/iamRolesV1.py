import boto3
import csv

#client = boto3.client('iam',aws_access_key_id="XXXX",aws_secret_access_key="YYY")
client = boto3.client('iam')
users = client.list_users()
user_list = []
ofh= open("userlist.csv", "w")
fieldnames = ['userName', 'Groups', 'Policies','isMFADeviceConfigured']
writer = csv.DictWriter(ofh, fieldnames=fieldnames)
writer.writeheader()
for key in users['Users']:
    result = {}
    Policies = []
    Groups=[]
    result['userName']=key['UserName']
    k1 = key['UserName']
    List_of_Policies =  client.list_user_policies(UserName=key['UserName'])
    print(type(List_of_Policies['PolicyNames']))
    List_of_Policies1 =  client.list_attached_user_policies(UserName=key['UserName'])
#    if List_of_Policies1:
#        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!###############################################################################")
#        print(List_of_Policies1)
#        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!###############################################################################")
#        print(List_of_Policies1['AttachedPolicies'][0]['PolicyName'])
#        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!###############################################################################")
#        print(type(List_of_Policies1['AttachedPolicies']))
        #for item in List_of_Policies1['AttachedPolicies']:
        #    print(item)
    # Need to read the policies attached from group.  For this extract the group assoicated with the user first
    # Then iterate over the groups and ginf policies.
    # Finally append the policies to List_of_Policies['PolicyNames']
    List_of_Groups =  client.list_groups_for_user(UserName=key['UserName'])
    for Group in List_of_Groups['Groups']:
        Groups.append(Group['GroupName'])
    result['Groups'] = Groups
    if Groups:
        print("List of group Policies ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        for x in Groups:
             List_of_Group_Policies =  client.list_attached_group_policies(GroupName=x)
             print (List_of_Group_Policies)
             for y in  List_of_Group_Policies['AttachedPolicies']:
                 List_of_Policies['PolicyNames'].append(y['PolicyName'])

    if not List_of_Policies1:
        result['Policies'] = List_of_Policies['PolicyNames']
        print("###############################################################################")
    else:
        for x in List_of_Policies1['AttachedPolicies']:
            #print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
            #print(x)
            #print(x['PolicyName'])
            List_of_Policies['PolicyNames'].append(x['PolicyName'])

        result['Policies'] = List_of_Policies['PolicyNames']
    #print('****************************************************')
    print (result['Policies'])


    List_of_MFA_Devices = client.list_mfa_devices(UserName=key['UserName'])

    if not len(List_of_MFA_Devices['MFADevices']):
        result['isMFADeviceConfigured']=False
    else:
        result['isMFADeviceConfigured']=True
    user_list.append(result)
   # print(result)
    for k,v in result.items():
        if v :
            #print(v)
            pass
        else:
            result[k] = None

    #writer.writerow(result['userName'],result['Groups'],  result['Policies'], result['isMFADeviceConfigured'])
    #print(result)
    writer.writerow(result)

for key in user_list:
#    print (key)
    pass
#for k, v in result.items():
#        writer.writerow([k, v])


