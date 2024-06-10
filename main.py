import loader
import validator
import writer

if __name__ == '__main__':
    for filename, content in loader.load_txt(loader.dir):
        result = validator.validate(content)
        writer.write_json(filename, result)
        break
    
