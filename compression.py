import os
import zipfile
import zlib

def compress_file(file_name):
    try:
        with open(file_name, 'rb') as file:
            file_data = file.read()
    except FileNotFoundError:
        print("The file was not found.")
        return

    # Use ZIP compression (zlib) for binary data (e.g., PPT, Word, Excel, images)
    zip_compressed_data = zlib.compress(file_data)

    # Save the compressed data
    if not os.path.exists("compressed"):
        os.makedirs("compressed")

    output_file_name = "compressed/" + os.path.basename(file_name) + '.zip'
    with open(output_file_name, 'wb') as output_file:
        output_file.write(zip_compressed_data)

    print(f"Compressed data has been saved to {output_file_name}.")


def decompress_file(file_name):
    try:
        with open(file_name, 'rb') as file:
            compressed_data = file.read()
    except FileNotFoundError:
        print("The file was not found.")
        return

    # Decompress using zlib (ZIP decompression)
    decompressed_data = zlib.decompress(compressed_data)

    # Save decompressed file
    if not os.path.exists("decompressed"):
        os.makedirs("decompressed")

    output_file_name = "decompressed/" + os.path.basename(file_name).replace('.zip', '')
    with open(output_file_name, 'wb') as output_file:
        output_file.write(decompressed_data)

    print(f"Decompressed data has been saved to {output_file_name}.")


def main():
    while True:
        print("\nSelect an option:")
        print("1. Compress a file")
        print("2. Decompress a file")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            files = [f for f in os.listdir("files") if os.path.isfile(os.path.join("files", f))]
            if not files:
                print("No files found in the 'files' folder.")
                continue

            print("\nSelect a file to compress:")
            for idx, file in enumerate(files):
                print(f"{idx + 1}. {file}")
            file_choice = int(input(f"Enter your choice (1 - {len(files)}): ")) - 1
            compress_file(os.path.join("files", files[file_choice]))

        elif choice == "2":
            compressed_files = [f for f in os.listdir("compressed") if os.path.isfile(os.path.join("compressed", f))]
            if not compressed_files:
                print("No files found in the 'compressed' folder.")
                continue

            print("\nSelect a file to decompress:")
            for idx, file in enumerate(compressed_files):
                print(f"{idx + 1}. {file}")
            file_choice = int(input(f"Enter your choice (1 - {len(compressed_files)}): ")) - 1
            file_path = os.path.join("compressed", compressed_files[file_choice])
            decompress_file(file_path)

        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
