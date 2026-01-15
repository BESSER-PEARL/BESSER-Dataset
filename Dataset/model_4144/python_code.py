from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Expression:

    pass
class arithmetics_NumberLiteral(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class arithmetics_Multi(Expression):

    pass
class arithmetics_FunctionCall(Expression):

    pass
class arithmetics_Div(Expression):

    pass
class arithmetics_Minus(Expression):

    pass
class arithmetics_Plus(Expression):

    pass
class arithmetics_AbstractDefinition:

    def __init__(self, name: str, arithmetics_AbstractDefinition: "arithmetics_FunctionCall" = None):
        self.name = name
        self.arithmetics_AbstractDefinition = arithmetics_AbstractDefinition
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def arithmetics_AbstractDefinition(self):
        return self.__arithmetics_AbstractDefinition

    @arithmetics_AbstractDefinition.setter
    def arithmetics_AbstractDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arithmetics_AbstractDefinition__arithmetics_AbstractDefinition", None)
        self.__arithmetics_AbstractDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arithmetics_FunctionCall"):
                opp_val = getattr(old_value, "arithmetics_FunctionCall", None)
                if opp_val == self:
                    setattr(old_value, "arithmetics_FunctionCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arithmetics_FunctionCall"):
                opp_val = getattr(value, "arithmetics_FunctionCall", None)
                setattr(value, "arithmetics_FunctionCall", self)

class arithmetics_Expression:

    pass
class AbstractDefinition:

    pass
class arithmetics_DeclaredParameter(AbstractDefinition):

    pass
class Statement:

    pass
class arithmetics_Evaluation(Statement):

    pass
class arithmetics_Definition(Statement, AbstractDefinition):

    pass
class arithmetics_Statement:

    pass
class arithmetics_Import:

    def __init__(self, importedNamespace: str, arithmetics_Import: "arithmetics_Module" = None):
        self.importedNamespace = importedNamespace
        self.arithmetics_Import = arithmetics_Import
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

    @property
    def arithmetics_Import(self):
        return self.__arithmetics_Import

    @arithmetics_Import.setter
    def arithmetics_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arithmetics_Import__arithmetics_Import", None)
        self.__arithmetics_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arithmetics_Module"):
                opp_val = getattr(old_value, "arithmetics_Module", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arithmetics_Module"):
                opp_val = getattr(value, "arithmetics_Module", None)
                if opp_val is None:
                    setattr(value, "arithmetics_Module", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class arithmetics_Module:

    def __init__(self, name: str, arithmetics_Module: set["arithmetics_Import"] = None, arithmetics_Module2: set["arithmetics_Statement"] = None):
        self.name = name
        self.arithmetics_Module = arithmetics_Module if arithmetics_Module is not None else set()
        self.arithmetics_Module2 = arithmetics_Module2 if arithmetics_Module2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def arithmetics_Module2(self):
        return self.__arithmetics_Module2

    @arithmetics_Module2.setter
    def arithmetics_Module2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arithmetics_Module__arithmetics_Module2", None)
        self.__arithmetics_Module2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arithmetics_Statement"):
                    opp_val = getattr(item, "arithmetics_Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "arithmetics_Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arithmetics_Statement"):
                    opp_val = getattr(item, "arithmetics_Statement", None)
                    
                    setattr(item, "arithmetics_Statement", self)
                    

    @property
    def arithmetics_Module(self):
        return self.__arithmetics_Module

    @arithmetics_Module.setter
    def arithmetics_Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arithmetics_Module__arithmetics_Module", None)
        self.__arithmetics_Module = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arithmetics_Import"):
                    opp_val = getattr(item, "arithmetics_Import", None)
                    
                    if opp_val == self:
                        setattr(item, "arithmetics_Import", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arithmetics_Import"):
                    opp_val = getattr(item, "arithmetics_Import", None)
                    
                    setattr(item, "arithmetics_Import", self)
                    
