import streamlit as st
import pandas as pd
import os

CHAT_DATA_FILE = 'chatdata.csv'

# Initialize chat history and data in session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'chat_data_df' not in st.session_state:
    if os.path.exists(CHAT_DATA_FILE):
        st.session_state.chat_data_df = pd.read_csv(CHAT_DATA_FILE)
    else:
        st.session_state.chat_data_df = pd.DataFrame(columns=['user_input', 'response_msg'])

st.title('Simple Streamlit Chatbot')

# Display chat messages from history on app rerun
for message in st.session_state.chat_history:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# React to user input
if prompt := st.chat_input('Say something...'):
    # Display user message in chat message container
    st.chat_message('user').markdown(prompt)
    # Add user message to chat history
    st.session_state.chat_history.append({'role': 'user', 'content': prompt})

    # Prepare response
    bot_response = ''
    user_input_lower = prompt.lower()
    
    # Check if input exists in our chat data
    if user_input_lower in st.session_state.chat_data_df['user_input'].str.lower().values:
        response_row = st.session_state.chat_data_df[st.session_state.chat_data_df['user_input'].str.lower() == user_input_lower].iloc[0]
        bot_response = response_row['response_msg']
    else:
        bot_response = "I'm sorry, I don't understand that. Could you teach me what to say?"
        # For a full 'learning' mechanism, you would need another input field or button here
        # For now, we'll just acknowledge and maybe add a placeholder to teach
        # You can add a button to 'Teach me' and then use st.text_input to get the response
        # For this example, we'll just add the new input with a placeholder response if not taught
        
        # Add new user input to data if it's not already there (case-insensitive check)
        if user_input_lower not in st.session_state.chat_data_df['user_input'].str.lower().values:
            new_row = pd.DataFrame([{'user_input': prompt, 'response_msg': '[NOT_TAUGHT_YET]'}])
            st.session_state.chat_data_df = pd.concat([st.session_state.chat_data_df, new_row], ignore_index=True)
            st.session_state.chat_data_df.to_csv(CHAT_DATA_FILE, index=False)


    # Display assistant response in chat message container
    with st.chat_message('assistant'):
        st.markdown(bot_response)
    # Add assistant response to chat history
    st.session_state.chat_history.append({'role': 'assistant', 'content': bot_response})

st.markdown("---<")
st.markdown("### Debug Info (for teaching the bot)")

with st.expander("Teach the bot new responses"): # Expander for teaching
    st.write("If the bot didn't understand, you can update its response here. Find the `[NOT_TAUGHT_YET]` entries.")
    
    edited_df = st.data_editor(st.session_state.chat_data_df, num_rows="dynamic")
    
    if not st.session_state.chat_data_df.equals(edited_df):
        st.session_state.chat_data_df = edited_df
        st.session_state.chat_data_df.to_csv(CHAT_DATA_FILE, index=False)
        st.success("Chat data updated and saved!")
        st.experimental_rerun()