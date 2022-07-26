#!/bin/sh
cd "$(dirname "$0")"
if [ ! -d qwertigraphy-clone ]; then
  git clone https://github.com/codepoke-kk/qwertigraphy.git qwertigraphy-clone
fi

git -C qwertigraphy-clone checkout master
git -C qwertigraphy-clone pull
cp -v qwertigraphy-clone/qwertigraph/dictionaries/anniversary_core.csv anniversary-core/anniversary_core.csv
cp -v qwertigraphy-clone/qwertigraph/dictionaries/anniversary_supplement.csv anniversary-supplement/anniversary_supplement.csv
git add anniversary-core/anniversary_core.csv anniversary-supplement/anniversary_supplement.csv
echo Qwertigraphy: Update to $(git -C qwertigraphy-clone rev-parse --short HEAD) > commit-message.txt
echo To complete the update, run
echo git commit -F qwertigraphy/commit-message.txt
