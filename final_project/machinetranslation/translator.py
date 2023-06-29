"""Translator module English and French."""
from deep_translator import MyMemoryTranslator

def englishToFrench(english_text):
    """Return string in french."""
    return MyMemoryTranslator('en-GB', 'fr-FR').translate(english_text)

def frenchToEnglish(french_text):
    """Return string in english."""
    return MyMemoryTranslator('fr-FR', 'en-GB').translate(french_text)
