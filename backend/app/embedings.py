from sentence_transformers import SentenceTransformer, util
from data import videos


class ContentEmbeddings:
    def __init__(self):
        self.model = SentenceTransformer(
            "sentence-transformers/paraphrase-multilingual-mpnet-base-v2"
        )

    def build_video_text(self, video: dict):

        return f"""
        {video["title"]}
        {video["description"]}
        {", ".join(video["tags"])}
        {video["category"]}
        """


    def video_to_vector(self,text:str):
        return self.model.encode(text)
    

    def compare_vectors(self, first_vector, second_vector) -> float:
        return util.cos_sim(first_vector, second_vector).item()


