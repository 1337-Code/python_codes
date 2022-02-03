flag = "inctfj{ABCDEFGHIJKLMNOPQSTUVWX}"

secrets_be_like = [0x74, 0x77, 0x69, 0x6e, 0x6b, 0x6c, 0x65, 0x74, 0x77, 0x69, 0x6e,
                   0x6b, 0x6c, 0x65, 0x6c, 0x69, 0x74, 0x74, 0x6c, 0x65, 0x73, 0x74, 0x61, 0x72]

print(len(flag))


def encrypt(flag):
    t1 = []
    for i in range(len(flag)):
        t1.append(ord(flag[i]) ^ secrets_be_like[i % len(secrets_be_like)])
    print(t1)
    return t1


def pepe_gaga(flag):
    t1 = ""
    for i in range(len(flag)):
        t1 += chr(flag[i])
    return t1.encode('utf8')


def shuffle2(flag):
    t1 = []
    for i in range(len(flag)//2):
        t1.append(flag[i])
    t2 = []
    for i in range(len(flag)//2, len(flag)):
        t2.append(flag[i])
    t3 = []
    for i in range(len(t1)//2):
        t3.append(t1[i])
    for i in range(len(t2)//2, len(t2)):
        t3.append(t2[i])
    t4 = []
    for i in range(len(t2)//2):
        t4.append(t2[i])
    for i in range(len(t1)//2, len(t1)):
        t4.append(t1[i])
    t5 = []
    for i in range(len(t3)):
        t5.append(t3[i])
    for i in range(len(t4)):
        t5.append(t4[i])
    # ['F', 'G', 'H', 'I', 'J', 'K', '{', 'A', 'B', 'C', 'D', 'E',
    #     'i', 'n', 'c', 't', 'f', 'j', 'M', 'N', 'O', 'P', 'L', '}']
    return t5


def shuffle1(flag):
    flag = list(flag)
    t1 = []
    for i in range(len(flag)//2, len(flag)):  # 12 - 24
        t1.append(flag[i])
    for i in range(len(flag)//2):  # 0-12
        t1.append(flag[i])

    # ['F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
    #     '}', 'i', 'n', 'c', 't', 'f', 'j', '{', 'A', 'B', 'C', 'D','E']
    return t1


print(pepe_gaga(encrypt(shuffle2(shuffle1(flag)))))
print(shuffle2(shuffle1(flag)))
