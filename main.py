from rembg import remove
import os
from tqdm import tqdm

directory = input('введите путь к папке в которой фотографии: ')
output_directory = input('введите путь к папке в которую хотите сохранить измененные фотографии: ')
for filename in tqdm(os.listdir(directory), desc='processing...'):

    name = filename.replace('.jpg','.png')
    input_path = os.path.join(directory, filename)
    output_path = f'{output_directory}/{name}.png'

    if os.path.isfile(input_path):
        with open(input_path,'rb') as i:
            with open(output_path, 'wb') as o:
                input = i.read()
                output = remove(input)
                o.write(output)