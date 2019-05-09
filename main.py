#%%
import cv2
image = cv2.imread("../surse/pic1.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("out.png", gray)
