import xml.etree.ElementTree as ET
import re

tree = ET.parse(r"test.xml")
root = tree.getroot()

pattren = r'<!\[CDATA\[(.*?)\]\]>'

sp_pattren = r'[/?=:&\.]'

all_path = []

for item in root.findall('.//item'):
    path_elem = item.find('path')
    if path_elem is not None:
        cdata_content = path_elem.text.strip() if path_elem.text else ''

        match = re.search(pattren, f'<![CDATA[{cdata_content}]]>')
        if match:
            cdata_content = match.group(1)

            split_content = re.split(sp_pattren, cdata_content)
            filter_parts = []

            for part in split_content:
                # if '?' in part or '.' in part:
                #     break
                filter_parts.append(part)

            all_path.extend(filter_parts)

unique = sorted(set(all_path),key=len)

with open('output.txt','w') as f:
    for path in unique:
        f.write(path+'\n')

print('已经处理完毕，输出到output.txt文件中')