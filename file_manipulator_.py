import sys
import os

# =====
# =====
# 1. reverse inputpath outputpath:
#     inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成します

# 2. copy inputpath outputpath:
#     inputpath にあるファイルのコピーを作成し、outputpath として保存します

# 3. duplicate_contents inputpath n:
#     inputpath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputpath に n 回複製します

# 4. replace_string inputpath needle newstring:
#     inputpath にあるファイルの内容から文字列 'needle' を検索し、'needle' の全てを 'newstring' に置き換えます
# =====
# =====

# === バリデーション ===

def argAmountCheck(num):
  if len(sys.argv) != int(num):
    print(f"Error: arguments should be #{num}")
    sys.exit()

def argTypeCheck(file_path):
  if not (os.path.exists(file_path) and os.path.isfile(file_path)):
    print(f"Error: argument {file_path} should be a file")
    sys.exit()

# === 各メソッド ===

def reverse(file_path):
  argAmountCheck(4)
  argTypeCheck(sys.argv[2])
  content = ''

  with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()
    reversed_content = content[::-1]

  with open(sys.argv[3], "w", encoding="utf-8") as new_file:
    new_file.write(reversed_content)

def copy(file_path, new_file_path):
  argAmountCheck(4)
  argTypeCheck(file_path)
  content = ''

  with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

  with open(new_file_path, 'w', encoding="utf-8") as file:
    file.write(content)

def duplicate_contents(file_path, num):
  argAmountCheck(4)
  argTypeCheck(file_path)

  with open(file_path, "r+", encoding="utf-8") as file:
    content = file.read()
    for _ in range(num):
      file.write(content)

def replace_string(file_path, needle, new_string):
  argAmountCheck(5)
  argTypeCheck(file_path)
  content = ''

  with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

  with open(file_path, "w", encoding="utf-8") as file:
    file.write(content.replace(needle, new_string))

# === メイン ===

if sys.argv[1] == 'reverse':
  reverse(sys.argv[2])
elif sys.argv[1] == 'copy':
  copy(sys.argv[2], sys.argv[3])
elif sys.argv[1] == 'duplicate_contents':
  duplicate_contents(sys.argv[2], int(sys.argv[3]))
elif sys.argv[1] == 'replace_string':
  replace_string(sys.argv[2], sys.argv[3], sys.argv[4])
else:
  print("Error: invalid argument")
  sys.exit()
