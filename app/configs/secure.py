import redis


REDIS_HOST = '172.16.13.1'
REDIS_PORT = 6379
REDIS_STORE = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)


MYSQL_HOST = '127.0.0.1'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '123456'
MYSQL_PORT = 3306

FDFS_HOST = "http://172.16.13.1:8080/"