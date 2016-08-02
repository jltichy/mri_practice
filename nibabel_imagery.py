#!/usr/bin/env python

# This is an introduction to nibabel from the site: http://nipy.org/nibabel/nibabel_images.html

#Import these two lines before you run this program.
#sudo pip install setuptools --upgrade
#sudo pip install nibabel

import os
import numpy as np

from nibabel.testing import data_path
example_file = os.path.join(data_path, 'example4d.nii.gz')

import nibabel as nib
img = nib.load(example_file)

img
img.dataobj

# Set numpy to print only 2 decimal digits for neatness
np.set_printoptions(precision=2, suppress=True)
img.affine

img.header
header = img.header
print(header)     

print(header.get_data_shape())

# Use: get_data_dtype() to get the numpy data type in which the image data is stored (or will be stored if you save the image):
print(header.get_data_dtype())

#Use: get_zooms() to get the voxel sizes in millimeters:
print(header.get_zooms())

img.dataobj
nib.is_proxy(img.dataobj)

array_data = np.arange(24, dtype=np.int16).reshape((2, 3, 4))
affine = np.diag([1, 2, 3, 1])
array_img = nib.Nifti1Image(array_data, affine)
array_img.dataobj
array_img.dataobj is array_data
nib.is_proxy(array_img.dataobj)

image_data = array_img.get_data()
image_data.shape
image_data is array_data
image_data = img.get_data()
image_data.shape
img.dataobj
data_again = img.get_data()
data_again is image_data

nib.save(array_img, 'my_image.nii')
img_again = nib.load('my_image.nii')
img_again.shape
array_img.to_filename('my_image_again.nii')
img_again = nib.load('my_image_again.nii')
img_again.shape
img_again.set_filename('another_image.nii')
img_again.get_filename()
