import cv2
import filters

from labTypings import RGB, Rectangle


def main():
    nInputImages = 4
    nFigureFrames = 1
    for i in range(nInputImages):
        inputImagePath = f"input/input{i + 1}.jpg"

        inputImage = cv2.imread(inputImagePath)
        if inputImage is None:
            raise ValueError(f"There is no input{i + 1}.jpg in input folder")

        result = filters.resize(inputImage, 2000, 1000)
        _ = cv2.imwrite(f"output/output{i + 1}_resize.jpg", result)
        result = filters.sepia(inputImage)
        _ = cv2.imwrite(f"output/output{i + 1}_sepia.jpg", result)
        result = filters.addVignette(inputImage, 0.8, 0.6)
        _ = cv2.imwrite(f"output/output{i + 1}_vignete.jpg", result)
        result = filters.pixelate(inputImage, Rectangle(100, 100, 1200, 300), 16)
        _ = cv2.imwrite(f"output/output{i + 1}_pixelate.jpg", result)
        result = filters.addRectFrame(inputImage, RGB(255, 0, 0), 10)
        _ = cv2.imwrite(f"output/output{i + 1}_rectFrame.jpg", result)
        for j in range(nFigureFrames):
            result = filters.addFigureFrame(inputImage, j + 1, 30)
            _ = cv2.imwrite(f"output/output{i + 1}_figureFrame{j + 1}.jpg", result)
        result = filters.addGlare(inputImage, 0.86)
        _ = cv2.imwrite(f"output/output{i + 1}_glare.jpg", result)
        result = filters.addWatercolor(inputImage)
        _ = cv2.imwrite(f"output/output{i + 1}_watercolor.jpg", result)


if __name__ == "__main__":
    main()
