from PIL import Image
import os

def convert_png_to_webp(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if filename.endswith('.png'):
            img = Image.open(os.path.join(input_dir, filename))
            output_filename = os.path.splitext(filename)[0] + '.webp'
            img.save(os.path.join(output_dir, output_filename), 'webp')
            print(f"Converted {filename} to {output_filename}")

input_directory = 'images'
output_directory = 'images'
convert_png_to_webp(input_directory, output_directory)