personal_data = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]
training_data = open('ques_ans.txt').read().splitlines()

conversation = personal_data + training_data