import re


MAPPING =  str.maketrans(
    {
        '■':' ',
        '【':'[',
        '】':']',
        '◆':'*',
        '〕':')',
        '〔':'(',
        '＠':'@',
        '〜':'~',
        '・':'*'
    }
)


def update_dicts(line: str, d: dict, idiom: dict):
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
        meaning = meaning.rstrip().translate(MAPPING)
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
