# Encryption Systems

## Overview
This repository contains implementations of various encryption methods, including:
- **Caesar Cipher**: A simple substitution cipher that shifts letters by a fixed number of places.
- **Substitution Cipher**: A mapping-based encryption where each letter is substituted with a unique counterpart.

## Files and Modules

### 1. `CaesarCipher.py`
- Implements the **Caesar Cipher** algorithm.
- Provides functions to **encrypt** and **decrypt** text.
- Supports processing **strings** and **lists**.

### 2. `SubstitutionCipher.py`
- Implements a custom **Substitution Cipher**.
- Uses predefined mappings for encryption and decryption.

### 3. `EncryptionManager.py`
- Handles user input and selects the encryption method.
- Allows encryption via **text input** or **file processing**.

## Usage
To run the encryption manager, execute:
```sh
python EncryptionManager.py
```
### Interactive Modes
1. **Text Mode** (`T`): Enter text manually for encryption.
2. **File Mode** (`F`): Provide file paths to encrypt/decrypt file contents.

### Encryption Methods
- **Caesar Cipher** (`CC`): Uses a fixed shift for encryption.
- **Substitution Cipher** (`SC`): Uses predefined character mappings.

## Known Issues
- File encryption in **Caesar Cipher** may not handle multi-line text correctly.
- **Substitution Cipher** incorrectly duplicates text during encryption.

## Future Improvements
- Fix multi-line processing issues in Caesar Cipher.
- Resolve text duplication issue in Substitution Cipher.
- Add support for additional encryption techniques.
