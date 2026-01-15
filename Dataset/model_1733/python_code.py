from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class transientotm_TWriter:

    def __init__(self, name: str, transientotm_TWriter: "transientotm_TBook" = None, transientotm_TWriter2: "transientotm_TBook" = None):
        self.name = name
        self.transientotm_TWriter = transientotm_TWriter
        self.transientotm_TWriter2 = transientotm_TWriter2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def transientotm_TWriter(self):
        return self.__transientotm_TWriter

    @transientotm_TWriter.setter
    def transientotm_TWriter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transientotm_TWriter__transientotm_TWriter", None)
        self.__transientotm_TWriter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transientotm_TBook"):
                opp_val = getattr(old_value, "transientotm_TBook", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transientotm_TBook"):
                opp_val = getattr(value, "transientotm_TBook", None)
                if opp_val is None:
                    setattr(value, "transientotm_TBook", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def transientotm_TWriter2(self):
        return self.__transientotm_TWriter2

    @transientotm_TWriter2.setter
    def transientotm_TWriter2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transientotm_TWriter__transientotm_TWriter2", None)
        self.__transientotm_TWriter2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transientotm_TBook3"):
                opp_val = getattr(old_value, "transientotm_TBook3", None)
                if opp_val == self:
                    setattr(old_value, "transientotm_TBook3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transientotm_TBook3"):
                opp_val = getattr(value, "transientotm_TBook3", None)
                setattr(value, "transientotm_TBook3", self)

class transientotm_TBook:

    def __init__(self, title: str, transientotm_TBook: set["transientotm_TWriter"] = None, transientotm_TBook3: "transientotm_TWriter" = None):
        self.title = title
        self.transientotm_TBook = transientotm_TBook if transientotm_TBook is not None else set()
        self.transientotm_TBook3 = transientotm_TBook3
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def transientotm_TBook3(self):
        return self.__transientotm_TBook3

    @transientotm_TBook3.setter
    def transientotm_TBook3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transientotm_TBook__transientotm_TBook3", None)
        self.__transientotm_TBook3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transientotm_TWriter2"):
                opp_val = getattr(old_value, "transientotm_TWriter2", None)
                if opp_val == self:
                    setattr(old_value, "transientotm_TWriter2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transientotm_TWriter2"):
                opp_val = getattr(value, "transientotm_TWriter2", None)
                setattr(value, "transientotm_TWriter2", self)

    @property
    def transientotm_TBook(self):
        return self.__transientotm_TBook

    @transientotm_TBook.setter
    def transientotm_TBook(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transientotm_TBook__transientotm_TBook", None)
        self.__transientotm_TBook = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "transientotm_TWriter"):
                    opp_val = getattr(item, "transientotm_TWriter", None)
                    
                    if opp_val == self:
                        setattr(item, "transientotm_TWriter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "transientotm_TWriter"):
                    opp_val = getattr(item, "transientotm_TWriter", None)
                    
                    setattr(item, "transientotm_TWriter", self)
                    
