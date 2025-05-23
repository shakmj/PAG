Here's a clean and properly formatted version of your README file in Markdown for GitHub:

```markdown
# PAG: Precision Agriculture Project

**Date**: 19/04/2025

**PAG (Precision Agriculture)** is a project that utilizes Copernicus satellite images to help farmers inspect their lands. The code presented here transforms crop imagery into vegetation indices (VIs) and calculates statistical data for analysis.

This repository also includes code samples and work from the older `HighlandSystem` project.

---

## 📁 Project Contents

### 1. `test_text_data_extract`
- Extracts structured metadata such as sensor type, field ID, and date from image filenames.
- Useful for organizing and labeling image data.
- **Reason**: This is typically the first step in the workflow.

---

### 2. `vi_auto_calculator`
- Automatically calculates several VIs (NDVI, NDRE, GNDVI, NGRDI) from multispectral images.
- Identifies required bands, applies formulas, saves maps as `.tiff`, and optionally visualizes NDVI.
- **Reason**: Follows metadata extraction to generate VIs for analysis.

---

### 3. `raster_ndvi_calculation`
- Extracts regions of interest from satellite images using shapefiles.
- Computes NDVI or NDRE from spectral bands.
- Saves outputs as new GeoTIFFs and visualizes with `matplotlib`.
- **Reason**: Performed after VI calculation to focus on areas of interest.

---

### 4. `photo_cropper`
- Crops raster images using shapefiles.
- Extracts geometry from shapefiles and saves cropped results as GeoTIFFs.
- **Reason**: Essential for isolating relevant regions before analysis.

---

### 5. `cropper_v1`
- Similar to `photo_cropper` with additional statistical analysis (mean, median, etc.).
- Designed for command-line use; accepts image and shapefile inputs.
- Outputs include processed images and statistical summaries.
- **Reason**: Used after cropping and index calculations for in-depth analytics.

---

### 6. `plot_vi_photo_from_tif`
- Reads a `.tif` satellite image (e.g., NDVI) using `rasterio`.
- Visualizes with `matplotlib` and `seaborn` (heatmaps and boxplots).
- Loads sample dataset for comparison.
- **Reason**: Used after image processing to visualize results.

---

### 7. `vi_development_chart_from_tiffs`
- Processes a series of VI images (e.g., NDVI, TGI).
- Filters outliers and calculates mean VI values over time.
- Produces development charts and histograms.
- **Reason**: Provides visual temporal analysis of vegetation changes.

---

### 8. `rg_4_ndvi_time_series_from_tiff`
- Loads NDVI time series from GeoTIFFs.
- Filters low-quality pixels using thresholds.
- Computes mean NDVI over time and visualizes with time series and histograms.
- **Reason**: Final step in temporal analysis pipeline.

---

## 🧠 Logical Workflow

1. `test_text_data_extract`
2. `vi_auto_calculator`
3. `raster_ndvi_calculation`
4. `photo_cropper`
5. `cropper_v1`
6. `plot_vi_photo_from_tif`
7. `vi_development_chart_from_tiffs`
8. `rg_4_ndvi_time_series_from_tiff`

This sequence flows logically from:
- Data extraction
- Vegetation index calculation
- Image cropping
- Visualization
- Time series analysis

---

## 🌱 Goal

To support precision farming by analyzing satellite imagery, calculating vegetation indices, and visualizing crop health trends over time.

---

## 🛰️ Tools & Libraries

- `rasterio`
- `matplotlib`
- `seaborn`
- `numpy`
- Shapefiles / GeoTIFF
```

Let me know if you want to add screenshots, usage examples, or a `requirements.txt` section.
