from rembg import remove

file_name = input()
input_path = f'/home/ilmir/{file_name}'
output_path = '/home/ilmir/Pictures/cup.png'

with open(input_path,'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)