#!coding:utf-8
import sys
import post
import bloglist
import dbcontrol
import glob
import os
import datetime

if __name__ == '__main__':
    postfile = sys.argv[1].split('.md')[0]
    send = post.Post()
    blog = bloglist.blogget()
    res = None
    body = open(postfile + '.md', encoding='utf-8').read()

    if not(glob.glob(os.getcwd() + '/blogdb/')):
        db = dbcontrol.blogdb()
        [db.write(x[0], x[1]) for x in blog.getblog_all()]
    else:
        db = dbcontrol.blogdb()
        res = db.search(postfile)
    if res:
        send.send(postfile, body, datetime.datetime.now(), res.decode('utf-8'))
    else:
        send.send(postfile, body, datetime.datetime.now())
        [db.write(x[0], x[1]) for x in blog.getblog_all()]
