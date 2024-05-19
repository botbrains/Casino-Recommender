import streamlit as st
from streamlit_image_select import image_select

casinos = [
    {
        "name": "Betplay.io", 
        "games": ["slots", "poker", "blackjack", "roulette"],
        "payments": ["crypto", "debit / credit card"],
        "affiliate_link": "https://betplay.io/?ref=betrlist",
        "logo": "betplay.png"
    },
    {
        "name": "BC.Game", 
        "games": ["roulette", "slots"],
        "payments": ["crypto"],
        "affiliate_link": "https://bc.game/i-betrlist-n/",
        "logo": "bcgame.png"
    },
    {
        "name": "BitStarz", 
        "games": ["slots", "poker", "roulette"],
        "payments": ["crypto", "bank transfer", "debit / credit card"],
        "affiliate_link": "https://bs3.direct/b393c8f59",
        "logo": "bitstarz.png"
    },
    {
        "name": "Pulsz", 
        "games": ["slots"],
        "payments": ["bank transfer", "debit / credit card"],
        "affiliate_link": "https://www.pulsz.com/?invited_by=xu4qcd",
        "logo": "pulsz.png"
    },
]

def recommend_casino(games, payments):
    matching_casinos = []
    for casino in casinos:
        if all(game in casino['games'] for game in games) and all(payment in casino['payments'] for payment in payments):
            matching_casinos.append(casino)
    return matching_casinos

st.title("AI Casino Recommender")

# Paginated survey for game preferences
st.sidebar.title("Game Preferences")
game_options = {
    "Slots": "slots.png",
    "Poker": "poker.png",
    "Blackjack": "poker_image.png",
    "Roulette": "roulette.png"
}
selected_games = image_select("Select preferred games", game_options, key="games")

# Paginated survey for payment preferences
st.sidebar.title("Payment Preferences")
payment_options = {
    "Crypto": "crypto.png",
    "Bank Transfer": "bank_image.png",
    "Debit / Credit Card": "card_image.png"
}
selected_payments = image_select("Select preferred payment methods", payment_options, key="payments")

if st.sidebar.button("Find Casinos"):
    recommended = recommend_casino(selected_games, selected_payments)
    if recommended:
        for casino in recommended:
            st.subheader(casino['name'])
            st.write("Games:", ", ".join(casino['games']))
            st.write("Payments:", ", ".join(casino['payments']))
            st.image(casino['logo'], use_column_width=True)
            st.markdown(f"[Visit {casino['name']} now!]({casino['affiliate_link']})")
    else:
        st.write("No matching casinos found.")
