#!/usr/bin/env bash

cd ../../../

PYTHONPATH=. python tools/data/build_file_list.py excavator data/excavator/videos/ --level 2 --format videos --shuffle
echo "Filelist for videos generated."

cd tools/data/excavator/
