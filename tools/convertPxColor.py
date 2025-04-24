from PIL import Image
import os
import sys

def process_image(file_path):
    """Process a single image file to change white pixels to red."""
    with Image.open(file_path) as img:
        img = img.convert("RGBA")
        pixels = img.load()
        
        # Modify white pixels to red
        for y in range(img.height):
            for x in range(img.width):
                r, g, b, a = pixels[x, y]
                pixels[x, y] = (0, g, 0, a)  # Change to red
        print(f"Changed white pixels to red in {file_path}.")
        # Save the modified image
        img.save(file_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convertPxColor.py <path>")
        sys.exit(1)

    user_path = sys.argv[1]

    if os.path.isdir(user_path):
        print(f"Processing files in directory: {user_path}")

        # Iterate over all PNG files in the directory
        for file_name in os.listdir(user_path):
            if file_name.endswith('.png'):
                file_path = os.path.join(user_path, file_name)
                process_image(file_path)

        print("All white pixels have been changed to red in PNG files.")

    elif os.path.isfile(user_path) and user_path.endswith('.png') or user_path.endswith('.dds'):
        print(f"Processing single file: {user_path}")
        process_image(user_path)
        print("White pixels have been changed to red in the file.")

    else:
        print("The provided path is not a valid directory or PNG file.")
