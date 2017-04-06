#!/usr/bin/env python3
# coding:utf-8
import operator
import string

import requests
import re

import zhon.hanzi
from bs4 import BeautifulSoup
import jieba


def get_web(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    body = response.text
    return body


def find_content(xml):
    bs = BeautifulSoup(xml, 'lxml')
    article = bs.body.find('div', {'class': 'article'})
    title = article.h1.get_text()
    content = article.find('div', {'class': 'show-content'}).get_text()
    return [title, content]


def clean_input(inputs):
    result = []
    for s in inputs:
        s = re.sub('\n+', '', s)
        s = re.sub(' +', '', s)
        s = re.sub('\s*', '', s)
        s = re.sub('\ufeff', '', s)
        s = re.sub('[%s]+' % zhon.hanzi.punctuation, '', s)
        s = re.sub('[%s]+' % string.punctuation, '', s)
        result.append(s)
    return result


def cut_word(inputs):
    results = []
    for s in inputs:
        cut = jieba.cut(s)
        for i in cut:
            results.append(i)
    return results


def count_word(inputs):
    results = {}
    for s in inputs:
        if s not in results:
            results[s] = 0
        results[s] += 1
    return results


def clean_words(inputs):
    results = {}
    for key, value in inputs:
        if len(key) > 1:
            results[key] = value
    return sorted(results.items(), key=operator.itemgetter(1), reverse=True)


def save_file(dict):
    with open('/home/wuhaojie/WorkSpace/Python/data.txt', 'w') as file:
        file.write('词语' + '\t\t\t' + '次数' + '\t\t\t')
        file.write('词语' + '\t\t\t' + '次数' + '\n')
        count = 1
        for k, v in dict:
            file.write(k + '\t\t\t' + str(v) + '\t\t\t')
            if count % 2 == 0:
                file.write('\n')
            count += 1


html = get_web('http://www.jianshu.com/p/c65582ffc06f')
contents = find_content(html)
bold_data = clean_input(contents)
words = cut_word(bold_data)
word_counts = count_word(words)
cleaned_counts = clean_words(word_counts.items())
save_file(cleaned_counts)
print(cleaned_counts)
