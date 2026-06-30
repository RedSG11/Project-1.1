#------Libraries------
import langcodes
import streamlit as st
from deep_translator import GoogleTranslator
from langdetect import DetectorFactory, LangDetectException, detect
from nltk.tokenize import TreebankWordDetokenizer, wordpunct_tokenize
from spellchecker import SpellChecker

#------Support Lists------
DetectorFactory.seed = 0
min_input_length = 3

# pyspellchecker chỉ hỗ trợ một số ngôn ngữ
SPELL_LANGS = {"en", "es", "fr", "pt", "de", "ru", "ar", "eu", "lv", "nl"}

# Ngôn ngữ đích cho App 1
TARGET_LANGS = {
    "Tiếng Việt": "vi",
    "Tiếng Anh": "en",
    "Tiếng Pháp": "fr",
    "Tiếng Nhật": "ja",
    "Tiếng Trung (Giản thể)": "zh-CN",
    "Tiếng Hàn": "ko",
    "Tiếng Tây Ban Nha": "es",
    "Tiếng Đức": "de",
}

EXAMPLES_T = [
    "Every morning, I drink a cup of coffee.",
    "Bonjour, comment allez-vous?",
    "Xin chào, hôm nay trời đẹp quá.",
]
EXAMPLES_S = [
    "Yesturday, I recieveed a mesage from my freind.",
    "Definately a great oppurtunity.",
    "Je voudraiis allerr au marchee.",
]

#------Support Functions------
@st.cache_resource(show_spinner=False)

def get_spellchecker(lang_code): #Function to load spellchecker model
    return SpellChecker(language=lang_code)

def language_name(lang_code): #Function to translate lang_code (en, vi) to lang_name (English, Vietnamese)
    try:
        return langcodes.Language.get(lang_code).display_name()
    except Exception:
        return lang_code or "Unknown"

def detect_language(raw): #Function to detect the language of raw texts
    try:
        return detect(raw)
    except LangDetectException:
        return None
    
def fix_typos(text, lang_code):
    spell = get_spellchecker(lang_code) 
    words = wordpunct_tokenize(text) #Split text into individual strings and add into a list called words
    fixed = [] #Initialize an empty "fixed" list
    for word in words: #Loop through the words list
        if word.isalpha() and len(word) > 1: #Only fix typo if word is alphabetical and has more than 1 character
            suggestion = spell.correction(word.lower()) or word #Load spellchecker and initialize suggestion
            suggestion = suggestion.title() if word.istitle() else suggestion #If raw word is title, suggestion should be title
            suggestion = suggestion.upper() if word.isupper() else suggestion
            fixed.append(suggestion)
        else:
            fixed.append(word)
    return TreebankWordDetokenizer().detokenize(fixed), fixed != tokens #Special function to reconnect word strings into sentences

#------Main Functions------
def run_translation(text, target_code):
    raw = text.strip()
    if len(raw) < min_input_length:
        return {"Ok": False, "Error": f'Please type at least {min_input_length} characters'}
    source = detect_language(raw)
    if source == target_code:
        return {
            "ok": True,
            "source": language_name(source),
            "target": language_name(target_code),
            "translated": raw,
            "note": "Text has already been in target language" 
        }
    if source is None:
        return {
            "ok": False,
            "error" : "Cannot detect language"
        }
    try:
        translated = GoogleTranslator(source=source, target=target_code).translate(raw)
    except Exception as e:
        return {"ok": False, "error": f"Lỗi dịch: {e}"}
    return {
        "ok": True,
        "source": language_name(source),
        "target": language_name(target_code),
        "translated": translated
    }

def run_spellchecker(text):
    raw = text.strip()
    if len(raw) < min_input_length:
        return {"Ok": False, "Error": f'Please type at least {min_input_length} characters'}
    lang = detect_language(text)
    if lang is None: 
        return {
            "ok": False,
            "error" : "Cannot detect language"
        }
    if lang not in SPELL_LANGS:
        return {
            "ok": False,
            "error": "Unsupported language"
        }
    fixed, changed = fix_typos(raw, lang)
    return {
        "ok": True,
        "language": language_name(lang),
        "fixed": fixed,
        "changed": changed,
    }

#------UI------
st.set_page_config(page_title="NLP Pipeline Demo", layout="centered")
st.title("Streamlit NLP Pipeline Demo")
st.caption("Two applications: Translator • Spelling Checker")
tab_t, tab_s = st.tabs(["Translator", "Spelling Checker"])

#------Tab 1: Translator------
with tab_t:
    st.session_state.setdefault("res_t", None)

    with st.expander("Ví dụ"):
        for ex in EXAMPLES_T:
            st.markdown(f"- {ex}")
    with st.form("form_translate"):
        text_t = st.text_area("Input", height = 90, placeholder="Type texts in any language")
        target = st.selectbox("Translate to:", options = list(TARGET_LANGS.keys()))
        submitted_t = st.form_submit_button("Translate", type = "primary")
    if submitted_t:
        st.session_state.res_t = run_translation(text_t, TARGET_LANGS[target])
    res = st.session_state.res_t
    if res:
        if res["ok"]: #If run_translation has returned "ok": True
            st.caption(f'Source language: {res['source']} -> Target language: {res['target']}') #take 'source' and 'target' from run_translation
            st.success(res['translated']) #take 'translated' from run_translation
            if res.get("note"): #if there is 'note'
                st.info(res["note"]) #take 'note' from run_translation
        else:
            st.warning(res['error'])
