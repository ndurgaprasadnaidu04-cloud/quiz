questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is closest to the Sun?",
        "options": ["Venus", "Earth", "Mars", "Mercury"],
        "answer": "Mercury"
    },
    {
        "question": "How many sides does a triangle have?",
        "options": ["2", "3", "4", "5"],
        "answer": "3"
    },
]


def display_question(number, question_data):
    """Display a single question with its options."""
    print(f"\nQuestion {number}: {question_data['question']}")
    print("-" * 40)
    for i, option in enumerate(question_data["options"], start=1):
        print(f"  {i}. {option}")

def get_player_answer(question_data):
    """Ask the player to pick an option and return their answer."""
    while True:
        try:
            choice = int(input("\nYour answer (enter the number,Welcome to Durga's Quiz): "))
            if 1 <= choice <= len(question_data["options"]):
                return question_data["options"][choice - 1]
            else:
                print(f"Please enter a number between 1 and {len(question_data['options'])}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_quiz():
    """Run the full quiz game."""
    print("=" * 40)
    print("       WELCOME TO THE QUIZ GAME!")
    print("=" * 40)

    name = input("\nWhat is your name? ").strip()
    if not name:
        name = "Player"

    print(f"\nHello, {name}! Get ready to answer {len(questions)} questions.")
    input("Press Enter to start...")

    score = 0

    for i, question_data in enumerate(questions, start=1):
        display_question(i, question_data)
        player_answer = get_player_answer(question_data)

        if player_answer == question_data["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was: {question_data['answer']}")

    # Final results
    print("\n" + "=" * 40)
    print("          QUIZ COMPLETE!")
    print("=" * 40)
    print(f"\n{name}, you scored {score} out of {len(questions)}!")

    percentage = (score / len(questions)) * 100
    if percentage == 100:
        print("🏆 Perfect score! Amazing!")
    elif percentage >= 70:
        print("🌟 Great job!")
    elif percentage >= 50:
        print("👍 Not bad, keep practicing!")
    else:
        print("📚 Keep studying, you'll do better next time!")

    print("\nThanks for playing!")

# Start the game
if __name__ == "__main__":
    play_quiz()
