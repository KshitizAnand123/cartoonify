import cv2
import numpy as np


def edge_mask(img, line_size, blur_value):

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray_blur = cv2.medianBlur(gray, blur_value)

    edges = cv2.adaptiveThreshold(
        gray_blur,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        line_size,
        blur_value
    )

    return edges


def color_quantization(img, k):

    # Downsample image for faster clustering
    small = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

    data = np.float32(small).reshape((-1,3))

    criteria = (
        cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,
        10,
        1.0
    )

    _, label, center = cv2.kmeans(
        data,
        k,
        None,
        criteria,
        5,
        cv2.KMEANS_RANDOM_CENTERS
    )

    center = np.uint8(center)

    result = center[label.flatten()]
    result = result.reshape(small.shape)

    # Resize back to original size
    result = cv2.resize(result, (img.shape[1], img.shape[0]))

    return result


def cartoonify_image(img):

    # Resize large images to reduce computation
    height, width = img.shape[:2]

    if width > 800:
        scale = 800 / width
        img = cv2.resize(img, (int(width * scale), int(height * scale)))

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    edges = edge_mask(img, 7, 7)

    quantized = color_quantization(img, 8)

    blurred = cv2.bilateralFilter(
        quantized,
        d=5,
        sigmaColor=75,
        sigmaSpace=75
    )

    cartoon = cv2.bitwise_and(
        blurred,
        blurred,
        mask=edges
    )

    return cartoon