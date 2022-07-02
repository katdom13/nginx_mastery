import base64
import hashlib
import time
from datetime import datetime


def generate_secure_link(secret, url, expiry):
    link = f"{secret}{url}{expiry}"

    # generate md5 hash in binary format
    hash = hashlib.md5(str(link).encode("utf-8")).digest()

    # apply base 64 encoding
    base64_hash = base64.urlsafe_b64encode(hash)

    # decode to string, strip symbols
    str_hash = base64_hash.decode("utf-8").rstrip("=")

    return f"{url}?md5={str_hash}&expires={expiry}"


secret = "enigma"
url = "/file/test.mp3"

# make epoch time
date_time = datetime(2023, 12, 30, 0, 0, 0)
expiry = int(time.mktime(date_time.timetuple()))

print(generate_secure_link(secret, url, expiry))
