import xml.etree.ElementTree as ET

with open("currency.xml", "rb") as f: # Читаем как бинарный файл и обрабатываем
    content = f.read()

xml_start = content.find(b'<?xml') # Удаляем все до <?xml
if xml_start > 0:
    content = content[xml_start:]

xml_text = content.decode('windows-1251') # Декодируем как windows-1251
root = ET.fromstring(xml_text) # Парсим

all_values = []
for valute in root.findall('Valute'):
    value = valute.find('Value').text.replace(',', '.')
    all_values.append(float(value))

print(f'Средний показатель Value: {sum(all_values) / len(all_values)}')
    


