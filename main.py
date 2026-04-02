from crop import crop, resize
from flip import flip_horizontal, flip_vertical, rotate
from enhance import enhance_brightness, enhance_contrast, enhance_color, enhance_sharpness, blur_effect
from convert import grayscale
from metadata import get_image_metadata

img1 = '/home/adeelt/Pictures/Standee.png'

img = grayscale(img1)
img.show()
