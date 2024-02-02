# -*- coding: utf-8 -*-
"""
英辞郎をMDict形式に変換します。
"""

from writemdict import MDictWriter, encrypt_key
import sys
import codecs
import re

args = sys.argv

d = {}
idiom = {}
change = {'■':' ' ,'【':'[' ,'】':']' ,'◆':'*'
        ,'〕':')' ,'〔':'(' ,'＠':'@' ,'〜':'~'
        ,'・':'*'}
change =  str.maketrans(change)

with codecs.open(args[1], 'r', 'Shift-JIS', 'ignore') as f:
    line = f.readline()

    while line:
        if line[:1] == '■':
            word,meaning = line[1:].split(':',1)
            match = re.findall(r'｛.+?｝', meaning)
            for m in match:
                meaning = meaning.replace(m,'')
            match = re.search(r'{(.+)}', word)
            if match:
                word = word.replace(match.group(0),'')  # 検索パターン全体に一致する文字列
                meaning = '<' + match.group(1)+ '>' + meaning
            word = word.rstrip()
            meaning = meaning.rstrip().translate(change)
            if ' ' not in word and '-' not in word:
                if d.get(word):
                    d[word] += '\n' + meaning
                else:
                    d[word] = meaning
            else:
                if idiom.get(word):
                    idiom[word] += '\n' + meaning
                else:
                    idiom[word] = meaning
        line = f.readline()

print(d['within'])

with open('eijiro.mdx', 'wb') as outfile:
    writer = MDictWriter(d,
                         'EIJIRO',
                         '\"UTF-8\" encoding.',
                         encoding='utf-8')
    writer.write(outfile)

with open('eijidiom.mdx', 'wb') as outfile:
    writer = MDictWriter(idiom,
                         'EIJIdiom',
                         '\"UTF-8\" encoding.',
                         encoding='utf-8')
    writer.write(outfile)