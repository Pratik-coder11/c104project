import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, "Sun", (20,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))

cv2.putText(img, "Mercury", (265,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Venus", (339,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Earth", (415,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Mars", (485,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Jupiter", (570,255), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Saturn", (720,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Uranus", (992,288), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Neptune", (1130,288), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))



cv2.imshow("Solar System", img)
cv2.waitKey(5000)

cv2.imwrite("Solar_system_with_name.jpg", img)

cv2.destroyAllWindows()
