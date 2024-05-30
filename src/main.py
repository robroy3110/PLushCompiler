from optparse import OptionParser

from parser import main

parser = OptionParser()
parser.add_option("-o", "--out", dest="filename", default=False,
                  help="write output to <filename>", metavar="<filename>")
parser.add_option("-t", "--tree",
                  action="store_true", dest="tree", default=False,
                  help="shows the AST in JSON")

parser.add_option("-i", "--instant",
                  action="store_true", dest="run", default=False,
                  help="runs the result instead of saving")

(options, args) = parser.parse_args()

if not options.filename:
    if len(args) > 0:
        options.filename = args[0].replace(".pl", ".out")
    else:
        options.filename = "a.out"

if len(args) > 0:
    f = args[0]
else:
    f = False

main(options, f)