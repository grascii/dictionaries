# Grascii Dictionaries

## About

This repository is a collection of Grascii dictionaries for use with
the [Grascii](https://github.com/grascii/grascii) Python Package. It contains
the dictionary source files for Grascii's built-in dictionaries as well as other
optional community-sourced dictionaries.

## Installing and Using a Dictionary

1. Go to the [releases page](https://github.com/grascii/dictionaries/releases)
    and download the zip of the dictionary you would like to install. See [Available Dictionaries](#available-dictionaries) for
    a description of the available dictionaries.

2. Unzip the downloaded file.

    At this point, the dictionary is usable:

    For example, if you chose the anniversary-core-qwertigraphy dictionary,
    you could search the dictionary with:

    `$ grascii search --dictionary ./anniversary-core-qwertigraphy --interactive`

    If you would like to install the dictionary for easier use, continue with step
    3.

3. Install the dictionary supplying an optional custom name.

    `$ grascii dictionary install --name anniversary-core ./anniversary-core-qwertigraphy`

4. Verify the installation.

    ```
    $ grascii dictionary list
    Built-in Dictionaries:
    preanniversary

    Installed Dictionaries:
    anniversary-core
    ```

    Now you can use the dictionary like so:

    `$ grascii search --dictionary :anniversary-core --interactive`

## Available Dictionaries

### Built-ins

These dictionaries are included in releases of the Grascii Python package. Fixes
and changes to these dictionaries are applied here and then pulled into the
[grascii](https://github.com/grascii/grascii) repository for releases. Most
built-in dictionaries are based on the official Gregg Shorthand dictionaries
published by the Gregg Publishing Company.

#### `preanniversary`

This is the Grascii Dictionary based on the 1916 Gregg Shorthand Dictionary.
Use this dictionary if you would like to have the latest updates in between
releases of Grascii or have the updates even when using an older version of
Grascii.

#### `preanniversary-phrases`

This dictionary is based on the 1924 *Gregg Shorthand Phrase Book* and contains
over 3000 phrases according to the pre-anniversary version of the Gregg
Shorthand system. Use this dictionary if you would like to have the latest updates
in between releases of Grascii or are using a Grascii version older than 0.7.0.

### Additional Dictionaries

These dictionaries are not shipped with Grascii and are available as optional
resources. Note that they are not necessarily based on official Gregg Shorthand
dictionaries and do not necessarily follow the same standards or internal
consistency as built-ins. However, they are invaluable resources that fill in
the holes left by the built-ins.

#### Qwertigraphy Dictionaries

These dictionaries are pulled from [qwertigraphy](https://github.com/codepoke-kk/qwertigraphy)
and converted into Grascii's format. They are based on the anniversary version
of Gregg Shorthand. They are periodically updated with the latest changes from
the qwertigraphy repository.

##### `anniversary-core-qwertigraphy`

This dictionary contains over 8000 common words and phrases, many of which are
based on the Gregg Shorthand Anniversary Dictionary. A small number of entries
in the dictionary may be based on other versions of Gregg Shorthand.

##### `anniversary-supplement-qwertigraphy`

This dictionary contains over 900 more anniversary words and phrases. It includes
more forms of various words.

## Building Dictionaries from Source

### Prerequisites

- Python 3.6+
- Make (optional)

### Install Build Tools

`pip install -r requirements.txt`

### Build the Dictionaries

To make all the dictionaries:

`$ make`

If you would only like to build some of the dictionaries, list the dictionaries
you want to build. For example, to only build the preanniversary dictionary:

`$ make preanniversary.zip`

If you do not have `make`, you can build the dictionaries by executing the
commands found in the `Makefile` for the different dictionaries. Most often,
it is simply a matter of running `grascii dictionary build ...`.

## Dictionary Errors

If you come across any typos or incorrect entries in any of the dictionaries,
please open an issue or pull request pointing out the problematic entries.

## Contributing

Contributions of any kind are welcome and appreciated. You can contribute by:

- Creating issues for incorrect dictionary entries
- Correcting dictionary entries
- Helping write new dictionaries or expand existing ones
- Sharing reverse Gregg Shorthand dictionaries in any format
- Fixing and improving build scripts
- Editing documentation for correctness, completeness, and clarity

## Acknowledgements

A huge thank you to the author of
[qwertigraphy](https://github.com/codepoke-kk/qwertigraphy) for allowing the
use of its dictionaries!
