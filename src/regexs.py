#!/usr/bin/env python3
import re

regex0 = re.compile(r'\{+.+?\}+', re.MULTILINE | re.UNICODE)
regex1 = lambda x : \
re.compile(r'(?<!\'|\")'+x+'(?!\'|\")(?# regex for a character defined from the lambda not in quotes)'\
, re.MULTILINE | re.UNICODE)