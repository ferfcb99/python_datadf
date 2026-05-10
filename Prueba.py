import os
from PIL import Image
import pillow_heif
import rawpy
import imageio

# Initialize HEIC support
pillow_heif.register_heif_opener()

def batch_convert_to_png(source_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Supported extensions
    extensions = ('.heic', '.dng', '.jpg', '.jpeg')

    for filename in os.listdir(source_folder):
        file_ext = os.path.splitext(filename)[1].lower()
        file_path = os.path.join(source_folder, filename)
        target_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".png")

        if file_ext in extensions:
            print(f"Converting: {filename}...")
            try:
                if file_ext == '.dng':
                    # Special handling for RAW DNG files
                    with rawpy.imread(file_path) as raw:
                        rgb = raw.postprocess()
                        imageio.imsave(target_path, rgb)
                else:
                    # Handling for HEIC and standard formats
                    img = Image.open(file_path)
                    img.save(target_path, "PNG")
                
                print(f"Success: Saved to {target_path}")
            
            except Exception as e:
                print(f"Error converting {filename}: {e}")

# --- SET YOUR PATHS HERE ---
input_dir = r'C:\Users\fer_f\Downloads\Photos'  # Change this to your folder path
output_dir = r'C:\Users\fer_f\Downloads\Photos\Converted'  # Change this to your desired output folder path

batch_convert_to_png(input_dir, output_dir)