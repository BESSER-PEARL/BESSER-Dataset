from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Visibility(Enum):
    public = "public"
    protected = "protected"
    private = "private"


############################################
# Definition of Classes
############################################

class classes_Description:

    def __init__(self, description: str):
        self.description = description
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

class Value:

    pass
class classes_ConstantRef(Value):

    pass
class classes_IntegerLiteral(Value):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class BuiltInType:

    pass
class classes_IntegerType(BuiltInType):

    pass
class classes_StringType(BuiltInType):

    pass
class Type:

    pass
class classes_ClassRef(Type):

    pass
class classes_BuiltInType(Type):

    pass
class classes_Type:

    pass
class classes_Value:

    pass
class Description:

    pass
class classes_Attribute(Description):

    def __init__(self, visibility: str, name: str, classes_Attribute: "classes_Class" = None, classes_Attribute18: "classes_Type" = None, classes_Attribute20: "classes_Value" = None, classes_Attribute23: "classes_Value" = None):
        self.visibility = visibility
        self.name = name
        self.classes_Attribute = classes_Attribute
        self.classes_Attribute18 = classes_Attribute18
        self.classes_Attribute20 = classes_Attribute20
        self.classes_Attribute23 = classes_Attribute23
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def classes_Attribute18(self):
        return self.__classes_Attribute18

    @classes_Attribute18.setter
    def classes_Attribute18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Attribute__classes_Attribute18", None)
        self.__classes_Attribute18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_Type"):
                opp_val = getattr(old_value, "classes_Type", None)
                if opp_val == self:
                    setattr(old_value, "classes_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_Type"):
                opp_val = getattr(value, "classes_Type", None)
                setattr(value, "classes_Type", self)

    @property
    def classes_Attribute(self):
        return self.__classes_Attribute

    @classes_Attribute.setter
    def classes_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Attribute__classes_Attribute", None)
        self.__classes_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_Class16"):
                opp_val = getattr(old_value, "classes_Class16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_Class16"):
                opp_val = getattr(value, "classes_Class16", None)
                if opp_val is None:
                    setattr(value, "classes_Class16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classes_Attribute23(self):
        return self.__classes_Attribute23

    @classes_Attribute23.setter
    def classes_Attribute23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Attribute__classes_Attribute23", None)
        self.__classes_Attribute23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_Value24"):
                opp_val = getattr(old_value, "classes_Value24", None)
                if opp_val == self:
                    setattr(old_value, "classes_Value24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_Value24"):
                opp_val = getattr(value, "classes_Value24", None)
                setattr(value, "classes_Value24", self)

    @property
    def classes_Attribute20(self):
        return self.__classes_Attribute20

    @classes_Attribute20.setter
    def classes_Attribute20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Attribute__classes_Attribute20", None)
        self.__classes_Attribute20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_Value21"):
                opp_val = getattr(old_value, "classes_Value21", None)
                if opp_val == self:
                    setattr(old_value, "classes_Value21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_Value21"):
                opp_val = getattr(value, "classes_Value21", None)
                setattr(value, "classes_Value21", self)

class Content:

    pass
class classes_Association(Description, Content):

    def __init__(self, name: str, classes_Association: "classes_Class" = None, classes_Association4: "classes_Class" = None, classes_Association7: "classes_Value" = None, classes_Association10: "classes_Value" = None):
        self.name = name
        self.classes_Association = classes_Association
        self.classes_Association4 = classes_Association4
        self.classes_Association7 = classes_Association7
        self.classes_Association10 = classes_Association10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def classes_Association4(self):
        return self.__classes_Association4

    @classes_Association4.setter
    def classes_Association4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Association__classes_Association4", None)
        self.__classes_Association4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_Class5"):
                opp_val = getattr(old_value, "classes_Class5", None)
                if opp_val == self:
                    setattr(old_value, "classes_Class5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_Class5"):
                opp_val = getattr(value, "classes_Class5", None)
                setattr(value, "classes_Class5", self)

    @property
    def classes_Association(self):
        return self.__classes_Association

    @classes_Association.setter
    def classes_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Association__classes_Association", None)
        self.__classes_Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_Class"):
                opp_val = getattr(old_value, "classes_Class", None)
                if opp_val == self:
                    setattr(old_value, "classes_Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_Class"):
                opp_val = getattr(value, "classes_Class", None)
                setattr(value, "classes_Class", self)

    @property
    def classes_Association7(self):
        return self.__classes_Association7

    @classes_Association7.setter
    def classes_Association7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Association__classes_Association7", None)
        self.__classes_Association7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_Value8"):
                opp_val = getattr(old_value, "classes_Value8", None)
                if opp_val == self:
                    setattr(old_value, "classes_Value8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_Value8"):
                opp_val = getattr(value, "classes_Value8", None)
                setattr(value, "classes_Value8", self)

    @property
    def classes_Association10(self):
        return self.__classes_Association10

    @classes_Association10.setter
    def classes_Association10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Association__classes_Association10", None)
        self.__classes_Association10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_Value11"):
                opp_val = getattr(old_value, "classes_Value11", None)
                if opp_val == self:
                    setattr(old_value, "classes_Value11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_Value11"):
                opp_val = getattr(value, "classes_Value11", None)
                setattr(value, "classes_Value11", self)

class classes_Class(Description, Content):

    def __init__(self, name: str, classes_Class16: set["classes_Attribute"] = None, classes_Class26: "classes_ClassRef" = None, classes_Class: "classes_Association" = None, classes_Class5: "classes_Association" = None, classes_Class14: "classes_Class" = None, classes_Class12: set["classes_Class"] = None):
        self.name = name
        self.classes_Class16 = classes_Class16 if classes_Class16 is not None else set()
        self.classes_Class26 = classes_Class26
        self.classes_Class = classes_Class
        self.classes_Class5 = classes_Class5
        self.classes_Class14 = classes_Class14
        self.classes_Class12 = classes_Class12 if classes_Class12 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def classes_Class26(self):
        return self.__classes_Class26

    @classes_Class26.setter
    def classes_Class26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Class__classes_Class26", None)
        self.__classes_Class26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_ClassRef"):
                opp_val = getattr(old_value, "classes_ClassRef", None)
                if opp_val == self:
                    setattr(old_value, "classes_ClassRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_ClassRef"):
                opp_val = getattr(value, "classes_ClassRef", None)
                setattr(value, "classes_ClassRef", self)

    @property
    def classes_Class5(self):
        return self.__classes_Class5

    @classes_Class5.setter
    def classes_Class5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Class__classes_Class5", None)
        self.__classes_Class5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_Association4"):
                opp_val = getattr(old_value, "classes_Association4", None)
                if opp_val == self:
                    setattr(old_value, "classes_Association4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_Association4"):
                opp_val = getattr(value, "classes_Association4", None)
                setattr(value, "classes_Association4", self)

    @property
    def classes_Class12(self):
        return self.__classes_Class12

    @classes_Class12.setter
    def classes_Class12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Class__classes_Class12", None)
        self.__classes_Class12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classes_Class14"):
                    opp_val = getattr(item, "classes_Class14", None)
                    
                    if opp_val == self:
                        setattr(item, "classes_Class14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classes_Class14"):
                    opp_val = getattr(item, "classes_Class14", None)
                    
                    setattr(item, "classes_Class14", self)
                    

    @property
    def classes_Class14(self):
        return self.__classes_Class14

    @classes_Class14.setter
    def classes_Class14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Class__classes_Class14", None)
        self.__classes_Class14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_Class12"):
                opp_val = getattr(old_value, "classes_Class12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_Class12"):
                opp_val = getattr(value, "classes_Class12", None)
                if opp_val is None:
                    setattr(value, "classes_Class12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classes_Class16(self):
        return self.__classes_Class16

    @classes_Class16.setter
    def classes_Class16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Class__classes_Class16", None)
        self.__classes_Class16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classes_Attribute"):
                    opp_val = getattr(item, "classes_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "classes_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classes_Attribute"):
                    opp_val = getattr(item, "classes_Attribute", None)
                    
                    setattr(item, "classes_Attribute", self)
                    

    @property
    def classes_Class(self):
        return self.__classes_Class

    @classes_Class.setter
    def classes_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Class__classes_Class", None)
        self.__classes_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_Association"):
                opp_val = getattr(old_value, "classes_Association", None)
                if opp_val == self:
                    setattr(old_value, "classes_Association", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_Association"):
                opp_val = getattr(value, "classes_Association", None)
                setattr(value, "classes_Association", self)

class classes_Constant(Description, Content):

    def __init__(self, name: str, classes_Constant: "classes_Value" = None, classes_Constant28: "classes_ConstantRef" = None):
        self.name = name
        self.classes_Constant = classes_Constant
        self.classes_Constant28 = classes_Constant28
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def classes_Constant(self):
        return self.__classes_Constant

    @classes_Constant.setter
    def classes_Constant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Constant__classes_Constant", None)
        self.__classes_Constant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_Value"):
                opp_val = getattr(old_value, "classes_Value", None)
                if opp_val == self:
                    setattr(old_value, "classes_Value", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_Value"):
                opp_val = getattr(value, "classes_Value", None)
                setattr(value, "classes_Value", self)

    @property
    def classes_Constant28(self):
        return self.__classes_Constant28

    @classes_Constant28.setter
    def classes_Constant28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classes_Constant__classes_Constant28", None)
        self.__classes_Constant28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes_ConstantRef"):
                opp_val = getattr(old_value, "classes_ConstantRef", None)
                if opp_val == self:
                    setattr(old_value, "classes_ConstantRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes_ConstantRef"):
                opp_val = getattr(value, "classes_ConstantRef", None)
                setattr(value, "classes_ConstantRef", self)

class classes_Content:

    pass
class classes_ClassModel:

    pass