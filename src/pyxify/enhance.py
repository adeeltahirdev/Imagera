from PIL import Image, ImageEnhance, ImageFilter
from src.pyxify.validate import validate_image_and_image_path

def enhance_contrast(value: float, image: str | Image.Image) -> Image.Image:
    
    img = validate_image_and_image_path(image)
    
    enhancer = ImageEnhance.Contrast(img)
    enhanced_img = enhancer.enhance(value)
    
    return enhanced_img


def enhance_brightness(value: float, image: str | Image.Image) -> Image.Image:
    
    img = validate_image_and_image_path(image)
    
    enhancer = ImageEnhance.Brightness(img)
    enhanced_img = enhancer.enhance(value)
    
    return enhanced_img


def enhance_color(value: float, image: str | Image.Image) -> Image.Image:
    
    img = validate_image_and_image_path(image)
    
    enhancer = ImageEnhance.Color(img)
    enhanced_img = enhancer.enhance(value)
    
    return enhanced_img


def enhance_sharpness(value: float, image: str | Image.Image) -> Image.Image:
    
    img = validate_image_and_image_path(image)
    
    enhancer = ImageEnhance.Sharpness(img)
    enhanced_img = enhancer.enhance(value)
    
    return enhanced_img


def blur_effect(radius: float, image: str | Image.Image) -> Image.Image:
    
    img = validate_image_and_image_path(image)
    
    blurred_img = img.filter(ImageFilter.GaussianBlur(radius))
    
    return blurred_img