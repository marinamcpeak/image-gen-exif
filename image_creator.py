from PIL import Image
import piexif
import os
from datetime import datetime, timedelta
import random

# List of ten distinct locations within Alberta, Canada, each defined by
# a name, latitude (lat), and longitude (lon) in degrees, minutes, seconds.
locations = [
    {"name": "Edmonton", "lat": (53, 32, 0), "lon": (-113, 30, 0)},
    {"name": "Calgary", "lat": (51, 2, 0), "lon": (-114, 3, 0)},
    {"name": "Banff", "lat": (51, 10, 0), "lon": (-115, 34, 0)},
    {"name": "Jasper", "lat": (52, 52, 0), "lon": (-118, 5, 0)},
    {"name": "Lethbridge", "lat": (49, 41, 0), "lon": (-112, 50, 0)},
    {"name": "Medicine Hat", "lat": (50, 2, 0), "lon": (-110, 40, 0)},
    {"name": "Fort McMurray", "lat": (56, 43, 0), "lon": (-111, 23, 0)},
    {"name": "Grande Prairie", "lat": (55, 10, 0), "lon": (-118, 48, 0)},
    {"name": "Red Deer", "lat": (52, 16, 0), "lon": (-113, 48, 0)},
    {"name": "Drumheller", "lat": (51, 27, 45), "lon": (-112, 42, 59)},
]

def generate_random_timestamp():
    """
    Generates a random timestamp within the last three years.

    Returns:
        str: The timestamp in the format YYYY:MM:DD HH:MM:SS.
    """
    end = datetime.now()
    start = end - timedelta(days=3*365)
    random_time = start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))
    return random_time.strftime("%Y:%m:%d %H:%M:%S")

def create_image_with_exif(idx, output_folder):
    """
    Creates an image with randomized attributes and EXIF data.

    Parameters:
        idx (int): Index used to generate a unique filename.
        output_folder (str): Path to the folder where the image will be saved.
    """
    # Randomly choose the image orientation and size
    image_size = random.choice([(1280, 720), (720, 1280)])
    
    # Randomly generate an RGB color
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    # Select a random location from predefined locations
    location = random.choice(locations)
    
    # Generate a random timestamp within the last three years
    timestamp = generate_random_timestamp()

    # Construct the EXIF data dictionary
    exif_dict = {
        "0th": {
            piexif.ImageIFD.Make: "Python",
            piexif.ImageIFD.Software: "Pillow & Piexif"
        },
        "Exif": {
            piexif.ExifIFD.DateTimeOriginal: timestamp,
            piexif.ExifIFD.LensMake: "Virtual Lens",
        },
        "GPS": {
            piexif.GPSIFD.GPSLatitudeRef: 'N' if location["lat"][0] >= 0 else 'S',
            piexif.GPSIFD.GPSLatitude: [(abs(location["lat"][0]), 1), (location["lat"][1], 1), (location["lat"][2], 1)],
            piexif.GPSIFD.GPSLongitudeRef: 'E' if location["lon"][0] >= 0 else 'W',
            piexif.GPSIFD.GPSLongitude: [(abs(location["lon"][0]), 1), (location["lon"][1], 1), (location["lon"][2], 1)],
        }
    }
    
    # Dump the EXIF data into bytes and create the image
    exif_bytes = piexif.dump(exif_dict)
    img = Image.new('RGB', image_size, color=color)
    filename = f"photo_{idx:05d}.jpg"
    filepath = os.path.join(output_folder, filename)
    img.save(filepath, exif=exif_bytes)
