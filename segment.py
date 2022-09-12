

####################################################################################################
# Naive Cell Segmentation: 
#       Preprocess image
#       K means clustering to assign centroids to nuclei
#       Use centroid locations to construct voronoi diagram 
#       Use voronoi edges as a basis for segmentation
####################################################################################################
# FUCK YOU IM NOT DOING KMEANS
#       Watershed alg. based segmentation
####################################################################################################
import cv2 
import numpy as np

def preprocess(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    average = img.mean(axis=0).mean(axis=0)
    # Invert if image is bright, i.e, if avg > 127.5
    if average > 127.5:
        img = ~img

    return img

def matrix(img):
    img = np.array(img)
    return img


img = preprocess('test_data/test.jpg')
# img = matrix(img)

print(type(img))
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()