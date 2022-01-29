#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re
for param in sys.argv :
	#receber txt com ambas
	#txt a, txt b
	#string a, string b
	if re.search(r"(.txt$|.py$)", param, re.IGNORECASE):
		print("A string tem txt")
	else:
		print("A string não tem o nome Enzo")
	print(param)