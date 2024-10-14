from module.TxtReader import TxtReader
from module.TxtWriter import TxtWriter

class HuffmanDecoder:
    def __init__(self):
        self.coded_string = b""  # Use bytes to handle binary data
        self.binary_chars = ""
        self.decoded_string = ""
        self.codes = {}
        self.added_int = 0

    def decoder(self, input_file="examples/codedExample.txt", output_file="examples/decodedExample.txt"):
        self.coded_file_reader(input_file)

        if len(self.coded_string) == 0:
            print("Error: coded_string is empty.")
            return

        characters_in_set = self.coded_string[0] 
        print(f"Characters in set (during decoding): {characters_in_set}")

        if len(self.coded_string) < characters_in_set + 1:
            print("Error: coded_string is too short to contain the full dictionary.")
            return

        for i in range(characters_in_set):
            char = chr(self.coded_string[i + 1])  
            if i < 2:
                self.codes[char] = "0" + format(i, 'b')
            else:
                self.codes[char] = format(i, 'b')

        print(f"Decoded dictionary: {self.codes}")


        coded_text_with_dictionary = self.coded_string[characters_in_set + 1:]

        builder = []
        for byte in coded_text_with_dictionary:
            binary = format(byte, '08b')
            builder.append(binary)

        self.binary_chars = "".join(builder)


        padding_info = self.binary_chars[:3]
        padding_length = int(padding_info, 2)
        self.binary_chars = self.binary_chars[3:] 

        if padding_length > 0:
            self.binary_chars = self.binary_chars[:-padding_length]

        print(f"Binary chars before decoding: {self.binary_chars}")

        decoded_output = []
        buffer = ""
        for bit in self.binary_chars:
            buffer += bit
            if buffer in self.codes.values():
                for char, code in self.codes.items():
                    if buffer == code:
                        decoded_output.append(char)
                        buffer = ""
                        break

        print(f"Decoded output before joining: {decoded_output}")

        self.decoded_string = "".join(decoded_output)
        print(f"Decoded string: {self.decoded_string}")


        TxtWriter.write_file(self.decoded_string, output_file)


    def coded_file_reader(self, input_file):
        self.coded_string = TxtReader.read_file(input_file, binary=True)