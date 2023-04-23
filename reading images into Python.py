""" 
reading images into Python and its conversion using scikit-image
scikit-image: pip install scikit-image

"""

from skimage import io
img_int = io.imread('om.jpg')   #reading image
print (img_int.shape)           #shape or dimension of image (y,x,z)
 

from  skimage import img_as_float   # convert integer image into float image
img_float = img_as_float(img_int)

from skimage import img_as_ubyte    # convert float image into byte
img_byte = img_as_ubyte(img_float)

""" 
reading images into Python and its conversion using opencv
opencv: pip install opencv-python
"""
import cv2
img_cv2 = cv2.imread('om.jpg') # color image
#BGR instead of RGB
grey_img= cv2.imread('om.jpg', 0)  # gray scale image

img_BGR_RGB = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2RGB) # convert BGR to RGB

