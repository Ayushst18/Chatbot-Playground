import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq
import time

# Load environment variables
load_dotenv()

# Configure page
st.set_page_config(
    page_title="Chatbot Playground",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Claude-like styling
st.markdown("""
<style>
    /* Main container styling */
    .main > div {
        padding-top: 2rem;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #f8f9fa;
    }
      /* Chat message styling */
    .user-message {
        background-color: #1e3a8a;
        color: white;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border-left: 4px solid #3b82f6;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .assistant-message {
        background-color: #374151;
        color: white;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border-left: 4px solid #9ca3af;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);    }
    
    /* Input area styling */
    .stTextArea > div > div > textarea {
        min-height: 120px;
        border-radius: 8px;
        border: 2px solid #e9ecef;
        font-size: 14px;
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: #0066cc;
        box-shadow: 0 0 0 2px rgba(0, 102, 204, 0.2);
    }
    
    /* JavaScript for Enter key handling */
    .chat-input {
        position: relative;
    }
    
    /* Button styling */
    .stButton > button {
        background-color: #0066cc;
        color: white;
        border-radius: 6px;
        border: none;
        padding: 0.5rem 2rem;
        font-weight: 500;
        transition: all 0.2s;
    }
    
    .stButton > button:hover {
        background-color: #0052a3;
        transform: translateY(-1px);
    }
    
    /* Model selector styling */
    .stSelectbox > div > div {
        border-radius: 6px;
    }
    
    /* Header styling */
    .main-header {
        text-align: center;
        color: #333;
        margin-bottom: 2rem;
    }
    
    /* Settings panel */
    .settings-panel {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 8px;
        border: 1px solid #e9ecef;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Groq client
@st.cache_resource
def init_groq_client():
    return Groq(api_key=os.environ.get("GROQ_API_KEY"))

client = init_groq_client()

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "model" not in st.session_state:
    st.session_state.model = "llama-3.3-70b-versatile"
if "input_key" not in st.session_state:
    st.session_state.input_key = 0

# Sidebar - Model Configuration
with st.sidebar:
    st.markdown("## 🎛️ Model Configuration")
    
    # Model selection
    model_options = {
        "llama-3.3-70b-versatile": "Llama 3.3 70B Versatile",
        "llama-3.1-70b-versatile": "Llama 3.1 70B Versatile", 
        "llama-3.1-8b-instant": "Llama 3.1 8B Instant",
        "mixtral-8x7b-32768": "Mixtral 8x7B",
        "gemma2-9b-it": "Gemma 2 9B"
    }
    
    selected_model = st.selectbox(
        "Model",
        options=list(model_options.keys()),
        format_func=lambda x: model_options[x],
        index=0    )
    st.session_state.model = selected_model
    
    st.markdown("---")
    
    # Chat History
    if st.session_state.messages:
        st.markdown("## 💬 Chat History")
        message_count = len(st.session_state.messages)
        st.metric("Messages", message_count)
        
        # Show word count for conversation
        total_words = sum(len(msg["content"].split()) for msg in st.session_state.messages)
        st.metric("Total Words", total_words)
    
    st.markdown("---")
    
    # Clear conversation button
    if st.button("🗑️ Clear Conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    # Export conversation
    if st.session_state.messages:
        conversation_text = ""
        for msg in st.session_state.messages:
            role = "Human" if msg["role"] == "user" else "Assistant"
            conversation_text += f"{role}: {msg['content']}\n\n"
        
        st.download_button(
            "📄 Export Conversation",
            data=conversation_text,
            file_name="conversation.txt",
            mime="text/plain",
            use_container_width=True
        )

# Main area
st.markdown("<h1 class='main-header'>🤖 Chatbot Playground</h1>", unsafe_allow_html=True)

# Display current model info
st.info(f"**Current Model:** {model_options[st.session_state.model]}")

# Chat history display
chat_container = st.container()

with chat_container:
    if st.session_state.messages:
        for message in st.session_state.messages:
            if message["role"] == "user":
                st.markdown(f"""
                <div class="user-message">
                    <strong style="color: #dbeafe;">👤 You:</strong><br>
                    <span style="color: white;">{message["content"]}</span>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="assistant-message">
                    <strong style="color: #d1d5db;">🤖 Assistant:</strong><br>
                    <span style="color: white;">{message["content"]}</span>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="text-align: center; padding: 3rem; color: #6c757d;">
            <h3>👋 Welcome to the LLM Playground!</h3>
            <p>Start a conversation by typing your message below.</p>
        </div>
        """, unsafe_allow_html=True)

# Input area
st.markdown("---")
input_container = st.container()

# Add JavaScript for Enter key handling
st.markdown("""
<script>
document.addEventListener('DOMContentLoaded', function() {
    function setupEnterKeyHandler() {
        const textArea = document.querySelector('textarea[aria-label="Message"]');
        if (textArea) {
            textArea.addEventListener('keydown', function(e) {
                if (e.key === 'Enter' && !e.shiftKey) {
                    e.preventDefault();
                    const sendButton = document.querySelector('button[kind="primaryFormSubmit"]');
                    if (sendButton && this.value.trim()) {
                        sendButton.click();
                    }
                }
            });
        }
    }
    
    // Setup initially
    setupEnterKeyHandler();
    
    // Setup after Streamlit reruns
    const observer = new MutationObserver(function(mutations) {
        setupEnterKeyHandler();
    });
    
    observer.observe(document.body, {
        childList: true,
        subtree: true
    });
});
</script>
""", unsafe_allow_html=True)

with input_container:
    # Use a form to handle input submission and clearing
    with st.form(key="chat_form", clear_on_submit=True):
        # Create columns for input and button
        col1, col2 = st.columns([4, 1])
        
        with col1:
            user_input = st.text_area(
                "Message",
                placeholder="Type your message here... (Press Enter to send, Shift+Enter for new line)",
                height=120,
                key=f"user_input_{st.session_state.input_key}",
                label_visibility="collapsed"
            )
        
        with col2:
            send_button = st.form_submit_button(
                "Send 📤",
                use_container_width=True,
                type="primary"
            )

# Handle message sending
if send_button and user_input.strip():
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Increment input key to clear the form on next run
    st.session_state.input_key += 1
    
    # Show thinking indicator
    with st.spinner("🤔 Thinking..."):
        try:
            # Prepare messages for API
            api_messages = []
            for msg in st.session_state.messages:
                api_messages.append({
                    "role": msg["role"],
                    "content": msg["content"]                })
            
            # Make API call
            chat_completion = client.chat.completions.create(
                messages=api_messages,
                model=st.session_state.model,
                temperature=0.7,
                max_tokens=2048,
            )
            
            # Get response
            response_content = chat_completion.choices[0].message.content
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response_content})
            
        except Exception as e:
            st.error(f"Error: {str(e)}")
            # Remove the user message if API call failed
            st.session_state.messages.pop()
    
    # Rerun to update the interface
    st.rerun()

# Keyboard shortcut hint
st.markdown("""
<div style="text-align: center; color: #6c757d; font-size: 12px; margin-top: 1rem;">
    💡 Pro tip: Press Enter to send your message, Shift+Enter for new line
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #6c757d; font-size: 12px;">
    Powered by Groq API • Built with Streamlit
</div>
""", unsafe_allow_html=True)
