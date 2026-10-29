from textblob import TextBlob
import wikipediaapi

wiki = wikipediaapi.Wikipedia(
    user_agent="LearningApp/1.0 (masoncute4real@gmail.com)",
    language="en",
)


def search_wikipedia(name):
    """
    Search Wikipedia for a given query/name.

    Parameters:
    name (str): The search term to look up on Wikipedia.
    """
    print(f"Searching for name: {name}")
    return wiki.search(name)


def summarize_wikipedia(name):
    """Summarize the Wikipedia page for a given query/name."""
    print(f"Summarizing page for name: {name}")
    page = wiki.page(name)
    if not page.exists():
        return ""
    return page.summary


def get_text_blob(text):
    """Get a TextBlob for the given text."""
    return TextBlob(text)


def get_phrases(name):
    """Find the Wikipedia page for a name and return its noun phrases."""
    text = summarize_wikipedia(name)
    blob = get_text_blob(text)
    phrases = blob.noun_phrases
    print(phrases)
    return phrases