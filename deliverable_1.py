from matplotlib import pyplot as plt
import matplotlib.image as mpimg
from PIL import Image



image = mpimg.imread('/media/Bozu.png')

#changes image to redscale
def redify(img):
  R, G, B = img[:,:,1], img[:,:,0], img[:,:,0]
  imgRed = 255 * R + 0 * G + 0 * B
  plt.imshow(imgRed, cmap='Reds_r')
  return imgRed


#changes image to greenscale
def greenify(img):
  R, G, B = img[:,:,0], img[:,:,1], img[:,:,0]
  imgGreen = 0 * R + 255 * G + 0 * B
  plt.imshow(imgGreen, cmap='Greens_r')
  return imgGreen

#changes image to bluescale
def blueify(img):
  R, G, B = img[:,:,0], img[:,:,0], img[:,:,1]
  imgBlue = 0 * R + 255 * G + 0 * B
  plt.imshow(imgBlue, cmap='Blues_r')
  return imgBlue

#changes image to grayscale
def grayify(img):
  R, G, B = img[:,:,0], img[:,:,1], img[:,:,2]
  imgGray = 0.2989 * R + 0.5870 * G + 0.1140 * B
  plt.imshow(imgGray, cmap='gray')
  return imgGray

#returns images
redify(image)
plt.show()
blueify(image)
plt.show()
greenify(image)
plt.show()
grayify(image)
plt.show()