# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, razd=','):
    str1 = set(str1.split(razd))
    str2 = set(str2.split(razd))
    s = str1.intersection(str2)
    return sorted(s)



participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, '|'))
# TODO Провеьте работу функции с разделителем отличным от запятой
