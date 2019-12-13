import redis

REDIS_HOST = '127.0.0.1'
#REDIS_HOST = '172.16.13.1'
REDIS_PORT = 6379
REDIS_STORE = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
PATH = 'C:\\Users\\admin\\Desktop\\test'# 工作区绝对路径地址