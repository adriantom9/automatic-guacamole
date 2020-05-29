# import the necessary packages
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import imutils
import cv2

# load the image
image = cv2.imread("cita.jpg")

# define the list of boundaries

boundaries = ([0, 80, 0], [100, 255, 100])


lower = np.array(boundaries[0], dtype = "uint8")
upper = np.array(boundaries[1], dtype = "uint8")

# find the colors within the specified boundaries and apply
# the mask
mask = cv2.inRange(image, lower, upper)
output = cv2.bitwise_and(image, image, mask = mask)
naming = "image.jpg"
# show the images
cv2.imwrite(naming, output)

def midpoint(ptA, ptB):
	return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

num = 0
width = 1

# load the image, convert it to grayscale, and blur it slightly
#image2 = cv2.imread("image.jpg")
#image2 = cv2.imread("pokemon_games.png")
image2 = image
gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
cv2.imwrite("grayscale.jpg", gray)
gray = cv2.GaussianBlur(gray, (7, 7), 0)
cv2.imwrite("blur.jpg", gray)

# perform edge detection, then perform a dilation + erosion to
# close gaps in between object edges
edged = cv2.Canny(gray, 50, 100)
cv2.imwrite("canny.jpg", edged)
edged = cv2.dilate(edged, None, iterations=1)
cv2.imwrite("dilate.jpg", edged)
edged = cv2.erode(edged, None, iterations=1)
cv2.imwrite("erode.jpg", edged)

# find contours in the edge map
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
#print(cnts)
cnts = imutils.grab_contours(cnts)
#print(cnts)
# sort the contours from left-to-right and initialize the
# 'pixels per metric' calibration variable
(cnts, _) = contours.sort_contours(cnts)
pixelsPerMetric = None

#cuman buat gambar ajah
# loop over the contours individually
for c in cnts:
	# if the contour is not sufficiently large, ignore it
	if cv2.contourArea(c) < 300:
		continue

	# compute the rotated bounding box of the contour
	orig = image.copy()
	#orig = cv2.imread("graphicdesignlove.jpg")
	box = cv2.minAreaRect(c)
	box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
	box = np.array(box, dtype="int")

	# order the points in the contour such that they appear
	# in top-left, top-right, bottom-right, and bottom-left
	# order, then draw the outline of the rotated bounding
	# box
	box = perspective.order_points(box)
	cv2.drawContours(orig, [box.astype("int")], -1, (0, 255, 0), 2)

	# loop over the original points and draw them
	for (x, y) in box:
		cv2.circle(orig, (int(x), int(y)), 5, (0, 0, 255), -1)

	
    # unpack the ordered bounding box, then compute the midpoint
	# between the top-left and top-right coordinates, followed by
	# the midpoint between bottom-left and bottom-right coordinates
	(tl, tr, br, bl) = box
	(tltrX, tltrY) = midpoint(tl, tr)
	(blbrX, blbrY) = midpoint(bl, br)

	# compute the midpoint between the top-left and top-right points,
	# followed by the midpoint between the top-righ and bottom-right
	(tlblX, tlblY) = midpoint(tl, bl)
	(trbrX, trbrY) = midpoint(tr, br)
	tlbl = (tlblX, tlblY)
	trbr = (trbrX, trbrY)
    
	(cx, cy) = midpoint(tlbl, trbr)
    
	# draw the midpoints on the image
	cv2.circle(orig, (int(tltrX), int(tltrY)), 5, (255, 0, 0), -1)
	cv2.circle(orig, (int(blbrX), int(blbrY)), 5, (255, 0, 0), -1)
	cv2.circle(orig, (int(tlblX), int(tlblY)), 5, (255, 0, 0), -1)
	cv2.circle(orig, (int(trbrX), int(trbrY)), 5, (255, 0, 0), -1)

	# draw lines between the midpoints
	cv2.line(orig, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)),
		(255, 0, 255), 2)
	cv2.line(orig, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)),
		(255, 0, 255), 2)

	# compute the Euclidean distance between the midpoints
	dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
	dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))

	# if the pixels per metric has not been initialized, then
	# compute it as the ratio of pixels to supplied metric
	# (in this case, inches)
	if pixelsPerMetric is None:
		pixelsPerMetric = dB / width

	# compute the size of the object
	dimA = dA / pixelsPerMetric
	dimB = dB / pixelsPerMetric

	# draw the object sizes on the image
	
	cv2.putText(orig, "H = {:.1f}cm".format(dimA),
		(int(cx) + 10, int(cy) - 20), cv2.FONT_HERSHEY_SIMPLEX,
		0.65, (255, 255, 255), 2)
	
	cv2.putText(orig, "W = {:.1f}cm".format(dimB),
		(int(cx) + 10, int(cy) + 20), cv2.FONT_HERSHEY_SIMPLEX,
		0.65, (255, 255, 255), 2)
    

	# show the output image
	
	
	filename = "/var/www/html/object" + str(num) + ".jpg"
	num = num+1
	print(filename)
	cv2.imwrite(filename, orig)
	# cv2.imshow("Image", orig)
	# cv2.waitKey(0)
