import os
import zlib
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk


def compress_file(file_name):
    try:
        with open(file_name, 'rb') as file:
            file_data = file.read()
        zip_compressed_data = zlib.compress(file_data)

        if not os.path.exists("compressed"):
            os.makedirs("compressed")

        output_file_name = "compressed/" + os.path.basename(file_name) + '.zip'
        with open(output_file_name, 'wb') as output_file:
            output_file.write(zip_compressed_data)

        return f"Compressed file saved to: {output_file_name}"
    except Exception as e:
        return f"Compression failed: {e}"

def decompress_file(file_name):
    try:
        with open(file_name, 'rb') as file:
            compressed_data = file.read()

        decompressed_data = zlib.decompress(compressed_data)

        if not os.path.exists("decompressed"):
            os.makedirs("decompressed")

        output_file_name = "decompressed/" + os.path.basename(file_name).replace('.zip', '')
        with open(output_file_name, 'wb') as output_file:
            output_file.write(decompressed_data)

        return f"Decompressed file saved to: {output_file_name}", decompressed_data
    except Exception as e:
        return f"Decompression failed: {e}", b''


def main():
    root = tk.Tk()
    root.title("Zlib File Compressor")
    root.geometry("900x600")
    root.configure(bg="#f0f8ff")

    # Scrollable Frame Setup
    canvas = tk.Canvas(root, bg="#f0f8ff")
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas, bg="#f0f8ff")

    scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    tk.Label(scroll_frame, text="Zlib File Compressor", font=("Helvetica", 24, "bold"),
             bg="#f0f8ff", fg="#333").pack(pady=20)

    # text_area = scrolledtext.ScrolledText(scroll_frame, wrap=tk.WORD, width=100, height=15,
    #                                       font=("Helvetica", 12))
    # text_area.pack(pady=10)

    result_label = tk.Label(scroll_frame, text="", font=("Helvetica", 12), bg="#f0f8ff", fg="#333")
    result_label.pack(pady=10)

    button_frame = tk.Frame(scroll_frame, bg="#f0f8ff")
    button_frame.pack(pady=10)

    # def compress_text_callback():
    #     input_text = text_area.get("1.0", tk.END).strip().encode()
    #     if not input_text:
    #         result_label.config(text="Input text is empty.")
    #         return

    #     compressed_data = zlib.compress(input_text)
    #     text_area.delete("1.0", tk.END)
    #     text_area.insert(tk.END, compressed_data.hex())  # Show as hex
    #     result_label.config(text="Text compressed using zlib.")

    # def decompress_text_callback():
    #     input_hex = text_area.get("1.0", tk.END).strip()
    #     try:
    #         binary_data = bytes.fromhex(input_hex)
    #         decompressed_data = zlib.decompress(binary_data)
    #         text_area.delete("1.0", tk.END)
    #         try:
    #             text_area.insert(tk.END, decompressed_data.decode())
    #             result_label.config(text="Decompressed successfully.")
    #         except:
    #             text_area.insert(tk.END, decompressed_data.hex())
    #             result_label.config(text="Decompressed (binary data displayed as hex).")
    #     except Exception as e:
    #         result_label.config(text=f"Decompression failed: {e}")

    # tk.Button(button_frame, text="Compress Text", command=compress_text_callback,
    #           width=20, height=2, bg="#4682b4", fg="white", font=("Helvetica", 12)).grid(row=0, column=0, padx=10)
    # tk.Button(button_frame, text="Decompress Text", command=decompress_text_callback,
    #           width=20, height=2, bg="#4682b4", fg="white", font=("Helvetica", 12)).grid(row=0, column=1, padx=10)

    # File operation buttons
    file_button_frame = tk.Frame(scroll_frame, bg="#f0f8ff")
    file_button_frame.pack(pady=20)

    def compress_file_callback():
        file = filedialog.askopenfilename()
        if file:
            result = compress_file(file)
            result_label.config(text=result)

    def decompress_file_callback():
        file = filedialog.askopenfilename(filetypes=[("ZIP Compressed Files", "*.zip")])
        if file:
            result, content = decompress_file(file)
            result_label.config(text=result)
            # try:
            #     text_area.delete("1.0", tk.END)
            #     text_area.insert(tk.END, content.decode())
            # except:
            #     text_area.delete("1.0", tk.END)
            #     text_area.insert(tk.END, content.hex())

    tk.Button(file_button_frame, text="Compress File", command=compress_file_callback,
              width=20, height=2, bg="#6a5acd", fg="white", font=("Helvetica", 12)).grid(row=0, column=0, padx=40)
    tk.Button(file_button_frame, text="Decompress File", command=decompress_file_callback,
              width=20, height=2, bg="#6a5acd", fg="white", font=("Helvetica", 12)).grid(row=0, column=1, padx=40)

    # Exit button
    tk.Button(scroll_frame, text="Exit", command=root.quit,
              width=25, height=2, bg="#b22222", fg="white", font=("Helvetica", 12)).pack(pady=40)

    root.mainloop()
if __name__ == "__main__":
    main()
