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
        help='The folder name that contains images to be made into gifs', 
        required=True)

    parser.add_argument('--output_file', type=str,
        help='The folder name that contains images to be made into gifs', 
        required=True)
    
    parser.add_argument('--duration', type=float,
        default=0.13,
        help='Duration between frames in the animated gif (default: %(default)s)')
    
    args = parser.parse_args()
    return args


def make_gif(img_folder, output_file, duration, verbose):

    output_folder = os.path.join('image_output', 'alina_final_result')
    if args.verbose: print(output_folder)
    
    files = os.listdir(output_folder)
    if args.verbose: print(files)

    filenames = [os.path.join(output_folder, x) for x in files if x.endswith(('.png'))]
    images = list(map(lambda filename: imageio.imread(filename), filenames))
    output_file = os.path.join(output_folder, 'animated.gif')
    if os.path.exists(output_file): os.remove(output_file)
    imageio.mimsave(os.path.join(output_file), images, duration = 0.13)




def main():
    global args
    args = parse_args()
    if args.verbose: print(args)
    make_gif(args.img_folder, args.output_file, args.duration)
    

if __name__ == '__main__':
  main()