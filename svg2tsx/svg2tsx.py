#! /usr/bin/env python3
# converts an svg into a react component

import sys
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader
from pathlib import Path


def parse_svg(file_name):
    data = None
    with open(file_name, 'r') as svgFile:
        data = BeautifulSoup(svgFile, "xml")
    return data.find_all("path")


def transform(pathsData, componentName):
    j2_env = Environment(loader=FileSystemLoader("./icon_template.tsx"),
                         trim_blocks=True)

    with open('./icon_template.j2', 'r') as svgFile:
        templateText = "".join(svgFile.readlines())
    return Environment().from_string(templateText).render(pathDataSet=pathsData,componentName=componentName)


if __name__ == "__main__":
    if(len(sys.argv) != 3):
        print(f"error with args: {' '.join(sys.argv)}")
        print("should be ./transform2TSX.py [input file path] [output directory]")
        exit(1)
    inFilePath = sys.argv[1]
    inFileName = Path(inFilePath).name
    componentName = ".".join(inFileName.split('.')[0:-1])
    upperCaseName = list(componentName)
    upperCaseName[0] = upperCaseName[0].upper()

    for i in range(len(upperCaseName)-1,-1,-1):
        if upperCaseName[i] == '-':
            upperCaseName.pop(i)
            upperCaseName[i]=upperCaseName[i].upper()
    componentName = upperCaseName
    upperCaseName = "".join(upperCaseName)


    outFilePath = sys.argv[2]
    path_data = [elem["d"] for elem in parse_svg(inFilePath)]
    outData = transform(path_data,upperCaseName)
    
    componentName[0] = componentName[0].lower()
    componentName = "".join(componentName)
    print(f"{outFilePath}/{componentName}.tsx")
    with open(f"{outFilePath}/{componentName}.tsx", "w") as out_file_fd:
        out_file_fd.write(outData)