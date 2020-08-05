import xml.etree.ElementTree as ET
# Triple quote strings mean potentially multi line strings
data = '''<blah>
    <people>
        <person>
            <name>Chuck</name>
            <phone type="intl">
                +1 734 303 4456
            </phone>
            <email hide="yes"/>
        </person>
        <person>
            <name>Brent</name>
            <phone type="intl">
                +1 734 303 4456
            </phone>
            <email hide="yes"/>
        </person>
    </people>
</blah>'''

# Form a tree from the information provided in the XML
# Syntax errors can cause .formstring() to error
tree = ET.fromstring(data)
lst = tree.findall('people/person')
print(tree)