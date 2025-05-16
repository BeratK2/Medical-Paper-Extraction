import os 
import fitz 
import json 

directory = './papers'
text = ''
output = 'proton_papers.jsonl'

for file in os.listdir(directory):
    print(file)
    path = './papers/' + file 
    doc = fitz.open(path)
    for page in doc:
        text += page.get_text()
    data = {"doi": os.path.splitext(file)[0], "paper": text}
    
    with open(output, 'a', encoding='utf-8') as f:
        f.write(json.dumps(data) + '\n')
    doc.close()