# PAG
PAG : precision agriculture, is a project uses copernicus satellite images to help the farmer to inspect their lands. The code presentend, crop trnasform to vi's and calculate statiscis.


19/4/2025

in this file i will arrange and store codes and work sample from my old project highlandsystem.
about the project: 


inhalt:
-plot_vi_photo_from_tif:
This code reads a .tif satellite image (e.g., NDVI) using rasterio, then visualizes it using matplotlib and seaborn heatmaps.
It also loads a sample dataset to display a boxplot for basic data visualization with Seaborn.

-raster_ndvi_calclation:
This code extracts specific areas from a satellite image using a shapefile and computes vegetation indices like NDVI or 
NDRE from spectral bands. It saves the results as new GeoTIFF images and visualizes them using matplotlib and rasterio.

-rg_4_ndvi_time_series_from_tiff_:
This code loads a series of NDVI GeoTIFF images, filters out low-quality pixels using thresholding, 
and calculates the mean NDVI values over time. It then visualizes the time series and histograms to analyze vegetation changes in a specific field.

-"test_text_data_extract":
This code extracts structured information such as sensor type, field ID, and date from a list of image filenames by splitting 
the text based on underscores (_). It stores the results in a NumPy array and prints the date component from each filename.

-vi_auto_calculator:
This code automatically calculates several vegetation indices (VIs) such as NDVI, NDRE,
GNDVI, and NGRDI from a multispectral image by identifying required bands and applying their respective formulas. It generates and saves each VI map as a .tiff file, 
and optionally visualizes and exports NDVI as a color-mapped image.

-vi_devlopment_chart_from_tiff's_:
This code processes a series of vegetation index (VI) images (e.g., NDVI or TGI) from a specified field, filters out 
outliers using thresholds, and calculates the mean values over time. It then generates a development chart showing the time series of VI values 
along with histograms for visual analysis.

-cropper v1:
This code processes satellite images by cropping them using shapefiles, extracting statistical data (mean, median, etc.), and calculating vegetation 
indices (like NDVI) for visual and analytical purposes.
It is designed to be executed from the command line, requiring image and shapefile inputs, and produces statistical summaries and processed images.

-photo cropper:
This code processes satellite image cropping using shapefiles. It reads a given shapefile, extracts the geometric shapes, 
and uses them to crop a raster image, saving the cropped result as a new GeoTIFF file.


1. test_text_data_extract
Reason: This script extracts structured information (e.g., sensor type, field ID, date) from filenames, which is typically one of the first steps. It helps organize and label the images that will be processed in subsequent steps.
2. vi_auto_calculator
Reason: After extracting the necessary metadata from the filenames, the next logical step is to automatically calculate vegetation indices (e.g., NDVI, NDRE) from the multispectral images. This is an essential preprocessing step for most vegetation analysis.
3. raster_ndvi_calculation
Reason: This code extracts specific regions of interest from satellite images using shapefiles and computes vegetation indices like NDVI or NDRE. It could be used after calculating indices in the previous step to focus on specific areas (e.g., using the shapefile to crop regions of interest).
4. photo_cropper
Reason: This code is similar to the previous one, but it specifically focuses on cropping the raster image based on the shapefiles. It’s essential to crop the image to focus on the relevant area before doing any detailed analysis.
5. cropper_v1
Reason: This code performs similar cropping and vegetation index calculations but also includes statistical data extraction (e.g., mean, median) for analytical purposes. It would follow the cropping and index calculation steps for further analysis.
6. plot_vi_photo_from_tif
Reason: After processing the images and calculating vegetation indices, it's time to visualize them. This script allows visualization of the vegetation index (e.g., NDVI) with heatmaps and boxplots, providing insights into the data.
7. vi_development_chart_from_tiffs
Reason: This code takes the processed vegetation index images and tracks their development over time, which is typically done after the visualizations. It provides a time series analysis and histograms to track changes and analyze vegetation health.
8. rg_4_ndvi_time_series_from_tiff
Reason: This script handles the analysis of NDVI time series, including filtering low-quality pixels and calculating mean NDVI values over time. It would follow the development chart analysis since it provides a more in-depth, temporal analysis of vegetation changes.

Final Logical Order:

test_text_data_extract


vi_auto_calculator


raster_ndvi_calculation
photo_cropper


cropper_v1


plot_vi_photo_from_tif


vi_development_chart_from_tiffs


rg_4_ndvi_time_series_from_tiff


This sequence progresses logically from extracting and organizing data, calculating vegetation indices, cropping images, visualizing data, and finally analyzing the time series of vegetation indices.
