import qrcode
import time

def generate_qr_code(data):
    # Check if input data is empty
    if not data:
        print("Error: Input cannot be empty.")
        return
    
    # Create a QRCode instance
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        version=10,
        box_size=10,
        border=5
    )
    
    # Add data to the QRCode instance
    qr.add_data(data)
    qr.make(fit=True)
    
    # Generate the QR code image
    img = qr.make_image()
    
    # Generate timestamp for filename
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    
    # Define the filename for the QR code image
    filename = '{}.png'.format(timestamp)
    
    # Save the QR code image
    img.save(filename)
    
    # Provide feedback to the user
    print(f"QR code generated successfully. Saved as: {filename}")

def main():
    # Prompt user for input
    data = input("Please enter your text or link:\n>> ")
    
    # Generate QR code based on user input
    generate_qr_code(data)

if __name__ == "__main__":
    main()
