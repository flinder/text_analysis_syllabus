import bibtexparser
from pprint import pprint

# +++++++++++++
# CONFIG
# +++++++++++++

BIBFILE = 'bibliography.bib'
OUTFILE = 'bibliography.md'

# Open and parse the bib file
with open(BIBFILE) as bibfile:
    bibliography = bibfile.read()

bib_database = bibtexparser.loads(bibliography)

# Sort into categories 
items = {}
for entry in bib_database.entries:
    
    try:
        cat = entry['category']
    except KeyError:
        cat = 'no_category'
    # Make category if doesn't exist
    if cat not in items.keys():
        items[cat] = []

    # Append entry in relevant category
    items[cat].append(entry)

def writeline(line):
    line = line + '\n\n'
    outfile.write(line)

# Write markdown
with open(OUTFILE, 'w+') as outfile:
    
    writeline('# Text Analysis Community Syllabus')
    writeline('This is an automatically generated document please do not edit this document. If you want to add references insert the information into `bibliography.bib`. See the `README.md` for details')
    for cat in items.keys():
        writeline('##' + cat)
        
        for entry in items[cat]:
            if entry['ENTRYTYPE'] == 'book':
                line = "{} ({}). *{}*".format(entry['author'], entry['year'],
                                            entry['title'])
            else:
                try:
                    journal = entry['journal']
                except KeyError:
                    journal = entry['booktitle']
                line = "{} ({}). *{}*. {}.".format(entry['author'], 
                                                  entry['year'],
                                                  entry['title'],
                                                  journal)
            writeline(line) 
