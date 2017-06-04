#!/usr/bin/python

from xml.etree import ElementTree as et

tree = et.parse('test.xml')
root = tree.getroot()

for child in root.findall('to'):
    print child.text
    child.text='thanasis'

tree.write('test2.xml')
