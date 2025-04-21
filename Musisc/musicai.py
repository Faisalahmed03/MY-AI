# musicai_web.py

import streamlit as st

# Title
st.title("🎧 Mood Music AI")
st.subheader("Tell me how you're feeling, I'll find the vibe 🎵")

# Mood input
mood = st.selectbox(
    "How are you feeling right now?",
    ["Happy", "Sad", "Chill", "Focused", "Heartbroken", "Angry", "Romantic"]
)

# Mood-based playlist dictionary
playlists = {
    "Happy": {
        "name": "Feel-Good Hits 😄",
        "link": "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC",
        "quote": "Keep smiling, the world is brighter with you in it!"
    },
    "Sad": {
        "name": "Sad Bops 💔",
        "link": "https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1",
        "quote": "It’s okay to feel down. Music heals. ❤️"
    },
    "Chill": {
        "name": "Lofi Chill Vibes ☕",
        "link": "https://open.spotify.com/playlist/37i9dQZF1DX889U0CL85jj",
        "quote": "Take it easy. Breathe. You've got this."
    },
    "Focused": {
        "name": "Deep Focus 🎯",
        "link": "https://open.spotify.com/playlist/37i9dQZF1DWZeKCadgRdKQ",
        "quote": "Let the beats help you lock in 🔒"
    },
    "Heartbroken": {
        "name": "Heartbreak Anthems 💔🎶",
        "link": "https://open.spotify.com/playlist/37i9dQZF1DX7gIoKXt0gmx",
        "quote": "Feel it all. Music understands."
    },
    "Angry": {
        "name": "Rage & Release 🔥",
        "link": "https://open.spotify.com/playlist/37i9dQZF1DWYMFZRu0uESB",
        "quote": "Let it out through the volume. You're strong."
    },
    "Romantic": {
        "name": "Date Night ❤️",
        "link": "https://open.spotify.com/playlist/37i9dQZF1DX50QitC6Oqtn",
        "quote": "Love is in the air — and the playlist 🎶"
    }
}

# Show recommendation
if mood:
    selected = playlists[mood]
    st.markdown(f"### 🎵 {selected['name']}")
    st.markdown(f"[▶️ Open Playlist]({selected['link']})")
    st.info(selected["quote"])
