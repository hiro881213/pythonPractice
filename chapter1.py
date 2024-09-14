# 変数の宣言
num = 1
name = 'Hiro'
is_ok = True

print('##### 変数の宣言 #####')
print(num)
print(name)
print(is_ok)

# 変数の型
print('##### 変数の型 #####')
print(type(num))
print(type(name))

# Boolean型
print('##### Boolean型 #####')
print(is_ok, type(is_ok))

# 変数に違う型を入れる
print('##### 変数に違う型を入れる #####')
num_2 = 1
name_2 = 'rihito'
print(name_2, type(name_2))

name_2 = num_2
print(name_2, type(name_2))

# 型変換処理
print('##### 型変換処理 #####')
name_3 = '1'
print(name_3, type(name_3))

new_num = int(name_3)
print(new_num, type(new_num))
