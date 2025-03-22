from pexpect import pxssh

def Login(server,username,password):
    try:
        s = pxssh.pxssh()
        s.login(server,username,password)
        print("yes")
    except:
        print("no")


def main():

    Login("192.168.249.129","root","1toor")


if __name__ == "__main__":
    main()