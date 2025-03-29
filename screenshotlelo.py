import pyscreenshot # type: ignore
image = pyscreenshot.grab()
image.show() #for displaying the image
image.save('screenshot2.png') #for saving the image
 