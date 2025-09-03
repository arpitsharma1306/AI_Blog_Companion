# ✍️ AI Blog Companion

AI Blog Companion is a **Streamlit-based web app** that helps you create professional blogs along with images.  
It combines **Google Gemini** (for text generation) and **Hugging Face Qwen Image Model** (for image generation) to make blog writing easier and more engaging.

---

## 🌟 Features
- Generate **well-structured blog posts** with a title, keywords, and target word count.
- Create **custom images** for your blog using text prompts.
- Clean **Streamlit interface** with sidebar inputs and live results.
- Outputs blog text in **Markdown format** (headings, lists, highlights).
- Lightweight and easily deployable on **Render**, **Streamlit Cloud**, or other PaaS.

---

## 🚀 Tech Stack
- [Streamlit](https://streamlit.io/) – UI framework  
- [Google Generative AI (Gemini)](https://ai.google.dev/) – Blog text generation  
- [Hugging Face Hub](https://huggingface.co/) – Image generation (Qwen/Qwen-Image)  
- [Python-dotenv](https://pypi.org/project/python-dotenv/) – Environment variable management  
- [Pillow](https://pypi.org/project/Pillow/) – Image handling  

---

## 📦 Installation
Clone the repository:

git clone https://github.com/arpitsharma1306/AI_Blog_Companion.git
cd AI_Blog_Companion
Create a virtual environment (recommended):

python -m venv venv
# Activate it
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
Install dependencies:
pip install -r requirements.txt
🔑 Environment Variables
Create a .env file in the root directory and add your keys:
GOOGLE_API_KEY=your_google_gemini_api_key
HF_TOKEN=your_huggingface_api_token
