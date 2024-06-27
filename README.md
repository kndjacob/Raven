# Raven

Welcome to **Raven**! Raven is a Python-based application designed to make encryption and decryption of text files simple and straightforward. Whether you need to protect sensitive information or simply want to explore cryptography, Raven is here to help.

## Introduction

Raven allows you to:

- Encrypt text files using a custom key
- Decrypt text files using the same key
- Generate secure keys for encryption and decryption
- Create new text files for your messages

With an easy-to-use interface and clear instructions, Raven ensures that even those new to encryption can use it effectively.

## Features

- **Encryption**: Encrypt any `.txt` file using a specified key.
- **Decryption**: Decrypt any `.txt` file using the same key it was encrypted with.
- **Key Generation**: Generate a 1024-character key for secure encryption.
- **Message Creation**: Create new `.txt` files for encryption.

## Getting Started

### Prerequisites

- Python 3.x installed on your system
- Basic understanding of how to run Python scripts

### Installation

1. Clone this repository to your local machine:
    ```sh
    git clone https://github.com/your-username/raven.git
    ```
2. Navigate to the project directory:
    ```sh
    cd raven
    ```

### Running Raven

To start Raven, simply run the `raven.py` script:
```sh
python raven.py
```

# Usage Instructions

Once you run the script, you will be presented with a menu:

```mathematica
(E)ncrypt - Encrypt a .txt
(D)ecrypt - Decrypt a .txt
(G)enerate Key - Generate a 1024 character key
(N)ew Message - Create your own .txt
(I)nformation - FIRST TIME USERS READ ME!
(Q)uit - Exits the application
```
## Encrypting a File
- Select `E` from the main menu.
- Enter the name of the key file (without the `.txt` extension).
- Enter the name of the text file you want to encrypt (without the `.txt` extension).
- Save the encrypted message with a memorable name.

## Decrypting a File
- Select `D` from the main menu.
- Enter the name of the key file (without the `.txt` extension) used to encrypt the message.
- Enter the name of the encrypted text file (without the `.txt` extension).
- Save the decrypted message with a memorable name.

## Generating a Key
- Select `G` from the main menu.
- Enter a name for the key file (without the `.txt` extension).
- The key will be generated and saved automatically.

## Creating a New Message
- Select `N` from the main menu.
- Type your message.
- Enter a name to save the message file (without the `.txt` extension).

## Information
- Select `I` from the main menu to read important information about how to use Raven.

**Happy encrypting!**
