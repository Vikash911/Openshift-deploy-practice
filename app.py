# app.py
import cv2
import numpy as np

def main():
    # Create a black image
    image = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.circle(image, (50, 50), 40, (255, 0, 0), -1)
    cv2.imwrite("output.png", image)
    print("Image created and saved as output.png")

if __name__ == "__main__":
    main()

