#辞書を読み込み
f = open("dictionary.txt")
data = f.read()
f.close()
dictionary_data = data.lower().split("\n")#大文字が含まれている場合、小文字に文字に直す


#1文字enter無し入力getch()
#(参照)https://torina.top/detail/428/
try:
    from msvcrt import getch
except ImportError:
    def getch():
        import sys
        import tty
        import termios
        fd = sys.stdin.fileno()#標準入力のファイルディスクプリタを取得
        old = termios.tcgetattr(fd)#fdの端末属性をゲットする
        try:
            tty.setraw(fd)#fdのモードをrawモードに切替
            return sys.stdin.read(1)#入力したデータを受け取って表示
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)#fdモードをoldから取得

            
#main
input_char = ""#入力された文字
match = ""#入力された文字に含まれる単語全て
long_char = ""#BESTな単語
char_point = 0#dictionaryの得点
long_char_point = 0#BESTな単語の得点

while True:
    print(match)
    print("BEST : " + long_char)
    
    key = ord(getch())
    input_char += chr(key)
    print("\n>>> " + input_char + "\n")
    if key == 3:#C-x-cで終了
        break
    else:
        match = ""
        for dictionary in dictionary_data:
            each_dictionary = list(dictionary)
            char = input_char
            count = 0
            for match_char in each_dictionary:
                if char.find(match_char) != -1:
                    char = char[:(char.find(match_char))]+char[(char.find(match_char))+1:]
                else:
                    count = 1
                    break
            if count != 1:
                match += dictionary + " "
                char_point = len(dictionary)
                
                for d in dictionary:
                    if d == "c" or d == "f" or d == "h" or d == "l" or d == "m" or d == "p" or d == "v" or d == "w" or d == "y":
                        char_point += 1
                    elif d == "j" or d == "k" or d == "q" or d == "x" or d == "z":
                        char_point += 2
                if long_char_point < char_point:
                    long_char = dictionary
                    long_char_point = char_point
                     

        
                     
