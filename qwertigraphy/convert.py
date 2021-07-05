
import argparse
import csv
import re
import sys

from grascii import grammar

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
    return join(tokens)

def join(tokens):
    exceptions = {"OE", "EU"}
    builder = []
    for i in range(len(tokens)):
        builder.append(tokens[i])
        if i + 1 < len(tokens):
            combined = tokens[i] + tokens[i + 1]
            if combined in grammar.STROKES and combined not in exceptions:
                builder.append("-")
            elif i + 2 < len(tokens):
                combined = tokens[i] + tokens[i + 1] + tokens[i + 2]
                if combined in grammar.STROKES and combined not in exceptions:
                    builder.append("-")
    return "".join(builder)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input_csv', type=argparse.FileType())
    parser.add_argument('output_file', type=argparse.FileType('w'))
    args = parser.parse_args(sys.argv[1:])

    with args.input_csv as csv_file:
        with args.output_file as out:
            reader = csv.DictReader(csv_file)
            count = 0
            for row in reader:
                converted = convert(row["form"])
                if converted:
                    count += 1
                    out.write(converted)
                    out.write(" ")
                    out.write(row["word"])
                    out.write("\n")
                else:
                    print(row["word"], row["form"], transform(row["form"]))

        print(count)
