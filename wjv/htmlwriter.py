#!/usr/bin/env python3

import math
import itertools

HEADER = """<html><head>
<link rel="stylesheet" href="bracket.css">
</head>
<body>
<h1>WJV Tournament</h1>
<main id="tournament">"""

FOOTER = """</main>
</body></html>
"""

def create_matches(athletes):
    matches = []
    it = iter(athletes)
    for _ in range(len(athletes)//2):
        matches.append( (next(it), next(it)) )
    return matches

def create_html_from_list(athletes):

    page = ""
    page += HEADER

    num_rounds = math.ceil(math.log(len(athletes), 2))+1
    num_matches = len(athletes)//2

    rnd = 1
    page += '\n  <ul class="round round-{}">'.format(rnd)

    for match in create_matches(athletes):
        page += '\n    <li class="spacer">&nbsp;</li>'
        page += '\n    <li class="game game-top">{}</li>'.format(match[0].name())
        page += '\n    <li class="game game-spacer">&nbsp;</li>'
        page += '\n    <li class="game game-bottom">{}</li>'.format(match[1].name())

    page += '\n    <li class="spacer">&nbsp;</li>'
    page += '\n  </ul>'

    for rnd in [2,3,4]:
        num_matches = num_matches//2
        page += '\n  <ul class="round round-{}">'.format(rnd)
        for _ in range(num_matches):
            page += '\n    <li class="spacer">&nbsp;</li>'
            page += '\n    <li class="game game-top">&nbsp;</li>'
            page += '\n    <li class="game game-spacer">&nbsp;</li>'
            page += '\n    <li class="game game-bottom">&nbsp;</li>'
        page += '\n    <li class="spacer">&nbsp;</li>'
        page += '\n  </ul>'



    page += FOOTER
    with open("bracket.html", "w+") as htmlfile:
        htmlfile.write(page)
