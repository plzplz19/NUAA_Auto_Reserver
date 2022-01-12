import rsa
from rsa import common
import base64

def genKeys(n=512):
    pubkey,privkey = rsa.newkeys(n)

    pub = pubkey.save_pkcs1()
    pri = privkey.save_pkcs1()

    # 将公钥保存到文件 ,将字节写入文件需要加上decode（'utf-8'），python3新增
    with open("public.pub", 'w+') as file:  # public.pub，保存的文件名，可更改路径，这里保存在当前路径下
        file.write(pub.decode("utf-8"))
    # 将私钥保存到文件
    with open("private.pem", 'w+') as file:
        file.write(pri.decode('utf-8'))

def readPubKey(path):
    # 取出公钥
    with open(path, "r") as file_pub:
        # 从文件中读出数据
        pub_data = file_pub.read()
        # 将读出数据通过PublicKey.load_pkcs1()转换为公钥
        pubkey = rsa.PublicKey.load_pkcs1(pub_data)
        return pubkey

def readPrikey(path):
    # 取出私钥
    with open(path, "r") as file_pri:
        pri_data = file_pri.read()
        # 将读出数据通过PrivateKey.load_pkcs1()转换为私钥
        prikey = rsa.PrivateKey.load_pkcs1(pri_data) 
        return prikey   

def myEncrypt(str_to_encrypt,public_key):
    # 获取密文块的明文槽长度
    max_message_length = common.byte_size(public_key.n) - 11
    # 以二进制编码读取文件
    cipher_text_list = []
    # with open(path, 'rb') as f:
    fs = str_to_encrypt.encode()
    # 设置二进制串的切片轮次
    epoch = len(fs) // max_message_length

    for i in range(epoch):
        # 对原始明文进行切片
        fragment = fs[max_message_length * i: max_message_length * (i + 1)]
        # 使用公钥对子串进行加密
        cipher_text_fragment = rsa.encrypt(fragment, public_key)
        # 将密文块填充至列表
        cipher_text_list.append(cipher_text_fragment)
    # 将最后一部分明文进行加密并填充
    cipher_text_list.append(rsa.encrypt(fs[max_message_length * epoch:], public_key))

    # 返回密文块列表
    return cipher_text_list

def myDecrypt(cipher_text_list,secret_key):
    # 创建明文空间
    plain_text = bytes('', 'utf-8')

    # with open(path,'r') as f:
    #     cipher_text_list = f.read()

    for fragment in cipher_text_list:
        # 使用私钥对密文块进行解密
        plain_text_fragment = rsa.decrypt(fragment, secret_key)
        # 将明文串合并至明文空间
        plain_text += plain_text_fragment

    # 返回明文
    return plain_text

if __name__ == '__main__':
    #genKeys()
    pub_key = readPubKey('./yun_public.pub')
    #pri_key = readPrikey('./private.pem')
    cipher_text = myEncrypt('123456',public_key=pub_key)

    with open('cipher.txt','wb') as f:
        cipher_text_encoded = [base64.b64encode(i)+'\n'.encode() for i in cipher_text]
        f.writelines(cipher_text_encoded)
    
    with open('cipher.txt','rb') as f:
        temp = f.readlines()
        to_be_decrypt = [base64.b64decode(i) for i in temp]

    #plain_text = myDecrypt(to_be_decrypt,pri_key).decode()




    