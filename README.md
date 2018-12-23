# Command Line Tool for Animated Gif Creation

This is a simple Python command line tool for the creation of animated gifs.

![animated](https://github.com/mrdevlar/make_gif/blob/master/examples/animation.gif)

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
usage: make_gif.py [-h] [-v] [-o OUTPUT_FILE] [-t TYPES [TYPES ...]]
                   [-i IGNORE_FILES [IGNORE_FILES ...]] [-s] [-d DURATION]
                   img_folder

Makes an animated gif from a folder of pictures

positional arguments:
  img_folder            The folder name that contains images to be made into a
                        gif.

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Boolean flag indicating if statements should be
                        printed to the console.
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        The output file of the animated gif (default:
                        animation.gif).
  -t TYPES [TYPES ...], --types TYPES [TYPES ...]
                        The file types to consider when making the animated
                        gifs (default: ['png', 'jpg']).
  -i IGNORE_FILES [IGNORE_FILES ...], --ignore_files IGNORE_FILES [IGNORE_FILES ...]
                        List of files to ignore within the folder.
  -s, --shuffle         Shuffles the order of the files that make up the
                        animated gif.
  -d DURATION, --duration DURATION
                        Duration between frames in the animated gif (default:
                        0.13).
```