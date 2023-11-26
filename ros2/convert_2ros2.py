from pathlib import Path
import rosbags.convert as convert
import argparse
from tqdm import tqdm


def convert_2ros2(input_bags, output_destination):
    for input_bag in tqdm(input_bags, desc='Converting bags'):
        output_bag = output_destination / input_bag.name.removesuffix('.bag')
        try:
            convert.convert(input_bag, output_bag)
        except convert.ConverterError:
            print(f"Skipping {input_bag.name}: Output directory already exists")
        

def find_bags(path):
    path = Path(path)
    if path.is_file():
        return [path]
    return [f for f in path.iterdir() if f.suffix == '.bag']

if __name__ == '__main__':
    """
    This script converts a ROS1 bag to a ROS2 bag.
    Usage:
        python convert_2ros2.py <input folder/bag> <output folders/bags>
    """

    destination_path = Path.cwd()

    parser = argparse.ArgumentParser(prog='convertros2', description='A utility to convert ROS1 bag(s) to ROS2 bag(s)')

    parser.add_argument('-i', '--input', type=str, help='Input folder/bag')
    parser.add_argument('-d', '--dest', type=str, help='Output folder destination. Default where your input folder is. Optional argument, default is input folder file.', nargs='?', const='')

    args = parser.parse_args()

    if not args.input:
        print("Please provide an input folder/bag.")
        parser.print_help()
        exit()

    if not args.dest:
        input_path = Path(args.input)
        if input_path.is_file():
            destination_path = Path(args.input).parent
        else:
            destination_path = Path(args.input)
    else:
        destination_path = Path(args.dest)

    input_bags = find_bags(args.input)
    print(f'Found {len(input_bags)} bags to convert')
    print(f'Starting converting bags to {destination_path}')        

    convert_2ros2(input_bags, destination_path)

    print(f'Finished converting bags')