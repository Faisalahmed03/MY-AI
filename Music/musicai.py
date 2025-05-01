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

# Mood-based playlist dictionary with both Spotify and YouTube links
playlists = {
    "Happy": {
        "name": "Feel-Good Hits 😄",
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC",
        "youtube": "https://www.youtube.com/playlist?list=PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI",
        "quote": "Keep smiling, the world is brighter with you in it!"
    },
    "Sad": {
        "name": "Sad Bops 💔",
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1",
        "youtube": "https://www.youtube.com/playlist?list=PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj",
        "quote": "It’s okay to feel down. Music heals. ❤️"
    },
    "Chill": {
        "name": "Lofi Chill Vibes ☕",
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DX889U0CL85jj",
        "youtube": "https://www.youtube.com/playlist?list=PLzauDReXbuX14vId-JU6aDQ4U8Ov2xUHe",
        "quote": "Take it easy. Breathe. You've got this."
    },
    "Focused": {
        "name": "Deep Focus 🎯",
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DWZeKCadgRdKQ",
        "youtube": "https://www.youtube.com/playlist?list=PL8F6B0753B2CCA128",
        "quote": "Let the beats help you lock in 🔒"
    },
    "Heartbroken": {
        "name": "Heartbreak Anthems 💔🎶",
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DX7gIoKXt0gmx",
        "youtube": "https://www.youtube.com/playlist?list=PLH6pfBXQXHEC4vJbYKSlChJyUYP3U-E3e",
        "quote": "Feel it all. Music understands."
    },
    "Angry": {
        "name": "Rage & Release 🔥",
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DWYMFZRu0uESB",
        "youtube": "https://www.youtube.com/playlist?list=PLDIoUOhQQPlU5P2E_oQ1E3U-5iV5iYzCj",
        "quote": "Let it out through the volume. You're strong."
    },
    "Romantic": {
        "name": "Date Night ❤️",
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DX50QitC6Oqtn",
        "youtube": "https://www.youtube.com/playlist?list=PLVav3Y_2PqDf2N_xV93wYu9fqib5Wj4tx",
        "quote": "Love is in the air — and the playlist 🎶"
    }
}

# Show recommendation
if mood:
    selected = playlists[mood]
    st.markdown(f"### 🎵 {selected['name']}")
    st.markdown(f"[▶️ Open on Spotify]({selected['spotify']})")
    st.markdown(f"[📺 Open on YouTube]({selected['youtube']})")
    st.info(selected["quote"])
