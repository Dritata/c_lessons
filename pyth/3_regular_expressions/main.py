#Пример Break
import re
lst=""

with open(r"./src.txt", encoding="utf-8") as fin:
  text = fin.read()
  pattern=re.compile(r'(\d+)-(\w+)')
  #pattern=re.compile(r'(d)+')
  match_is=re.search(r'(\w)+.(\d)+','AV.12')
  #match_is = pattern.search(r'\2.\1','AVE.123')
  #match_is = pattern.sub(r'\2-\2','AVE1-f123')
  print(match_is)
  #print(re.split(r' {2}.+ :\n( {4}.+\n( {6}.+, .+\n)*){3}', text))
  for function_match in re.finditer(r' {2}.+ :\n( {4}.+\n( {6}.+, .+\n)*){3}', text):
    print(function_match.group())
    re.findall(r
    #result=re.findall(r'( {4}.+\n( {6}.+, .+\n)*)',function_match.group());
    #print(function_match.group(2))
    #for i in result:
      
    #print(function_match.group(1))
    #print(function_match.group())

