
anniversary-supplement-qwertigraphy: qwertigraphy/anniversary-supplement/anniversary_supplement.csv
	python qwertigraphy/convert.py qwertigraphy/anniversary-supplement/anniversary_supplement.csv qwertigraphy/anniversary-supplement/dictionary_src.txt
	grascii dictionary build qwertigraphy/anniversary-supplement/dictionary_src.txt --output anniversary-supplement-qwertigraphy
	zip anniversary-supplement-qwertigraphy.zip anniversary-supplement-qwertigraphy/*
	rm anniversary-supplement-qwertigraphy/*
	rmdir anniversary-supplement-qwertigraphy

anniversary-core-qwertigraphy: qwertigraphy/anniversary-core/anniversary_core.csv
	python qwertigraphy/convert.py qwertigraphy/anniversary-core/anniversary_core.csv qwertigraphy/anniversary-core/dictionary_src.txt
	grascii dictionary build qwertigraphy/anniversary-core/dictionary_src.txt --output anniversary-core-qwertigraphy
	zip anniversary-core-qwertigraphy.zip anniversary-core-qwertigraphy/*
	rm anniversary-core-qwertigraphy/*
	rmdir anniversary-core-qwertigraphy
