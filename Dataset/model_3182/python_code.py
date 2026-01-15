from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Type(Enum):
    INT = "INT"
    STRING = "STRING"
    Boolean = "Boolean"
    Double = "Double"
    Void = "Void"


############################################
# Definition of Classes
############################################

class architecture_AtomicType:

    def __init__(self, atomType: str, architecture_AtomicType40: "architecture_Operation" = None, architecture_AtomicType42: "architecture_Component" = None, architecture_AtomicType: "architecture_Variable" = None):
        self.atomType = atomType
        self.architecture_AtomicType40 = architecture_AtomicType40
        self.architecture_AtomicType42 = architecture_AtomicType42
        self.architecture_AtomicType = architecture_AtomicType
        
    @property
    def atomType(self) -> str:
        return self.__atomType

    @atomType.setter
    def atomType(self, atomType: str):
        self.__atomType = atomType

    @property
    def architecture_AtomicType(self):
        return self.__architecture_AtomicType

    @architecture_AtomicType.setter
    def architecture_AtomicType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architecture_AtomicType__architecture_AtomicType", None)
        self.__architecture_AtomicType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "architecture_Variable34"):
                opp_val = getattr(old_value, "architecture_Variable34", None)
                if opp_val == self:
                    setattr(old_value, "architecture_Variable34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "architecture_Variable34"):
                opp_val = getattr(value, "architecture_Variable34", None)
                setattr(value, "architecture_Variable34", self)

    @property
    def architecture_AtomicType42(self):
        return self.__architecture_AtomicType42

    @architecture_AtomicType42.setter
    def architecture_AtomicType42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architecture_AtomicType__architecture_AtomicType42", None)
        self.__architecture_AtomicType42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "architecture_Component43"):
                opp_val = getattr(old_value, "architecture_Component43", None)
                if opp_val == self:
                    setattr(old_value, "architecture_Component43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "architecture_Component43"):
                opp_val = getattr(value, "architecture_Component43", None)
                setattr(value, "architecture_Component43", self)

    @property
    def architecture_AtomicType40(self):
        return self.__architecture_AtomicType40

    @architecture_AtomicType40.setter
    def architecture_AtomicType40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architecture_AtomicType__architecture_AtomicType40", None)
        self.__architecture_AtomicType40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "architecture_Operation39"):
                opp_val = getattr(old_value, "architecture_Operation39", None)
                if opp_val == self:
                    setattr(old_value, "architecture_Operation39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "architecture_Operation39"):
                opp_val = getattr(value, "architecture_Operation39", None)
                setattr(value, "architecture_Operation39", self)

class architecture_Variable:

    def __init__(self, name: str, architecture_Variable23: "architecture_Binding" = None, architecture_Variable29: "architecture_Binding" = None, architecture_Variable: "architecture_Architecture" = None, architecture_Variable34: "architecture_AtomicType" = None, architecture_Variable37: "architecture_Operation" = None):
        self.name = name
        self.architecture_Variable23 = architecture_Variable23
        self.architecture_Variable29 = architecture_Variable29
        self.architecture_Variable = architecture_Variable
        self.architecture_Variable34 = architecture_Variable34
        self.architecture_Variable37 = architecture_Variable37
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def architecture_Variable(self):
        return self.__architecture_Variable

    @architecture_Variable.setter
    def architecture_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architecture_Variable__architecture_Variable", None)
        self.__architecture_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "architecture_Architecture18"):
                opp_val = getattr(old_value, "architecture_Architecture18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "architecture_Architecture18"):
                opp_val = getattr(value, "architecture_Architecture18", None)
                if opp_val is None:
                    setattr(value, "architecture_Architecture18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def architecture_Variable34(self):
        return self.__architecture_Variable34

    @architecture_Variable34.setter
    def architecture_Variable34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architecture_Variable__architecture_Variable34", None)
        self.__architecture_Variable34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "architecture_AtomicType"):
                opp_val = getattr(old_value, "architecture_AtomicType", None)
                if opp_val == self:
                    setattr(old_value, "architecture_AtomicType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "architecture_AtomicType"):
                opp_val = getattr(value, "architecture_AtomicType", None)
                setattr(value, "architecture_AtomicType", self)

    @property
    def architecture_Variable37(self):
        return self.__architecture_Variable37

    @architecture_Variable37.setter
    def architecture_Variable37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architecture_Variable__architecture_Variable37", None)
        self.__architecture_Variable37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "architecture_Operation36"):
                opp_val = getattr(old_value, "architecture_Operation36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "architecture_Operation36"):
                opp_val = getattr(value, "architecture_Operation36", None)
                if opp_val is None:
                    setattr(value, "architecture_Operation36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def architecture_Variable23(self):
        return self.__architecture_Variable23

    @architecture_Variable23.setter
    def architecture_Variable23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architecture_Variable__architecture_Variable23", None)
        self.__architecture_Variable23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "architecture_Binding22"):
                opp_val = getattr(old_value, "architecture_Binding22", None)
                if opp_val == self:
                    setattr(old_value, "architecture_Binding22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "architecture_Binding22"):
                opp_val = getattr(value, "architecture_Binding22", None)
                setattr(value, "architecture_Binding22", self)

    @property
    def architecture_Variable29(self):
        return self.__architecture_Variable29

    @architecture_Variable29.setter
    def architecture_Variable29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architecture_Variable__architecture_Variable29", None)
        self.__architecture_Variable29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "architecture_Binding28"):
                opp_val = getattr(old_value, "architecture_Binding28", None)
                if opp_val == self:
                    setattr(old_value, "architecture_Binding28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "architecture_Binding28"):
                opp_val = getattr(value, "architecture_Binding28", None)
                setattr(value, "architecture_Binding28", self)

class architecture_Operation:

    def __init__(self, name: str, architecture_Operation26: "architecture_Binding" = None, architecture_Operation: "architecture_Component" = None, architecture_Operation13: "architecture_Component" = None, architecture_Operation16: "architecture_Component" = None, architecture_Operation39: "architecture_AtomicType" = None, architecture_Operation32: "architecture_Binding" = None, architecture_Operation36: set["architecture_Variable"] = None):
        self.name = name
        self.architecture_Operation26 = architecture_Operation26
        self.architecture_Operation = architecture_Operation
        self.architecture_Operation13 = architecture_Operation13
        self.architecture_Operation16 = architecture_Operation16
        self.architecture_Operation39 = architecture_Operation39
        self.architecture_Operation32 = architecture_Operation32
        self.architecture_Operation36 = architecture_Operation36 if architecture_Operation36 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def architecture_Operation36(self):
        return self.__architecture_Operation36

    @architecture_Operation36.setter
    def architecture_Operation36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architecture_Operation__architecture_Operation36", None)
        self.__architecture_Operation36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "architecture_Variable37"):
                    opp_val = getattr(item, "architecture_Variable37", None)
                    
                    if opp_val == self:
                        setattr(item, "architecture_Variable37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "architecture_Variable37"):
                    opp_val = getattr(item, "architecture_Variable37", None)
                    
                    setattr(item, "architecture_Variable37", self)
                    

    @property
    def architecture_Operation32(self):
        return self.__architecture_Operation32

    @architecture_Operation32.setter
    def architecture_Operation32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architecture_Operation__architecture_Operation32", None)
        self.__architecture_Operation32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "architecture_Binding31"):
                opp_val = getattr(old_value, "architecture_Binding31", None)
                if opp_val == self:
                    setattr(old_value, "architecture_Binding31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "architecture_Binding31"):
                opp_val = getattr(value, "architecture_Binding31", None)
                setattr(value, "architecture_Binding31", self)

    @property
    def architecture_Operation(self):
        return self.__architecture_Operation

    @architecture_Operation.setter
    def architecture_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architecture_Operation__architecture_Operation", None)
        self.__architecture_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "architecture_Component10"):
                opp_val = getattr(old_value, "architecture_Component10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "architecture_Component10"):
                opp_val = getattr(value, "architecture_Component10", None)
                if opp_val is None:
                    setattr(value, "architecture_Component10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def architecture_Operation26(self):
        return self.__architecture_Operation26

    @architecture_Operation26.setter
    def architecture_Operation26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architecture_Operation__architecture_Operation26", None)
        self.__architecture_Operation26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "architecture_Binding25"):
                opp_val = getattr(old_value, "architecture_Binding25", None)
                if opp_val == self:
                    setattr(old_value, "architecture_Binding25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "architecture_Binding25"):
                opp_val = getattr(value, "architecture_Binding25", None)
                setattr(value, "architecture_Binding25", self)

    @property
    def architecture_Operation39(self):
        return self.__architecture_Operation39

    @architecture_Operation39.setter
    def architecture_Operation39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architecture_Operation__architecture_Operation39", None)
        self.__architecture_Operation39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "architecture_AtomicType40"):
                opp_val = getattr(old_value, "architecture_AtomicType40", None)
                if opp_val == self:
                    setattr(old_value, "architecture_AtomicType40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "architecture_AtomicType40"):
                opp_val = getattr(value, "architecture_AtomicType40", None)
                setattr(value, "architecture_AtomicType40", self)

    @property
    def architecture_Operation13(self):
        return self.__architecture_Operation13

    @architecture_Operation13.setter
    def architecture_Operation13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architecture_Operation__architecture_Operation13", None)
        self.__architecture_Operation13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "architecture_Component12"):
                opp_val = getattr(old_value, "architecture_Component12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "architecture_Component12"):
                opp_val = getattr(value, "architecture_Component12", None)
                if opp_val is None:
                    setattr(value, "architecture_Component12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def architecture_Operation16(self):
        return self.__architecture_Operation16

    @architecture_Operation16.setter
    def architecture_Operation16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architecture_Operation__architecture_Operation16", None)
        self.__architecture_Operation16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "architecture_Component15"):
                opp_val = getattr(old_value, "architecture_Component15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "architecture_Component15"):
                opp_val = getattr(value, "architecture_Component15", None)
                if opp_val is None:
                    setattr(value, "architecture_Component15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class architecture_Binding:

    pass
class architecture_Import:

    def __init__(self, importedNamespace: str, architecture_Import: "architecture_AbstractModel" = None):
        self.importedNamespace = importedNamespace
        self.architecture_Import = architecture_Import
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

    @property
    def architecture_Import(self):
        return self.__architecture_Import

    @architecture_Import.setter
    def architecture_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architecture_Import__architecture_Import", None)
        self.__architecture_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "architecture_AbstractModel4"):
                opp_val = getattr(old_value, "architecture_AbstractModel4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "architecture_AbstractModel4"):
                opp_val = getattr(value, "architecture_AbstractModel4", None)
                if opp_val is None:
                    setattr(value, "architecture_AbstractModel4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class architecture_AbstractModel:

    pass
class architecture_DomainDeclaration:

    def __init__(self, name: str, architecture_DomainDeclaration: "architecture_Model" = None, architecture_DomainDeclaration2: set["architecture_AbstractModel"] = None):
        self.name = name
        self.architecture_DomainDeclaration = architecture_DomainDeclaration
        self.architecture_DomainDeclaration2 = architecture_DomainDeclaration2 if architecture_DomainDeclaration2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def architecture_DomainDeclaration(self):
        return self.__architecture_DomainDeclaration

    @architecture_DomainDeclaration.setter
    def architecture_DomainDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architecture_DomainDeclaration__architecture_DomainDeclaration", None)
        self.__architecture_DomainDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "architecture_Model"):
                opp_val = getattr(old_value, "architecture_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "architecture_Model"):
                opp_val = getattr(value, "architecture_Model", None)
                if opp_val is None:
                    setattr(value, "architecture_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def architecture_DomainDeclaration2(self):
        return self.__architecture_DomainDeclaration2

    @architecture_DomainDeclaration2.setter
    def architecture_DomainDeclaration2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architecture_DomainDeclaration__architecture_DomainDeclaration2", None)
        self.__architecture_DomainDeclaration2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "architecture_AbstractModel"):
                    opp_val = getattr(item, "architecture_AbstractModel", None)
                    
                    if opp_val == self:
                        setattr(item, "architecture_AbstractModel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "architecture_AbstractModel"):
                    opp_val = getattr(item, "architecture_AbstractModel", None)
                    
                    setattr(item, "architecture_AbstractModel", self)
                    

class architecture_Model:

    pass
class architecture_Architecture:

    pass
class architecture_Component:

    def __init__(self, name: str, architecture_Component: "architecture_AbstractModel" = None, architecture_Component10: set["architecture_Operation"] = None, architecture_Component12: set["architecture_Operation"] = None, architecture_Component15: set["architecture_Operation"] = None, architecture_Component43: "architecture_AtomicType" = None):
        self.name = name
        self.architecture_Component = architecture_Component
        self.architecture_Component10 = architecture_Component10 if architecture_Component10 is not None else set()
        self.architecture_Component12 = architecture_Component12 if architecture_Component12 is not None else set()
        self.architecture_Component15 = architecture_Component15 if architecture_Component15 is not None else set()
        self.architecture_Component43 = architecture_Component43
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def architecture_Component(self):
        return self.__architecture_Component

    @architecture_Component.setter
    def architecture_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architecture_Component__architecture_Component", None)
        self.__architecture_Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "architecture_AbstractModel6"):
                opp_val = getattr(old_value, "architecture_AbstractModel6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "architecture_AbstractModel6"):
                opp_val = getattr(value, "architecture_AbstractModel6", None)
                if opp_val is None:
                    setattr(value, "architecture_AbstractModel6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def architecture_Component43(self):
        return self.__architecture_Component43

    @architecture_Component43.setter
    def architecture_Component43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architecture_Component__architecture_Component43", None)
        self.__architecture_Component43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "architecture_AtomicType42"):
                opp_val = getattr(old_value, "architecture_AtomicType42", None)
                if opp_val == self:
                    setattr(old_value, "architecture_AtomicType42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "architecture_AtomicType42"):
                opp_val = getattr(value, "architecture_AtomicType42", None)
                setattr(value, "architecture_AtomicType42", self)

    @property
    def architecture_Component12(self):
        return self.__architecture_Component12

    @architecture_Component12.setter
    def architecture_Component12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architecture_Component__architecture_Component12", None)
        self.__architecture_Component12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "architecture_Operation13"):
                    opp_val = getattr(item, "architecture_Operation13", None)
                    
                    if opp_val == self:
                        setattr(item, "architecture_Operation13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "architecture_Operation13"):
                    opp_val = getattr(item, "architecture_Operation13", None)
                    
                    setattr(item, "architecture_Operation13", self)
                    

    @property
    def architecture_Component10(self):
        return self.__architecture_Component10

    @architecture_Component10.setter
    def architecture_Component10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architecture_Component__architecture_Component10", None)
        self.__architecture_Component10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "architecture_Operation"):
                    opp_val = getattr(item, "architecture_Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "architecture_Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "architecture_Operation"):
                    opp_val = getattr(item, "architecture_Operation", None)
                    
                    setattr(item, "architecture_Operation", self)
                    

    @property
    def architecture_Component15(self):
        return self.__architecture_Component15

    @architecture_Component15.setter
    def architecture_Component15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_architecture_Component__architecture_Component15", None)
        self.__architecture_Component15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "architecture_Operation16"):
                    opp_val = getattr(item, "architecture_Operation16", None)
                    
                    if opp_val == self:
                        setattr(item, "architecture_Operation16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "architecture_Operation16"):
                    opp_val = getattr(item, "architecture_Operation16", None)
                    
                    setattr(item, "architecture_Operation16", self)
                    
