class ResCleaner:
    def make_json_safe(self,video:dict):
        video = video.copy()
        video.pop("vector", None)
        if "score" in video:
            video["score"] = float(video["score"])
        if "similarity" in video:
            video["similarity"] = float(video["similarity"])
        return video

