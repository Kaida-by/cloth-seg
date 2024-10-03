!git clone https://github.com/Kaida-by/cloth-seg.git

import zipfile
import os
import time

from google.colab import drive
from PIL import Image

drive.mount('/content/drive/')

cd cloth-seg/

zip_file = '/content/drive/My Drive/imaterialist-fashion-2020-fgvc7.zip'

z = zipfile.ZipFile(zip_file, 'r')
z.extractall()

!python train.py