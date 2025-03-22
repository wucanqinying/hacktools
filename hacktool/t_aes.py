from Crypto.Cipher import AES
import binascii

def main():
    key = b'abcdefghabcdefgh'
    """
    text = "haha123 wocao"
    text = text+(len(key)-(len(text)%len(key)))*"="
    print(text)
    aes = AES.new(key,AES.MODE_ECB)
    encrypt_text = aes.encrypt(text.encode())
    encrypt_res = binascii.b2a_hex(encrypt_text)
    print(encrypt_res)
    """

    encrypt_res = b'5ff27bccfc1aa3c0335f2f21bb9f17db'
    aes = AES.new(key,AES.MODE_ECB)
    encrypt_res = binascii.a2b_hex(encrypt_res)
    decrypt_text = aes.decrypt(encrypt_res)
    text = decrypt_text.decode()
    print(text)



if __name__ == "__main__":
    main()
