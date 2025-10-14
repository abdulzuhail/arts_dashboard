import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import config
from concurrent.futures import ThreadPoolExecutor, as_completed
client = MongoClient(config.MONGO_URI)
db = client[config.DB_NAME]
collection = db[config.COLLECTION_NAME]
def has_jsonld(url):
    try:
        res = requests.get(url, timeout=5, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(res.text, "html.parser")
        return bool(soup.find("script", type="application/ld+json"))
    except Exception as e:
        print(f"Error checking {url}: {e}")
        return None
def process_org(org):
    url = org["website"]
    result = has_jsonld(url)
    if result is None:
        print(f"Skipped {url}")
    else:
        collection.update_one({"website": url}, {"$set": {"has_jsonld": result}})
        print(f"{url} {'contains' if result else 'does not contain'} JSON-LD")
def main():
    orgs = list(collection.find({"website": {"$ne": None}}, {"_id": 0, "website": 1}))
    print(f"Checking {len(orgs)} websites for JSON-LD structured data...\n")
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(process_org, orgs)
    print("\nWebsite analysis complete.")
if __name__ == "__main__":
    main()