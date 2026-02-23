from core.engine import PitchEngine

engine = PitchEngine()

print("\nPitchSense CLI\n")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit"]:
        print("Thank you......")
        break

    result = engine.evaluate_pitch(user_input)

    print("\nPitchSense:")
    print(result["mentor_response"])
    print("\n" + "-"*60 + "\n")