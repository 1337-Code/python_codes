encrypted_flag = b'@\x13Z1Z\x18:E(\x03\x1b\x18\x18:\x01\x14\x1d\x1a\x0f\x11\x15\x1e\x1aF\x1a\x19Y\x17Z\x02\x02'
shuffled_flag = [61, 61, 34, 34, 38, 34, 42, 53, 53, 42, 42, 46, 42, 34,
                 36, 20, 29, 26, 15, 17, 21, 30, 26, 34, 37, 36, 61, 59, 61, 59, 61]
secrets_be_like = [0x74, 0x77, 0x69, 0x6e, 0x6b, 0x6c, 0x65, 0x74, 0x77, 0x69, 0x6e,
                   0x6b, 0x6c, 0x65, 0x6c, 0x69, 0x74, 0x74, 0x6c, 0x65, 0x73, 0x74, 0x61, 0x72]
print(encrypted_flag)
arr_bytes = []
for byte in encrypted_flag:
    arr_bytes.append(byte)


def encrypt(flag):
    t1 = []
    for i in range(len(flag)):
        t1.append(chr(flag[i] ^ secrets_be_like[i % len(secrets_be_like)]))
    print(t1)
    return t1


print(''.join(encrypt(arr_bytes)))
# ['F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
#     '}', 'i', 'n', 'c', 't', 'f', 'j', '{', 'A', 'B', 'C', 'D','E']
