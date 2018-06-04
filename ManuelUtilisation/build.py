import os
print("")
print("      Building report")
print("")
os.system("pdflatex manuel.tex")
os.system("makeindex manuel.tex")
os.system("pdflatex manuel.tex")
os.system("pdflatex manuel.tex")

print("")
print("      Clean directory")
print("")
files = ["manuel.aux", "manuel.log", "manuel.out", "manuel.glo", "manuel.ilg", "manuel.ind", "manuel.ist", "manuel.toc", "manuel.lof", "manuel.lot", "manuel.synctex.gz"]
for file in files:
	if os.path.isfile(file):
		os.remove(file)