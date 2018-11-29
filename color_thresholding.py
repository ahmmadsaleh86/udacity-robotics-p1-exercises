# Import some packages from matplotlib
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

# Define a function to perform a color threshold
def color_thresh(img, rgb_thresh=(0, 0, 0)):
    ####### TODO
    # Create an empty array the same size in x and y as the image
        # but just a single channel
    binary_image = np.zeros((img.shape[0], img.shape[1]))
    # Apply the thresholds for RGB and
        # assign 1's where threshold was exceeded
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            if (img[i][j] >= rgb_thresh).all():
                binary_image[i][j] = 1
    return binary_image

if __name__=="__main__":
    # Define the filename, read and plot the image
    filename = 'D:\\udacity_robotics\\IMG\\robocam_2018_10_22_03_04_38_989.jpg'
    image = mpimg.imread(filename)
    print(image.dtype, image.shape, np.min(image), np.max(image))

    # Define color selection criteria
    ###### TODO: MODIFY THESE VARIABLES TO MAKE YOUR COLOR SELECTION
    red_threshold = 160
    green_threshold = 160
    blue_threshold = 160
    ######
    rgb_threshold = (red_threshold, green_threshold, blue_threshold)
    # pixels below the thresholds
    colorsel = color_thresh(image, rgb_thresh=rgb_threshold)

    # Display
    plt.imshow(colorsel)
    plt.show()




