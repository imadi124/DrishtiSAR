import streamlit as st

# Set up the professional page layout and metadata
st.set_page_config(
    page_title="DhristiSAR | Active Development",
    page_icon="🛰️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Header Section
st.title("🛰️ DhristiSAR")
st.subheader("Multimodal SAR-Optical Pipeline for Cloud-Free Disaster Early Warning")

# Status Alert
st.warning("**🚧 System Status: Active Development 🚧**\n\nThe DhristiSAR dashboard is currently under construction. Our backend AI models are currently being trained and integrated.")

st.divider()

# Project Pitch / About Section
st.markdown("### 🌍 The Vision")
st.markdown("""
During critical disasters like the Kerala floods or Assam monsoons, traditional optical satellites are blinded by clouds. **DhristiSAR** bridges this gap. 

By utilizing state-of-the-art **Diffusion Models**, we fuse all-weather SAR (Synthetic Aperture Radar) data with optical imagery to artificially "erase" clouds. These clean images are then fed into deep learning detection models to provide authorities with real-time, all-weather situational awareness.
""")

# Planned Features Grid
st.markdown("### 🚀 Upcoming Features")

col1, col2 = st.columns(2)

with col1:
    st.info("**🌥️ AI Cloud Removal**\n\nFusing Sentinel-1 (SAR) and Sentinel-2 to generate crystal-clear optical maps, regardless of weather.")
    st.error("**🚨 Disaster Detection**\n\nAutomated bounding boxes and alerts for rapidly spreading floods and forest fires.")

with col2:
    st.success("**🗺️ LULC Change Mapping**\n\nHigh-precision 'before-and-after' segmentation maps to track urban and environmental shifts.")
    st.warning("**⏱️ Early Warning System**\n\nTime-series analysis to predict disaster trajectories and generate early warning scores.")

st.divider()

st.markdown("### 🗓️ Expected Timeline")
st.info("**v1 launch: May 2026**")

st.markdown("### 📬 Contact & Links")
st.write("Email: abhayaditya150@gmail.com")
st.markdown("[LinkedIn](https://www.linkedin.com/in/abhayaditya/)")
st.markdown("[GitHub Repository](https://github.com/imadi124/DhristiSAR)")

st.divider()

# Footer
st.caption("Building the future of disaster management. Stay tuned for updates!")
st.caption("Check back soon for the v1.0 release!")