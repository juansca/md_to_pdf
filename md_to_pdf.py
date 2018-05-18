"""Markdown to PDF

Usage:
  md_to_pdf.py [-i <file> -o <file>]
  md_to_pdf.py -h | --help

Options:
  -i <file>     Input Markdown filename
  -o <file>     Output PDF filename
  -h --help     Show this screen.
"""

from markdown import markdown
import pdfkit
from docopt import docopt
import os

if __name__ == '__main__':
    opts = docopt(__doc__)
    cwd = os.getcwd()
    in_file = os.path.join(cwd, opts['-i'])

    if opts['-o'] is not None:
        out_file = os.path.join(cwd, opts['-o'])

    out_file = in_file.split('.')[0] + '.pdf'

    with open(in_file, 'r') as f:
        html_text = markdown(f.read(), output_format='html4')

    pdfkit.from_string(html_text, out_file)
