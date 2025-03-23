import os
import random
from PIL import Image, ImageDraw, ImageFont

# Configuration
IMAGES_FOLDER = "verstappen_images"
FONT_PATH = "arial.ttf"  # Replace with a meme-style font path if available
OUTPUT_FOLDER = "generated_memes"

# Optional default Verstappen quotes
default_quotes = [
    "I was just cruising, mate.",
    "It's lights out and away I dominate!",
    "Max wins again? Shock horror!",
    "Another Grand Chelem? Why not.",
    "P1? You already know.",
    "They tried. I flew.",
    "This car is a rocket ship."
]

def list_images():
    image_files = [f for f in os.listdir(IMAGES_FOLDER) if f.endswith(('jpg', 'jpeg', 'png'))]
    for idx, file in enumerate(image_files):
        print(f"{idx + 1}: {file}")
    return image_files

def get_user_quote():
    quote = input("Enter your Verstappen meme quote (or press enter for a random one): ")
    return quote if quote.strip() else random.choice(default_quotes)

def get_user_image(image_files):
    try:
        choice = int(input("Pick an image number (or 0 for random): "))
        if choice == 0:
            return random.choice(image_files)
        else:
            return image_files[choice - 1]
    except (ValueError, IndexError):
        print("Invalid input. Using random image.")
        return random.choice(image_files)

def generate_meme(image_path, quote):
    img = Image.open(os.path.join(IMAGES_FOLDER, image_path))
    draw = ImageDraw.Draw(img)

    # Font settings
    width, height = img.size
    font_size = int(width / 18)
    font = ImageFont.truetype(FONT_PATH, font_size)

    # Text size & position
    bbox = draw.textbbox((0, 0), quote, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = (width - text_width) / 2
    y = height - text_height - 40

    # Draw outline
    outline_range = 2
    for dx in range(-outline_range, outline_range + 1):
        for dy in range(-outline_range, outline_range + 1):
            draw.text((x + dx, y + dy), quote, font=font, fill="black")

    # Draw main text
    draw.text((x, y), quote, font=font, fill="white")

    # Save the meme
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
    filename = f"verstappen_meme_{random.randint(1000,9999)}.jpg"
    output_path = os.path.join(OUTPUT_FOLDER, filename)
    img.save(output_path)
    print(f"\n✅ Meme generated and saved as: {output_path}")

def main():
    print("🔥 Verstappen Meme Generator 🔥")
    image_files = list_images()
    quote = get_user_quote()
    image_choice = get_user_image(image_files)
    generate_meme(image_choice, quote)

if __name__ == "__main__":
    main()