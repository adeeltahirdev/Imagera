from PIL import Image, ImageOps
from src.pyxify.validate import validate_image_and_image_path

def grayscale(image: str | Image.Image) -> Image.Image:
    
    img = validate_image_and_image_path(image)
    
    gryascale_img = ImageOps.grayscale(img)
    
    return gryascale_img