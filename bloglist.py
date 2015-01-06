#!coding:utf-8
import configparser
from requests_oauthlib import OAuth1Session


class blogget:
    def __init__(self):
        conf = configparser.ConfigParser()
        conf.read('./config.ini')
        self.oauth_consumer_key = conf.get('hatena', 'oauth_consumer_key')
        self.oauth_consumer_secret = conf.get('hatena', 'oauth_consumer_secret')
        self.blog_api_key = conf.get('hatena', 'api_key')
        self.rootendpoint = conf.get('hatena', 'rootendpoint')
        self.access_token = conf.get('hatena', 'access_token')
        self.access_token_secret = conf.get('hatena', 'access_token_secret')

    def getblog_all(self):
        auth = OAuth1Session(self.oauth_consumer_key, self.oauth_consumer_secret, self.access_token, self.access_token_secret)
        res = auth.get('http://kuroneko0208.hatenablog.com/atom/entry')
        print(res.text)

    def getblog_recent(self):
        auth = OAuth1Session(self.oauth_consumer_key, self.oauth_consumer_secret, self.access_token, self.access_token_secret)
        auth_res = auth.get('https://blog.hatena.ne.jp/kuroneko0208/kuroneko0208.hatenablog.com/atom/entry')
        listrow_id = filter(lambda x: x.find('<link rel="edit"') >= 0, auth_res.text.split('\n'))
        listrow_title = filter(lambda x: x.find('<title>') >= 0, auth_res.text.split('\n'))
        list_id = map(lambda x: x.split('/')[7].split('"')[0], list(listrow_id))
        list_title = map(lambda x: x.split('>')[1].split('<')[0], list(listrow_title)[1:])
        result = zip(list_title, list_id)
        return list(result)

if __name__ == '__main__':
    pass
