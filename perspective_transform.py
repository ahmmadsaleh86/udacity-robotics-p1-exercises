import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import  numpy as np
import cv2


def getPerspectiveImage(img, src, des):
    M = cv2.getPerspectiveTransform(src, des)

    result = cv2.warpPerspective(img, M, (img.shape[1], img.shape[0]))

    return result


if __name__ == "__main__":

    # Define the filename, read and plot the image
    filename = 'example_grid1.jpg'
    image = mpimg.imread(filename)

    src = np.float32([
        [14, 140],
        [301, 140],
        [199, 96],
        [118, 96]
    ])

    des = np.float32([
        [image.shape[1]/2 - 5, image.shape[0] - 10],
        [image.shape[1] / 2 + 5, image.shape[0] - 10],
        [image.shape[1] / 2 + 5, image.shape[0] - 20],
        [image.shape[1]/2 - 5, image.shape[0] - 20]
    ])

    perspectiveImage = getPerspectiveImage(image, src, des)


    # Display
    plt.imshow(perspectiveImage)
    plt.show()