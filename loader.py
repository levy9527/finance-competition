dir = "./round1_txt"

def load_txt(dir):
    import os
    for root, dirs, files in os.walk(dir):
        for file in files:
            try:
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    yield file.split('.')[0], f.read()
            except Exception as e:
                print(f"读取文件 {file} 时发生错误: {e}")

if __name__ == '__main__':
    for content in load_txt(dir):
        print(content)
        break
    
    