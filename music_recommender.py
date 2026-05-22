import random

def recommend_music(emotion):

    playlists = {

        "joy": [
            "🌞 Golden Hour Vibes",
            "🎉 Happy Beats & Good Energy",
            "🚗 Feel Good Roadtrip",
            "✨ Dancing Through Life",
            "🎶 Bright Morning Motivation"
        ],

        "sadness": [
            "🌧️ Midnight Healing",
            "💙 Soft Rain & Memories",
            "🌌 Late Night Thoughts",
            "🎹 Piano for Heavy Hearts",
            "✨ Calm Your Mind"
        ],

        "anger": [
            "🔥 Chaos & Energy",
            "⚡ Unleash The Storm",
            "🎸 Intense Focus Mix",
            "💥 Break The Pressure",
            "🚀 Adrenaline Rush"
        ],

        "fear": [
            "🌙 Safe Space Melodies",
            "✨ Gentle Mind Reset",
            "💫 Calm Anxiety Playlist",
            "🎧 Deep Breathing Sounds",
            "🌿 Peaceful Inner Silence"
        ],

        "neutral": [
            "☁️ Easy Evening Tunes",
            "🎶 Soft Everyday Mix",
            "🌤️ Balanced Mood Playlist",
            "🚶 Calm Walk Music",
            "✨ Peaceful Atmosphere"
        ],

        "surprise": [
            "🎇 Unexpected Energy",
            "🎉 Mood Shift Mix",
            "⚡ Exciting Discoveries",
            "🌈 Spontaneous Vibes"
        ],

        "disgust": [
            "🌿 Emotional Detox",
            "🌧️ Reset Your Mind",
            "✨ Fresh Start Playlist",
            "🎧 Escape The Noise"
        ]
    }

    recommendations = playlists.get(emotion, ["🎵 No playlist found"])

    return random.sample(
        recommendations,
        min(3, len(recommendations))
    )