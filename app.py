import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import pymysql
import plotly_express as px
import requests
import json
import plotly.io as pio
import matplotlib.pyplot as plt

# Connection Parameters
connection = pymysql.connect(
         host = 'localhost',
         user = 'root',
         password = '12345',
         database = 'phonepe')

#cursor creation
cursor = connection.cursor()
#agg transaction_df
cursor.execute("SELECT * FROM aggregated_transaction")
connection.commit()
table1 = cursor.fetchall()

Agg_transaction= pd.DataFrame(table1,columns=('State', 'Year', 'Quater', 'Transaction_type', 
                                             'Transaction_count','Transaction_amount'))
# print(Agg_transaction)

#agg insurance_df
cursor.execute("SELECT * FROM aggregated_insurance")
connection.commit()
table2 = cursor.fetchall()
Agg_insurance= pd.DataFrame(table2,columns=('State', 'Year', 'Quater', 'Insurance_type', 
                                             'Insurance_count','Insurance_amount'))
# print(Agg_insurance)

#agg user_df
cursor.execute("SELECT * FROM aggregated_user")
connection.commit()
table3 = cursor.fetchall()
Agg_user= pd.DataFrame(table3,columns=('State', 'Year', 'Quater', 'Brands', 
                                             'User_count','Percentage'))
# print(Agg_user)

#map transaction_df
cursor.execute("SELECT * FROM map_transaction")
connection.commit()
table4 = cursor.fetchall()
Map_transaction= pd.DataFrame(table4,columns=('State', 'Year', 'Quater', 'District', 
                                             'Transaction_count','Transaction_amount'))
# print(Map_transaction)

#map insurance_df
cursor.execute("SELECT * FROM map_insurance")
connection.commit()
table5 = cursor.fetchall()
Map_insurance= pd.DataFrame(table5,columns=('State', 'Year', 'Quater', 'District', 
                                             'Insurance_count','Insurance_amount'))
# print(Map_insurance)

#map user_df
cursor.execute("SELECT * FROM map_user")
connection.commit()
table6 = cursor.fetchall()
Map_user= pd.DataFrame(table6,columns=('State', 'Year', 'Quater', 'District', 
                                             'RegisteredUsers','AppOpens'))
# print(Map_user)

#top transaction_df
cursor.execute("SELECT * FROM top_transaction")
connection.commit()
table7 = cursor.fetchall()
Top_transaction= pd.DataFrame(table7,columns=('State', 'Year', 'Quater', 'Entity_Level', 'Entity_Name',
                                             'Transaction_count','Transaction_amount'))
# print(Top_transaction)

#top insurance_df
cursor.execute("SELECT * FROM top_insurance")
connection.commit()
table8 = cursor.fetchall()
Top_insurance= pd.DataFrame(table8,columns=('State', 'Year', 'Quater', 'Entity_Level', 'Entity_Name',
                                            'Insurance_count', 'Insurance_amount'))
# print(Top_insurance)

#top user_df
cursor.execute("SELECT * FROM top_user")
connection.commit()
table9 = cursor.fetchall()
Top_user= pd.DataFrame(table9,columns=('State', 'Year', 'Quater', 'Entity_Level', 'Name',
                                             'Registered_Users'))
# print(Top_user)

def local_css(css_text: str):
    st.markdown(f"<style>{css_text}</style>", unsafe_allow_html=True)

#Agg transaction

def Transaction_amount_count_Y(df, year, dynamic_key):
  atacy = df[df["Year"] == year]
  atacy.reset_index(drop= True, inplace= True)

  atacyg= atacy.groupby("State")[["Transaction_count","Transaction_amount"]].sum()
  atacyg.reset_index(inplace= True)

  col1, col2 = st.columns(2)
  with col1:

    fig_amount = px.bar(atacyg, x="State", y= "Transaction_amount", title= f"{year} TRANSACTION AMOUNT",
                        color_discrete_sequence= px.colors.sequential.ice_r, height= 650, width= 600)
    st.plotly_chart(fig_amount, key=f"{dynamic_key}_amount_bar")

  with col2:

    fig_count = px.bar(atacyg, x="State", y= "Transaction_count", title= f"{year} TRANSACTION COUNT",
                        color_discrete_sequence= px.colors.sequential.Bluered_r, height= 650, width= 600)
    st.plotly_chart(fig_count, key=f"{dynamic_key}_count_bar")

  col1, col2 = st.columns(2)
  with col1:

    url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    respo = requests.get(url)
    data1 =json.loads(respo.content)
    states_name = []
    for feature in data1["features"]:
        states_name.append(feature["properties"]["ST_NM"])

    states_name.sort()

    fig_india_1= px.choropleth(atacyg, geojson= data1, locations= "State", featureidkey=  "properties.ST_NM", 
                                color= "Transaction_amount", color_continuous_scale= "rainbow",
                                range_color= (atacyg["Transaction_amount"].min(),atacyg["Transaction_amount"].max()),
                                hover_name= "State", title= f"{year} TRANSACTION AMOUNT", fitbounds= "locations",
                                height= 600, width= 600)
    fig_india_1.update_geos(visible= False)
    st.plotly_chart(fig_india_1, key=f"{dynamic_key}_amount_map")
  with col2:
     
    fig_india_2= px.choropleth(atacyg, geojson= data1, locations= "State", featureidkey=  "properties.ST_NM", 
                                color= "Transaction_count", color_continuous_scale= "rainbow",
                                range_color= (atacyg["Transaction_count"].min(),atacyg["Transaction_count"].max()),
                                hover_name= "State", title= f"{year} TRANSACTION COUNT", fitbounds= "locations",
                                height= 600, width= 600)
    fig_india_2.update_geos(visible= False)
    st.plotly_chart(fig_india_2, key=f"{dynamic_key}_count_map")

    return atacy

def Transaction_amount_count_Y_Q(df, quater, dynamic_key):
  atacy = df[df["Quater"] == quater]
  atacy.reset_index(drop= True, inplace= True)
  atacyg= atacy.groupby("State")[["Transaction_count","Transaction_amount"]].sum()
  atacyg.reset_index(inplace= True)

  col1,col2= st.columns(2)
  with col1:

    fig_amount = px.bar(atacyg, x="State", y= "Transaction_amount", title= f"{atacy['Year'].min()} YEAR {quater} QUATER TRANSACTION AMOUNT",
                        color_discrete_sequence= px.colors.sequential.ice_r, height= 650, width= 600)
    st.plotly_chart(fig_amount, key=f"{dynamic_key}_amount_bar")
  with col2:
     
    fig_count = px.bar(atacyg, x="State", y= "Transaction_count", title= f"{atacy['Year'].min()} YEAR {quater} QUATER TRANSACTION COUNT",
                        color_discrete_sequence= px.colors.sequential.Bluered_r, height= 650, width= 600)
    st.plotly_chart(fig_count, key=f"{dynamic_key}_count_bar")
 
  col1,col2= st.columns(2)
  with col1:
     
    url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    respo = requests.get(url)
    data1 =json.loads(respo.content)
    states_name = []
    for feature in data1["features"]:
        states_name.append(feature["properties"]["ST_NM"])

    states_name.sort()

    fig_india_1= px.choropleth(atacyg, geojson= data1, locations= "State", featureidkey=  "properties.ST_NM", 
                                color= "Transaction_amount", color_continuous_scale= "rainbow",
                                range_color= (atacyg["Transaction_amount"].min(),atacyg["Transaction_amount"].max()),
                                hover_name= "State", title= f"{atacy['Year'].min()} YEAR {quater} QUATER TRANSACTION AMOUNT",
                                fitbounds= "locations", height= 600, width= 600)
    fig_india_1.update_geos(visible= False)
    st.plotly_chart(fig_india_1, key=f"{dynamic_key}_amount_map")

  with col2:
     
    fig_india_2= px.choropleth(atacyg, geojson= data1, locations= "State", featureidkey=  "properties.ST_NM", 
                                color= "Transaction_count", color_continuous_scale= "rainbow",
                                range_color= (atacyg["Transaction_count"].min(),atacyg["Transaction_count"].max()),
                                hover_name= "State", title= f"{atacy['Year'].min()} YEAR {quater} QUATER TRANSACTION COUNT", 
                                fitbounds= "locations", height= 600, width= 600)
    fig_india_2.update_geos(visible= False)
    st.plotly_chart(fig_india_2, key=f"{dynamic_key}_count_map")

  return atacy

def Aggre_Transaction_Type(df, state):

    atacy = df[df["State"] == state]
    atacy.reset_index(drop= True, inplace= True)

    atacyg= atacy.groupby("Transaction_type")[["Transaction_count","Transaction_amount"]].sum()
    atacyg.reset_index(inplace= True)

    col1,col2= st.columns(2)
    with col1:

      fig_pie_1= px.pie(data_frame= atacyg, names= "Transaction_type", values= "Transaction_amount", width= 600, 
                      title= f"{state.upper()} TRANSACTION AMOUNT", hole= 0.6)
      st.plotly_chart(fig_pie_1)

    with col2:
       
      fig_pie_2= px.pie(data_frame= atacyg, names= "Transaction_type", values= "Transaction_count", width= 600, 
                      title= f"{state.upper()} TRANSACTION COUNT", hole= 0.6)
      st.plotly_chart(fig_pie_2)

#Agg Insurance 

def Insurance_amount_count_Y(df, year, dynamic_key):
  
  aiacy = df[df["Year"] == year]
  aiacy.reset_index(drop= True, inplace= True)

  aiacyg= aiacy.groupby("State")[["Insurance_count","Insurance_amount"]].sum()
  aiacyg.reset_index(inplace= True)

  col1, col2 = st.columns(2)
  with col1:

    fig_amount = px.bar(aiacyg, x="State", y= "Insurance_amount", title= f"{year} INSURANCE AMOUNT",
                        color_discrete_sequence= px.colors.sequential.ice_r, height= 650, width= 600)
    st.plotly_chart(fig_amount, key=f"{dynamic_key}_ins_amount_bar")
    
  with col2:

    fig_count = px.bar(aiacyg, x="State", y= "Insurance_count", title= f"{year} INSURANCE COUNT",
                        color_discrete_sequence= px.colors.sequential.Bluered_r, height= 650, width= 600)
    st.plotly_chart(fig_count, key=f"{dynamic_key}_ins_count_bar")

  col1, col2 = st.columns(2)
  with col1:
       
    url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    respo = requests.get(url)
    data1 =json.loads(respo.content)
    states_name = []
    for feature in data1["features"]:
        states_name.append(feature["properties"]["ST_NM"])

    states_name.sort()

    fig_india_1= px.choropleth(aiacyg, geojson= data1, locations= "State", featureidkey=  "properties.ST_NM", 
                                color= "Insurance_amount", color_continuous_scale= "rainbow",
                                range_color= (aiacyg["Insurance_amount"].min(),aiacyg["Insurance_amount"].max()),
                                hover_name= "State", title= f"{year} INSURANCE AMOUNT", fitbounds= "locations",
                                height= 600, width= 600)
    fig_india_1.update_geos(visible= False)
    st.plotly_chart(fig_india_1, key=f"{dynamic_key}_ins_amount_map")
  with col2:

    fig_india_2= px.choropleth(aiacyg, geojson= data1, locations= "State", featureidkey=  "properties.ST_NM", 
                                color= "Insurance_count", color_continuous_scale= "rainbow",
                                range_color= (aiacyg["Insurance_count"].min(),aiacyg["Insurance_count"].max()),
                                hover_name= "State", title= f"{year} INSURANCE COUNT", fitbounds= "locations",
                                height= 600, width= 600)
    fig_india_2.update_geos(visible= False)
    st.plotly_chart(fig_india_2, key=f"{dynamic_key}_ins_count_map")
    
  return aiacy

def Insurance_amount_count_Y_Q(df, quater, dynamic_key):

    aiacy = df[df["Quater"] == quater]
    aiacy.reset_index(drop= True, inplace= True)

    aiacyg= aiacy.groupby("State")[["Insurance_count","Insurance_amount"]].sum()
    aiacyg.reset_index(inplace= True)

    col1,col2 = st.columns(2)
    with col1:

        fig_amount = px.bar(aiacyg, x="State", y= "Insurance_amount", title= f"{aiacy['Year'].min()} YEAR {quater} QUATER INSURANCE AMOUNT",
                            color_discrete_sequence= px.colors.sequential.ice_r, height= 650, width= 600)
        st.plotly_chart(fig_amount, key=f"{dynamic_key}_ins_amount_bar")

    with col2:

        fig_count = px.bar(aiacyg, x="State", y= "Insurance_count", title= f"{aiacy['Year'].min()} YEAR {quater} QUATER INSURANCE COUNT",
                            color_discrete_sequence= px.colors.sequential.Bluered_r, height= 650, width= 600)
        st.plotly_chart(fig_count, key=f"{dynamic_key}_ins_count_bar")

    col1,col2= st.columns(2)
    with col1:

        url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
        respo = requests.get(url)
        data1 =json.loads(respo.content)
        states_name = []
        for feature in data1["features"]:
            states_name.append(feature["properties"]["ST_NM"])

        states_name.sort()

        fig_india_1= px.choropleth(aiacyg, geojson= data1, locations= "State", featureidkey=  "properties.ST_NM", 
                                    color= "Insurance_amount", color_continuous_scale= "rainbow",
                                    range_color= (aiacyg["Insurance_amount"].min(),aiacyg["Insurance_amount"].max()),
                                    hover_name= "State", title= f"{aiacy['Year'].min()} YEAR {quater} QUATER INSURANCE AMOUNT",
                                    fitbounds= "locations", height= 600, width= 600)
        fig_india_1.update_geos(visible= False)
        st.plotly_chart(fig_india_1, key=f"{dynamic_key}_ins_amount_map")

    with col2:

        fig_india_2= px.choropleth(aiacyg, geojson= data1, locations= "State", featureidkey=  "properties.ST_NM", 
                                    color= "Insurance_count", color_continuous_scale= "rainbow",
                                    range_color= (aiacyg["Insurance_count"].min(),aiacyg["Insurance_count"].max()),
                                    hover_name= "State", title= f"{aiacy['Year'].min()} YEAR {quater} QUATER INSURANCE COUNT", 
                                    fitbounds= "locations", height= 600, width= 600)
        fig_india_2.update_geos(visible= False)
        st.plotly_chart(fig_india_2, key=f"{dynamic_key}_ins_count_map")

    return aiacy

#Aggregated User
def Aggre_user_plot_1(df, year):
    
    agusy = df[df["Year"] == year]
    agusy.reset_index(drop= True, inplace= True)

    agusyg = pd.DataFrame(agusy.groupby("Brands")["User_count"].sum())
    agusyg.reset_index(inplace= True)

    fig_bar_1 = px.bar(agusyg, x= "Brands", y= "User_count", title= "BRANDS AND USER COUNT",
                    width= 1000, color_discrete_sequence= px.colors.sequential.Magenta_r, hover_name="Brands")
    st.plotly_chart(fig_bar_1)

    return agusy 

#Aggregated_User_Analysis 2
def Aggre_user_plot_2(df, quater):
    agusyq = df[df["Quater"]== quater]
    agusyq.reset_index(drop= True, inplace= True)

    agusyqg= pd.DataFrame(agusyq.groupby("Brands")["User_count"].sum())
    agusyqg.reset_index(inplace= True)

    fig_bar_1 = px.bar(agusyqg, x= "Brands", y= "User_count", title= f"{quater} QUATER, BRANDS AND USER COUNT",
                        width= 1000, color_discrete_sequence= px.colors.sequential.Burg_r, hover_name= "Brands")
    st.plotly_chart(fig_bar_1)

    return agusyq

#Aggregated User Analysis 3
def Aggre_user_plot_3(df, state):
    agusyqs= df[df["State"] == state]
    agusyqs.reset_index(drop= True, inplace= True)

    fig_line_1= px.line(agusyqs, x= "Brands", y= "User_count", hover_data= ["Percentage"], 
                        title= f"{state.upper()} BRANDS, USER COUNT, PERCENTAGE",width= 1000, markers= True)
    st.plotly_chart(fig_line_1)

#Map transaction 
def Map_tra_dis(df, state):

    atacy = df[df["State"] == state]
    atacy.reset_index(drop= True, inplace= True)

    atacyg= atacy.groupby("District")[["Transaction_count","Transaction_amount"]].sum()
    atacyg.reset_index(inplace= True)

    col1,col2= st.columns(2)
    with col1:
      fig_bar_1= px.bar(atacyg, x= "Transaction_amount", y= "District", orientation= "h", height= 600,
                    title= f"{state.upper()} DISTRICT AND TRANSACTION_AMOUNT", color_discrete_sequence= px.colors.sequential.Brwnyl)
      st.plotly_chart(fig_bar_1)

    with col2:

      fig_bar_1= px.bar(atacyg, x= "Transaction_count", y= "District", orientation= "h", height= 600,
                    title= f"{state.upper()} DISTRICT AND TRANSACTION_COUNT", color_discrete_sequence= px.colors.sequential.Bluered_r)
      st.plotly_chart(fig_bar_1)

#Map insurance
def Map_ins_dis(df, state):
  aiacy = df[df["State"] == state]
  aiacy.reset_index(drop= True, inplace= True)

  aiacyg= aiacy.groupby("District")[["Insurance_count","Insurance_amount"]].sum()
  aiacyg.reset_index(inplace= True)

  col1,col2= st.columns(2)
  with col1:
     
     fig_bar_1= px.bar(aiacyg, x= "Insurance_amount", y= "District", orientation= "h", height= 600,
                      title= f"{state.upper()} DISTRICT AND INSURANCE_AMOUNT", color_discrete_sequence= px.colors.sequential.Brwnyl)
     st.plotly_chart(fig_bar_1)
  with col2:

    fig_bar_2= px.bar(aiacyg, x= "Insurance_count", y= "District", orientation= "h", height= 600,
                        title= f"{state.upper()} DISTRICT AND INSURANCE_COUNT", color_discrete_sequence= px.colors.sequential.Mint_r)
    st.plotly_chart(fig_bar_2)

#Map user plot 1
def Map_user_plot_1(df, year):
    mauy = df[df["Year"] == year]
    mauy.reset_index(drop= True, inplace= True)

    mauyg = mauy.groupby("State")[["RegisteredUsers", "AppOpens"]].sum()
    mauyg.reset_index(inplace= True)
           
    fig_line_2= px.line(mauyg, x= "State", y= ["RegisteredUsers", "AppOpens"],
                            title= f"{year} REGISTEREDUSER AND APPOPENS", width= 1000, height= 800, markers= True)
    st.plotly_chart(fig_line_2)

    return mauy

#Map user plot 2
def Map_user_plot_2(df, quater):
    mauyq = df[df["Quater"] == quater]
    mauyq.reset_index(drop= True, inplace= True)

    mauyqg = mauyq.groupby("State")[["RegisteredUsers", "AppOpens"]].sum()
    mauyqg.reset_index(inplace= True)
    
    fig_line_3= px.line(mauyqg, x= "State", y= ["RegisteredUsers", "AppOpens"],
                            title= f"{df['Year'].min()} YEAR {quater} QUATER REGISTEREDUSER AND APPOPENS", width= 1000, height= 800, markers= True,
                            color_discrete_sequence= px.colors.sequential.Burg_r)
    st.plotly_chart(fig_line_3)

    return mauyq

#Map user plot 3
def Map_user_plot_3(df, state):
    mauyqs = df[df["State"] == state]
    mauyqs.reset_index(drop= True, inplace= True)

    col1,col2= st.columns(2)
    with col1:

      fig_line_4= px.bar(mauyqs, x= "RegisteredUsers", y= "District", orientation= "h",
                              title= f"{state.upper()} REGISTEREDUSER", height= 800, color_discrete_sequence= px.colors.sequential.Bluered_r)
      st.plotly_chart(fig_line_4)

    with col2:

      fig_line_5= px.bar(mauyqs, x= "AppOpens", y= "District", orientation= "h",
                              title= f"{state.upper()} APPOPENS", height= 800, color_discrete_sequence= px.colors.sequential.Blues_r)
      st.plotly_chart(fig_line_5)

#Top Transaction year funtion
def Top_Transaction_amount_count_Y(df, year):
    
    Toty = df[df["Year"] == year]
    Toty.reset_index(drop=True, inplace=True)

    Totyg = Toty.groupby("State")[["Transaction_count", "Transaction_amount"]].sum().reset_index()
    Totyg.reset_index(inplace=True)

    col1,col2= st.columns(2)
    with col1:
   
      fig_bar_top1 = px.bar(Totyg, x="State", y="Transaction_amount",
                          title=f"{year} TRANSACTION AMOUNT",
                          color_discrete_sequence=px.colors.sequential.ice_r,
                          height=650, width=800)
      st.plotly_chart(fig_bar_top1)

    with col2:

      fig__bar_top2 = px.bar(Totyg, x="State", y="Transaction_count",
                        title=f"{year} TRANSACTION COUNT",
                        color_discrete_sequence=px.colors.sequential.Bluered_r,
                        height=650, width=800)
      st.plotly_chart(fig__bar_top2)

    url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    respo = requests.get(url)
    india_map = json.loads(respo.content)

    col1,col2= st.columns(2)
    with col1:

      fig_india_amount = px.choropleth(Totyg, geojson=india_map, locations="State",
                                      featureidkey="properties.ST_NM",
                                      color="Transaction_amount", color_continuous_scale="rainbow",
                                      range_color=(Totyg["Transaction_amount"].min(),
                                                    Totyg["Transaction_amount"].max()),
                                      hover_name="State",
                                      title=f"{year} TRANSACTION AMOUNT",
                                      fitbounds="locations",
                                      height=600, width=600)
      fig_india_amount.update_geos(visible=False)
      st.plotly_chart(fig_india_amount)

    with col2:

      fig_india_count = px.choropleth(Totyg, geojson=india_map, locations="State",
                                      featureidkey="properties.ST_NM",
                                      color="Transaction_count", color_continuous_scale="rainbow",
                                      range_color=(Totyg["Transaction_count"].min(),
                                                  Totyg["Transaction_count"].max()),
                                      hover_name="State",
                                      title=f"{year} TRANSACTION COUNT",
                                      fitbounds="locations",
                                      height=600, width=600)
      fig_india_count.update_geos(visible=False)
      st.plotly_chart(fig_india_count)
    
    df_district = Toty[Toty["Entity_Level"] == "district"]
    grouped_district = df_district.groupby(["State", "Entity_Name"])[["Transaction_count", "Transaction_amount"]].sum().reset_index()

    if not grouped_district.empty:
        fig_district_1 = px.bar(grouped_district, x="Entity_Name", y="Transaction_amount",
                            title=f"{year} TRANSACTION AMOUNT BY DISTRICT",
                            color="State",
                            height=650, width=1500)
        st.plotly_chart(fig_district_1)

        fig_district_2 = px.bar(grouped_district, x="Entity_Name", y="Transaction_count",
                           title=f"{year} TRANSACTION COUNT BY DISTRICT",
                           color="State",
                           height=650, width=1500)
        st.plotly_chart(fig_district_2)

   
    df_pincode = Toty[Toty["Entity_Level"] == "pincode"]
    grouped_pincode = df_pincode.groupby(["State", "Entity_Name"])[["Transaction_count", "Transaction_amount"]].sum().reset_index()

    if not grouped_pincode.empty:
        fig_pincode_1 = px.bar(grouped_pincode, x="Entity_Name", y="Transaction_amount",
                            title=f"{year} TRANSACTION AMOUNT BY PINCODE",
                            color="State",
                            height=650, width=1500)
        st.plotly_chart(fig_pincode_1)

        fig_pincode_2 = px.bar(grouped_pincode, x="Entity_Name", y="Transaction_count",
                           title=f"{year} TRANSACTION COUNT BY PINCODE",
                           color="State",
                           height=650, width=1500)
        st.plotly_chart(fig_pincode_2)
        
    return Toty


def Top_Transaction_amount_count_Q(df, quater):
    # Filter for given Quarter
    Totq = df[df["Quater"] == quater]
    Totq.reset_index(drop=True, inplace=True)

    grouped_state = Totq.groupby("State")[["Transaction_count", "Transaction_amount"]].sum().reset_index()
    grouped_state.reset_index(inplace=True)

    col1,col2= st.columns(2)
    with col1:
   
      fig_bar_top1 = px.bar(grouped_state, x="State", y="Transaction_amount",
                          title=f"{Totq['Year'].min()} YEAR {quater} QUATER TRANSACTION AMOUNT",
                          color_discrete_sequence=px.colors.sequential.ice_r,
                          height=650, width=800)
      st.plotly_chart(fig_bar_top1)

    with col2:

      fig_bar_top2 = px.bar(grouped_state, x="State", y="Transaction_count",
                        title=f"{Totq['Year'].min()} YEAR {quater} QUATER TRANSACTION COUNT",
                        color_discrete_sequence=px.colors.sequential.Bluered_r,
                        height=650, width=800)
      st.plotly_chart(fig_bar_top2)


    url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    respo = requests.get(url)
    india_map = json.loads(respo.content)

    col1,col2= st.columns(2)
    with col1:

      fig_india_amount = px.choropleth(grouped_state, geojson=india_map, locations="State",
                                      featureidkey="properties.ST_NM",
                                      color="Transaction_amount", color_continuous_scale="rainbow",
                                      range_color=(grouped_state["Transaction_amount"].min(),
                                                    grouped_state["Transaction_amount"].max()),
                                      hover_name="State",
                                      title=f"{Totq['Year'].min()} YEAR {quater} QUATER TRANSACTION AMOUNT",
                                      fitbounds="locations",
                                      height=600, width=600)
      fig_india_amount.update_geos(visible=False)
      st.plotly_chart(fig_india_amount)

    with col2:

      fig_india_count = px.choropleth(grouped_state, geojson=india_map, locations="State",
                                      featureidkey="properties.ST_NM",
                                      color="Transaction_count", color_continuous_scale="rainbow",
                                      range_color=(grouped_state["Transaction_count"].min(),
                                                  grouped_state["Transaction_count"].max()),
                                      hover_name="State",
                                      title=f"{Totq['Year'].min()} YEAR {quater} QUATER TRANSACTION COUNT",
                                      fitbounds="locations",
                                      height=600, width=600)
      fig_india_count.update_geos(visible=False)
      st.plotly_chart(fig_india_count)


    df_district = Totq[Totq["Entity_Level"] == "district"]
    grouped_district = df_district.groupby(["State", "Entity_Name"])[["Transaction_count", "Transaction_amount"]].sum().reset_index()

    if not grouped_district.empty:
        fig_district_1 = px.bar(grouped_district, x="Entity_Name", y="Transaction_amount",
                            title=f"Q{quater} TRANSACTION AMOUNT BY DISTRICT",
                            color="State",
                            height=650, width=1500)
        st.plotly_chart(fig_district_1)

        fig_district_2 = px.bar(grouped_district, x="Entity_Name", y="Transaction_count",
                           title=f"Q{quater} TRANSACTION COUNT BY DISTRICT",
                           color="State",
                           height=650, width=1500)
        st.plotly_chart(fig_district_2)

    df_pincode = Totq[Totq["Entity_Level"] == "pincode"]
    grouped_pincode = df_pincode.groupby(["State", "Entity_Name"])[["Transaction_count", "Transaction_amount"]].sum().reset_index()

    if not grouped_pincode.empty:
        fig_pincode_1 = px.bar(grouped_pincode, x="Entity_Name", y="Transaction_amount",
                            title=f"Q{quater} TRANSACTION AMOUNT BY PINCODE",
                            color="State",
                            height=650, width=1500)
        st.plotly_chart(fig_pincode_1)

        fig_pincode_2 = px.bar(grouped_pincode, x="Entity_Name", y="Transaction_count",
                           title=f"Q{quater} TRANSACTION COUNT BY PINCODE",
                           color="State",
                           height=650, width=1500)
        st.plotly_chart(fig_pincode_2)

    return Totq

#Top transaction type

def Top_Transaction_Type(df, state):
    
    Totqs = df[df["State"] == state]
    Totqs.reset_index(drop=True, inplace=True)

    
    df_district = Totqs[Totqs["Entity_Level"] == "district"]
    grouped_district = df_district.groupby("Entity_Name")[["Transaction_count", "Transaction_amount"]].sum().reset_index()

    if not grouped_district.empty:
        fig_district_amount = px.pie(data_frame=grouped_district, 
                                     names="Entity_Name", values="Transaction_amount", width=600,
                                     title=f"{state.upper()} DISTRICT TRANSACTION AMOUNT", hole=0.6)
        st.plotly_chart(fig_district_amount)


        fig_district_count = px.pie(data_frame=grouped_district, 
                                    names="Entity_Name", values="Transaction_count", width=600,
                                    title=f"{state.upper()} DISTRICT TRANSACTION COUNT", hole=0.6)
        st.plotly_chart(fig_district_count)

    
    df_pincode = Totqs[Totqs["Entity_Level"] == "pincode"]
    grouped_pincode = df_pincode.groupby("Entity_Name")[["Transaction_count", "Transaction_amount"]].sum().reset_index()

    if not grouped_pincode.empty:
        fig_pincode_amount = px.pie(data_frame=grouped_pincode, 
                                    names="Entity_Name", values="Transaction_amount", width=600,
                                    title=f"{state.upper()} PINCODE TRANSACTION AMOUNT", hole=0.6)
        st.plotly_chart(fig_pincode_amount)

        fig_pincode_count = px.pie(data_frame=grouped_pincode, 
                                   names="Entity_Name", values="Transaction_count", width=600,
                                   title=f"{state.upper()} PINCODE TRANSACTION COUNT", hole=0.6)
        st.plotly_chart(fig_pincode_count)

# Top Insurance year
def Top_Insurance_amount_count_Y(df, year):
        
    Toiy = df[df["Year"] == year]
    Toiy.reset_index(drop=True, inplace=True)
    
    Toiyg = Toiy.groupby("State")[["Insurance_count", "Insurance_amount"]].sum().reset_index()
    Toiyg.reset_index(inplace=True)

    col1, col2= st.columns(2)
    with col1:

      fig_bar_top1 = px.bar(Toiyg, x="State", y="Insurance_amount",
                            title=f"{year} INSURANCE AMOUNT",
                            color_discrete_sequence=px.colors.sequential.Peach,
                            height=650, width=800)
      st.plotly_chart(fig_bar_top1)
    with col2:

      fig_bar_top2 = px.bar(Toiyg, x="State", y="Insurance_count",
                            title=f"{year} INSURANCE COUNT",
                            color_discrete_sequence=px.colors.sequential.Pinkyl_r,
                            height=650, width=800)
      st.plotly_chart(fig_bar_top2)

    url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    respo = requests.get(url)
    india_map = json.loads(respo.content)

    col1, col2= st.columns(2)
    with col1:

      fig_india_amount = px.choropleth(Toiyg, geojson=india_map, locations="State",
                                      featureidkey="properties.ST_NM",
                                      color="Insurance_amount", color_continuous_scale="rainbow",
                                      range_color=(Toiyg["Insurance_amount"].min(),
                                                    Toiyg["Insurance_amount"].max()),
                                      hover_name="State",
                                      title=f"{year} INSURANCE AMOUNT",
                                      fitbounds="locations",
                                      height=600, width=600)
      fig_india_amount.update_geos(visible=False)
      st.plotly_chart(fig_india_amount)
    with col2:
       
      fig_india_count = px.choropleth(Toiyg, geojson=india_map, locations="State",
                                      featureidkey="properties.ST_NM",
                                      color="Insurance_count", color_continuous_scale="rainbow",
                                      range_color=(Toiyg["Insurance_count"].min(),
                                                  Toiyg["Insurance_count"].max()),
                                      hover_name="State",
                                      title=f"{year} INSURANCE COUNT",
                                      fitbounds="locations",
                                      height=600, width=600)
      fig_india_count.update_geos(visible=False)
      st.plotly_chart(fig_india_count)

    df_district = Toiy[Toiy["Entity_Level"] == "district"]
    grouped_district = df_district.groupby(["State", "Entity_Name"])[["Insurance_count", "Insurance_amount"]].sum().reset_index()
    
    if not grouped_district.empty:
        fig_district_1 = px.bar(grouped_district, x="Entity_Name", y="Insurance_amount",
                                title=f"{year} INSURANCE AMOUNT BY DISTRICT",
                                color="State",
                                height=650, width=1500)
        st.plotly_chart(fig_district_1)

        fig_district_2 = px.bar(grouped_district, x="Entity_Name", y="Insurance_count",
                                title=f"{year} INSURANCE COUNT BY DISTRICT",
                                color="State",
                                height=650, width=1500)
        st.plotly_chart(fig_district_2)

    df_pincode = Toiy[Toiy["Entity_Level"] == "pincode"]
    grouped_pincode = df_pincode.groupby(["State", "Entity_Name"])[["Insurance_count", "Insurance_amount"]].sum().reset_index()
    
   
    if not grouped_pincode.empty:
        fig_pincode_1 = px.bar(grouped_pincode, x="Entity_Name", y="Insurance_amount",
                              title=f"{year} INSURANCE AMOUNT BY PINCODE",
                              color="State",
                              height=650, width=1500)
        st.plotly_chart(fig_pincode_1)

        fig_pincode_2 = px.bar(grouped_pincode, x="Entity_Name", y="Insurance_count",
                              title=f"{year} INSURANCE COUNT BY PINCODE",
                              color="State",
                              height=650, width=1500)
        st.plotly_chart(fig_pincode_2)

    return Toiy

def Top_Insurance_amount_count_Q(df, quater):
  
    Toiy = df[df["Quater"] == quater]
    Toiy.reset_index(drop=True, inplace=True)

    grouped_state = Toiy.groupby("State")[["Insurance_count", "Insurance_amount"]].sum().reset_index()

    col1, col2= st.columns(2)
    with col1:

      fig_bar_top1 = px.bar(grouped_state, x="State", y="Insurance_amount",
                          title=f"{Toiy['Year'].min()} YEAR {quater} QUATER INSURANCE AMOUNT",
                          color_discrete_sequence=px.colors.sequential.RdPu_r,
                          height=650, width=800)
      st.plotly_chart(fig_bar_top1)
    with col2:
       
      fig_bar_top2 = px.bar(grouped_state, x="State", y="Insurance_count",
                        title=f"{Toiy['Year'].min()} YEAR {quater} QUATER INSURANCE COUNT",
                        color_discrete_sequence=px.colors.sequential.Tealgrn,
                        height=650, width=800)
      st.plotly_chart(fig_bar_top2)

    url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    respo = requests.get(url)
    india_map = json.loads(respo.content)

    col1, col2= st.columns(2)
    with col1:
       
      fig_india_amount = px.choropleth(grouped_state, geojson=india_map, locations="State",
                                      featureidkey="properties.ST_NM",
                                      color="Insurance_amount", color_continuous_scale="rainbow",
                                      range_color=(grouped_state["Insurance_amount"].min(),
                                                    grouped_state["Insurance_amount"].max()),
                                      hover_name="State",
                                      title=f"{Toiy['Year'].min()} YEAR {quater} QUATER INSURANCE AMOUNT",
                                      fitbounds="locations",
                                      height=600, width=600)
      fig_india_amount.update_geos(visible=False)
      st.plotly_chart(fig_india_amount)
    with col2:
       
      fig_india_count = px.choropleth(grouped_state, geojson=india_map, locations="State",
                                      featureidkey="properties.ST_NM",
                                      color="Insurance_count", color_continuous_scale="rainbow",
                                      range_color=(grouped_state["Insurance_count"].min(),
                                                  grouped_state["Insurance_count"].max()),
                                      hover_name="State",
                                      title=f"{Toiy['Year'].min()} YEAR {quater} QUATER INSURANCE COUNT",
                                      fitbounds="locations",
                                      height=600, width=600)
      fig_india_count.update_geos(visible=False)
      st.plotly_chart(fig_india_count)

    df_district = Toiy[Toiy["Entity_Level"] == "district"]
    grouped_district = df_district.groupby(["State", "Entity_Name"])[["Insurance_count", "Insurance_amount"]].sum().reset_index()

       
    if not grouped_district.empty:
        fig_district_1 = px.bar(grouped_district, x="Entity_Name", y="Insurance_amount",
                            title=f"Q{quater} INSURANCE AMOUNT BY DISTRICT",
                            color="State",
                            height=650, width=1500)
        st.plotly_chart(fig_district_1)

        fig_district_2 = px.bar(grouped_district, x="Entity_Name", y="Insurance_count",
                          title=f"Q{quater} INSURANCE COUNT BY DISTRICT",
                          color="State",
                          height=650, width=1500)
        st.plotly_chart(fig_district_2)

    df_pincode = Toiy[Toiy["Entity_Level"] == "pincode"]
    grouped_pincode = df_pincode.groupby(["State", "Entity_Name"])[["Insurance_count", "Insurance_amount"]].sum().reset_index()
     
    if not grouped_pincode.empty:
        fig_pincode_1 = px.bar(grouped_pincode, x="Entity_Name", y="Insurance_amount",
                            title=f"Q{quater} INSURANCE AMOUNT BY PINCODE",
                            color="State",
                            height=650, width=1500)
        st.plotly_chart(fig_pincode_1)

        fig_pincode_2 = px.bar(grouped_pincode, x="Entity_Name", y="Insurance_count",
                          title=f"Q{quater} INSURANCE COUNT BY PINCODE",
                          color="State",
                          height=650, width=1500)
        st.plotly_chart(fig_pincode_2)

    return Toiy

def Top_insurance_dis(df, state, level="district"):
    
    Toiyd = df[(df["State"] == state) & (df["Entity_Level"] == level)]
    Toiyd.reset_index(drop=True, inplace=True)
       
    Toiydg = Toiyd.groupby("Entity_Name")[["Insurance_count", "Insurance_amount"]].sum()
    Toiydg.reset_index(inplace=True)

    col1, col2= st.columns(2)
    with col1:

      fig_bar_1 = px.bar(
          Toiydg, x="Insurance_amount", y="Entity_Name", orientation="h", height=600,
          title=f"{state.upper()} {level.upper()} - INSURANCE AMOUNT",
          color_discrete_sequence=px.colors.sequential.RdPu_r
      )
      st.plotly_chart(fig_bar_1)
    with col2:
       
      fig_bar_2 = px.bar(
          Toiydg, x="Insurance_count", y="Entity_Name", orientation="h", height=600,
          title=f"{state.upper()} {level.upper()} - INSURANCE COUNT",
          color_discrete_sequence=px.colors.sequential.Sunsetdark_r
      )
      st.plotly_chart(fig_bar_2)

# Top user plot 1
def Top_user_plot_1(df, year):
   
    df["Registered_Users"] = pd.to_numeric(df["Registered_Users"], errors="coerce").fillna(0)

    tuy = df[df["Year"] == year].reset_index(drop=True)

    tuyg = tuy.groupby(["State", "Quater"])["Registered_Users"].sum().reset_index()

    fig = px.bar(tuyg, x="State", y="Registered_Users", color="Quater", barmode="group", width=1000, height=800,
                 hover_name="State", title=f"{year} REGISTERED USERS")
    st.plotly_chart(fig, use_container_width=True)

    return tuyg

#Top user plot 2
def Top_user_plot_2(df, state):
    # Normalize strings for consistent matching
    tuys = df[df["State"].str.strip().str.lower() == state.strip().lower()].reset_index(drop=True)
    
    level = st.radio("Select Level", ["District", "Pincode"])

    if level == "District":
        tuys = tuys[tuys["Entity_Level"].str.lower() == "district"].rename(columns={"Name": "District"})
        hover_column = "District"
       
    else:
        tuys = tuys[tuys["Entity_Level"].str.lower() == "pincode"].rename(columns={"Name": "Pincode"})
        hover_column = "Pincode"
        

    if tuys.empty:
        st.warning(f"No data available for {level} level in {state}.")
    else:
        fig = px.bar(tuys, x="Quater", y="Registered_Users", color="Registered_Users", hover_data=["Entity_Level", hover_column],
            title="REGISTERED USERS, PINCODE, DISTRICTS", width=1000, height=800,
            color_continuous_scale=px.colors.sequential.algae_r)
        st.plotly_chart(fig, use_container_width=True)


def ques1():
    brand= Agg_user[["Brands","User_count"]]
    brand1= brand.groupby("Brands")["User_count"].sum().sort_values(ascending=False)
    brand2= pd.DataFrame(brand1).reset_index()

    fig_brands= px.pie(brand2, values= "User_count", names= "Brands", color_discrete_sequence=px.colors.sequential.dense_r,
                       title= "Top Mobile Brands of User_count")
    return st.plotly_chart(fig_brands)

def ques2():
    lt= Agg_transaction[["State", "Transaction_amount"]]
    lt1= lt.groupby("State")["Transaction_amount"].sum().sort_values(ascending= True)
    lt2= pd.DataFrame(lt1).reset_index().head(10)

    fig_lts= px.bar(lt2, x= "State", y= "Transaction_amount",title= "LOWEST TRANSACTION AMOUNT and STATES",
                    color_discrete_sequence= px.colors.sequential.Oranges_r)
    return st.plotly_chart(fig_lts)

def ques3():
    htd= Map_transaction[["District", "Transaction_amount"]]
    htd1= htd.groupby("District")["Transaction_amount"].sum().sort_values(ascending=False)
    htd2= pd.DataFrame(htd1).head(10).reset_index()

    fig_htd= px.pie(htd2, values= "Transaction_amount", names= "District", title="TOP 10 DISTRICTS OF HIGHEST TRANSACTION AMOUNT",
                    color_discrete_sequence=px.colors.sequential.Emrld_r)
    return st.plotly_chart(fig_htd)

def ques4():
    htd= Map_transaction[["District", "Transaction_amount"]]
    htd1= htd.groupby("District")["Transaction_amount"].sum().sort_values(ascending=True)
    htd2= pd.DataFrame(htd1).head(10).reset_index()

    fig_htd= px.pie(htd2, values= "Transaction_amount", names= "District", title="TOP 10 DISTRICTS OF LOWEST TRANSACTION AMOUNT",
                    color_discrete_sequence=px.colors.sequential.Greens_r)
    return st.plotly_chart(fig_htd)


def ques5():
    sa= Map_user[["State", "AppOpens"]]
    sa1= sa.groupby("State")["AppOpens"].sum().sort_values(ascending=False)
    sa2= pd.DataFrame(sa1).reset_index().head(10)

    fig_sa= px.bar(sa2, x= "State", y= "AppOpens", title="Top 10 States With AppOpens",
                color_discrete_sequence= px.colors.sequential.deep_r)
    return st.plotly_chart(fig_sa)

def ques6():
    sa= Map_user[["State", "AppOpens"]]
    sa1= sa.groupby("State")["AppOpens"].sum().sort_values(ascending=True)
    sa2= pd.DataFrame(sa1).reset_index().head(10)

    fig_sa= px.bar(sa2, x= "State", y= "AppOpens", title="lowest 10 States With AppOpens",
                color_discrete_sequence= px.colors.sequential.dense_r)
    return st.plotly_chart(fig_sa)

def ques7():
    stc= Agg_transaction[["State", "Transaction_count"]]
    stc1= stc.groupby("State")["Transaction_count"].sum().sort_values(ascending=True)
    stc2= pd.DataFrame(stc1).reset_index()

    fig_stc= px.bar(stc2, x= "State", y= "Transaction_count", title= "STATES WITH LOWEST TRANSACTION COUNT",
                    color_discrete_sequence= px.colors.sequential.Jet_r)
    return st.plotly_chart(fig_stc)

def ques8():
    stc= Agg_transaction[["State", "Transaction_count"]]
    stc1= stc.groupby("State")["Transaction_count"].sum().sort_values(ascending=False)
    stc2= pd.DataFrame(stc1).reset_index()

    fig_stc= px.bar(stc2, x= "State", y= "Transaction_count", title= "STATES WITH HIGHEST TRANSACTION COUNT",
                    color_discrete_sequence= px.colors.sequential.Magenta_r)
    return st.plotly_chart(fig_stc)

def ques9():
    ht= Agg_transaction[["State", "Transaction_amount"]]
    ht1= ht.groupby("State")["Transaction_amount"].sum().sort_values(ascending= False)
    ht2= pd.DataFrame(ht1).reset_index().head(10)

    fig_lts= px.bar(ht2, x= "State", y= "Transaction_amount",title= "HIGHEST TRANSACTION AMOUNT and STATES",
                    color_discrete_sequence= px.colors.sequential.Oranges_r)
    return st.plotly_chart(fig_lts)

def ques10():
    dt= Map_transaction[["District", "Transaction_amount"]]
    dt1= dt.groupby("District")["Transaction_amount"].sum().sort_values(ascending=True)
    dt2= pd.DataFrame(dt1).reset_index().head(50)

    fig_dt= px.bar(dt2, x= "District", y= "Transaction_amount", title= "DISTRICTS WITH LOWEST TRANSACTION AMOUNT",
                color_discrete_sequence= px.colors.sequential.Mint_r)
    return st.plotly_chart(fig_dt)

  

# streamlit part

st.set_page_config(layout= "wide")
st.title("PHONEPE DATA VISUALIZATION AND EXPLORATION")

with st.sidebar:

    select= option_menu("Main Menu",["HOME", "DATA EXPLORATION", "TOP CHARTS"])

if select == "HOME":
    st.header("📊 Transactions & Users Overview")

    # --- Toggle buttons ---
    col1, col2 = st.columns(2)
    with col1:
        view_type = st.radio("📌 Select View:", ["Transactions", "Users"], horizontal=True)
    with col2:
        year = st.selectbox("📅 Select Year", sorted(Agg_transaction["Year"].unique()), index=0)
        quarter = st.selectbox("🗓️ Select Quarter", ["All"] + sorted(Agg_transaction["Quater"].unique()), index=0)
        quarter = None if quarter == "All" else quarter

    st.markdown("---")

    # --- KPIs ---
    if view_type == "Transactions":
        df = Agg_transaction.copy()
        if year: df = df[df["Year"] == year]
        if quarter: df = df[df["Quater"] == quarter]

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Transactions", f"{df['Transaction_count'].sum():,}")
        col2.metric("Total Payment Value (₹)", f"{df['Transaction_amount'].sum()/1e7:,.2f} Cr")
        avg_value = df['Transaction_amount'].sum() / df['Transaction_count'].sum()
        col3.metric("Avg. Transaction Value (₹)", f"{avg_value:,.0f}")

    else:  # Users
        df = Map_user.copy()
        if year: df = df[df["Year"] == year]
        if quarter: df = df[df["Quater"] == quarter]

        col1, col2 = st.columns(2)
        col1.metric("Total Registered Users", f"{df["RegisteredUsers"].sum():,}")
        col2.metric("App Opens", f"{df["AppOpens"].sum():,}")

    st.markdown("---")

    # --- Categories (for Transactions only) ---
    if view_type == "Transactions":
        st.subheader("📂 Categories")
        cat_df = df.groupby("Transaction_type").agg({"Transaction_count": "sum"}).reset_index()
        st.dataframe(cat_df, use_container_width=True)
        st.markdown("---")

    # --- Top 10 States ---
    if view_type == "Transactions":
        top_states = df.groupby("State").agg({"Transaction_amount":"sum"}).reset_index().sort_values("Transaction_amount", ascending=False).head(10)
        color_column = "Transaction_amount"
    else:
        top_states = df.groupby("State").agg({"RegisteredUsers":"sum"}).reset_index().sort_values("RegisteredUsers", ascending=False).head(10)
        color_column = "RegisteredUsers"

    st.subheader(f"🏆 Top 10 States by {view_type}")
    selected_state = st.selectbox("🔍 Explore a State", ["All India"] + top_states["State"].tolist())
    st.table(top_states)

    # --- Bar Chart for Top 10 ---
    st.bar_chart(top_states.set_index("State")[color_column])

    st.markdown("---")

    # --- India Map ---
    st.subheader(f"🗺️ All-India {view_type} Map")

    if view_type == "Transactions":
        state_df = df.groupby("State").agg({"Transaction_amount": "sum"}).reset_index()
        color_column = "Transaction_amount"
    else:
        state_df = df.groupby("State").agg({"RegisteredUsers": "sum"}).reset_index()
        color_column = "RegisteredUsers"

    # 🌐 Load India GeoJSON
    geojson_url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response = requests.get(geojson_url)
    india_geojson = response.json()

    # 🗺️ Create Choropleth Map
    fig_map = px.choropleth(
        state_df,
        geojson=india_geojson,
        featureidkey="properties.ST_NM",
        locations="State",
        color=color_column,
        color_continuous_scale="Viridis",
        title=f"Total {view_type} Across India"
    )

    # 🔎 Zoom if state is selected
    if selected_state != "All India":
        fig_map.update_geos(fitbounds="locations", visible=True,
                            center={"lat": 22.9734, "lon": 78.6569}, projection_scale=5)
        fig_map.update_layout(title_text=f"{view_type} in {selected_state}")

    fig_map.update_geos(fitbounds="locations", visible=False)

    # 📍 Display map
    st.plotly_chart(fig_map, use_container_width=True)



elif select =="DATA EXPLORATION":

    tab1, tab2, tab3 = st.tabs(["Aggregated Analysis", "Map Analysis", "Top Analysis"])

    with tab1:

        method = st.radio("Select The Method",["Transaction Analysis", "Insurance Analysis", "User Analysis"])

        if method == "Transaction Analysis":
            col1, col2= st.columns(2)
            with col1:

              year= st.slider("Select The Year", Agg_transaction["Year"].min(), Agg_transaction["Year"].max(), Agg_transaction["Year"].min())

            tacy= Transaction_amount_count_Y(Agg_transaction, year, f'fig_1_{year}')

            col1,col2= st.columns(2)

            with col1:
               state = st.selectbox("Select The State", tacy["State"].unique())

            Aggre_Transaction_Type(tacy, state)

            col1,col2 = st.columns(2)
            with col1:

              quater= st.slider("Select The Quater", tacy["Quater"].min(), tacy["Quater"].max(), tacy["Quater"].min())

            Aggre_Transaction_Type_Q = Transaction_amount_count_Y_Q(tacy, quater, f"agg_tran_q_{quater}")

            col1,col2= st.columns(2)
            with col1:
               state = st.selectbox("Select The State_Ty", Aggre_Transaction_Type_Q["State"].unique())

            Aggre_Transaction_Type(Aggre_Transaction_Type_Q, state)


        elif method == "Insurance Analysis":
            
            col1, col2= st.columns(2)
            with col1:

              year= st.slider("Select The Year Iy", Agg_insurance["Year"].min(), Agg_insurance["Year"].max(), Agg_insurance["Year"].min())

            iacy= Insurance_amount_count_Y(Agg_insurance, year, f'fig_2_{year}')

            col1,col2 = st.columns(2)
            with col1:

              quater= st.slider("Select The Quater Iq", iacy["Quater"].min(), iacy["Quater"].max(), iacy["Quater"].min())

            Insurance_amount_count_Y_Q(iacy, quater, f'fig_2_{year}_{quater}')

        elif method == "User Analysis":
            col1, col2= st.columns(2)
            with col1:

              year= st.slider("Select The Year Uy", Agg_user["Year"].min(), Agg_user["Year"].max(), Agg_user["Year"].min())

            Aggre_user_Y= Aggre_user_plot_1(Agg_user, year)

            col1,col2 = st.columns(2)
            with col1:

              quater= st.slider("Select The Quater Uq", Aggre_user_Y["Quater"].min(), Aggre_user_Y["Quater"].max(), Aggre_user_Y["Quater"].min())

            Aggre_user_Y_Q = Aggre_user_plot_2(Aggre_user_Y, quater)

            state = st.selectbox("Select The State_Usy", Aggre_user_Y_Q["State"].unique())

            Aggre_user_plot_3(Aggre_user_Y_Q, state)


    with tab2:

        method_2 = st.radio("Select The Method",["Map Transaction", "Map Insurance", "Map User"])

        if method_2 == "Map Transaction":
                       
          year= st.slider("Select The Year_My", Map_transaction["Year"].min(), Map_transaction["Year"].max(), Map_transaction["Year"].min())

          Map_tra_Y= Transaction_amount_count_Y(Map_transaction, year, f'fig_3_{year}')
          
              
          state = st.selectbox("Select The State_Ms", Map_tra_Y["State"].unique())

          Map_tra_dis(Map_tra_Y, state)

          quater= st.slider("Select The Quater_Mq", Map_tra_Y["Quater"].min(), Map_tra_Y["Quater"].max(), Map_tra_Y["Quater"].min())

          Map_tra_Y_Q = Transaction_amount_count_Y_Q(Map_tra_Y, quater, f"map_tran_q_{quater}")

          state = st.selectbox("Select The State_Msy", Map_tra_Y_Q["State"].unique())
      
          Map_tra_dis(Map_tra_Y_Q, state)
            

        elif method_2 == "Map Insurance":
            
            year= st.slider("Select The Year_Miy", Map_insurance["Year"].min(), Map_insurance["Year"].max(), Map_insurance["Year"].min()) 

            Map_ins_tac_Y= Insurance_amount_count_Y(Map_insurance, year, f'fig_4_{year}')
            
            col1,col2= st.columns(2)
            with col1:
               state = st.selectbox("Select The State_Mis", Map_ins_tac_Y["State"].unique())

            Map_ins_dis(Map_ins_tac_Y, state)

            col1,col2 = st.columns(2)
            with col1:

              quater= st.slider("Select The Quater Mq", Map_ins_tac_Y["Quater"].min(), Map_ins_tac_Y["Quater"].max(), Map_ins_tac_Y["Quater"].min())

            Map_ins_tac_Y_Q= Insurance_amount_count_Y_Q(Map_ins_tac_Y, quater, f"map_ins_q_{quater}")

            col1,col2= st.columns(2)
            with col1:
               state = st.selectbox("Select The State_Mps", Map_ins_tac_Y_Q["State"].unique())

            Map_ins_dis(Map_ins_tac_Y_Q, state)

        elif method_2 == "Map User":
            col1, col2= st.columns(2)
            with col1:

              year= st.slider("Select The Year_Muy", Map_user["Year"].min(), Map_user["Year"].max(), Map_user["Year"].min())

            Map_user_Y= Map_user_plot_1(Map_user, year)

            col1, col2= st.columns(2)
            with col1:
               
              quater= st.slider("Select The Quater_Muq", Map_user_Y["Quater"].min(), Map_user_Y["Quater"].max(), Map_user_Y["Quater"].min())

            Map_user_Y_Q = Map_user_plot_2(Map_user_Y, quater)

            col1, col2= st.columns(2)
            with col1:
               
              state = st.selectbox("Select The State_Mus", Map_user_Y_Q["State"].unique())

            Map_user_plot_3(Map_user_Y_Q, state)


    with tab3:

        method_3 = st.radio("Select The Method",["Top Transaction", "Top Insurance", "Top User"])

        if method_3 == "Top Transaction":
            col1, col2= st.columns(2)
            with col1:

              year= st.slider("Select The Year_Topy", Top_transaction["Year"].min(), Top_transaction["Year"].max(), Top_transaction["Year"].min())

            Top_tra_Y= Top_Transaction_amount_count_Y(Top_transaction, year)

            col1,col2= st.columns(2)

            with col1:
               state = st.selectbox("Select The State_Tops", Top_tra_Y["State"].unique())

            Top_Transaction_Type(Top_tra_Y, state)

            col1,col2 = st.columns(2)
            with col1:

              quater= st.slider("Select The Quater_Tpq", Top_tra_Y["Quater"].min(), Top_tra_Y["Quater"].max(), Top_tra_Y["Quater"].min())

            Top_tra_Y_Q = Top_Transaction_amount_count_Q(Top_tra_Y, quater)

            col1,col2= st.columns(2)
            with col1:
               state = st.selectbox("Select The State_Ty", Top_tra_Y_Q["State"].unique(), key="state_ty_select")

            Top_Transaction_Type(Top_tra_Y_Q, state)

        elif method_3 == "Top Insurance":
            col1,col2 = st.columns(2) 
            with col1:
               
             year= st.slider("Select The Year_Toi", Top_insurance["Year"].min(), Top_insurance["Year"].max(), Top_insurance["Year"].min()) 

            Top_Ins_Y= Top_Insurance_amount_count_Y(Top_insurance, year)
            
            col1,col2= st.columns(2)
            with col1:
               state = st.selectbox("Select The State_Tos", Top_Ins_Y["State"].unique())

            Top_insurance_dis(Top_Ins_Y, state)

            col1,col2 = st.columns(2)
            with col1:

              quater= st.slider("Select The Quater Toq", Top_Ins_Y["Quater"].min(), Top_Ins_Y["Quater"].max(), Top_Ins_Y["Quater"].min())

            Top_ins_Y_Q= Top_Insurance_amount_count_Q(Top_Ins_Y, quater)

            col1,col2= st.columns(2)
            with col1:
               state = st.selectbox("Select The State_Tos", Top_ins_Y_Q["State"].unique())

            Top_insurance_dis(Top_ins_Y_Q, state)

        elif method_3 == "Top User":
            col1, col2= st.columns(2)
            with col1:

              year= st.slider("Select The Year_Tuy", Top_user["Year"].min(), Top_user["Year"].max(), Top_user["Year"].min())
            Top_user_Y= Top_user_plot_1(Top_user, year)

            col1,col2= st.columns(2)
            with col1:
               state = st.selectbox("Select The State_Tus", Top_user["State"].unique())
            Top_user_plot_2(Top_user, state)

elif select =="TOP CHARTS":       
    ques= st.selectbox("**Select the Question**",('Top Brands Of Mobiles Used','States With Lowest Trasaction Amount',
                                  'Districts With Highest Transaction Amount','Top 10 Districts With Lowest Transaction Amount',
                                  'Top 10 States With AppOpens','Least 10 States With AppOpens','States With Lowest Trasaction Count',
                                 'States With Highest Trasaction Count','States With Highest Trasaction Amount',
                                 'Top 50 Districts With Lowest Transaction Amount'))
    
    if ques=="Top Brands Of Mobiles Used":
        ques1()

    elif ques=="States With Lowest Trasaction Amount":
        ques2()

    elif ques=="Districts With Highest Transaction Amount":
        ques3()

    elif ques=="Top 10 Districts With Lowest Transaction Amount":
        ques4()

    elif ques=="Top 10 States With AppOpens":
        ques5()

    elif ques=="Least 10 States With AppOpens":
        ques6()

    elif ques=="States With Lowest Trasaction Count":
        ques7()

    elif ques=="States With Highest Trasaction Count":
        ques8()

    elif ques=="States With Highest Trasaction Amount":
        ques9()

    elif ques=="Top 50 Districts With Lowest Transaction Amount":
        ques10()
