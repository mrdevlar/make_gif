# Animated Gif Creation Tool

This is a simple Python command line tool for the creation of animated gifs.

## Dependencies
- [ImageIO](https://pypi.org/project/imageio/)

## Installation and Use

### Basic Usage
Provide the `make_gif.py` script with an `--img_folder` argument followed by a folder containing 
```
python make_gif.py --img_folder my_folder
```

### Advanced Usage

All the bells and whistles can be found by calling `-h`.

```
usage: make_gif.py [-h] [--verbose] --img_folder IMG_FOLDER
                   [--output_file OUTPUT_FILE] [--duration DURATION]
                   [--types TYPES [TYPES ...]] [--shuffle]

Makes an animated gif from a folder of pictures

optional arguments:
  -h, --help            show this help message and exit
  --verbose             Boolean flag indicating if statements should be
                        printed to the console.
  --img_folder IMG_FOLDER
                        The folder name that contains images to be made into a
                        gif.
  --output_file OUTPUT_FILE
                        The output file of the animated gif (default:
                        animation.gif).
  --duration DURATION   Duration between frames in the animated gif (default:
                        0.13).
  --types TYPES [TYPES ...]
                        The file types to consider when making the animated
                        gifs (default: ['png', 'jpg']).
  --shuffle             Shuffles the order of the files that make up the
                        animated gif.
```