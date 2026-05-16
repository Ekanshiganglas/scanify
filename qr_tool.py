import sys
import cv2
import qrcode


# ── Generate ───────────────────────────────────────────────────────────────────

def generate_qr():
    print("\n--- Generate QR Code ---")
    data     = input("Enter text or URL: ").strip()
    filename = input("Save as (default: qrcode.png): ").strip() or "qrcode.png"

    if not filename.endswith(".png"):
        filename += ".png"

    img = qrcode.make(data)
    img.save(filename)

    print(f"\n  QR code saved as '{filename}'")


# ── Scan ───────────────────────────────────────────────────────────────────────

def scan_qr():
    print("\n--- Scan QR Code ---")
    filename = input("Enter image filename (default: qrcode.png): ").strip() or "qrcode.png"

    image = cv2.imread(filename)

    if image is None:
        print(f"  Error: Could not open '{filename}'. Check the filename.")
        return

    # Upscale + grayscale for better detection
    scale  = 2
    width  = int(image.shape[1] * scale)
    height = int(image.shape[0] * scale)
    image  = cv2.resize(image, (width, height), interpolation=cv2.INTER_LINEAR)
    gray   = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    detector = cv2.QRCodeDetector()
    data, points, _ = detector.detectAndDecode(gray)

    if not data:
        print("  No QR code found. Make sure the image is clear and not decorated.")
        return

    print("\n" + "-" * 40)
    print(f"  QR Code detected!")
    print(f"  Data : {data}")
    print("-" * 40)


# ── Menu ───────────────────────────────────────────────────────────────────────

def menu():
    while True:
        print("\n" + "=" * 40)
        print("        Scanify - QR Code Tool")
        print("=" * 40)
        print("  1. Generate QR code")
        print("  2. Scan QR code")
        print("  3. Exit")
        print("=" * 40)

        choice = input("Choose an option (1/2/3): ").strip()

        if choice == "1":
            generate_qr()
        elif choice == "2":
            scan_qr()
        elif choice == "3":
            print("\n  Goodbye!\n")
            sys.exit(0)
        else:
            print("  Invalid choice. Please enter 1, 2, or 3.")


# ── Entry point ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    menu()
