import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import  numpy as np
import cv2

def recognize_rock(img, lower, upper):
    # Convert BGR to HSV
    #hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Threshold the HSV image to get only blue colors
    #mask = cv2.inRange(hsv, lower, upper)
    binary = np.zeros((img.shape[0], img.shape[1]))

    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            if (img[i][j] >= lower).all() and (img[i][j] <= upper).all():
                binary[i][j] = 1

    return binary

if __name__=="__main__":
    # Define the filename, read and plot the image
    filename = 'D:\\udacity_robotics\\IMG\\robocam_2018_10_22_03_05_21_134.jpg'
    image = mpimg.imread(filename)

    # define range of rock color in HSV
    lower = (145, 123, 0)
    upper = (223, 232, 86)

    mask = recognize_rock(image, lower, upper)

    print(mask)
    plt.imshow(mask, cmap='gray')
    #plt.imshow(image)
    plt.show()