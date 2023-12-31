# xclean

File de-duplication utility

## Installation

### Using pypi

    pip install xclean

### Using github

    pip install https://github.com/bbc6502/xclean/archive/refs/heads/main.zip

## Usage

    usage: xclean [-h] [-m MAIN] [-t TARGET] [-a ARCHIVE_TO] [-e [EXTENSIONS ...]] [--remove] [--trash] [--clean]

    options:
      -h, --help            show this help message and exit
      -m MAIN, --main MAIN
                            Directory where master files reside
      -t TARGET, --target TARGET
                            Directory where duplicate files may reside
      -a ARCHIVE_TO, --archive-to ARCHIVE_TO
                            Archive duplicates to folder
      -e [EXTENSIONS ...], --extensions [EXTENSIONS ...]
                            Extensions
      --remove              Remove duplicate files
      --trash               Trash duplicate files
      --clean               Clean database
      --xmp                 Include XMP files as well
