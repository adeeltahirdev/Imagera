from PIL import Image
import os

def validate_image_path(image_path: str) -> Image.Image:
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f'File not found: {image_path}')
    
    img = Image.open(image_path)
    
    return img


def validate_file_is_image(image_path: str) -> Image.Image:
    try:
        img = Image.open(image_path)
        img.verify()
    
    except (IOError, SyntaxError):
        raise ValueError(f'File is not a valid image: {image_path}')
    
    
    return Image.open(image_path)
    

def validate_image_and_image_path(image: str | Image.Image) -> Image.Image | None:
    
    if isinstance(image, str):
        img = validate_image_path(image)
        img = validate_file_is_image(image)
        return img
    
    elif isinstance(image, Image.Image):
        return image
    
    else:
        raise ValueError('Input must be a file path or a PIL image object')
    

    