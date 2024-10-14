from encoding.HuffmanEncoder import HuffmanEncoder
from decoding.HuffmanDecoder import HuffmanDecoder

def main():
    choice = input("Wybierz opcję: (1) Zakoduj plik, (2) Odkoduj plik: ")

    if choice == "1":
        encoder = HuffmanEncoder()
        encoder.file_name = "do_kompresji.txt"  
        encoder.encode_string("examples/skompresowany.txt")
    
    elif choice == "2":
        decoder = HuffmanDecoder()
        decoder.decoder("examples/skompresowany.txt", "examples/zdekompresowany.txt")
        print("Plik został odkodowany i zapisany w 'examples/decodedExample.txt'.")
    
    else:
        print("Nieprawidłowa opcja. Wybierz 1 lub 2.")


if __name__ == "__main__":
    main()
