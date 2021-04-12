from PIL import Image,ImageDraw,ImageFilter
from IPython.display import display
import urllib.request
# ouvrir une image hberge sur internet
im = Image.open(urllib.request.urlopen('https://raw.githubusercontent.com/hackathon-nsi/h7n-nsi-01/main/images/washington.bmp'))

#im = Image.open('chihiros.jpg')

# informations sur l'image
print(im.format, im.size, im.mode)

#---------------- Image 1 ---------------#
#                 echiquier              #
# fait une nouvelle image avec des bandes verticales 
def ImageStripes(im,width,yShift):
    maxX,maxY = im.size
    newImage = Image.new(mode = "RGB", size = (maxX, maxY+width))
    for x in range(0,maxX,width):
    #(left, upper, right, lower) = (x,0, x+width, maxY)
        box = (x,0, x+width, maxY)
        cropStrip = im.crop(box)
        boxNew=(x,yShift,x+width,maxY+yShift)
        newImage.paste(cropStrip, boxNew)
        if yShift == width :
            yShift = 0
        else:
            yShift = width
    return newImage

def GeneratePicture1(img):
    newImage= ImageStripes(img,32,32)

    #tourner l image de 90 degres
    newImage = newImage.rotate(angle=90,expand=True)
    #fait de nouvelles bandes
    newImage= ImageStripes(newImage,32,32)
    # retourner l image de 90 degres
    newImage = newImage.rotate(angle=-90,expand=True)
    return newImage


img1 = GeneratePicture1(im)
img1.show()




#---------------- IMAGE 2 ---------------#
#                 boites                 #
def GeneratePicture2(im,distance=32,boxSize=2):
    imNew = im.copy()
    maxX,maxY = imNew.size
    draw = ImageDraw.Draw(imNew)
    
    for x in range(0,maxX,distance):
        for y in range(0,maxY,distance):
            if x !=0 and y !=0 :
                box = [(x - boxSize, y - boxSize),(x+boxSize, y+boxSize) ]
                draw.rectangle(box, fill ="#ffff33", outline ="red")
    return imNew

img2 = GeneratePicture2(im)
img2.show()



# filtre sur l image: Find_Edges
img3 = im.copy().resize(img1.size)
imageWithEdges = img3.filter(ImageFilter.FIND_EDGES)
imageWithEdges.show()


#unir 2 images avec mask
#https://note.nkmk.me/en/python-pillow-composite/
mask = Image.new("L", img1.size, 200)
img4 = Image.composite(img1, img2, mask)
img4.show()





# unir les 2 images avec une mask 2 Bilder übereinanderlegen wobei die maske eine blured ellipse ist


maxX,maxY = img1.size
x,y = maxX/2,maxY/2
mask = Image.new("L", img1.size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((x-100,y-300,x+100,y+300), fill=255)
mask_blur = mask.filter(ImageFilter.GaussianBlur(20))
img5 = Image.composite(img1, img2, mask_blur)


img3.convert("L")

#img6 = Image.composite(im.copy().resize(img5.size), img5, img3)

print(img5.size)
print(img3.size)

#img1.show()
#img2.show()
#img3.show()
#img4.show()
#img5.show()
#img6.show()