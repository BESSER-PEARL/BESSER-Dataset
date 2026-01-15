from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class style_StylePointer:

    pass
class style_StyleSet:

    def __init__(self, uid: str, name: str, style_StyleSet: "style_StyleLibrary" = None):
        self.uid = uid
        self.name = name
        self.style_StyleSet = style_StyleSet
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def style_StyleSet(self):
        return self.__style_StyleSet

    @style_StyleSet.setter
    def style_StyleSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_style_StyleSet__style_StyleSet", None)
        self.__style_StyleSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "style_StyleLibrary"):
                opp_val = getattr(old_value, "style_StyleLibrary", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "style_StyleLibrary"):
                opp_val = getattr(value, "style_StyleLibrary", None)
                if opp_val is None:
                    setattr(value, "style_StyleLibrary", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class style_StyleLibrary:

    def __init__(self, uid: str, name: str, style_StyleLibrary: set["style_StyleSet"] = None, style_StyleLibrary2: "style_StylePointer" = None):
        self.uid = uid
        self.name = name
        self.style_StyleLibrary = style_StyleLibrary if style_StyleLibrary is not None else set()
        self.style_StyleLibrary2 = style_StyleLibrary2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def style_StyleLibrary(self):
        return self.__style_StyleLibrary

    @style_StyleLibrary.setter
    def style_StyleLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_style_StyleLibrary__style_StyleLibrary", None)
        self.__style_StyleLibrary = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "style_StyleSet"):
                    opp_val = getattr(item, "style_StyleSet", None)
                    
                    if opp_val == self:
                        setattr(item, "style_StyleSet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "style_StyleSet"):
                    opp_val = getattr(item, "style_StyleSet", None)
                    
                    setattr(item, "style_StyleSet", self)
                    

    @property
    def style_StyleLibrary2(self):
        return self.__style_StyleLibrary2

    @style_StyleLibrary2.setter
    def style_StyleLibrary2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_style_StyleLibrary__style_StyleLibrary2", None)
        self.__style_StyleLibrary2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "style_StylePointer"):
                opp_val = getattr(old_value, "style_StylePointer", None)
                if opp_val == self:
                    setattr(old_value, "style_StylePointer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "style_StylePointer"):
                opp_val = getattr(value, "style_StylePointer", None)
                setattr(value, "style_StylePointer", self)
