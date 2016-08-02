#!/usr/bin/env python

import numpy as np
from nibabel.testing import data_path
example_filename = os.path.join(data_path, 'example4d.nii.gz')
import nibabel as nib
img = nib.load(example_filename)
img.shape
img.get_data_dtype() == np.dtype(np.int16)
img.affine.shape
data = img.get_data()
type(data)
hdr = img.header
raw = hdr.structarr
array(10, dtype=uint8)

data = np.ones((32, 32, 15, 100), dtype=np.int16)
img = nib.Nifti1Image(data, np.eye(4))
img.get_data_dtype() == np.dtype(np.int16)
img.header.get_xyzt_units()

img.to_filename(os.path.join('build','test4d.nii.gz'))
