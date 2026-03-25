import streamlit as st
from PIL import Image, ImageOps

# Set up the professional page layout and metadata
st.set_page_config(
    page_title="DrishtiSAR | Active Development",
    page_icon="🛰️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Header Section
st.title("🛰️ DrishtiSAR")
st.subheader("Multimodal SAR-Optical Pipeline for Cloud-Free Disaster Early Warning")

# Status Alert
st.warning("**🚧 System Status: Active Development 🚧**\n\nThe DrishtiSAR dashboard is currently under construction. Our backend AI models are currently being trained and integrated.")

st.divider()

# Project Pitch / About Section
st.markdown("### 🌍 The Vision")
st.markdown("""
During critical disasters like the Kerala floods or Assam monsoons, traditional optical satellites are blinded by clouds. **DrishtiSAR** bridges this gap. 

By utilizing state-of-the-art **Diffusion Models**, we fuse all-weather SAR (Synthetic Aperture Radar) data with optical imagery to artificially "erase" clouds. These clean images are then fed into deep learning detection models to provide authorities with real-time, all-weather situational awareness.
""")

# Planned Features Grid
st.markdown("### 🚀 Upcoming Features")

def load_feature_image(path, size=(900, 520)):
    img = Image.open(path).convert("RGB")
    return ImageOps.fit(img, size, method=Image.Resampling.LANCZOS)

cards = [
    {
        "icon": "🌥️",
        "title": "AI Cloud Removal",
        "desc": "Fusing Sentinel-1 (SAR) and Sentinel-2 to generate crystal-clear optical maps, regardless of weather.",
        "img": "assets/images/cloud removal.jpg",
    },
    {
        "icon": "🗺️",
        "title": "LULC Change Mapping",
        "desc": "High-precision 'before-and-after' segmentation maps to track urban and environmental shifts.",
        "img": "assets/images/LULC change.jpg",
    },
    {
        "icon": "🚨",
        "title": "Disaster Detection",
        "desc": "Automated bounding boxes and alerts for rapidly spreading floods and forest fires.",
        "img": "assets/images/disaster_detection.png",
    },
    {
        "icon": "⏱️",
        "title": "Early Warning System",
        "desc": "Time-series analysis to predict disaster trajectories and generate early warning scores.",
        "img": "assets/images/time-series analysis.jpg",
    },
]

for i in range(0, len(cards), 2):
    col1, col2 = st.columns(2)
    for col, card in zip([col1, col2], cards[i:i+2]):
        with col:
            with st.container(border=True):
                st.markdown(f"**{card['icon']} {card['title']}**")
                st.image(load_feature_image(card["img"]), use_container_width=True)
                st.write(card["desc"])

st.divider()

st.markdown("### 🗓️ Expected Timeline")
st.info("**v1 launch: May 2026**")

st.markdown("### 📬 Contact & Links")
st.write("Email: abhayaditya150@gmail.com")
st.markdown("[LinkedIn](https://www.linkedin.com/in/abhayaditya/)")
st.markdown("[GitHub Repository](https://github.com/imadi124/DrishtiSAR)")

st.divider()

# Footer
st.caption("Building the future of disaster management. Stay tuned for updates!")
st.caption("Check back soon for the v1.0 release!")