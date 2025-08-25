# 📊 PhonePe Transaction Insights

## 📌 Project Overview
This project analyzes **PhonePe Pulse data** (transactions, users, and insurance).  
It extracts JSON data → stores in MySQL → analyzes with SQL & Python → visualizes with Streamlit.

## 🛠️ Tech Stack
- Python (Streamlit, Pandas, Plotly, Matplotlib)
- MySQL (via PyMySQL)
- GitHub for version control

## 📂 Project Structure
```
PhonePe-Transaction-Insights/
│── app.py
│── requirements.txt
│── README.md
│── sql/
│── docs/
```

## 🗄️ Database Schema
### Aggregated Tables
- aggregated_transaction(State, Year, Quater, Transaction_type, Transaction_count, Transaction_amount)
- aggregated_insurance(State, Year, Quater, Insurance_type, Insurance_count, Insurance_amount)
- aggregated_user(State, Year, Quater, Brands, User_count, Percentage)

### Map Tables
- map_transaction(State, Year, Quater, District, Transaction_count, Transaction_amount)
- map_insurance(State, Year, Quater, District, Insurance_count, Insurance_amount)
- map_user(State, Year, Quater, District, RegisteredUsers, AppOpens)

### Top Tables
- top_user(State, Year, Quater, Entity_Level, Name, Registered_Users)
- top_transaction(...)
- top_insurance(...)

## 📊 Dashboard Features
- Aggregated transactions by category
- Choropleth maps for states/districts
- Top states, districts, pincodes
- Insurance trends over time
- User adoption & brand shares

## 🎯 Results
- Built an end-to-end ETL + Analytics + Visualization pipeline
- Clear state/district level insights on PhonePe adoption
- Hands-on with **SQL + Python + Streamlit**

**Name**: <Your Aswathy B>  
**Contact**: <aswathybalky@gmail.com or www.linkedin.com/in/aswathy-balakrishnan-38761b145>
