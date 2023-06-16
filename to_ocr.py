import os
import pytesseract
from PIL import Image


def process_images(num_images, output_file):
    try:
        num_images = int(num_images)
    except ValueError:
        print("Invalid input. Please enter a valid number of images.")
        return

    output_file = output_file.strip()
    if not output_file.endswith('.txt'):
        output_file += '.txt'

    with open(output_file, 'a') as f:
        for x in range(1, num_images + 1):
            image_file = f"image {x}.jpg"
            if not os.path.exists(image_file):
                print(f"Image '{image_file}' not found. Skipping...")
                continue

            f.write(f'\n###### Image {x} Data #####\n')
            image = Image.open(image_file)
            text = pytesseract.image_to_string(image)
            f.write(text + '\n')
            f.write(f'###### Image {x} Data END #####\n')
            os.system('clear')
            print(f'Progress: {int((x / num_images) * 100)}%')

    print("Completed")


if __name__ == '__main__':
    num_images = input("Total Images? ")
    process_images(num_images, 'data.txt')
    input("Press Enter to Exit :)")