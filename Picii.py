import PIL.Image

# ASCII Characters used ot build the output
ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']
    
# Resize image
def resizeImage(image, newWidth=100):
    width, height = image.size # Get image size
    ratio = height / width # Get image ratio
    newHeight = int(newWidth * ratio) # Set new height based on ratio and new width
    return image.resize((newWidth, newHeight)) # Return new image
    
def main():
    # Get an image from user input
    path = input("Enter a valid pathname to an image:\n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, " Is not a valid pathname to an image")
