import streamlit as st
import numpy as np
from streamlit_image_select import image_select

# Initialize session state
if 'step' not in st.session_state:
    st.session_state.step = 0
    st.session_state.preferences = {
        "game_preference": [],
        "provider_preference": [],
        "payment_preference": [],
    }

# Define the list of online casinos with affiliate links and logos
casinos = [
    {
        "name": "Betplay.io", 
        "games": ["slots", "poker", "blackjack", "roulette"], 
        "providers": ["No Preference", "Netent", "Microgaming"], 
        "payments": ["crypto"],
        "affiliate_link": "https://betplay.io/?ref=betrlist",
        "logo": "betplay.png"
    },
    {
        "name": "BC.Game", 
        "games": ["roulette", "slots"], 
        "providers": ["No Preference", "Microgaming", "Netent"], 
        "payments": ["crypto", "card"],
        "affiliate_link": "https://bc.game/i-betrlist-n/",
        "logo": "bcgame.png"
    },
    {
        "name": "BitStarz", 
        "games": ["slots", "poker", "roulette"], 
        "providers": ["No Preference", "Playtech", "Microgaming", "Netent"], 
        "payments": ["crypto", "bank", "card"],
        "affiliate_link": "https://bs3.direct/b393c8f59",
        "logo": "bitstarz.png"
    },
    {
        "name": "Pulsz", 
        "games": ["slots", "roulette"], 
        "providers": ["No Preference", "Microgaming", "Playtech", "Netent"], 
        "payments": ["bank", "card"],
        "affiliate_link": "https://www.pulsz.com/?invited_by=xu4qcd",
        "logo": "pulsz.png"
    },
]

# Function to calculate similarity score between user preferences and casino features
def calculate_similarity(user_prefs, casino):
    game_pref = user_prefs["game_preference"]
    provider_pref = user_prefs["provider_preference"]
    payment_pref = user_prefs["payment_preference"]
    
    game_sim = len(set(game_pref).intersection(casino["games"])) / len(game_pref) if game_pref else 0
    provider_sim = len(set(provider_pref).intersection(casino["providers"])) / len(provider_pref) if provider_pref else 0
    payment_sim = len(set(payment_pref).intersection(casino["payments"])) / len(payment_pref) if payment_pref else 0
    
    return np.mean([game_sim, provider_sim, payment_sim])

# Steps to ask questions
if st.session_state.step == 0:
    st.title("AI Casino Finder")
    st.subheader("What style of casino games do you prefer?")
    
    # Display images for game types
    selected_games = image_select(
        label="Choose your favorite styles of casino gameplay",
        images=["slots.png", "poker_image.png", "blackjack.png", "roulette.png"],
        captions=["Slots", "Poker", "Blackjack", "Roulette"],
        multi_select=True
    )
    st.session_state.preferences["game_preference"] = [caption.lower() for caption in selected_games]

    if st.button("Next"):
        st.session_state.step += 1

elif st.session_state.step == 1:
    st.subheader("Select your favorite game provider!")
    
    # Display images for game providers
    selected_providers = image_select(
        label="Select favorite game providers",
        images=["no_preference.png", "netent.png", "microgaming.png", "playtech.png"],
        captions=["No Preference", "Netent", "Microgaming", "Playtech"],
        multi_select=True
    )
    st.session_state.preferences["provider_preference"] = [caption for caption in selected_providers]

    if st.button("Next"):
        st.session_state.step += 1

elif st.session_state.step == 2:
    st.subheader("Which payment option do you prefer?")
    
    # Display images for payment methods
    selected_payments = image_select(
        label="Select favorite payment methods",
        images=["crypto.png", "bank_image.png", "card_image.png"],
        captions=["Crypto", "Bank", "Card"],
        multi_select=True
    )
    st.session_state.preferences["payment_preference"] = [caption.lower() for caption in selected_payments]

    if st.button("Find AI Casino Recommendations"):
        st.session_state.step += 1

# Display the best casinos based on user preferences
if st.session_state.step == 3:
    user_prefs = st.session_state.preferences
    best_casinos = sorted(casinos, key=lambda x: calculate_similarity(user_prefs, x), reverse=True)[:2]
    if best_casinos:
        st.subheader("Based on your preferences, AI recommends the following casino(s):")
        for casino in best_casinos:
            st.image(casino["logo"], width=250)
            st.write(f"**{casino['name']}**")
            # Provide the unique affiliate link for the casino
            st.write(f"[Visit {casino['name']}]({casino['affiliate_link']})")
    else:
        st.subheader("No casinos match your preferences. Please try different options.")
    if st.button("Start Over"):
        st.session_state.step = 0
        st.session_state.preferences = {
            "game_preference": [],
            "provider_preference": [],
            "payment_preference": [],
        }