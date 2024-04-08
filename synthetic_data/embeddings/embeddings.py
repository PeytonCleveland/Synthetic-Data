from llama_index.embeddings.openai import OpenAIEmbedding
from synthetic_data.settings import settings
 
class Embeddings:
    def __init__(self, model = 'text-embedding-3-large'):
        self.model = model
        self.embeddings = []
        self.llm = OpenAIEmbedding(model=model, api_key=settings.OPENAI_API_KEY)

    def add(self, text):
        self.embeddings.append((text, self.llm.get_text_embedding(text)))
        return self
    
    def add_list(self, texts):
        batch = self.llm.get_text_embedding_batch(texts)
        for text, embedding in zip(texts, batch):
            self.embeddings.append((text, embedding))

        return self
    
    def dedupe(self, threshold=0.9):
        unique_embeddings = []
        for emb in self.embeddings:
            if all(self.llm.similarity(emb[1], uniq_emb[1]) < threshold for uniq_emb in unique_embeddings):
                unique_embeddings.append(emb)
        print(f"Removed {len(self.embeddings) - len(unique_embeddings)} duplicates")
        self.embeddings = unique_embeddings
        return self
    
    def get(self):
        return self.embeddings
