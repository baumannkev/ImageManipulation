import cmpt120image

# Get the approximate color to check if it is green
def getApproxColorName(img, h, w):
    pixel = img[h][w]
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]
    if (r >= 100 and g <= 200 and b <= 75) and (r > g):
        colorName = "red"
    elif (r <= 200 and g >= 100 and b <= 75) and (r < g):
        colorName = "green"
    else:
        colorName = "other"
    return colorName

# swap Red & Green
def swapRedGreen(img):
    h = len(img)
    w = len(img[0])
    final = cmpt120image.createBlackImage(h,w)

    for row in range(h):
        for col in range(w):
            if getApproxColorName(img, row, col) == "red":
                final[row][col] = [70,209,8]
            elif getApproxColorName(img, row, col) == "green":
                final[row][col] = [229,13,19]
            else:
                final[row][col] = img[row][col]
    return final

# Check the sum of the pixels to see if they exceed the max possible / 2
def checkSum(img, h, w):
    pixel = img[h][w]
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]

    sum = (r + g + b)
    if (sum < 384):
        whiteOrBlack = "black"
    else:
        whiteOrBlack = "white"
    return whiteOrBlack
# make img Black & White
def blackWhite(img):
    h = len(img)
    w = len(img[0])
    final = cmpt120image.createBlackImage(h,w)

    for row in range(h):
        for col in range(w):
            if checkSum(img, row, col) == "white":
                final[row][col] = [255,255,255]
            elif checkSum(img, row, col) == "black":
                final[row][col] = [0, 0, 0]
            else:
                final[row][col] = img[row][col]
    return final

  #reflect image horizontally
def reflect(img):
    h = len(img)
    w = len(img[0])
    final = cmpt120image.createBlackImage(h,w)
    h1 = h//2
    w1 = w//2

    for row in range(h):
       for col in range(w // 2):
           final[row][col] = img[row][col]
           final[row][ -col - 1] = img[row][col]
    return final

#Check if pixels are less than 229
def checkBright(img, h, w):
    pixel = img[h][w]
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]

    if (r < 229 and g < 229 and b < 229):
        pixel[0] = r*1.1
        pixel[1] = g*1.1
        pixel[2] = b*1.1
        return pixel
    else:
        return pixel
#brighten image
def brighten(img):
  h = len(img)
  w = len(img[0])
  final = cmpt120image.createBlackImage(h,w)
  for row in range(h):
        for col in range(w):
             final[row][col] = checkBright(img, row, col)

  return final
