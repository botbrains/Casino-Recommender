import streamlit as st
import numpy as np

# Initialize session state
if 'step' not in st.session_state:
    st.session_state.step = 0
    st.session_state.preferences = {
        "game_preference": None,
        "provider_preference": None,
        "payment_preference": None,
    }

# Define the list of online casinos with affiliate links
casinos = [
    {
        "name": "Betplay.io", 
        "games": ["slots", "poker", "blackjack", "roulette"], 
        "providers": ["No Preference", "Netent", "Microgaming"], 
        "payments": ["crypto"],
        "affiliate_link": "https://betplay.io/?ref=betrlist"
    },
    {
        "name": "BC.Game", 
        "games": ["roulette", "slots"], 
        "providers": ["No Preference", "Microgaming", "Netent"], 
        "payments": ["crypto", "card"],
        "affiliate_link": "https://bc.game/i-betrlist-n/"
    },
    {
        "name": "BitStarz", 
        "games": ["slots", "poker", "roulette"], 
        "providers": ["No Preference", "Playtech", "Microgaming", "Netent"], 
        "payments": ["crypto", "bank", "card"],
        "affiliate_link": "https://bs3.direct/b393c8f59"
    },
    {
        "name": "Pulsz", 
        "games": ["slots", "roulette"], 
        "providers": ["No Preference", "Microgaming", "Playtech", "Netent"], 
        "payments": ["bank", "card"],
        "affiliate_link": "www.pulsz.com/?invited_by=xu4qcd"
    },
]

# Function to calculate similarity score between user preferences and casino features
def calculate_similarity(user_prefs, casino):
    game_sim = len(set(user_prefs["game_preference"]).intersection(casino["games"])) / len(user_prefs["game_preference"])
    provider_sim = len(set(user_prefs["provider_preference"]).intersection(casino["providers"])) / len(user_prefs["provider_preference"])
    payment_sim = len(set(user_prefs["payment_preference"]).intersection(casino["payments"])) / len(user_prefs["payment_preference"])
    return np.mean([game_sim, provider_sim, payment_sim])

# Steps to ask questions
if st.session_state.step == 0:
    st.title("AI Casino Finder")
    st.subheader("What style of casino games do you prefer?")
    
    # Display images for game types
    st.image("slots.png", caption="Slots", width=100)
    st.image("poker.png", caption="Poker", width=100)
    st.image("poker.png", caption="Blackjack", width=100)
    st.image("roulette.png", caption="Roulette", width=100)
    
    st.session_state.preferences["game_preference"] = st.multiselect(
        "Choose favorite styles of casino gameplay", 
        ["slots", "poker", "blackjack", "roulette"],
        default=None,
    )
    if st.button("Next"):
        st.session_state.step += 1

elif st.session_state.step == 1:
    st.subheader("Select your favorite game provider!")
    
    # Display images for game providers
    st.image("no_preference_image.png", caption="No Preference", width=100)
    st.image("netent.png", caption="Netent", width=100)
    st.image("microgaming.png", caption="Microgaming", width=100)
    st.image("playtech.png", caption="Playtech", width=100)
    
    st.session_state.preferences["provider_preference"] = st.multiselect(
        "Select favorite game providers", 
        ["No Preference", "Netent", "Microgaming", "Playtech"],
        default=None,
    )
    if st.button("Next"):
        st.session_state.step += 1

elif st.session_state.step == 2:
    st.subheader("Which payment option do you prefer?")
    
    # Display images for payment methods
    st.image("crypto_image.png", caption="Crypto", width=100)
    st.image("bank_image.png", caption="Bank", width=100)
    st.image("card_image.png", caption="Card", width=100)
    
    st.session_state.preferences["payment_preference"] = st.multiselect(
        "Select favorite payment methods", 
        ["crypto", "bank", "card"],
        default=None,
    )
    if st.button("Find AI Casino Recommendations"):
        st.session_state.step += 1

# Display the best casinos based on user preferences
if st.session_state.step == 3:
    user_prefs = st.session_state.preferences
    best_casinos = sorted(casinos, key=lambda x: calculate_similarity(user_prefs, x), reverse=True)[:2]
    if best_casinos:
        st.subheader("Based on your preferences, AI recommends the following casino(s):")
        for casino in best_casinos:
            st.write(f"**{casino['name']}**")
            # Provide the unique affiliate link for the casino
            st.write(f"[Visit {casino['name']}]({casino['affiliate_link']})")
    else:
        st.subheader("No casinos match your preferences. Please try different options.")
    if st.button("Start Over"):
        st.session_state.step = 0
        st.session_state.preferences = {
            "game_preference": None,
            "provider_preference": None,
            "payment_preference": None,
        }
