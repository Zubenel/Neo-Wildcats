from PIL import Image
im = Image.open("home.png")
print(im.format, im.size, im.mode) # Format, (width, height), number and names of the bands:

# "L" for luminance (grayscale)
# "RGB" for true color images
# "CMYK" for pre-press images
try:
    print("Showing file...")
    im.show()
except:
    print("Nor possible to open file")
print("End")
