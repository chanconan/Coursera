import re
def regex_find_sum(text):
    file = open(text)
    print(sum([int(i) for i in (re.findall("[0-9]+", file.read()))]))

print(regex_find_sum("regex_sum_42.txt"))
print(regex_find_sum("regex_sum_866594.txt"))