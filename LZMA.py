import os
import lzma

def compress_file_lzma(file_name):
    try:
        with open(file_name, 'rb') as file:
            file_data = file.read()
    except FileNotFoundError:
        print("The file was not found.")
        return

    # Use LZMA compression for better compression ratios
    compressed_data = lzma.compress(file_data)

    # Save the compressed data
    if not os.path.exists("compressed"):
        os.makedirs("compressed")

    output_file_name = "compressed/" + os.path.basename(file_name) + '.xz'  # .xz is the extension for LZMA files
    with open(output_file_name, 'wb') as output_file:
        output_file.write(compressed_data)

    print(f"Compressed data has been saved to {output_file_name}.")

def decompress_file_lzma(file_name):
    try:
        with open(file_name, 'rb') as file:
            compressed_data = file.read()
    except FileNotFoundError:
        print("The file was not found.")
        return

    # Decompress using LZMA
    decompressed_data = lzma.decompress(compressed_data)

    # Save decompressed file
    if not os.path.exists("decompressed"):
        os.makedirs("decompressed")

    output_file_name = "decompressed/" + os.path.basename(file_name).replace('.xz', '')
    with open(output_file_name, 'wb') as output_file:
        output_file.write(decompressed_data)

    print(f"Decompressed data has been saved to {output_file_name}.")
