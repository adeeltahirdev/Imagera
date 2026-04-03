from PIL import Image
from src.pyxify.validate import validate_image_and_image_path


def crop(left: float, top: float, right: float, bottom: float, image: str | Image.Image) -> Image.Image:
    
    cropped_image = validate_image_and_image_path(image)
    
    cropped_image = cropped_image.crop((left, top, right, bottom))
    
    return cropped_image


def resize(width: int, height: int, image: str | Image.Image) -> Image.Image:
    
    resized_img = validate_image_and_image_path(image)
    
    resized_img = resized_img.resize((width, height))
    
    return resized_img