import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# HTTP域名 or host
BASE_URL = os.environ.get("base_url") or "https://dt-dev.arctron.cn/api"

# MYSQL Config
CASE_DATABASE = {
    "dev": {
        "HOST": "10.241.11.7",
        "PORT": "3306",
        "NAME": "datatron",
        "USER": "root",
        "PASSWORD": "pAssw0rd",
        "CHARSET": "utf8"
    },
    "testcase": {
        "HOST": "127.0.0.1",
        "PORT": "3306",
        "NAME": "guest",
        "USER": "root",
        "PASSWORD": "123456",
        "CHARSET": "utf8"
    }
}