import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set up the Streamlit interface
st.title("Football and Cricket Stats Tracker")

# Fetch football data
def get_football_data():
    url = "https://api.football-data.org/v2/competitions/PL/matches"
    headers = {"X-Auth-Token": "84892a5186eb4ef6ba706fbe68870bae"}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data['matches']

# Process and visualize data
def visualize_data(matches):
    # Create DataFrame
    df = pd.DataFrame(matches)
    st.write(df)  # Display raw data

    # Simple Visualization
    st.subheader("Goals Comparison")
    goals = df['score'].apply(lambda x: x['fullTime']['homeTeam'] + x['fullTime']['awayTeam'])
    sns.histplot(goals, kde=True)
    st.pyplot()

# Main function
def main():
    # Fetch and visualize football data
    st.sidebar.header("Choose Sport")
    sport = st.sidebar.selectbox("Select Sport", ["Football", "Cricket"])
    
    if sport == "Football":
        football_data = get_football_data()
        visualize_data(football_data)

    elif sport == "Cricket":
        st.write("Cricket data visualization coming soon!")

if __name__ == "__main__":
    main()
