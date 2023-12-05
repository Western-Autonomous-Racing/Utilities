from pathlib import Path
import rosbags.convert as convert
import argparse
from tqdm import tqdm
import sys
import os


def convert_2ros2(input_bags, output_destination, bag_suffix):
    for input_bag in tqdm(input_bags, desc='Converting bags'):
        if bag_suffix == '.bag':
            output_bag = output_destination / input_bag.name.removesuffix('.bag')
        else:
            session_name = Path(input_bag).parent
            if not os.path.exists(output_destination / session_name.name):
                os.mkdir(output_destination / session_name.name)    
            output_bag = output_destination / (str(session_name.name) + '/recording.bag')  # Fix: Convert session_name.name to str
        try:
            convert.convert(input_bag, output_bag)
        except convert.ConverterError as e:
            print(f"Error: {str(e)}")
        

def find_bags(path, bag_suffix):
    path = Path(path)
    if path.is_file():
        return [path]
    
    if bag_suffix == '.db3':
        return [f.parent for f in path.rglob('*.db3')]

    return [f for f in path.rglob('*.bag')]

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
    parser.add_argument('-r', '--ros1_to_ros2', action='store_true', help='Convert from ROS1 bag to ROS2 bag. Optional argument, default is converting from ROS2 to ROS1 bags.')
    args = parser.parse_args()

    bag_suffix = '.bag'
    if not args.ros1_to_ros2:
        bag_suffix = '.db3'

    if not args.input:
        print("Please provide an input folder/bag.")
        parser.print_help()
        sys.exit(0)

    if not args.dest:
        input_path = Path(args.input)
        if input_path.is_file():
            destination_path = Path(args.input).parent
        else:
            destination_path = Path(args.input)
    else:
        destination_path = Path(args.dest)

    input_bags = find_bags(args.input, bag_suffix)
    print(f'Found {len(input_bags)} bags to convert')
    print(f'Starting converting bags to {destination_path}')        

    convert_2ros2(input_bags, destination_path, bag_suffix)

    print(f'Finished converting bags')