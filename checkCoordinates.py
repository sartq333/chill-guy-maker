import cv2

# Load the image
image = cv2.imread('chillguy.jpeg')

# Display the image in a window
cv2.imshow('Image Window', image)

# Wait for a key press indefinitely or for a specific amount of time (in milliseconds)
cv2.waitKey(0)  # Use 0 to wait indefinitely

# Close all OpenCV windows
cv2.destroyAllWindows()
