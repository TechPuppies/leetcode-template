# coding=utf-8
import os
import re
import threading
import urllib2
from bs4 import BeautifulSoup


LANG = 'python'
COMMENT_MARK = '#'
FILE_EXT = 'py'


class DownloadThread(threading.Thread):

    def __init__(self, tr):
        threading.Thread.__init__(self)
        self.tr = tr

    def run(self):
        tr = self.tr
        a = tr.find_all('a')[0]
        rate = tr.find_all('td')[3].text
        url = a.get('href')
        name = url.split('/')[2].replace('-', '_')
        print('downloading... %s' % name)
        if url == '#':
            return
        with open(LANG + '/' + name + '.' + FILE_EXT, 'wb') as pyfile:
            res = self._add_head(rate.encode('utf-8'), url.encode('utf-8'))
            subps_html = urllib2.urlopen(
                "https://oj.leetcode.com" + url).read()
            subps = BeautifulSoup(subps_html)

            content = subps.select('div.question-content')[0].text
            contents = content.replace('\r', '').split('\n')
            for line in contents:
                line = line.strip()
                res.extend(self._limit_line_length(line.encode('utf-8')))

            codes = re.findall(
                r'scope\.code\.' + LANG + ' \= \'(.*?)\'', subps_html)
            res.append(
                '\n\n' + codes[0].replace('\\u000D\\u000A', '\n')
                .replace('\u003C', '<')
                .replace('\u003E', '>')
                .replace('\u003D', '=')
                .replace('\u002D', '-')
                .replace('\r', ''))
            pyfile.write('\n'.join(res))

    def _add_head(self, rate, url):
        res = []
        if LANG == 'python':
            res = [COMMENT_MARK + ' coding=utf-8', ]
        res.append(COMMENT_MARK + ' AC Rate: ' + rate)
        url_str = 'SOURCE URL: https://oj.leetcode.com' + url
        res.extend(self._limit_line_length(url_str))
        return res

    def _limit_line_length(self, line, limit=76):
        if not line:
            return [COMMENT_MARK, ]
        if len(line) <= limit or LANG != 'python':
            return [COMMENT_MARK + ' %s' % line]
        else:
            res = []
            num = len(line) / limit
            for i in range(num+1):
                new_line = line[i * (limit + 1):(i + 1) * (limit + 1)]
                new_line = new_line.strip()
                if new_line:
                    res.append(COMMENT_MARK + ' %s' % new_line)
            return res


def main():
    global LANG, COMMENT_MARK, FILE_EXT
    msg = 'Please choose the programming'
    msg += ' language you want to practice:\n1. Python\n2. Java\n'
    l = raw_input(msg)

    while not l in ['1', '2']:
        l = raw_input('Only 1 or 2 is allowed.')

    if l == '1' or l == 1:
        COMMENT_MARK = '#'
        FILE_EXT = 'py'
        LANG = 'python'
    elif l == '2' or l == 2:
        COMMENT_MARK = '//'
        FILE_EXT = 'java'
        LANG = 'java'
    else:
        exit()

    if not os.path.exists(LANG):
        os.makedirs(LANG)

    ps = urllib2.urlopen("https://oj.leetcode.com/problems/").read()
    ps = BeautifulSoup(ps)
    ts = []
    for tr in ps.select('table#problemList')[0].find_all('tr'):
        if len(tr.find_all('td')) == 4:
            t = DownloadThread(tr)
            ts.append(t)
            t.start()

    for t in ts:
        t.join()
    print('Donezo!')

if __name__ == '__main__':
    main()
