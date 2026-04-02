from validate import validate_image_and_image_path, validate_image_path, validate_file_is_image

def test_validate_image_path(tmp_path):
    
    tmp_path = '/home/adeelt/Pictures/Standee.png'
    
    assert validate_image_path(tmp_path) is not None
    
def test_validate_file_is_image(tmp_path):
    
    tmp_path = '/home/adeelt/Pictures/Standee.png'
    
    assert validate_file_is_image(tmp_path) is not None
    
def test_validate_image_and_image_path(tmp_path):
    
    tmp_path ='/home/adeelt/Pictures/Standee.png'
    
    assert validate_image_and_image_path(tmp_path) is not None