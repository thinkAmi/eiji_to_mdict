"""
英辞郎をMDict形式に変換します。
"""

import argparse
import io
from pathlib import Path
import zipfile

from writemdict import MDictWriter
from .eiji_to_mdict import update_dicts


def get_args():
    parser = argparse.ArgumentParser(description='英辞郎ファイルからMDictファイルを作成します')
    parser.add_argument("zipFileName", help='英辞郎のzipファイル名です')
    return parser.parse_args()


def write_file(fileName, data):
    with open(fileName, 'wb') as outfile:
        writer = MDictWriter(data,
                            'EIJIdiom',
                            '\"UTF-8\" encoding.',
                            encoding='utf-8')
        writer.write(outfile)


def convert(path):
    d = {}
    idiom = {}

    with zipfile.ZipFile(path) as zf:
        originalFileName = zf.namelist()[0]
        
        with zf.open(originalFileName) as tf:
            for line in io.TextIOWrapper(tf, encoding='Shift-JIS', errors='ignore'):
                update_dicts(line, d, idiom)

    # デバッグ用途で入れておく
    print(d['within'])

    write_file('eijiro.mdx', d)
    write_file('eijidiom.mdx', idiom)


def main():
    args = get_args()

    path = Path(args.zipFileName)

    if not path.exists():
        print('ファイルが見つかりませんでした')
        return
    
    convert(path)

    print('処理を終了します')


if __name__ == '__main__':
    main()