# QR Code Generator

This Python script generates QR codes from user-provided text or links and saves them as PNG image files.

## Requirements

- Python 3.x
- `qrcode` library (`pip install qrcode[pil]`)

## Usage

1. Clone this repository or download the `qr_code_generator.py` script.
2. Install the required dependencies: `pip install qrcode`.
3. Run the script: `python qr_code_generator.py`.
4. Enter your text or link when prompted.
5. The script will generate a QR code image and save it as a PNG file in the current directory.

## Example

```bash
$ python qr_code_generator.py
Please enter your text or link:
>> https://www.example.com
QR code generated successfully. Saved as: 20240303-134545.png
```

## Options

- You can customize the QR code parameters such as error correction level, version, box size, and border directly in the script.


