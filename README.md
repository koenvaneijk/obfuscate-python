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

The output file will be a single Python file that contains all the code from the input folder, but all the code will be compressed as a single line.

## Disclaimer
I am not responsible for any damage caused by this software. Use at your own risk. This software is provided as-is, without any warranty. Only use this software for legitimate purposes and within  the constraints of applicable laws.

## License
This software is licensed under the AGPLv3 license.
