import os

def calFileUnits(file):
    thoughtUnits = '#*123456789'
    num = 0

    f = open(file, 'r')
    contents = f.readlines()

    for line in contents:
        line.lstrip()
        if (thoughtUnits.find(line[0]) > 0):
            num += 1
    f.close()
    return num
def calFileUnitsPerSize(file):
    units = calFileUnits(file)
    size = os.path.getsize(file)
    return units / size

def getAllMdFile(path):
    files = []
    for parent, dirnames, filenames in os.walk(path):
        for file in filenames:
            file = parent +'/'+ file
            files.append(file)
    markdownFiles = []
    for file in files:
        if (file[-3:] == '.md'):
            markdownFiles.append(file)
    return markdownFiles

markdownFiles = getAllMdFile('.')
markdownFilesUnitsNums = []


for file in markdownFiles:
    fileUnitNum = calFileUnits(file)
    fileUnitPerSize = calFileUnitsPerSize(file)

    f = open(file, 'r+')
    contents = f.readlines()
    contents[-1:] = '# 文件思想数目为{}个 文件单位思想为{}'.format(fileUnitNum-1, fileUnitPerSize * 100) 
    content = ''
    for line in contents:
        content += line
    f.close()

    f = open(file, 'w')
    f.write(content)
    f.close()
    markdownFilesUnitsNums.append(fileUnitNum)