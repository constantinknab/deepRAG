import ollama

def generate_answer(question: str, chunks: list[dict]) -> str:
	context_parts = []

	for i, chunk in enumerate(chunks, start=1):
		title = chunk["metadata"]["title"]
		text = chunk["text"]

		context_parts.append(
			f"[Source {i}]\nTitle: {title}\nText: {text}"
		)

	context = "\n\n".join(context_parts)

	prompt = f"""
You are answering a question using only the provided Wikipedia-derived sources.

Question:
{question}

Sources:
{context}

Write a clear, structured answer. Do not invent facts. If the sources do not contain enough evidence, say so.

At the end, list the source titles you used.
"""

	response = ollama.chat(
		model="llama3.2",
		messages=[
			{
				"role": "user",
				"content": prompt
			}
		]
	)

	return response["message"]["content"]
