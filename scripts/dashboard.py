import streamlit as st
import pandas as pd
import plotly.express as px
from pymongo import MongoClient
import config
client = MongoClient(config.MONGO_URI)
db = client[config.DB_NAME]
collection = db[config.COLLECTION_NAME]
st.set_page_config(page_title="Arts Organizations in Canada", layout="wide")
st.title("Arts Organizations in Canada Dashboard")
st.sidebar.header("Filters")
filters = {
    "name": st.sidebar.text_input("Search by Organization Name"),
    "location": st.sidebar.text_input("Search by Location"), 
    "type": st.sidebar.text_input("Search by Art Type")
}
query = {key: {"$regex": value, "$options": "i"} for key, value in filters.items() if value}
df = pd.DataFrame(list(collection.find(query, {"_id": 0})))
if df.empty:
    st.warning("No organizations found.")
else:
    st.success(f"Found {len(df)} organizations.")
    st.dataframe(df, use_container_width=True)
    st.download_button(
        label="Download CSV",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name="organizations.csv",
        mime="text/csv",
    )
    st.header("Data Visualizations")
    def create_chart(column, title, chart_type="bar"):
        if column in df.columns and not df[column].isna().all():
            st.subheader(title)
            counts = df[column].value_counts()
            if chart_type == "line":
                counts = counts.sort_index()
                st.line_chart(counts)
            else:
                st.bar_chart(counts)
    create_chart("location", "Distribution of Organizations by Location")
    create_chart("type", "Types of Art Forms Represented")
    if "founded_year" in df.columns and not df["founded_year"].isna().all():
        df["founded_year"] = pd.to_numeric(df["founded_year"], errors="coerce")
        create_chart("founded_year", "Yearly Growth of Organizations", "line")
    st.header("JSON-LD Structured Data Adoption")  
    if "has_jsonld" in df.columns:
        total_with_jsonld = df["has_jsonld"].sum()
        percent = (total_with_jsonld / len(df) * 100) if len(df) > 0 else 0
        st.metric("Organizations using JSON-LD", f"{percent:.1f}%")
        fig = px.pie(df, names="has_jsonld", title="JSON-LD Adoption",
                    color_discrete_map={True: "yellow", False: "red"})
        st.plotly_chart(fig, use_container_width=True)
        if "location" in df.columns:
            jsonld_by_loc = df.groupby("location")["has_jsonld"].mean() * 100
            fig2 = px.bar(jsonld_by_loc.reset_index(), x="location", y="has_jsonld",
                         title="JSON-LD Adoption by Location (%)",
                         labels={"has_jsonld": "Adoption (%)"})
            st.plotly_chart(fig2, use_container_width=True)
    else:
        st.warning("Run the website analysis script to enable JSON-LD insights.")