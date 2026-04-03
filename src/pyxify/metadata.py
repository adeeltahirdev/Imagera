from PIL import Image
from src.pyxify.validate import validate_image_and_image_path


def get_image_metadata(image: str | Image.Image) -> None:
    
    img = validate_image_and_image_path(image)
    
    metadata = {
        'FileName': img.filename,
        'Image Size': img.size,
        'Image Height': img.height,
        'Image Width': img.width,
        'Image Format': img.format,
        'Image Mode': img.mode,        
    }
    
    for label, value in metadata.items():
        print(f'{label:25}: {value}')