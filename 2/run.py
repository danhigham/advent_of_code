import re

f = open("./2/input.txt")
raw_data = f.read().split("\n")

first_valid_count = 0
second_valid_count = 0

for x in raw_data:
    if (x.strip()==""):
        continue
    value = re.search(':\s([a-z]*)', x).group(1)
    minOcc = int(re.search('^(\d*)-', x).group(1))
    maxOcc = int(re.search('^\d*-(\d*)\s', x).group(1))
    letter = re.search('^\d*-\d*\s([a-z])', x).group(1)

    firstPos = minOcc
    secondPos = maxOcc

    occCount = value.count(letter)

    if (occCount >= minOcc and occCount <= maxOcc):
        first_valid_count = first_valid_count + 1

    print(value[firstPos-1] + " " + letter)

    if (value[firstPos-1] == letter and value[secondPos-1] == letter):
        continue
    if (value[firstPos-1] == letter or value[secondPos-1] == letter):
        second_valid_count = second_valid_count + 1

print(first_valid_count)
print(second_valid_count)
print(len(raw_data))