import streamlit as st

st.set_page_config(
    page_title="🎖️ Art of War",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inject custom CSS for styling the page and text
st.markdown(
    """
    <style>
    /* Set the background image for the entire app */
    .stApp {
        background: url('https://static.vecteezy.com/system/resources/previews/027/103/278/non_2x/silhouette-soldiers-descend-from-helicopter-warning-of-danger-against-a-sunset-background-with-space-for-text-promoting-peace-and-cessation-of-hostilities-free-photo.jpg')
                no-repeat center center fixed;
        background-size: cover;
    }

    /* Make the sidebar slightly translucent */
    [data-testid="stSidebar"] {
        background-color: rgba(0, 0, 0, 0.6);
    }

    /* Main container for the text to improve readability */
    .content-box {
        background-color: rgba(0, 0, 0, 0.6); /* Semi-transparent black background */
        color: white; /* Set text color to white for contrast */
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        max-width: 800px; /* Set a max-width for better readability on wide screens */
        margin: auto; /* Center the box */
    }
    
    /* Ensure headings are properly spaced */
    .content-box h2, .content-box h3, .content-box h4 {
        margin: 0;
        padding: 0.25em 0;
    }

    /* Style for the list to ensure it's properly aligned */
    .content-box ul {
        list-style-position: inside;
        display: inline-block; /* Allows the list to be centered */
        text-align: left; /* Aligns the text within the list to the left */
        padding-left: 0;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# --- App Content ---

# Main title, centered using HTML
st.markdown("<h1 style='text-align: center;'>🎖️ Art of War</h1>", unsafe_allow_html=True)

# Use a div with the custom class to wrap and style the main text content
st.markdown("""
<div class="content-box">
    <h3>Welcome to</h3>
    <h2>The Military Data Analysis Platform</h2>
    <br>
    <p>Embark on a journey through the unseen dynamics of global defense.</p>
    
    <h4>What you’ll discover:</h4>
    <ul>
        <li><b>Defense Budgets</b> – track spending trends across decades</li>
        <li><b>Military Strength</b> – compare personnel, tanks, aircraft and more</li>
        <li><b>Trade & Alliances</b> – map out import/export flows and partnerships</li>
        <li><b>Hidden Patterns</b> – uncover insights with interactive charts</li>
    </ul>
    <br>
    <p>Dive deep into data and explore the forces shaping our world</p>
    <p>— all in one place!</p>
</div>
""", unsafe_allow_html=True)

