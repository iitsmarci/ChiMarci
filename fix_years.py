import os
import glob
import re

for year in range(1, 6):
    files = glob.glob(f'src/components/content/year{year}/*.tsx')
    for f in files:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # We need to insert `year={N}` right after `<LessonTemplate`
        # Using regex to find the `<LessonTemplate` tag and replace it
        
        content = re.sub(r'<LessonTemplate(\s+)', f'<LessonTemplate\\1year={{{year}}}\\1', content, count=1)
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
print("Added year prop to all files.")
