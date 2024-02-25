from PIL import Image
import os

def resize_and_optimize_images(source_folder, destination_folder, max_width, max_height, quality=85):
    """
    Resizes and optimizes images from a source folder and saves them to a destination folder.
    :param source_folder: The folder containing the images to be processed.
    :param destination_folder: The folder where the processed images will be saved.
    :param max_width: Maximum width of the resized images.
    :param max_height: Maximum height of the resized images.
    :param quality: Quality for image saving, defaults to 85. Higher values retain more quality.
    """
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(source_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            file_path = os.path.join(source_folder, filename)
            image = Image.open(file_path)
            
            # Calculate the new image size
            img_ratio = image.width / image.height
            target_ratio = max_width / max_height
            if img_ratio >= target_ratio:
                # Width is the limiting factor
                new_width = min(image.width, max_width)
                new_height = round(new_width / img_ratio)
            else:
                # Height is the limiting factor
                new_height = min(image.height, max_height)
                new_width = round(new_height * img_ratio)
            
            # Resize and optimize the image
            resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
            optimized_path = os.path.join(destination_folder, filename)
            resized_image.save(optimized_path, quality=quality, optimize=True)

source_folder = 'source'
destination_folder = 'dest'
max_width = 1280  # Example width
max_height = 1280  # Example height

resize_and_optimize_images(source_folder, destination_folder, max_width, max_height)
