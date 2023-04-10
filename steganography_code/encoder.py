from utils import *
from PIL import Image
import hashlib


# maximum length of message is 255 characters
# input doesn't accept for example ř, č..
class Encoder:
    def __init__(self, file_path, user_message, output_name):
        while True:
            try:
                self.file_path = file_path
                self.__image__ = Image.open(self.file_path)
                self.output_name = output_name
                break
            except FileNotFoundError as e:
                print('Choose correct file and extension')

        while True:
            try:
                self.__msg__ = user_message
                if (len(self.__msg__) == 0 or len(self.__msg__) > 255):
                    raise ValueError
                break
            except ValueError:
                print('Message is either too long or too short, please enter a message between 1 and 255 characters')

        self.__msg_binary__ = convert_ascii_to_binary(self.__msg__)
        self.__msg_binary_length__ = len(self.__msg_binary__)
        self.__msg_length__ = len(self.__msg__)
        self.__msg_length_binary__ = format_bits_to_correct_length(
            bin(self.__msg_length__)[2:]
        )
        self.__new_image__ = self.__image__
        self.__pixels__ = list(self.__image__.getdata())

    # formats binary values for pixel colors as numeric values in tuple
    # example "0000 0001" "0000 0010" "0000 0100" -> "(1,2,4)"
    def __get_pixel_data__(self, red_bin, green_bin, blue_bin):
        return (int(red_bin, base=2), int(green_bin, base=2), int(blue_bin, base=2))

    # main method
    def encode(self):
        self.__encode_msg_length__()
        self.__encode_msg__()
        self.__new_image__.putdata(self.__pixels__)
        while True:
            try:
                self.__file_out__ = self.output_name
                self.__new_image__.save(self.__file_out__, str(self.__file_out__.split(".")[1].upper()))
                break
            except KeyError:
                print('Please only use .png extension')

        self.__file_hash()

    # encode msg length in the first 3 pixels as 8 bit number
    def __encode_msg_length__(self):
        position = 0
        pixel_num = 0
        for pixel in self.__pixels__:
            # get binary representation of decimal number which was in input image for all colors
            red_bin = bin(pixel[0])[2:]
            green_bin = bin(pixel[1])[2:]
            blue_bin = bin(pixel[2])[2:]

            # if last bit doesn't equal to current bit of message length binary number change it
            if red_bin[-1] != self.__msg_length_binary__[position]:
                red_bin = change_last_bit(red_bin)
            position += 1
            if position == 8:
                self.__pixels__[pixel_num] = self.__get_pixel_data__(
                    red_bin, green_bin, blue_bin
                )
                break

            if green_bin[-1] != self.__msg_length_binary__[position]:
                green_bin = change_last_bit(green_bin)
            position += 1
            if position == 8:
                self.__pixels__[pixel_num] = self.__get_pixel_data__(
                    red_bin, green_bin, blue_bin
                )
                break

            if blue_bin[-1] != self.__msg_length_binary__[position]:
                blue_bin = change_last_bit(blue_bin)
            position += 1
            if position == 8:
                self.__pixels__[pixel_num] = self.__get_pixel_data__(
                    red_bin, green_bin, blue_bin
                )
                break
            self.__pixels__[pixel_num] = self.__get_pixel_data__(
                red_bin, green_bin, blue_bin
            )
            pixel_num += 1

    # encode msg in the rest of the pixels
    def __encode_msg__(self):
        position = 0
        pixel_num = 0
        for pixel in self.__pixels__:
            # skip first 3 pixels because there is already a message length encoded
            if pixel_num < 3:
                pixel_num += 1
                continue

            # get binary representation of decimal number which was in input image for all colors
            red_bin = bin(pixel[0])[2:]
            green_bin = bin(pixel[1])[2:]
            blue_bin = bin(pixel[2])[2:]

            # if last bit doesn't equal to current bit of message change it
            if red_bin[-1] != self.__msg_binary__[position]:
                red_bin = change_last_bit(red_bin)
            position += 1
            if position == self.__msg_binary_length__:
                self.__pixels__[pixel_num] = self.__get_pixel_data__(
                    red_bin, green_bin, blue_bin
                )
                break

            if green_bin[-1] != self.__msg_binary__[position]:
                green_bin = change_last_bit(green_bin)
            position += 1
            if position == self.__msg_binary_length__:
                self.__pixels__[pixel_num] = self.__get_pixel_data__(
                    red_bin, green_bin, blue_bin
                )
                break

            if blue_bin[-1] != self.__msg_binary__[position]:
                blue_bin = change_last_bit(blue_bin)
            position += 1
            if position == self.__msg_binary_length__:
                self.__pixels__[pixel_num] = self.__get_pixel_data__(
                    red_bin, green_bin, blue_bin
                )
                break
            self.__pixels__[pixel_num] = self.__get_pixel_data__(
                red_bin, green_bin, blue_bin
            )
            pixel_num += 1

    def __file_hash(self):
        #for old file
        sha256 = hashlib.sha256()
        with open(self.file_path, "rb") as f:
            while True:
                data = f.read(65536) #arbitrary number to reduce RAM usage
                if not data:
                    break
                sha256.update(data)
        print(f"Old file hash: {sha256.hexdigest()}")

        #for new file
        sha256 = hashlib.sha256()
        with open(self.__file_out__, "rb") as f:
            while True:
                data = f.read(65536)
                if not data:
                    break
                sha256.update(data)
        print(f"New file hash: {sha256.hexdigest()}")


