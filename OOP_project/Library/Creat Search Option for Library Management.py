class SubstringSearch:
    def __init__(self, string_list):
        self.string_list = string_list

    def search_substring(self, substring):
        found_strings = [string for string in self.string_list if substring in string]
        return found_strings
if __name__ == "__main__":
    strings = ['Michael J. Moran',
               'Howard N. Shapiro',
               'Daisie D. Boettnerand Margaret B. Bailey',
               'Wiley',
               'Yunus A. Cengel',
               'McGraw Hill V.P. Vasandaniand D.S.Kumar',
               'Metropolitan Ronald Tocci',
               'Neal Widmerand Greg Moss',
               'Prentice Hall Pradeep K. Sinha and Priti Sinha',
               'BPB Publications Peter Norton',
               'McGraw-Hill Education Robert L. Boylestad',
               'Pearson B.L. Theraja and A.K. Theraja',
               'S Chand & Company Ltd Charles K. Alexander and Matthew N.O. Sadiku',
               'McGraw Hill Education'
               ]
    search_instance = SubstringSearch(strings)
    search_substring = input("Search text ")
    found_strings = search_instance.search_substring(search_substring)

    if found_strings:
        for string in found_strings:
            print(f"{string}")
    else:
        print(f"Result '{search_substring}' was not found.")
