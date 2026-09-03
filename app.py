import streamlit as st
from google import genai


# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="AI Content Assistant",
    page_icon="✍️",
    layout="centered"
)


# -----------------------------
# Gemini configuration
# -----------------------------

try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
except Exception:
    GEMINI_API_KEY = None


# -----------------------------
# App title
# -----------------------------

st.title("✍️ AI Content Assistant")

st.write(
    "Create ready-to-publish social media content "
    "with AI."
)


# -----------------------------
# User inputs
# -----------------------------

content_type = st.selectbox(
    "Content Type",
    [
        "Social Media Post",
        "LinkedIn Post",
        "Instagram Caption",
        "X / Twitter Post",
        "Facebook Post",
        "Blog Introduction",
        "Promotional Copy"
    ]
)


platform = st.selectbox(
    "Platform",
    [
        "Instagram",
        "LinkedIn",
        "X / Twitter",
        "Facebook",
        "TikTok",
        "YouTube",
        "General"
    ]
)


topic = st.text_input(
    "Topic",
    placeholder="Example: AI tools for small businesses"
)


target_audience = st.text_input(
    "Target Audience",
    placeholder="Example: startup founders"
)


tone = st.selectbox(
    "Tone",
    [
        "Professional",
        "Friendly",
        "Casual",
        "Inspirational",
        "Educational",
        "Persuasive",
        "Witty",
        "Bold"
    ]
)


# -----------------------------
# Generate content
# -----------------------------

if st.button(
    "Generate Content",
    use_container_width=True
):

    if not topic.strip():
        st.warning("Please enter a topic.")
        st.stop()

    if not target_audience.strip():
        st.warning(
            "Please enter a target audience."
        )
        st.stop()

    if not GEMINI_API_KEY:
        st.error(
            "Gemini API key is not configured."
        )
        st.stop()

    try:
        client = genai.Client(
            api_key=GEMINI_API_KEY
        )

        prompt = f"""
You are an expert social media content writer.

Create high-quality, natural,
ready-to-publish content.

Content Type:
{content_type}

Platform:
{platform}

Topic:
{topic}

Target Audience:
{target_audience}

Tone:
{tone}

Return the answer using exactly this format:

POST:
[Write the complete post here]

CAPTION:
[Write a short engaging caption here]

HASHTAGS:
[Write 8-12 relevant hashtags here]

Important instructions:

- Make the content suitable for the selected platform.
- Write for the specified target audience.
- Follow the requested tone.
- Make the content useful and engaging.
- Do not invent statistics.
- Do not invent studies.
- Do not invent customer results.
- Do not invent fake quotes.
- Keep the content ready to copy and paste.
"""

        with st.spinner(
            "Creating your content..."
        ):
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

        generated_content = response.text

        st.success(
            "Content generated successfully!"
        )

        st.subheader("Generated Content")

        st.text_area(
            "Your content",
            value=generated_content,
            height=500
        )

    except Exception as e:
        st.error(
            f"Something went wrong: {e}"
        )
