<a id="styles"></a>  
<img src="https://readme-typing-svg.herokuapp.com?font=Lexend+Giga&size=25&pause=1000&color=CCA9DD&vCenter=true&width=435&height=50&lines=ImageEncrypt" width="450"/>

---

This tool allows you to encrypt and decrypt images using a keyword-based encryption method. The encryption adds random noise to the image and embeds text into the noise, while the decryption restores the image using the same keyword.

<a id="styles"></a>  
<img src="https://readme-typing-svg.herokuapp.com?font=Lexend+Giga&size=20&pause=1000&color=CCA9DD&vCenter=true&width=435&height=50&lines=Features" width="450"/>

---

- Encrypt images with a password/keyword.
- Embed custom text into the encrypted image.
- Decrypt encrypted images using the same keyword.

<a id="styles"></a>  
<img src="https://readme-typing-svg.herokuapp.com?font=Lexend+Giga&size=20&pause=1000&color=CCA9DD&vCenter=true&width=435&height=50&lines=Requirements" width="450"/>

---

- Python 3.x
- OpenCV (`cv2`)
- NumPy
- Cryptography library (`cryptography`)

<a id="styles"></a>  
<img src="https://readme-typing-svg.herokuapp.com?font=Lexend+Giga&size=20&pause=1000&color=CCA9DD&vCenter=true&width=435&height=50&lines=Setup" width="450"/>

---

1. Clone or download the repository.
2. Install the required dependencies:

   ```bash
   pip install opencv-python numpy cryptography
   ```

3. Make sure you have an image file (e.g., `.png`, `.jpg`) to encrypt.

<a id="styles"></a>  
<img src="https://readme-typing-svg.herokuapp.com?font=Lexend+Giga&size=20&pause=1000&color=CCA9DD&vCenter=true&width=435&height=50&lines=Usage" width="450"/>

---

<a id="styles"></a>  
<img src="https://readme-typing-svg.herokuapp.com?font=Lexend+Giga&size=15&pause=1000&color=CCA9DD&vCenter=true&width=435&height=30&lines=Running+the+program" width="450"/>

---

1. Open a terminal and navigate to the folder containing the `ImageEncrypt.py` file.
2. Run the script:
   ```bash
   python ImageEncrypt.py
   ```

<a id="styles"></a>  
<img src="https://readme-typing-svg.herokuapp.com?font=Lexend+Giga&size=20&pause=1000&color=CCA9DD&vCenter=true&width=435&height=50&lines=Options" width="450"/>

---

- **Encrypt Image:**
  - Provide the path of the image to encrypt.
  - Enter a password/keyword to encrypt the image.
  - The tool will generate an encrypted image file and a noise image with embedded text.
- **Decrypt Image:**
  - Provide the path of the encrypted file (not the noise image).
  - Enter the same password/keyword used during encryption.
  - The tool will decrypt and save the original image.
- **Open Encrypted Image:**
  - Choose option `3` from the menu.
  - Select the encrypted file and enter its password.
  - The image is displayed without saving a decrypted copy.

You can also open the password viewer directly from PowerShell:

```bash
python ImageEncrypt.py --view "C:\path\to\encrypted-file"
```

The noise image can be selected instead; the viewer automatically finds its matching encrypted file. To launch the GUI helper with a noise image:

```bash
pythonw ImageViewer.pyw "C:\path\to\test_noise.png"
```

Windows Photos cannot display a password prompt. For double-click behavior, associate the noise image files with `ImageViewer.pyw` once in Windows' **Open with** settings.

<a id="styles"></a>  
<img src="https://readme-typing-svg.herokuapp.com?font=Lexend+Giga&size=15&pause=1000&color=CCA9DD&vCenter=true&width=435&height=30&lines=Example+Commands" width="450"/>

---

#### Encrypting an Image

```bash
Enter input image path: /path/to/image.jpg
Enter encryption keyword: mysecretkey
Enter output file path (without extension): /path/to/encrypted_image
Enter text to embed in encrypted image: Any text you want
```

#### Decrypting an Image

```bash
Enter encrypted file path (without _noise.png): /path/to/encrypted_image
Enter decryption keyword: mysecretkey
Enter output image path: /path/to/decrypted_image.png
```

<a id="styles"></a>  
<img src="https://readme-typing-svg.herokuapp.com?font=Lexend+Giga&size=20&pause=1000&color=CCA9DD&vCenter=true&width=435&height=50&lines=Notes" width="450"/>

---

- Always remember the keyword used for encryption; it's required for decryption.
- The noise image (`_noise.png`) is generated for visual effect and contains embedded text.

<a id="styles"></a>  
<img src="https://readme-typing-svg.herokuapp.com?font=Lexend+Giga&size=20&pause=1000&color=CCA9DD&vCenter=true&width=435&height=50&lines=License" width="450"/>

---

This project is licensed under the YASL License - see the [License](License.md) file for details.
