from data import videos
from embedings import ContentEmbeddings
from users_profile import UserProfileBuilder
from recommender import RecommendationEngine

class RunRecommendations:
    def __init__(self):
        #======================================#
        self.embeddings = ContentEmbeddings()
        self.engine = RecommendationEngine()
        self.user = UserProfileBuilder()
        #======================================#
        self.videos_with_vectors = []
        self.shown_video_ids = set()
        self.all_interactions = [{"video_id": 3, "action": "like"},{"video_id": 4, "action": "like"},]
        for video in videos:
            video_text = self.embeddings.build_video_text(video)
            video["vector"] = self.embeddings.video_to_vector(video_text)
            self.videos_with_vectors.append(video)





    def build_category_scores(self):
        video_map = {
            video["id"]: video
            for video in self.videos_with_vectors
        }

        action_scores = {
            "like": 2.0,
            "save": 2.5,
            "long_view": 1.2,
            "view": 0.3,
            "skip": -0.7,
            "dislike": -2.0,
        }

        category_scores = {}

        for interaction in self.all_interactions:
            video = video_map.get(interaction["video_id"])
            if video is None:
                continue

            category = video["category"]
            action = interaction["action"]
            score = action_scores.get(action, 0)

            category_scores[category] = category_scores.get(category, 0) + score

        return category_scores


    def build_user_vector(self):
        return self.user.build_user_vector(
            interactions=self.all_interactions,
            videos_with_vectors=self.videos_with_vectors
        )


    def build_user_categories(self):
        interacted_video_ids = {
            interaction["video_id"]
            for interaction in self.all_interactions
        }
        return {
            video["category"]
            for video in self.videos_with_vectors
            if video["id"] in interacted_video_ids
        }
    def make_recommends(self,mode:str="focus",diver_lvl:float = 0.05, limit:int = 3):
        #  for v in self.all_interactions:
        #     self.shown_video_ids.add(v["video_id"])
         recommendations = self.engine.recommend(
            user_vector=user_vector,
            videos_with_vectors=self.videos_with_vectors,
            seen_video_ids=self.shown_video_ids,
            diversity_level=diver_lvl,
            mode=mode,
            limit=limit
        )
         if not recommendations:
            return {"message" : "No available videos for recommendations"}
         for v in recommendations:
             self.shown_video_ids.add(v["video"]["id"])
         return recommendations

engine = RunRecommendations() 
user_vector = engine.build_user_vector()
user_categories = engine.build_user_categories()
category_scores = engine.build_category_scores()

user_categories

# print("Initial user categories:", user_categories)
# print("Initial category scores:", category_scores)


# while True:
#     if user_vector is None:
#         print("Недостаточно данных для построения user_vector.")
#         break


#     recommendations = engine.make_recommends()

#     for item in recommendations:
#         video = item["video"]

#         print("-" * 50)
#         print("ID:", video["id"])
#         print("Title:", video["title"])
#         print("Category:", video["category"])
#         print("Relevance:", round(item["relevance"], 3))
#         print("Novelty:", round(item["novelty"], 3))
#         print("Category score:", round(item["category_score"], 3))
#         print("Final score:", round(item["final_score"], 3))
#         print("-" * 50)
#         print("1 - Like; 2 - Dislike; 3 - Skip; 0 - Exit")
#         print("-" * 50)

#         user_choose = input("Choose action: ")

#         if user_choose == "1":
#             action = "like"

#         elif user_choose == "2":
#             action = "dislike"

#         elif user_choose == "3":
#             action = "skip"

#         elif user_choose == "0":
#             print("Exit.")
#             exit()

#         else:
#             print("Unknown action. Treated as skip.")
#             action = "skip"

#         interaction = {
#             "video_id": video["id"],
#             "action": action
#         }


#         engine.all_interactions.append(interaction)

#         engine.shown_video_ids.add(video["id"])

#     user_vector = engine.build_user_vector()
#     user_categories = engine.build_user_categories()
#     category_scores = engine.build_category_scores()

