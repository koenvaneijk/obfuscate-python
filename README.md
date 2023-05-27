# Obfuscate Python

A Python script that obfuscates Python code in a directory by compressing it into a single line in a single .py file. Uses only the Python standard library, no third-party modules required.

## Installation

```bash
git clone https://github.com/koenvaneijk/obfuscate-python
cd obfuscate-python
python3 -m pip install .
```

## Usage

Put the Python code (and any required modules) in a folder, name the entrypoint `__init__.py` and then run the following command:

```bash
python3 -m obfuscate <path-to-folder> <output.py>
```

For example:
    
```bash
python3 -m obfuscate ./example example.py
```

The output file will be a single Python file that contains all the code from the input folder, but all the code will be compressed as a single line, like this:

```python
import zlib;import io;import zipfile;data = b'x\x9c\x0b\xf0ff\x11a\x00\x81\xdc\xad\xbb\xc3\xfc\x82-\xd7\xe8\x01\xd9 ,\x00\xc4\x19\x99))\xa9y\xf1\xb9\xf9)\xa59\xa9z\x05\x95)\xa9i\n%\x19\x99\xc5\xf1@\x04\x91\xd3\xd0\xb4\xe2R\x00\x82\x82\xa2\xcc\xbc\x12\r%O\xf5\\\x05\x88\x84\xa2\x92f\x00\xdc\xec*\xa0\xd9\xb2\xac\x0b\x18\x82\x80l\x10\xe6\x06\xe2\xf8\xf8\xcc\xbc\xcc\x92\xf8x\xa0\xb1iE\xf90mP\xbb\x142s\x0b\xf2\x8bJ\xd0,\xe3\xe2\x029 71\x13n-\xbac\xb8\xb8 \xb2\x01\xde\x8cL"\xcc\xb8=\x06\x03K\x1a\x19\xb0x\x13Y76\xa7#t\xc7\xa0z$\xc0\x9b\x95\r$\xc1\x04\x84\xe5@\xfa:X\x19\x006\xe2W\t';decompressed_data = zlib.decompress(data);bundle_io = io.BytesIO(decompressed_data);zip = zipfile.ZipFile(bundle_io);import tempfile;temp = tempfile.TemporaryDirectory();zip.extractall(temp.name);import os;os.chdir(temp.name);import sys;sys.path.append(temp.name);source = zip.read('__init__.py');exec(source);
```

## Disclaimer
I am not responsible for any damage caused by this software. Use at your own risk. This software is provided as-is, without any warranty. Only use this software for legitimate purposes and within  the constraints of applicable laws.

## License
This software is licensed under the AGPLv3 license.
