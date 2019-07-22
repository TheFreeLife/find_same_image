from PIL import Image 

im = Image.open("test_image5.jpeg") 
im2 = Image.open("test_image10.jpeg")

pixels = list(im.getdata())
pixels2 = list(im2.getdata())

if pixels == pixels2:
    print('OK')
else:
    print('NO')
