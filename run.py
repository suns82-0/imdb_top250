from scrapy import cmdline


name = 'imdb'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())
