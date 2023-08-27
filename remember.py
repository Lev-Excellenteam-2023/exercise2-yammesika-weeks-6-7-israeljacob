from PIL import Image


def encrypted_message(path: str) -> str:
    """
    Extracts an encrypted message from an image.

    Parameters:
        path (str): The path to the image file.

    Returns:
        str: The extracted encrypted message.
    """
    image = Image.open(path)
    width, height = image.size
    return "".join(chr(y) for x in range(width) for y in range(height) if image.getpixel((x, y)) == 1)


print(encrypted_message('code.png'))
# Place gunpowder beneath the House of Lords. 11/05/1605
