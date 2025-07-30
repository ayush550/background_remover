Run: python app.py

Framework: Flask

Image Processing:
rembg (based on U-2-Net)

Errors if encountered:
AttributeError: module 'PIL.Image' has no attribute 'Resampling'

Reason: happens because the rembg library uses PIL.Image.Resampling, which was introduced 
in Pillow 9.1.0 and later. If you have an older version of Pillow, it doesn’t include Image.Resampling

Solution:
pip install --upgrade pillow

Verify:
python -c "import PIL; print(PIL.__version__)"

Output must be something like: 10.4.0

