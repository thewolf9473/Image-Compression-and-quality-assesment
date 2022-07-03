# -*- coding: utf-8 -*-
"""Image Compression and quality assesment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10otJRtexhWx4jpMZXif3o0zxoqhruqRq

Dependencies and Libraries
"""

import numpy
from PIL import Image

!wget https://d8it4huxumps7.cloudfront.net/files/62babe062492f_images.zip  ##Source for the image dataset(Here 15 High Quality images)

!unzip 62babe062492f_images.zip -d data

!pip install image-quality

import imquality.brisque as brisque
from skimage import io, img_as_float

"""**Image** **Quality** **Assessment** **Using** **Brisque**"""

img = img_as_float(io.imread('/content/data/Images/sample1.jpg', as_gray=True))
score=brisque.score(img)
print(score)

"""**Image** **Compression**

Using SVD For image compression
If A is the matrix of the original image then using SVD we have
A=UEV
U= unitary matrix
E= Rectangular Diagonal Matrix
V= Unitary Matrix
"""

def openImage(imagePath):
    imOrig = Image.open(imagePath)
    im = numpy.array(imOrig)

    aRed = im[:, :, 0]
    aGreen = im[:, :, 1]
    aBlue = im[:, :, 2]

    return [aRed, aGreen, aBlue, imOrig]

def compressSingleChannel(channelDataMatrix, singularValuesLimit):
    uChannel, sChannel, vhChannel = numpy.linalg.svd(channelDataMatrix)
    aChannelCompressed = numpy.zeros((channelDataMatrix.shape[0], channelDataMatrix.shape[1]))
    k = singularValuesLimit

    leftSide = numpy.matmul(uChannel[:, 0:k], numpy.diag(sChannel)[0:k, 0:k])
    aChannelCompressedInner = numpy.matmul(leftSide, vhChannel[0:k, :])
    aChannelCompressed = aChannelCompressedInner.astype('uint8')
    return aChannelCompressed

aRed, aGreen, aBlue, originalImage = openImage('/content/data/Images/sample10.jpg') ##Enter The Path of your Image(One At a time)

imageWidth = 512
imageHeight = 512

singularValuesLimit = 160

aRedCompressed = compressSingleChannel(aRed, singularValuesLimit)
aGreenCompressed = compressSingleChannel(aGreen, singularValuesLimit)
aBlueCompressed = compressSingleChannel(aBlue, singularValuesLimit)

imr = Image.fromarray(aRedCompressed, mode=None)
img = Image.fromarray(aGreenCompressed, mode=None)
imb = Image.fromarray(aBlueCompressed, mode=None)

newImage = Image.merge("RGB", (imr, img, imb))
newImage.save('/content/compressed/new10.jpg')

mr = imageHeight
mc = imageWidth

originalSize = mr * mc * 3
compressedSize = singularValuesLimit * (1 + mr + mc) * 3

"""**Image Size Comparrison of Both the images**"""

print('original size:')
print(originalSize)

print('compressed size:')
print(compressedSize)

print('Ratio compressed size / original size:')
ratio = compressedSize * 1.0 / originalSize
print(ratio)

print('Compressed image size is ' + str(round(ratio * 100, 2)) + '% of the original image ')

"""**Brisque for the Compressed Image**"""

img = img_as_float(io.imread('/content/compressed/new.jpg', as_gray=True))
score=brisque.score(img)
print(score)

