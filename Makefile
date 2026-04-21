
all: anniversary-core-qwertigraphy.zip anniversary-supplement-qwertigraphy.zip preanniversary.zip preanniversary-phrases.zip anniversary.zip

clean:
	rm -f anniversary-core-qwertigraphy.zip anniversary-supplement-qwertigraphy.zip preanniversary.zip preanniversary-phrases.zip anniversary.zip

.PHONY: all clean

anniversary-supplement-qwertigraphy.zip: qwertigraphy/convert.py qwertigraphy/anniversary-supplement/anniversary_uniform_supplement.csv
	python qwertigraphy/convert.py qwertigraphy/anniversary-supplement/anniversary_uniform_supplement.csv qwertigraphy/anniversary-supplement/dictionary_src.txt
	grascii dictionary build qwertigraphy/anniversary-supplement/dictionary_src.txt --output anniversary-supplement-qwertigraphy
	zip -rmT anniversary-supplement-qwertigraphy.zip anniversary-supplement-qwertigraphy

anniversary-core-qwertigraphy.zip: qwertigraphy/convert.py qwertigraphy/anniversary-core/anniversary_uniform_core.csv
	python qwertigraphy/convert.py qwertigraphy/anniversary-core/anniversary_uniform_core.csv qwertigraphy/anniversary-core/dictionary_src.txt
	grascii dictionary build qwertigraphy/anniversary-core/dictionary_src.txt --output anniversary-core-qwertigraphy
	zip -rmT anniversary-core-qwertigraphy.zip anniversary-core-qwertigraphy

preanniversary.zip: builtins/preanniversary/*.txt
	grascii dictionary build builtins/preanniversary/*.txt --output preanniversary
	zip -rmT preanniversary.zip preanniversary

preanniversary-phrases.zip: builtins/preanniversary-phrases/*.txt
	grascii dictionary build builtins/preanniversary-phrases/*.txt --output preanniversary-phrases
	zip -rmT preanniversary-phrases.zip preanniversary-phrases

anniversary.zip: builtins/anniversary/*.txt
	grascii dictionary build builtins/anniversary/*.txt --output anniversary
	zip -rmT anniversary.zip anniversary
