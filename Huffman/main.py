from encoding.HuffmanEncoder import HuffmanEncoder
from decoding.HuffmanDecoder import HuffmanDecoder

def main():
    encoder = HuffmanEncoder()
    decoder = HuffmanDecoder()

    encoder.file_name = "do_kompresji.txt"  
    encoder.encode_string("examples/skompresowany.txt") 
    decoder.decoder("examples/skompresowany.txt", "examples/zdekompresowany.txt") 

if __name__ == "__main__":
    main()

