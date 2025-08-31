import os, json
import pandas as pd
# # Transaction Individual Data Analysis
# Data = open("F:/MDTM46B/Phonepe/data/top/transaction/country/india/state/andaman-&-nicobar-islands/2018/1.json",'r')
# D = json.load(Data)
# print(D)

#agg transaction data
# path1  =  "F:/MDTM46B/Phonepe/data/aggregated/transaction/country/india/state/"
# Agg_list  =  os.listdir(path1)

# clm1 = {'State':[], 'Year':[],'Quater':[],'Transacion_type':[], 'Transacion_count':[], 'Transacion_amount':[]}
# for state in Agg_list:
#     state1 = path1+state+"/"
#     Agg_yr = os.listdir(state1)
#     for year in Agg_yr:
#         year1 = state1+year+"/"
#         Agg_yr_list = os.listdir(year1)
#         for data in Agg_yr_list:
#             data1 = year1+data
#             Data = open(data1,'r')
#             D = json.load(Data)
#             for z in D['data']['transactionData']:
#               Name = z['name']
#               count = z['paymentInstruments'][0]['count']
#               amount = z['paymentInstruments'][0]['amount']
#               clm1['Transacion_type'].append(Name)
#               clm1['Transacion_count'].append(count)
#               clm1['Transacion_amount'].append(amount)
#               clm1['State'].append(state)
#               clm1['Year'].append(year)
#               clm1['Quater'].append(int(data.strip('.json')))
# # #Succesfully created a dataframe
# Agg_Trans = pd.DataFrame(clm1)
# Agg_Trans["State"] = Agg_Trans["State"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
# Agg_Trans["State"] = Agg_Trans["State"].str.replace("-"," ")
# Agg_Trans["State"] = Agg_Trans["State"].str.title()
# Agg_Trans['State'] = Agg_Trans['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")
# # print(Agg_Trans)

# #agg insurance data
# path2  =  "F:/MDTM46B/Phonepe/data/aggregated/insurance/country/india/state/"
# Agg_insure_list  =  os.listdir(path2)

# clm2 = {'State':[], 'Year':[],'Quater':[],'Insurance_type':[], 'Insurance_count':[], 'Insurance_amount':[]}
# for state in Agg_insure_list:
#     state2 = path2+state+"/"
#     Agg_yr = os.listdir(state2)
#     for year in Agg_yr:
#         year2 = state2+year+"/"
#         Agg_yr_list = os.listdir(year2)
#         for data in Agg_yr_list:
#             data2 = year2+data
#             Data = open(data2,'r')
#             E = json.load(Data)
#             for z in E['data']['transactionData']:
#               Name = z['name']
#               count = z['paymentInstruments'][0]['count']
#               amount = z['paymentInstruments'][0]['amount']
#               clm2['Insurance_type'].append(Name)
#               clm2['Insurance_count'].append(count)
#               clm2['Insurance_amount'].append(amount)
#               clm2['State'].append(state)
#               clm2['Year'].append(year)
#               clm2['Quater'].append(int(data.strip('.json')))
# #Succesfully created a dataframe
# Agg_insur = pd.DataFrame(clm2)
# Agg_insur["State"] = Agg_insur["State"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
# Agg_insur["State"] = Agg_insur["State"].str.replace("-"," ")
# Agg_insur["State"] = Agg_insur["State"].str.title()
# Agg_insur['State'] = Agg_insur['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")
# # print(Agg_insur)

# #agg user data
# path3  =  "F:/MDTM46B/Phonepe/data/aggregated/user/country/india/state/"
# Agg_user_list  =  os.listdir(path3)

# clm3 = {'State':[], 'Year':[],'Quater':[],'Brands':[], 'User_count':[], 'Percentage':[]}
# for state in Agg_user_list:
#     state3 = path3+state+"/"
#     Agg_yr = os.listdir(state3)
#     for year in Agg_yr:
#         year3 = state3+year+"/"
#         Agg_yr_list = os.listdir(year3)
#         for data in Agg_yr_list:
#             data3 = year3+data
#             Data = open(data3,'r')
#             F = json.load(Data)
#             if F.get('data') and F['data'].get('usersByDevice'):
#              for z in F['data']['usersByDevice']:
#               Brands = z['brand']
#               count = z['count']
#               percentage = z['percentage']
#               clm3['Brands'].append(Brands)
#               clm3['User_count'].append(count)
#               clm3['Percentage'].append(percentage)
#               clm3['State'].append(state)
#               clm3['Year'].append(year)
#               clm3['Quater'].append(int(data.strip('.json')))
# #Succesfully created a dataframe
# Agg_user = pd.DataFrame(clm3)
# Agg_user["State"] = Agg_user["State"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
# Agg_user["State"] = Agg_user["State"].str.replace("-"," ")
# Agg_user["State"] = Agg_user["State"].str.title()
# Agg_user['State'] = Agg_user['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")
# # print(Agg_user)

# #Map transaction data
# path4  =  "F:/MDTM46B/Phonepe/data/map/transaction/hover/country/india/state/"
# Map_list  =  os.listdir(path4)

# clm4 = {'State':[], 'Year':[],'Quater':[],'District':[], 'Transaction_count':[], 'Transaction_amount':[]}
# for state in Map_list:
#     state4 = path4+state+"/"
#     Map_yr = os.listdir(state4)
#     for year in Map_yr:
#         year4 = state4+year+"/"
#         Map_yr_list = os.listdir(year4)
#         for data in Map_yr_list:
#             data4 = year4+data
#             Data = open(data4,'r')
#             G = json.load(Data)
#             for z in G['data']['hoverDataList']:
#               Name = z['name']
#               count = z['metric'][0]['count']
#               amount = z['metric'][0]['amount']
#               clm4['District'].append(Name)
#               clm4['Transaction_count'].append(count)
#               clm4['Transaction_amount'].append(amount)
#               clm4['State'].append(state)
#               clm4['Year'].append(year)
#               clm4['Quater'].append(int(data.strip('.json')))
# #Succesfully created a dataframe
# Map_trans = pd.DataFrame(clm4)
# Map_trans["State"] = Map_trans["State"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
# Map_trans["State"] = Map_trans["State"].str.replace("-"," ")
# Map_trans["State"] = Map_trans["State"].str.title()
# Map_trans['State'] = Map_trans['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")
# print(Map_trans)

# #Map Insurance data
# path5 =  "F:/MDTM46B/Phonepe/data/map/insurance/hover/country/india/state/"
# Map_Insure_list  =  os.listdir(path5)

# clm5 = {'State':[], 'Year':[],'Quater':[],'District':[], 'Insurance_count':[], 'Insurance_amount':[]}
# for state in Map_Insure_list:
#     state5 = path5+state+"/"
   
#     Map_yr = os.listdir(state5)
#     for year in Map_yr:
#         year5 = state5+year+"/"
#         Map_yr_list = os.listdir(year5)
#         for data in Map_yr_list:
#             data5 = year5+data
#             Data = open(data5,'r')
#             H = json.load(Data)
#             for z in H['data']['hoverDataList']:
#               Name = z['name']
#               count = z['metric'][0]['count']
#               amount = z['metric'][0]['amount']
#               clm5['District'].append(Name)
#               clm5['Insurance_count'].append(count)
#               clm5['Insurance_amount'].append(amount)
#               clm5['State'].append(state)
#               clm5['Year'].append(year)
#               clm5['Quater'].append(int(data.strip('.json')))
# #Succesfully created a dataframe
# Map_insur = pd.DataFrame(clm5)
# Map_insur["State"] = Map_insur["State"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
# Map_insur["State"] = Map_insur["State"].str.replace("-"," ")
# Map_insur["State"] = Map_insur["State"].str.title()
# Map_insur['State'] = Map_insur['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")
# print(Map_insur)

# # Map User data
# path6 =  "F:/MDTM46B/Phonepe/data/map/user/hover/country/india/state/"
# Map_User_list  =  os.listdir(path6)

# clm6 = {'State':[], 'Year':[],'Quater':[],'District':[], 'RegisteredUsers':[], 'AppOpens':[]}
# for state in Map_User_list:
#     state6 = path6+state+"/"
   
#     Map_yr = os.listdir(state6)
#     for year in Map_yr:
#         year6 = state6+year+"/"
#         Map_yr_list = os.listdir(year6)
#         for data in Map_yr_list:
#             data6 = year6+data
#             Data = open(data6,'r')
#             I = json.load(Data)
#             for district, info in I['data']['hoverData'].items():
#               registeredUsers = info['registeredUsers']
#               appOpens = info['appOpens']
#               clm6['District'].append(district)
#               clm6['RegisteredUsers'].append(registeredUsers)
#               clm6['AppOpens'].append(appOpens)
#               clm6['State'].append(state)
#               clm6['Year'].append(year)
#               clm6['Quater'].append(int(data.strip('.json')))
# #Succesfully created a dataframe
# Map_users = pd.DataFrame(clm6)
# Map_users["State"] = Map_users["State"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
# Map_users["State"] = Map_users["State"].str.replace("-"," ")
# Map_users["State"] = Map_users["State"].str.title()
# Map_users['State'] = Map_users['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")
# print(Map_users)

# #Top transaction data
# path7  =  "F:/MDTM46B/Phonepe/data/top/transaction/country/india/state/"
# Top8_list  =  os.listdir(path7)

# clm7 = {'State':[], 'Year':[],'Quater':[], 'Entity_Level':[], 'Entity_Name': [], 'Transaction_count':[], 'Transaction_amount':[]}
# for state in Top8_list:
#     state7 = path7+state+"/"
#     Top_yr = os.listdir(state7)
#     for year in Top_yr:
#         year7 = state7+year+"/"
#         Top_yr_list = os.listdir(year7)
#         for data in Top_yr_list:
#             data7 = os.path.join(year7, data)
#             with open(data7, 'r') as f:
#              J = json.load(f)
#             for z in J['data']['districts']:
#               entityName = z['entityName']
#               count = z['metric']['count']
#               amount = z['metric']['amount']
#               clm7['Entity_Level'].append('district')
#               clm7['Entity_Name'].append(entityName)
#               clm7['Transaction_count'].append(count)
#               clm7['Transaction_amount'].append(amount)
#               clm7['State'].append(state)
#               clm7['Year'].append(year)
#               clm7['Quater'].append(int(data.strip('.json')))

#               for z in J['data']['pincodes']:
#                 clm7['State'].append(state)
#                 clm7['Year'].append(year)
#                 clm7['Quater'].append(int(data.strip('.json')))
#                 clm7['Entity_Level'].append('pincode')
#                 clm7['Entity_Name'].append(z['entityName'])
#                 clm7['Transaction_count'].append(z['metric']['count'])
#                 clm7['Transaction_amount'].append(z['metric']['amount'])
# #Succesfully created a dataframe
# Top_trans = pd.DataFrame(clm7)
# Top_trans["State"] = Top_trans["State"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
# Top_trans["State"] = Top_trans["State"].str.replace("-"," ")
# Top_trans["State"] = Top_trans["State"].str.title()
# Top_trans['State'] = Top_trans['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")
# print(Top_trans)

# #Top Insurance data
# path8  =  "F:/MDTM46B/Phonepe/data/top/insurance/country/india/state/"
# Top_insure_list = os.listdir(path8)

# clm8 = {'State':[], 'Year':[],'Quater':[], 'Entity_Level':[], 'Entity_Name':[], 'Insurance_count':[], 'Insurance_amount':[]}
# for state in Top_insure_list:
#     state8 = path8+state+"/"
#     Top_yr = os.listdir(state8)
#     for year in Top_yr:
#         year8 = state8+year+"/"
#         Top_yr_list = os.listdir(year8)
#         for data in Top_yr_list:
#             data8 = year8+data
#             Data = open(data8,'r')
#             K = json.load(Data)
#             for z in K['data']['districts']:
#               entityName = z['entityName']
#               count = z['metric']['count']
#               amount = z['metric']['amount']
#               clm8['Entity_Name'].append(entityName)
#               clm8['Entity_Level'].append('district')
#               clm8['Insurance_count'].append(count)
#               clm8['Insurance_amount'].append(amount)
#               clm8['State'].append(state)
#               clm8['Year'].append(year)
#               clm8['Quater'].append(int(data.strip('.json')))

#               for z in K['data']['pincodes']:
#                 clm8['State'].append(state)
#                 clm8['Year'].append(year)
#                 clm8['Quater'].append(int(data.strip('.json')))
#                 clm8['Entity_Level'].append('pincode')
#                 clm8['Entity_Name'].append(z['entityName'])
#                 clm8['Insurance_count'].append(z['metric']['count'])
#                 clm8['Insurance_amount'].append(z['metric']['amount'])
# #Succesfully created a dataframe
# Top_insur = pd.DataFrame(clm8)
# Top_insur["State"] =Top_insur["State"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
# Top_insur["State"] = Top_insur["State"].str.replace("-"," ")
# Top_insur["State"] = Top_insur["State"].str.title()
# Top_insur['State'] = Top_insur['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")
# print(Top_insur)

# # # Top user data
# path9 =  "F:/MDTM46B/Phonepe/data/top/user/country/india/state/"
# Top_user_list  =  os.listdir(path9)

# clm9 = {'State':[], 'Year':[],'Quater':[],'Entity_Level':[], 'Name':[], 'Registered_Users':[]}
# for state in Top_user_list:
#     state9= path9+state+"/"
#     Top_yr = os.listdir(state9)
#     for year in Top_yr:
#         year8 = state9+year+"/"
#         Top_yr_list = os.listdir(year8)
#         for data in Top_yr_list:
#             data9 = year8+data
#             Data = open(data9,'r')
#             L = json.load(Data)
#             for z in L['data']['districts']:
#               Name = z['name']
#               registeredUsers = ['registeredUsers']
#               clm9['Name'].append(Name)
#               clm9['Entity_Level'].append('district')
#               clm9['Registered_Users'].append(registeredUsers)
#               clm9['State'].append(state)
#               clm9['Year'].append(year)
#               clm9['Quater'].append(int(data.strip('.json')))

#             for z in L['data']['pincodes']:
#                Name = z['name']
#                registeredUsers = ['registeredUsers']
#                clm9['Name'].append(Name)
#                clm9['Entity_Level'].append('pincode')
#                clm9['Registered_Users'].append(registeredUsers)
#                clm9['State'].append(state)
#                clm9['Year'].append(year)
#                clm9['Quater'].append(int(data.strip('.json')))
# #Succesfully created a dataframe
# Top_users = pd.DataFrame(clm9)
# Top_users["State"] = Top_users["State"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
# Top_users["State"] = Top_users["State"].str.replace("-"," ")
# Top_users["State"] = Top_users["State"].str.title()
# Top_users['State'] = Top_users['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")
# print(Top_users)

# print('Agg_Trans=', Agg_Trans.columns)
# print('Agg_insur=',Agg_insur.columns)
# print('Agg_user=',Agg_user.columns)
# print('Map_trans=',Map_trans.columns)
# print('Map_insur=',Map_insur.columns)
# print('Map_users=',Map_users.columns)
# print('Top_trans=',Top_trans.columns)
# print('Top_insur=',Top_insur.columns)
# print('Top_users=',Top_users.columns)