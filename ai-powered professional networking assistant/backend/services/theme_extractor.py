from transformers import pipeline


class ThemeExtractor:
    def __init__(self):
        self.classifier = pipeline(
            "zero-shot-classification",
            model="distilbert-base-uncased-mnli"
        )

    def extract_themes(self, text: str):
        candidate_themes = [
            "Artificial Intelligence",
            "Machine Learning",
            "Climate Change",
            "Sustainability",
            "Urban Planning",
            "Healthcare",
            "Blockchain",
            "Cybersecurity",
            "Data Science",
            "Robotics",
            "Internet of Things",
            "Smart Cities",
            "Renewable Energy",
            "Business",
            "Entrepreneurship",
            "Finance",
            "Education",
            "Technology"
        ]

        result = self.classifier(
            text,
            candidate_themes,
            multi_label=True
        )

        themes = []

        for label, score in zip(
            result["labels"],
            result["scores"]
        ):
            if score >= 0.25:
                themes.append({
                    "theme": label,
                    "score": round(float(score), 3)
                })

        return themes


theme_extractor = ThemeExtractor()
