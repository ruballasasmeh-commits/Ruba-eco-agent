"""
EcoLoop — sustainability agent (Streamlit version)

Run it from the PyCharm terminal with:
    streamlit run app.py

The whole app (materials, tracker, quiz, Bin Blitz game, read-aloud,
English/Arabic) lives in ecoloop.html. This file shows it full-screen
inside Streamlit.
"""
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="EcoLoop — sustainability agent",
    page_icon="♻️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Remove Streamlit's own header, menu, footer and padding so EcoLoop fills the page
st.markdown(
    """
    <style>
      header[data-testid="stHeader"], #MainMenu, footer {display: none !important;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      [data-testid="stAppViewContainer"] {padding: 0 !important;}
      iframe {border: 0; display: block; width: 100%; height: 100vh !important;}
    </style>
    """,
    unsafe_allow_html=True,
)

HTML_FILE = Path(__file__).parent / "ecoloop.html"


@st.cache_data
def load_html(path: str, modified: float) -> str:
    """Read the app file. `modified` makes Streamlit reload it after you edit it."""
    return Path(path).read_text(encoding="utf-8")


if not HTML_FILE.exists():
    st.error(
        "ecoloop.html is missing. Put it in the same folder as app.py and refresh."
    )
    st.stop()

html = load_html(str(HTML_FILE), HTML_FILE.stat().st_mtime)

# The height here is a fallback; the CSS above stretches the app to the full window.
# New Streamlit versions use st.iframe; older ones use components.html.
if hasattr(st, "iframe"):
    st.iframe(html, height=900)
else:
    import streamlit.components.v1 as components

    components.html(html, height=900, scrolling=True)
