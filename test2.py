import os
import hashlib
def file_as_bytes(file):
    with file:
        return file.read()
photos = os.listdir()
photos_with_md5 = [(fname, hashlib.md5(file_as_bytes(open(fname, 'rb'))).digest()) for fname in photos]
print photos_with_md5

