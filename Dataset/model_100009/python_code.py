from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class bibtex_Edition:

    def __init__(self, edition: str, bibtex_Edition: "bibtex_Book" = None, bibtex_Edition134: "bibtex_Manual" = None, bibtex_Edition80: "bibtex_Inbook" = None):
        self.edition = edition
        self.bibtex_Edition = bibtex_Edition
        self.bibtex_Edition134 = bibtex_Edition134
        self.bibtex_Edition80 = bibtex_Edition80
        
        pass
    @property
    def edition(self):
        return self.__edition

    @edition.setter
    def edition(self, edition: str):
        self.__edition = edition


    @property
    def bibtex_Edition134(self):
        return self.__bibtex_Edition134

    @bibtex_Edition134.setter
    def bibtex_Edition134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Edition__bibtex_Edition134", None)
        self.__bibtex_Edition134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Manual133"):
                opp_val = getattr(old_value, "bibtex_Manual133", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Manual133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Manual133"):
                opp_val = getattr(value, "bibtex_Manual133", None)
                setattr(value, "bibtex_Manual133", self)

    @property
    def bibtex_Edition80(self):
        return self.__bibtex_Edition80

    @bibtex_Edition80.setter
    def bibtex_Edition80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Edition__bibtex_Edition80", None)
        self.__bibtex_Edition80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Inbook79"):
                opp_val = getattr(old_value, "bibtex_Inbook79", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Inbook79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Inbook79"):
                opp_val = getattr(value, "bibtex_Inbook79", None)
                setattr(value, "bibtex_Inbook79", self)

    @property
    def bibtex_Edition(self):
        return self.__bibtex_Edition

    @bibtex_Edition.setter
    def bibtex_Edition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Edition__bibtex_Edition", None)
        self.__bibtex_Edition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Book36"):
                opp_val = getattr(old_value, "bibtex_Book36", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Book36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Book36"):
                opp_val = getattr(value, "bibtex_Book36", None)
                setattr(value, "bibtex_Book36", self)

class bibtex_Editor:

    def __init__(self, editor: str, bibtex_Editor: "bibtex_Book" = None, bibtex_Editor50: "bibtex_Conference" = None, bibtex_Editor156: "bibtex_Proceedings" = None, bibtex_Editor88: "bibtex_Incollection" = None, bibtex_Editor108: "bibtex_Inproceedings" = None):
        self.editor = editor
        self.bibtex_Editor = bibtex_Editor
        self.bibtex_Editor50 = bibtex_Editor50
        self.bibtex_Editor156 = bibtex_Editor156
        self.bibtex_Editor88 = bibtex_Editor88
        self.bibtex_Editor108 = bibtex_Editor108
        
        pass
    @property
    def editor(self):
        return self.__editor

    @editor.setter
    def editor(self, editor: str):
        self.__editor = editor


    @property
    def bibtex_Editor50(self):
        return self.__bibtex_Editor50

    @bibtex_Editor50.setter
    def bibtex_Editor50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Editor__bibtex_Editor50", None)
        self.__bibtex_Editor50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Conference49"):
                opp_val = getattr(old_value, "bibtex_Conference49", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Conference49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Conference49"):
                opp_val = getattr(value, "bibtex_Conference49", None)
                setattr(value, "bibtex_Conference49", self)

    @property
    def bibtex_Editor156(self):
        return self.__bibtex_Editor156

    @bibtex_Editor156.setter
    def bibtex_Editor156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Editor__bibtex_Editor156", None)
        self.__bibtex_Editor156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Proceedings"):
                opp_val = getattr(old_value, "bibtex_Proceedings", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Proceedings", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Proceedings"):
                opp_val = getattr(value, "bibtex_Proceedings", None)
                setattr(value, "bibtex_Proceedings", self)

    @property
    def bibtex_Editor108(self):
        return self.__bibtex_Editor108

    @bibtex_Editor108.setter
    def bibtex_Editor108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Editor__bibtex_Editor108", None)
        self.__bibtex_Editor108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Inproceedings107"):
                opp_val = getattr(old_value, "bibtex_Inproceedings107", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Inproceedings107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Inproceedings107"):
                opp_val = getattr(value, "bibtex_Inproceedings107", None)
                setattr(value, "bibtex_Inproceedings107", self)

    @property
    def bibtex_Editor88(self):
        return self.__bibtex_Editor88

    @bibtex_Editor88.setter
    def bibtex_Editor88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Editor__bibtex_Editor88", None)
        self.__bibtex_Editor88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Incollection87"):
                opp_val = getattr(old_value, "bibtex_Incollection87", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Incollection87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Incollection87"):
                opp_val = getattr(value, "bibtex_Incollection87", None)
                setattr(value, "bibtex_Incollection87", self)

    @property
    def bibtex_Editor(self):
        return self.__bibtex_Editor

    @bibtex_Editor.setter
    def bibtex_Editor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Editor__bibtex_Editor", None)
        self.__bibtex_Editor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Book27"):
                opp_val = getattr(old_value, "bibtex_Book27", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Book27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Book27"):
                opp_val = getattr(value, "bibtex_Book27", None)
                setattr(value, "bibtex_Book27", self)

class bibtex_Address:

    def __init__(self, address: str, bibtex_Address: "bibtex_Book" = None, bibtex_Address43: "bibtex_Booklet" = None, bibtex_Address61: "bibtex_Conference" = None, bibtex_Address123: "bibtex_Inproceedings" = None, bibtex_Address131: "bibtex_Manual" = None, bibtex_Address141: "bibtex_Mastersthesis" = None, bibtex_Address154: "bibtex_Phdthesis" = None, bibtex_Address165: "bibtex_Proceedings" = None, bibtex_Address177: "bibtex_Techreport" = None, bibtex_Address77: "bibtex_Inbook" = None, bibtex_Address100: "bibtex_Incollection" = None):
        self.address = address
        self.bibtex_Address = bibtex_Address
        self.bibtex_Address43 = bibtex_Address43
        self.bibtex_Address61 = bibtex_Address61
        self.bibtex_Address123 = bibtex_Address123
        self.bibtex_Address131 = bibtex_Address131
        self.bibtex_Address141 = bibtex_Address141
        self.bibtex_Address154 = bibtex_Address154
        self.bibtex_Address165 = bibtex_Address165
        self.bibtex_Address177 = bibtex_Address177
        self.bibtex_Address77 = bibtex_Address77
        self.bibtex_Address100 = bibtex_Address100
        
        pass
    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address


    @property
    def bibtex_Address131(self):
        return self.__bibtex_Address131

    @bibtex_Address131.setter
    def bibtex_Address131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Address__bibtex_Address131", None)
        self.__bibtex_Address131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Manual130"):
                opp_val = getattr(old_value, "bibtex_Manual130", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Manual130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Manual130"):
                opp_val = getattr(value, "bibtex_Manual130", None)
                setattr(value, "bibtex_Manual130", self)

    @property
    def bibtex_Address43(self):
        return self.__bibtex_Address43

    @bibtex_Address43.setter
    def bibtex_Address43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Address__bibtex_Address43", None)
        self.__bibtex_Address43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Booklet42"):
                opp_val = getattr(old_value, "bibtex_Booklet42", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Booklet42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Booklet42"):
                opp_val = getattr(value, "bibtex_Booklet42", None)
                setattr(value, "bibtex_Booklet42", self)

    @property
    def bibtex_Address141(self):
        return self.__bibtex_Address141

    @bibtex_Address141.setter
    def bibtex_Address141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Address__bibtex_Address141", None)
        self.__bibtex_Address141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Mastersthesis140"):
                opp_val = getattr(old_value, "bibtex_Mastersthesis140", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Mastersthesis140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Mastersthesis140"):
                opp_val = getattr(value, "bibtex_Mastersthesis140", None)
                setattr(value, "bibtex_Mastersthesis140", self)

    @property
    def bibtex_Address123(self):
        return self.__bibtex_Address123

    @bibtex_Address123.setter
    def bibtex_Address123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Address__bibtex_Address123", None)
        self.__bibtex_Address123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Inproceedings122"):
                opp_val = getattr(old_value, "bibtex_Inproceedings122", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Inproceedings122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Inproceedings122"):
                opp_val = getattr(value, "bibtex_Inproceedings122", None)
                setattr(value, "bibtex_Inproceedings122", self)

    @property
    def bibtex_Address77(self):
        return self.__bibtex_Address77

    @bibtex_Address77.setter
    def bibtex_Address77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Address__bibtex_Address77", None)
        self.__bibtex_Address77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Inbook76"):
                opp_val = getattr(old_value, "bibtex_Inbook76", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Inbook76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Inbook76"):
                opp_val = getattr(value, "bibtex_Inbook76", None)
                setattr(value, "bibtex_Inbook76", self)

    @property
    def bibtex_Address61(self):
        return self.__bibtex_Address61

    @bibtex_Address61.setter
    def bibtex_Address61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Address__bibtex_Address61", None)
        self.__bibtex_Address61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Conference60"):
                opp_val = getattr(old_value, "bibtex_Conference60", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Conference60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Conference60"):
                opp_val = getattr(value, "bibtex_Conference60", None)
                setattr(value, "bibtex_Conference60", self)

    @property
    def bibtex_Address(self):
        return self.__bibtex_Address

    @bibtex_Address.setter
    def bibtex_Address(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Address__bibtex_Address", None)
        self.__bibtex_Address = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Book34"):
                opp_val = getattr(old_value, "bibtex_Book34", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Book34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Book34"):
                opp_val = getattr(value, "bibtex_Book34", None)
                setattr(value, "bibtex_Book34", self)

    @property
    def bibtex_Address100(self):
        return self.__bibtex_Address100

    @bibtex_Address100.setter
    def bibtex_Address100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Address__bibtex_Address100", None)
        self.__bibtex_Address100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Incollection99"):
                opp_val = getattr(old_value, "bibtex_Incollection99", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Incollection99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Incollection99"):
                opp_val = getattr(value, "bibtex_Incollection99", None)
                setattr(value, "bibtex_Incollection99", self)

    @property
    def bibtex_Address177(self):
        return self.__bibtex_Address177

    @bibtex_Address177.setter
    def bibtex_Address177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Address__bibtex_Address177", None)
        self.__bibtex_Address177 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Techreport176"):
                opp_val = getattr(old_value, "bibtex_Techreport176", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Techreport176", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Techreport176"):
                opp_val = getattr(value, "bibtex_Techreport176", None)
                setattr(value, "bibtex_Techreport176", self)

    @property
    def bibtex_Address165(self):
        return self.__bibtex_Address165

    @bibtex_Address165.setter
    def bibtex_Address165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Address__bibtex_Address165", None)
        self.__bibtex_Address165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Proceedings164"):
                opp_val = getattr(old_value, "bibtex_Proceedings164", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Proceedings164", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Proceedings164"):
                opp_val = getattr(value, "bibtex_Proceedings164", None)
                setattr(value, "bibtex_Proceedings164", self)

    @property
    def bibtex_Address154(self):
        return self.__bibtex_Address154

    @bibtex_Address154.setter
    def bibtex_Address154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Address__bibtex_Address154", None)
        self.__bibtex_Address154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Phdthesis153"):
                opp_val = getattr(old_value, "bibtex_Phdthesis153", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Phdthesis153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Phdthesis153"):
                opp_val = getattr(value, "bibtex_Phdthesis153", None)
                setattr(value, "bibtex_Phdthesis153", self)

class bibtex_Series:

    def __init__(self, series: str, bibtex_Series: "bibtex_Book" = None, bibtex_Series74: "bibtex_Inbook" = None, bibtex_Series111: "bibtex_Inproceedings" = None):
        self.series = series
        self.bibtex_Series = bibtex_Series
        self.bibtex_Series74 = bibtex_Series74
        self.bibtex_Series111 = bibtex_Series111
        
        pass
    @property
    def series(self):
        return self.__series

    @series.setter
    def series(self, series: str):
        self.__series = series


    @property
    def bibtex_Series111(self):
        return self.__bibtex_Series111

    @bibtex_Series111.setter
    def bibtex_Series111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Series__bibtex_Series111", None)
        self.__bibtex_Series111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Inproceedings110"):
                opp_val = getattr(old_value, "bibtex_Inproceedings110", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Inproceedings110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Inproceedings110"):
                opp_val = getattr(value, "bibtex_Inproceedings110", None)
                setattr(value, "bibtex_Inproceedings110", self)

    @property
    def bibtex_Series74(self):
        return self.__bibtex_Series74

    @bibtex_Series74.setter
    def bibtex_Series74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Series__bibtex_Series74", None)
        self.__bibtex_Series74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Inbook73"):
                opp_val = getattr(old_value, "bibtex_Inbook73", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Inbook73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Inbook73"):
                opp_val = getattr(value, "bibtex_Inbook73", None)
                setattr(value, "bibtex_Inbook73", self)

    @property
    def bibtex_Series(self):
        return self.__bibtex_Series

    @bibtex_Series.setter
    def bibtex_Series(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Series__bibtex_Series", None)
        self.__bibtex_Series = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Book32"):
                opp_val = getattr(old_value, "bibtex_Book32", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Book32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Book32"):
                opp_val = getattr(value, "bibtex_Book32", None)
                setattr(value, "bibtex_Book32", self)

class bibtex_Journal:

    def __init__(self, journal: str, bibtex_Journal: "bibtex_Article" = None):
        self.journal = journal
        self.bibtex_Journal = bibtex_Journal
        
        pass
    @property
    def journal(self):
        return self.__journal

    @journal.setter
    def journal(self, journal: str):
        self.__journal = journal


    @property
    def bibtex_Journal(self):
        return self.__bibtex_Journal

    @bibtex_Journal.setter
    def bibtex_Journal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Journal__bibtex_Journal", None)
        self.__bibtex_Journal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Article15"):
                opp_val = getattr(old_value, "bibtex_Article15", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Article15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Article15"):
                opp_val = getattr(value, "bibtex_Article15", None)
                setattr(value, "bibtex_Article15", self)

class bibtex_Publisher:

    def __init__(self, publisher: str, bibtex_Publisher: "bibtex_Book" = None, bibtex_Publisher58: "bibtex_Conference" = None, bibtex_Publisher63: "bibtex_Inbook" = None, bibtex_Publisher120: "bibtex_Inproceedings" = None, bibtex_Publisher159: "bibtex_Proceedings" = None, bibtex_Publisher97: "bibtex_Incollection" = None):
        self.publisher = publisher
        self.bibtex_Publisher = bibtex_Publisher
        self.bibtex_Publisher58 = bibtex_Publisher58
        self.bibtex_Publisher63 = bibtex_Publisher63
        self.bibtex_Publisher120 = bibtex_Publisher120
        self.bibtex_Publisher159 = bibtex_Publisher159
        self.bibtex_Publisher97 = bibtex_Publisher97
        
        pass
    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher: str):
        self.__publisher = publisher


    @property
    def bibtex_Publisher159(self):
        return self.__bibtex_Publisher159

    @bibtex_Publisher159.setter
    def bibtex_Publisher159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Publisher__bibtex_Publisher159", None)
        self.__bibtex_Publisher159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Proceedings158"):
                opp_val = getattr(old_value, "bibtex_Proceedings158", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Proceedings158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Proceedings158"):
                opp_val = getattr(value, "bibtex_Proceedings158", None)
                setattr(value, "bibtex_Proceedings158", self)

    @property
    def bibtex_Publisher63(self):
        return self.__bibtex_Publisher63

    @bibtex_Publisher63.setter
    def bibtex_Publisher63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Publisher__bibtex_Publisher63", None)
        self.__bibtex_Publisher63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Inbook"):
                opp_val = getattr(old_value, "bibtex_Inbook", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Inbook", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Inbook"):
                opp_val = getattr(value, "bibtex_Inbook", None)
                setattr(value, "bibtex_Inbook", self)

    @property
    def bibtex_Publisher120(self):
        return self.__bibtex_Publisher120

    @bibtex_Publisher120.setter
    def bibtex_Publisher120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Publisher__bibtex_Publisher120", None)
        self.__bibtex_Publisher120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Inproceedings119"):
                opp_val = getattr(old_value, "bibtex_Inproceedings119", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Inproceedings119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Inproceedings119"):
                opp_val = getattr(value, "bibtex_Inproceedings119", None)
                setattr(value, "bibtex_Inproceedings119", self)

    @property
    def bibtex_Publisher58(self):
        return self.__bibtex_Publisher58

    @bibtex_Publisher58.setter
    def bibtex_Publisher58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Publisher__bibtex_Publisher58", None)
        self.__bibtex_Publisher58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Conference57"):
                opp_val = getattr(old_value, "bibtex_Conference57", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Conference57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Conference57"):
                opp_val = getattr(value, "bibtex_Conference57", None)
                setattr(value, "bibtex_Conference57", self)

    @property
    def bibtex_Publisher97(self):
        return self.__bibtex_Publisher97

    @bibtex_Publisher97.setter
    def bibtex_Publisher97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Publisher__bibtex_Publisher97", None)
        self.__bibtex_Publisher97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Incollection96"):
                opp_val = getattr(old_value, "bibtex_Incollection96", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Incollection96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Incollection96"):
                opp_val = getattr(value, "bibtex_Incollection96", None)
                setattr(value, "bibtex_Incollection96", self)

    @property
    def bibtex_Publisher(self):
        return self.__bibtex_Publisher

    @bibtex_Publisher.setter
    def bibtex_Publisher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Publisher__bibtex_Publisher", None)
        self.__bibtex_Publisher = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Book"):
                opp_val = getattr(old_value, "bibtex_Book", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Book", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Book"):
                opp_val = getattr(value, "bibtex_Book", None)
                setattr(value, "bibtex_Book", self)

class bibtex_Pages:

    def __init__(self, pages: str, bibtex_Pages: "bibtex_Article" = None, bibtex_Pages53: "bibtex_Conference" = None, bibtex_Pages68: "bibtex_Inbook" = None, bibtex_Pages114: "bibtex_Inproceedings" = None, bibtex_Pages91: "bibtex_Incollection" = None):
        self.pages = pages
        self.bibtex_Pages = bibtex_Pages
        self.bibtex_Pages53 = bibtex_Pages53
        self.bibtex_Pages68 = bibtex_Pages68
        self.bibtex_Pages114 = bibtex_Pages114
        self.bibtex_Pages91 = bibtex_Pages91
        
        pass
    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, pages: str):
        self.__pages = pages


    @property
    def bibtex_Pages(self):
        return self.__bibtex_Pages

    @bibtex_Pages.setter
    def bibtex_Pages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Pages__bibtex_Pages", None)
        self.__bibtex_Pages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Article21"):
                opp_val = getattr(old_value, "bibtex_Article21", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Article21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Article21"):
                opp_val = getattr(value, "bibtex_Article21", None)
                setattr(value, "bibtex_Article21", self)

    @property
    def bibtex_Pages68(self):
        return self.__bibtex_Pages68

    @bibtex_Pages68.setter
    def bibtex_Pages68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Pages__bibtex_Pages68", None)
        self.__bibtex_Pages68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Inbook67"):
                opp_val = getattr(old_value, "bibtex_Inbook67", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Inbook67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Inbook67"):
                opp_val = getattr(value, "bibtex_Inbook67", None)
                setattr(value, "bibtex_Inbook67", self)

    @property
    def bibtex_Pages53(self):
        return self.__bibtex_Pages53

    @bibtex_Pages53.setter
    def bibtex_Pages53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Pages__bibtex_Pages53", None)
        self.__bibtex_Pages53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Conference52"):
                opp_val = getattr(old_value, "bibtex_Conference52", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Conference52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Conference52"):
                opp_val = getattr(value, "bibtex_Conference52", None)
                setattr(value, "bibtex_Conference52", self)

    @property
    def bibtex_Pages114(self):
        return self.__bibtex_Pages114

    @bibtex_Pages114.setter
    def bibtex_Pages114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Pages__bibtex_Pages114", None)
        self.__bibtex_Pages114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Inproceedings113"):
                opp_val = getattr(old_value, "bibtex_Inproceedings113", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Inproceedings113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Inproceedings113"):
                opp_val = getattr(value, "bibtex_Inproceedings113", None)
                setattr(value, "bibtex_Inproceedings113", self)

    @property
    def bibtex_Pages91(self):
        return self.__bibtex_Pages91

    @bibtex_Pages91.setter
    def bibtex_Pages91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Pages__bibtex_Pages91", None)
        self.__bibtex_Pages91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Incollection90"):
                opp_val = getattr(old_value, "bibtex_Incollection90", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Incollection90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Incollection90"):
                opp_val = getattr(value, "bibtex_Incollection90", None)
                setattr(value, "bibtex_Incollection90", self)

class bibtex_Number:

    def __init__(self, number: str, bibtex_Number: "bibtex_Article" = None, bibtex_Number174: "bibtex_Techreport" = None):
        self.number = number
        self.bibtex_Number = bibtex_Number
        self.bibtex_Number174 = bibtex_Number174
        
        pass
    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number


    @property
    def bibtex_Number(self):
        return self.__bibtex_Number

    @bibtex_Number.setter
    def bibtex_Number(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Number__bibtex_Number", None)
        self.__bibtex_Number = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Article19"):
                opp_val = getattr(old_value, "bibtex_Article19", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Article19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Article19"):
                opp_val = getattr(value, "bibtex_Article19", None)
                setattr(value, "bibtex_Article19", self)

    @property
    def bibtex_Number174(self):
        return self.__bibtex_Number174

    @bibtex_Number174.setter
    def bibtex_Number174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Number__bibtex_Number174", None)
        self.__bibtex_Number174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Techreport173"):
                opp_val = getattr(old_value, "bibtex_Techreport173", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Techreport173", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Techreport173"):
                opp_val = getattr(value, "bibtex_Techreport173", None)
                setattr(value, "bibtex_Techreport173", self)

class bibtex_Volume:

    def __init__(self, volume: str, bibtex_Volume: "bibtex_Article" = None, bibtex_Volume30: "bibtex_Book" = None, bibtex_Volume71: "bibtex_Inbook" = None):
        self.volume = volume
        self.bibtex_Volume = bibtex_Volume
        self.bibtex_Volume30 = bibtex_Volume30
        self.bibtex_Volume71 = bibtex_Volume71
        
        pass
    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume: str):
        self.__volume = volume


    @property
    def bibtex_Volume30(self):
        return self.__bibtex_Volume30

    @bibtex_Volume30.setter
    def bibtex_Volume30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Volume__bibtex_Volume30", None)
        self.__bibtex_Volume30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Book29"):
                opp_val = getattr(old_value, "bibtex_Book29", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Book29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Book29"):
                opp_val = getattr(value, "bibtex_Book29", None)
                setattr(value, "bibtex_Book29", self)

    @property
    def bibtex_Volume(self):
        return self.__bibtex_Volume

    @bibtex_Volume.setter
    def bibtex_Volume(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Volume__bibtex_Volume", None)
        self.__bibtex_Volume = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Article17"):
                opp_val = getattr(old_value, "bibtex_Article17", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Article17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Article17"):
                opp_val = getattr(value, "bibtex_Article17", None)
                setattr(value, "bibtex_Article17", self)

    @property
    def bibtex_Volume71(self):
        return self.__bibtex_Volume71

    @bibtex_Volume71.setter
    def bibtex_Volume71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Volume__bibtex_Volume71", None)
        self.__bibtex_Volume71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Inbook70"):
                opp_val = getattr(old_value, "bibtex_Inbook70", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Inbook70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Inbook70"):
                opp_val = getattr(value, "bibtex_Inbook70", None)
                setattr(value, "bibtex_Inbook70", self)

class bibtex_Note:

    def __init__(self, note: str, bibtex_Note: "bibtex_BibType" = None):
        self.note = note
        self.bibtex_Note = bibtex_Note
        
        pass
    @property
    def note(self):
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note


    @property
    def bibtex_Note(self):
        return self.__bibtex_Note

    @bibtex_Note.setter
    def bibtex_Note(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Note__bibtex_Note", None)
        self.__bibtex_Note = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_BibType10"):
                opp_val = getattr(old_value, "bibtex_BibType10", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_BibType10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_BibType10"):
                opp_val = getattr(value, "bibtex_BibType10", None)
                setattr(value, "bibtex_BibType10", self)

class bibtex_Author:

    def __init__(self, author: str, bibtex_Author: "bibtex_Article" = None, bibtex_Author25: "bibtex_Book" = None, bibtex_Author38: "bibtex_Booklet" = None, bibtex_Author45: "bibtex_Conference" = None, bibtex_Author125: "bibtex_Manual" = None, bibtex_Author143: "bibtex_Misc" = None, bibtex_Author136: "bibtex_Mastersthesis" = None, bibtex_Author148: "bibtex_Phdthesis" = None, bibtex_Author167: "bibtex_Techreport" = None, bibtex_Author179: "bibtex_Unpublished" = None, bibtex_Author82: "bibtex_Incollection" = None, bibtex_Author102: "bibtex_Inproceedings" = None):
        self.author = author
        self.bibtex_Author = bibtex_Author
        self.bibtex_Author25 = bibtex_Author25
        self.bibtex_Author38 = bibtex_Author38
        self.bibtex_Author45 = bibtex_Author45
        self.bibtex_Author125 = bibtex_Author125
        self.bibtex_Author143 = bibtex_Author143
        self.bibtex_Author136 = bibtex_Author136
        self.bibtex_Author148 = bibtex_Author148
        self.bibtex_Author167 = bibtex_Author167
        self.bibtex_Author179 = bibtex_Author179
        self.bibtex_Author82 = bibtex_Author82
        self.bibtex_Author102 = bibtex_Author102
        
        pass
    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author


    @property
    def bibtex_Author167(self):
        return self.__bibtex_Author167

    @bibtex_Author167.setter
    def bibtex_Author167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Author__bibtex_Author167", None)
        self.__bibtex_Author167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Techreport"):
                opp_val = getattr(old_value, "bibtex_Techreport", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Techreport", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Techreport"):
                opp_val = getattr(value, "bibtex_Techreport", None)
                setattr(value, "bibtex_Techreport", self)

    @property
    def bibtex_Author45(self):
        return self.__bibtex_Author45

    @bibtex_Author45.setter
    def bibtex_Author45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Author__bibtex_Author45", None)
        self.__bibtex_Author45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Conference"):
                opp_val = getattr(old_value, "bibtex_Conference", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Conference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Conference"):
                opp_val = getattr(value, "bibtex_Conference", None)
                setattr(value, "bibtex_Conference", self)

    @property
    def bibtex_Author25(self):
        return self.__bibtex_Author25

    @bibtex_Author25.setter
    def bibtex_Author25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Author__bibtex_Author25", None)
        self.__bibtex_Author25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Book24"):
                opp_val = getattr(old_value, "bibtex_Book24", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Book24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Book24"):
                opp_val = getattr(value, "bibtex_Book24", None)
                setattr(value, "bibtex_Book24", self)

    @property
    def bibtex_Author102(self):
        return self.__bibtex_Author102

    @bibtex_Author102.setter
    def bibtex_Author102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Author__bibtex_Author102", None)
        self.__bibtex_Author102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Inproceedings"):
                opp_val = getattr(old_value, "bibtex_Inproceedings", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Inproceedings", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Inproceedings"):
                opp_val = getattr(value, "bibtex_Inproceedings", None)
                setattr(value, "bibtex_Inproceedings", self)

    @property
    def bibtex_Author136(self):
        return self.__bibtex_Author136

    @bibtex_Author136.setter
    def bibtex_Author136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Author__bibtex_Author136", None)
        self.__bibtex_Author136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Mastersthesis"):
                opp_val = getattr(old_value, "bibtex_Mastersthesis", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Mastersthesis", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Mastersthesis"):
                opp_val = getattr(value, "bibtex_Mastersthesis", None)
                setattr(value, "bibtex_Mastersthesis", self)

    @property
    def bibtex_Author125(self):
        return self.__bibtex_Author125

    @bibtex_Author125.setter
    def bibtex_Author125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Author__bibtex_Author125", None)
        self.__bibtex_Author125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Manual"):
                opp_val = getattr(old_value, "bibtex_Manual", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Manual", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Manual"):
                opp_val = getattr(value, "bibtex_Manual", None)
                setattr(value, "bibtex_Manual", self)

    @property
    def bibtex_Author143(self):
        return self.__bibtex_Author143

    @bibtex_Author143.setter
    def bibtex_Author143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Author__bibtex_Author143", None)
        self.__bibtex_Author143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Misc"):
                opp_val = getattr(old_value, "bibtex_Misc", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Misc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Misc"):
                opp_val = getattr(value, "bibtex_Misc", None)
                setattr(value, "bibtex_Misc", self)

    @property
    def bibtex_Author38(self):
        return self.__bibtex_Author38

    @bibtex_Author38.setter
    def bibtex_Author38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Author__bibtex_Author38", None)
        self.__bibtex_Author38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Booklet"):
                opp_val = getattr(old_value, "bibtex_Booklet", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Booklet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Booklet"):
                opp_val = getattr(value, "bibtex_Booklet", None)
                setattr(value, "bibtex_Booklet", self)

    @property
    def bibtex_Author82(self):
        return self.__bibtex_Author82

    @bibtex_Author82.setter
    def bibtex_Author82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Author__bibtex_Author82", None)
        self.__bibtex_Author82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Incollection"):
                opp_val = getattr(old_value, "bibtex_Incollection", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Incollection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Incollection"):
                opp_val = getattr(value, "bibtex_Incollection", None)
                setattr(value, "bibtex_Incollection", self)

    @property
    def bibtex_Author(self):
        return self.__bibtex_Author

    @bibtex_Author.setter
    def bibtex_Author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Author__bibtex_Author", None)
        self.__bibtex_Author = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Article"):
                opp_val = getattr(old_value, "bibtex_Article", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Article", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Article"):
                opp_val = getattr(value, "bibtex_Article", None)
                setattr(value, "bibtex_Article", self)

    @property
    def bibtex_Author179(self):
        return self.__bibtex_Author179

    @bibtex_Author179.setter
    def bibtex_Author179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Author__bibtex_Author179", None)
        self.__bibtex_Author179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Unpublished"):
                opp_val = getattr(old_value, "bibtex_Unpublished", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Unpublished", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Unpublished"):
                opp_val = getattr(value, "bibtex_Unpublished", None)
                setattr(value, "bibtex_Unpublished", self)

    @property
    def bibtex_Author148(self):
        return self.__bibtex_Author148

    @bibtex_Author148.setter
    def bibtex_Author148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Author__bibtex_Author148", None)
        self.__bibtex_Author148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Phdthesis"):
                opp_val = getattr(old_value, "bibtex_Phdthesis", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Phdthesis", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Phdthesis"):
                opp_val = getattr(value, "bibtex_Phdthesis", None)
                setattr(value, "bibtex_Phdthesis", self)

class BibType:

    pass
class bibtex_Booklet(BibType):

    pass
class bibtex_Book(BibType):

    pass
class bibtex_Article(BibType):

    pass
class bibtex_Key:

    def __init__(self, key: str, bibtex_Key: "bibtex_BibType" = None):
        self.key = key
        self.bibtex_Key = bibtex_Key
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def bibtex_Key(self):
        return self.__bibtex_Key

    @bibtex_Key.setter
    def bibtex_Key(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Key__bibtex_Key", None)
        self.__bibtex_Key = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_BibType12"):
                opp_val = getattr(old_value, "bibtex_BibType12", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_BibType12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_BibType12"):
                opp_val = getattr(value, "bibtex_BibType12", None)
                setattr(value, "bibtex_BibType12", self)

class bibtex_Month:

    def __init__(self, month: str, bibtex_Month: "bibtex_BibType" = None):
        self.month = month
        self.bibtex_Month = bibtex_Month
        
        pass
    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month


    @property
    def bibtex_Month(self):
        return self.__bibtex_Month

    @bibtex_Month.setter
    def bibtex_Month(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Month__bibtex_Month", None)
        self.__bibtex_Month = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_BibType8"):
                opp_val = getattr(old_value, "bibtex_BibType8", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_BibType8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_BibType8"):
                opp_val = getattr(value, "bibtex_BibType8", None)
                setattr(value, "bibtex_BibType8", self)

class bibtex_Year:

    def __init__(self, year: str, bibtex_Year: "bibtex_BibType" = None):
        self.year = year
        self.bibtex_Year = bibtex_Year
        
        pass
    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year


    @property
    def bibtex_Year(self):
        return self.__bibtex_Year

    @bibtex_Year.setter
    def bibtex_Year(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Year__bibtex_Year", None)
        self.__bibtex_Year = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_BibType6"):
                opp_val = getattr(old_value, "bibtex_BibType6", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_BibType6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_BibType6"):
                opp_val = getattr(value, "bibtex_BibType6", None)
                setattr(value, "bibtex_BibType6", self)

class bibtex_Title:

    def __init__(self, title: str, bibtex_Title: "bibtex_BibType" = None):
        self.title = title
        self.bibtex_Title = bibtex_Title
        
        pass
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def bibtex_Title(self):
        return self.__bibtex_Title

    @bibtex_Title.setter
    def bibtex_Title(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Title__bibtex_Title", None)
        self.__bibtex_Title = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_BibType4"):
                opp_val = getattr(old_value, "bibtex_BibType4", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_BibType4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_BibType4"):
                opp_val = getattr(value, "bibtex_BibType4", None)
                setattr(value, "bibtex_BibType4", self)

class bibtex_CiteKey:

    def __init__(self, citeKey: str, bibtex_CiteKey: "bibtex_BibType" = None):
        self.citeKey = citeKey
        self.bibtex_CiteKey = bibtex_CiteKey
        
        pass
    @property
    def citeKey(self):
        return self.__citeKey

    @citeKey.setter
    def citeKey(self, citeKey: str):
        self.__citeKey = citeKey


    @property
    def bibtex_CiteKey(self):
        return self.__bibtex_CiteKey

    @bibtex_CiteKey.setter
    def bibtex_CiteKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_CiteKey__bibtex_CiteKey", None)
        self.__bibtex_CiteKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_BibType2"):
                opp_val = getattr(old_value, "bibtex_BibType2", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_BibType2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_BibType2"):
                opp_val = getattr(value, "bibtex_BibType2", None)
                setattr(value, "bibtex_BibType2", self)

class bibtex_BibType:

    pass
class bibtex_Model:

    pass
class bibtex_Unpublished(BibType):

    pass
class bibtex_Crossref:

    def __init__(self, crossref: str):
        self.crossref = crossref
        
        pass
    @property
    def crossref(self):
        return self.__crossref

    @crossref.setter
    def crossref(self, crossref: str):
        self.__crossref = crossref


class bibtex_Techreport(BibType):

    pass
class bibtex_Type:

    def __init__(self, type: str, bibtex_Type: "bibtex_Techreport" = None):
        self.type = type
        self.bibtex_Type = bibtex_Type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def bibtex_Type(self):
        return self.__bibtex_Type

    @bibtex_Type.setter
    def bibtex_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Type__bibtex_Type", None)
        self.__bibtex_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Techreport171"):
                opp_val = getattr(old_value, "bibtex_Techreport171", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Techreport171", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Techreport171"):
                opp_val = getattr(value, "bibtex_Techreport171", None)
                setattr(value, "bibtex_Techreport171", self)

class bibtex_Institution:

    def __init__(self, institution: str, bibtex_Institution: "bibtex_Techreport" = None):
        self.institution = institution
        self.bibtex_Institution = bibtex_Institution
        
        pass
    @property
    def institution(self):
        return self.__institution

    @institution.setter
    def institution(self, institution: str):
        self.__institution = institution


    @property
    def bibtex_Institution(self):
        return self.__bibtex_Institution

    @bibtex_Institution.setter
    def bibtex_Institution(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Institution__bibtex_Institution", None)
        self.__bibtex_Institution = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Techreport169"):
                opp_val = getattr(old_value, "bibtex_Techreport169", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Techreport169", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Techreport169"):
                opp_val = getattr(value, "bibtex_Techreport169", None)
                setattr(value, "bibtex_Techreport169", self)

class bibtex_Proceedings(BibType):

    pass
class bibtex_Phdthesis(BibType):

    pass
class bibtex_Misc(BibType):

    pass
class bibtex_School:

    def __init__(self, school: str, bibtex_School: "bibtex_Mastersthesis" = None, bibtex_School151: "bibtex_Phdthesis" = None):
        self.school = school
        self.bibtex_School = bibtex_School
        self.bibtex_School151 = bibtex_School151
        
        pass
    @property
    def school(self):
        return self.__school

    @school.setter
    def school(self, school: str):
        self.__school = school


    @property
    def bibtex_School(self):
        return self.__bibtex_School

    @bibtex_School.setter
    def bibtex_School(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_School__bibtex_School", None)
        self.__bibtex_School = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Mastersthesis138"):
                opp_val = getattr(old_value, "bibtex_Mastersthesis138", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Mastersthesis138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Mastersthesis138"):
                opp_val = getattr(value, "bibtex_Mastersthesis138", None)
                setattr(value, "bibtex_Mastersthesis138", self)

    @property
    def bibtex_School151(self):
        return self.__bibtex_School151

    @bibtex_School151.setter
    def bibtex_School151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_School__bibtex_School151", None)
        self.__bibtex_School151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Phdthesis150"):
                opp_val = getattr(old_value, "bibtex_Phdthesis150", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Phdthesis150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Phdthesis150"):
                opp_val = getattr(value, "bibtex_Phdthesis150", None)
                setattr(value, "bibtex_Phdthesis150", self)

class bibtex_Manual(BibType):

    pass
class bibtex_Mastersthesis(BibType):

    pass
class bibtex_Inproceedings(BibType):

    pass
class bibtex_Incollection(BibType):

    pass
class bibtex_Inbook(BibType):

    def __init__(self, author: bool, editor: bool, bibtex_Inbook65: "bibtex_Chapter" = None, bibtex_Inbook: "bibtex_Publisher" = None, bibtex_Inbook73: "bibtex_Series" = None, bibtex_Inbook67: "bibtex_Pages" = None, bibtex_Inbook70: "bibtex_Volume" = None, bibtex_Inbook76: "bibtex_Address" = None, bibtex_Inbook79: "bibtex_Edition" = None):
        self.author = author
        self.editor = editor
        self.bibtex_Inbook65 = bibtex_Inbook65
        self.bibtex_Inbook = bibtex_Inbook
        self.bibtex_Inbook73 = bibtex_Inbook73
        self.bibtex_Inbook67 = bibtex_Inbook67
        self.bibtex_Inbook70 = bibtex_Inbook70
        self.bibtex_Inbook76 = bibtex_Inbook76
        self.bibtex_Inbook79 = bibtex_Inbook79
        
        pass
    @property
    def editor(self):
        return self.__editor

    @editor.setter
    def editor(self, editor: bool):
        self.__editor = editor


    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author: bool):
        self.__author = author


    @property
    def bibtex_Inbook67(self):
        return self.__bibtex_Inbook67

    @bibtex_Inbook67.setter
    def bibtex_Inbook67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Inbook__bibtex_Inbook67", None)
        self.__bibtex_Inbook67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Pages68"):
                opp_val = getattr(old_value, "bibtex_Pages68", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Pages68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Pages68"):
                opp_val = getattr(value, "bibtex_Pages68", None)
                setattr(value, "bibtex_Pages68", self)

    @property
    def bibtex_Inbook76(self):
        return self.__bibtex_Inbook76

    @bibtex_Inbook76.setter
    def bibtex_Inbook76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Inbook__bibtex_Inbook76", None)
        self.__bibtex_Inbook76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Address77"):
                opp_val = getattr(old_value, "bibtex_Address77", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Address77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Address77"):
                opp_val = getattr(value, "bibtex_Address77", None)
                setattr(value, "bibtex_Address77", self)

    @property
    def bibtex_Inbook65(self):
        return self.__bibtex_Inbook65

    @bibtex_Inbook65.setter
    def bibtex_Inbook65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Inbook__bibtex_Inbook65", None)
        self.__bibtex_Inbook65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Chapter"):
                opp_val = getattr(old_value, "bibtex_Chapter", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Chapter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Chapter"):
                opp_val = getattr(value, "bibtex_Chapter", None)
                setattr(value, "bibtex_Chapter", self)

    @property
    def bibtex_Inbook(self):
        return self.__bibtex_Inbook

    @bibtex_Inbook.setter
    def bibtex_Inbook(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Inbook__bibtex_Inbook", None)
        self.__bibtex_Inbook = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Publisher63"):
                opp_val = getattr(old_value, "bibtex_Publisher63", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Publisher63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Publisher63"):
                opp_val = getattr(value, "bibtex_Publisher63", None)
                setattr(value, "bibtex_Publisher63", self)

    @property
    def bibtex_Inbook73(self):
        return self.__bibtex_Inbook73

    @bibtex_Inbook73.setter
    def bibtex_Inbook73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Inbook__bibtex_Inbook73", None)
        self.__bibtex_Inbook73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Series74"):
                opp_val = getattr(old_value, "bibtex_Series74", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Series74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Series74"):
                opp_val = getattr(value, "bibtex_Series74", None)
                setattr(value, "bibtex_Series74", self)

    @property
    def bibtex_Inbook79(self):
        return self.__bibtex_Inbook79

    @bibtex_Inbook79.setter
    def bibtex_Inbook79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Inbook__bibtex_Inbook79", None)
        self.__bibtex_Inbook79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Edition80"):
                opp_val = getattr(old_value, "bibtex_Edition80", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Edition80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Edition80"):
                opp_val = getattr(value, "bibtex_Edition80", None)
                setattr(value, "bibtex_Edition80", self)

    @property
    def bibtex_Inbook70(self):
        return self.__bibtex_Inbook70

    @bibtex_Inbook70.setter
    def bibtex_Inbook70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Inbook__bibtex_Inbook70", None)
        self.__bibtex_Inbook70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Volume71"):
                opp_val = getattr(old_value, "bibtex_Volume71", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Volume71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Volume71"):
                opp_val = getattr(value, "bibtex_Volume71", None)
                setattr(value, "bibtex_Volume71", self)

class bibtex_Chapter:

    def __init__(self, chapter: str, bibtex_Chapter: "bibtex_Inbook" = None):
        self.chapter = chapter
        self.bibtex_Chapter = bibtex_Chapter
        
        pass
    @property
    def chapter(self):
        return self.__chapter

    @chapter.setter
    def chapter(self, chapter: str):
        self.__chapter = chapter


    @property
    def bibtex_Chapter(self):
        return self.__bibtex_Chapter

    @bibtex_Chapter.setter
    def bibtex_Chapter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Chapter__bibtex_Chapter", None)
        self.__bibtex_Chapter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Inbook65"):
                opp_val = getattr(old_value, "bibtex_Inbook65", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Inbook65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Inbook65"):
                opp_val = getattr(value, "bibtex_Inbook65", None)
                setattr(value, "bibtex_Inbook65", self)

class bibtex_Organization:

    def __init__(self, organization: str, bibtex_Organization: "bibtex_Conference" = None, bibtex_Organization117: "bibtex_Inproceedings" = None, bibtex_Organization128: "bibtex_Manual" = None, bibtex_Organization162: "bibtex_Proceedings" = None, bibtex_Organization94: "bibtex_Incollection" = None):
        self.organization = organization
        self.bibtex_Organization = bibtex_Organization
        self.bibtex_Organization117 = bibtex_Organization117
        self.bibtex_Organization128 = bibtex_Organization128
        self.bibtex_Organization162 = bibtex_Organization162
        self.bibtex_Organization94 = bibtex_Organization94
        
        pass
    @property
    def organization(self):
        return self.__organization

    @organization.setter
    def organization(self, organization: str):
        self.__organization = organization


    @property
    def bibtex_Organization162(self):
        return self.__bibtex_Organization162

    @bibtex_Organization162.setter
    def bibtex_Organization162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Organization__bibtex_Organization162", None)
        self.__bibtex_Organization162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Proceedings161"):
                opp_val = getattr(old_value, "bibtex_Proceedings161", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Proceedings161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Proceedings161"):
                opp_val = getattr(value, "bibtex_Proceedings161", None)
                setattr(value, "bibtex_Proceedings161", self)

    @property
    def bibtex_Organization(self):
        return self.__bibtex_Organization

    @bibtex_Organization.setter
    def bibtex_Organization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Organization__bibtex_Organization", None)
        self.__bibtex_Organization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Conference55"):
                opp_val = getattr(old_value, "bibtex_Conference55", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Conference55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Conference55"):
                opp_val = getattr(value, "bibtex_Conference55", None)
                setattr(value, "bibtex_Conference55", self)

    @property
    def bibtex_Organization128(self):
        return self.__bibtex_Organization128

    @bibtex_Organization128.setter
    def bibtex_Organization128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Organization__bibtex_Organization128", None)
        self.__bibtex_Organization128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Manual127"):
                opp_val = getattr(old_value, "bibtex_Manual127", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Manual127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Manual127"):
                opp_val = getattr(value, "bibtex_Manual127", None)
                setattr(value, "bibtex_Manual127", self)

    @property
    def bibtex_Organization117(self):
        return self.__bibtex_Organization117

    @bibtex_Organization117.setter
    def bibtex_Organization117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Organization__bibtex_Organization117", None)
        self.__bibtex_Organization117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Inproceedings116"):
                opp_val = getattr(old_value, "bibtex_Inproceedings116", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Inproceedings116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Inproceedings116"):
                opp_val = getattr(value, "bibtex_Inproceedings116", None)
                setattr(value, "bibtex_Inproceedings116", self)

    @property
    def bibtex_Organization94(self):
        return self.__bibtex_Organization94

    @bibtex_Organization94.setter
    def bibtex_Organization94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Organization__bibtex_Organization94", None)
        self.__bibtex_Organization94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Incollection93"):
                opp_val = getattr(old_value, "bibtex_Incollection93", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Incollection93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Incollection93"):
                opp_val = getattr(value, "bibtex_Incollection93", None)
                setattr(value, "bibtex_Incollection93", self)

class bibtex_Booktitle:

    def __init__(self, booktitle: str, bibtex_Booktitle: "bibtex_Conference" = None, bibtex_Booktitle85: "bibtex_Incollection" = None, bibtex_Booktitle105: "bibtex_Inproceedings" = None):
        self.booktitle = booktitle
        self.bibtex_Booktitle = bibtex_Booktitle
        self.bibtex_Booktitle85 = bibtex_Booktitle85
        self.bibtex_Booktitle105 = bibtex_Booktitle105
        
        pass
    @property
    def booktitle(self):
        return self.__booktitle

    @booktitle.setter
    def booktitle(self, booktitle: str):
        self.__booktitle = booktitle


    @property
    def bibtex_Booktitle85(self):
        return self.__bibtex_Booktitle85

    @bibtex_Booktitle85.setter
    def bibtex_Booktitle85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Booktitle__bibtex_Booktitle85", None)
        self.__bibtex_Booktitle85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Incollection84"):
                opp_val = getattr(old_value, "bibtex_Incollection84", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Incollection84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Incollection84"):
                opp_val = getattr(value, "bibtex_Incollection84", None)
                setattr(value, "bibtex_Incollection84", self)

    @property
    def bibtex_Booktitle105(self):
        return self.__bibtex_Booktitle105

    @bibtex_Booktitle105.setter
    def bibtex_Booktitle105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Booktitle__bibtex_Booktitle105", None)
        self.__bibtex_Booktitle105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Inproceedings104"):
                opp_val = getattr(old_value, "bibtex_Inproceedings104", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Inproceedings104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Inproceedings104"):
                opp_val = getattr(value, "bibtex_Inproceedings104", None)
                setattr(value, "bibtex_Inproceedings104", self)

    @property
    def bibtex_Booktitle(self):
        return self.__bibtex_Booktitle

    @bibtex_Booktitle.setter
    def bibtex_Booktitle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Booktitle__bibtex_Booktitle", None)
        self.__bibtex_Booktitle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Conference47"):
                opp_val = getattr(old_value, "bibtex_Conference47", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Conference47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Conference47"):
                opp_val = getattr(value, "bibtex_Conference47", None)
                setattr(value, "bibtex_Conference47", self)

class bibtex_Conference(BibType):

    pass
class bibtex_Howpublished:

    def __init__(self, howpublished: str, bibtex_Howpublished: "bibtex_Booklet" = None, bibtex_Howpublished146: "bibtex_Misc" = None):
        self.howpublished = howpublished
        self.bibtex_Howpublished = bibtex_Howpublished
        self.bibtex_Howpublished146 = bibtex_Howpublished146
        
        pass
    @property
    def howpublished(self):
        return self.__howpublished

    @howpublished.setter
    def howpublished(self, howpublished: str):
        self.__howpublished = howpublished


    @property
    def bibtex_Howpublished(self):
        return self.__bibtex_Howpublished

    @bibtex_Howpublished.setter
    def bibtex_Howpublished(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Howpublished__bibtex_Howpublished", None)
        self.__bibtex_Howpublished = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Booklet40"):
                opp_val = getattr(old_value, "bibtex_Booklet40", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Booklet40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Booklet40"):
                opp_val = getattr(value, "bibtex_Booklet40", None)
                setattr(value, "bibtex_Booklet40", self)

    @property
    def bibtex_Howpublished146(self):
        return self.__bibtex_Howpublished146

    @bibtex_Howpublished146.setter
    def bibtex_Howpublished146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bibtex_Howpublished__bibtex_Howpublished146", None)
        self.__bibtex_Howpublished146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bibtex_Misc145"):
                opp_val = getattr(old_value, "bibtex_Misc145", None)
                if opp_val == self:
                    setattr(old_value, "bibtex_Misc145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bibtex_Misc145"):
                opp_val = getattr(value, "bibtex_Misc145", None)
                setattr(value, "bibtex_Misc145", self)
