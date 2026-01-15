from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class clazz_BRef:

    def __init__(self, name: str, clazz_BRef: "clazz_B" = None):
        self.name = name
        self.clazz_BRef = clazz_BRef
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def clazz_BRef(self):
        return self.__clazz_BRef

    @clazz_BRef.setter
    def clazz_BRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_clazz_BRef__clazz_BRef", None)
        self.__clazz_BRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "clazz_B2"):
                opp_val = getattr(old_value, "clazz_B2", None)
                if opp_val == self:
                    setattr(old_value, "clazz_B2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "clazz_B2"):
                opp_val = getattr(value, "clazz_B2", None)
                setattr(value, "clazz_B2", self)

class clazz_Annotation:

    def __init__(self, tag: str, clazz_Annotation: "clazz_B" = None):
        self.tag = tag
        self.clazz_Annotation = clazz_Annotation
        
    @property
    def tag(self) -> str:
        return self.__tag

    @tag.setter
    def tag(self, tag: str):
        self.__tag = tag

    @property
    def clazz_Annotation(self):
        return self.__clazz_Annotation

    @clazz_Annotation.setter
    def clazz_Annotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_clazz_Annotation__clazz_Annotation", None)
        self.__clazz_Annotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "clazz_B"):
                opp_val = getattr(old_value, "clazz_B", None)
                if opp_val == self:
                    setattr(old_value, "clazz_B", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "clazz_B"):
                opp_val = getattr(value, "clazz_B", None)
                setattr(value, "clazz_B", self)

class clazz_B:

    def __init__(self, name: str, clazz_B: "clazz_Annotation" = None, clazz_B2: "clazz_BRef" = None):
        self.name = name
        self.clazz_B = clazz_B
        self.clazz_B2 = clazz_B2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def clazz_B2(self):
        return self.__clazz_B2

    @clazz_B2.setter
    def clazz_B2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_clazz_B__clazz_B2", None)
        self.__clazz_B2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "clazz_BRef"):
                opp_val = getattr(old_value, "clazz_BRef", None)
                if opp_val == self:
                    setattr(old_value, "clazz_BRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "clazz_BRef"):
                opp_val = getattr(value, "clazz_BRef", None)
                setattr(value, "clazz_BRef", self)

    @property
    def clazz_B(self):
        return self.__clazz_B

    @clazz_B.setter
    def clazz_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_clazz_B__clazz_B", None)
        self.__clazz_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "clazz_Annotation"):
                opp_val = getattr(old_value, "clazz_Annotation", None)
                if opp_val == self:
                    setattr(old_value, "clazz_Annotation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "clazz_Annotation"):
                opp_val = getattr(value, "clazz_Annotation", None)
                setattr(value, "clazz_Annotation", self)
