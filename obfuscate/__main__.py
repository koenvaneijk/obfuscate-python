import argparse
import io
import zipfile
import zlib
import os

class Compressor:
    def __init__(self, folder: str, output: str):
        self.folder = folder
        self.output = output

    def compress_files(self):
        # Create a zip file of the source files
        with io.BytesIO() as bundle_io:
            with zipfile.ZipFile(bundle_io, "w") as bundle:
                # add all files from the folder, but the folder should be the root of the zip file
                for root, dirs, files in os.walk(self.folder):
                    for file in files:
                        bundle.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), self.folder))

            # Get the contents of the BytesIO object
            data = bundle_io.getvalue()

        # Compress the data
        compressed_data = zlib.compress(data)
        compressed_string = repr(compressed_data)

        # Write the decompression code to a file
        with open(self.output, "w") as file:
            file.write(f"""import zlib;import io;import zipfile;data = {repr(compressed_data)};decompressed_data = zlib.decompress(data);bundle_io = io.BytesIO(decompressed_data);zip = zipfile.ZipFile(bundle_io);import tempfile;temp = tempfile.TemporaryDirectory();zip.extractall(temp.name);import os;os.chdir(temp.name);import sys;sys.path.append(temp.name);source = zip.read('__init__.py');exec(source);""")

def main():
    parser = argparse.ArgumentParser(description="Compresses all files in a directory and writes a Python script to decompress them.")
    parser.add_argument('folder', help='The directory with the files to compress.')
    parser.add_argument('output', help='The output Python script that will contain the decompression code.')

    args = parser.parse_args()

    compressor = Compressor(args.folder, args.output)
    compressor.compress_files()

if __name__ == "__main__":
    main()
    
