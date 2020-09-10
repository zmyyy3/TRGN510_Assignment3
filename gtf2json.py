#!/usr/bin/python

import json

with open('Homo_sapiens.GRCh37.75.gtf') as f:
    data = f.readlines()
    
gene_file = []
for i in data[5:]:
    tmp = i.split('\t')
    if tmp[2] == 'gene':
        dic = {}
        dic['geneName'] = tmp[-1].split('";')[1].split(' "')[-1]
        dic['chr'] = tmp[0]
        dic['startPos'] = tmp[3]
        dic['endPos'] = tmp[4]
        gene_file.append(dic)  

with open("record.json","w") as f:
    json.dump(gene_file,f)
