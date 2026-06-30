# File Compression and Decompression using Multiple Algorithms

## Overview
This project is a Python-based file compression and decompression tool that supports multiple algorithms including:

- Zlib (ZIP-style compression)
- LZMA (high compression ratio algorithm)

It allows users to compress and decompress various file types such as documents, images, and binary files through a simple command-line interface.

---

## Features

- Compress files using Zlib
- Compress files using LZMA (.xz format)
- Decompress compressed files safely
- Automatically creates required folders:
  - files/ (input files)
  - compressed/ (compressed output)
  - decompressed/ (restored files)
- Interactive CLI menu system
- Supports binary files (images, PPT, Word, etc.)

---

## Algorithms Used

### Zlib Compression
- Fast compression method
- Produces compact binary output
- Good for general-purpose compression

### LZMA Compression
- Higher compression ratio than Zlib
- Uses .xz format
- Slower but more efficient

---

## Project Structure

project/
│
├── files/              # Input files
├── compressed/         # Compressed output files
├── decompressed/       # Decompressed output files
│
├── compression.py      # Zlib compression code
├── lzma.py             # LZMA compression code
├── demo.py             # Main menu program
└── README.md

---

## How to Run

### 1. Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

### 2. Add files
Place your files inside the folder:
files/

### 3. Run the program
python demo.py

---

## Usage

Menu Options:
1. Compress a file
2. Decompress a file
3. Exit

Compression:
- Select file → choose compression method → saved in compressed/

Decompression:
- Select compressed file → restored in decompressed/

---

## Requirements

- Python 3.x

Built-in libraries used:
- os
- zlib
- lzma

---

## Future Improvements

- GUI using Tkinter
- Drag & drop file support
- Compression ratio comparison
- Add more algorithms (Huffman, Brotli)
- Progress bar for large files

---

## Author

Nandinee Gohil

---

## License

This project is for educational purposes only.