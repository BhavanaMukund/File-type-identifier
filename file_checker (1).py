def load_magic_numbers():
    return {
        b"\x89PNG\r\n\x1a\n": "PNG Image",
        b"\xff\xd8\xff": "JPEG Image",
        b"%PDF": "PDF Document",
        b"PK\x03\x04": "ZIP Archive",
        b"ID3": "MP3 Audio",
        b"\x00\x00\x00\x18ftyp": "MP4 Video",
        b"\x7fELF": "ELF Executable (Linux)",
        b"MZ": "EXE Executable (Windows)"
    }
def identify_file_type(file_path):
    magic_numbers = load_magic_numbers()

    with open(file_path, "rb") as f:
        file_start = f.read(16)
    for magic, filetype in magic_numbers.items():
        if file_start.startswith(magic):
            return filetype
    return "Unknown or Unsupported File Type"
if __name__ == "__main__":
 path = input("Enter file path: ")
try:
    result = identify_file_type(path)
    print("\nDetected Type:", result)
except FileNotFoundError:
    print("Error: File not found.")
