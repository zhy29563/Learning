import numpy as np
import cv2 as cv

# Returns true if the specified image can be decoded by OpenCV.
# retval	=	cv.haveImageReader(	filename	)
retval = cv.haveImageReader('lena.png')
print(retval)

# Returns true if an image with the specified filename can be encoded by OpenCV.
# retval	=	cv.haveImageWriter(	filename	)
retval = cv.haveImageWriter('lena.png')
print(retval)

# Reads an image from a buffer in memory.
# The function imdecode reads an image from the specified buffer in the memory. 
# If the buffer is too short or contains invalid data, the function returns an empty matrix ( Mat::data==NULL ).
# In the case of color images, the decoded images will have the channels stored in B G R order.
f = open('lena.png' , 'rb+')
buffer = f.read()
f.close()

image = np.asarray(bytearray(buffer), dtype="uint8")
image = cv.imdecode(image, cv.IMREAD_COLOR)
cv.imshow('lena',image)
cv.waitKey()

# Encodes an image into a memory buffer.
# The function imencode compresses the image and stores it in the memory buffer that is resized to fit the result. 
# See cv::imwrite for the list of supported formats and flags description.
# retval, buf = cv.imencode(ext, img[, params])
# Parameters
#   ext	    File extension that defines the output format.
#   img	    Image to be written.
#   buf	    Output buffer resized to fit the compressed image.
#   params	Format-specific parameters. See cv::imwrite and cv::ImwriteFlags.
retval, buf = cv.imencode('.png', image, params=None)
print(retval)

# Loads an image from a file.
# The function imread loads an image from the specified file and returns it.
# If the image cannot be read (because of missing file, improper permissions, unsupported or invalid format),
# the function returns an empty matrix ( Mat::data==NULL ).
# retval	=	cv.imread(	filename[, flags]	)

# Currently, the following file formats are supported:
#   Windows bitmaps - *.bmp, *.dib (always supported)
#   JPEG files - *.jpeg, *.jpg, *.jpe (see the Note section)
#   JPEG 2000 files - *.jp2 (see the Note section)
#   Portable Network Graphics - *.png (see the Note section)
#   WebP - *.webp (see the Note section)
#   Portable image format - *.pbm, *.pgm, *.ppm *.pxm, *.pnm (always supported)
#   PFM files - *.pfm (see the Note section)
#   Sun rasters - *.sr, *.ras (always supported)
#   TIFF files - *.tiff, *.tif (see the Note section)
#   OpenEXR Image files - *.exr (see the Note section)
#   Radiance HDR - *.hdr, *.pic (always supported)
#   Raster and Vector geospatial data supported by GDAL (see the Note section)
retval = cv.imread('lena.png')

'''
    ☯ The function determines the type of an image by the content, not by the file extension.
    ☯ In the case of color images, the decoded images will have the channels stored in B G R order.
    ☯ When using IMREAD_GRAYSCALE, the codec's internal grayscale conversion will be used, if available. 
       Results may differ to the output of cvtColor()
    ☯ On Microsoft Windows* OS and MacOSX*, the codecs shipped with an OpenCV image (libjpeg, libpng, libtiff, and libjasper) are used by default.
       So, OpenCV can always read JPEGs, PNGs, and TIFFs. On MacOSX, there is also an option to use native MacOSX image readers. 
       But beware that currently these native image loaders give images with different pixel values because of the color management embedded into MacOSX.
    ☯ On Linux*, BSD flavors and other Unix-like open-source operating systems, OpenCV looks for codecs supplied with an OS image. 
       Install the relevant packages (do not forget the development files, for example, "libjpeg-dev", in Debian* and Ubuntu*) to get the codec support or turn on the OPENCV_BUILD_3RDPARTY_LIBS flag in CMake.
    ☯ In the case you set WITH_GDAL flag to true in CMake and IMREAD_LOAD_GDAL to load the image, then the GDAL driver will be used in order to decode the image, supporting the following formats: Raster, Vector.
    ☯ If EXIF information is embedded in the image file, the EXIF orientation will be taken into account and thus the image will be rotated accordingly except if the flags IMREAD_IGNORE_ORIENTATION or IMREAD_UNCHANGED are passed.
    ☯ Use the IMREAD_UNCHANGED flag to keep the floating point values from PFM image.
    ☯ By default number of pixels must be less than 2^30. Limit can be set using system variable OPENCV_IO_MAX_IMAGE_PIXELS
'''
# ImreadModes
'''
cv.IMREAD_UNCHANGED
    If set, return the loaded image as is (with alpha channel, otherwise it gets cropped). Ignore EXIF orientation.

cv.IMREAD_GRAYSCALE
    If set, always convert image to the single channel grayscale image (codec internal conversion).

cv.IMREAD_COLOR
    If set, always convert image to the 3 channel BGR color image.

cv.IMREAD_ANYDEPTH
    If set, return 16-bit/32-bit image when the input has the corresponding depth, otherwise convert it to 8-bit.

cv.IMREAD_ANYCOLOR
    If set, the image is read in any possible color format.

cv.IMREAD_LOAD_GDAL
    If set, use the gdal driver for loading the image.

cv.IMREAD_REDUCED_GRAYSCALE_2
    If set, always convert image to the single channel grayscale image and the image size reduced 1/2.

cv.IMREAD_REDUCED_COLOR_2
    If set, always convert image to the 3 channel BGR color image and the image size reduced 1/2.

cv.IMREAD_REDUCED_GRAYSCALE_4
    If set, always convert image to the single channel grayscale image and the image size reduced 1/4.

cv.IMREAD_REDUCED_COLOR_4
    If set, always convert image to the 3 channel BGR color image and the image size reduced 1/4.

cv.IMREAD_REDUCED_GRAYSCALE_8
    If set, always convert image to the single channel grayscale image and the image size reduced 1/8.

cv.IMREAD_REDUCED_COLOR_8
    If set, always convert image to the 3 channel BGR color image and the image size reduced 1/8.

cv.IMREAD_IGNORE_ORIENTATION
    If set, do not rotate the image according to EXIF's orientation flag.
'''

# Loads a multi-page image from a file.
# The function imreadmulti loads a multi-page image from the specified file into a vector of Mat objects.
# 	retval, mats	=	cv.imreadmulti(	filename[, mats[, flags]]	)
# Parameters
#   filename	Name of file to be loaded.
#   flags	    Flag that can take values of cv::ImreadModes, default with cv::IMREAD_ANYCOLOR.
#   mats	    A vector of Mat objects holding each page, if more than one.
retval, mats = cv.imreadmulti('lena.png')
print(type(mats))
