from PIL import Image, ImageDraw

def redact(x1, y1, x2, y2, x3, y3, x4, y4, image_input_path, image_output_path):
    # Open the input image
    with Image.open(image_input_path) as im:
        # Create a new image object with the same mode and size as the input image
        draw = ImageDraw.Draw(im)
        # Draw a black polygon with the provided coordinates
        draw.polygon([(x1, y1), (x2, y2), (x3, y3), (x4, y4)], fill="BLACK") #RED, GREEN, BLUE, TRANSPARENCY (0-255)
        # Save the modified image to the output path
        im.save(image_output_path)

input_path = "C:/temp/before.tif"
output_path = "C:/temp/redacted.tif"
redact(260, 150, 580, 150, 580, 300, 260, 300, input_path, output_path)