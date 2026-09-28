from services.theme_extractor import theme_extractor


text = """
AI for Sustainable Cities is a conference discussing
artificial intelligence, climate change, urban planning,
and sustainable technologies.
"""

themes = theme_extractor.extract_themes(text)

print("\nDetected Themes:\n")

for item in themes:
    print(
        f"{item['theme']} "
        f"({item['score']})"
    )
