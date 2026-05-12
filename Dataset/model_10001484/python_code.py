from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Class4:

    def __init__(self, attribute: str, class23: "vcx" = None):
        self.attribute = attribute
        self.class23 = class23
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def class23(self):
        return self.__class23
    @class23.setter
    def class23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Class4__class23", None)
        self.__class23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class42"):
                opp_val = getattr(old_value, "class42", None)
                if opp_val == self:
                    setattr(old_value, "class42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class42"):
                opp_val = getattr(value, "class42", None)
                setattr(value, "class42", self)



class vcx:

    def __init__(self, attribute: bool, attribute2: str, class42: "Class4" = None, vvvv4: "vvvv" = None, classqwe6: "cgv_Classqwe" = None):
        self.attribute = attribute
        self.attribute2 = attribute2
        self.class42 = class42
        self.vvvv4 = vvvv4
        self.classqwe6 = classqwe6
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: bool):
        self.__attribute = attribute

    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def vvvv4(self):
        return self.__vvvv4
    @vvvv4.setter
    def vvvv4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcx__vvvv4", None)
        self.__vvvv4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class25"):
                opp_val = getattr(old_value, "class25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class25"):
                opp_val = getattr(value, "class25", None)
                if opp_val is None:
                    setattr(value, "class25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def class42(self):
        return self.__class42
    @class42.setter
    def class42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcx__class42", None)
        self.__class42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class23"):
                opp_val = getattr(old_value, "class23", None)
                if opp_val == self:
                    setattr(old_value, "class23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class23"):
                opp_val = getattr(value, "class23", None)
                setattr(value, "class23", self)

    @property
    def classqwe6(self):
        return self.__classqwe6
    @classqwe6.setter
    def classqwe6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vcx__classqwe6", None)
        self.__classqwe6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class27"):
                opp_val = getattr(old_value, "class27", None)
                if opp_val == self:
                    setattr(old_value, "class27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class27"):
                opp_val = getattr(value, "class27", None)
                setattr(value, "class27", self)



class Class:

    pass


class ccc:

    def __init__(self, qwe: str, c20: "aaa" = None):
        self.qwe = qwe
        self.c20 = c20
        
        pass
    @property
    def qwe(self):
        return self.__qwe
    @qwe.setter
    def qwe(self, qwe: str):
        self.__qwe = qwe

    @property
    def c20(self):
        return self.__c20
    @c20.setter
    def c20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccc__c20", None)
        self.__c20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c31"):
                opp_val = getattr(old_value, "c31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c31"):
                opp_val = getattr(value, "c31", None)
                if opp_val is None:
                    setattr(value, "c31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class aaa:

    def __init__(self, attribute: bool, qwe: aaa, c31: set["ccc"] = None):
        self.attribute = attribute
        self.qwe = qwe
        self.c31 = c31 if c31 is not None else set()
        
        pass
    @property
    def qwe(self):
        return self.__qwe
    @qwe.setter
    def qwe(self, qwe: aaa):
        self.__qwe = qwe

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: bool):
        self.__attribute = attribute

    @property
    def c31(self):
        return self.__c31
    @c31.setter
    def c31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aaa__c31", None)
        self.__c31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "c20"):
                    opp_val = getattr(item, "c20", None)
                    
                    if opp_val == self:
                        setattr(item, "c20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "c20"):
                    opp_val = getattr(item, "c20", None)
                    
                    setattr(item, "c20", self)
                    



class vvvv:

    def __init__(self, zsxc: int, class25: set["vcx"] = None):
        self.zsxc = zsxc
        self.class25 = class25 if class25 is not None else set()
        
        pass
    @property
    def zsxc(self):
        return self.__zsxc
    @zsxc.setter
    def zsxc(self, zsxc: int):
        self.__zsxc = zsxc

    @property
    def class25(self):
        return self.__class25
    @class25.setter
    def class25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vvvv__class25", None)
        self.__class25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vvvv4"):
                    opp_val = getattr(item, "vvvv4", None)
                    
                    if opp_val == self:
                        setattr(item, "vvvv4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vvvv4"):
                    opp_val = getattr(item, "vvvv4", None)
                    
                    setattr(item, "vvvv4", self)
                    



class cgv_Classqwe:

    def __init__(self, qw: aaa, class27: "vcx" = None):
        self.qw = qw
        self.class27 = class27
        
        pass
    @property
    def qw(self):
        return self.__qw
    @qw.setter
    def qw(self, qw: aaa):
        self.__qw = qw

    @property
    def class27(self):
        return self.__class27
    @class27.setter
    def class27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cgv_Classqwe__class27", None)
        self.__class27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classqwe6"):
                opp_val = getattr(old_value, "classqwe6", None)
                if opp_val == self:
                    setattr(old_value, "classqwe6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classqwe6"):
                opp_val = getattr(value, "classqwe6", None)
                setattr(value, "classqwe6", self)

