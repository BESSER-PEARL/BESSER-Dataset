from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Model:

    pass
class TypedElement:

    pass
class testmodel_Attribute(TypedElement):

    pass
class ModelElement:

    pass
class testmodel_Association(ModelElement):

    def __init__(self, firstLabel: str, secondLabel: str, testmodel_Association: "testmodel_Class" = None, testmodel_Association7: "testmodel_Class" = None):
        self.firstLabel = firstLabel
        self.secondLabel = secondLabel
        self.testmodel_Association = testmodel_Association
        self.testmodel_Association7 = testmodel_Association7
        
    @property
    def firstLabel(self) -> str:
        return self.__firstLabel

    @firstLabel.setter
    def firstLabel(self, firstLabel: str):
        self.__firstLabel = firstLabel

    @property
    def secondLabel(self) -> str:
        return self.__secondLabel

    @secondLabel.setter
    def secondLabel(self, secondLabel: str):
        self.__secondLabel = secondLabel

    @property
    def testmodel_Association7(self):
        return self.__testmodel_Association7

    @testmodel_Association7.setter
    def testmodel_Association7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmodel_Association__testmodel_Association7", None)
        self.__testmodel_Association7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testmodel_Class8"):
                opp_val = getattr(old_value, "testmodel_Class8", None)
                if opp_val == self:
                    setattr(old_value, "testmodel_Class8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testmodel_Class8"):
                opp_val = getattr(value, "testmodel_Class8", None)
                setattr(value, "testmodel_Class8", self)

    @property
    def testmodel_Association(self):
        return self.__testmodel_Association

    @testmodel_Association.setter
    def testmodel_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmodel_Association__testmodel_Association", None)
        self.__testmodel_Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testmodel_Class5"):
                opp_val = getattr(old_value, "testmodel_Class5", None)
                if opp_val == self:
                    setattr(old_value, "testmodel_Class5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testmodel_Class5"):
                opp_val = getattr(value, "testmodel_Class5", None)
                setattr(value, "testmodel_Class5", self)

class testmodel_Group(ModelElement, Model):

    pass
class testmodel_Class(ModelElement):

    pass
class NamedElement:

    pass
class testmodel_TypedElement(NamedElement):

    pass
class testmodel_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class testmodel_ModelElement(NamedElement):

    pass
class testmodel_Model:

    pass