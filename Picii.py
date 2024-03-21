import PIL.Image

def main():

    # Get an image from user input
    path = input("Enter a valid pathname to an image:\n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, " Is not a valid pathname to an image")
