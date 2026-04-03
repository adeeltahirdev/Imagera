# Pyxify

Pyxify is a simple and lightweight Python library for basic image processing tasks.  
It is built using Pillow and provides easy-to-use functions for resizing, cropping, enhancing, and manipulating images.

---

## ✨ Features

- Resize images
- Crop images
- Convert images to grayscale
- Flip images (horizontal & vertical)
- Rotate images
- Enhance:
  - Brightness
  - Contrast
  - Color
  - Sharpness
- Apply blur effect
- Extract image metadata

---

## 🚀 Installation

```bash
pip install pyxify
```

---

## 📌 Usage

### Import Library

```python
from pyxify import *
```

---

### Resize Image

```python
img = resize(200, 200, "image.jpg")
```

### Crop Image

```python
img = crop(10, 10, 100, 100, "image.jpg")
```

### Convert To Grayscale

```python
img = grayscale("image.png")
```

### Flip Image

```python
img = flip_horizontal("image.png")
img = flip_vertical("image.png")
```

### Rotate Image

```python
img = rotate(90, "image.jpg")
```

### Enhance Image

```python
img = enhance_brightness(2.5, "image.png")
img = enhance_contrast(2.5, "image.png")
img = enhance_color(2.5, "image.png")
img = enhance_sharpness(2.5, "image.png")
```

### Apply Blur

```python
img = blur_effect(5.0, "image.png")
```

### Get Image Metadata

```python
get_image_metadata("image.png")
```

---

## ⚠️ Error Handling

The library handles common errors:

- `FileNotFoundError` → When the file does not exist  
- `ValueError` → When the file is not a valid image  

---

## 📂 Supported Input

- File Path (`str`)
- PIL Image object

---

## 🧪 Testing

The project includes test cases using `pytest` with ~95% coverage.

Run tests:

```bash
pytest
```

---

## 📦 Dependencies

- Pillow

### Dev Dependencies

- pytest  
- pytest-cov  

---

## 👨‍💻 Author

**Adeel Tahir**

---

## 📜 License

This project is licensed under the MIT License.
