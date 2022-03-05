#! /usr/bin/env python3

# rename files to have correct extention based on content


import filetype
import os
import shutil


def formatPath(path):
    return os.path.sep.join(path.split("/"))

def mkdir(path):
    try:
        os.mkdir(formatPath(path))

    except FileExistsError:
        pass
def cp(src, dst):
    src = formatPath(src)
    dst = formatPath(dst)
    try:
        shutil.copyfile(src, dst)
    except:
        print(f"Error on copying file {src} to {dst}")

def main():
    files = os.listdir("./")
    mkdir("./output")
    fail_path = "./output/fail/"
    mkdir(fail_path)
    for file in files:
        try:
            kind = filetype.guess(file)
        except IsADirectoryError:
            pass
        if kind is None:
            cp(file,f"{fail_path}/{file}")
        else:
            dst = f"./output/{kind.extension}"
            mkdir(dst)
            cp(file, f"{dst}/{file}.{kind.extension}")

if __name__ == '__main__':
    main()
