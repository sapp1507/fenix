import re
from docx import Document
from utils import day_text

document = Document('1.docx')

multi_space_pattern = re.compile(r'\s{2,}')

menu = []
i = 0
for table in document.tables:
    for row in table.rows:
        name, weight, price = [multi_space_pattern.sub(
            ' ', i.text.strip()) for i in row.cells]

        if name == weight == price or (not weight or not price) or str(name).capitalize() in day_text:
            print()
            name = name.title()
            print(name)
            # if str(name).capitalize() in day_text:
            menu.append({'day': name})
            menu[i]['dish'] = []
            i += 1
            continue
        menu[i-1]['dish'].append({
            'name': name, 'weight': weight, 'price': price
        })


        # if str(name).capitalize() in day_text:
        #     menu.append({'id': i, 'day': name})
        #     i += 1
        #     continue


        print(f'{name} {weight} {price}')
    print(menu)
    break
