import chromadb
from src.embedder import embed_text

CHROMA_DIR = "data/chroma"

def retrieve_chunks(question: str, top_k: int = 6) -> list[dict]:
	client = chromadb.PersistentClient(path=CHROMA_DIR)
	collection = client.get_or_create_collection(name="wiki_chunks")

	query_embedding = embed_text(question)

	results = collection.query(
		query_embeddings=[query_embedding],
		n_results=top_k
	)

	chunks = []

	for i in range(len(results["documents"][0])):
		chunks.append({
			"text": results["documents"][0][i],
			"metadata": results["metadatas"][0][i],
			"distance": results["distances"][0][i]
		})

	return chunks
