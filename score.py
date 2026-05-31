def calculate_score(user_answers, questions):

    score = 0

    for i,q in enumerate(questions):
        if user_answers[i] == q["answer"]:
            score += 1

    return score