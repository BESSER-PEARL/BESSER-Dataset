from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Expression:

    pass
class eol_module_ExpressionOrStatementBlock:

    pass
class eol_module_FormalParameterExpression:

    pass
class eol_module_NameExpression(Expression):

    def __init__(self, name: str, isType: bool, eol_module_NameExpression: "eol_module_OperationDefinition" = None):
        self.name = name
        self.isType = isType
        self.eol_module_NameExpression = eol_module_NameExpression
        
    @property
    def isType(self) -> bool:
        return self.__isType

    @isType.setter
    def isType(self, isType: bool):
        self.__isType = isType

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eol_module_NameExpression(self):
        return self.__eol_module_NameExpression

    @eol_module_NameExpression.setter
    def eol_module_NameExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_module_NameExpression__eol_module_NameExpression", None)
        self.__eol_module_NameExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_module_OperationDefinition29"):
                opp_val = getattr(old_value, "eol_module_OperationDefinition29", None)
                if opp_val == self:
                    setattr(old_value, "eol_module_OperationDefinition29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_module_OperationDefinition29"):
                opp_val = getattr(value, "eol_module_OperationDefinition29", None)
                setattr(value, "eol_module_OperationDefinition29", self)

class eol_module_Type:

    pass
class eol_module_Expression(ABC):

    pass
class eol_module_Import:

    def __init__(self, imported: str, eol_module_Import7: "eol_module_EOLLibraryModule" = None, eol_module_Import: "eol_module_EOLLibraryModule" = None):
        self.imported = imported
        self.eol_module_Import7 = eol_module_Import7
        self.eol_module_Import = eol_module_Import
        
    @property
    def imported(self) -> str:
        return self.__imported

    @imported.setter
    def imported(self, imported: str):
        self.__imported = imported

    @property
    def eol_module_Import7(self):
        return self.__eol_module_Import7

    @eol_module_Import7.setter
    def eol_module_Import7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_module_Import__eol_module_Import7", None)
        self.__eol_module_Import7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_module_EOLLibraryModule8"):
                opp_val = getattr(old_value, "eol_module_EOLLibraryModule8", None)
                if opp_val == self:
                    setattr(old_value, "eol_module_EOLLibraryModule8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_module_EOLLibraryModule8"):
                opp_val = getattr(value, "eol_module_EOLLibraryModule8", None)
                setattr(value, "eol_module_EOLLibraryModule8", self)

    @property
    def eol_module_Import(self):
        return self.__eol_module_Import

    @eol_module_Import.setter
    def eol_module_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_module_Import__eol_module_Import", None)
        self.__eol_module_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_module_EOLLibraryModule"):
                opp_val = getattr(old_value, "eol_module_EOLLibraryModule", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_module_EOLLibraryModule"):
                opp_val = getattr(value, "eol_module_EOLLibraryModule", None)
                if opp_val is None:
                    setattr(value, "eol_module_EOLLibraryModule", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Block:

    pass
class eol_module_AnnotationBlock(Block):

    pass
class eol_module_Statement(ABC):

    pass
class eol_module_Block:

    pass
class EOLLibraryModule:

    pass
class eol_module_EOLModule(EOLLibraryModule):

    pass
class eol_module_OperationDefinition:

    pass
class eol_module_ModelDeclarationStatement:

    pass
class eol_module_EOLLibraryModule:

    def __init__(self, name: str, eol_module_EOLLibraryModule2: set["eol_module_ModelDeclarationStatement"] = None, eol_module_EOLLibraryModule4: set["eol_module_OperationDefinition"] = None, eol_module_EOLLibraryModule8: "eol_module_Import" = None, eol_module_EOLLibraryModule: set["eol_module_Import"] = None):
        self.name = name
        self.eol_module_EOLLibraryModule2 = eol_module_EOLLibraryModule2 if eol_module_EOLLibraryModule2 is not None else set()
        self.eol_module_EOLLibraryModule4 = eol_module_EOLLibraryModule4 if eol_module_EOLLibraryModule4 is not None else set()
        self.eol_module_EOLLibraryModule8 = eol_module_EOLLibraryModule8
        self.eol_module_EOLLibraryModule = eol_module_EOLLibraryModule if eol_module_EOLLibraryModule is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eol_module_EOLLibraryModule4(self):
        return self.__eol_module_EOLLibraryModule4

    @eol_module_EOLLibraryModule4.setter
    def eol_module_EOLLibraryModule4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_module_EOLLibraryModule__eol_module_EOLLibraryModule4", None)
        self.__eol_module_EOLLibraryModule4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eol_module_OperationDefinition"):
                    opp_val = getattr(item, "eol_module_OperationDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "eol_module_OperationDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eol_module_OperationDefinition"):
                    opp_val = getattr(item, "eol_module_OperationDefinition", None)
                    
                    setattr(item, "eol_module_OperationDefinition", self)
                    

    @property
    def eol_module_EOLLibraryModule(self):
        return self.__eol_module_EOLLibraryModule

    @eol_module_EOLLibraryModule.setter
    def eol_module_EOLLibraryModule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_module_EOLLibraryModule__eol_module_EOLLibraryModule", None)
        self.__eol_module_EOLLibraryModule = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eol_module_Import"):
                    opp_val = getattr(item, "eol_module_Import", None)
                    
                    if opp_val == self:
                        setattr(item, "eol_module_Import", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eol_module_Import"):
                    opp_val = getattr(item, "eol_module_Import", None)
                    
                    setattr(item, "eol_module_Import", self)
                    

    @property
    def eol_module_EOLLibraryModule8(self):
        return self.__eol_module_EOLLibraryModule8

    @eol_module_EOLLibraryModule8.setter
    def eol_module_EOLLibraryModule8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_module_EOLLibraryModule__eol_module_EOLLibraryModule8", None)
        self.__eol_module_EOLLibraryModule8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_module_Import7"):
                opp_val = getattr(old_value, "eol_module_Import7", None)
                if opp_val == self:
                    setattr(old_value, "eol_module_Import7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_module_Import7"):
                opp_val = getattr(value, "eol_module_Import7", None)
                setattr(value, "eol_module_Import7", self)

    @property
    def eol_module_EOLLibraryModule2(self):
        return self.__eol_module_EOLLibraryModule2

    @eol_module_EOLLibraryModule2.setter
    def eol_module_EOLLibraryModule2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_module_EOLLibraryModule__eol_module_EOLLibraryModule2", None)
        self.__eol_module_EOLLibraryModule2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eol_module_ModelDeclarationStatement"):
                    opp_val = getattr(item, "eol_module_ModelDeclarationStatement", None)
                    
                    if opp_val == self:
                        setattr(item, "eol_module_ModelDeclarationStatement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eol_module_ModelDeclarationStatement"):
                    opp_val = getattr(item, "eol_module_ModelDeclarationStatement", None)
                    
                    setattr(item, "eol_module_ModelDeclarationStatement", self)
                    
