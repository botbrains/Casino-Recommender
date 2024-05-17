import streamlit as st

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
        "name": "Casino A", 
        "games": ["slots", "poker", "blackjack"], 
        "providers": ["NetEnt", "Microgaming"], 
        "payments": ["crypto", "card"],
        "affiliate_link": "https://affiliate.example.com/casinoA"
    },
    {
        "name": "Casino B", 
        "games": ["roulette", "slots"], 
        "providers": ["Playtech"], 
        "payments": ["bank", "card"],
        "affiliate_link": "https://affiliate.example.com/casinoB"
    },
    {
        "name": "Casino C", 
        "games": ["poker", "roulette"], 
        "providers": ["NetEnt"], 
        "payments": ["crypto", "bank"],
        "affiliate_link": "https://affiliate.example.com/casinoC"
    },
    {
        "name": "Casino D", 
        "games": ["blackjack", "slots"], 
        "providers": ["Microgaming", "Playtech"], 
        "payments": ["crypto", "bank", "card"],
        "affiliate_link": "https://affiliate.example.com/casinoD"
    },
]

# Function to filter casinos based on user preferences
def filter_casinos(casinos, preferences):
    filtered_casinos = []
    for casino in casinos:
        if preferences["game_preference"] in casino["games"] and preferences["payment_preference"] in casino["payments"]:
            if preferences["provider_preference"] == "No Preference" or preferences["provider_preference"] in casino["providers"]:
                filtered_casinos.append(casino)
    return filtered_casinos

# Steps to ask questions
if st.session_state.step == 0:
    st.title("Find Your Best Online Casino")
    st.subheader("What type of games do you play?")
    
    # Display images for game types
    st.image("slots.png", caption="Slots", width=100)
    st.image("poker.png", caption="Poker", width=100)
    st.image("poker.png", caption="Blackjack", width=100)
    st.image("roulette.png", caption="Roulette", width=100)
    
    st.session_state.preferences["game_preference"] = st.radio(
        "Select a game type", 
        ["slots", "poker", "blackjack", "roulette"]
    )
    if st.button("Next"):
        st.session_state.step += 1

elif st.session_state.step == 1:
    st.subheader("Are you looking for a specific game provider?")
    
    # Display images for game providers
    st.image("no_preference_image.png", caption="No Preference", width=100)
    st.image("netent.png", caption="NetEnt", width=100)
    st.image("microgaming.png", caption="Microgaming", width=100)
    st.image("playtech.png", caption="Playtech", width=100)
    
    st.session_state.preferences["provider_preference"] = st.radio(
        "Select a game provider", 
        ["No Preference", "NetEnt", "Microgaming", "Playtech"]
    )
    if st.button("Next"):
        st.session_state.step += 1

elif st.session_state.step == 2:
    st.subheader("What payment options do you prefer?")
    
    # Display images for payment methods
    st.image("crypto_image.png", caption="Crypto", width=100)
    st.image("bank_image.png", caption="Bank", width=100)
    st.image("card_image.png", caption="Card", width=100)
    
    st.session_state.preferences["payment_preference"] = st.radio(
        "Select a payment method", 
        ["crypto", "bank", "card"]
    )
    if st.button("Find Best Casino"):
        st.session_state.step += 1

# Display the best casinos based on user preferences
if st.session_state.step == 3:
    best_casinos = filter_casinos(casinos, st.session_state.preferences)
    if best_casinos:
        st.subheader("Based on your preferences, we recommend the following casino(s):")
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
