from src.retriever import retrieve_chunks
from src.generator import generate_answer

def answer_question(question: str) -> str:
	chunks = retrieve_chunks(question, top_k=6)
	answer = generate_answer(question, chunks)

	return answer
