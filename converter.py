from PIL import Image

    # converting jpg image to png

im = Image.open("naruto.jpg").convert("RGB")
im.save("naruto.png", "png")


/*Converting png image to jpg*/

from PIL import Image

im = Image.open("naruto.png").convert("RGB")
im.save("naruto.jpg", "jpeg")
