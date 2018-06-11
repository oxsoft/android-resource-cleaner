import os
import commands

PATH = 'app/src/main/res/layout/'

for fileName in os.listdir(PATH):
    name = fileName[:-4]
    binding = ''.join(map(lambda x: x[0].upper() + x[1:], name.split('_'))) + 'Binding'
    print name, binding,
    check1 = commands.getoutput('git grep -l "@layout/' + name + '" | wc -l')
    check2 = commands.getoutput('git grep -l "R.layout.' + name + '" | wc -l')
    check3 = commands.getoutput('git grep -l "' + binding + '" | wc -l')
    print check1, check2, check3
    if check1.strip() == '0' and check2.strip() == '0' and check3.strip() == '0':
        os.remove(PATH + fileName)
