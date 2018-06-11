import commands
import xml.etree.ElementTree as ET

TARGET = 'app/src/main/res/values/strings.xml'
tree = ET.parse(TARGET)
root = tree.getroot()

for child in root:
    name = child.attrib['name']
    print name,
    check1 = commands.getoutput('git grep -l "@string/' + name + '" | wc -l')
    check2 = commands.getoutput('git grep -l "R.string.' + name + '" | wc -l')
    print check1, check2
    if check1.strip() == '0' and check2.strip() == '0':
        commands.getoutput("sed -i '' -e '/" + name + "/d' " + TARGET)
