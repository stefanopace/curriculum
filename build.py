from os import listdir
from os.path import isfile, join

def indentation_level(line):
    level = 0
    for split in line.split('    '):
        if split == '':
            level += 1
        else:
            break
    return level


content_path = 'src/content/'
content_filenames = [f for f in listdir(content_path) if isfile(join(content_path, f))]

with open('src/assets/template.html') as file:
    template = ''.join(file.readlines())

for content_filename in content_filenames:
    with open(content_path + content_filename) as content_file:
        content = content_file.readlines()
    
    html=['<div>']
    previous_indentation_level = 0
    for line in content:
        current_indentation_level = indentation_level(line)
        if (current_indentation_level > previous_indentation_level):
            for i in range(current_indentation_level - previous_indentation_level):
                html.append('<div>')
        
        if (current_indentation_level < previous_indentation_level):
            for i in range(previous_indentation_level - current_indentation_level):
                html.append('</div>')

        if (current_indentation_level == 0):
            html.append('<b class="fucsia">'+line+'</b><br>')
        else:
            html.append(line+'<br>')
        previous_indentation_level = current_indentation_level

    for i in range(previous_indentation_level):
        html.append('</div>')
    html.append('</div><br>')
    template = template.replace('%'+content_filename+'%', ''.join(html))

index = template

with open('build/curriculum/index.html', 'w') as builded:
    builded.write(index)

print('index.html builded')