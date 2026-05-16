# Scanify 🔍

A simple Python tool to generate and scan QR codes — right from your terminal.

## Features

- Generate QR codes from any text or URL
- Scan QR codes from image files
- Simple menu-driven CLI interface

## Requirements

- Python 3.8+
- opencv-python
- qrcode[pil]

## Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/YOUR_USERNAME/scanify.git
   cd scanify
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   source .venv/bin/activate  # Mac/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

```bash
python qr_tool.py
```

You will see a menu:

```
========================================
        QR Code Tool
========================================
  1. Generate QR code
  2. Scan QR code
  3. Exit
========================================
```

- **Option 1** — Enter any text or URL and it saves a QR code as a `.png` file
- **Option 2** — Enter an image filename to scan and decode the QR code
- **Option 3** — Exit the program

## Example

Generate a QR code:
```
Choose an option (1/2/3): 1
Enter text or URL: https://github.com
Save as (default: qrcode.png): mygithub.png

  QR code saved as 'mygithub.png'
```

Scan it back:
```
Choose an option (1/2/3): 2
Enter image filename (default: qrcode.png): mygithub.png

----------------------------------------
  QR Code detected!
  Data : https://github.com
----------------------------------------
```

## Project Structure

```
scanify/
├── qr_tool.py        # Main script
├── requirements.txt  # Dependencies
├── .gitignore        # Files to ignore
└── README.md         # This file
```

## License

MIT
