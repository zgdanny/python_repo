import hashlib
import base64

password = "abcd1234"

m = hashlib.md5()
m.update(password.encode('utf-8'))
digest = m.hexdigest()
print("MD5 digest:", digest)

digest_byte = digest.encode('utf-8')
b64_byte = base64.b64encode(digest_byte)
b64_str = b64_byte.decode('utf-8')
print("Base64 encode:", b64_str)
