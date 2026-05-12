from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Bibtex_Entry:

    def __init__(self, title: str, id: str, Entry: "Bibtex_LiteratureDb" = None, publications: set["Bibtex_Author"] = None, entries: "Bibtex_LiteratureDb" = None, Entry7: "Bibtex_Author" = None):
        self.title = title
        self.id = id
        self.Entry = Entry
        self.publications = publications if publications is not None else set()
        self.entries = entries
        self.Entry7 = Entry7
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def publications(self):
        return self.__publications

    @publications.setter
    def publications(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bibtex_Entry__publications", None)
        self.__publications = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Author4"):
                    opp_val = getattr(item, "Author4", None)
                    
                    if opp_val == self:
                        setattr(item, "Author4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Author4"):
                    opp_val = getattr(item, "Author4", None)
                    
                    setattr(item, "Author4", self)
                    

    @property
    def entries(self):
        return self.__entries

    @entries.setter
    def entries(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bibtex_Entry__entries", None)
        self.__entries = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LiteratureDb"):
                opp_val = getattr(old_value, "LiteratureDb", None)
                if opp_val == self:
                    setattr(old_value, "LiteratureDb", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LiteratureDb"):
                opp_val = getattr(value, "LiteratureDb", None)
                setattr(value, "LiteratureDb", self)

    @property
    def Entry(self):
        return self.__Entry

    @Entry.setter
    def Entry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bibtex_Entry__Entry", None)
        self.__Entry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "literaturedb2"):
                opp_val = getattr(old_value, "literaturedb2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "literaturedb2"):
                opp_val = getattr(value, "literaturedb2", None)
                if opp_val is None:
                    setattr(value, "literaturedb2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Entry7(self):
        return self.__Entry7

    @Entry7.setter
    def Entry7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bibtex_Entry__Entry7", None)
        self.__Entry7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "author"):
                opp_val = getattr(old_value, "author", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "author"):
                opp_val = getattr(value, "author", None)
                if opp_val is None:
                    setattr(value, "author", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Bibtex_Author:

    def __init__(self, name: str, Author4: "Bibtex_Entry" = None, author: set["Bibtex_Entry"] = None, author9: "Bibtex_LiteratureDb" = None, Author: "Bibtex_LiteratureDb" = None):
        self.name = name
        self.Author4 = Author4
        self.author = author if author is not None else set()
        self.author9 = author9
        self.Author = Author
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def Author4(self):
        return self.__Author4

    @Author4.setter
    def Author4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bibtex_Author__Author4", None)
        self.__Author4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publications"):
                opp_val = getattr(old_value, "publications", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publications"):
                opp_val = getattr(value, "publications", None)
                if opp_val is None:
                    setattr(value, "publications", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Author(self):
        return self.__Author

    @Author.setter
    def Author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bibtex_Author__Author", None)
        self.__Author = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "literaturedb"):
                opp_val = getattr(old_value, "literaturedb", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "literaturedb"):
                opp_val = getattr(value, "literaturedb", None)
                if opp_val is None:
                    setattr(value, "literaturedb", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bibtex_Author__author", None)
        self.__author = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Entry7"):
                    opp_val = getattr(item, "Entry7", None)
                    
                    if opp_val == self:
                        setattr(item, "Entry7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Entry7"):
                    opp_val = getattr(item, "Entry7", None)
                    
                    setattr(item, "Entry7", self)
                    

    @property
    def author9(self):
        return self.__author9

    @author9.setter
    def author9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bibtex_Author__author9", None)
        self.__author9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LiteratureDb10"):
                opp_val = getattr(old_value, "LiteratureDb10", None)
                if opp_val == self:
                    setattr(old_value, "LiteratureDb10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LiteratureDb10"):
                opp_val = getattr(value, "LiteratureDb10", None)
                setattr(value, "LiteratureDb10", self)

class Bibtex_LiteratureDb:

    def __init__(self, name: str, literaturedb2: set["Bibtex_Entry"] = None, LiteratureDb: "Bibtex_Entry" = None, LiteratureDb10: "Bibtex_Author" = None, literaturedb: set["Bibtex_Author"] = None):
        self.name = name
        self.literaturedb2 = literaturedb2 if literaturedb2 is not None else set()
        self.LiteratureDb = LiteratureDb
        self.LiteratureDb10 = LiteratureDb10
        self.literaturedb = literaturedb if literaturedb is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def LiteratureDb(self):
        return self.__LiteratureDb

    @LiteratureDb.setter
    def LiteratureDb(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bibtex_LiteratureDb__LiteratureDb", None)
        self.__LiteratureDb = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entries"):
                opp_val = getattr(old_value, "entries", None)
                if opp_val == self:
                    setattr(old_value, "entries", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entries"):
                opp_val = getattr(value, "entries", None)
                setattr(value, "entries", self)

    @property
    def literaturedb(self):
        return self.__literaturedb

    @literaturedb.setter
    def literaturedb(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bibtex_LiteratureDb__literaturedb", None)
        self.__literaturedb = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Author"):
                    opp_val = getattr(item, "Author", None)
                    
                    if opp_val == self:
                        setattr(item, "Author", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Author"):
                    opp_val = getattr(item, "Author", None)
                    
                    setattr(item, "Author", self)
                    

    @property
    def LiteratureDb10(self):
        return self.__LiteratureDb10

    @LiteratureDb10.setter
    def LiteratureDb10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bibtex_LiteratureDb__LiteratureDb10", None)
        self.__LiteratureDb10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "author9"):
                opp_val = getattr(old_value, "author9", None)
                if opp_val == self:
                    setattr(old_value, "author9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "author9"):
                opp_val = getattr(value, "author9", None)
                setattr(value, "author9", self)

    @property
    def literaturedb2(self):
        return self.__literaturedb2

    @literaturedb2.setter
    def literaturedb2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bibtex_LiteratureDb__literaturedb2", None)
        self.__literaturedb2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Entry"):
                    opp_val = getattr(item, "Entry", None)
                    
                    if opp_val == self:
                        setattr(item, "Entry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Entry"):
                    opp_val = getattr(item, "Entry", None)
                    
                    setattr(item, "Entry", self)
                    
