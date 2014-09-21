# coding=utf-8
import os
import re
import threading
import urllib2
from bs4 import BeautifulSoup

class Download(object):
    # default is python
    lang = 'python'
    ext = 'py'
    comment_mark = '#'
    limit = 80

    def __init__(self, url, rate):
        if url == '#':
            raise ValueError
        self.url = 'https://oj.leetcode.com%s' % url
        self.rate = rate

    def get_file_path(self):
        name = self.url.split('/')[-2].replace('-', '_')
        return '%s/%s.%s' % (self.lang, name, self.ext)

    def get_wrapped_line(self, line):
        line = line.rstrip()
        res = []
        if not line:
            pass
        elif len(line) <= self.limit:
            res.append('%s' % line )
        else:
            while len(line) > self.limit:
                break_point = line[:self.limit].rfind(' ')
                if break_point <= 0:
                    res.append(line)
                    break
                res.append(line[:break_point])
                line = line[break_point+1:]
        return res

    def get_html(self):
        if not hasattr(self, 'html') or not self.html:
            self.html = urllib2.urlopen(self.url).read()
        return self.html

    def get_parsed_html(self):
        if not hasattr(self, 'parsed_html') or not self.parsed_html:
            self.parsed_html = BeautifulSoup(self.get_html())
        return self.parsed_html

    def get_header(self):
        res = ['coding=utf-8', 'AC Rate: %s' % self.rate.encode('utf-8'), self.url.encode('utf-8')]
        return ['%s %s' % (self.comment_mark, i) for i in res]

    def get_content(self):
        res = []
        content = self.get_parsed_html().select('div.question-content')[0].text
        contents = content.replace('\r', '').split('\n')
        for line in contents:
            res.extend(self.get_wrapped_line(line.encode('utf-8')))
        return ['%s %s' % (self.comment_mark, i) for i in res]

    def get_code(self):
        pattern = r'scope\.code\.' + self.lang + r' \= \'(.*?)\''
        codes = re.findall(pattern,
            self.get_html(),
            re.U)[0].decode("unicode-escape").encode('utf-8')
        return codes.split('\r\n')

    def get_all(self):
        res = self.get_header()
        res.append('')
        res.extend(self.get_content())
        res.append('')
        res.extend(self.get_code())
        return res

    def download(self):
        with open(self.get_file_path(), 'wb') as source_file:
            print('downloading... %s' % self.get_file_path())
            source_file.write('\n'.join(self.get_all()))



class JavaDownload(Download):
    lang = 'java'
    ext = 'java'
    comment_mark = '//'
    limit = 80

    def get_file_path(self):
        name = self.url.split('/')[-2].replace('-', '_')
        name = name.title().replace('_', '')
        if ord(name[0]) < 65 or ord(name[0]) > 90:
            name = 'LC' + name
        folder = '%s/%s' % (self.lang, name)
        if not os.path.exists(folder):
            os.makedirs(folder)
        return '%s/Solution.%s' % (folder, self.ext)

    def get_header(self):
        res = super(JavaDownload, self).get_header()
        res.pop(0)
        return res

    def get_code(self):
        res = super(JavaDownload, self).get_code()
        res.insert(0, '')  # empty line
        res.insert(0, 'import java.util.*')
        return res

class CppDownload(Download):
    lang = 'cpp'
    ext = 'cpp'
    comment_mark = '//'
    limit = 80



class DownloadThread(threading.Thread):

    def __init__(self, tr, download_class):
        threading.Thread.__init__(self)
        self.tr = tr
        self.download_class = download_class

    def run(self):
        tr = self.tr
        url, rate = tr.find_all('a')[0].get('href'), tr.find_all('td')[3].text
        self.download_class(url, rate).download()


class DownloadAll():

    def __init__(self, lang):
        self.lang = lang
        if lang == 'python':
            self.download_class = Download
        elif lang == 'java':
            self.download_class = JavaDownload
        elif lang == 'cpp':
            self.download_class = CppDownload
        else:
            exit(-1)

    def get_list(self):
        ps = urllib2.urlopen("https://oj.leetcode.com/problems/").read()
        ps = BeautifulSoup(ps)
        for tr in ps.select('table#problemList')[0].find_all('tr'):
            yield tr

    def download_all(self):
        if not os.path.exists(self.lang):
            os.makedirs(self.lang)

        ts = []
        for tr in self.get_list():
            if len(tr.find_all('a')) > 0 and \
                tr.find_all('a')[0].get('href') != '#':
                t = DownloadThread(tr, self.download_class)
                ts.append(t)
                t.start()

            if len(ts) >= 20:
                while ts:
                    t = ts.pop()
                    t.join()

        while ts:
            t = ts.pop()
            t.join()
        print 'Donezo!'


def main():
    msg = 'Please choose the programming'
    msg += ' language you want to practice:\n1. Python\n2. Java\n3. C++\n'
    l = raw_input(msg)

    while not l in ['1', '2', '3']:
        l = raw_input('Only 1, 2 or 3 is allowed.')

    if l == '1' or l == 1:
        DownloadAll('python').download_all()
    elif l == '2' or l == 2:
        DownloadAll('java').download_all()
    elif l == '3' or l == 3:
        DownloadAll('cpp').download_all()
    else:
        exit()

if __name__ == '__main__':
    main()
