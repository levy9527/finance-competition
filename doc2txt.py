import logging
import os
import subprocess
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def doc2txt(file_path, outdir):
    '''
    convert doc[x] to txt
    
    前提：
    1.安装软件　https://www.libreoffice.org/download/download-libreoffice/

    2.找到命令行执行路径:
    find /usr/local/bin -name soffice
    # 或者
    find /Applications -name soffice

    3.建立软链接：
    sudo ln -s /Applications/LibreOffice.app/Contents/MacOS/soffice /usr/local/bin/soffice
    '''
    absolute_file_path = os.path.abspath(file_path)
    logging.info(f'converting {absolute_file_path} to txt')
    
    subprocess.check_output(f'soffice --headless --convert-to txt "{absolute_file_path}" --outdir {outdir}', shell=True)

if __name__ == '__main__':
    input_dir = 'round1_test_data'
    outdir = 'round1_txt'
    # file_path = f'{input_dir}/中华人民共和国企业破产法.doc'
    # doc2txt(file_path, outdir)
    import docx2txt
    
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.doc'):
                doc2txt(os.path.join(root, file), outdir)
            elif file.endswith('.docx'):
                with open(os.path.join(outdir, file.replace('.docx', '.txt')), 'w', encoding='utf-8') as f:
                    f.write(
                        docx2txt.process(os.path.join(root, file))
                    )
            else:
                logging.warning(f'unknown file: {file}')
    logging.info('doc[x]2txt all done!')
