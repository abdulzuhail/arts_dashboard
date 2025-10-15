# 🎨 **Arts Organizations in Canada Dashboard**

An interactive **data visualization dashboard** built using **Streamlit**, **MongoDB**, and **Plotly** to analyze and display insights about **arts organizations across Canada**.  
This project fetches **real-time data from Wikidata**, stores it in **MongoDB**, and provides visual insights into **distribution, art forms, and JSON-LD structured data adoption** among organizations.

---

## 🎥 **Project Demo**

🎬 **Watch the Dashboard in Action:**  
👉 [Click to view on GitHub](https://github.com/abdulzuhail/arts_dashboard/blob/main/streamlit-dashboard.mp4)

🎞️ **Preview Below:**  
https://github.com/abdulzuhail/arts_dashboard/blob/main/streamlit-dashboard.mp4

---

## 🚀 **KEY FEATURES**

### ✅ **1. Data Fetching from Wikidata**
- Retrieves organization data (name, type, province, website, founded year).
- Automatically stores or updates data in **MongoDB**.

### ✅ **2. Streamlit Dashboard Interface**
- Search and filter organizations by **name**, **location**, or **type**.
- Download filtered results as **CSV**.
- Interactive charts powered by **Plotly**.

### ✅ **3. Visual Analytics**
- 📊 **Bar Chart** — Distribution of organizations by province.  
- 📈 **Line Chart** — Yearly growth of new organizations.  
- 🥧 **Pie Chart** — JSON-LD adoption (Yes vs No).

### ✅ **4. JSON-LD Website Analysis**
- Scans organization websites for **JSON-LD structured data**.
- Displays **adoption percentage** and **province-wise breakdown**.

### ✅ **5. Insights Summary**
- Highlights total organizations, art form diversity, and digital readiness across provinces.

---

## 🧠 **TECH STACK**

| Category | Tools Used |
|-----------|------------|
| **Frontend** | Streamlit, Plotly |
| **Backend** | Python |
| **Database** | MongoDB |
| **Data Source** | Wikidata SPARQL Endpoint |
| **Libraries** | Pandas, BeautifulSoup, Requests |

---

## ⚙️ **INSTALLATION & SETUP**

### 1️⃣ Clone the Repository
git clone https://github.com/abdulzuhail/arts_dashboard.git
cd arts_dashboard
### 2️⃣ **INSTALL DEPENDENCIES**
pip install -r requirements.txt
git clone https://github.com/abdulzuhail/arts_dashboard.git
cd arts_dashboard
