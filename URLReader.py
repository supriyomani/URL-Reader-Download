import urllib.request
from html.parser import HTMLParser
from html.entities import name2codepoint

urlpart1 = "http://"
urlpart2 = "www."
urlpart3 = ""
urlpart4 = "space"
urlpart5 = ".com"

def downloadImg(DIUrlPath2):
    DIopfilename = DIUrlPath2
    ##DIopfilename
    DIUrlPath1 = urlpart1+urlpart2+urlpart3+urlpart4+urlpart5
    DIUrlPath = DIUrlPath1+"/"+DIUrlPath2
    urllib.request.urlretrieve(DIUrlPath,"E://Kohls//Exp//Pics//"+DIopfilename.replace("/","-"))

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)
    def handle_endtag(self, tag):
        print("End tag  :", tag)
    def handle_data(self, data):
        print("Data     :", data)
    def handle_comment(self, data):
        print("Comment  :", data)
    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)
    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)
    def handle_decl(self, data):
        print("Decl     :", data)

class MyAnchorParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "a" or tag == "link":
            print("Start tag:", tag)
            for attr in attrs:
                print("     attr:", attr)

class MyImgParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "img":
            for attr in attrs:
                if attr[0] == 'src':
                    urlpart2 = attr[1]
                    if urlpart2[0:4] == "http" or urlpart2[0:2] == "..":
                        print("urlpart2:", urlpart2)
                    else:
                        print("urlpart2:", urlpart2)
                        ##downloadImg(urlpart2)

try:
    UrlPath1 = urlpart1+urlpart2+urlpart3+urlpart4+urlpart5
    for x in range(0, 10):
        for y in range(0, 10):
            UrlPath2 = "image.php?img="+str(x)+"-"+str(y)+".jpg"
            local_filename, headers = urllib.request.urlretrieve(UrlPath1+"/"+UrlPath2)
            html = open(local_filename)
            parser = MyImgParser()
            parser.feed(html.read())
except urllib.error.URLError as e:
    print(e.reason)
