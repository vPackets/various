import os
from heic2png import HEIC2PNG
from PIL import Image

input_folder = "."
output_folder = os.path.join(input_folder, "converted_pngs")
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith(".HEIC"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".png")

        print(f"Converting {filename} to {output_path}")
        try:
            # Convert HEIC to PNG (temporary path)
            temp_png = os.path.join(output_folder, "__temp.png")
            heic_img = HEIC2PNG(input_path, quality=90)
            heic_img.save(temp_png)

            # Open the temp PNG and resize it
            with Image.open(temp_png) as img:
                new_size = (
                    int(img.width * 0.6),
                    int(img.height * 0.6)
                )
                resized = img.resize(new_size, Image.LANCZOS)
                resized.save(output_path, format="PNG")
                print(f"✅ Saved resized PNG: {output_path}")

            # Remove temp file
            os.remove(temp_png)

        except Exception as e:
            print(f"❌ Failed to process {filename}: {e}")

