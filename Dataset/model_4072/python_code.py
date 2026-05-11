from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class SimpleUml_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class NamedElement:

    pass
class SimpleUml_Property(NamedElement):

    def __init__(self, primitiveType: str, isContainment: bool, SimpleUml_Property: "SimpleUml_Class" = None, SimpleUml_Property5: "SimpleUml_Class" = None):
        self.primitiveType = primitiveType
        self.isContainment = isContainment
        self.SimpleUml_Property = SimpleUml_Property
        self.SimpleUml_Property5 = SimpleUml_Property5
        
        pass
    @property
    def primitiveType(self):
        return self.__primitiveType

    @primitiveType.setter
    def primitiveType(self, primitiveType: str):
        self.__primitiveType = primitiveType


    @property
    def isContainment(self):
        return self.__isContainment

    @isContainment.setter
    def isContainment(self, isContainment: bool):
        self.__isContainment = isContainment


    @property
    def SimpleUml_Property(self):
        return self.__SimpleUml_Property

    @SimpleUml_Property.setter
    def SimpleUml_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleUml_Property__SimpleUml_Property", None)
        self.__SimpleUml_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleUml_Class"):
                opp_val = getattr(old_value, "SimpleUml_Class", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleUml_Class"):
                opp_val = getattr(value, "SimpleUml_Class", None)
                if opp_val is None:
                    setattr(value, "SimpleUml_Class", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SimpleUml_Property5(self):
        return self.__SimpleUml_Property5

    @SimpleUml_Property5.setter
    def SimpleUml_Property5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleUml_Property__SimpleUml_Property5", None)
        self.__SimpleUml_Property5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleUml_Class6"):
                opp_val = getattr(old_value, "SimpleUml_Class6", None)
                if opp_val == self:
                    setattr(old_value, "SimpleUml_Class6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleUml_Class6"):
                opp_val = getattr(value, "SimpleUml_Class6", None)
                setattr(value, "SimpleUml_Class6", self)

class SimpleUml_Package(NamedElement):

    pass
class SimpleUml_Class(NamedElement):

    pass