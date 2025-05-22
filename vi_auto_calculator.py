# -*- coding: utf-8 -*-
"""VI auto calculator.ipynb


comment by:30/4/25: 
vi_auto_calculator:
This code automatically calculates several vegetation indices (VIs) such as NDVI, NDRE,
GNDVI, and NGRDI from a multispectral image by identifying required bands and applying their respective formulas. It generates and saves each VI map as a .tiff file, 
and optionally visualizes and exports NDVI as a color-mapped image.

"""

#install raterio evrey time.
!pip install rasterio
!pip install fiona

#import the libraries to 
# calculate VIs :
import rasterio
from   rasterio import plot
import matplotlib.pyplot as plt
import numpy as np

#function use to extract available bands of a photo:
def extract_bands_name(name):
  b = name.split('B')
  bs = b[1:]
  #split_bands
  bands_s=[]
  first_b = [char for char in bs[0]]
  for char in bs[0]:
    bands_s.append(char)

  for i in range(len(bs)-1):
    bands_s.append(bs[i+1])
  return bands_s

# what is the role of this function                 ??????
def vi_cal_v2(photo,n_vi,save_name,nameOfphoto):
  #DECLARE refrence DATA:
  vi_dep_numberMode = {"ndvi":["8","4"],"ndre":["8","5"],"gndvi":["8","3"],"tgi":["3","4","2"],"ngrdi":["3","4"],"msavi":["8","4"],}
  depAck = True
  # 1) check that the photo contain the needed bands:
  # 2) extract the photo bands>>
  photo_bands = extract_bands_name(nameOfphoto)
  # what is the desiered vi,what's needed vi:
  dep_bands = vi_dep_numberMode[n_vi]
  for b in(dep_bands):
    if b not in photo_bands :
      depAck = False
      print("dependent band missed : " ,str(b))
      return("dependent band missed : "+str(b))
  # if  we reach this point it's OK >>> now let's calculate VI.
  B_n = [photo_bands.index(dep_bands[0])+1,photo_bands.index(dep_bands[1])+1]
  # pull the formula,get desired bands (m,n)

  ##run the formula  :::
  ch1_n = photo.read(B_n[1]).astype('float64')#-b
  ch2_m = photo.read(B_n[0]).astype('float64')#+b
  #ndvi calculation, empty cells or nodata cells are reported as 0
  vi=np.where(
    (ch2_m+ch1_n)==0.,
    0,
    (ch2_m-ch1_n)/(ch2_m+ch1_n))
  vi[:5,:5]
  ## create the vi map :::
  viImage = rasterio.open('/content/'+save_name+'.tiff','w',driver='Gtiff',
                          width=photo.width,
                          height = photo.height,
                          count=1, crs=photo.crs,
                          transform=photo.transform,
                          dtype='float64')
  # save map::
  viImage.write(vi,1)
  viImage.close()

## requiest vi's for one photo.
## u need photo,vi,savename ,nameof photo
pic_id = "/content/Nawa-rg4_9-2-2022_B234589.tif"
photo = rasterio.open(pic_id) 
# what is the next variable vi>?
vi = ["ndre","gndvi","ngrdi","ndvi"]

# what is the role of the next for>???
for g in vi:
  save_id = "Nawa-rg4_10-1-2022_"+ g
  vi_cal_v2(photo,"ndvi",save_id,pic_id)



#Plot vi map section.

for h in(vi):
  pic_path = "Nawa-rg4_9-2-2022_"+h # what is h??
  vi_photo = rasterio.open('/content/'+pic_path+'.tiff')
  #fig = plt.figure(figsize=(18,12),cmap ="Reds")               do we need it?
  plt.figure(1)
  plt.imshow(vi_photo.read(1), cmap='Reds')
  #plot.show(vi_photo)
  plt.savefig('/content/ndre.png')

# Allow division by zero
numpy.seterr(divide='ignore', invalid='ignore')

# Calculate NDVI
ndvi = (band_nir.astype(float) - band_red.astype(float)) / (band_nir + band_red)

# Set spatial characteristics of the output object to mirror the input
kwargs = src.meta
kwargs.update(
    dtype=rasterio.float32,
    count = 1)

# Create the file
with rasterio.open('ndvi.tif', 'w', **kwargs) as dst:
        dst.write_band(1, ndvi.astype(rasterio.float32))

import matplotlib.pyplot as plt
plt.imsave("ndvi_cmap.png", ndvi, cmap=plt.cm.summer)