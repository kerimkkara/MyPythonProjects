import cv2
import glob
import os 


i=0
inputFolder = ('games')
os.mkdir("gamesresized")
for img in glob.glob(inputFolder + "/*.png"):
    i+=1
    image = cv2.imread(img)
    imageresized = cv2.resize(image, (250,250))
    cv2.imwrite("gamesresized/"+ "/image%04i.webp" %i, imageresized)
    cv2.waitKey(30)
