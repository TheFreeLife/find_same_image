from PIL import Image 

im = Image.open("C:/Users/happy/Desktop/test_folder/kei100.jpeg") 
im2 = Image.open("C:/Users/happy/Desktop/test_folder/kei300.jpeg")

pixels = list(im.getdata())
pixels2 = list(im2.getdata())

if pixels == pixels2:
    print('OK')
else:
    print('NO')
