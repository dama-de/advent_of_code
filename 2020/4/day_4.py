import re


def check_height(h):
    height, unit = re.fullmatch("(\\d{2,3})(cm|in)", h).groups()
    return (unit == "cm" and 150 <= int(height) <= 193) or (unit == "in" and 59 <= int(height) <= 76)


def solve(passports):
    required_fields = {"byr": lambda y: 1920 <= int(y) <= 2002,
                       "iyr": lambda y: 2010 <= int(y) <= 2020,
                       "eyr": lambda y: 2020 <= int(y) <= 2030,
                       "hgt": lambda h: check_height(h),
                       "hcl": lambda c: re.fullmatch("#[0-9a-f]{6}", c),
                       "ecl": lambda c: c in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
                       "pid": lambda i: re.fullmatch("\\d{9}", i)}

    all_present_count, all_valid_count = 0, 0
    for passport in passports:
        fields_with_value = [field.split(":") for field in re.split("[ \\n]", passport) if not field.startswith("cid")]
        existing_labels = [field[0] for field in fields_with_value]
        all_present = all(req in existing_labels for req in required_fields)
        all_present_count += all_present
        try:
            all_valid_count += (all_present and all(required_fields[field[0]](field[1]) for field in fields_with_value))
        except:
            continue

    return len(passports), all_present_count, all_valid_count


if __name__ == '__main__':
    fin = open("input.txt", "r")
    text = fin.read().split("\n\n")

    print(solve(text))
