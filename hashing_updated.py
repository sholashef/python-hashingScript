import hashlib

#prompt to specify the directory of the file 

file_path = input("Enter path_to_your_file.txt")

# Function to calculate the SHA-256 hash of a file

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            # Read the file in chunks to avoid loading the entire file into memory
            for chunk in iter(lambda: file.read(4096), b""):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

# Example usage
#file_path = "path_to_your_file.txt"  # Replace with the path to your file
hash_value = calculate_sha256(file_path)

if hash_value:
    print(f"SHA-256 Hash of {file_path}: {hash_value}")
else:
    print(f"File not found: {file_path}")
