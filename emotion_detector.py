from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=None
)

def detect_emotion(text):

    text = text.lower()

    emotion_keywords = {

        "anger": [
            "angry",
            "anger",
            "furious",
            "mad",
            "annoyed",
            "irritated",
            "frustrated",
            "rage",
            "hate"
        ],

        "sadness": [
            "sad",
            "cry",
            "crying",
            "depressed",
            "heartbroken",
            "lonely",
            "hurt",
            "broken",
            "empty",
            "upset",
            "miss someone",
            "lost"
        ],

        "joy": [
            "happy",
            "joy",
            "excited",
            "smile",
            "great",
            "amazing",
            "wonderful",
            "good",
            "peaceful",
            "grateful"
        ],

        "fear": [
            "fear",
            "afraid",
            "anxious",
            "scared",
            "worried",
            "panic",
            "overthinking",
            "nervous",
            "stress",
            "stressed"
        ],

        "neutral": [
            "okay",
            "fine",
            "normal",
            "nothing",
            "neutral",
            "calm"
        ],

        "surprise": [
            "surprised",
            "shock",
            "unexpected",
            "suddenly",
            "wow"
        ],

        "disgust": [
            "disgust",
            "gross",
            "disappointed",
            "disturbed"
        ]
    }

    # KEYWORD MATCHING

    for emotion, keywords in emotion_keywords.items():

        for word in keywords:

            if word in text:
                return emotion

    # AI MODEL PREDICTION

    try:

        results = classifier(text)

        detected_emotion = results[0][0]["label"]

        return detected_emotion

    except:

        return "neutral"