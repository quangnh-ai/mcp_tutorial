import wikipedia

def get_wikipedia_summary(query: str) -> str:
    data = wikipedia.summary(query)
    return data