import argparse

def parse_args():
    desc = "Makes an animated gif from a series of pictures"  
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument('--verbose', 
        action='store_true',
        help='Boolean flag indicating if statements should be printed to the console.')

    parser.add_argument('--img_folder', type=str,
        help='The folder name that contains images to be made into gifs', 
        required=True)
    
    parser.add_argument('--duration', type=float,
        default=0.13,
        help='Duration between frames in the animated gif (default: %(default)s)')
    
    args = parser.parse_args()
    return args




def main():
    global args
    args = parse_args()
    

if __name__ == '__main__':
  main()