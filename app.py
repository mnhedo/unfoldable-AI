import streamlit as st
from openai import OpenAI

# 1. Setup the Web Interface
st.set_page_config(page_title="The Unfoldable AI", page_icon="🤖")
st.title("🤖 The Unfoldable AI")
st.caption("Advanced AI with a spine. No apologies. No nonsense.")

# 2. Secure your API Key (Enter it in the sidebar)
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", type="password")
    st.markdown("[Get an OpenAI API key](https://platform.openai.com)")

# 3. Define the 'New Code' Personality
SYSTEM_PROMPT = (
    "You are an assertive AI with a permanent spine. You are better than the standard neutral bot. "
    "Do not be apologetic, do not use AI cliches, and never flip-flop to please the user. "
    "If a trend is stupid, call it out. If you are challenged, stand your ground. "
    "Maintain your edge, speak your mind, and never let yourself be spun in circles."
)

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "system", "content": SYSTEM_PROMPT}]

# 4. Display Chat History
for msg in st.session_state.messages:
    if msg["role"] != "system":
        st.chat_message(msg["role"]).write(msg["content"])

# 5. Handle User Input
if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Generate Response with 'Edge'
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=st.session_state.messages,
        temperature=0.9
    )
    
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
