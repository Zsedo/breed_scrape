Requirements:
- Python 2.7.15
- Scrapy 1.5.0

Ran on:
```
Scrapy 1.5.0 started (bot: yapprScrape)
Versions: lxml 4.2.1.0, libxml2 2.9.8, cssselect 1.0.3, parsel
1.4.0, w3lib 1.19.0, Twisted 18.4.0, Python 2.7.15 (default, Sep 18 2018, 20:30:11) - [GCC 4.2.1 Compatible
Apple LLVM 9.0.0 (clang-900.0.39.2)], pyOpenSSL 18.0.0 (OpenSSL 1.1.0h  27 Mar 2018), cryptography 2.2.2, Platform Darwin-16.7.0-x86_64-i386-64bit
```

To launch run:
```
scrapy crawl yappr_spider -o name_of_save_file.csv
```

File will be opened with appending, so remember to either delete old file or save to a new file.