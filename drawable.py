import os
import commands

ROOT = 'app/src/main/res/'

def files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            yield os.path.join(root, file)

for path in files(ROOT):
    if not path.startswith(ROOT + 'drawable'):
        continue
    if path[-4:] not in ('.png', '.xml'): continue
    name = path.split('/')[-1][:-4]
    if name[-2:] == '.9':
        name = name[:-2]
    print name,
    check1 = commands.getoutput('git grep -l "@drawable/' + name + '" | wc -l')
    check2 = commands.getoutput('git grep -l "R.drawable.' + name + '" | wc -l')
    print check1, check2
    if check1.strip() == '0' and check2.strip() == '0':
        os.remove(path)
