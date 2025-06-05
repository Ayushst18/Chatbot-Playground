# 🤖 Chatbot Playground

A modern, Claude-style chatbot interface built with Streamlit and powered by Groq's lightning-fast LLM API. Experience seamless conversations with state-of-the-art language models in an intuitive, web-based playground.

![Chatbot Playground](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-FF6B35?style=for-the-badge&logo=groq&logoColor=white)

## ✨ Features

- 🎨 **Claude-inspired UI** - Clean, modern interface with dark-themed chat bubbles
- ⚡ **Multiple LLM Models** - Choose from Llama 3.3, Llama 3.1, Mixtral, and Gemma models
- 🎛️ **Advanced Controls** - Adjust temperature, max tokens, and system prompts
- ⌨️ **Keyboard Shortcuts** - Press Enter to send, Shift+Enter for new lines
- 💾 **Export Conversations** - Download chat history as text files
- 🔄 **Auto-clearing Input** - Input field clears automatically after sending
- 📱 **Responsive Design** - Works seamlessly on desktop and mobile devices
- 🚀 **Lightning Fast** - Powered by Groq's optimized inference infrastructure

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Groq API key (get one free at [console.groq.com](https://console.groq.com))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/chatbot-playground.git
   cd chatbot-playground
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   # source .venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

5. **Run the application**
   ```bash
   streamlit run streamlit_app.py
   ```

6. **Open your browser** and navigate to `http://localhost:8501`

## 🎮 Usage

### Basic Chat
1. Select your preferred LLM model from the sidebar
2. Type your message in the input area
3. Press **Enter** to send or **Shift+Enter** for new lines
4. Enjoy conversing with the AI!

### Advanced Features
- **Temperature Control**: Adjust response creativity (0.0 = deterministic, 2.0 = very creative)
- **Max Tokens**: Control response length
- **System Prompts**: Define the AI's personality and behavior
- **Export Chat**: Download conversation history as a text file
- **Clear History**: Reset the conversation at any time

## 🔧 Configuration

### Available Models
- **Llama 3.3 70B Versatile** - Latest and most capable
- **Llama 3.1 70B Versatile** - Excellent for complex reasoning
- **Llama 3.1 8B Instant** - Fast responses for quick interactions
- **Mixtral 8x7B** - Great balance of speed and quality
- **Gemma 2 9B** - Efficient and reliable

### Environment Variables
| Variable | Description | Required |
|----------|-------------|----------|
| `GROQ_API_KEY` | Your Groq API key | Yes |

## 📁 Project Structure

```
chatbot-playground/
├── streamlit_app.py      # Main Streamlit application
├── main.py              # Original CLI version
├── requirements.txt     # Python dependencies
├── .env                # Environment variables (create this)
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## 🛠️ Development

### Running in Development Mode
```bash
streamlit run streamlit_app.py --server.runOnSave true
```

### Key Components

- **Chat Interface**: Real-time conversation display with styled message bubbles
- **Model Configuration**: Sidebar controls for model selection and parameters
- **Session Management**: Persistent chat history during the session
- **Input Handling**: Form-based input with keyboard shortcuts
- **Export Functionality**: Download conversations as text files

## 🎨 Customization

### Styling
The interface uses custom CSS for Claude-like styling. You can modify the appearance by editing the CSS in `streamlit_app.py`:

```python
st.markdown("""
<style>
    .user-message {
        background-color: #1e3a8a;  # Customize colors
        color: white;
        # ... more styles
    }
</style>
""", unsafe_allow_html=True)
```

### Adding New Models
To add new Groq models, update the `model_options` dictionary in `streamlit_app.py`:

```python
model_options = {
    "new-model-name": "Display Name",
    # ... existing models
}
```

## 🚀 Deployment

### Streamlit Cloud
1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Add your `GROQ_API_KEY` in the secrets section
5. Deploy!

### Local Network Access
```bash
streamlit run streamlit_app.py --server.address 0.0.0.0
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io) for the amazing web app framework
- [Groq](https://groq.com) for providing fast LLM inference
- [Anthropic](https://anthropic.com) for inspiration from Claude's interface design

---

⭐ If you found this project helpful, please consider giving it a star on GitHub!
