import numpy as np


ACTION_WEIGHTS = {
    "like": 1.01,
    "save": 1.3,
    "long_view": 0.8,
    "view": 0.2,
    "skip": -0.4,
    "dislike": -1.0,
}


class UserProfileBuilder:
    def build_user_vector(self, interactions: list, videos_with_vectors: list):
        vectors = []
        weights = []

        video_map = {
            video["id"]: video
            for video in videos_with_vectors
        }

        for interaction in interactions:
            video_id = interaction["video_id"]
            action = interaction["action"]

            video = video_map.get(video_id)

            if not video:
                continue

            vector = video.get("vector")
            weight = ACTION_WEIGHTS.get(action, 0.0)

            if vector is None or weight == 0:
                continue

            vectors.append(vector)
            weights.append(weight)

        if not vectors:
            return None

        user_vector = np.average(
            vectors,
            axis=0,
            weights=weights
        ).astype("float32")

        norm = np.linalg.norm(user_vector)

        if norm > 0:
            user_vector = user_vector / norm

        return user_vector