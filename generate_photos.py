import argparse
from multiprocessing import Pool
import os
from image_creator import create_image_with_exif

def parse_args():
    """
    Parses command line arguments for the script.

    Returns:
        Namespace: An argparse Namespace instance containing parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description='Generate photos with randomized EXIF data including timestamp and GPS coordinates.'
    )
    parser.add_argument(
        'num_photos', type=int, 
        help='The number of photos to generate.'
    )
    parser.add_argument(
        'output_folder', type=str, 
        help='The output folder where the generated photos will be saved.'
    )
    return parser.parse_args()

def main():
    """
    Main function to generate photos with EXIF data.

    This function handles parsing command line arguments, creating the
    output directory if it does not exist, and initiating the parallel
    processing to generate the specified number of photos.
    """
    # Parse command line arguments
    args = parse_args()

    # Ensure the output folder exists; create it if necessary
    if not os.path.exists(args.output_folder):
        os.makedirs(args.output_folder)

    # Prepare tasks for parallel execution. Each task consists of an
    # index and the output folder path.
    tasks = [(i, args.output_folder) for i in range(args.num_photos)]

    # Use multiprocessing to generate photos in parallel, improving efficiency
    with Pool() as pool:
        pool.starmap(create_image_with_exif, tasks)

if __name__ == "__main__":
    main()
