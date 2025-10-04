import streamlit as st
import pandas as pd
from pymongo import MongoClient
import sys
import os

# Ensure scripts.config is importable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import scripts.config as config

client = MongoClient(config.MONGO_URI)
db = client[config.DB_NAME]
collection = db[config.COLLECTION_NAME]

st.title("Arts Organizations in Canada")
st.sidebar.header("Filters")
name_filter = st.sidebar.text_input("Search by Organization Name")
location_filter = st.sidebar.text_input("Search by Location")
type_filter = st.sidebar.text_input("Search by Type")

query = {}
if name_filter:
    query["name"] = {"$regex": name_filter, "$options": "i"}
if location_filter:
    query["location"] = {"$regex": location_filter, "$options": "i"}
if type_filter:
    query["type"] = {"$regex": type_filter, "$options": "i"}

orgs = list(collection.find(query, {"_id": 0}))
df = pd.DataFrame(orgs)

if not df.empty:
    st.success(f"Found {len(df)} organizations")
    st.dataframe(df)
    st.subheader("Data Visualizations")
    if "location" in df.columns and not df["location"].isnull().all():
        st.write("### Distribution of Organizations by Province")
        province_counts = df["location"].value_counts()
        st.bar_chart(province_counts)
    if "type" in df.columns and not df["type"].isnull().all():
        st.write("### Types of Art Forms Represented")
        type_counts = df["type"].value_counts()
        st.bar_chart(type_counts)
    if "founded_year" in df.columns and not df["founded_year"].isnull().all():
        st.write("### Yearly Growth of Organizations")
        yearly_counts = df["founded_year"].value_counts().sort_index()
        st.line_chart(yearly_counts)
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(label="Download CSV", data=csv, file_name="organizations.csv", mime="text/csv")
else:
    st.warning("No organizations found with the given filters.")