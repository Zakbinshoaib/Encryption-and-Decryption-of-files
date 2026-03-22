# Encryption and Decryption of Files

This project provides a simple yet effective solution for encrypting and decrypting files using Python. It leverages the `cryptography` library to ensure that your files are secure and can only be accessed with the correct decryption key.

## Features

- **File Encryption**: Encrypt any file using a securely generated encryption key.
- **File Decryption**: Decrypt files back to their original state with the correct key.
- **User-Friendly Interface**: A simple graphical file selection dialog to choose files for encryption and decryption.
- **Key Management**: Automatically generates and saves an encryption key for later use.

## How It Works

The project consists of two main scripts:

- `app.py`: Handles the encryption process. It prompts the user to select a file, generates a unique encryption key, and saves the encrypted version of the file.
- `dec_code.py`: Handles decryption. It requires the encryption key generated during the encryption process to decrypt the file and restore it to its original form.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

Make sure you have Python installed on your system. You will also need the following libraries:

- `cryptography`: For handling the encryption and decryption logic.
- `tkinter`: For the file selection dialog (usually included with Python).

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Zakbinshoaib/Encryption-and-Decryption-of-files.git
   cd Encryption-and-Decryption-of-files
   ```

2. Install the required library:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Encrypt a File

1. Run the `app.py` script:
   ```bash
   python app.py
   ```
2. A file dialog will open — select the file you want to encrypt.
3. The script will generate an `encryption_key.key` file and an encrypted copy of your file (e.g., `enc_filename.txt`).

> **Important**: Keep `encryption_key.key` safe. You will need it to decrypt the file later.

### Decrypt a File

1. Run the `dec_code.py` script:
   ```bash
   python dec_code.py
   ```
2. A file dialog will open — select the encrypted file (e.g., `enc_filename.txt`).
3. The script will use the `encryption_key.key` in the current directory to decrypt the file and save it as a new file (e.g., `denc_filename.txt`).

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
