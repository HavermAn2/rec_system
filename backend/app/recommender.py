import random
from sentence_transformers import util



class RecommendationEngine:
    def calculate_relevance(self, user_vector, video_vector) -> float:
        return util.cos_sim(user_vector, video_vector).item()

    # def calculate_novelty(self, video: dict, user_categories: set) -> float:
    #     if video["category"] in user_categories:
    #         return 0.1
    #     return 0.4

    def recommend(
        self,
        user_vector,
        videos_with_vectors: list,
        seen_video_ids: set,
        diversity_level: float ,
        mode: str,
        limit:int
    ):
        mode_settings = {
            "focus": {"diversity": 0.05, "random": 0.0},
            "balance": {"diversity": 0.25, "random": 0.02},
            "exploration": {"diversity": 0.5, "random": 0.05},
            "surprise": {"diversity": 0.7, "random": 0.15},
        }

        settings = mode_settings.get(mode)
        diversity = diversity_level if diversity_level is not None else settings["diversity"]
        random_power = settings["random"]


        recommendations = []
        for video in videos_with_vectors:
            if video["id"] in seen_video_ids:
                continue
            category = video["category"]
            relevance = self.calculate_relevance(user_vector, video["vector"])
            # novelty = self.calculate_novelty(video, user_categories)
            random_factor = random.random() * random_power

            # category_score = category_scores.get(category, 0)

            # if category_score > 0:
            #     category_bonus = category_score * 0.15
            #     category_penalty = 0
            # elif category_score < 0:
            #     category_bonus = 0
            #     category_penalty = abs(category_score) * 0.3
            # else:
            #     category_bonus = 0
            #     category_penalty = 0

            final_score = (
                relevance * 0.75
               * diversity
                + random_factor
                
            )

            recommendations.append({
                "video": video,
                "relevance": relevance,
                # "novelty": novelty,
                # "category_score": category_score,
                "final_score": final_score
            })

        recommendations.sort(
            key=lambda item: item["final_score"],
            reverse=True
        )
            
        return recommendations[:limit]