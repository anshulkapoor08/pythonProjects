import pyscreenshot # type: ignore
image = pyscreenshot.grab(bbox=(10, 10, 500, 500))
image.show() #for displaying the image
image.save('screenshot2.png') #for saving the image
