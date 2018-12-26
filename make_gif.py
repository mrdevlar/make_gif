import argparse
import imageio
import moviepy.editor as mp
import os
import random


def parse_args():

    desc = "Makes an animated gif from a folder of pictures"  
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument('img_folder', type=str,
        help='The folder name that contains images to be made into a gif.')

    parser.add_argument('-v', '--verbose', action='store_true',
        help='Boolean flag indicating if statements should be printed to the console.')

    parser.add_argument('-o', '--output_file', type=str,
        default='animation.gif',
        help='The output file of the animated gif or webm (default: %(default)s).')

    parser.add_argument('-t','--types', nargs='+', type=str,
        default=['png', 'jpg'],
        help='The file types to consider when making the animated gifs (default: %(default)s).')

    parser.add_argument('-i', '--ignore_files', nargs='+', type=str,
        default=[],
        help='List of files to ignore within the folder.')

    parser.add_argument('-s', '--shuffle', action='store_true',
        help='Shuffles the order of the files that make up the animated gif.')
    
    group = parser.add_mutually_exclusive_group()

    group.add_argument('-d', '--duration', type=float,
        default=0.13,
        help='Duration between frames in the animated gif (default: %(default)s).')
    
    # @TODO Speed Argument using count and add to group
    
    args = parser.parse_args()
    return args


def make_gif(img_folder, output_file, duration, types, verbose, shuffle, ignore_files):
    
    if verbose: print("Image Folder: ", img_folder, '\n')
    
    files = os.listdir(img_folder)
    if verbose: print("Input Files: \n", files, '\n')

    if ignore_files: 
        files = list(set(files) - set(ignore_files))

    
    filenames = [os.path.join(img_folder, f) for f in files if f.endswith(tuple(types))]

    if verbose: print("The following file types are used: ", tuple(types), '\n')

    if shuffle: random.shuffle(filenames)
    if verbose: print("Shuffling images\n")
    
    images = list(map(lambda filename: imageio.imread(filename), filenames))
    
    if os.path.exists(output_file): os.remove(output_file)
    
    
    
    if output_file.endswith('gif'):
        imageio.mimsave(output_file, images, duration = 0.13)
    elif output_file.endswith('webm'):
        imageio.mimsave('temp.gif', images, duration = 0.13)
        clip = mp.VideoFileClip('temp.gif')
        clip.write_videofile(output_file, preset="high")
        clip.close()
        os.remove('temp.gif') 
    if verbose: print('Wrote %s' % output_file)
    

def main():
    global args
    args = parse_args()
    if args.verbose: print("Input Arguments\n", args, '\n')
    
    make_gif(img_folder = args.img_folder, 
            output_file = args.output_file, 
            duration    = args.duration, 
            types       = args.types, 
            verbose     = args.verbose, 
            shuffle     = args.shuffle,
            ignore_files= args.ignore_files)
    

if __name__ == '__main__':
  main()
