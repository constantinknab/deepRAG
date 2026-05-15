import os
import chromadb
from src.chunker import chunk_text
from src.embedder import embed_text

ARTICLES_DIR = "data/articles"
CHROMA_DIR = "data/chroma"

def ingest_articles():
	client = chromadb.PersistentClient(path=CHROMA_DIR)
	collection = client.get_or_create_collection(name="wiki_chunks")

	for filename in os.listdir(ARTICLES_DIR):
		if not filename.endswith(".txt"):
			continue

		path = os.path.join(ARTICLES_DIR, filename)

		with open(path, "r", encoding="utf-8") as file:
			text = file.read()

		title = filename.replace(".txt", "").replace("_", " ").title()
		chunks = chunk_text(text)

		for index, chunk in enumerate(chunks):
			chunk_id = f"{filename}_{index}"

			embedding = embed_text(chunk)

			collection.add(
				ids=[chunk_id],
				embeddings=[embedding],
				documents=[chunk],
				metadatas=[{
					"title": title,
					"source_file": filename,
					"chunk_index": index
				}]
			)

	print("Ingestion complete.")

if __name__ == "__main__":
	ingest_articles()
