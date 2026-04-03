from PIL import Image
from src.pyxify.validate import validate_image_and_image_path


def flip_horizontal(image: str | Image.Image) -> Image.Image:
    
    img = validate_image_and_image_path(image)
    
    flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    
    return flipped_img

def flip_vertical(image: str | Image.Image) -> Image.Image:
    
    img = validate_image_and_image_path(image)
    
    flipped_img = img.transpose(Image.FLIP_TOP_BOTTOM)
    
    return flipped_img


def rotate(angle: float, image: str | Image.Image) -> Image.Image:
    
    img = validate_image_and_image_path(image)
    
    rotated_img = img.rotate(angle)
    
    return rotated_img