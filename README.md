# 🧠 ATHENA - An AI Assistant GUI App

ATHENA is a Python-based AI assistant with a graphical user interface built using Kivy. It uses Mistral's powerful large language model to provide interactive, intelligent responses in a chat format.

---

## ✨ Features

- 🖥️ Graphical chat interface using Kivy  
- 🤖 AI responses powered by Mistral's LLM  
- 💬 Maintains session-based chat history  
- 🎨 Colored message styling (user vs assistant)  
- 🔁 Ability to reset context via keyword  

---

## 🗂️ Project Structure

```
athena-assistant/
├── main_application.py   # Main Kivy app logic
├── time_.py              # Mistral AI backend logic
├── assistant.kv          # Kivy GUI layout file
```

---

## 🚀 Installation & Setup

### 1. Clone this repository

```bash
git clone https://github.com/your-username/athena-assistant.git
cd athena-assistant
```

### 2. Install all required Python modules

Just copy and paste this:

```bash
pip install kivy mistralai
```

If Kivy throws errors, refer to the official guide for your OS:  
👉 https://kivy.org/doc/stable/gettingstarted/installation.html

---

## 🔐 API Key Setup

1. Go to [https://mistral.ai/](https://mistral.ai/) and sign up.
2. Get your API key.
3. Open the file `time_.py` and replace this line:

```python
api_key = "your_actual_api_key_here"
```

Put your API key inside the quotes.

---

## ▶️ Running the App

After setup, launch the app with:

```bash
python main_application.py
```

This will open the ATHENA assistant GUI window.

---

## 🧠 Future Improvements

- 🔐 Environment variable for API key  
- 🧏‍♂️ Voice input/output  
- 💾 Persistent memory  
- 🌗 Dark/light theme toggle  
- 📱 Mobile UI via KivyMD  

---

## 🙋 Contact

For questions or suggestions, open an issue on this repository.

