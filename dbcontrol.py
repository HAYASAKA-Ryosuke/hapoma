#!coding:utf-8
import plyvel


class blogdb:
    def __init__(self):
        self.db = plyvel.DB('./blogdb/', create_if_missing=True)

    def search(self, blogtitle):
        return self.db.get(str.encode(blogtitle))

    def write(self, blogtitle, postdate):
        self.db.put(str.encode(blogtitle), str.encode(postdate))

if __name__ == '__main__':
    blog = blogdb()
    print(blog.search(b'hello'))
    blog.write(str.encode('hello'), str.encode('12345'))
    print(blog.search(str.encode('hello')))
    blog.write(str.encode('hello'), str.encode('12348'))
    print(blog.search(str.encode('hello')))
