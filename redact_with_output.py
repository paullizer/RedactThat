import json
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

json_file = 'output.json'
input_path = "before.tif"
output_path = "redacted_using_output.tif"

with open(json_file, 'r', encoding='utf-8') as file_handle:
    output = json.load(file_handle)

    for nodes in output:
        for lines in nodes['lines']:
            if 'GRANITE RIDGE LP' in lines['content']:
                redact(lines['boundingBox'][0], lines['boundingBox'][1], lines['boundingBox'][2], lines['boundingBox'][3], lines['boundingBox'][4], lines['boundingBox'][5], lines['boundingBox'][6], lines['boundingBox'][7], input_path, output_path)




#redact(260, 150, 580, 150, 580, 300, 260, 300, input_path, output_path)