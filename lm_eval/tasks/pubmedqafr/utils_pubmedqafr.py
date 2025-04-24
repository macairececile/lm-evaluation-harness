def doc_to_text(doc) -> str:
    answers = "".join((f"{k}. {v}\n") for k, v in doc["options"].items())
    return f"Question: {doc['question']}\n{answers}Réponse:"


def doc_to_target(doc) -> int:
    return doc["answer"]
