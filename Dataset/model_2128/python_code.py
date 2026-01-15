from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class tTCTest_Propose_Refactoring:

    pass
class Condition:

    pass
class tTCTest_Expect_False(Condition):

    pass
class tTCTest_Expect_True(Condition):

    pass
class tTCTest_Warning:

    def __init__(self, message: str, tTCTest_Warning: "tTCTest_Condition" = None):
        self.message = message
        self.tTCTest_Warning = tTCTest_Warning
        
    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def tTCTest_Warning(self):
        return self.__tTCTest_Warning

    @tTCTest_Warning.setter
    def tTCTest_Warning(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tTCTest_Warning__tTCTest_Warning", None)
        self.__tTCTest_Warning = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tTCTest_Condition44"):
                opp_val = getattr(old_value, "tTCTest_Condition44", None)
                if opp_val == self:
                    setattr(old_value, "tTCTest_Condition44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tTCTest_Condition44"):
                opp_val = getattr(value, "tTCTest_Condition44", None)
                setattr(value, "tTCTest_Condition44", self)

class Implementation:

    pass
class tTCTest_Implements_Not(Implementation):

    pass
class tTCTest_Implements(Implementation):

    pass
class Containment:

    pass
class tTCTest_Contains_Not(Containment):

    pass
class tTCTest_Contains(Containment):

    pass
class tTCTest_Class_Element:

    def __init__(self, name: str, tTCTest_Class_Element: "tTCTest_Containment" = None):
        self.name = name
        self.tTCTest_Class_Element = tTCTest_Class_Element
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tTCTest_Class_Element(self):
        return self.__tTCTest_Class_Element

    @tTCTest_Class_Element.setter
    def tTCTest_Class_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tTCTest_Class_Element__tTCTest_Class_Element", None)
        self.__tTCTest_Class_Element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tTCTest_Containment53"):
                opp_val = getattr(old_value, "tTCTest_Containment53", None)
                if opp_val == self:
                    setattr(old_value, "tTCTest_Containment53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tTCTest_Containment53"):
                opp_val = getattr(value, "tTCTest_Containment53", None)
                setattr(value, "tTCTest_Containment53", self)

class Propose_Refactoring:

    pass
class tTCTest_Propose_Create_Superclass_Refactoring(Propose_Refactoring):

    pass
class tTCTest_Propose_Pullup_Method_Refactoring(Propose_Refactoring):

    pass
class Refactoring_Instance:

    pass
class tTCTest_Pull_Up_Refactoring(Refactoring_Instance):

    pass
class tTCTest_Refactoring:

    pass
class Refactoring:

    pass
class tTCTest_No_Refactoring(Refactoring):

    pass
class tTCTest_Test_Flow:

    pass
class Assertion:

    pass
class tTCTest_Assert_True(Assertion):

    pass
class tTCTest_Assert_False(Assertion):

    pass
class Test_Step_Element:

    pass
class tTCTest_Implementation(Test_Step_Element):

    pass
class tTCTest_Compile(Test_Step_Element):

    pass
class tTCTest_Condition(Test_Step_Element):

    pass
class tTCTest_Synchronize(Test_Step_Element):

    pass
class tTCTest_Containment(Test_Step_Element):

    pass
class tTCTest_Assertion(Test_Step_Element):

    pass
class tTCTest_Test_Step(Test_Step_Element):

    pass
class tTCTest_Test_Step_Element:

    pass
class tTCTest_Create_Superclass_Refactoring(Refactoring_Instance):

    pass
class tTCTest_Refactoring_Instance(Refactoring):

    def __init__(self, name: str, tTCTest_Refactoring_Instance: "tTCTest_Test_File" = None):
        self.name = name
        self.tTCTest_Refactoring_Instance = tTCTest_Refactoring_Instance
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tTCTest_Refactoring_Instance(self):
        return self.__tTCTest_Refactoring_Instance

    @tTCTest_Refactoring_Instance.setter
    def tTCTest_Refactoring_Instance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tTCTest_Refactoring_Instance__tTCTest_Refactoring_Instance", None)
        self.__tTCTest_Refactoring_Instance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tTCTest_Test_File8"):
                opp_val = getattr(old_value, "tTCTest_Test_File8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tTCTest_Test_File8"):
                opp_val = getattr(value, "tTCTest_Test_File8", None)
                if opp_val is None:
                    setattr(value, "tTCTest_Test_File8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tTCTest_Classes:

    def __init__(self, name: str, tTCTest_Classes10: set["tTCTest_Java_Class"] = None, tTCTest_Classes: "tTCTest_Test_File" = None, tTCTest_Classes29: "tTCTest_Create_Superclass_Refactoring" = None):
        self.name = name
        self.tTCTest_Classes10 = tTCTest_Classes10 if tTCTest_Classes10 is not None else set()
        self.tTCTest_Classes = tTCTest_Classes
        self.tTCTest_Classes29 = tTCTest_Classes29
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tTCTest_Classes10(self):
        return self.__tTCTest_Classes10

    @tTCTest_Classes10.setter
    def tTCTest_Classes10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tTCTest_Classes__tTCTest_Classes10", None)
        self.__tTCTest_Classes10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tTCTest_Java_Class11"):
                    opp_val = getattr(item, "tTCTest_Java_Class11", None)
                    
                    if opp_val == self:
                        setattr(item, "tTCTest_Java_Class11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tTCTest_Java_Class11"):
                    opp_val = getattr(item, "tTCTest_Java_Class11", None)
                    
                    setattr(item, "tTCTest_Java_Class11", self)
                    

    @property
    def tTCTest_Classes(self):
        return self.__tTCTest_Classes

    @tTCTest_Classes.setter
    def tTCTest_Classes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tTCTest_Classes__tTCTest_Classes", None)
        self.__tTCTest_Classes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tTCTest_Test_File4"):
                opp_val = getattr(old_value, "tTCTest_Test_File4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tTCTest_Test_File4"):
                opp_val = getattr(value, "tTCTest_Test_File4", None)
                if opp_val is None:
                    setattr(value, "tTCTest_Test_File4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tTCTest_Classes29(self):
        return self.__tTCTest_Classes29

    @tTCTest_Classes29.setter
    def tTCTest_Classes29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tTCTest_Classes__tTCTest_Classes29", None)
        self.__tTCTest_Classes29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tTCTest_Create_Superclass_Refactoring"):
                opp_val = getattr(old_value, "tTCTest_Create_Superclass_Refactoring", None)
                if opp_val == self:
                    setattr(old_value, "tTCTest_Create_Superclass_Refactoring", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tTCTest_Create_Superclass_Refactoring"):
                opp_val = getattr(value, "tTCTest_Create_Superclass_Refactoring", None)
                setattr(value, "tTCTest_Create_Superclass_Refactoring", self)

class tTCTest_Java_Class:

    def __init__(self, name: str, package: str, class_name: str, tTCTest_Java_Class11: "tTCTest_Classes" = None, tTCTest_Java_Class14: "tTCTest_Java_Method" = None, tTCTest_Java_Class18: "tTCTest_Java_Field" = None, tTCTest_Java_Class: "tTCTest_Test_File" = None, tTCTest_Java_Class24: "tTCTest_Pull_Up_Refactoring" = None, tTCTest_Java_Class32: "tTCTest_Create_Superclass_Refactoring" = None, tTCTest_Java_Class51: "tTCTest_Containment" = None, tTCTest_Java_Class55: "tTCTest_Implementation" = None, tTCTest_Java_Class58: "tTCTest_Implementation" = None):
        self.name = name
        self.package = package
        self.class_name = class_name
        self.tTCTest_Java_Class11 = tTCTest_Java_Class11
        self.tTCTest_Java_Class14 = tTCTest_Java_Class14
        self.tTCTest_Java_Class18 = tTCTest_Java_Class18
        self.tTCTest_Java_Class = tTCTest_Java_Class
        self.tTCTest_Java_Class24 = tTCTest_Java_Class24
        self.tTCTest_Java_Class32 = tTCTest_Java_Class32
        self.tTCTest_Java_Class51 = tTCTest_Java_Class51
        self.tTCTest_Java_Class55 = tTCTest_Java_Class55
        self.tTCTest_Java_Class58 = tTCTest_Java_Class58
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def package(self) -> str:
        return self.__package

    @package.setter
    def package(self, package: str):
        self.__package = package

    @property
    def class_name(self) -> str:
        return self.__class_name

    @class_name.setter
    def class_name(self, class_name: str):
        self.__class_name = class_name

    @property
    def tTCTest_Java_Class51(self):
        return self.__tTCTest_Java_Class51

    @tTCTest_Java_Class51.setter
    def tTCTest_Java_Class51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tTCTest_Java_Class__tTCTest_Java_Class51", None)
        self.__tTCTest_Java_Class51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tTCTest_Containment"):
                opp_val = getattr(old_value, "tTCTest_Containment", None)
                if opp_val == self:
                    setattr(old_value, "tTCTest_Containment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tTCTest_Containment"):
                opp_val = getattr(value, "tTCTest_Containment", None)
                setattr(value, "tTCTest_Containment", self)

    @property
    def tTCTest_Java_Class11(self):
        return self.__tTCTest_Java_Class11

    @tTCTest_Java_Class11.setter
    def tTCTest_Java_Class11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tTCTest_Java_Class__tTCTest_Java_Class11", None)
        self.__tTCTest_Java_Class11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tTCTest_Classes10"):
                opp_val = getattr(old_value, "tTCTest_Classes10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tTCTest_Classes10"):
                opp_val = getattr(value, "tTCTest_Classes10", None)
                if opp_val is None:
                    setattr(value, "tTCTest_Classes10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tTCTest_Java_Class58(self):
        return self.__tTCTest_Java_Class58

    @tTCTest_Java_Class58.setter
    def tTCTest_Java_Class58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tTCTest_Java_Class__tTCTest_Java_Class58", None)
        self.__tTCTest_Java_Class58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tTCTest_Implementation57"):
                opp_val = getattr(old_value, "tTCTest_Implementation57", None)
                if opp_val == self:
                    setattr(old_value, "tTCTest_Implementation57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tTCTest_Implementation57"):
                opp_val = getattr(value, "tTCTest_Implementation57", None)
                setattr(value, "tTCTest_Implementation57", self)

    @property
    def tTCTest_Java_Class24(self):
        return self.__tTCTest_Java_Class24

    @tTCTest_Java_Class24.setter
    def tTCTest_Java_Class24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tTCTest_Java_Class__tTCTest_Java_Class24", None)
        self.__tTCTest_Java_Class24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tTCTest_Pull_Up_Refactoring"):
                opp_val = getattr(old_value, "tTCTest_Pull_Up_Refactoring", None)
                if opp_val == self:
                    setattr(old_value, "tTCTest_Pull_Up_Refactoring", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tTCTest_Pull_Up_Refactoring"):
                opp_val = getattr(value, "tTCTest_Pull_Up_Refactoring", None)
                setattr(value, "tTCTest_Pull_Up_Refactoring", self)

    @property
    def tTCTest_Java_Class14(self):
        return self.__tTCTest_Java_Class14

    @tTCTest_Java_Class14.setter
    def tTCTest_Java_Class14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tTCTest_Java_Class__tTCTest_Java_Class14", None)
        self.__tTCTest_Java_Class14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tTCTest_Java_Method13"):
                opp_val = getattr(old_value, "tTCTest_Java_Method13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tTCTest_Java_Method13"):
                opp_val = getattr(value, "tTCTest_Java_Method13", None)
                if opp_val is None:
                    setattr(value, "tTCTest_Java_Method13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tTCTest_Java_Class18(self):
        return self.__tTCTest_Java_Class18

    @tTCTest_Java_Class18.setter
    def tTCTest_Java_Class18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tTCTest_Java_Class__tTCTest_Java_Class18", None)
        self.__tTCTest_Java_Class18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tTCTest_Java_Field"):
                opp_val = getattr(old_value, "tTCTest_Java_Field", None)
                if opp_val == self:
                    setattr(old_value, "tTCTest_Java_Field", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tTCTest_Java_Field"):
                opp_val = getattr(value, "tTCTest_Java_Field", None)
                setattr(value, "tTCTest_Java_Field", self)

    @property
    def tTCTest_Java_Class32(self):
        return self.__tTCTest_Java_Class32

    @tTCTest_Java_Class32.setter
    def tTCTest_Java_Class32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tTCTest_Java_Class__tTCTest_Java_Class32", None)
        self.__tTCTest_Java_Class32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tTCTest_Create_Superclass_Refactoring31"):
                opp_val = getattr(old_value, "tTCTest_Create_Superclass_Refactoring31", None)
                if opp_val == self:
                    setattr(old_value, "tTCTest_Create_Superclass_Refactoring31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tTCTest_Create_Superclass_Refactoring31"):
                opp_val = getattr(value, "tTCTest_Create_Superclass_Refactoring31", None)
                setattr(value, "tTCTest_Create_Superclass_Refactoring31", self)

    @property
    def tTCTest_Java_Class(self):
        return self.__tTCTest_Java_Class

    @tTCTest_Java_Class.setter
    def tTCTest_Java_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tTCTest_Java_Class__tTCTest_Java_Class", None)
        self.__tTCTest_Java_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tTCTest_Test_File2"):
                opp_val = getattr(old_value, "tTCTest_Test_File2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tTCTest_Test_File2"):
                opp_val = getattr(value, "tTCTest_Test_File2", None)
                if opp_val is None:
                    setattr(value, "tTCTest_Test_File2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tTCTest_Java_Class55(self):
        return self.__tTCTest_Java_Class55

    @tTCTest_Java_Class55.setter
    def tTCTest_Java_Class55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tTCTest_Java_Class__tTCTest_Java_Class55", None)
        self.__tTCTest_Java_Class55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tTCTest_Implementation"):
                opp_val = getattr(old_value, "tTCTest_Implementation", None)
                if opp_val == self:
                    setattr(old_value, "tTCTest_Implementation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tTCTest_Implementation"):
                opp_val = getattr(value, "tTCTest_Implementation", None)
                setattr(value, "tTCTest_Implementation", self)

class tTCTest_Test_Case:

    def __init__(self, name: str, description: str, java_program: str, tTCTest_Test_Case: "tTCTest_Test_File" = None, tTCTest_Test_Case22: "tTCTest_Test_Flow" = None):
        self.name = name
        self.description = description
        self.java_program = java_program
        self.tTCTest_Test_Case = tTCTest_Test_Case
        self.tTCTest_Test_Case22 = tTCTest_Test_Case22
        
    @property
    def java_program(self) -> str:
        return self.__java_program

    @java_program.setter
    def java_program(self, java_program: str):
        self.__java_program = java_program

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def tTCTest_Test_Case(self):
        return self.__tTCTest_Test_Case

    @tTCTest_Test_Case.setter
    def tTCTest_Test_Case(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tTCTest_Test_Case__tTCTest_Test_Case", None)
        self.__tTCTest_Test_Case = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tTCTest_Test_File"):
                opp_val = getattr(old_value, "tTCTest_Test_File", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tTCTest_Test_File"):
                opp_val = getattr(value, "tTCTest_Test_File", None)
                if opp_val is None:
                    setattr(value, "tTCTest_Test_File", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tTCTest_Test_Case22(self):
        return self.__tTCTest_Test_Case22

    @tTCTest_Test_Case22.setter
    def tTCTest_Test_Case22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tTCTest_Test_Case__tTCTest_Test_Case22", None)
        self.__tTCTest_Test_Case22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tTCTest_Test_Flow"):
                opp_val = getattr(old_value, "tTCTest_Test_Flow", None)
                if opp_val == self:
                    setattr(old_value, "tTCTest_Test_Flow", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tTCTest_Test_Flow"):
                opp_val = getattr(value, "tTCTest_Test_Flow", None)
                setattr(value, "tTCTest_Test_Flow", self)

class tTCTest_Test_File:

    def __init__(self, name: str, tTCTest_Test_File: set["tTCTest_Test_Case"] = None, tTCTest_Test_File2: set["tTCTest_Java_Class"] = None, tTCTest_Test_File4: set["tTCTest_Classes"] = None, tTCTest_Test_File6: set["tTCTest_Java_Method"] = None, tTCTest_Test_File8: set["tTCTest_Refactoring_Instance"] = None):
        self.name = name
        self.tTCTest_Test_File = tTCTest_Test_File if tTCTest_Test_File is not None else set()
        self.tTCTest_Test_File2 = tTCTest_Test_File2 if tTCTest_Test_File2 is not None else set()
        self.tTCTest_Test_File4 = tTCTest_Test_File4 if tTCTest_Test_File4 is not None else set()
        self.tTCTest_Test_File6 = tTCTest_Test_File6 if tTCTest_Test_File6 is not None else set()
        self.tTCTest_Test_File8 = tTCTest_Test_File8 if tTCTest_Test_File8 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tTCTest_Test_File(self):
        return self.__tTCTest_Test_File

    @tTCTest_Test_File.setter
    def tTCTest_Test_File(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tTCTest_Test_File__tTCTest_Test_File", None)
        self.__tTCTest_Test_File = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tTCTest_Test_Case"):
                    opp_val = getattr(item, "tTCTest_Test_Case", None)
                    
                    if opp_val == self:
                        setattr(item, "tTCTest_Test_Case", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tTCTest_Test_Case"):
                    opp_val = getattr(item, "tTCTest_Test_Case", None)
                    
                    setattr(item, "tTCTest_Test_Case", self)
                    

    @property
    def tTCTest_Test_File6(self):
        return self.__tTCTest_Test_File6

    @tTCTest_Test_File6.setter
    def tTCTest_Test_File6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tTCTest_Test_File__tTCTest_Test_File6", None)
        self.__tTCTest_Test_File6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tTCTest_Java_Method"):
                    opp_val = getattr(item, "tTCTest_Java_Method", None)
                    
                    if opp_val == self:
                        setattr(item, "tTCTest_Java_Method", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tTCTest_Java_Method"):
                    opp_val = getattr(item, "tTCTest_Java_Method", None)
                    
                    setattr(item, "tTCTest_Java_Method", self)
                    

    @property
    def tTCTest_Test_File2(self):
        return self.__tTCTest_Test_File2

    @tTCTest_Test_File2.setter
    def tTCTest_Test_File2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tTCTest_Test_File__tTCTest_Test_File2", None)
        self.__tTCTest_Test_File2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tTCTest_Java_Class"):
                    opp_val = getattr(item, "tTCTest_Java_Class", None)
                    
                    if opp_val == self:
                        setattr(item, "tTCTest_Java_Class", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tTCTest_Java_Class"):
                    opp_val = getattr(item, "tTCTest_Java_Class", None)
                    
                    setattr(item, "tTCTest_Java_Class", self)
                    

    @property
    def tTCTest_Test_File8(self):
        return self.__tTCTest_Test_File8

    @tTCTest_Test_File8.setter
    def tTCTest_Test_File8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tTCTest_Test_File__tTCTest_Test_File8", None)
        self.__tTCTest_Test_File8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tTCTest_Refactoring_Instance"):
                    opp_val = getattr(item, "tTCTest_Refactoring_Instance", None)
                    
                    if opp_val == self:
                        setattr(item, "tTCTest_Refactoring_Instance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tTCTest_Refactoring_Instance"):
                    opp_val = getattr(item, "tTCTest_Refactoring_Instance", None)
                    
                    setattr(item, "tTCTest_Refactoring_Instance", self)
                    

    @property
    def tTCTest_Test_File4(self):
        return self.__tTCTest_Test_File4

    @tTCTest_Test_File4.setter
    def tTCTest_Test_File4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tTCTest_Test_File__tTCTest_Test_File4", None)
        self.__tTCTest_Test_File4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tTCTest_Classes"):
                    opp_val = getattr(item, "tTCTest_Classes", None)
                    
                    if opp_val == self:
                        setattr(item, "tTCTest_Classes", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tTCTest_Classes"):
                    opp_val = getattr(item, "tTCTest_Classes", None)
                    
                    setattr(item, "tTCTest_Classes", self)
                    

class tTCTest_Fields:

    def __init__(self, name: str, tTCTest_Fields: set["tTCTest_Java_Field"] = None):
        self.name = name
        self.tTCTest_Fields = tTCTest_Fields if tTCTest_Fields is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tTCTest_Fields(self):
        return self.__tTCTest_Fields

    @tTCTest_Fields.setter
    def tTCTest_Fields(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tTCTest_Fields__tTCTest_Fields", None)
        self.__tTCTest_Fields = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tTCTest_Java_Field20"):
                    opp_val = getattr(item, "tTCTest_Java_Field20", None)
                    
                    if opp_val == self:
                        setattr(item, "tTCTest_Java_Field20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tTCTest_Java_Field20"):
                    opp_val = getattr(item, "tTCTest_Java_Field20", None)
                    
                    setattr(item, "tTCTest_Java_Field20", self)
                    

class tTCTest_Methods:

    def __init__(self, name: str, tTCTest_Methods: set["tTCTest_Java_Method"] = None):
        self.name = name
        self.tTCTest_Methods = tTCTest_Methods if tTCTest_Methods is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tTCTest_Methods(self):
        return self.__tTCTest_Methods

    @tTCTest_Methods.setter
    def tTCTest_Methods(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tTCTest_Methods__tTCTest_Methods", None)
        self.__tTCTest_Methods = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tTCTest_Java_Method16"):
                    opp_val = getattr(item, "tTCTest_Java_Method16", None)
                    
                    if opp_val == self:
                        setattr(item, "tTCTest_Java_Method16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tTCTest_Java_Method16"):
                    opp_val = getattr(item, "tTCTest_Java_Method16", None)
                    
                    setattr(item, "tTCTest_Java_Method16", self)
                    

class Class_Element:

    pass
class tTCTest_Java_Field(Class_Element):

    def __init__(self, field_name: str, tTCTest_Java_Field: "tTCTest_Java_Class" = None, tTCTest_Java_Field20: "tTCTest_Fields" = None):
        self.field_name = field_name
        self.tTCTest_Java_Field = tTCTest_Java_Field
        self.tTCTest_Java_Field20 = tTCTest_Java_Field20
        
    @property
    def field_name(self) -> str:
        return self.__field_name

    @field_name.setter
    def field_name(self, field_name: str):
        self.__field_name = field_name

    @property
    def tTCTest_Java_Field20(self):
        return self.__tTCTest_Java_Field20

    @tTCTest_Java_Field20.setter
    def tTCTest_Java_Field20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tTCTest_Java_Field__tTCTest_Java_Field20", None)
        self.__tTCTest_Java_Field20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tTCTest_Fields"):
                opp_val = getattr(old_value, "tTCTest_Fields", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tTCTest_Fields"):
                opp_val = getattr(value, "tTCTest_Fields", None)
                if opp_val is None:
                    setattr(value, "tTCTest_Fields", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tTCTest_Java_Field(self):
        return self.__tTCTest_Java_Field

    @tTCTest_Java_Field.setter
    def tTCTest_Java_Field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tTCTest_Java_Field__tTCTest_Java_Field", None)
        self.__tTCTest_Java_Field = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tTCTest_Java_Class18"):
                opp_val = getattr(old_value, "tTCTest_Java_Class18", None)
                if opp_val == self:
                    setattr(old_value, "tTCTest_Java_Class18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tTCTest_Java_Class18"):
                opp_val = getattr(value, "tTCTest_Java_Class18", None)
                setattr(value, "tTCTest_Java_Class18", self)

class tTCTest_Java_Method(Class_Element):

    def __init__(self, method_name: str, tTCTest_Java_Method13: set["tTCTest_Java_Class"] = None, tTCTest_Java_Method16: "tTCTest_Methods" = None, tTCTest_Java_Method: "tTCTest_Test_File" = None, tTCTest_Java_Method27: "tTCTest_Pull_Up_Refactoring" = None):
        self.method_name = method_name
        self.tTCTest_Java_Method13 = tTCTest_Java_Method13 if tTCTest_Java_Method13 is not None else set()
        self.tTCTest_Java_Method16 = tTCTest_Java_Method16
        self.tTCTest_Java_Method = tTCTest_Java_Method
        self.tTCTest_Java_Method27 = tTCTest_Java_Method27
        
    @property
    def method_name(self) -> str:
        return self.__method_name

    @method_name.setter
    def method_name(self, method_name: str):
        self.__method_name = method_name

    @property
    def tTCTest_Java_Method27(self):
        return self.__tTCTest_Java_Method27

    @tTCTest_Java_Method27.setter
    def tTCTest_Java_Method27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tTCTest_Java_Method__tTCTest_Java_Method27", None)
        self.__tTCTest_Java_Method27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tTCTest_Pull_Up_Refactoring26"):
                opp_val = getattr(old_value, "tTCTest_Pull_Up_Refactoring26", None)
                if opp_val == self:
                    setattr(old_value, "tTCTest_Pull_Up_Refactoring26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tTCTest_Pull_Up_Refactoring26"):
                opp_val = getattr(value, "tTCTest_Pull_Up_Refactoring26", None)
                setattr(value, "tTCTest_Pull_Up_Refactoring26", self)

    @property
    def tTCTest_Java_Method(self):
        return self.__tTCTest_Java_Method

    @tTCTest_Java_Method.setter
    def tTCTest_Java_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tTCTest_Java_Method__tTCTest_Java_Method", None)
        self.__tTCTest_Java_Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tTCTest_Test_File6"):
                opp_val = getattr(old_value, "tTCTest_Test_File6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tTCTest_Test_File6"):
                opp_val = getattr(value, "tTCTest_Test_File6", None)
                if opp_val is None:
                    setattr(value, "tTCTest_Test_File6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tTCTest_Java_Method16(self):
        return self.__tTCTest_Java_Method16

    @tTCTest_Java_Method16.setter
    def tTCTest_Java_Method16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tTCTest_Java_Method__tTCTest_Java_Method16", None)
        self.__tTCTest_Java_Method16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tTCTest_Methods"):
                opp_val = getattr(old_value, "tTCTest_Methods", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tTCTest_Methods"):
                opp_val = getattr(value, "tTCTest_Methods", None)
                if opp_val is None:
                    setattr(value, "tTCTest_Methods", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tTCTest_Java_Method13(self):
        return self.__tTCTest_Java_Method13

    @tTCTest_Java_Method13.setter
    def tTCTest_Java_Method13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tTCTest_Java_Method__tTCTest_Java_Method13", None)
        self.__tTCTest_Java_Method13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tTCTest_Java_Class14"):
                    opp_val = getattr(item, "tTCTest_Java_Class14", None)
                    
                    if opp_val == self:
                        setattr(item, "tTCTest_Java_Class14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tTCTest_Java_Class14"):
                    opp_val = getattr(item, "tTCTest_Java_Class14", None)
                    
                    setattr(item, "tTCTest_Java_Class14", self)
                    
