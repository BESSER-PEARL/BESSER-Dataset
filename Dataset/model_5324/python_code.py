from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class subPackage_Foo:

    pass
class subsub_Bar:

    pass
class myPackage_subsub_Baz(subsub_Bar, subPackage_Foo):

    pass
class myPackage_subsub_Bar:

    def __init__(self, s: str):
        self.s = s
        
    @property
    def s(self) -> str:
        return self.__s

    @s.setter
    def s(self, s: str):
        self.__s = s

class MyClass:

    pass
class myPackage_subPackage_Foo(MyClass):

    pass
class myPackage_AThirdClass(MyClass):

    def __init__(self, thirdAttribute: str):
        self.thirdAttribute = thirdAttribute
        
    @property
    def thirdAttribute(self) -> str:
        return self.__thirdAttribute

    @thirdAttribute.setter
    def thirdAttribute(self, thirdAttribute: str):
        self.__thirdAttribute = thirdAttribute

class myPackage_MyOtherClass:

    def __init__(self, otherAttribute: str, myPackage_MyOtherClass: "myPackage_MyClass" = None):
        self.otherAttribute = otherAttribute
        self.myPackage_MyOtherClass = myPackage_MyOtherClass
        
    @property
    def otherAttribute(self) -> str:
        return self.__otherAttribute

    @otherAttribute.setter
    def otherAttribute(self, otherAttribute: str):
        self.__otherAttribute = otherAttribute

    @property
    def myPackage_MyOtherClass(self):
        return self.__myPackage_MyOtherClass

    @myPackage_MyOtherClass.setter
    def myPackage_MyOtherClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myPackage_MyOtherClass__myPackage_MyOtherClass", None)
        self.__myPackage_MyOtherClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myPackage_MyClass"):
                opp_val = getattr(old_value, "myPackage_MyClass", None)
                if opp_val == self:
                    setattr(old_value, "myPackage_MyClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myPackage_MyClass"):
                opp_val = getattr(value, "myPackage_MyClass", None)
                setattr(value, "myPackage_MyClass", self)

class myPackage_MyClass:

    def __init__(self, myAttribute: str, myPackage_MyClass: "myPackage_MyOtherClass" = None):
        self.myAttribute = myAttribute
        self.myPackage_MyClass = myPackage_MyClass
        
    @property
    def myAttribute(self) -> str:
        return self.__myAttribute

    @myAttribute.setter
    def myAttribute(self, myAttribute: str):
        self.__myAttribute = myAttribute

    @property
    def myPackage_MyClass(self):
        return self.__myPackage_MyClass

    @myPackage_MyClass.setter
    def myPackage_MyClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myPackage_MyClass__myPackage_MyClass", None)
        self.__myPackage_MyClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myPackage_MyOtherClass"):
                opp_val = getattr(old_value, "myPackage_MyOtherClass", None)
                if opp_val == self:
                    setattr(old_value, "myPackage_MyOtherClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myPackage_MyOtherClass"):
                opp_val = getattr(value, "myPackage_MyOtherClass", None)
                setattr(value, "myPackage_MyOtherClass", self)
