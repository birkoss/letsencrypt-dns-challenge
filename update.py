#!/usr/bin/env python

import sys
import os
import time

if len(sys.argv) < 5:
	exit(0)

if sys.argv[1] == "deploy_challenge":
	os.system("python3 ~/Code/cPanel-Update-Dns/updatedns.py --domain birkoss.com --type TXT --name _acme-challenge." + sys.argv[2] + ". --value '" + sys.argv[4] + "'")
	print("   - Waiting 2 minutes to be sure the DNS are refreshed!")
	time.sleep(120)
#elif sys.argv[1] == "clean_challenge":
#os.system("python3 ~/Code/cPanel-Update-Dns/updatedns.py --domain birkoss.com --type TXT --name _acme-challenge." + sys.argv[2] + ". --value ''")
