from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class hierarchy_Book:

    def __init__(self, Name: str, genre: str, hierarchy_Book: "hierarchy_Fiction" = None, hierarchy_Book7: "hierarchy_NonFiction" = None):
        self.Name = Name
        self.genre = genre
        self.hierarchy_Book = hierarchy_Book
        self.hierarchy_Book7 = hierarchy_Book7
        
    @property
    def genre(self) -> str:
        return self.__genre

    @genre.setter
    def genre(self, genre: str):
        self.__genre = genre

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def hierarchy_Book7(self):
        return self.__hierarchy_Book7

    @hierarchy_Book7.setter
    def hierarchy_Book7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hierarchy_Book__hierarchy_Book7", None)
        self.__hierarchy_Book7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hierarchy_NonFiction6"):
                opp_val = getattr(old_value, "hierarchy_NonFiction6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hierarchy_NonFiction6"):
                opp_val = getattr(value, "hierarchy_NonFiction6", None)
                if opp_val is None:
                    setattr(value, "hierarchy_NonFiction6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hierarchy_Book(self):
        return self.__hierarchy_Book

    @hierarchy_Book.setter
    def hierarchy_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hierarchy_Book__hierarchy_Book", None)
        self.__hierarchy_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hierarchy_Fiction4"):
                opp_val = getattr(old_value, "hierarchy_Fiction4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hierarchy_Fiction4"):
                opp_val = getattr(value, "hierarchy_Fiction4", None)
                if opp_val is None:
                    setattr(value, "hierarchy_Fiction4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class hierarchy_NonFiction:

    def __init__(self, Name: str, hierarchy_NonFiction: "hierarchy_HierLibrary" = None, hierarchy_NonFiction6: set["hierarchy_Book"] = None):
        self.Name = Name
        self.hierarchy_NonFiction = hierarchy_NonFiction
        self.hierarchy_NonFiction6 = hierarchy_NonFiction6 if hierarchy_NonFiction6 is not None else set()
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def hierarchy_NonFiction6(self):
        return self.__hierarchy_NonFiction6

    @hierarchy_NonFiction6.setter
    def hierarchy_NonFiction6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hierarchy_NonFiction__hierarchy_NonFiction6", None)
        self.__hierarchy_NonFiction6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hierarchy_Book7"):
                    opp_val = getattr(item, "hierarchy_Book7", None)
                    
                    if opp_val == self:
                        setattr(item, "hierarchy_Book7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hierarchy_Book7"):
                    opp_val = getattr(item, "hierarchy_Book7", None)
                    
                    setattr(item, "hierarchy_Book7", self)
                    

    @property
    def hierarchy_NonFiction(self):
        return self.__hierarchy_NonFiction

    @hierarchy_NonFiction.setter
    def hierarchy_NonFiction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hierarchy_NonFiction__hierarchy_NonFiction", None)
        self.__hierarchy_NonFiction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hierarchy_HierLibrary2"):
                opp_val = getattr(old_value, "hierarchy_HierLibrary2", None)
                if opp_val == self:
                    setattr(old_value, "hierarchy_HierLibrary2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hierarchy_HierLibrary2"):
                opp_val = getattr(value, "hierarchy_HierLibrary2", None)
                setattr(value, "hierarchy_HierLibrary2", self)

class hierarchy_Fiction:

    def __init__(self, Name: str, hierarchy_Fiction: "hierarchy_HierLibrary" = None, hierarchy_Fiction4: set["hierarchy_Book"] = None):
        self.Name = Name
        self.hierarchy_Fiction = hierarchy_Fiction
        self.hierarchy_Fiction4 = hierarchy_Fiction4 if hierarchy_Fiction4 is not None else set()
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def hierarchy_Fiction4(self):
        return self.__hierarchy_Fiction4

    @hierarchy_Fiction4.setter
    def hierarchy_Fiction4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hierarchy_Fiction__hierarchy_Fiction4", None)
        self.__hierarchy_Fiction4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hierarchy_Book"):
                    opp_val = getattr(item, "hierarchy_Book", None)
                    
                    if opp_val == self:
                        setattr(item, "hierarchy_Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hierarchy_Book"):
                    opp_val = getattr(item, "hierarchy_Book", None)
                    
                    setattr(item, "hierarchy_Book", self)
                    

    @property
    def hierarchy_Fiction(self):
        return self.__hierarchy_Fiction

    @hierarchy_Fiction.setter
    def hierarchy_Fiction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hierarchy_Fiction__hierarchy_Fiction", None)
        self.__hierarchy_Fiction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hierarchy_HierLibrary"):
                opp_val = getattr(old_value, "hierarchy_HierLibrary", None)
                if opp_val == self:
                    setattr(old_value, "hierarchy_HierLibrary", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hierarchy_HierLibrary"):
                opp_val = getattr(value, "hierarchy_HierLibrary", None)
                setattr(value, "hierarchy_HierLibrary", self)

class hierarchy_HierLibrary:

    def __init__(self, Name: str, hierarchy_HierLibrary: "hierarchy_Fiction" = None, hierarchy_HierLibrary2: "hierarchy_NonFiction" = None):
        self.Name = Name
        self.hierarchy_HierLibrary = hierarchy_HierLibrary
        self.hierarchy_HierLibrary2 = hierarchy_HierLibrary2
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def hierarchy_HierLibrary(self):
        return self.__hierarchy_HierLibrary

    @hierarchy_HierLibrary.setter
    def hierarchy_HierLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hierarchy_HierLibrary__hierarchy_HierLibrary", None)
        self.__hierarchy_HierLibrary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hierarchy_Fiction"):
                opp_val = getattr(old_value, "hierarchy_Fiction", None)
                if opp_val == self:
                    setattr(old_value, "hierarchy_Fiction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hierarchy_Fiction"):
                opp_val = getattr(value, "hierarchy_Fiction", None)
                setattr(value, "hierarchy_Fiction", self)

    @property
    def hierarchy_HierLibrary2(self):
        return self.__hierarchy_HierLibrary2

    @hierarchy_HierLibrary2.setter
    def hierarchy_HierLibrary2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hierarchy_HierLibrary__hierarchy_HierLibrary2", None)
        self.__hierarchy_HierLibrary2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hierarchy_NonFiction"):
                opp_val = getattr(old_value, "hierarchy_NonFiction", None)
                if opp_val == self:
                    setattr(old_value, "hierarchy_NonFiction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hierarchy_NonFiction"):
                opp_val = getattr(value, "hierarchy_NonFiction", None)
                setattr(value, "hierarchy_NonFiction", self)
