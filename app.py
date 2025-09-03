import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
from huggingface_hub import InferenceClient
from PIL import Image
from io import BytesIO

# ------------------- LOAD ENVIRONMENT VARIABLES -------------------
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
HF_TOKEN = os.getenv("HF_TOKEN")

if not GOOGLE_API_KEY or not HF_TOKEN:
    st.error("❌ Missing API keys. Please set GOOGLE_API_KEY and HF_TOKEN in a .env file or environment.")
    st.stop()
    
# ------------------- STREAMLIT PORT FIX -------------------
port = int(os.environ.get("PORT", "8080"))
os.environ["STREAMLIT_SERVER_PORT"] = str(port)
os.environ["STREAMLIT_SERVER_ADDRESS"] = "0.0.0.0"

# ------------------- CONFIGURE CLIENTS -------------------
# Configure Gemini client
genai.configure(api_key=GOOGLE_API_KEY)

# Hugging Face inference client (Qwen Image model)
client = InferenceClient(
    provider="fal-ai",
    api_key=HF_TOKEN,
)

# ------------------- STREAMLIT PAGE SETTINGS -------------------
st.set_page_config(
    layout="wide",
    page_title="BlogCraft AI",
    page_icon="✍️"
)

st.title("✍️ BlogCraft: AI Blog Writer + Image Generator")
st.subheader("Create compelling blogs with text (Gemini) + images (Qwen)")

# ------------------- BLOG GENERATION -------------------
@st.cache_data
def generate_blog(title: str, keywords: str, num_words: int) -> str:
    prompt = (
        f"Generate a professional, well-structured blog post with title '{title}' "
        f"and keywords '{keywords}'. Around {num_words} words. "
        f"Use markdown formatting (headings, bullet points)."
    )
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        resp = model.generate_content(prompt)
        return resp.text or "⚠️ No text returned."
    except Exception as e:
        st.error(f"Blog generation error: {e}")
        return ""

# ------------------- IMAGE GENERATION -------------------
def generate_image(img_prompt: str, index: int = 0) -> str | None:
    try:
        image = client.text_to_image(
            img_prompt,
            model="Qwen/Qwen-Image",
        )
        file_name = f"generated_image_{index}.png"
        image.save(file_name)
        return file_name
    except Exception as e:
        st.warning(f"Image {index+1} failed: {e}")
        return None

# ------------------- SIDEBAR -------------------
with st.sidebar:
    st.title("📝 Blog Inputs")
    blog_title = st.text_input("Blog Title", placeholder="e.g., The Future of Renewable Energy")
    keywords = st.text_area("Keywords", placeholder="e.g., solar, wind, sustainability")
    num_words = st.slider("Word Count", 250, 1500, 600, 50)
    num_images = st.slider("Number of Images", 0, 3, 1, 1)
    image_prompt = st.text_area("Image Prompt", placeholder="e.g., A modern illustration of solar panels and wind turbines")
    submit = st.button("✨ Generate Blog ✨", type="primary")

# ------------------- MAIN EXECUTION -------------------
if submit:
    if not blog_title:
        st.error("Please enter a blog title.")
    else:
        st.header(f"✒️ Blog: {blog_title}")

        # Generate images
        if num_images > 0 and image_prompt.strip():
            st.subheader("🖼️ Generated Images")
            for i in range(num_images):
                with st.spinner(f"Creating image {i+1}/{num_images}..."):
                    img_path = generate_image(image_prompt, i)
                    if img_path:
                        st.image(img_path, use_container_width=True)

        # Generate blog
        with st.spinner("Crafting your blog..."):
            blog = generate_blog(blog_title, keywords, num_words)
        st.markdown(blog)
