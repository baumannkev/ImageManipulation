import cmpt120image
import cmpt120imageManip

img = cmpt120image.getImage("saul.jpg")

print("FILTERS\n1: Swap red and green\n2: Convert to black and white\n3: Reflect\n4: Brighten\n5: Reload Image\n0: Quit")
while True:
    userInput = input("Enter 1 to 5, 0 to quit: ")
    if (userInput == "1"):
        returnImage = cmpt120imageManip.swapRedGreen(img)
        cmpt120image.showImage(returnImage)
        cmpt120image.saveImage(returnImage, "imgRGswap.png")
    elif(userInput == "2"):
        returnImage = cmpt120imageManip.blackWhite(img)
        cmpt120image.showImage(returnImage)
        cmpt120image.saveImage(returnImage, "imgBW.png")
    elif(userInput == "3"):
        returnImage = cmpt120imageManip.reflect(img)
        cmpt120image.showImage(returnImage)
        cmpt120image.saveImage(returnImage, "imgReflect.png")
    elif(userInput == "4"):
        returnImage = cmpt120imageManip.brighten(img)
        cmpt120image.showImage(returnImage)
        cmpt120image.saveImage(returnImage, "imgBrighten.png")
    elif(userInput == "5"):
        img = cmpt120image.getImage("bird.png")
        cmpt120image.showImage(img)
    elif(userInput == "0"):
        break



