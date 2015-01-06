#!coding:utf-8
import configparser
from requests_oauthlib import OAuth1Session
import time


class Post:
    def __init__(self):
        conf = configparser.ConfigParser()
        conf.read('./config.ini')
        self.oauth_consumer_key = conf.get('hatena', 'oauth_consumer_key')
        self.oauth_consumer_secret = conf.get('hatena', 'oauth_consumer_secret')
        self.blog_api_key = conf.get('hatena', 'api_key')
        self.rootendpoint = conf.get('hatena', 'rootendpoint')
        self.access_token = conf.get('hatena', 'access_token')
        self.access_token_secret = conf.get('hatena', 'access_token_secret')

    def send(self, title, body, updated, blog_id=None):
        xmlbody = '<?xml version="1.0" encoding="utf-8"?>\
<entry xmlns="http://www.w3.org/2005/Atom"\
xmlns:app="http://www.w3.org/2007/app">\
<title>%s</title>\
<author><name>name</name></author>\
<content type="text/plain">\
%s \
</content>\
<updated>%s</updated>\
<app:control>\
<app:draft>yes</app:draft>\
</app:control>\
</entry>' % (title, body, updated.strftime("%Y-%m-%dT%H:%M:%S"))
        auth = OAuth1Session(self.oauth_consumer_key, self.oauth_consumer_secret, self.access_token, self.access_token_secret)
        if blog_id:
            print(str(int(time.mktime(updated.timetuple()))))
            auth.put(self.rootendpoint + '/entry/' + blog_id, data=xmlbody)
        else:
            auth.post(self.rootendpoint + '/entry', data=xmlbody)

if __name__ == '__main__':
    post = Post()
    post.new('tes', 'tesss')
