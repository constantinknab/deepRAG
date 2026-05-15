import sys
from src.pipeline import answer_question

def main():
	if len(sys.argv) < 2:
		print("Usage: python app.py \"your question here\"")
		return

	question = sys.argv[1]
	answer = answer_question(question)
	print(answer)

if __name__ == "__main__":
	main()
