import streamlit as st
from PIL import Image
import time
import requests
import io

st.set_page_config(page_title="Face Recognition (Mock)", layout="wide")

st.markdown("""
<h1 style='text-align:center; font-family: Poppins, sans-serif; color:#0b2545'>Face Recognition — Mock Mode</h1>
<p style='text-align:center; color:#1f2937'>This is a mock runner that skips native face libraries so the UI can be inspected.</p>
""", unsafe_allow_html=True)

col1, col2 = st.columns([2,1])

with col1:
    st.subheader("Live Camera (Mock)")
    # Use a placeholder image to represent camera feed
    placeholder = st.image(Image.new('RGB', (640, 480), color=(30,30,30)))
    st.caption("Camera feed is mocked — replace with real camera when native libs are available.")

with col2:
    st.subheader("Controls")
    run = st.checkbox("Simulate Face Detection", value=True)
    st.markdown("**Detected People**")
    detected = st.empty()
    if run:
        detected.write("- Alice\n- Bob\n- Unknown")
    else:
        detected.write("(not running)")

st.markdown("---")
st.subheader("Missing Persons (fetched from backend)")

backend_url = st.text_input("Backend URL", value="http://localhost:5000/api/missingpeople/getallpersons")
if st.button("Fetch from backend"):
    try:
        r = requests.get(backend_url, timeout=5)
        r.raise_for_status()
        data = r.json()
        for person in data:
            name = person.get('name') or person.get('Name') or person.get('name', 'Unknown')
            st.write(f"**{name}** — {person.get('address','')}")
            imgdata = person.get('image') or person.get('imageData') or None
            # if backend returns binary image blob as base64 or bytes, skip here
    except Exception as e:
        st.error(f"Failed to fetch: {e}")

st.write("\n---\n")
st.caption("Mock mode: no native face libraries are imported. To enable full detection, run the original app with a Python environment that has `face_recognition`/`dlib` installed.")
