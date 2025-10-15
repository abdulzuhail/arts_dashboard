PROJECT_TITLE: "🎨 ARTS ORGANIZATIONS IN CANADA DASHBOARD"

DESCRIPTION: >
  **An interactive data visualization dashboard** built using **Streamlit**, **MongoDB**, 
  and **Plotly** to analyze and display information about **arts organizations across Canada**.  
  This project fetches real-time data from **Wikidata**, stores it in **MongoDB**, 
  and provides insights into **distribution, art forms, and JSON-LD structured data adoption**.

---

PROJECT_DEMO:
  TITLE: "🎥 PROJECT DEMO"
  LINK: "https://github.com/abdulzuhail/arts_dashboard/blob/main/streamlit-dashboard.mp4"
  PREVIEW: "https://github.com/abdulzuhail/arts_dashboard/blob/main/streamlit-dashboard.mp4"
  NOTE: >
    🎬 **Watch the dashboard in action** to explore how data visualization and insights 
    are presented interactively using Streamlit.

---

FEATURES:
  - TITLE: "✅ DATA FETCHING FROM WIKIDATA"
    DETAILS:
      - "Retrieves arts organization data — name, type, province, website, and founded year."
      - "Automatically stores or updates data in MongoDB."

  - TITLE: "✅ STREAMLIT DASHBOARD INTERFACE"
    DETAILS:
      - "Search and filter organizations by name, location, or type."
      - "Download filtered data as CSV directly from the dashboard."
      - "Interactive visualizations built using Plotly."

  - TITLE: "✅ VISUAL ANALYTICS"
    DETAILS:
      - "📊 **Bar Charts:** Distribution of organizations by province."
      - "📈 **Line Charts:** Yearly growth trend of new organizations."
      - "🥧 **Pie Charts:** JSON-LD adoption (Yes vs No)."

  - TITLE: "✅ JSON-LD WEBSITE ANALYSIS"
    DETAILS:
      - "Scans organization websites for JSON-LD structured data."
      - "Displays adoption percentage and province-wise breakdown."

  - TITLE: "✅ INSIGHTS SUMMARY"
    DETAILS:
      - "Shows total organizations, diversity of art types, and overall digital readiness."

---

TECH_STACK:
  FRONTEND: ["Streamlit", "Plotly"]
  BACKEND: ["Python"]
  DATABASE: ["MongoDB"]
  DATA_SOURCE: ["Wikidata SPARQL Endpoint"]
  LIBRARIES: ["Pandas", "BeautifulSoup", "Requests"]

---

INSTALLATION_AND_SETUP:
  STEP_1: 
    TITLE: "1️⃣ CLONE THE REPOSITORY"
    COMMANDS:
      - "git clone https://github.com/abdulzuhail/arts_dashboard.git"
      - "cd arts_dashboard"

  STEP_2: 
    TITLE: "2️⃣ INSTALL DEPENDENCIES"
    COMMANDS:
      - "pip install -r requirements.txt"

  STEP_3:
    TITLE: "3️⃣ CONFIGURE MONGODB"
    FILE: "scripts/config.py"
    CONTENT:
      MONGO_URI: "mongodb://localhost:27017/"
      DB_NAME: "arts_db"
      COLLECTION_NAME: "organizations"

  STEP_4:
    TITLE: "4️⃣ FETCH DATA FROM WIKIDATA"
    COMMAND: "python scripts/fetch_wikidata.py"

  STEP_5:
    TITLE: "5️⃣ ANALYZE WEBSITES FOR JSON-LD"
    COMMAND: "python scripts/website.py"

  STEP_6:
    TITLE: "6️⃣ RUN STREAMLIT DASHBOARD"
    COMMAND: "streamlit run scripts/dashboard.py"

---

📊 SAMPLE_VISUALS:
  - NAME: "📍 ORGANIZATIONS BY PROVINCE"
    DESCRIPTION: "Displays the geographic distribution of arts organizations across Canada."

  - NAME: "🎭 TYPES OF ART FORMS"
    DESCRIPTION: "Visualizes representation of visual, performing, and cultural arts."

  - NAME: "📈 YEARLY GROWTH TRENDS"
    DESCRIPTION: "Shows how arts organizations have grown over time."

  - NAME: "🌐 JSON-LD ADOPTION"
    DESCRIPTION: "Highlights the percentage of organizations using structured data."

---

🧩 FUTURE_ENHANCEMENTS:
  - "🔁 Integrate automatic scheduled updates for Wikidata data fetching."
  - "📊 Add province-level drill-down and interactive filtering."
  - "🌍 Expand data sources for deeper cultural and organizational insights."
