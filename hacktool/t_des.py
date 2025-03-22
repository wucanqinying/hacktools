from Crypto.Cipher import DES
import binascii

def main():

    key = b'aabbccdd'
    des = DES.new(key,DES.MODE_ECB)
    encrypt_res = b'1880cda4acf8dc938e5544346db3acc2'

    encrypt_text = binascii.a2b_hex(encrypt_res)
    decrypt_res = des.decrypt(encrypt_text)
    print(decrypt_res)

if __name__ == "__main__":
    main()
