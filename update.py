import sys
import os

if sys.argv[1] == "deploy_challenge":
	os.system("python3 ~/Code/cPanel-Update-Dns/updatedns.py --domain birkoss.com --type TXT --name _acme-challenge." + sys.argv[2] + ". --value '" + sys.argv[4] + "'")
elif sys.argv[1] == "clean_challenge":
	os.system("python3 ~/Code/cPanel-Update-Dns/updatedns.py --domain birkoss.com --type TXT --name _acme-challenge." + sys.argv[2] + ". --value ''")
