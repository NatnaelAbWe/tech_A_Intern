import random
import time

def run_quiz():
    """Runs an interactive multiple-choice quiz."""
    questions = [
        {
            'id': 1,
            'question': 'Which planet is known as the Red Planet?',
            'options': ['A. Earth', 'B. Mars', 'C. Jupiter', 'D. Venus'],
            'answer': 'B'
        },
        {
            'id': 2,
            'question': 'Who wrote the play "Romeo and Juliet"?',
            'options': ['A. Charles Dickens', 'B. William Shakespeare', 'C. Mark Twain', 'D. Jane Austen'],
            'answer': 'B'
        },
        # You can add more questions here if needed
    ]

    score = 0
    total_questions = len(questions)
    start_time = time.time()

    print("\n🎯 Welcome to the Quiz! 🎯")
    print(f"You will be asked {total_questions} questions. Let's begin!\n")

    # Shuffle and iterate through the questions
    for question in random.sample(questions, k=total_questions):
        print(f"❓ {question['question']}")
        for option in question['options']:
            print(option)

        user_answer = input("👉 Enter your answer (A, B, C, or D): ").strip().upper()

        if user_answer == question['answer']:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Incorrect! The correct answer was {question['answer']}.\n")

        time.sleep(1)  # Pause briefly for better readability

    end_time = time.time()
    total_time = round(end_time - start_time, 2)

    print("🎉 Quiz Completed! 🎉")
    print(f"📊 Your Score: {score}/{total_questions}")
    print(f"⏳ Time Taken: {total_time} seconds\n")
    
    # Provide feedback based on performance
    if score == total_questions:
        print("🏆 Amazing! You got all answers correct!")
    elif score > total_questions // 2:
        print("👍 Good job! Keep practicing!")
    else:
        print("💡 Keep learning and try again!")

if __name__ == "__main__":
    run_quiz()
