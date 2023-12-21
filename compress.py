from PIL import Image

in_img = 'input.png'
out_img = 'compressed.png' 

# Open the image
with Image.open(in_img) as img:
    # Save the compressed image
    img.save(out_img, 'PNG', quality=80)

print(f"Image compressed successfully!")
