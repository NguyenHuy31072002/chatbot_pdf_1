import uuid
import streamlit as st

# Tạo session ID
def get_session_id():
    if 'session_id' not in st.session_state:
        st.session_state['session_id'] = str(uuid.uuid4())
    return st.session_state['session_id']

# Xóa lịch sử chat
def clear_chat_history():
    session_id = get_session_id()
    st.session_state[session_id]['messages'] = [{"role": "assistant", "content": "Upload some PDFs or DOCs and ask me a question."}]
