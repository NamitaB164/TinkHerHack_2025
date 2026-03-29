# ✨ Chatty: Magical Stories & Friendship for Little Explorers

**Chatty** is a therapeutic AI-powered application designed specifically to support and entertain **hospitalized children**. By combining the power of Google's Gemini AI with a soothing, magical interface, Chatty provides emotional support, creative distraction, and a friendly companion during challenging times.

---

## 💜 Our Mission
Hospital stays can be lonely and scary for children. Chatty was built to:
- **Inspire Imagination**: Generate endless, unique stories across various genres.
- **Provide Companionship**: A supportive AI friend that's always ready to chat and cheer them up.
- **Create a Safe Space**: A kid-friendly interface with gentle colors and interactive magic.

---

## 🚀 Features

### 📖 The Story Teller
A magical library where children can choose their own adventure!
- **Genres**: Fantasy, Mystery, Dreams, Adventure, and Fairytales.
- **AI-Powered**: Generates unique, moral-driven stories in real-time.
- **Read-to-Me**: Integrated Text-to-Speech (TTS) so children can close their eyes and listen.

### 👾 My Friend (Chatbot)
A cheerful AI companion powered by **Gemini 3 Flash**.
- **Playful Personality**: Uses emojis and encouraging language.
- **Supportive**: Ready to tell jokes, share fun facts, or just listen.
- **Kid-Safe**: Designed with strict system instructions for simple, positive interactions.

### 🎨 Premium UI/UX
- **Purple-Lavender Theme**: Soft, calming colors tailored for a supportive environment.
- **Glassmorphism**: Modern, sleek cards with translucent effects.
- **Magic Wand Effects**: Sparkle and particle animations on every interaction.
- **Floating Particles**: Drifting magical shapes to make the screen feel alive.

---

## 🛠️ Technical Setup

### Prerequisites
- Python 3.10+
- A Google Gemini API Key

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/NamitaB164/TinkHerHack_2025.git
   cd TinkHerHack_2025
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Create a `.env` file in the root directory (refer to `.env.example`):
   ```env
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

5. **Run the Application**:
   ```bash
   python manage.py runserver
   ```
   Visit `http://127.0.0.1:8000` to begin the magic!

---

## 📂 Project Structure
- `core/`: Main Django settings and URL configurations.
- `storytelling_app/`: The AI Story Generator and reader view.
- `chatbot_app/`: The supportive AI friend chat interface.
- `templates/`: Global layout and landing pages.
- `static/`: Global CSS, JS, and asset files.

---

## 💎 Credits & Support
Made with 💜 for the **TinkHerHack 2025** hackathon. 

---
*“Because every child deserves a little magic, even in a hospital bed.”* ✨
