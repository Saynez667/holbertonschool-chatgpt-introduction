#!/usr/bin/python3
import sys

# Affiche tous les arguments passés en ligne de commande, sauf le nom du script
for i in range(1, len(sys.argv)):
	print(sys.argv[i])
