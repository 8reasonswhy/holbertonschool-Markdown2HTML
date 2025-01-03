#!/usr/bin/python3

"""
Ce module prend en argument un fichier Markdown et génère un fichier HTML.
Il vérifie que le nombre d'arguments est correct et que le fichier Markdown existe.
"""
import sys
import os
def main():

    if len(sys.argv) > 2 :
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    markdown = sys.argv[1]
    output = sys.argv[2]
    if not os.path.exists(markdown):
        print("Missing markdown_file", file = sys.stderr)
        sys.exit(1)
    sys.exist(0)
if __name__ == "__main__":
    main()
