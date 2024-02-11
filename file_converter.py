# -*- coding: utf-8 -*-
# 次のコマンドでマークダウンをHTMLに変換する
# python3 file_converter.py markdown sample.md output.md

import markdown
import sys
import os

# === バリデーション ===

def argAmountCheck(num):
  if len(sys.argv) != int(num):
    print("Error: arguments should be #{}".format(num))
    sys.exit()

def argTypeCheck(file_path):
  if not (os.path.exists(file_path) and os.path.isfile(file_path)):
    print("Error: argument {} should be a file".format(file_path))
    sys.exit()

# === メソッド ===

def convertToHtml(file_path, new_file_path):
  argAmountCheck(4)
  argTypeCheck(sys.argv[2])
  content = ''

  with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

  with open(new_file_path, "w", encoding="utf-8") as new_file:
    html = markdown.markdown(content)
    new_file.write(html)

# === メイン処理 ===

if sys.argv[1] == 'markdown':
  convertToHtml(sys.argv[2], sys.argv[3])
else:
  print("Error: invalid argument")
  sys.exit()
