import argparse
import imageio
import os


def parse_args():

    desc = "Makes an animated gif from a folder of pictures"  
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument('--verbose', 
        action='store_true',
        help='Boolean flag indicating if statements should be printed to the console.')

    parser.add_argument('--img_folder', type=str,
        required=True,
        help='The folder name that contains images to be made into gifs')

    parser.add_argument('--output_file', type=str,
        default='animation.gif',
        help='The output file of the animed gif')
    
    parser.add_argument('--duration', type=float,
        default=0.13,
        help='Duration between frames in the animated gif (default: %(default)s)')

    parser.add_argument('--types', nargs='+', type=str,
        default=['png', 'jpg'],
        help='The file types to consider when making the animated gifs (default: %(default)s)')
    
    args = parser.parse_args()
    return args


def make_gif(img_folder, output_file, duration, verbose):
    
    if args.verbose: print("Image Folder: ", img_folder, '\n')
    
    files = os.listdir(img_folder)
    if args.verbose: print("Input Files: \n", files, '\n')
    
    filenames = [os.path.join(img_folder, f) for f in files if f.endswith(tuple(args.types))]
    if args.verbose: print("The following file types are used: ", tuple(args.types), '\n')
    
    images = list(map(lambda filename: imageio.imread(filename), filenames))
    
    imageio.mimsave(output_file, images, duration = 0.13)
    if args.verbose: print('Wrote %s' % output_file)


def main():
    global args
    args = parse_args()
    if args.verbose: print(args, '\n')
    make_gif(args.img_folder, args.output_file, args.duration, args.verbose)
    

if __name__ == '__main__':
  main()