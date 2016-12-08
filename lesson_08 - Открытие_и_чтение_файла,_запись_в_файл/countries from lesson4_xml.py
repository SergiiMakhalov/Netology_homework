import xml.etree.ElementTree as ET
from pprint import pprint
tree = ET.parse('countries_SM.xml')

for e in tree.iter():
	pprint(e)