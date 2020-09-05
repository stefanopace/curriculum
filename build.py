with open('src/assets/template.html') as file:
    template = ''.join(line.strip() for line in file.readlines())

index = template

with open('build/curriculum/index.html', 'w') as builded:
    builded.write(index)

print('index.html builded')