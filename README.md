# Utilities
Useful Scripts and Commands to get things to work

# Setup

```bash
git clone https://github.com/Western-Autonomous-Racing/Utilities.git
cd Utilities
chmod +x init.sh
```

# ROS2 Utilities

## ROS1 to ROS2 Bag Conversion

Using `convert_2ros2.py`.

```bash
usage: convertros2 [-h] [-i INPUT] [-d [DEST]]

A utility to convert ROS1 bag(s) to ROS2 bag(s)

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input folder/bag
  -d [DEST], --dest [DEST]
                        Output folder destination. Default where your input folder is.
```