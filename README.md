# compressionIMG

Easy to use Python script based on Pillow that allows you to compress any JPEG / PNG files.

## Installation & Usage 

1. use `pip install pillow` to install the Pillow package in your Python environment
2. move the `main.py` into the dir which contains the images to be compressed / resized
3. run `main.py`

## Configuration

You can also adjust some configuration within the `main()`function. 

´´´Pyhton
# setup configuration
    cfg = {
        'cropping': True,                       # want to crop your images?
        'crop_x': 400,                          # crop width to ??? px
        'crop_y': 550,                          # crop height to ??? px
        'compressing': True,                    # want to compress your images?
        'format': 'PNG',                        # output format of your images
        'quality': 50,                          # high compression | 0 to 100 | no compression
        'formats': ('.jpg', '.jpeg', '.png'),   # allowed image formats
        'verbose': False                        # verbose flag?
    }
```
