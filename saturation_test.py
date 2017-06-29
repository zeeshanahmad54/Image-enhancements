from PIL import Image, ImageEnhance

image = Image.open("img.png")	#path of the image to be read
converter = ImageEnhance.Color(image)
image_pos = converter.enhance(1.2)	#enhancement value > 1 for positive saturation
image_pos.save("image_pos.png")
image_neg = converter.enhance(0.5)	#enhancement value < 1 for negative saturation
image_neg.save("image_neg.png")
