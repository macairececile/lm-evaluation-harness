# Copied from Master
def doc_to_text(doc) -> str:
    """
    Question: <question>
    Choix:
    A. <choice1>
    B. <choice2>
    C. <choice3>
    D. <choice4>
    Réponse:
    """
    choices = [doc["options"]["A"], doc["options"]["B"], doc["options"]["C"], doc["options"]["D"]]
    option_choices = {
        "A": choices[0],
        "B": choices[1],
        "C": choices[2],
        "D": choices[3],
    }

    prompt = "Question: " + doc["question"] + "\nChoix:\n"
    for choice, option in option_choices.items():
        prompt += f"{choice.upper()}. {option}\n"
    prompt += "Réponse:"
    return prompt
