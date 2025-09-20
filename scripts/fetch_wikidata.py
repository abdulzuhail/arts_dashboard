import requests
import pandas as pd
from pymongo import MongoClient
from datetime import datetime, UTC
import config
query = """
SELECT ?org ?orgLabel ?typeLabel ?locationLabel ?website
WHERE {
  ?org wdt:P31/wdt:P279* wd:Q20897549;  
       wdt:P17 wd:Q16.                  
  OPTIONAL { ?org wdt:P856 ?website }
  OPTIONAL { ?org wdt:P159 ?location }
  OPTIONAL { ?org wdt:P31 ?type }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
LIMIT 1000
"""
url = "https://query.wikidata.org/sparql"
headers = {
    "Accept": "application/sparql-results+json",
    "User-Agent": "MyPythonApp/1.0 (https://example.com)"
}
response = requests.get(url, params={"query": query}, headers=headers)
response.raise_for_status()
results = response.json()["results"]["bindings"]
data = []
for r in results:
    org_url = r.get("org", {}).get("value", "")
    wikidata_id = org_url.split("/")[-1] if org_url else ""
    doc = {
        "wikidata_id": wikidata_id,
        "name": r.get("orgLabel", {}).get("value"),
        "type": r.get("typeLabel", {}).get("value"),
        "location": r.get("locationLabel", {}).get("value"),
        "website": r.get("website", {}).get("value"),
        "fetched_at": datetime.now(UTC)
    }
    data.append(doc)
df = pd.DataFrame(data)
print(df.head())
client = MongoClient(config.MONGO_URI)
db = client[config.DB_NAME]
collection = db[config.COLLECTION_NAME]
for doc in data:
    collection.update_one(
        {"wikidata_id": doc["wikidata_id"]}, 
        {"$set": doc, "$setOnInsert": {"created_at": datetime.now(UTC)}},
        upsert=True )
print(f"Inserted {len(data)} records into MongoDB")
client.close()