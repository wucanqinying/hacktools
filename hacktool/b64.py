import base64

def main():
    s = "haha123"
    bs = base64.b64encode(s.encode("utf-8"))

    print(bs.decode("utf-8"))

    bs1 = 'aGFoYTEyMw=='
    s1 = str(base64.b64decode(bs1),"utf-8")
    print(s1)

if __name__ == "__main__":
    main()