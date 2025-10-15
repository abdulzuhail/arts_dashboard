project:
  title: "🎨 Arts Organizations in Canada Dashboard"
  description: >
    An interactive data visualization dashboard built using Streamlit, MongoDB, and Plotly 
    to analyze and display information about arts organizations across Canada. 
    The project fetches real-time data from Wikidata, stores it in MongoDB, and provides 
    insights into distribution, art forms, and structured data (JSON-LD) adoption.

demo:
  title: "🎥 Project Demo"
  link: "https://github.com/abdulzuhail/arts_dashboard/blob/main/streamlit-dashboard.mp4"
  preview_url: "https://github.com/abdulzuhail/arts_dashboard/blob/main/streamlit-dashboard.mp4"

features:
  - title: "✅ Data Fetching from Wikidata"
    details:
      - "Retrieves arts organization data (name, type, province, website, founded year)."
      - "Automatically stores or updates data in MongoDB."

  - title: "✅ Streamlit Dashboard Interface"
    details:
      - "Search and filter organizations by name, location, and type."
      - "Download filtered results as CSV."
      - "Interactive charts built with Plotly."

  - title: "✅ Visual Analytics"
    details:
      - "Bar Charts: Distribution of organizations by province."
      - "Line Charts: Yearly growth of new organizations."
      - "Pie Charts: JSON-LD adoption (Yes vs No)."

  - title: "✅ JSON-LD Website Analysis"
    details:
      - "Scans organization websites for JSON-LD structured data."
      - "Displays adoption percentage and breakdown by province."

  - title: "✅ Insights Summary"
    details:
      - "Highlights total organizations, art form diversity, and digital readiness across provinces."

tech_stack:
  frontend: ["Streamlit", "Plotly"]
  backend: ["Python"]
  database: ["MongoDB"]
  data_source: ["Wikidata SPARQL Endpoint"]
  libraries: ["Pandas", "BeautifulSoup", "Requests"]

installation:
  steps:
    - step: "1️⃣ Clone the repository"
      commands:
        - "git clone https://github.com/abdulzuhail/arts_dashboard.git"
        - "cd arts_dashboard"

    - step: "2️⃣ Install dependencies"
      commands:
        - "pip install -r requirements.txt"

    - step: "3️⃣ Configure MongoDB"
      file: "scripts/config.py"
      content:
        MONGO_URI: "mongodb://localhost:27017/"
        DB_NAME: "arts_db"
        COLLECTION_NAME: "organizations"

    - step: "4️⃣ Fetch data from Wikidata"
      command: "python scripts/fetch_wikidata.py"

    - step: "5️⃣ Analyze websites for JSON-LD"
      command: "python scripts/website.py"

    - step: "6️⃣ Run Streamlit Dashboard"
      command: "streamlit run scripts/dashboard.py"

visuals:
  - name: "📍 Organizations by Province"
    description: "Displays geographic distribution of arts organizations."

  - name: "🎭 Types of Art Forms"
    description: "Visualizes representation of visual, performing, and cultural art forms."

  - name: "📈 Yearly Growth Trends"
    description: "Shows growth patterns of arts organizations over time."

  - name: "🌐 JSON-LD Adoption"
    description: "Highlights percentage of organizations using structured data."

future_enhancements:
  - "Integrate automatic scheduled updates for Wikidata fetch."
  - "Add province-level drill-down analysis."
  - "Expand data sources for better cultural insights."
