import sys

from ImageEncrypt import ImageCrypto


ImageCrypto().view_encrypted_image(sys.argv[1] if len(sys.argv) > 1 else None)