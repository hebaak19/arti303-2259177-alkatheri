"""TODO: This moudle converts raw text into a cleaned-up format for display."""


def clean_name(raw):
    """TODO: collapse whitespace, then title-case."""
    cleaned = " ".join(raw.split())
    cleaned = cleaned.title()
    return cleaned
