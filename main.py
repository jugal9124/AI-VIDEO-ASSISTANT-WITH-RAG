from dotenv import load_dotenv
from utils.audio_processor import process_input
from core.transcriber import transcribe_all
from core.summarize import summarize, generate_title
from core.extractor import extract_action_items, extract_key_decisions, extract_questions
from core.rag_engine import build_rag_chain, ask_question

load_dotenv()


def run_pipeline(source: str, language: str = "english"):
  print("starting AI Video Assitent")
  
  chunks = process_input(source)
  
  transcript = transcribe_all(chunks, language=language)
  print(f"raw transcription (first 300 characters) {transcript[:300]}")
  
  title = generate_title(transcript)
  
  summary = summarize(transcript)
  
  action_items = extract_action_items(transcript)
  
  decisions = extract_key_decisions(transcript)
  questions = extract_questions(transcript)
  
  rag_chain = build_rag_chain(transcript)
  
  return {
    "title": title,
    "summary": summary,
    "action_items": action_items,
    "decisions": decisions,
    "questions": questions,
    "rag_chain": rag_chain
  }


if __name__ == "__main__":
  source = input("Enter Youtube URL or Local file path: ").strip()
  language = input("Language (default is 'english'): ").strip() or "english"
  
  result = run_pipeline(source, language)
  
  print("\n" + "=" * 60)
  print(f"📌 TITLE: {result['title']}")
  print(f"\n📋 Summary:\n{result['summary']}")
  print(f"\n✅ Action items:\n{result['action_items']}")
  print(f"\n🔑 Key decisions:\n{result['decisions']}")
  print(f"\n❓ Open questions:\n{result['questions']}")
  print("\n" + "=" * 60)

  print("\n💬 Chat with your meeting (type 'exit' to quit)\n")
  rag_chain = result['rag_chain']
  while True:
    question = input("You: ").strip()
    if question.lower() in ["exit", "quit", "q"]:
      print("👋🏻 Goodbye!")
      break
    if not question:
      continue
    answer = ask_question(rag_chain, question)
    print(f"\n🎂 Assitant: {answer}\n")



