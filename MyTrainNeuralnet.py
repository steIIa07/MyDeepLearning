import numpy as np
import os
import cv2

data_dir = "./MyDeepLearning/dataset/cat_dog/"

print(data_dir)

catImgs = []
dogImgs = []

img = cv2.imread(data_dir + "cat.0.jpg")
catImgs.append(img)
img = cv2.imread(data_dir + "dog.0.jpg")
dogImgs.append(img)


# for file in os.listdir(data_dir):
#     img_path = os.path.join(data_dir, file)
#     img = cv2.imread(img_path)

#     if file.startswith("cat"):
#         catImgs.append(file)
#     elif file.startswith("dog"):
#         dogImgs.append(file)

cv2.imshow("cat", catImgs[0])
cv2.imshow("dog", dogImgs[0])