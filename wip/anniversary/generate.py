import glob
import json
from collections import Counter
from pathlib import Path
from shutil import rmtree

from grascii import DictionaryBuilder, DictionaryOutputOptions
from grascii.dictionary import Dictionary


def change_case(grascii: str, translation: str, logger):
    return grascii.upper(), translation.lower()


# prepare dictionaries that preserve boundaries ('-') in the output
builder = DictionaryBuilder(pipeline=[change_case], quiet=True)

builder.build(
    glob.glob("../../qwertigraphy/anniversary-core/dictionary_src.txt"),
    DictionaryOutputOptions("qwertigraphy-core", True),
)

builder.build(
    glob.glob("../../qwertigraphy/anniversary-supplement/dictionary_src.txt"),
    DictionaryOutputOptions("qwertigraphy-supplement", True),
)

builder.build(
    glob.glob("../../builtins/preanniversary/*.txt"),
    DictionaryOutputOptions("preanniversary-bound", True),
)

# load grascii dictionies into python dictionaries
qwertigraphy_core = {
    entry.translation: entry.grascii
    for entry in Dictionary.new("qwertigraphy-core").dump()
}

qwertigraphy_supplement = {
    entry.translation: entry.grascii
    for entry in Dictionary.new("qwertigraphy-supplement").dump()
}

preanniversary = {
    entry.translation: entry.grascii
    for entry in Dictionary.new("preanniversary-bound").dump()
}

# load anniversary reference.json from richyliu/greggdict
with Path("./reference.json").open("r") as ref:
    references = json.loads(ref.read())

# prepare output directory
output = Path("src")
if output.exists():
    rmtree(output)
output.mkdir()
current_file = output.joinpath("a.txt")

total = 0
unknown = 0

for i, page in enumerate(references):
    col1 = []
    col2 = []
    col3 = []

    counter = Counter()

    # sort words into columns based on their position in the page
    for word in page["words"]:
        if word["x"] < 500:
            col1.append(word)
        elif word["x"] < 1500:
            col2.append(word)
        else:
            col3.append(word)

        counter[word["t"][0]] += 1

    col1.sort(key=lambda w: w["y"])
    col2.sort(key=lambda w: w["y"])
    col3.sort(key=lambda w: w["y"])

    # determine what letter this page belongs to
    most_common = counter.most_common(1)[0][0]
    target_file = f"{most_common}.txt"
    if current_file.name != target_file:
        current_file = output.joinpath(target_file)

    with current_file.open("a") as f:
        for j, col in enumerate([col1, col2, col3]):
            f.write(f"# Page {i + 1} Column {j + 1}\n")
            for word in col:
                # see if the word exists in one of the starter dictionaries
                # to provide an initial grascii string
                key = word["t"].lower()
                if key in qwertigraphy_core:
                    grascii = qwertigraphy_core[key]
                elif key in qwertigraphy_supplement:
                    grascii = qwertigraphy_supplement[key]
                elif key in preanniversary:
                    grascii = preanniversary[key]
                else:
                    grascii = "!"
                    unknown += 1

                f.write(f"{grascii.lower()}\t{word['t']}\n")

                total += 1

            f.write("\n")


print(f"{total - unknown}/{total}")
print((total - unknown) / total)
