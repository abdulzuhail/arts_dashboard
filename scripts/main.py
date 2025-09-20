from fastapi import FastAPI, HTTPException, Body
from fastapi.responses import StreamingResponse
from pymongo import MongoClient
import pandas as pd, io
import config
app = FastAPI()
client = MongoClient(config.MONGO_URI)
db = client[config.DB_NAME]
collection = db[config.COLLECTION_NAME]
@app.get("/organizations")
def get_all(name: str = None, province: str = None):
    query = {}
    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if province:
        query["province"] = {"$regex": province, "$options": "i"}
    return list(collection.find(query, {"_id": 0}))
@app.get("/organizations/{org_id}")
def get_one(org_id: str):
    org = collection.find_one({"wikidata_id": org_id}, {"_id": 0})
    if not org:
        raise HTTPException(status_code=404)
    return org
@app.get("/organizations/download")
def download():
    orgs = list(collection.find({}, {"_id": 0}))
    if not orgs:
        raise HTTPException(status_code=404, detail="No data found")
    df = pd.DataFrame(orgs)
    stream = io.StringIO()
    df.to_csv(stream, index=False)
    stream.seek(0)
    return StreamingResponse(stream, media_type="text/csv", headers={
        "Content-Disposition": "attachment; filename=organizations.csv"
    })
@app.post("/organizations")
def add(org: dict = Body(...)):
    if "wikidata_id" not in org:
        raise HTTPException(status_code=400)
    collection.insert_one(org)
    return org
@app.put("/organizations/{org_id}")
def update(org_id: str, update: dict = Body(...)):
    result = collection.update_one({"wikidata_id": org_id}, {"$set": update})
    if result.matched_count == 0:
        raise HTTPException(status_code=404)
    return {"message": "Updated"}
@app.delete("/organizations/{org_id}")
def delete(org_id: str):
    result = collection.delete_one({"wikidata_id": org_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404)
    return {"message": "Deleted"}