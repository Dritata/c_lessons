#Пример Break
import re
lst=""
with open(r"./src.txt", encoding="utf-8") as fin:
  text = fin.read()
  for function_match in re.finditer(r' {2}.+ :\n( {4}.+\n( {6}.+, .+\n)*)+', text):
    #print(function_match.group(1))
    result=re.finditer(r'\1\2',function_match.group(1));
    print(result)
    #print(function_match.group())
