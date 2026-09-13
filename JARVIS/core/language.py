# core/language.py
"""Utility functions for language handling in JARVIS.

Provides a canonical mapping from language codes to Kokoro TTS voice prefixes
and a helper to select an appropriate voice based on the desired language.
This module is deliberately lightweight and has no external dependencies.
"""

# Mapping of language codes to Kokoro voice prefixes.
# The prefix is the first part of a Kokoro voice name (e.g. "hf_" for Hindi).
LANGUAGE_VOICE_PREFIX = {
    "en": "a",   # American English (e.g., af_*, am_*) – default
    "hi": "h",   # Hindi (e.g., hf_*, hm_*)
    # Additional languages can be added here in the future.
}

def voice_prefix_for_language(lang: str) -> str:
    """Return the Kokoro voice prefix for a given language code.

    Args:
        lang: ISO‑639‑1 language code (e.g., "en", "hi").

    Returns:
        The prefix string used by Kokoro voice identifiers. Falls back to
        "a" (English) if the language is unknown.
    """
    if not isinstance(lang, str):
        return "a"
    lang_code = lang.strip().lower()
    return LANGUAGE_VOICE_PREFIX.get(lang_code, "a")

def voice_for_language(lang: str, base_voice: str = "af_heart") -> str:
    """Construct a full Kokoro voice name matching the desired language.

    The *base_voice* is expected to be in the form "<prefix>_<suffix>".
    The function replaces the prefix with the appropriate language prefix
    while preserving the suffix.

    Args:
        lang: Target language code (e.g., "en" or "hi").
        base_voice: Existing voice name from configuration.

    Returns:
        A voice name suitable for ``KokoroTTSEngine``.
    """
    prefix = voice_prefix_for_language(lang)
    suffix = base_voice.split("_", 1)[1] if "_" in base_voice else base_voice
    return f"{prefix}_{suffix}"
