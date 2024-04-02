# def rifma(poem):
#     phrases_list = poem.lower().split()
#     sum_vowels = lambda phrase: sum(1 for symbol in phrase if symbol in "аеёиоуыэюя")
#     tmp = sum_vowels(phrases_list[0])
#     if all([sum_vowels(phrase) ==tmp for phrase in phrases_list[1:]]):
#         return "Парам пам-пам"
#     return "Пам парам"

# print(rifma('пара-ра-рам рам-пам-папам па-ра-па-дам'))

#2----------------------------

def rifma(poem):
    phrases_list = poem.lower().split()
    if len(phrases_list) <= 1:
        return "Количество фраз должно быть больше одной!"
    sum_vowels = lambda phrase: len(list(filter(lambda symbol: symbol in "аеёиоуыэюя", phrase)))
    vowels_0 = sum_vowels(phrases_list[0])
    if all(map(lambda phrase:sum_vowels(phrase) ==vowels_0, phrases_list[1:])):
        return "Парам пам-пам"
    return "Пам парам"
    
        

poem = 'за-гад-ка-ра-свет-ка-ра-газ-да-не-на-ма-ли-ва-ла'

print(rifma(poem))