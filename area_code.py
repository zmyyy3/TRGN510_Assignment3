#!/usr/bin/python

import sys
import re
import fileinput

phone_number_file = sys.argv[1]
for each_line in fileinput.input(phone_number_file):
    area_code = re.findall(r'^(\d{3})', each_line)
    print(area_code)
