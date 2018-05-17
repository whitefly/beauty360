from random import choice
class MiddleAgent(object):
    def __init__(self):
        # ios,window.firefox
        self.agent_pool = [
            'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
            "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:56.0) Gecko/20100101 Firefox/56.0"
        ]

    def process_request(self, request, spider):
        request.headers["User-Agent"] = choice(self.agent_pool)
