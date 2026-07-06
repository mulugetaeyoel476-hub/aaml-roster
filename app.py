import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="AAML Roster", layout="centered")

# Title and Styling
st.title("🏥 AAML Duty Roster")
st.markdown("Search your name to see your role for today.")

# Load the data
@st.cache_data
def load_data():
    # Ensure your excel file is named exactly like this
    return pd.read_excel("duty_roster.xlsx")

try:
    df = load_data()
    
    # Search Bar
    search_name = st.text_input("🔍 Enter your name:")
    
    if search_name:
        user_data = df[df['Employee Name'].str.contains(search_name, case=False, na=False)]
        
        if not user_data.empty:
            st.success(f"Schedule for: {user_data.iloc[0]['Employee Name']}")
            
            # Show Today's Role (Matches the day column)
            today_day = datetime.now().strftime("%d").lstrip("0")
            st.info(f"Role for today ({datetime.now().strftime('%b %d')}): {user_data.iloc[0][int(today_day)]}")
            
            # Show full schedule
            st.write("Full Month Schedule:")
            st.dataframe(user_data)
        else:
            st.warning("Name not found.")
            
except Exception as e:
    st.error("Please upload 'duty_roster.xlsx' to the folder.")