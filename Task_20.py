#20 В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JZ', 10: 'QZ'}
points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}

word = input().upper()#перевод строки в верхний регистр
count = 0
if word[0] in 'QWERTYUIOPASDFGHJKLZXCVBNM':
    for sym in word:
        for point in points_en:
            if sym in points_en[point]:
                count += point
else:
    for sym in word:
        for point in points_ru:
            if sym in points_ru[point]:
                count += point
print(count)