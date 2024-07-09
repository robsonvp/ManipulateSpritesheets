from PIL import Image
import os

def resize_image(input_path, output_path, size=(64, 64)):
    try:
        with Image.open(input_path) as img:
            # Use LANCZOS filter for high-quality downsampling
            img = img.resize(size, Image.LANCZOS)
            img.save(output_path, quality=95)  # Save with high quality
            print(f"Resized {input_path} and saved to {output_path}")
    except Exception as e:
        print(f"Failed to resize {input_path}: {e}")

def resize_images_in_range(start, end, input_dir, output_dir, size=(64, 64)):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    for i in range(start, end + 1):
        input_filename = f"sprite_{i}.png"  # Changed to .png as per your example
        output_filename = f"sprite_{i}.png"
        input_path = os.path.join(input_dir, input_filename)
        output_path = os.path.join(output_dir, output_filename)
        
        resize_image(input_path, output_path, size)

# Example usage
input_directory = 'C:/exampleInputFolder'
output_directory = 'C:/exampleOutputFolder'
resize_images_in_range(0, 251, input_directory, output_directory)
