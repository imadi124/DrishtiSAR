# 🛰️ DhristiSAR: Multimodal SAR-Optical Diffusion Pipeline

**DhristiSAR** is an AI-powered satellite imagery pipeline designed for cloud-free disaster early warning and Land Use/Land Cover (LULC) change detection. 

During heavy monsoons or natural disasters, crucial optical satellite imagery is often blocked by clouds. This project aims to solve that by fusing all-weather SAR data (Sentinel-1) with optical data (Sentinel-2/Cartosat) using advanced Diffusion Models to generate clean, cloud-free imagery. This clean data is then processed to detect disasters and map land changes in real-time.

### 🚧 Project Status: Active Development 🚧
*This project is currently in the research and development phase. The architecture and features outlined below represent the planned roadmap.*

### 🌍 Core Vision
* **AI-Powered Cloud Eraser:** Utilizing cutting-edge Diffusion Models to translate SAR signals into accurate, cloud-free optical representations.
* **Automated Disaster Detection:** Deploying YOLOv8/U-Net architectures to instantly identify floods, forest fires, and structural damage.
* **LULC Change Mapping:** Generating clear "before-and-after" segmentation maps to track environmental and urban changes.
* **Early Warning Insights:** Analyzing time-series data to predict disaster spread (e.g., flood expansion) and issue automated alerts.

### 🛠️ Planned Tech Stack
* **Data Sources:** Sentinel-1 (SAR), Sentinel-2 / ISRO Cartosat (Optical)
* **AI/ML:** PyTorch, Hugging Face Diffusers, Ultralytics (YOLOv8), Segmentation Models
* **Geospatial Processing:** Rasterio, GeoPandas
* **Frontend:** Streamlit

---
*Built to empower all-weather, real-time disaster management.*

### 🛠️ Contribution
Contributions to DhristiSAR are highly encouraged. Whether it is code improvements, bug fixes, documentation updates, or feature enhancements, feel free to contribute to the project repository.

### 📜 License
DhristiSAR is licensed under the MIT License, granting you the freedom to use, modify, and distribute the code in accordance with the terms of the license.
