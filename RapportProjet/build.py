import os
print("")
print("      Building report")
print("")
os.system("pdflatex rapport.tex")
os.system("makeindex rapport.tex")
os.system("pdflatex rapport.tex")
os.system("pdflatex rapport.tex")

print("")
print("      Clean directory")
print("")
files = ["rapport.aux", "rapport.log", "rapport.out", "rapport.glo", "rapport.ilg", "rapport.ind", "rapport.ist", "rapport.toc", "rapport.lof", "rapport.lot", "rapport.synctex.gz"]
for file in files:
	if os.path.isfile(file):
		os.remove(file)