import cv2
import filters
import argparse

from labTypings import RGB, Rectangle


def main(args: argparse.Namespace):
    imagePath = args.image

    image = cv2.imread(imagePath)

    if image is None:
        raise ValueError(f"There is no image: {imagePath}")

    if args.filterType == "resize":
        height: int | None = args.height
        width: int | None = args.width

        if height is None:
            height = int(image.shape[0])
        if width is None:
            width = int(image.shape[1])
        filteredImage = filters.resize(image, width, height)
    elif args.filterType == "sepia":
        filteredImage = filters.sepia(image)
    elif args.filterType == "vignette":
        opacity: float | None = args.opacity

        if opacity is None:
            filteredImage = filters.addVignette(image, args.radius)
        else:
            filteredImage = filters.addVignette(image, args.radius, opacity)
    elif args.filterType == "pixelate":
        rect = Rectangle(*args.region)
        filteredImage = filters.pixelate(image, rect, args.blockSize)
    elif args.filterType == "rectFrame":
        borderColor = RGB(*args.color)
        filteredImage = filters.addRectFrame(image, borderColor, args.width)
    elif args.filterType == "figureFrame":
        whiteThreshold: float | None = args.whiteThreshold

        if whiteThreshold is None:
            filteredImage = filters.addFigureFrame(
                image,
                args.frameIndex,
            )
        else:
            filteredImage = filters.addFigureFrame(
                image, args.frameIndex, whiteThreshold
            )
    elif args.filterType == "glare":
        opacity: float | None = args.opacity

        if opacity is None:
            filteredImage = filters.addGlare(image)
        else:
            filteredImage = filters.addGlare(image, opacity)
    elif args.filterType == "watercolor":
        opacity: float | None = args.opacity

        if opacity is None:
            filteredImage = filters.addWatercolor(image)
        else:
            filteredImage = filters.addWatercolor(image, opacity)

    cv2.imshow("Original", image)
    cv2.imshow("Filtered", filteredImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pass


if __name__ == "__main__":
    argParser = argparse.ArgumentParser(prog="cvFilter")
    argParser.add_argument("--image", type=str, required=True, help="Path to image")

    subparsers = argParser.add_subparsers(
        dest="filterType", title="Filters", help="A filter applied to the image"
    )

    resizeParser = subparsers.add_parser("resize")
    resizeParser.add_argument(
        "--height", type=int, help="If not specified, original height will be used"
    )
    resizeParser.add_argument(
        "--width", type=int, help="If not specified, original height will be used"
    )

    sepiaParser = subparsers.add_parser("sepia")
    vignetteParser = subparsers.add_parser("vignette")
    vignetteParser.add_argument(
        "--radius", type=float, required=True, help="Value from 0 to 1"
    )
    vignetteParser.add_argument("--opacity", type=float)

    pixelateParser = subparsers.add_parser("pixelate")
    pixelateParser.add_argument(
        "--region",
        type=int,
        help="Coordiantes of top left cornern, width and height",
        required=True,
        nargs=4,
    )
    pixelateParser.add_argument("--blockSize", type=int, required=True)

    rectFrameParser = subparsers.add_parser("rectFrame")
    rectFrameParser.add_argument(
        "--color", type=int, help="RGB", required=True, nargs=3
    )
    rectFrameParser.add_argument("--width", type=int, required=True)

    figureFrameParser = subparsers.add_parser("figureFrame")
    figureFrameParser.add_argument("--frameIndex", type=int, required=True)
    figureFrameParser.add_argument("--whiteThreshold", type=float)

    glareParser = subparsers.add_parser("glare")
    glareParser.add_argument("--opacity", type=float)

    watercolorParser = subparsers.add_parser("watercolor")
    watercolorParser.add_argument("--opacity", type=float)

    main(argParser.parse_args())
