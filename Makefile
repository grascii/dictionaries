
anniversary-supplement-qwertigraphy: qwertigraphy/anniversary-supplement/anniversary_supplement.csv
	python qwertigraphy/convert.py qwertigraphy/anniversary-supplement/anniversary_supplement.csv qwertigraphy/anniversary-supplement/dictionary_src.txt
	grascii dictionary build qwertigraphy/anniversary-supplement/dictionary_src.txt --output anniversary-supplement-qwertigraphy
	zip anniversary-supplement-qwertigraphy.zip anniversary-supplement-qwertigraphy/*
	rm anniversary-supplement-qwertigraphy/*
	rmdir anniversary-supplement-qwertigraphy
