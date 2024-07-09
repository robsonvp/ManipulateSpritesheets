from PIL import Image
import os

def cut_spritesheet(file_path, output_folder, sprite_size=(32, 32)):
    # Load the image
    try:
        sheet = Image.open(file_path)
    except IOError:
        print("Unable to load sprite sheet.")
        return

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Calculate the number of sprites in each row and column
    sheet_width, sheet_height = sheet.size
    columns = sheet_width // sprite_size[0]
    rows = sheet_height // sprite_size[1]

    # Loop through each sprite and save it
    count = 0
    for row in range(rows):
        for col in range(columns):
            # Define the bounding box of the sprite
            left = col * sprite_size[0]
            top = row * sprite_size[1]
            right = left + sprite_size[0]
            bottom = top + sprite_size[1]
            bbox = (left, top, right, bottom)

            # Crop the sprite
            sprite = sheet.crop(bbox)

            # Save the sprite
            sprite_file_name = f"sprite_{count}.png"
            sprite.save(os.path.join(output_folder, sprite_file_name))
            print(f"Saved {sprite_file_name}")
            count += 1

if __name__ == "__main__":
    # Path to your sprite sheet
    sprite_sheet_path = "C:\\Users\\binho\\Desktop\\Juegos\\CustomScripts\\demoniaMule\\outfit_1302.png"
    # Directory where you want to save the tiles
    output_directory = "C:\\Users\\binho\\Desktop\\Juegos\\CustomScripts\\demoniaMule"

    cut_spritesheet(sprite_sheet_path, output_directory)

