import langcodes
import streamlit as st
from deep_translator import GoogleTranslator
from langdetect import DetectorFactory, LangDetectException, detect
from nltk.tokenize import TreebankWordDetokenizer, wordpunct_tokenize
from spellchecker import SpellChecker

DetectorFactory.seed = 0
MIN_INPUT_LENGTH = 3

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
