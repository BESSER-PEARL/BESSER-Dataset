from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class MyClass37:

    pass


class MyClass36:

    pass


class MyClass35:

    pass


class MyClass34:

    pass


class MyClass33:

    pass


class MyClass32:

    pass


class MyClass6:

    pass


class MyClass5:

    pass


class MyClass4:

    pass


class MyClass3:

    pass


class MyClass2:

    pass


class sfbsdf:

    pass


class MyClass:

    def __init__(self, TenCoSo: str, attribute: str, attribute2: str, attribute3: str, MyClass_sfbsdf_00: "sfbsdf" = None):
        self.TenCoSo = TenCoSo
        self.attribute = attribute
        self.attribute2 = attribute2
        self.attribute3 = attribute3
        self.MyClass_sfbsdf_00 = MyClass_sfbsdf_00
        
        pass
    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def attribute3(self):
        return self.__attribute3
    @attribute3.setter
    def attribute3(self, attribute3: str):
        self.__attribute3 = attribute3

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def TenCoSo(self):
        return self.__TenCoSo
    @TenCoSo.setter
    def TenCoSo(self, TenCoSo: str):
        self.__TenCoSo = TenCoSo

    @property
    def MyClass_sfbsdf_00(self):
        return self.__MyClass_sfbsdf_00
    @MyClass_sfbsdf_00.setter
    def MyClass_sfbsdf_00(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MyClass__MyClass_sfbsdf_00", None)
        self.__MyClass_sfbsdf_00 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MyClass_sfbsdf_11"):
                opp_val = getattr(old_value, "MyClass_sfbsdf_11", None)
                if opp_val == self:
                    setattr(old_value, "MyClass_sfbsdf_11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MyClass_sfbsdf_11"):
                opp_val = getattr(value, "MyClass_sfbsdf_11", None)
                setattr(value, "MyClass_sfbsdf_11", self)

