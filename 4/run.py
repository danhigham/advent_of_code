import re

f = open("./4/input.txt")
raw_data = f.read().split("\n\n")

valid_records = 0
for x in raw_data:
    keys_to_find=['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']
    keys_validation={
        'byr': '19[2-9]{1}[0-9]{1}|200[0-2]',
        'iyr': '201[0-9]|2020',
        'eyr': '202[0-9]|2030',
        'hgt': '((1[5-8][0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6])in)',
        'hcl': '#[0-9a-f]{6}',
        'ecl': '^amb|blu|brn|gry|grn|hzl|oth$',
        'pid': '^[0-9]{9}$',
        'cid': '.?'
    }

    pairs = re.findall('([a-z]{3}:[a-zA-Z0-9#]*)', x)
    for pair in pairs:
        key = re.search('([a-z]{3}):', pair).groups(0)[0]
        keys_to_find.remove(key)

    if len(keys_to_find) == 0 or (len(keys_to_find) == 1 and keys_to_find[0] == "cid"):

        vals_valid = True

        for pair in pairs:
            key = re.search('([a-z]{3}):', pair).groups(0)[0]
            val = re.search('([a-z]{3}):(.*)', pair).groups(0)[1]

            validation_re = keys_validation[key]

            if key=="pid" and re.match(validation_re, val.strip()) != None:
                print(val + " " + str(vals_valid))

            if re.match(validation_re, val.strip()) == None:
                vals_valid = False
                break

            

        if vals_valid:
            valid_records = valid_records + 1

print(valid_records)