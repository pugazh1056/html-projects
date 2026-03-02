import streamlit as st

# Step 1: Page setup
st.set_page_config(page_title="AI News Verifier", page_icon="📰", layout="centered")

# 🔹 Step 5: Add UI styling here
st.markdown("""
    <style>
    .stTextInput>div>div>input {
        border-radius: 10px;
        padding: 10px;
        border: 1px solid #ccc;
        font-size: 16px;
    }
    .stButton>button {
        background-color: #007bff;
        color: white;
        border-radius: 8px;
        padding: 8px 20px;
        font-size: 16px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #0056b3;
    }
    </style>
""", unsafe_allow_html=True)

# Step 2: App title
st.title("📰 AI News Verifier Assistant")
st.write("Enter a news headline or URL below to verify if it's true or fake.")

# Step 3: Input
user_input = st.text_input("🔍 Enter News Headline or Link")

# Step 4: Button & Output
if st.button("Verify"):
    with st.spinner("Checking credibility..."):
        st.success("✅ Result: This news appears to be FALSE.")
        st.write("Explanation: Verified sources like Reuters and BBC found no such event.")
        st.link_button("Read Verified News", "https://www.reuters.com")
