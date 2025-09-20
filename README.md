# BIP39-2-PK

## Overview

BIP39-2-PK is a Python script that interactively derives an Ethereum private key and address from a BIP-39 mnemonic phrase. It uses the `bip_utils` library to perform BIP-44 derivation for Ethereum, allowing users to specify an address index.

## Features

- Securely accepts a BIP-39 mnemonic phrase via hidden input.
- Supports derivation of Ethereum addresses at a user-specified index (default: 0).
- Outputs the derived Ethereum address and private key in hexadecimal format.
- Follows the BIP-44 derivation path: `m/44'/60'/0'/0/{index}`.

## Requirements

- Python 3.6+
- `bip_utils` library

## Installation

1. Clone or download this repository.
2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:

   ```bash
   python bip39_to_pk.py
   ```

2. Enter your BIP-39 mnemonic phrase (words separated by spaces) when prompted. The input is hidden for security.
3. Optionally, specify an address index (default is 0).
4. The script will output the derived Ethereum address and private key.

### Example

```bash
$ python bip39_to_pk.py
Enter your BIP-39 mnemonic (words separated by spaces): [hidden input]
Address index [default: 0]: 0

Derived account
  Index    : 0
  Address  : 0x1234567890abcdef1234567890abcdef12345678
  PrivKey  : 0xabcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890
```

## Security Notes

- The mnemonic input is handled securely using `getpass` to prevent it from being displayed.
- Ensure you run this script in a secure environment, as the private key is sensitive information.
- Do not share your mnemonic or private key.

## Dependencies

- `bip_utils`: A Python library for BIP-39 and BIP-44 key derivation.

## License

This project is licensed under the MIT License.
