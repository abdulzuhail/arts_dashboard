import requests
from pymongo import MongoClient
import datetime
import config
query = """
SELECT ?org ?orgLabel ?description ?cityLabel ?provinceLabel ?website ?foundedYear
WHERE {
  ?org wdt:P31/wdt:P279* wd:Q20897549;
       wdt:P17 wd:Q16.
  OPTIONAL { ?org schema:description ?description FILTER(LANG(?description) = "en") }
  OPTIONAL { ?org wdt:P159 ?city. }
  OPTIONAL { ?org wdt:P131 ?province. }
  OPTIONAL { ?org wdt:P856 ?website. }
  OPTIONAL { ?org wdt:P571 ?foundedYear. }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en".}}
LIMIT 1000
"""
url = "https://query.wikidata.org/sparql"
headers = {"Accept":"application/sparql-results+json",
           "User-Agent":"ArtsDashboardBot/1.0 (contact@example.com)"}
print("Fetching data from Wikidata...")
response = requests.get(url,params={"query": query},headers=headers, timeout=60)
response.raise_for_status()
results = response.json()["results"]["bindings"]
data = []
for r in results:
    founded_raw = r.get("foundedYear", {}).get("value")
    founded_year = founded_raw.split("-")[0] if founded_raw else None
    doc = {
        "name": r.get("orgLabel", {}).get("value"),
        "description": r.get("description", {}).get("value"),
        "city": r.get("cityLabel", {}).get("value"),
        "province": r.get("provinceLabel", {}).get("value"),
        "website": r.get("website", {}).get("value"),
        "founded_year": int(founded_year) if founded_year and founded_year.isdigit() else None,
        "wikidata_id": r.get("org", {}).get("value"),
        "fetched_at": datetime.datetime.utcnow()}
    data.append(doc)
print(f"Retrieved{len(data)}records")
print("Saving to MongoDB")
client = MongoClient(config.MONGO_URI)
db = client[config.DB_NAME]
collection = db[config.COLLECTION_NAME]
for doc in data:
    collection.update_one(
        {"wikidata_id": doc["wikidata_id"]},
        {"$set": doc, "$setOnInsert": {"created_at": datetime.datetime.utcnow()}},
        upsert=True)
print("Fetch completed")
client.close()