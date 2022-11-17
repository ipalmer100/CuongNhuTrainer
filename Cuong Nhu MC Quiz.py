# Create Question class and use it to build a multiple choice quiz
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
# import Question.py and then class from Question.py
question_prompts = [
    "What are the five firsts of friendship?\n(a) Communicate, smile, care, share, forgive"
    "\n(b) Communicate, spread love, grin, trade, be kind"
    "\n(c) Talk, smirk, love, shove, wear glove\n\n",
    # question_prompts[0]
    "What is the second D of a winner?\n(a) Direction\n(b) Discipline\n(c) Determination\n\n",
    # question_prompts[1]
    "From which country did Vovinam originate?"
    "\n(a) Japan\n(b) China\n(c) Vietnam\n(d) Korea\n(e) None of the above\n\n",
    # [2]
    "From which country did Judo originate?\n(a) Japan\n(b) China\n(c) Vietnam\n(d) Korea\n(e) None of the above\n\n",
    # [3]
    "From which country did Shotokan originate?"
    "\n(a) Japan\n(b) China\n(c) Vietnam\n(d) Korea\n(e) None of the above\n\n",
    # [4]
    "From which country did Boxing originate?\n(a) Japan\n(b) China\n(c) Vietnam\n(d) Korea\n(e) None of the above\n\n",
    # [5]
    "From which country did Aikido originate?\n(a) Japan\n(b) China\n(c) Vietnam\n(d) Korea\n(e) None of the above\n\n",
    # [6]
    "From which country did Wing Chun originate?"
    "\n(a) Japan\n(b) China\n(c) Vietnam\n(d) Korea\n(e) None of the above\n\n",
    # [7]
    "From which country did Tai Chi Chuan (Shadowboxing) originate?"
    "\n(a) Japan\n(b) China\n(c) Vietnam\n(d) Korea\n(e) None of the above\n\n",
    # [8]
    "What are the five As of self defense?"
    "\n(a) Alertness, Apathy, Attack, Aggrandize, Amass"
    "\n(b) Ambivalence, Ambidextrous, Atheism, Apologize, Asynchronous"
    "\n(c) Avoidance, Actualize, Ambivalence, Actuation, Attack"
    "\n(d) Awareness, Alertness, Avoidance, Anticipation, Action\n\n",
    # [9]
    "What are the mental keynotes for students of Cuong Nhu?"
    "\n(a) Self-confidence, Self-control, Modesty, Pro-defeatist attitude"
    "\n(b) Self-deprecation, Self-indulgence, Large ego, Non-winnist attitude"
    "\n(c) Self-confidence, Self-control, Modesty, Non-defeatist attitude"
    "\n(d) Self-confidence, Self-care, Timeliness, Cleanliness\n\n",
    # [10]
    "Finish the sixth code of ethics: Cuong Nhu students, through dedicated daily practice, increase their "
    "___, ___, and ___."
    "\n(a) Spirit, Strength, Moral Character"
    "\n(b) Spirit, Stamina, Moral Character"
    "\n(c) Fortitude, Mental Endurance, Strength"
    "\n(d) Senselessness, Selfishness, Moral Ambiguity\n\n",
    # [11]
    "Only by absolute discipline of ___, ___, and ___ do students maintain honor in Cuong Nhu."
    "\n(a) Mind, Matter, Morality"
    "\n(b) Mind, Body, Spirit"
    "\n(c) Body, Mind, Soul"
    "\n(d) Mind, Matter, Ki\n\n",
    # [12]
    "Osoto Gari is a Judo technique also known as ___."
    "\n(a) small outer reap"
    "\n(b) big inner reap"
    "\n(c) small inner reap"
    "\n(d) big outer reap\n\n",
    # [13]
    "Kosoto Gari is a Judo technique also known as ___."
    "\n(a) small outer reap"
    "\n(b) big inner reap"
    "\n(c) small inner reap"
    "\n(d) big outer reap\n\n",
    # [14]
    "During which year was Cuong Nhu created?"
    "\n(a) 1972"
    "\n(b) 1979"
    "\n(c) 1965"
    "\n(d) 1963\n\n",
    # [15]
    "What is the translation for 'Beautiful springtime'?"
    "\n(a) Judo"
    "\n(b) Aikido"
    "\n(c) Wing Chun"
    "\n(d) Shotokan\n\n",
    # [16]
    "What is the translation for 'Way of combined inner strength'?"
    "\n(a) Judo"
    "\n(b) Aikido"
    "\n(c) Wing Chun"
    "\n(d) Shotokan\n\n",
    # [17]
    "What is the translation for 'Hall of waves and pine'?"
    "\n(a) Judo"
    "\n(b) Aikido"
    "\n(c) Wing Chun"
    "\n(d) Shotokan\n\n",
    # [18]
]

questions = [
    Question(question_prompts[0], "a"), # Question created from class in Question.py
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c"),
    Question(question_prompts[3], "a"),
    Question(question_prompts[4], "a"),
    Question(question_prompts[5], "e"),
    Question(question_prompts[6], "a"),
    Question(question_prompts[7], "b"),
    Question(question_prompts[8], "b"),
    Question(question_prompts[9], "d"),
    Question(question_prompts[10], "c"),
    Question(question_prompts[11], "b"),
    Question(question_prompts[12], "b"),
    Question(question_prompts[13], "d"),
    Question(question_prompts[14], "a"),
    Question(question_prompts[15], "c"),
    Question(question_prompts[16], "c"),
    Question(question_prompts[17], "b"),
    Question(question_prompts[18], "d"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    final_score = (int(score) / int(len(questions)))*100
    print("You got " + str(score) + "/" + str(len(questions)) + " correct.")
    print((str(round(final_score))) + "%")

run_test(questions)

