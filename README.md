# ✍️ AI Content Assistant

An AI-powered content generation assistant built with **Python, Streamlit, and Google Gemini API**.

The application helps users quickly create platform-ready content by selecting a content type, social media platform, target audience, and writing tone. Gemini generates a complete post along with an engaging caption and relevant hashtags.

## 🚀 Features

* 📝 Select different content types
* 📱 Choose the target social media platform
* 🎯 Define your target audience
* 🎨 Select the desired writing tone
* 🤖 Generate AI-powered content using Google Gemini
* 📄 Generate a complete ready-to-publish post
* 💬 Generate an engaging caption
* #️⃣ Generate relevant hashtags
* ⚡ Simple and clean Streamlit interface
* 🔐 API key stored securely using Streamlit Secrets
* ☁️ Deployable on Streamlit Community Cloud
* 📦 GitHub-ready project

## 🛠️ Technology Stack

* **Python** — Application programming language
* **Streamlit** — User interface
* **Google Gemini API** — AI content generation
* **Google Colab** — Development and testing
* **GitHub** — Source code and version control
* **Cloudflare** — Domain/DNS management

## 📂 Project Structure

```text
ai-content-assistant/
│
├── app.py
├── requirements.txt
└── README.md
```

## ⚙️ Supported Content Types

The application currently supports:

* Social Media Post
* LinkedIn Post
* Instagram Caption
* X / Twitter Post
* Facebook Post
* Blog Introduction
* Promotional Copy

## 📱 Supported Platforms

Users can generate content for:

* Instagram
* LinkedIn
* X / Twitter
* Facebook
* TikTok
* YouTube
* General platforms

## 🎨 Available Tones

Users can choose from:

* Professional
* Friendly
* Casual
* Inspirational
* Educational
* Persuasive
* Witty
* Bold

## 🔑 Gemini API Setup

This project uses the Google Gemini API for content generation.

Create your Gemini API key using Google AI Studio:

https://aistudio.google.com/

**Never put your API key directly inside `app.py` or upload it to GitHub.**

For Streamlit Community Cloud, add your key through the application's **Secrets** settings:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

The application reads the key using:

```python
st.secrets["GEMINI_API_KEY"]
```

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-content-assistant.git
```

### 2. Open the project

```bash
cd ai-content-assistant
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure your Gemini API key

For local development, configure your Streamlit secret:

```text
.streamlit/
└── secrets.toml
```

Add:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

**Do not commit `secrets.toml` to GitHub.**

Add it to `.gitignore`:

```text
.streamlit/secrets.toml
venv/
__pycache__/
```

### 6. Start the application

```bash
streamlit run app.py
```

The application will normally be available at:

```text
http://localhost:8501
```

## ☁️ Deployment

The application can be deployed using **Streamlit Community Cloud**.

Basic deployment process:

1. Upload the project to GitHub.
2. Open Streamlit Community Cloud.
3. Connect your GitHub account.
4. Select the `ai-content-assistant` repository.
5. Select the `main` branch.
6. Set `app.py` as the main file.
7. Add `GEMINI_API_KEY` under Streamlit Secrets.
8. Deploy the application.

## 🔒 Security

The Gemini API key should always remain private.

Do not:

* Put the API key inside `app.py`
* Commit the API key to GitHub
* Share the API key publicly
* Put the API key in frontend JavaScript

Use Streamlit Secrets for production deployments.

## 🔄 How It Works

The application follows a simple workflow:

```text
User
  │
  ▼
Streamlit UI
  │
  ├── Content Type
  ├── Platform
  ├── Topic
  ├── Target Audience
  └── Tone
  │
  ▼
Python Application
  │
  ▼
Google Gemini API
  │
  ▼
Generated Content
  │
  ├── Complete Post
  ├── Caption
  └── Hashtags
  │
  ▼
User
```

## 📌 Example

### User Input

```text
Content Type: LinkedIn Post
Platform: LinkedIn
Topic: AI tools for small businesses
Target Audience: Small business owners
Tone: Professional
```

### AI Output

```text
POST:
Generated LinkedIn post...

CAPTION:
Generated engaging caption...

HASHTAGS:
#AI #SmallBusiness #Technology #Entrepreneurship
```

## 🔮 Future Improvements

Possible future features include:

* 🌍 Multiple language support
* 📏 Short, medium, and long content options
* 🔄 Regenerate content button
* 📋 One-click copy buttons
* 💾 Content history
* 📊 Content scoring
* 🎯 More audience/persona options
* 🖼️ AI image generation
* 📅 Content calendar
* 📤 Export content to PDF or TXT
* 🔐 User authentication
* 🗄️ Database for saved posts

## 🤝 Contributing

Contributions are welcome.

To contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Push the branch.
6. Create a pull request.

## 📄 License

This project is available for educational and personal use. Add an appropriate open-source license if you plan to distribute the project publicly.

---

### Built With ❤️

**Python + Streamlit + Google Gemini**
