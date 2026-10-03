import os
import glob

files = glob.glob('src/components/content/year*/*.tsx')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    content = content.replace('import { MathEq } from "../../ui/MathEq";', 'import { MathEq } from "../LessonTemplate";')
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
print(f"Fixed {len(files)} files.")
