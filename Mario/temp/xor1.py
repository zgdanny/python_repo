def xor_encrypt(message, key):

    # 如果消息或密钥是字符串，则将其转换为字节数组
    if isinstance(message, str):
        message = message.encode()
    if isinstance(key, str):
        key = key.encode()

    # 使用异或加密消息
    encrypted_bytes = bytearray()
    for i in range(len(message)):
        encrypted_bytes.append(message[i] ^ key[i % len(key)])

    return encrypted_bytes


def xor_decrypt(ciphertext, key):

    decrypted_bytes = bytearray()
    for i in range(len(ciphertext)):
        decrypted_bytes.append(ciphertext[i] ^ key.encode()[i % len(key)])

    # 将解密后的字节数组转换为字符串
    decrypted_message = decrypted_bytes.decode()

    return decrypted_message


# Example usage
message = "hello world!!!"
key = "secretkey"

# Encrypt the message
encrypted_bytes = xor_encrypt(message, key)
print(">>>encrypted_bytes:", encrypted_bytes)
# Decrypt the ciphertext
decrypted_message = xor_decrypt(encrypted_bytes, key)
print(">>>decrypted_message:", decrypted_message)
# Check if the decrypted message matches the original message
assert decrypted_message == message
