from PIL import Image, ImageFilter


def blur_image(img):
    '''Blurring an Image'''
    blured_img = img.filter(ImageFilter.BLUR)
    return blured_img


def sharpen_image(img):
    '''Sharpening an image'''
    sharpened_img = img.filter(ImageFilter.SHARPEN)
    return sharpened_img


def gray_scale(img):
    gray_scaled_img = img.convert('L')
    return gray_scaled_img


def smoothen_image(img):
    '''Smoothening the Image'''
    smooth_img = img.filter(ImageFilter.SMOOTH)


def show(img):
    '''Showing the img'''
    img.show()


def rotate(img, degrees):
    '''Rotate img by degrees and show it'''
    rotated_img = img.rotate(degrees)
    rotated_img.show()


def resize(img, res):
    '''Resize image to resolution'''
    resized_img = img.resize(res)
    resized_img.show()


def crop(img, box):
    '''Cropping the image where box is the cordinates of the actual rectangle cordintes'''
    region = img.crop(box)
    region.show()



# Converting the jpg file into Image instance that PIL gives us
img = Image.open('./images/pikachu.jpg')

crop(img,(100,100,400,400))

# Returns the format of the file
print(img.format)

# Returns the format of the file
#print(dir(img))


# Saving filtered image
#sharpen_image(img).save("sharp.png", 'png')  # we have a blurred image





