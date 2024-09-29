import sys
import os
import pathlib
import zipfile

dirname=input("enter directory to be backed up:")
if not os.path.isdir(dirname):
    print("directory doesn't exist")
    sys.exit(0)

curdir=pathlib.Path(dirname)

with zipfile.ZipFile("myzip.zip",mode='w') as archive:
    for filepath in curdir.rglob('*'):
        archive.write(filepath,arcname=filepath.relative_to(curdir))

if os.path.isfile("myzip"):
    print("archive created successfully")
