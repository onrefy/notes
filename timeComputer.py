# coding=gbk
import codecs

import json

jsonFile = 'threshTime.json'
timeList = {}
with open(jsonFile, 'r') as f:
    timeList = json.loads(f.read())
output = codecs.open('timeReport.md','w','utf-8')
for key in timeList:
    time  = timeList[key]
    output.write('# ' + key + ': '+str(time) + 'h' +'\n')
    output.write('## ')
    for i in range(24):
        if (i < 7):
            output.write('s')
        else:
            if (i < 7+time):
                output.write('x')
            else:
                output.write('-')
    output.write('\n')
output.close()