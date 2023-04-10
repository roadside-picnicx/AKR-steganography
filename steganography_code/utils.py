#basic utilities like converting to binary from ascii and vice versa
# example "1010" -> "1011"
def change_last_bit(bits):
    position = -1
    tmp = list(bits)
    tmp[-1] = "1" if bits[-1] == "0" else "0"
    return "".join(tmp)


# example "11 1010" -> "0011 1010"
def format_bits_to_correct_length(bits):
    if len(bits) == 8:
        return bits
    else:
        return f"{'0'*(8-len(bits))}{bits}"


# example "a" -> "01010101"
def get_ascii_code(char):
    return format_bits_to_correct_length(bin(ord(char))[2:])


# example "uwu" -> "000010010001010110110010"
def convert_ascii_to_binary(msg):
    bits = ""
    for char in msg:
        bits = bits + get_ascii_code(char)
    return bits


# example "[01110111, 11010111]" -> "ad"
def convert_binary_to_ascii(chars_bin):
    chars = []
    for char_bin in chars_bin:
        chars.append(chr(int(char_bin, base=2)))
    return "".join(chars)
