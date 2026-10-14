from fastapi import FastAPI
from pydantic import BaseModel
from  recommender import RecommendationEngine
from embedings import ContentEmbeddings
from users_profile import UserProfileBuilder
from main import RunRecommendations
#================================#
app = FastAPI()
engine = RunRecommendations()
#================================#

class UserData(BaseModel):
    userVector: list

@app.get("/api/health")
def health():
    return {
        "status": "ok"
    }
@app.get("/api/v1/feed",status_code=200)
def feed(mode:str, diver_lvl:float):
    res = []
    user_vector = engine.build_user_vector()
    if user_vector is None:
        return {"message": "User vector doesnt exists"}
    recommendations = engine.make_recommends(mode,diver_lvl)
    for item in recommendations:
        video = item["video"]
        res.append([f"ID - {video["id"]}, Title  - {video["title"]}"])
      
    return res



 







