# Напишите программу, которая принимает на вход строку и отслеживает, сколько раз
# каждый символ уже встречался. количество повторов добавляется к символам с помощью
# постфикса _n.
# Input: a a a b c a a d c d d 
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
  
# text = 'a a a b c a a d c d d'
# list_symbols = text.split()
# print(list_symbols)
# uniq_symb = dict()
# for symbol in list_symbols:
#     if symbol not in uniq_symb:
#         uniq_symb[symbol] = 0
#         print(symbol, end= " ")
#     else:
#         uniq_symb[symbol] +=1
#         print(f"{symbol}_{uniq_symb[symbol]}", end=" ")
        
#2.--------------------------------------------------------

text = 'a a a b c a a d c d d'
list_symbols = text.split()
print(list_symbols)
uniq_symb = dict()
print()
result = ""
for symbol in list_symbols:
    if symbol not in uniq_symb:

        result += f"{symbol} "
    else:

        result += f"{symbol}_{uniq_symb[symbol]} "
    uniq_symb[symbol] = uniq_symb.get(symbol, 0) +1
print(result.strip())

