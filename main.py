from rembg import remove

input_path = '/home/ilmir/cup.jpeg'
output_path = '/home/ilmir/Pictures/cup.png'

with open(input_path,'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)