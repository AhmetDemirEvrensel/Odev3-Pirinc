import cv2
import numpy as np

image = cv2.imread("odev3/pirincc.jpg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, thresholded_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)

kernel = np.ones((5, 5), np.uint8)

erosion = cv2.erode(thresholded_image, kernel, iterations=1)

dilation = cv2.dilate(erosion, kernel, iterations=1)

_, labels, stats, centroids = cv2.connectedComponentsWithStats(dilation)

rice_count = len(stats) - 1 
print(f"Pirinç Sayısı: {rice_count}")

# Görüntüleri göster
cv2.imshow("Original Image", image)
cv2.imshow("Thresholded Image", thresholded_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
