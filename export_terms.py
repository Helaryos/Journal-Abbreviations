#%%
def import_file(filename):
    termlist = {}
    with open(filename) as f:
        for line in f:
            entry = line.split("	")
            journal = entry.pop(0)
            if "." in entry[-1]:
                newabbr = entry[-1].replace(".", "")
                entry.append(newabbr)
            abbrs = "	".join(entry).replace("\n", "") + "\n"
            termlist[journal] = abbrs
    return termlist
def export_terms(terms, filename):
    with open(filename, "w") as f:
        for journal in terms:
            f.write(f"{journal}	{terms[journal]}")

file_endnote_chem = "Chemical.txt"
file_endnote_phys = "Physics.txt"
file_endnote_bio = "BioScience.txt"
file_ubc = "UBC Science and Engineering Journal Abbreviations.txt"
file = "merged.txt"
terms_bio = import_file(file_endnote_bio)
terms_phys = import_file(file_endnote_phys)
terms_chem = import_file(file_endnote_chem)
terms = import_file(file_ubc)
terms.update(terms_bio)
terms.update(terms_phys)
terms.update(terms_chem)
export_terms(terms, file)