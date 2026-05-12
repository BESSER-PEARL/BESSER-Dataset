from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Bibtex_Tag:

    def __init__(self, Name: str, Bibtex_Tag: "Bibtex_BibtexEntry" = None):
        self.Name = Name
        self.Bibtex_Tag = Bibtex_Tag
        
        pass
    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name


    @property
    def Bibtex_Tag(self):
        return self.__Bibtex_Tag

    @Bibtex_Tag.setter
    def Bibtex_Tag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bibtex_Tag__Bibtex_Tag", None)
        self.__Bibtex_Tag = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Bibtex_BibtexEntry"):
                opp_val = getattr(old_value, "Bibtex_BibtexEntry", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Bibtex_BibtexEntry"):
                opp_val = getattr(value, "Bibtex_BibtexEntry", None)
                if opp_val is None:
                    setattr(value, "Bibtex_BibtexEntry", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def toString(self) :
        # TODO: Implement toString method
        pass

class Bibtex_BibtexEntry:

    def __init__(self, Text: str, Title: str, Author: str, Journal: str, Volume: str, Pages: str, Year: str, publicationFilePath: str, Bibtex_BibtexEntry: set["Bibtex_Tag"] = None):
        self.Text = Text
        self.Title = Title
        self.Author = Author
        self.Journal = Journal
        self.Volume = Volume
        self.Pages = Pages
        self.Year = Year
        self.publicationFilePath = publicationFilePath
        self.Bibtex_BibtexEntry = Bibtex_BibtexEntry if Bibtex_BibtexEntry is not None else set()
        
        pass
    @property
    def Author(self):
        return self.__Author

    @Author.setter
    def Author(self, Author: str):
        self.__Author = Author


    @property
    def Year(self):
        return self.__Year

    @Year.setter
    def Year(self, Year: str):
        self.__Year = Year


    @property
    def Journal(self):
        return self.__Journal

    @Journal.setter
    def Journal(self, Journal: str):
        self.__Journal = Journal


    @property
    def Pages(self):
        return self.__Pages

    @Pages.setter
    def Pages(self, Pages: str):
        self.__Pages = Pages


    @property
    def Volume(self):
        return self.__Volume

    @Volume.setter
    def Volume(self, Volume: str):
        self.__Volume = Volume


    @property
    def Title(self):
        return self.__Title

    @Title.setter
    def Title(self, Title: str):
        self.__Title = Title


    @property
    def Text(self):
        return self.__Text

    @Text.setter
    def Text(self, Text: str):
        self.__Text = Text


    @property
    def publicationFilePath(self):
        return self.__publicationFilePath

    @publicationFilePath.setter
    def publicationFilePath(self, publicationFilePath: str):
        self.__publicationFilePath = publicationFilePath


    @property
    def Bibtex_BibtexEntry(self):
        return self.__Bibtex_BibtexEntry

    @Bibtex_BibtexEntry.setter
    def Bibtex_BibtexEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bibtex_BibtexEntry__Bibtex_BibtexEntry", None)
        self.__Bibtex_BibtexEntry = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Bibtex_Tag"):
                    opp_val = getattr(item, "Bibtex_Tag", None)
                    
                    if opp_val == self:
                        setattr(item, "Bibtex_Tag", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Bibtex_Tag"):
                    opp_val = getattr(item, "Bibtex_Tag", None)
                    
                    setattr(item, "Bibtex_Tag", self)
                    

    def toString(self) :
        # TODO: Implement toString method
        pass
