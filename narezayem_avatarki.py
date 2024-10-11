from PIL import Image

monro = Image.open("monro.jpg")
monro_red, monro_green, monro_blue = monro.split()

coordinates_left = (50, 0, monro.width, monro.height)
coordinates_right = (0, 0, monro.width-50, monro.height)
coordinates_center = (25, 0, monro.width-25, monro.height)

monro_red_front = monro_red.crop(coordinates_left)
monro_red_back = monro_red.crop(coordinates_center)
monro_blue_front = monro_blue.crop(coordinates_right)
monro_blue_back = monro_blue.crop(coordinates_center)
monro_green_front = monro_green.crop(coordinates_center)

monro_red = Image.blend(monro_red_front, monro_red_back, 0.6)
monro_blue = Image.blend(monro_blue_front, monro_blue_back, 0.6)

monro_image = Image.merge('RGB', (monro_red, monro_green_front, monro_blue))
monro_image.save('monro_image.jpg', format='JPEG')
monro_image.thumbnail((80, 80))
monro_image.save('monro_avatar.jpg', format='JPEG')
