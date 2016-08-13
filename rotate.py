#instrall pillow, becasuse we need it
def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    
install_and_import('pillow')

from PIL import Image
import os

imgfolder = "./images"
flipped = "./flipped"

for dirpath, dirnames, dafile in os.walk( imgfolder ):
	for image in dafile:
		img = Image.open(dirpath+"\/"+image)
		img = img.transpose(Image.FLIP_LEFT_RIGHT)
		img.save(flipped+"\/"+image, "JPEG")
		img.close()