import streamlit as st
import requests
import time

st.set_page_config(
    page_title="LLM Translator",
    layout="wide"
)

ip_api = "api"
port_api = "5000"

st.markdown("""
<style>
.header {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 20px;
}
.translation-info {
    color: #1e88e5;
    font-size: 14px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

LANGUAGES = {
    "English": "English",
    "Spanish": "Spanish",
    "French": "French",
    "German": "German",
    "Russian": "Russian",
    "Chinese": "Chinese",
    "Japanese": "Japanese"
}

st.markdown('<p class="header">LLM Translator</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    from_lang = st.selectbox(
        "From",
        options=list(LANGUAGES.keys()),
        key="from_lang",
        index=0
    )

with col2:
    to_lang = st.selectbox(
        "To",
        options=list(LANGUAGES.keys()),
        key="to_lang",
        index=4  # Russian по умолчанию
    )

source_text = st.text_area(
    "Text to translate",
    height=200,
    placeholder="Type or paste your text here...",
    key="input_text"
)

# Кнопка перевода
if st.button("Translate", key="translate_btn", use_container_width=True):
    if source_text:
        start_time = time.time()
        with st.spinner("Translating..."):
            try:
                response = requests.post(
                    f"http://{ip_api}:{port_api}/translate",
                    json={
                        "text": source_text,
                        "source_language": LANGUAGES[from_lang],
                        "target_language": LANGUAGES[to_lang]
                    },
                    timeout=60
                )
                
                if response.status_code == 200:
                    result = response.json()
                    translation_time = round(time.time() - start_time, 2)
                    
                    st.markdown(f"""
                    <div class="translation-info">
                        Translated in {translation_time}s
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.text_area(
                        "Translation",
                        value=result["translation"],
                        height=200,
                        key="output_text",
                        disabled=True
                    )
                else:
                    st.error(f"Translation error: {response.json().get('detail', 'Unknown error')}")
                    
            except requests.exceptions.RequestException as e:
                st.error(f"Connection error: {str(e)}")
            except Exception as e:
                st.error(f"Unexpected error: {str(e)}")
    else:
        st.warning("Please enter text to translate")

# Добавим сообщение, если API не доступен
try:
    requests.get(f"http://{ip_api}:{port_api}/health", timeout=2)
except:
    st.warning("Translation API is not available. Please make sure the API server is running")