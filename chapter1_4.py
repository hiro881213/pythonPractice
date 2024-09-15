print("##### 文字列を表示する ######")
s = "help"
print(s)

print("##### 文字列を表示する2 ######")
print("help")

print("##### シングルクオートとダブルクオート #####")
print('single')
print("double")

print("##### ダブルクオートの中にシングルクオート #####")
print("I don't know")

print("##### シングルクオートの中にシングルクオート #####")
print('I don\'t know')

print("ダブルクオートの中にダブルクオート")
print("say \"I don't know\"")

print("##### 改行 #####")
print('Hello.\nHow are you?')

print("##### 意図せぬ改行の回避 #####")
print(r'C:\name\name')

print("##### 複数行にわたる文字列の出力 #####")
print("""
    line 1
    line 2
    line 3
""")

print("##### 複数行にわたる文字列の出力(不要な文字を削除) #####")
print("*************************")
print("""\
    line 1 
    line 2
    line 3\
""")
print("*************************")

print("##### 文字列を連結する(掛け算) #####")
print("Hello" * 3)

print("##### 文字列を連結する(連結) #####")
print("Hi " * 3 + 'Mike')
