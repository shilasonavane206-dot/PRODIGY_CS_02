
from PIL import Image, ImageFilter

# Secret encryption key
key = 50

# Open original image
img = Image.open("input.png").convert("RGB")

# --------------------------------
# 1. IMAGE ENCRYPTION
# --------------------------------

encrypted_img = Image.new("RGB", img.size)

for x in range(img.width):
    for y in range(img.height):

        r, g, b = img.getpixel((x, y))

        # XOR encryption
        new_pixel = (
            r ^ key,
            g ^ key,
            b ^ key
        )

        encrypted_img.putpixel((x, y), new_pixel)

# Save encrypted image
encrypted_img.save("encrypted.png")

print("Image encrypted successfully!")


# --------------------------------
# 2. IMAGE DECRYPTION
# --------------------------------

encrypted_image = Image.open("encrypted.png").convert("RGB")

decrypted_img = Image.new("RGB", encrypted_image.size)

for x in range(encrypted_image.width):
    for y in range(encrypted_image.height):

        r, g, b = encrypted_image.getpixel((x, y))

        # XOR decryption using same key
        original_pixel = (
            r ^ key,
            g ^ key,
            b ^ key
        )

        decrypted_img.putpixel((x, y), original_pixel)

# Save decrypted image
decrypted_img.save("decrypted.png")

print("Image decrypted successfully!")


# --------------------------------
# 3. BLACK & WHITE BLUR EFFECT
# --------------------------------

bw_img = img.convert("L")

blurred_img = bw_img.filter(
    ImageFilter.GaussianBlur(radius=100)
)

blurred_img.save("black_white_blur.png")

print("Black & White Blur created successfully!")

print("All tasks completed!")
