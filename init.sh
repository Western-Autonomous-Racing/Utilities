#!/bin/bash

# Add convert_2ros2.py to .bashrc
echo "alias convertros2='python $(pwd)/ros2/convert_2ros2.py'" >> ~/.bashrc


# Source the terminal
source ~/.bashrc
