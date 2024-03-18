# ImageGenExif

## Overview
ImageGenExif is a Python application designed to generate a specified number of images with randomized EXIF data. Each image is assigned a solid color, a random orientation (landscape or portrait), and includes EXIF metadata such as a random timestamp within the last three years and GPS coordinates from predefined locations in Alberta, Canada.

## Installation

Before running ImageGenExif, you need to install the required Python packages. Make sure you have Python and pip installed on your system and then run the following command in the terminal to install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage
To use ImageGenExif, you simply need to specify the number of photos you wish to generate and the output directory where the photos will be saved. Here is the command line syntax:

```bash
python generate_photos.py [number_of_photos] [output_directory]
```

### Example
To generate 10 photos and save them in a directory named "output_photos" in the current directory, you would run:

```bash
python generate_photos.py 10 ./output_photos
```

If the directory does not exist, ImageGenExif will create it for you.
