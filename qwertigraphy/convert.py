
import argparse
import csv
import re
import sys
from functools import partial

from grascii import grammar
from grascii import GrasciiParser, GrasciiValidator

from lark import UnexpectedInput

stroke_map = {
        "c": "CH",
        "ch": "CH",
        "df": "DF",
        "dm": "DM",
        "dn": "DN",
        "ea": "A&'",
        "eu": "EU",
        "h": "'",
        "ia": "A&E",
        "jnt": "JNT",
        "ld": "LD",
        "rd": "RD",
        "mn": "MN",
        "mt": "MT",
        "nd": "ND",
        "ng": "NG",
        "nk": "NK",
        "nt": "NT",
        "oe": "OE",
        "sh": "SH",
        "s2h": "SH",
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
        # supp
        "pl": "PL",
        "pr": "PR",
        "bl": "BL",
        "ss": "SS",
        "re": "RE",
        "y": "E",
        "kp": "KP",
        "br": "BR",
        # core
        "fl": "FL",
        "fr": "FR",
        "xs": "XS",
        "ss2": "SS(",  # base direction on the lower s
        "s2s": "SS)",  # base direction on the lower s
        "o1": "O",
        "o2": "O(",
        "ea2": "A&E~",
        "ye2": "E~|",
        "ya2": "A~|",
        "yi2": "I~|",
        "<": "\\",
        "": "",
}

SUBSTITUTIONS = [
    partial(re.compile(r"\^-h-\\").sub, "h"),  # leading aspirate
    partial(re.compile(r"\\-h").sub, "h"),  # ending -ing
    partial(re.compile(r"s22").sub, "s2"),  # correct a probable typo
]

def transform(form):
    if form.startswith("^-"):
        # handle prefixes
        form = form[2:] + "-/"
    for sub in SUBSTITUTIONS:
        form = sub(form)
    return form

gparser = GrasciiParser()

def convert_stroke(stroke):
    try:
        return stroke_map[stroke.lower()]
    except KeyError:
        interpretations = gparser.interpret(stroke.upper())
        return "".join(interpretations[0])


def convert(form):
    form = transform(form)
    tokens = form.split('-')
    try:
        tokens = list(map(convert_stroke, tokens))
    except UnexpectedInput:
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
            total_count = 0
            success_count = 0
            for row in reader:
                converted = convert(row["form"])
                if converted:
                    success_count += 1
                    out.write(converted)
                    out.write(" ")
                    out.write(row["word"])
                    out.write("\n")
                else:
                    print(row["word"], row["form"], transform(row["form"]))
                total_count += 1

        print(f"Successfully converted {success_count}/{total_count} ({success_count / total_count * 100:.2f}%)")
