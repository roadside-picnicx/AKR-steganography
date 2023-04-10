from utils import *
from PIL import Image
import hashlib


class Decoder:
    def __init__(self,file_path):
        while True:
            try:
                self.file_path = file_path  # change to input or connect to gui
                self.__image__ = Image.open(self.file_path)
                break
            except FileNotFoundError as e:
                print('Choose correct file and extension')

        self.__image__ = Image.open(self.file_path)
        self.__pixels__ = list(self.__image__.getdata())
        self.__msg_length_binary__ = ""
        self.__msg_binary__ = ""

    # calculate decimal value of message length from binary
    # calculate length of message in binary
    def __get_msg_length__(self):
        self.__msg_length__ = int(self.__msg_length_binary__, base=2)
        self.__msg_binary_length__ = self.__msg_length__ * 8

    # parse message to bytes from message binary string and convert it
    def __get_msg__(self):
        chars_bin = []
        position = 0
        for i in range(self.__msg_length__):
            letter_bin = ""
            for bit in list(self.__msg_binary__)[position:]:
                letter_bin += bit
                position += 1
                if position % 8 == 0:
                    break
            chars_bin.append(letter_bin)
        self.__msg__ = convert_binary_to_ascii(chars_bin)

    # main method
    def decode(self):
        self.__decode_msg_length__()
        self.__decode_msg__()
        self.__file_hash()

    # decode msg length from the first 3 pixels as 8 bit number
    def __decode_msg_length__(self):
        position = 0
        for pixel in self.__pixels__:
            # get binary representation of decimal number which was in input image for all colors
            red_bin = bin(pixel[0])[2:]
            green_bin = bin(pixel[1])[2:]
            blue_bin = bin(pixel[2])[2:]

            # get last bit of color and add it to message length binary
            self.__msg_length_binary__ += red_bin[-1]
            position += 1
            if position == 8:
                break

            self.__msg_length_binary__ += green_bin[-1]
            position += 1
            if position == 8:
                break

            self.__msg_length_binary__ += blue_bin[-1]
            position += 1
            if position == 8:
                break

        self.__get_msg_length__()

    def __decode_msg__(self):
        # decode msg from the rest of the pixels
        position = 0
        skip_pixel_count = 3
        for pixel in self.__pixels__:
            # skip first 3 pixels because message length was already decoded
            if skip_pixel_count != 0:
                skip_pixel_count -= 1
                continue

            # get binary representation of decimal number which was in input image for all colors
            red_bin = bin(pixel[0])[2:]
            green_bin = bin(pixel[1])[2:]
            blue_bin = bin(pixel[2])[2:]

            # get last bit of color and add it to message binary
            self.__msg_binary__ += red_bin[-1]
            position += 1
            if position == self.__msg_binary_length__:
                break

            self.__msg_binary__ += green_bin[-1]
            position += 1
            if position == self.__msg_binary_length__:
                break

            self.__msg_binary__ += blue_bin[-1]
            position += 1
            if position == self.__msg_binary_length__:
                break

        self.__get_msg__()

    def __file_hash(self):
        # for old file
        sha256 = hashlib.sha256()
        with open(self.file_path, "rb") as f:
            while True:
                data = f.read(65536)  # arbitrary number to reduce RAM usage
                if not data:
                    break
                sha256.update(data)
        print(f"File hash: {sha256.hexdigest()}")

    # print decoded output
    #def show_decoded_output(self):
        #print("Hidden message was: " + self.__msg__ +"\n")


