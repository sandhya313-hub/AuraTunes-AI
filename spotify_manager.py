import random

def get_spotify_playlists(emotion, language):

    search_queries = {

        "English": {
            "joy": [
                "happy english songs",
                "feel good english music",
                "upbeat english playlist"
            ],

            "sadness": [
                "sad english songs",
                "emotional english playlist",
                "calm healing music"
            ],

            "anger": [
                "power workout songs",
                "rock energy playlist",
                "intense motivation music"
            ],

            "fear": [
                "peaceful piano music",
                "calm anxiety relief",
                "deep relaxation music"
            ],

            "neutral": [
                "chill english playlist",
                "soft evening music",
                "peaceful vibes"
            ]
        },

        "Telugu": {
            "joy": [
                "telugu party songs",
                "tollywood dance hits",
                "happy telugu playlist"
            ],

            "sadness": [
                "telugu melody songs",
                "emotional telugu playlist",
                "sad telugu songs"
            ],

            "anger": [
                "telugu mass songs",
                "high energy telugu songs",
                "telugu motivation hits"
            ],

            "fear": [
                "calm telugu melodies",
                "relaxing telugu music",
                "peaceful telugu songs"
            ],

            "neutral": [
                "telugu chill songs",
                "soft telugu playlist",
                "telugu relaxing music"
            ]
        },

        "Hindi": {
            "joy": [
                "bollywood party hits",
                "happy hindi songs",
                "bollywood dance playlist"
            ],

            "sadness": [
                "sad hindi songs",
                "bollywood emotional playlist",
                "heartbreak hindi music"
            ],

            "anger": [
                "bollywood power songs",
                "hindi motivation playlist",
                "intense hindi music"
            ],

            "fear": [
                "peaceful hindi songs",
                "relaxing bollywood playlist",
                "calm hindi melodies"
            ],

            "neutral": [
                "hindi chill playlist",
                "soft bollywood songs",
                "evening hindi vibes"
            ]
        },

        "Tamil": {
            "joy": [
                "tamil party songs",
                "kollywood hits",
                "happy tamil playlist"
            ],

            "sadness": [
                "tamil melody songs",
                "sad tamil playlist",
                "emotional tamil songs"
            ],

            "anger": [
                "tamil mass songs",
                "tamil energetic playlist",
                "powerful tamil hits"
            ],

            "fear": [
                "calm tamil songs",
                "peaceful tamil melodies",
                "soft tamil playlist"
            ],

            "neutral": [
                "tamil chill songs",
                "relaxing tamil music",
                "tamil evening vibes"
            ]
        },

        "Korean": {
            "joy": [
                "kpop happy playlist",
                "upbeat korean songs",
                "korean dance hits"
            ],

            "sadness": [
                "sad korean songs",
                "korean chill playlist",
                "emotional kpop"
            ],

            "anger": [
                "powerful kpop songs",
                "kpop workout playlist",
                "intense korean music"
            ],

            "fear": [
                "calm korean playlist",
                "peaceful kpop songs",
                "relaxing korean music"
            ],

            "neutral": [
                "korean chill vibes",
                "soft kpop playlist",
                "korean relaxing music"
            ]
        },

        "Japanese": {
            "joy": [
                "jpop happy playlist",
                "upbeat japanese songs",
                "japanese pop hits"
            ],

            "sadness": [
                "sad japanese songs",
                "emotional jpop playlist",
                "japanese calm music"
            ],

            "anger": [
                "anime workout songs",
                "powerful japanese music",
                "high energy jpop"
            ],

            "fear": [
                "peaceful japanese songs",
                "calm anime music",
                "relaxing japanese playlist"
            ],

            "neutral": [
                "japanese chill playlist",
                "soft japanese songs",
                "relaxing jpop"
            ]
        }

    }

    # DEFAULTS
    language_data = search_queries.get(
        language,
        search_queries["English"]
    )

    emotion_queries = language_data.get(
        emotion,
        language_data["neutral"]
    )

    # RANDOMIZE RESULTS
    selected_queries = random.sample(
        emotion_queries,
        min(2, len(emotion_queries))
    )

    playlists = []

    for query in selected_queries:

        spotify_url = (
            "https://open.spotify.com/search/"
            + query.replace(" ", "%20")
            + "/playlists"
        )

        playlists.append({
            "name": query.title(),
            "url": spotify_url
        })

    return playlists