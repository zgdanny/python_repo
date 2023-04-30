import base64

# 原始的二进制数据串
binary_data = "11001000011101101011101110100001"

# 将二进制数据转为字节数组
byte_array = bytearray(int(binary_data[i:i+8], 2)
                       for i in range(0, len(binary_data), 8))


# 使用 base64 模块对字节数组进行编码
encoded_data = base64.b64encode(byte_array)

# 将编码后的数据转换为字符串并输出
encoded_str = encoded_data.decode('ascii')
print(encoded_str)  # 输出 y3Z7

# 将编码后的数据解码为字节数组
decoded_data = base64.b64decode(encoded_data)

# 将字节数组转为二进制数据串
binary_data_decoded = ''.join(format(byte, '08b') for byte in decoded_data)

# 比较解码后的二进制数据串和原始的二进制数据串是否相同
assert binary_data_decoded == binary_data
