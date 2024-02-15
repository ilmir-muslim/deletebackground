from rembg import remove
import os
from tqdm import tqdm

directory = '/home/ilmir/photos_for_bgdel'

for filename in tqdm(os.listdir(directory), desc='processing...'):

    name = filename.replace('.jpg','')
    input_path = os.path.join(directory, filename)
    output_path = f'/home/ilmir/Pictures/{name}.png'

    if os.path.isfile(input_path):
        with open(input_path,'rb') as i:
            with open(output_path, 'wb') as o:
                input = i.read()
                output = remove(input)
                o.write(output)