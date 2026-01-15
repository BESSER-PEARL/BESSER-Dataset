from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class library_OclLibrary:

    def __init__(self, name: str, library_OclLibrary: set["library_OclExpression"] = None):
        self.name = name
        self.library_OclLibrary = library_OclLibrary if library_OclLibrary is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def library_OclLibrary(self):
        return self.__library_OclLibrary

    @library_OclLibrary.setter
    def library_OclLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_OclLibrary__library_OclLibrary", None)
        self.__library_OclLibrary = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_OclExpression"):
                    opp_val = getattr(item, "library_OclExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "library_OclExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_OclExpression"):
                    opp_val = getattr(item, "library_OclExpression", None)
                    
                    setattr(item, "library_OclExpression", self)
                    

class library_OclExpression:

    def __init__(self, name: str, description: str, query: str, context: str, library_OclExpression: "library_OclLibrary" = None):
        self.name = name
        self.description = description
        self.query = query
        self.context = context
        self.library_OclExpression = library_OclExpression
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def query(self) -> str:
        return self.__query

    @query.setter
    def query(self, query: str):
        self.__query = query

    @property
    def context(self) -> str:
        return self.__context

    @context.setter
    def context(self, context: str):
        self.__context = context

    @property
    def library_OclExpression(self):
        return self.__library_OclExpression

    @library_OclExpression.setter
    def library_OclExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_OclExpression__library_OclExpression", None)
        self.__library_OclExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_OclLibrary"):
                opp_val = getattr(old_value, "library_OclLibrary", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_OclLibrary"):
                opp_val = getattr(value, "library_OclLibrary", None)
                if opp_val is None:
                    setattr(value, "library_OclLibrary", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
