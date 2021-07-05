
import csv
import re

stroke_map = {
        "ch": "CH",
        "df": "DF",
        "ea": "A&'",
        "h": "'",
        "ia": "A&E",
        "jnt": "JNT",
        "ld": "LD",
        "mn": "MN",
        "mt": "MT",
        "ng": "NG",
        "nk": "NK",
        "nt": "NT",
        "sh": "SH",
        "ss": "SS",
        "td": "TD",
        "th": "TH",
        "tm": "TM",
        "tn": "TN",
        "w": "_",
        "ya": "A|",
        "ye": "E|",
        "yi": "I|",
        "a": "A",
        "a1": "A",
        "a2": "A~",
        "e": "E",
        "e1": "E",
        "e2": "E~",
        "i": "I",
        "i1": "I",
        "i2": "I~",
        "s": "S",
        "s1": "S)",
        "s2": "S(",
        "th": "TH",
        "th1": "TH(",
        "th2": "TH)",
        "x": "X",
        "x1": "X)",
        "x2": "X(",
        "/": "^",
        "\\": "^",
        "b": "B",
        "d": "D",
        "f": "F",
        "g": "G",
        "j": "J",
        "k": "K",
        "l": "L",
        "m": "M",
        "n": "N",
        "o": "O",
        "p": "P",
        "r": "R",
        "t": "T",
        "u": "U",
        "v": "V",
        "z": "Z",
        "pl": "PL",
        "pr": "PR",
        "bl": "BL",
        "ss": "SS",
        "re": "RE",
}

def transform(form):
    form = re.sub(r"\^-\\-h", "h", form)
    form = re.sub(r"\\-h-e$", "/-e", form)
    form = re.sub(r"\\-h-s$", "/-s2", form)
    form = re.sub(r"\\-h", "h", form)
    return form

def convert(form):
    form = transform(form)
    tokens = form.split('-')
    try:
        tokens = list(map(lambda s: stroke_map[s], tokens))
    except KeyError:
        return
    return tokens

with open('./anniversary-supplement/anniversary_supplement.csv') as csv_file:
    reader = csv.DictReader(csv_file)
    count = 0
    for row in reader:
        converted = convert(row["form"])
        if converted:
            count += 1
            print(row["word"], converted)
        else:
            pass
            # print(row["word"], row["form"], transform(row["form"]))

    print(count)
