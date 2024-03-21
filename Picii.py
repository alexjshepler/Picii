import PIL.Image

# ASCII Characters used ot build the output
ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']
    
# Resize image
def resizeImage(image, newWidth=100):
    width, height = image.size # Get image size
    ratio = height / width # Get image ratio
    newHeight = int(newWidth * ratio) # Set new height based on ratio and new width
    return (image.resize((newWidth, newHeight))) # Return new image
    

# Convert to grayscale
def convertToGrayscale(image):
    return image.convert('L')

# Convert pixels to ASCII
def pixelsToAscii(image):
    img = image.getdata()
    return "".join([ASCII_CHARS[i//25] for i in img])

def main(newWidth=100):
    # Get an image from user input
    path = input("Enter a valid pathname to an image:\n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, " Is not a valid pathname to an image")
        
    # Convert Image to ASCII
    newImageData = pixelsToAscii(convertToGrayscale(resizeImage(image)))
    
    # Format Image
    pixelCount = len(newImageData)
    asciiImage = '\n'.join(newImageData[i:(i+newWidth)] for i in range(0, pixelCount, newWidth))
    
    print(asciiImage)
    
    # Save Image
    with open("asciiImage.txt", "w") as f:
        f.write(asciiImage)
    
main()
