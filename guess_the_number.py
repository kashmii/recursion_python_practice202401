import sys
import random

def input_validation(num):
        try:
                int(num)
        except ValueError as e:
                print(f'Error: {e}')
                sys.exit()

# Part 1 最小値と最大値を入力してもらう
sys.stdout.buffer.write(b'Input 2 numbers. Smaller one and bigger.\n')
sys.stdout.flush()
smaller_num = sys.stdin.buffer.readline().decode().rstrip('\n')

input_validation(smaller_num)

sys.stdout.buffer.write(b'Bigger one please.\n')
sys.stdout.flush()

bigger_num = sys.stdin.buffer.readline().decode().rstrip('\n')

input_validation(bigger_num)
# check num's big and small
if int(smaller_num) >= int(bigger_num):
        print(f"Error: 2nd number must be larger than 1st one!")
        sys.exit()

# Part 2 乱数を生成する
random_int = random.randint(int(smaller_num), int(bigger_num))

# Part 3 乱数を推測してもらい、正解したら終了
sys.stdout.buffer.write(b'Guess the number between ones you input.\nYou have 3 chances.\n')
sys.stdout.flush()

print('? ? ? ? ?')
print('? ? ? ? ?')
print('? ? ? ? ?')

guessed_num = sys.stdin.buffer.readline().decode().rstrip('\n')
input_validation(guessed_num)

for _ in range(3):
        if random_int == int(guessed_num):
                print('You got it!!! The number is ' + guessed_num + '\nCongratulations!!!')
                sys.exit()
        else:
                print('No, try again')
                guessed_num = sys.stdin.buffer.readline().decode().rstrip('\n')
                input_validation(guessed_num)

print('Oh, you failed. The number was ' + str(random_int) + '\nTry again!')
