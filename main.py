# import required libraries
import os
import sys
from PIL import Image


def resizeCrop(im, crop_width, crop_height):
    # resize the image first
    curr_width, curr_height = im.size
    curr_ratio = curr_width / curr_height

    # check if current width or current
    # height fits better to desired format
    d_width = curr_width - crop_width
    d_height = curr_height - crop_height

    # resize to crop_width but with
    # old aspect ratio
    if d_width <= d_height:
        im = im.resize((crop_width, int(crop_width / curr_ratio)), Image.ANTIALIAS)
    else:
        im = im.resize((int(crop_height * curr_ratio), crop_height), Image.ANTIALIAS)

    # finally, crop the image to specific size
    im_cropped = im.crop((0, 0, crop_width, crop_height))

    return im_cropped


def saveImg(name, im, format, quality, cwd):
    # try to create folder for resized and cropped images
    try:
        os.mkdir(f'{cwd}/resized')
    except OSError:
        print("Creation of the directory %s failed" % f"{cwd}/resized")
    else:
        print("Successfully created the directory %s " % f"{cwd}/resized")

    # Save the picture with desired quality
    im.save(f"resized/{name}",
            f"{format}",
            optimize=True,
            quality=quality)


# Define a main function
def main():

    # setup configuration
    cfg = {
        'cropping': True,                      # want to crop your images?
        'crop_x': 400,                          # crop width to ??? px
        'crop_y': 550,                          # crop height to ??? px
        'compressing': True,                    # want to compress your images?
        'format': 'PNG',                        # output format of your images
        'quality': 50,                          # high compression | 0 to 100 | no compression
        'formats': ('.jpg', '.jpeg', '.png'),   # allowed image formats
        'verbose': False                        # verbose flag?
    }

    # finds current working dir
    # which should contain the images
    cwd = os.getcwd()

    # looping through all the files
    for file in os.listdir(cwd):

        # if the file format is JPG, JPEG or PNG
        if os.path.splitext(file)[1].lower() in cfg['formats']:
            print('processing', file)

            # load current image
            im = Image.open(f'{cwd}/{file}')

            # if image should be cropped
            if cfg['cropping']:
                im = resizeCrop(im=im, crop_width=cfg['crop_x'], crop_height=cfg['crop_y'])

            # if image should be compressed
            if cfg['compressing']:
                quality = cfg['quality']
            else:
                quality = 100

            # save cropped and compressed image
            saveImg(name=file, im=im, format=cfg['format'], quality=quality, cwd=cwd)

    print("Done")


# Driver code
if __name__ == "__main__":
    main()
