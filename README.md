# 📊 PhonePe Transaction Insights

## 📌 Project Overview
This project analyzes **digital payment trends in India** using PhonePe Pulse–style data.  
It extracts transactions, users, and insurance data from JSON sources (or SQL dumps), loads them into a **SQL database**, and provides **interactive insights** through a **Streamlit** dashboard.

## 🎯 Objectives
- Analyze and visualize aggregated payment categories
- Create geo insights at **state/district/pincode** levels
- Identify **top-performing** regions and categories
- Generate **business-ready insights** (marketing, fraud, growth)

## 🛠️ Tech Stack
- **Python**: Streamlit, Pandas, Plotly, Matplotlib, NumPy
- **Database**: MySQL (via PyMySQL/SQLAlchemy)
- **Viz**: Plotly/Matplotlib in Streamlit
- **Version Control**: Git & GitHub

## 📂 Project Structure
```
PhonePe-Transaction-Insights/
│── app.py                  # Streamlit dashboard
│── requirements.txt        # Dependencies to run the app
│── sql/                    # (Optional) schema & useful queries
│── docs/                   # PPT & docs (optional)
│── README.md               # You're reading this
│── .gitignore              # Ignore large/secret files
│── data/                   # (Optional) raw JSON (excluded from git by default)
```

## 🗄️ Database Design (suggested)
**Aggregated tables**: transactions, users, insurance  
**Map tables**: map_transactions, map_users, map_insurance (state/district totals)  
**Top tables**: top_transactions, top_users, top_insurance (states/districts/pincodes)

> Adjust the above to match your exact table names.

## ⚙️ Local Setup
1. **Clone** the repo
   ```bash
   git clone https://github.com/<your-username>/PhonePe-Transaction-Insights.git
   cd PhonePe-Transaction-Insights
   ```

2. **Install** dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure DB** in `app.py`
   ```python
   # Example only – replace with your credentials
   conn = pymysql.connect(
       host="localhost",
       user="root",
       password="your_password",
       database="phonepe"
   )
   ```

4. **Run** Streamlit
   ```bash
   streamlit run app.py
   ```

## 📊 Dashboard Highlights
- State-wise choropleth and bars for **transaction amount/count**
- **Top states/districts/pincodes**
- **User adoption** trends and **brand shares**
- **Insurance** trends and penetration

## 🧠 Business Use Cases
Customer segmentation • Fraud signals • Regional targeting • Category performance • Marketing optimization • Insurance growth

## 🚀 Results
- End-to-end ETL → SQL → Analytics → **Interactive dashboard**
- Clear visibility into **geography, time, and category** patterns
- Ready **insights** for stakeholders and product teams

## 📜 License
MIT (or choose your own)

---

**Name**: <Aswathy>  
**Contact**: <www.linkedin.com/in/aswathy-balakrishnan-38761b145>
