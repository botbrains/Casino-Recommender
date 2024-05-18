import streamlit as st

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

st.sidebar.title("Preferences")

games = st.sidebar.multiselect("Select preferred games", options=["slots", "poker", "blackjack", "roulette"])

payments = st.sidebar.multiselect("Select preferred payment methods", options=["crypto", "bank transfer", "debit / credit card"])

if st.sidebar.button("Find Casinos"):
    recommended = recommend_casino(games, payments)
    if recommended:
        for casino in recommended:
            st.subheader(casino['name'])
            st.write("Games:", ", ".join(casino['games']))
            st.write("Payments:", ", ".join(casino['payments']))
            st.image(casino['logo'], use_column_width=True)
            st.markdown(f"[Visit {casino['name']} now!]({casino['affiliate_link']})")
    else:
        st.write("No matching casinos found.")
