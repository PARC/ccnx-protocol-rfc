import sys
from bs4 import BeautifulSoup
import re

def append_document(document, fname, config):
    with open(fname, "r") as fh:
        html = fh.read()
        soup = BeautifulSoup(html, 'html.parser')

        toc = ""
        for div in soup.findAll('p', 'toc'): # there will only be one of these
            toc = div
            header = div.previous_sibling
            anchor = header.previous_sibling
            abreak = anchor.previous_sibling

            abreak.extract()
            anchor.extract()
            header.extract()
            div.extract()

        document = document.replace('pdf-' + config["nick"], config["pdf"])
        document = document.replace('txt-' + config["nick"], config["txt"])
        document = document.replace('github-' + config["nick"], config["github"])
        document = document.replace('<!-- toc-' + config["nick"] + ' -->', str(toc))
        document = document.replace('<!-- content-' + config["nick"] + ' -->', str(soup.body))

    return document


# Static source configuration
messages_config = {
    "nick" : "messages",
    "github" : "https://github.com/parc/ccnx-messages",
    "pdf": "https://github.com/PARC/ccnx-messages/blob/master/draft-irtf-icnrg-ccnxmessages-01.pdf",
    "txt" : "https://github.com/PARC/ccnx-messages/blob/master/draft-irtf-icnrg-ccnxmessages-01.txt"
}
semantics_config = {
    "nick" : "semantics",
    "github" : "https://github.com/parc/ccnx-semantics",
    "pdf": "https://github.com/PARC/ccnx-semantics/blob/master/draft-irtf-icnrg-ccnxsemantics-01.pdf",
    "txt" : "https://github.com/PARC/ccnx-semantics/blob/master/draft-irtf-icnrg-ccnxsemantics-01.txt"
}

# Input and output parameters
template_fname = "index.html.bare"
output_fname = "test.html"

with open(template_fname, "r") as fh:
    # Read in the template
    template = fh.read()

    # Append the generated files to the template
    template = append_document(template, "/Users/cwood/PARC/ccnx-messages/draft-irtf-icnrg-ccnxmessages-01.html", messages_config)
    template = append_document(template, "/Users/cwood/PARC/ccnx-semantics/draft-irtf-icnrg-ccnxsemantics-01.html", semantics_config)

    # Write out the template
    with open(output_fname, "w") as wh:
        wh.write(template)
