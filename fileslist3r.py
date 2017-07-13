#-------------------------------------------------------------------------------
# Name:        fileslist3r - Anti Ransomware Tip
# Purpose:
#
# Author:      R00T
#
# Created:     04/05/2017
# Copyright:   (c) R00T 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os, sys

dirList = os.path.dirname(os.path.realpath(__file__))# current directory
for root, dirs, files in os.walk(dirList):
    for name in files:
        if name.endswith((".txt", ".log", ".lst", ".doc", ".pdf", ".sh")):
            newname = os.path.splitext(os.path.basename(os.path.join(root, name)))[0]
	    os.rename(os.path.join(root, name), os.path.join(root, newname) )
