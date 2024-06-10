import datetime
import os

outdir = './round1_json' + '_' + datetime.datetime.now().strftime('%Y%m%d%H%M%S')
outfile = '使一颗心免于哀伤_金融规则长文本_result.json'

# 确保输出目录存在
os.makedirs(outdir, exist_ok=True)
def write_json(filename, result):
    with open(outdir + '/' + outfile, 'a', encoding='utf-8') as f:
        json = {'id': filename, 'sents': [result]}
        f.write(str(json))
        f.write('\n')