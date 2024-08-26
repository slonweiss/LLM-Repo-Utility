import os

def write_files_to_single_text(directory, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Loop through each file in the directory
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            
            # Check if it's a file (not a directory)
            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding='utf-8') as infile:
                    # Write the file title (filename) and a separator
                    outfile.write(f"Title: {filename}\n")
                    outfile.write("Contents:\n")
                    # Write the file's contents
                    outfile.write(infile.read())
                    # Add a separator between files
                    outfile.write("\n\n---\n\n")

    print(f"All files in {directory} have been written to {output_file}")

# Example usage
directory_path = r'C:\Users\jonwe\OneDrive\Documents\GitHub\EllipticCurveFiniteField'
output_file_path = 'combined_output.txt'
write_files_to_single_text(directory_path, output_file_path)
