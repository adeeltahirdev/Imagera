import pytest

# Test case for validations
from src.pyxify.validate import validate_image_and_image_path, validate_image_path, validate_file_is_image

def test_validate_image_path():
    
    img1 = '/home/adeelt/Pictures/Standee.png'
    img2 = '/home/adeelt/Pictures/invalid.png'
    
    assert validate_image_path(img1) is not None
    
    with pytest.raises(FileNotFoundError):
        validate_image_path(img2)
        
    
def test_validate_file_is_image():
    
    img1 = '/home/adeelt/Pictures/Standee.png'
    img2 = '/home/adeelt/Pictures/Muhammad_Adeel_Tahir.pdf'
    
    assert validate_file_is_image(img1) is not None
    
    with pytest.raises(ValueError):
        validate_file_is_image(img2)
    
def test_validate_image_and_image_path():
    
    img1 ='/home/adeelt/Pictures/Standee.png'
    img2 = '/home/adeelt/Pictures/invalid.png'
    img3 = '/home/adeelt/Pictures/Muhammad_Adeel_Tahir.pdf'
    
    assert validate_image_and_image_path(img1) is not None
    
    with pytest.raises(FileNotFoundError):
        validate_image_and_image_path(img2)
        
    with pytest.raises(ValueError):
        validate_image_and_image_path(img3)
    

# Test cases for convert
from src.pyxify.convert import grayscale

def test_grayscale():
    
    img1 ='/home/adeelt/Pictures/Standee.png'
    img2 = '/home/adeelt/Pictures/invalid.png'
    img3 = '/home/adeelt/Pictures/Muhammad_Adeel_Tahir.pdf'
    
    gray_img1 = grayscale(img1)
    
    assert gray_img1 is not None
    
    with pytest.raises(FileNotFoundError):
        grayscale(img2)
        
    with pytest.raises(ValueError):
        grayscale(img3)
    
    
# Test cases for meatadata
from src.pyxify.metadata import get_image_metadata

def test_get_image_metadata():
    
    img1 ='/home/adeelt/Pictures/Standee.png'
    img2 = '/home/adeelt/Pictures/invalid.png'
    img3 = '/home/adeelt/Pictures/Muhammad_Adeel_Tahir.pdf'
    
    metadata = get_image_metadata(img1)
    
    
    assert metadata is None
    
    with pytest.raises(FileNotFoundError):
        get_image_metadata(img2)
        
    with pytest.raises(ValueError):
        get_image_metadata(img3)
    

# Test cases for flip
from src.pyxify.flip import flip_horizontal, flip_vertical, rotate


def test_flip_horizontal():
    
    img1 ='/home/adeelt/Pictures/Standee.png'
    img2 = '/home/adeelt/Pictures/invalid.png'
    img3 = '/home/adeelt/Pictures/Muhammad_Adeel_Tahir.pdf'
    
    flip_img1 = flip_horizontal(img1)
    
    
    assert flip_img1 is not None
    
    with pytest.raises(FileNotFoundError):
        flip_horizontal(img2)
        
    with pytest.raises(ValueError):
        flip_horizontal(img3)
    
    
def test_flip_vertical():
    
    img1 ='/home/adeelt/Pictures/Standee.png'
    img2 = '/home/adeelt/Pictures/invalid.png'
    img3 = '/home/adeelt/Pictures/Muhammad_Adeel_Tahir.pdf'
    
    flip_img1 = flip_vertical(img1)
    
    assert flip_img1 is not None
    
    with pytest.raises(FileNotFoundError):
        flip_vertical(img2)
        
    with pytest.raises(ValueError):
        flip_vertical(img3)
    
    
def test_rotate():
    
    img1 ='/home/adeelt/Pictures/Standee.png'
    img2 = '/home/adeelt/Pictures/invalid.png'
    img3 = '/home/adeelt/Pictures/Muhammad_Adeel_Tahir.pdf'
    
    rotate_img1 = rotate(90, img1)
    
    
    assert rotate_img1 is not None
    
    with pytest.raises(FileNotFoundError):
        rotate(90, img2)
        
    with pytest.raises(ValueError):
        rotate(90, img3)
    
    
# Test cases for crop
from src.pyxify.crop import crop, resize


def test_crop():
    
    img1 ='/home/adeelt/Pictures/Standee.png'
    img2 = '/home/adeelt/Pictures/invalid.png'
    img3 = '/home/adeelt/Pictures/Muhammad_Adeel_Tahir.pdf'
    
    crop_img1 = crop(10, 10, 100, 100, img1)
    
    assert crop_img1 is not None
    
    with pytest.raises(FileNotFoundError):
        crop(10, 10, 100, 100, img2)
        
    with pytest.raises(ValueError):
        crop(10, 10, 100, 100, img3)
    
    
def test_resize():
    
    img1 ='/home/adeelt/Pictures/Standee.png'
    img2 = '/home/adeelt/Pictures/invalid.png'
    img3 = '/home/adeelt/Pictures/Muhammad_Adeel_Tahir.pdf'
    
    resize_img1 = resize(200, 200, img1)
    
    assert resize_img1 is not None
    
    with pytest.raises(FileNotFoundError):
        resize(200, 200, img2)
        
    with pytest.raises(ValueError):
        resize(200, 200, img3)
    
# Test cases fro enhance
from src.pyxify.enhance import enhance_brightness, enhance_contrast, enhance_color, enhance_sharpness, blur_effect


def test_enhance_brightness():
    
    img1 ='/home/adeelt/Pictures/Standee.png'
    img2 = '/home/adeelt/Pictures/invalid.png'
    img3 = '/home/adeelt/Pictures/Muhammad_Adeel_Tahir.pdf'
    
    enhance_img1 = enhance_brightness(2.5, img1)
    
    assert enhance_img1 is not None
    
    with pytest.raises(FileNotFoundError):
        enhance_brightness(2.5, img2)
    
    with pytest.raises(ValueError):
        enhance_brightness(2.5, img3)
    
    
def test_enhance_contrast():
    
    img1 ='/home/adeelt/Pictures/Standee.png'
    img2 = '/home/adeelt/Pictures/invalid.png'
    img3 = '/home/adeelt/Pictures/Muhammad_Adeel_Tahir.pdf'
    
    enhance_img1 = enhance_contrast(2.5, img1)
    
    assert enhance_img1 is not None
    
    with pytest.raises(FileNotFoundError):
        enhance_contrast(2.5, img2)
        
    with pytest.raises(ValueError):
        enhance_contrast(2.5, img3)
        
    
def test_enhance_color():
    
    img1 ='/home/adeelt/Pictures/Standee.png'
    img2 = '/home/adeelt/Pictures/invalid.png'
    img3 = '/home/adeelt/Pictures/Muhammad_Adeel_Tahir.pdf'
    
    enhance_img1 = enhance_color(2.5, img1)
    
    assert enhance_img1 is not None
    
    with pytest.raises(FileNotFoundError):
        enhance_color(2.5, img2)
        
    with pytest.raises(ValueError):
        enhance_color(2.5, img3)
        
    
def test_enhance_sharpness():
    
    img1 ='/home/adeelt/Pictures/Standee.png'
    img2 = '/home/adeelt/Pictures/invalid.png'
    img3 = '/home/adeelt/Pictures/Muhammad_Adeel_Tahir.pdf'
    
    enhance_img1 = enhance_sharpness(2.5, img1)
    
    assert enhance_img1 is not None
    
    with pytest.raises(FileNotFoundError):
        enhance_sharpness(2.5, img2)
        
    with pytest.raises(ValueError):
        enhance_sharpness(2.5, img3)
    
    
def test_blur_effect():
    
    img1 ='/home/adeelt/Pictures/Standee.png'
    img2 = '/home/adeelt/Pictures/invalid.png'
    img3 = '/home/adeelt/Pictures/Muhammad_Adeel_Tahir.pdf'
    
    blur_img1 = blur_effect(5.0, img1)
    
    assert blur_img1 is not None
    
    with pytest.raises(FileNotFoundError):
        blur_effect(5.0, img2)
        
    with pytest.raises(ValueError):
        blur_effect(5.0, img3)