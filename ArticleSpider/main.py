from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute(["scrapy", "crawl", "jianshu"])
# execute(["scrapy", "crawl", "infoq"])
# execute(["scrapy", "crawl", "zhihu"])
execute(["scrapy", "crawl", "github"])
