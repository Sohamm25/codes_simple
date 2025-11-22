from PIL import Image
def find_resolution(image_path):
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            return width, height
    except Exception as e: 
        print("Error:", e)
        return None
image_path = input("Enter the path to the image file: ")
resolution = find_resolution(image_path) 
if resolution:
    print("Image Resolution (Width x Height):", resolution)
