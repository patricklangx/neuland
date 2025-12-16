# Cache Poisoning Research


## X-HTTP-Method-Override, X-Oversized-Header and X-Metachar-Header

Research paper [Your Cache Has Fallen: Cache-Poisoned Denial-of-Service Attack](https://cpdos.org/paper/Your_Cache_Has_Fallen__Cache_Poisoned_Denial_of_Service_Attack__Preprint_.pdf) introducing *Cache-Poisoning-DoS attack (CPDoS)* with `X-HTTP-Method-Override`, `X-Oversized-Header` and `X-Metachar-Header` on various CDNs, web servers and web application firewalls.

### HTTP method overriding headers support of tested web frameworks


| Web framework | Programming lang. | Method overriding support | Error code when method not implemented |
| --- | --- | --- | --- |
| Rails | Ruby | # | undefined |
| Django | Python | ## | 405 |
| Flask | Python | ## | 405 |
| Express.js | JavaScript | ## | 405 |
| Meteor.js | JavaScript | # | undefined |
| BeeGo | Go | # | undefined |
| Gin | Go | # | undefined |
| Play 1 | Java | ### | 404 |
| Play 2 | Java/Scala | # | undefined |
| Spring Boot | Java | # | undefined |
| Symfony | PHP | ### | 405 |
| Lavarel | PHP | ### | 405 |
| ASP.NET | C# | # | undefined |

*Legend:* `#` must be implemented manually, `###` by default, `##` not by default but by extension

### Request header size limits of HTTP implementations

Here is the transformed table in Markdown format:

|  | HTTP implementation | Documented limit | Tested limit | Limit exceed error code |
| --- | --- | --- | --- | --- |
| CDN | Akamai | undefined | 32,760 bytes | No Response |
|  | Azure | undefined | 24,567 bytes | 400 |
|  | CDN77 | undefined | 16,383 bytes | 400 |
|  | CDNSun | undefined | 16,516 bytes | 400 |
|  | Cloudflare | undefined | ≈ 32,395 bytes | 400 |
|  | Cloudfront | 20,480 bytes | ≈ 24,713 bytes | 494 |
|  | Fastly | undefined | 69,623 bytes | No Response |
|  | G-Core Labs | undefined | 65,534 bytes | 400 |
|  | KeyCDN | undefined | 8,190 bytes | 400 |
|  | StackPath | undefined | ≈ 85,200 bytes | 400 |
| HTTP engine | Apache HTTPD | 8,190 bytes | 8,190 bytes | 400 |
|  | Apache HTTPD + ModSecurity | undefined | 8,190 bytes | 400 |
|  | Apache TS | 131,072 bytes | 65,661 bytes | 400 |
|  | Nginx | undefined | 20,584 bytes | 400 |
|  | Nginx + ModSecurity | undefined | 8,190 bytes | 400 |
|  | IIS | undefined | 16,375 bytes | 400, (404) |
|  | Squid | 65,536 bytes | 65,527 bytes | 400 |
|  | Tomcat | undefined | 8,184 bytes | 400 |
|  | Varnish | 8,192 bytes | 8,299 bytes | 400 |
| Cloud Service | Amazon S3 | undefined | ≈ 7,948 bytes | 400 |
|  | Github Pages | undefined | 8,190 bytes | 400 |
|  | Gitlab Pages | undefined | >500,000 bytes | undefined |
|  | Google Cloud Storage | undefined | 16,376 bytes | 413 |
|  | Heroku | 8,192 bytes | 8,154 bytes | 400 |
| Web Framework | BeeGo | undefined | >500,000 bytes | undefined |
|  | Express.js | undefined | 81,867 bytes | No Response |
|  | Gin | undefined | >500,000 bytes | undefined |
|  | Meteor.js | undefined | 81,770 bytes | 400 |
|  | Play 1 | undefined | 8,188 bytes | No Response |
|  | Play 2 | 8,192 bytes | 8,319 bytes | 4 |

### Meta string handling in request header of HTTP implementations

| Meta character in request header | Akamai | Azure CDN | CDNSun | Cloudflare | Cloudfront | Fastly | G-Core Labs | KeyCDN | Stackpath |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `\u0000` | 400 | 400 | 400 | 400 | 400 | 400 | No Response | 400 | 400 |
| `\u0001` ... `\u0006` | # | 400 | Sanitized | # | # | 400 | # | # | 400 |
| `\a` | # | 400 | Sanitized | # | # | 400 | # | # | 400 |
| `\b` | # | 400 | Sanitized | # | # | 400 | # | # | 400 |
| `\t` | # | # | # | # | # | # | # | # | # |
| `\n` | # | 400 | Sanitized | Sanitized | Sanitized | Sanitized | Sanitized | # | Sanitized |
| `\v` | # | 400 | Sanitized | # | Sanitized | 400 | # | # | Sanitized |
| `\f` | # | 400 | Sanitized | # | Sanitized | 400 | # | # | Sanitized |
| `\r` | # | 400 | Sanitized | Sanitized | Sanitized | 400 | Sanitized | # | Sanitized |
| `\u000e` ... `\u001f`, `\u007f` | # | 400 | Sanitized | # | # | 400 | # | # | 400 |
| Multiple Unicode control character (e.g. `\u0001\u0002`) | # | 400 | Sanitized | # | # | 400 | # | # | 400 |
| `(){0;}; touch /tmp/blns.shellshock1.fail;` | # | # | # | # | 403 | # | # | # | # |
| `() { _; } >_[$($())] { touch /tmp/blns.shellshock2.fail; }` | # | # | # | # | 403 | # | # | # | # |

| Meta character in request header | Apache HTTPD + (ModSecurity) | Apache TS | Nginx + (ModSecurity) | IIS | Tomcat | Squid | Varnish | Amazon S3 | Google Storage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `\u0000` | 400 | 400 | 400 | 400 | # | 400 | # | # | # |
| `\u0001` ... `\u0006` | 400 | # | # | 400 | # | 400 | # | # | # |
| `\a` | 400 | # | # | 400 | # | 400 | # | # | # |
| `\b` | 400 | # | # | 400 | # | 400 | # | # | # |
| `\t` | # | # | # | 400 | # | 400 | # | # | # |
| `\n` | 400 | # | Sanitized | # | # | # | Sanitized | # | # |
| `\v` | 400 | # | # | 400 | # | 400 | # | # | # |
| `\f` | 400 | # | # | 400 | # | 400 | # | # | # |
| `\r` | 400 | # | # | 400 | # | 400 | # | # | # |
| `\u000e` ... `\u001f`, `\u007f` | 400 | # | # | 400 | # | 400 | # | # | # |
| Multiple Unicode control character (e.g. `\u0001\u0002`) | 400 | # | # | 400 | # | 400 | # | # | # |
| `(){0;}; touch /tmp/blns.shellshock1.fail;` | # | # | # | # | # | # | # | # | # |
| `() { _; } >_[$($())] { touch /tmp/blns.shellshock2.fail; }` | # | # | # | # | # | # | # | # | # |

| Meta character in request header | Github Pages | Gitlab Pages | Heroku | Beego | Express.js | Gin | Meteor | Play 1 | Play 2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `\u0000` | No Response | 400 | # | 400 | # | 400 | 400 | # | 400 |
| `\u0001` ... `\u0006` | 400 | 400 | # | 400 | # | 400 | 400 | # | 400 |
| `\a` | 400 | 400 | # | 400 | # | 400 | 400 | # | 400 |
| `\b` | 400 | 400 | # | 400 | # | 400 | 400 | # | 400 |
| `\t` | 400 | # | # | # | # | # | # | # | # |
| `\n` | 400 | # | 400 | # | # | # | # | # | # |
| `\v` | 400 | 400 | # | 400 | # | 400 | 400 | # | 400 |
| `\f` | 400 | 400 | # | 400 | # | 400 | 400 | # | 400 |
| `\r` | 400 | 400 | # | 400 | # | 400 | # | # | 400 |
| `\u000e` ... `\u001f` | 400 | 400 | # | 400 | # | 400 | 400 | # | 400 |
| `\u0007f` | 400 | 400 | # | 400 | # | 400 | 400 | # | # |
| Multiple Unicode control character (e.g. `\u0001\u0002`) | 400 | 400 | # | 400 | No Response | 400 | No Response | # | 400 |
| `(){0;}; touch /tmp/blns.shellshock1.fail;` | # | # | # | # | # | # | # | # | # |
| `() { _; } >_[$($())] { touch /tmp/blns.shellshock2.fail; }` | # | # | # | # | # | # | # | # | # |

*Legend:* `#`  processed/forwarded without error and sanitization


## Headers indicating caching from various cache service and software

| **Cache Service/Software**      | **Response Header**               | **Hit**                      | **Miss**                     |
|---------------------------------|-----------------------------------|------------------------------|------------------------------|
| **Azure**                       | **X-Cache**                       | **TCP_HIT**                  | **TCP_MISS**                 |
| **Fastly**                      | **X-Cache**                       | **HIT**                      | **MISS**                     |
| **Akamai**                      | **X-Cache, Server-Timing**        | **desc=HIT**                 | **desc=MISS**                |
| **CDN77**                       | **X-Cache, X-77-Cache**           | **HIT**                      | **MISS**                     |
| **CloudFront**                  | **X-Cache**                       | **Hit from cloudfront**      | **Miss from cloudfront / RefreshHit from cloudfront**     |
| **UDomain**                     | **X-Cache-Status**                | **HIT**                      | **MISS**                     |
| **KeyCDN**                      | **X-Cache**                       | **HIT**                      | **MISS**                     |
| **Cloudflare**                  | **CF-Cache-Status**               | **HIT**                      | **MISS**                     |
| **GCoreLabs**                   | **Cache**                         | **HIT**                      | **MISS**                     |
| **ChinaCache**                  | **X-cc-via**                      | **\*[H,\*]**                 | **\*[M,\*]**                 |
| **Github Pages**                | **X-Cache**                       | **HIT**                      | **MISS**                     |
| **Google Cloud**                | **cdn_cache_status**              | **hit**                      | **mis**                      |
| **Incapsula CDN**               | **X-Iinfo**                       | **...0CNN...**               | **...PNNN...**               |
| **AlibabaCloud**                | **X-Cache**                       | **HIT TCP_IMS_HIT**          | **MISS TCP_MISS**            |
| **Tencent Cloud**               | **X-Cache-Lookup**                | **Hit From * / Cache Hit**   | **Cache Miss**               |
| **HUAWEI CLOUD**                | **X-Cache-Lookup**                | **Hit From \***              | **Miss From \***             |
| **Baidu AI Cloud CDN**          | **X-Cache-Status**                | **HIT**                      | **MISS**                     |
| **Apache Traffic Server**       | **X-Cache**                       | **HIT**                      | **MISS**                     |
| **Squid**                       | **X-Cache**                       | **Hit From \***              | **Miss From \***             |
| **Varnish**                     | **X-Cache**                       | **HIT**                      | **MISS**                     |
| **Nginx**                       | **Cache_status, X-Proxy-Cache**   | **HIT**                      | **MISS**                     |
| **Apache**                      | **X-Cache**                       | **HIT**                      | **MISS**                     |
| **Rack Cache**                  | **X-Rack-Cache**                  | **Hit**                      | **Fresh/Miss**               |

As JSON:

```
[
  {
    "Cache Service/Software": "Azure,"
    "Response Header": "X-Cache",
    "Hit": "TCP_HIT",
    "Miss": "TCP_MISS"
  },
  {
    "Cache Service/Software": "Fastly",
    "Response Header": "X-Cache",
    "Hit": "HIT",
    "Miss": "MISS"
  },
  {
    "Cache Service/Software": "Akamai",
    "Response Header": "X-Cache, Server-Timing",
    "Hit": "desc=HIT",
    "Miss": "desc=MISS"
  },
  {
    "Cache Service/Software": "CDN77",
    "Response Header": "X-Cache, X-77-Cache",
    "Hit": "HIT",
    "Miss": "MISS"
  },
  {
    "Cache Service/Software": "CloudFront",
    "Response Header": "X-Cache",
    "Hit": "Hit from cloudfront",
    "Miss": "Miss from cloudfront"
  },
  {
    "Cache Service/Software": "UDomain",
    "Response Header": "X-Cache-Status",
    "Hit": "HIT",
    "Miss": "MISS"
  },
  {
    "Cache Service/Software": "KeyCDN",
    "Response Header": "X-Cache",
    "Hit": "HIT",
    "Miss": "MISS"
  },
  {
    "Cache Service/Software": "Cloudflare",
    "Response Header": "CF-Cache-Status",
    "Hit": "HIT",
    "Miss": "MISS"
  },
  {
    "Cache Service/Software": "GCoreLabs",
    "Response Header": "Cache",
    "Hit": "HIT",
    "Miss": "MISS"
  },
  {
    "Cache Service/Software": "ChinaCache",
    "Response Header": "X-cc-via",
    "Hit": "*[H,*]",
    "Miss": "*[M,*]"
  },
  {
    "Cache Service/Software": "Github Pages",
    "Response Header": "X-Cache",
    "Hit": "HIT",
    "Miss": "MISS"
  },
  {
    "Cache Service/Software": "Google Cloud",
    "Response Header": "cdn_cache_status",
    "Hit": "hit",
    "Miss": "mis"
  },
  {
    "Cache Service/Software": "Incapsula CDN",
    "Response Header": "X-Iinfo",
    "Hit": "...0CNN...",
    "Miss": "...PNNN..."
  },
  {
    "Cache Service/Software": "AlibabaCloud",
    "Response Header": "X-Cache",
    "Hit": "HIT TCP_IMS_HIT",
    "Miss": "MISS TCP_MISS"
  },
  {
    "Cache Service/Software": "Tencent Cloud",
    "Response Header": "X-Cache-Lookup",
    "Hit": "Hit From * / Cache Hit",
    "Miss": "Cache Miss"
  },
  {
    "Cache Service/Software": "HUAWEI CLOUD",
    "Response Header": "X-Cache-Lookup",
    "Hit": "Hit From *",
    "Miss": "Miss From *"
  },
  {
    "Cache Service/Software": "Baidu AI Cloud CDN",
    "Response Header": "X-Cache-Status",
    "Hit": "HIT",
    "Miss": "MISS"
  },
  {
    "Cache Service/Software": "Apache Traffic Server",
    "Response Header": "X-Cache",
    "Hit": "HIT",
    "Miss": "MISS"
  },
  {
    "Cache Service/Software": "Squid",
    "Response Header": "X-Cache",
    "Hit": "Hit From *",
    "Miss": "Miss From *"
  },
  {
    "Cache Service/Software": "Varnish",
    "Response Header": "X-Cache",
    "Hit": "HIT",
    "Miss": "MISS"
  },
  {
    "Cache Service/Software": "Nginx",
    "Response Header": "Cache_status, X-Proxy-Cache",
    "Hit": "HIT",
    "Miss": "MISS"
  },
  {
    "Cache Service/Software": "Apache",
    "Response Header": "X-Cache",
    "Hit": "HIT",
    "Miss": "MISS"
  },
  {
    "Cache Service/Software": "Rack Cache",
    "Response Header": "X-Rack-Cache",
    "Hit": "Hit",
    "Miss": "Fresh/Miss"
  }
]
```

## Interesting Publications

* A Methodology for Web Cache Deception Vulnerability Discovery https://www.scitepress.org/Papers/2024/126920/126920.pdf
* Internet’s Invisible Enemy: Detecting and Measuring Web Cache
Poisoning in the Wild https://www.jianjunchen.com/p/web-cache-posioning.CCS24.pdf