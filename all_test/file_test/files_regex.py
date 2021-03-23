import re

# # open and copy
f = open("file_test.vtt", "r")
contents = f.read()
f.close()

# remove the timestamps and replace with space
timestamp = '\\n\\n\d{1,3}\\n\d\d:\d\d.\d\d\d --> \d\d:\d\d.\d\d\d\\n'
regex_times = re.compile('%s'%timestamp)
found = regex_times.findall(contents)
newcontents = regex_times.sub(' ',contents)

# replace 4-letter words for practice
allwords = newcontents.split()

for word in range(len(allwords)):
  if len(allwords[word])==4:
    allwords[word] = allwords[word][0] + '***'

# put back together as content
cleanedtext = ' '.join(allwords)

# create and save to results.txt
f= open("results.txt","w+")
f.write(cleanedtext)
f.close()