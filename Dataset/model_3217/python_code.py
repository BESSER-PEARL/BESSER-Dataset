from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Status(Enum):
    NORMAL = "NORMAL"
    FAILEDDEP = "FAILEDDEP"
    LIBRARY = "LIBRARY"
    IMPLICIT = "IMPLICIT"
class JumpStatementKind(Enum):
    JUMP = "JUMP"
    RETURN = "RETURN"
    THROW = "THROW"
class Visibilities(Enum):
    VISIBILITYSTRICTPROTECTED = "VISIBILITYSTRICTPROTECTED"
    VISIBILITYPUBLIC = "VISIBILITYPUBLIC"
    VISIBILITYPACKAGE = "VISIBILITYPACKAGE"
    VISIBILITYPROTECTED = "VISIBILITYPROTECTED"
    VISIBILITYPRIVAT = "VISIBILITYPRIVAT"
class LoopStatementKind(Enum):
    FOREACH = "FOREACH"
    WHILE = "WHILE"
    DOWHILE = "DOWHILE"
    FOR = "FOR"
class GlobalFunctionKind(Enum):
    NORMAL = "NORMAL"
    UNITINITIALIZER = "UNITINITIALIZER"
    UNITFINALIZER = "UNITFINALIZER"


############################################
# Definition of Classes
############################################

class variables_Field:

    pass
class variables_Variable:

    pass
class ThrowTypeAccess:

    pass
class LocalVariable:

    pass
class FormalParameter:

    pass
class DeclarationTypeAccess:

    pass
class functions_Constructor:

    pass
class functions_Method:

    pass
class functions_GlobalFunction:

    pass
class functions_Function:

    pass
class VariableAccess:

    pass
class gast_accesses_PropertyAccess(VariableAccess):

    pass
class gast_accesses_SelfAccess(VariableAccess):

    def __init__(self, super: bool):
        self.super = super
        
        pass
    @property
    def super(self):
        return self.__super

    @super.setter
    def super(self, super: bool):
        self.__super = super


class FunctionAccess:

    pass
class gast_accesses_DelegateAccess(FunctionAccess):

    pass
class Variable:

    pass
class gast_variables_GlobalVariable(Variable):

    pass
class gast_variables_CatchParameter(Variable):

    def __init__(self, rethrown: bool, Variable272: "gast_accesses_VariableAccess" = None, Variable: "gast_accesses_DeclarationTypeAccess" = None):
        self.rethrown = rethrown
        
        pass
    @property
    def rethrown(self):
        return self.__rethrown

    @rethrown.setter
    def rethrown(self, rethrown: bool):
        self.__rethrown = rethrown


class gast_variables_LocalVariable(Variable):

    pass
class gast_variables_FormalParameter(Variable):

    def __init__(self, passedByReference: bool, formalParameters: "Function" = None, Variable272: "gast_accesses_VariableAccess" = None, Variable: "gast_accesses_DeclarationTypeAccess" = None):
        self.passedByReference = passedByReference
        self.formalParameters = formalParameters
        
        pass
    @property
    def passedByReference(self):
        return self.__passedByReference

    @passedByReference.setter
    def passedByReference(self, passedByReference: bool):
        self.__passedByReference = passedByReference


    @property
    def formalParameters(self):
        return self.__formalParameters

    @formalParameters.setter
    def formalParameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_variables_FormalParameter__formalParameters", None)
        self.__formalParameters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Function318"):
                opp_val = getattr(old_value, "Function318", None)
                if opp_val == self:
                    setattr(old_value, "Function318", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Function318"):
                opp_val = getattr(value, "Function318", None)
                setattr(value, "Function318", self)

class CompositeAccess:

    pass
class TypeAccess:

    pass
class gast_accesses_DeclarationTypeAccess(TypeAccess):

    pass
class gast_accesses_RunTimeTypeAccess(TypeAccess):

    pass
class gast_accesses_ThrowTypeAccess(TypeAccess):

    def __init__(self, declared: bool):
        self.declared = declared
        
        pass
    @property
    def declared(self):
        return self.__declared

    @declared.setter
    def declared(self, declared: bool):
        self.__declared = declared


class gast_accesses_InheritanceTypeAccess(TypeAccess):

    def __init__(self, implementationInheritance: bool):
        self.implementationInheritance = implementationInheritance
        
        pass
    @property
    def implementationInheritance(self):
        return self.__implementationInheritance

    @implementationInheritance.setter
    def implementationInheritance(self, implementationInheritance: bool):
        self.__implementationInheritance = implementationInheritance


class gast_accesses_CastTypeAccess(TypeAccess):

    pass
class gast_accesses_StaticTypeAccess(TypeAccess):

    pass
class gast_accesses_ParameterInstantiationTypeAccess(TypeAccess):

    pass
class Property:

    pass
class InheritanceTypeAccess:

    pass
class types_GASTType:

    pass
class Method:

    pass
class Field:

    pass
class Destructor:

    pass
class Constructor:

    pass
class core_GenericEntity:

    pass
class gast_functions_GenericFunction(functions_GlobalFunction, core_GenericEntity):

    pass
class gast_functions_GenericConstructor(functions_Constructor, core_GenericEntity):

    pass
class gast_functions_GenericMethod(functions_Method, core_GenericEntity):

    pass
class Member:

    pass
class types_TypeDecorator:

    pass
class types_Member:

    pass
class gast_functions_Destructor(functions_Function, types_Member):

    pass
class gast_variables_Field(types_Member, variables_Variable):

    def __init__(self, propertyField: bool, fields: "GASTClass" = None):
        self.propertyField = propertyField
        self.fields = fields
        
        pass
    @property
    def propertyField(self):
        return self.__propertyField

    @propertyField.setter
    def propertyField(self, propertyField: bool):
        self.__propertyField = propertyField


    @property
    def fields(self):
        return self.__fields

    @fields.setter
    def fields(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_variables_Field__fields", None)
        self.__fields = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GASTClass324"):
                opp_val = getattr(old_value, "GASTClass324", None)
                if opp_val == self:
                    setattr(old_value, "GASTClass324", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTClass324"):
                opp_val = getattr(value, "GASTClass324", None)
                setattr(value, "GASTClass324", self)

class gast_types_GASTClass(types_Member, types_GASTType):

    def __init__(self, local: bool, primitive: bool, interface: bool, anonymous: bool, linesOfComments: int, inner: bool, surroundingClass207: set["Method"] = None, localClasses: "Function" = None, classes: "Package" = None, gast_types_GASTClass: set["GASTClass"] = None, surroundingClass215: set["GASTClass"] = None, innerClasses: "GASTClass" = None, gast_types_GASTClass220: set["InheritanceTypeAccess"] = None, surroundingClass: set["TypeAlias"] = None, surroundingClass198: set["Delegate"] = None, surroundingClass201: set["Constructor"] = None, surroundingClass203: set["Destructor"] = None, surroundingClass205: set["Field"] = None, gast_types_GASTClass222: "Field" = None, gastClass: set["GASTClass"] = None, friendClasses: "GASTClass" = None, gast_types_GASTClass232: set["Property"] = None, gast_types_GASTClass234: set["Access"] = None, gast_types_GASTClass237: set["GASTClass"] = None, gast_types_GASTClass229: set["Function"] = None):
        self.local = local
        self.primitive = primitive
        self.interface = interface
        self.anonymous = anonymous
        self.linesOfComments = linesOfComments
        self.inner = inner
        self.surroundingClass207 = surroundingClass207 if surroundingClass207 is not None else set()
        self.localClasses = localClasses
        self.classes = classes
        self.gast_types_GASTClass = gast_types_GASTClass if gast_types_GASTClass is not None else set()
        self.surroundingClass215 = surroundingClass215 if surroundingClass215 is not None else set()
        self.innerClasses = innerClasses
        self.gast_types_GASTClass220 = gast_types_GASTClass220 if gast_types_GASTClass220 is not None else set()
        self.surroundingClass = surroundingClass if surroundingClass is not None else set()
        self.surroundingClass198 = surroundingClass198 if surroundingClass198 is not None else set()
        self.surroundingClass201 = surroundingClass201 if surroundingClass201 is not None else set()
        self.surroundingClass203 = surroundingClass203 if surroundingClass203 is not None else set()
        self.surroundingClass205 = surroundingClass205 if surroundingClass205 is not None else set()
        self.gast_types_GASTClass222 = gast_types_GASTClass222
        self.gastClass = gastClass if gastClass is not None else set()
        self.friendClasses = friendClasses
        self.gast_types_GASTClass232 = gast_types_GASTClass232 if gast_types_GASTClass232 is not None else set()
        self.gast_types_GASTClass234 = gast_types_GASTClass234 if gast_types_GASTClass234 is not None else set()
        self.gast_types_GASTClass237 = gast_types_GASTClass237 if gast_types_GASTClass237 is not None else set()
        self.gast_types_GASTClass229 = gast_types_GASTClass229 if gast_types_GASTClass229 is not None else set()
        
        pass
    @property
    def primitive(self):
        return self.__primitive

    @primitive.setter
    def primitive(self, primitive: bool):
        self.__primitive = primitive


    @property
    def interface(self):
        return self.__interface

    @interface.setter
    def interface(self, interface: bool):
        self.__interface = interface


    @property
    def inner(self):
        return self.__inner

    @inner.setter
    def inner(self, inner: bool):
        self.__inner = inner


    @property
    def linesOfComments(self):
        return self.__linesOfComments

    @linesOfComments.setter
    def linesOfComments(self, linesOfComments: int):
        self.__linesOfComments = linesOfComments


    @property
    def anonymous(self):
        return self.__anonymous

    @anonymous.setter
    def anonymous(self, anonymous: bool):
        self.__anonymous = anonymous


    @property
    def local(self):
        return self.__local

    @local.setter
    def local(self, local: bool):
        self.__local = local


    @property
    def surroundingClass203(self):
        return self.__surroundingClass203

    @surroundingClass203.setter
    def surroundingClass203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__surroundingClass203", None)
        self.__surroundingClass203 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Destructor"):
                    opp_val = getattr(item, "Destructor", None)
                    
                    if opp_val == self:
                        setattr(item, "Destructor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Destructor"):
                    opp_val = getattr(item, "Destructor", None)
                    
                    setattr(item, "Destructor", self)
                    

    @property
    def innerClasses(self):
        return self.__innerClasses

    @innerClasses.setter
    def innerClasses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__innerClasses", None)
        self.__innerClasses = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GASTClass218"):
                opp_val = getattr(old_value, "GASTClass218", None)
                if opp_val == self:
                    setattr(old_value, "GASTClass218", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTClass218"):
                opp_val = getattr(value, "GASTClass218", None)
                setattr(value, "GASTClass218", self)

    @property
    def surroundingClass201(self):
        return self.__surroundingClass201

    @surroundingClass201.setter
    def surroundingClass201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__surroundingClass201", None)
        self.__surroundingClass201 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Constructor"):
                    opp_val = getattr(item, "Constructor", None)
                    
                    if opp_val == self:
                        setattr(item, "Constructor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Constructor"):
                    opp_val = getattr(item, "Constructor", None)
                    
                    setattr(item, "Constructor", self)
                    

    @property
    def surroundingClass205(self):
        return self.__surroundingClass205

    @surroundingClass205.setter
    def surroundingClass205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__surroundingClass205", None)
        self.__surroundingClass205 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Field"):
                    opp_val = getattr(item, "Field", None)
                    
                    if opp_val == self:
                        setattr(item, "Field", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Field"):
                    opp_val = getattr(item, "Field", None)
                    
                    setattr(item, "Field", self)
                    

    @property
    def gast_types_GASTClass229(self):
        return self.__gast_types_GASTClass229

    @gast_types_GASTClass229.setter
    def gast_types_GASTClass229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__gast_types_GASTClass229", None)
        self.__gast_types_GASTClass229 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Function230"):
                    opp_val = getattr(item, "Function230", None)
                    
                    if opp_val == self:
                        setattr(item, "Function230", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Function230"):
                    opp_val = getattr(item, "Function230", None)
                    
                    setattr(item, "Function230", self)
                    

    @property
    def gast_types_GASTClass237(self):
        return self.__gast_types_GASTClass237

    @gast_types_GASTClass237.setter
    def gast_types_GASTClass237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__gast_types_GASTClass237", None)
        self.__gast_types_GASTClass237 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass238"):
                    opp_val = getattr(item, "GASTClass238", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass238", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass238"):
                    opp_val = getattr(item, "GASTClass238", None)
                    
                    setattr(item, "GASTClass238", self)
                    

    @property
    def friendClasses(self):
        return self.__friendClasses

    @friendClasses.setter
    def friendClasses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__friendClasses", None)
        self.__friendClasses = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GASTClass227"):
                opp_val = getattr(old_value, "GASTClass227", None)
                if opp_val == self:
                    setattr(old_value, "GASTClass227", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTClass227"):
                opp_val = getattr(value, "GASTClass227", None)
                setattr(value, "GASTClass227", self)

    @property
    def gast_types_GASTClass222(self):
        return self.__gast_types_GASTClass222

    @gast_types_GASTClass222.setter
    def gast_types_GASTClass222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__gast_types_GASTClass222", None)
        self.__gast_types_GASTClass222 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Field223"):
                opp_val = getattr(old_value, "Field223", None)
                if opp_val == self:
                    setattr(old_value, "Field223", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Field223"):
                opp_val = getattr(value, "Field223", None)
                setattr(value, "Field223", self)

    @property
    def gast_types_GASTClass234(self):
        return self.__gast_types_GASTClass234

    @gast_types_GASTClass234.setter
    def gast_types_GASTClass234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__gast_types_GASTClass234", None)
        self.__gast_types_GASTClass234 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Access235"):
                    opp_val = getattr(item, "Access235", None)
                    
                    if opp_val == self:
                        setattr(item, "Access235", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Access235"):
                    opp_val = getattr(item, "Access235", None)
                    
                    setattr(item, "Access235", self)
                    

    @property
    def surroundingClass(self):
        return self.__surroundingClass

    @surroundingClass.setter
    def surroundingClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__surroundingClass", None)
        self.__surroundingClass = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypeAlias196"):
                    opp_val = getattr(item, "TypeAlias196", None)
                    
                    if opp_val == self:
                        setattr(item, "TypeAlias196", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypeAlias196"):
                    opp_val = getattr(item, "TypeAlias196", None)
                    
                    setattr(item, "TypeAlias196", self)
                    

    @property
    def classes(self):
        return self.__classes

    @classes.setter
    def classes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__classes", None)
        self.__classes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package211"):
                opp_val = getattr(old_value, "Package211", None)
                if opp_val == self:
                    setattr(old_value, "Package211", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package211"):
                opp_val = getattr(value, "Package211", None)
                setattr(value, "Package211", self)

    @property
    def localClasses(self):
        return self.__localClasses

    @localClasses.setter
    def localClasses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__localClasses", None)
        self.__localClasses = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Function209"):
                opp_val = getattr(old_value, "Function209", None)
                if opp_val == self:
                    setattr(old_value, "Function209", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Function209"):
                opp_val = getattr(value, "Function209", None)
                setattr(value, "Function209", self)

    @property
    def surroundingClass207(self):
        return self.__surroundingClass207

    @surroundingClass207.setter
    def surroundingClass207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__surroundingClass207", None)
        self.__surroundingClass207 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Method"):
                    opp_val = getattr(item, "Method", None)
                    
                    if opp_val == self:
                        setattr(item, "Method", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Method"):
                    opp_val = getattr(item, "Method", None)
                    
                    setattr(item, "Method", self)
                    

    @property
    def gastClass(self):
        return self.__gastClass

    @gastClass.setter
    def gastClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__gastClass", None)
        self.__gastClass = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass225"):
                    opp_val = getattr(item, "GASTClass225", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass225", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass225"):
                    opp_val = getattr(item, "GASTClass225", None)
                    
                    setattr(item, "GASTClass225", self)
                    

    @property
    def surroundingClass198(self):
        return self.__surroundingClass198

    @surroundingClass198.setter
    def surroundingClass198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__surroundingClass198", None)
        self.__surroundingClass198 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Delegate199"):
                    opp_val = getattr(item, "Delegate199", None)
                    
                    if opp_val == self:
                        setattr(item, "Delegate199", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Delegate199"):
                    opp_val = getattr(item, "Delegate199", None)
                    
                    setattr(item, "Delegate199", self)
                    

    @property
    def gast_types_GASTClass220(self):
        return self.__gast_types_GASTClass220

    @gast_types_GASTClass220.setter
    def gast_types_GASTClass220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__gast_types_GASTClass220", None)
        self.__gast_types_GASTClass220 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InheritanceTypeAccess"):
                    opp_val = getattr(item, "InheritanceTypeAccess", None)
                    
                    if opp_val == self:
                        setattr(item, "InheritanceTypeAccess", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InheritanceTypeAccess"):
                    opp_val = getattr(item, "InheritanceTypeAccess", None)
                    
                    setattr(item, "InheritanceTypeAccess", self)
                    

    @property
    def surroundingClass215(self):
        return self.__surroundingClass215

    @surroundingClass215.setter
    def surroundingClass215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__surroundingClass215", None)
        self.__surroundingClass215 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass216"):
                    opp_val = getattr(item, "GASTClass216", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass216", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass216"):
                    opp_val = getattr(item, "GASTClass216", None)
                    
                    setattr(item, "GASTClass216", self)
                    

    @property
    def gast_types_GASTClass(self):
        return self.__gast_types_GASTClass

    @gast_types_GASTClass.setter
    def gast_types_GASTClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__gast_types_GASTClass", None)
        self.__gast_types_GASTClass = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass213"):
                    opp_val = getattr(item, "GASTClass213", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass213", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass213"):
                    opp_val = getattr(item, "GASTClass213", None)
                    
                    setattr(item, "GASTClass213", self)
                    

    @property
    def gast_types_GASTClass232(self):
        return self.__gast_types_GASTClass232

    @gast_types_GASTClass232.setter
    def gast_types_GASTClass232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__gast_types_GASTClass232", None)
        self.__gast_types_GASTClass232 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property"):
                    opp_val = getattr(item, "Property", None)
                    
                    if opp_val == self:
                        setattr(item, "Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property"):
                    opp_val = getattr(item, "Property", None)
                    
                    setattr(item, "Property", self)
                    

class gast_functions_Method(functions_Function, types_Member):

    def __init__(self, propertyMethod: bool, gast_functions_Method: "Property" = None, methods: "GASTClass" = None):
        self.propertyMethod = propertyMethod
        self.gast_functions_Method = gast_functions_Method
        self.methods = methods
        
        pass
    @property
    def propertyMethod(self):
        return self.__propertyMethod

    @propertyMethod.setter
    def propertyMethod(self, propertyMethod: bool):
        self.__propertyMethod = propertyMethod


    @property
    def gast_functions_Method(self):
        return self.__gast_functions_Method

    @gast_functions_Method.setter
    def gast_functions_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Method__gast_functions_Method", None)
        self.__gast_functions_Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Property297"):
                opp_val = getattr(old_value, "Property297", None)
                if opp_val == self:
                    setattr(old_value, "Property297", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Property297"):
                opp_val = getattr(value, "Property297", None)
                setattr(value, "Property297", self)

    @property
    def methods(self):
        return self.__methods

    @methods.setter
    def methods(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Method__methods", None)
        self.__methods = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GASTClass299"):
                opp_val = getattr(old_value, "GASTClass299", None)
                if opp_val == self:
                    setattr(old_value, "GASTClass299", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTClass299"):
                opp_val = getattr(value, "GASTClass299", None)
                setattr(value, "GASTClass299", self)

class gast_functions_Delegate(functions_Function, types_Member, types_GASTType):

    def __init__(self, innerDelegate: bool, gast_functions_Delegate: "GASTClass" = None, gast_functions_Delegate281: set["Function"] = None, innerDelegates: "GASTClass" = None, delegates: "Package" = None):
        self.innerDelegate = innerDelegate
        self.gast_functions_Delegate = gast_functions_Delegate
        self.gast_functions_Delegate281 = gast_functions_Delegate281 if gast_functions_Delegate281 is not None else set()
        self.innerDelegates = innerDelegates
        self.delegates = delegates
        
        pass
    @property
    def innerDelegate(self):
        return self.__innerDelegate

    @innerDelegate.setter
    def innerDelegate(self, innerDelegate: bool):
        self.__innerDelegate = innerDelegate


    @property
    def delegates(self):
        return self.__delegates

    @delegates.setter
    def delegates(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Delegate__delegates", None)
        self.__delegates = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package286"):
                opp_val = getattr(old_value, "Package286", None)
                if opp_val == self:
                    setattr(old_value, "Package286", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package286"):
                opp_val = getattr(value, "Package286", None)
                setattr(value, "Package286", self)

    @property
    def innerDelegates(self):
        return self.__innerDelegates

    @innerDelegates.setter
    def innerDelegates(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Delegate__innerDelegates", None)
        self.__innerDelegates = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GASTClass284"):
                opp_val = getattr(old_value, "GASTClass284", None)
                if opp_val == self:
                    setattr(old_value, "GASTClass284", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTClass284"):
                opp_val = getattr(value, "GASTClass284", None)
                setattr(value, "GASTClass284", self)

    @property
    def gast_functions_Delegate281(self):
        return self.__gast_functions_Delegate281

    @gast_functions_Delegate281.setter
    def gast_functions_Delegate281(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Delegate__gast_functions_Delegate281", None)
        self.__gast_functions_Delegate281 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Function282"):
                    opp_val = getattr(item, "Function282", None)
                    
                    if opp_val == self:
                        setattr(item, "Function282", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Function282"):
                    opp_val = getattr(item, "Function282", None)
                    
                    setattr(item, "Function282", self)
                    

    @property
    def gast_functions_Delegate(self):
        return self.__gast_functions_Delegate

    @gast_functions_Delegate.setter
    def gast_functions_Delegate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Delegate__gast_functions_Delegate", None)
        self.__gast_functions_Delegate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GASTClass279"):
                opp_val = getattr(old_value, "GASTClass279", None)
                if opp_val == self:
                    setattr(old_value, "GASTClass279", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTClass279"):
                opp_val = getattr(value, "GASTClass279", None)
                setattr(value, "GASTClass279", self)

class gast_functions_Constructor(functions_Function, types_Member):

    def __init__(self, initializer: bool, constructors: "GASTClass" = None):
        self.initializer = initializer
        self.constructors = constructors
        
        pass
    @property
    def initializer(self):
        return self.__initializer

    @initializer.setter
    def initializer(self, initializer: bool):
        self.__initializer = initializer


    @property
    def constructors(self):
        return self.__constructors

    @constructors.setter
    def constructors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Constructor__constructors", None)
        self.__constructors = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GASTClass288"):
                opp_val = getattr(old_value, "GASTClass288", None)
                if opp_val == self:
                    setattr(old_value, "GASTClass288", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTClass288"):
                opp_val = getattr(value, "GASTClass288", None)
                setattr(value, "GASTClass288", self)

class gast_variables_Property(variables_Field, types_Member):

    pass
class gast_types_TypeAlias(types_Member, types_TypeDecorator):

    def __init__(self, innerTypeAlias: bool, gast_types_TypeAlias: "GASTType" = None, innerTypeAliases: "GASTClass" = None, typeAliases: "Package" = None):
        self.innerTypeAlias = innerTypeAlias
        self.gast_types_TypeAlias = gast_types_TypeAlias
        self.innerTypeAliases = innerTypeAliases
        self.typeAliases = typeAliases
        
        pass
    @property
    def innerTypeAlias(self):
        return self.__innerTypeAlias

    @innerTypeAlias.setter
    def innerTypeAlias(self, innerTypeAlias: bool):
        self.__innerTypeAlias = innerTypeAlias


    @property
    def innerTypeAliases(self):
        return self.__innerTypeAliases

    @innerTypeAliases.setter
    def innerTypeAliases(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_TypeAlias__innerTypeAliases", None)
        self.__innerTypeAliases = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GASTClass189"):
                opp_val = getattr(old_value, "GASTClass189", None)
                if opp_val == self:
                    setattr(old_value, "GASTClass189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTClass189"):
                opp_val = getattr(value, "GASTClass189", None)
                setattr(value, "GASTClass189", self)

    @property
    def gast_types_TypeAlias(self):
        return self.__gast_types_TypeAlias

    @gast_types_TypeAlias.setter
    def gast_types_TypeAlias(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_TypeAlias__gast_types_TypeAlias", None)
        self.__gast_types_TypeAlias = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GASTType187"):
                opp_val = getattr(old_value, "GASTType187", None)
                if opp_val == self:
                    setattr(old_value, "GASTType187", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTType187"):
                opp_val = getattr(value, "GASTType187", None)
                setattr(value, "GASTType187", self)

    @property
    def typeAliases(self):
        return self.__typeAliases

    @typeAliases.setter
    def typeAliases(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_TypeAlias__typeAliases", None)
        self.__typeAliases = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package191"):
                opp_val = getattr(old_value, "Package191", None)
                if opp_val == self:
                    setattr(old_value, "Package191", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package191"):
                opp_val = getattr(value, "Package191", None)
                setattr(value, "Package191", self)

class TypeDecorator:

    pass
class gast_types_GASTArray(TypeDecorator):

    def __init__(self, dimensions: int, gast_types_GASTArray: "GASTType" = None):
        self.dimensions = dimensions
        self.gast_types_GASTArray = gast_types_GASTArray
        
        pass
    @property
    def dimensions(self):
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, dimensions: int):
        self.__dimensions = dimensions


    @property
    def gast_types_GASTArray(self):
        return self.__gast_types_GASTArray

    @gast_types_GASTArray.setter
    def gast_types_GASTArray(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTArray__gast_types_GASTArray", None)
        self.__gast_types_GASTArray = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GASTType185"):
                opp_val = getattr(old_value, "GASTType185", None)
                if opp_val == self:
                    setattr(old_value, "GASTType185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTType185"):
                opp_val = getattr(value, "GASTType185", None)
                setattr(value, "GASTType185", self)

class gast_types_Reference(TypeDecorator):

    def __init__(self, explicit: bool, gast_types_Reference: "GASTType" = None):
        self.explicit = explicit
        self.gast_types_Reference = gast_types_Reference
        
        pass
    @property
    def explicit(self):
        return self.__explicit

    @explicit.setter
    def explicit(self, explicit: bool):
        self.__explicit = explicit


    @property
    def gast_types_Reference(self):
        return self.__gast_types_Reference

    @gast_types_Reference.setter
    def gast_types_Reference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_Reference__gast_types_Reference", None)
        self.__gast_types_Reference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GASTType178"):
                opp_val = getattr(old_value, "GASTType178", None)
                if opp_val == self:
                    setattr(old_value, "GASTType178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTType178"):
                opp_val = getattr(value, "GASTType178", None)
                setattr(value, "GASTType178", self)

class gast_annotations_ModelAnnotation(ABC):

    pass
class core_SourceEntity:

    pass
class core_NamedModelElement:

    pass
class gast_variables_Variable(core_SourceEntity, core_NamedModelElement):

    def __init__(self, const: bool, gast_variables_Variable: "GASTType" = None, surroundingVariable: "DeclarationTypeAccess" = None):
        self.const = const
        self.gast_variables_Variable = gast_variables_Variable
        self.surroundingVariable = surroundingVariable
        
        pass
    @property
    def const(self):
        return self.__const

    @const.setter
    def const(self, const: bool):
        self.__const = const


    @property
    def gast_variables_Variable(self):
        return self.__gast_variables_Variable

    @gast_variables_Variable.setter
    def gast_variables_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_variables_Variable__gast_variables_Variable", None)
        self.__gast_variables_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GASTType320"):
                opp_val = getattr(old_value, "GASTType320", None)
                if opp_val == self:
                    setattr(old_value, "GASTType320", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTType320"):
                opp_val = getattr(value, "GASTType320", None)
                setattr(value, "GASTType320", self)

    @property
    def surroundingVariable(self):
        return self.__surroundingVariable

    @surroundingVariable.setter
    def surroundingVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_variables_Variable__surroundingVariable", None)
        self.__surroundingVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DeclarationTypeAccess322"):
                opp_val = getattr(old_value, "DeclarationTypeAccess322", None)
                if opp_val == self:
                    setattr(old_value, "DeclarationTypeAccess322", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DeclarationTypeAccess322"):
                opp_val = getattr(value, "DeclarationTypeAccess322", None)
                setattr(value, "DeclarationTypeAccess322", self)

class gast_functions_Function(core_SourceEntity, core_NamedModelElement):

    def __init__(self, numberOfStatements: int, maximumNestingLevel: int, linesOfComments: int, linesOfCode: int, numberOfEdgesInCFG: int, numberOfNodesInCFG: int, operator: bool, function: "DeclarationTypeAccess" = None, surroundingFunction: set["FormalParameter"] = None, surroundingFunction303: set["LocalVariable"] = None, gast_functions_Function: set["Statement"] = None, gast_functions_Function307: set["ThrowTypeAccess"] = None, gast_functions_Function309: set["Access"] = None, surroundingFunction315: set["GASTClass"] = None, surroundingFunction312: "BlockStatement" = None):
        self.numberOfStatements = numberOfStatements
        self.maximumNestingLevel = maximumNestingLevel
        self.linesOfComments = linesOfComments
        self.linesOfCode = linesOfCode
        self.numberOfEdgesInCFG = numberOfEdgesInCFG
        self.numberOfNodesInCFG = numberOfNodesInCFG
        self.operator = operator
        self.function = function
        self.surroundingFunction = surroundingFunction if surroundingFunction is not None else set()
        self.surroundingFunction303 = surroundingFunction303 if surroundingFunction303 is not None else set()
        self.gast_functions_Function = gast_functions_Function if gast_functions_Function is not None else set()
        self.gast_functions_Function307 = gast_functions_Function307 if gast_functions_Function307 is not None else set()
        self.gast_functions_Function309 = gast_functions_Function309 if gast_functions_Function309 is not None else set()
        self.surroundingFunction315 = surroundingFunction315 if surroundingFunction315 is not None else set()
        self.surroundingFunction312 = surroundingFunction312
        
        pass
    @property
    def maximumNestingLevel(self):
        return self.__maximumNestingLevel

    @maximumNestingLevel.setter
    def maximumNestingLevel(self, maximumNestingLevel: int):
        self.__maximumNestingLevel = maximumNestingLevel


    @property
    def linesOfCode(self):
        return self.__linesOfCode

    @linesOfCode.setter
    def linesOfCode(self, linesOfCode: int):
        self.__linesOfCode = linesOfCode


    @property
    def numberOfStatements(self):
        return self.__numberOfStatements

    @numberOfStatements.setter
    def numberOfStatements(self, numberOfStatements: int):
        self.__numberOfStatements = numberOfStatements


    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: bool):
        self.__operator = operator


    @property
    def numberOfNodesInCFG(self):
        return self.__numberOfNodesInCFG

    @numberOfNodesInCFG.setter
    def numberOfNodesInCFG(self, numberOfNodesInCFG: int):
        self.__numberOfNodesInCFG = numberOfNodesInCFG


    @property
    def numberOfEdgesInCFG(self):
        return self.__numberOfEdgesInCFG

    @numberOfEdgesInCFG.setter
    def numberOfEdgesInCFG(self, numberOfEdgesInCFG: int):
        self.__numberOfEdgesInCFG = numberOfEdgesInCFG


    @property
    def linesOfComments(self):
        return self.__linesOfComments

    @linesOfComments.setter
    def linesOfComments(self, linesOfComments: int):
        self.__linesOfComments = linesOfComments


    @property
    def surroundingFunction315(self):
        return self.__surroundingFunction315

    @surroundingFunction315.setter
    def surroundingFunction315(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Function__surroundingFunction315", None)
        self.__surroundingFunction315 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass316"):
                    opp_val = getattr(item, "GASTClass316", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass316", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass316"):
                    opp_val = getattr(item, "GASTClass316", None)
                    
                    setattr(item, "GASTClass316", self)
                    

    @property
    def gast_functions_Function309(self):
        return self.__gast_functions_Function309

    @gast_functions_Function309.setter
    def gast_functions_Function309(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Function__gast_functions_Function309", None)
        self.__gast_functions_Function309 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Access310"):
                    opp_val = getattr(item, "Access310", None)
                    
                    if opp_val == self:
                        setattr(item, "Access310", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Access310"):
                    opp_val = getattr(item, "Access310", None)
                    
                    setattr(item, "Access310", self)
                    

    @property
    def function(self):
        return self.__function

    @function.setter
    def function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Function__function", None)
        self.__function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DeclarationTypeAccess"):
                opp_val = getattr(old_value, "DeclarationTypeAccess", None)
                if opp_val == self:
                    setattr(old_value, "DeclarationTypeAccess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DeclarationTypeAccess"):
                opp_val = getattr(value, "DeclarationTypeAccess", None)
                setattr(value, "DeclarationTypeAccess", self)

    @property
    def surroundingFunction303(self):
        return self.__surroundingFunction303

    @surroundingFunction303.setter
    def surroundingFunction303(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Function__surroundingFunction303", None)
        self.__surroundingFunction303 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LocalVariable"):
                    opp_val = getattr(item, "LocalVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "LocalVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LocalVariable"):
                    opp_val = getattr(item, "LocalVariable", None)
                    
                    setattr(item, "LocalVariable", self)
                    

    @property
    def gast_functions_Function(self):
        return self.__gast_functions_Function

    @gast_functions_Function.setter
    def gast_functions_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Function__gast_functions_Function", None)
        self.__gast_functions_Function = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Statement305"):
                    opp_val = getattr(item, "Statement305", None)
                    
                    if opp_val == self:
                        setattr(item, "Statement305", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Statement305"):
                    opp_val = getattr(item, "Statement305", None)
                    
                    setattr(item, "Statement305", self)
                    

    @property
    def surroundingFunction312(self):
        return self.__surroundingFunction312

    @surroundingFunction312.setter
    def surroundingFunction312(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Function__surroundingFunction312", None)
        self.__surroundingFunction312 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BlockStatement313"):
                opp_val = getattr(old_value, "BlockStatement313", None)
                if opp_val == self:
                    setattr(old_value, "BlockStatement313", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BlockStatement313"):
                opp_val = getattr(value, "BlockStatement313", None)
                setattr(value, "BlockStatement313", self)

    @property
    def surroundingFunction(self):
        return self.__surroundingFunction

    @surroundingFunction.setter
    def surroundingFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Function__surroundingFunction", None)
        self.__surroundingFunction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FormalParameter"):
                    opp_val = getattr(item, "FormalParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "FormalParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FormalParameter"):
                    opp_val = getattr(item, "FormalParameter", None)
                    
                    setattr(item, "FormalParameter", self)
                    

    @property
    def gast_functions_Function307(self):
        return self.__gast_functions_Function307

    @gast_functions_Function307.setter
    def gast_functions_Function307(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Function__gast_functions_Function307", None)
        self.__gast_functions_Function307 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ThrowTypeAccess"):
                    opp_val = getattr(item, "ThrowTypeAccess", None)
                    
                    if opp_val == self:
                        setattr(item, "ThrowTypeAccess", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ThrowTypeAccess"):
                    opp_val = getattr(item, "ThrowTypeAccess", None)
                    
                    setattr(item, "ThrowTypeAccess", self)
                    

class core_ModelElement:

    pass
class annotations_ModelAnnotation:

    pass
class gast_annotations_StructuralAbstraction(annotations_ModelAnnotation, core_NamedModelElement):

    pass
class gast_annotations_Clone(core_ModelElement, annotations_ModelAnnotation):

    pass
class gast_annotations_Comment(annotations_ModelAnnotation, core_SourceEntity):

    def __init__(self, formal: bool, todoCount: int, texts: str, todo: bool):
        self.formal = formal
        self.todoCount = todoCount
        self.texts = texts
        self.todo = todo
        
        pass
    @property
    def todoCount(self):
        return self.__todoCount

    @todoCount.setter
    def todoCount(self, todoCount: int):
        self.__todoCount = todoCount


    @property
    def formal(self):
        return self.__formal

    @formal.setter
    def formal(self, formal: bool):
        self.__formal = formal


    @property
    def todo(self):
        return self.__todo

    @todo.setter
    def todo(self, todo: bool):
        self.__todo = todo


    @property
    def texts(self):
        return self.__texts

    @texts.setter
    def texts(self, texts: str):
        self.__texts = texts


    def OCLtodo(self, gast_context, gast_diagnostics) :
        # TODO: Implement OCLtodo method
        pass

class gast_annotations_CloneInstance(core_ModelElement, annotations_ModelAnnotation):

    pass
class types_GASTClass:

    pass
class gast_types_GenericClass(types_GASTClass, core_GenericEntity):

    pass
class gast_annotations_Attribute(annotations_ModelAnnotation, types_GASTClass):

    pass
class Position:

    pass
class gast_core_Position:

    def __init__(self, endColumn: int, startColumn: int, endLine: int, startLine: int, gast_core_Position: "File" = None, gast_core_Position163: "File" = None, position: "SourceEntity" = None):
        self.endColumn = endColumn
        self.startColumn = startColumn
        self.endLine = endLine
        self.startLine = startLine
        self.gast_core_Position = gast_core_Position
        self.gast_core_Position163 = gast_core_Position163
        self.position = position
        
        pass
    @property
    def endColumn(self):
        return self.__endColumn

    @endColumn.setter
    def endColumn(self, endColumn: int):
        self.__endColumn = endColumn


    @property
    def startColumn(self):
        return self.__startColumn

    @startColumn.setter
    def startColumn(self, startColumn: int):
        self.__startColumn = startColumn


    @property
    def endLine(self):
        return self.__endLine

    @endLine.setter
    def endLine(self, endLine: int):
        self.__endLine = endLine


    @property
    def startLine(self):
        return self.__startLine

    @startLine.setter
    def startLine(self, startLine: int):
        self.__startLine = startLine


    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Position__position", None)
        self.__position = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SourceEntity"):
                opp_val = getattr(old_value, "SourceEntity", None)
                if opp_val == self:
                    setattr(old_value, "SourceEntity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SourceEntity"):
                opp_val = getattr(value, "SourceEntity", None)
                setattr(value, "SourceEntity", self)

    @property
    def gast_core_Position163(self):
        return self.__gast_core_Position163

    @gast_core_Position163.setter
    def gast_core_Position163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Position__gast_core_Position163", None)
        self.__gast_core_Position163 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "File164"):
                opp_val = getattr(old_value, "File164", None)
                if opp_val == self:
                    setattr(old_value, "File164", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "File164"):
                opp_val = getattr(value, "File164", None)
                setattr(value, "File164", self)

    @property
    def gast_core_Position(self):
        return self.__gast_core_Position

    @gast_core_Position.setter
    def gast_core_Position(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Position__gast_core_Position", None)
        self.__gast_core_Position = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "File161"):
                opp_val = getattr(old_value, "File161", None)
                if opp_val == self:
                    setattr(old_value, "File161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "File161"):
                opp_val = getattr(value, "File161", None)
                setattr(value, "File161", self)

    def EitherAssemblyFileOrSourceFileSet(self, gast_diagnostics, gast_context) :
        # TODO: Implement EitherAssemblyFileOrSourceFileSet method
        pass

class File:

    pass
class BasePath:

    pass
class GASTType:

    pass
class gast_types_TypeDecorator(GASTType):

    pass
class StructuralAbstraction:

    pass
class gast_annotations_Layer(StructuralAbstraction):

    pass
class gast_annotations_Subsystem(StructuralAbstraction):

    pass
class Clone:

    pass
class TypeParameterClass:

    pass
class TypeAlias:

    pass
class BaseAccess:

    pass
class gast_accesses_CompositeAccess(BaseAccess):

    pass
class gast_accesses_Access(BaseAccess):

    pass
class SourceEntity:

    pass
class gast_types_Member(SourceEntity):

    def __init__(self, visibility: str, abstract: bool, extern: bool, final: bool, internal: bool, introspectable: bool, typeParameterClassMember: bool, virtual: bool, override: bool, static: bool, gast_types_Member: "Member" = None, SourceEntity: "gast_core_Position" = None):
        self.visibility = visibility
        self.abstract = abstract
        self.extern = extern
        self.final = final
        self.internal = internal
        self.introspectable = introspectable
        self.typeParameterClassMember = typeParameterClassMember
        self.virtual = virtual
        self.override = override
        self.static = static
        self.gast_types_Member = gast_types_Member
        
        pass
    @property
    def static(self):
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static


    @property
    def final(self):
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final


    @property
    def visibility(self):
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility


    @property
    def override(self):
        return self.__override

    @override.setter
    def override(self, override: bool):
        self.__override = override


    @property
    def internal(self):
        return self.__internal

    @internal.setter
    def internal(self, internal: bool):
        self.__internal = internal


    @property
    def introspectable(self):
        return self.__introspectable

    @introspectable.setter
    def introspectable(self, introspectable: bool):
        self.__introspectable = introspectable


    @property
    def typeParameterClassMember(self):
        return self.__typeParameterClassMember

    @typeParameterClassMember.setter
    def typeParameterClassMember(self, typeParameterClassMember: bool):
        self.__typeParameterClassMember = typeParameterClassMember


    @property
    def abstract(self):
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract


    @property
    def extern(self):
        return self.__extern

    @extern.setter
    def extern(self, extern: bool):
        self.__extern = extern


    @property
    def virtual(self):
        return self.__virtual

    @virtual.setter
    def virtual(self, virtual: bool):
        self.__virtual = virtual


    @property
    def gast_types_Member(self):
        return self.__gast_types_Member

    @gast_types_Member.setter
    def gast_types_Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_Member__gast_types_Member", None)
        self.__gast_types_Member = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Member"):
                opp_val = getattr(old_value, "Member", None)
                if opp_val == self:
                    setattr(old_value, "Member", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Member"):
                opp_val = getattr(value, "Member", None)
                setattr(value, "Member", self)

    def getSurroundingClass(self) :
        # TODO: Implement getSurroundingClass method
        pass

class gast_accesses_BaseAccess(SourceEntity):

    pass
class gast_statements_Statement(SourceEntity):

    def __init__(self, numberOfStatements: int, linesOfCode: int, numberOfEdgesInCFG: int, numberOfNodesInCFG: int, maximumNestingLevel: int, numberOfComments: int, gast_statements_Statement: "Statement" = None, statement: "Branch" = None, body: "LoopStatement" = None, gast_statements_Statement15: set["Statement"] = None, gast_statements_Statement18: set["Statement"] = None, parentStatement: set["BaseAccess"] = None, statements: "CloneInstance" = None, statements9: "BlockStatement" = None, SourceEntity: "gast_core_Position" = None):
        self.numberOfStatements = numberOfStatements
        self.linesOfCode = linesOfCode
        self.numberOfEdgesInCFG = numberOfEdgesInCFG
        self.numberOfNodesInCFG = numberOfNodesInCFG
        self.maximumNestingLevel = maximumNestingLevel
        self.numberOfComments = numberOfComments
        self.gast_statements_Statement = gast_statements_Statement
        self.statement = statement
        self.body = body
        self.gast_statements_Statement15 = gast_statements_Statement15 if gast_statements_Statement15 is not None else set()
        self.gast_statements_Statement18 = gast_statements_Statement18 if gast_statements_Statement18 is not None else set()
        self.parentStatement = parentStatement if parentStatement is not None else set()
        self.statements = statements
        self.statements9 = statements9
        
        pass
    @property
    def maximumNestingLevel(self):
        return self.__maximumNestingLevel

    @maximumNestingLevel.setter
    def maximumNestingLevel(self, maximumNestingLevel: int):
        self.__maximumNestingLevel = maximumNestingLevel


    @property
    def numberOfComments(self):
        return self.__numberOfComments

    @numberOfComments.setter
    def numberOfComments(self, numberOfComments: int):
        self.__numberOfComments = numberOfComments


    @property
    def numberOfEdgesInCFG(self):
        return self.__numberOfEdgesInCFG

    @numberOfEdgesInCFG.setter
    def numberOfEdgesInCFG(self, numberOfEdgesInCFG: int):
        self.__numberOfEdgesInCFG = numberOfEdgesInCFG


    @property
    def linesOfCode(self):
        return self.__linesOfCode

    @linesOfCode.setter
    def linesOfCode(self, linesOfCode: int):
        self.__linesOfCode = linesOfCode


    @property
    def numberOfStatements(self):
        return self.__numberOfStatements

    @numberOfStatements.setter
    def numberOfStatements(self, numberOfStatements: int):
        self.__numberOfStatements = numberOfStatements


    @property
    def numberOfNodesInCFG(self):
        return self.__numberOfNodesInCFG

    @numberOfNodesInCFG.setter
    def numberOfNodesInCFG(self, numberOfNodesInCFG: int):
        self.__numberOfNodesInCFG = numberOfNodesInCFG


    @property
    def parentStatement(self):
        return self.__parentStatement

    @parentStatement.setter
    def parentStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_Statement__parentStatement", None)
        self.__parentStatement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BaseAccess"):
                    opp_val = getattr(item, "BaseAccess", None)
                    
                    if opp_val == self:
                        setattr(item, "BaseAccess", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BaseAccess"):
                    opp_val = getattr(item, "BaseAccess", None)
                    
                    setattr(item, "BaseAccess", self)
                    

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_Statement__body", None)
        self.__body = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LoopStatement"):
                opp_val = getattr(old_value, "LoopStatement", None)
                if opp_val == self:
                    setattr(old_value, "LoopStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LoopStatement"):
                opp_val = getattr(value, "LoopStatement", None)
                setattr(value, "LoopStatement", self)

    @property
    def gast_statements_Statement(self):
        return self.__gast_statements_Statement

    @gast_statements_Statement.setter
    def gast_statements_Statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_Statement__gast_statements_Statement", None)
        self.__gast_statements_Statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Statement"):
                opp_val = getattr(old_value, "Statement", None)
                if opp_val == self:
                    setattr(old_value, "Statement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Statement"):
                opp_val = getattr(value, "Statement", None)
                setattr(value, "Statement", self)

    @property
    def gast_statements_Statement15(self):
        return self.__gast_statements_Statement15

    @gast_statements_Statement15.setter
    def gast_statements_Statement15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_Statement__gast_statements_Statement15", None)
        self.__gast_statements_Statement15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Statement16"):
                    opp_val = getattr(item, "Statement16", None)
                    
                    if opp_val == self:
                        setattr(item, "Statement16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Statement16"):
                    opp_val = getattr(item, "Statement16", None)
                    
                    setattr(item, "Statement16", self)
                    

    @property
    def statements9(self):
        return self.__statements9

    @statements9.setter
    def statements9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_Statement__statements9", None)
        self.__statements9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BlockStatement10"):
                opp_val = getattr(old_value, "BlockStatement10", None)
                if opp_val == self:
                    setattr(old_value, "BlockStatement10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BlockStatement10"):
                opp_val = getattr(value, "BlockStatement10", None)
                setattr(value, "BlockStatement10", self)

    @property
    def gast_statements_Statement18(self):
        return self.__gast_statements_Statement18

    @gast_statements_Statement18.setter
    def gast_statements_Statement18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_Statement__gast_statements_Statement18", None)
        self.__gast_statements_Statement18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Statement19"):
                    opp_val = getattr(item, "Statement19", None)
                    
                    if opp_val == self:
                        setattr(item, "Statement19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Statement19"):
                    opp_val = getattr(item, "Statement19", None)
                    
                    setattr(item, "Statement19", self)
                    

    @property
    def statements(self):
        return self.__statements

    @statements.setter
    def statements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_Statement__statements", None)
        self.__statements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CloneInstance"):
                opp_val = getattr(old_value, "CloneInstance", None)
                if opp_val == self:
                    setattr(old_value, "CloneInstance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CloneInstance"):
                opp_val = getattr(value, "CloneInstance", None)
                setattr(value, "CloneInstance", self)

    @property
    def statement(self):
        return self.__statement

    @statement.setter
    def statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_Statement__statement", None)
        self.__statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Branch"):
                opp_val = getattr(old_value, "Branch", None)
                if opp_val == self:
                    setattr(old_value, "Branch", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Branch"):
                opp_val = getattr(value, "Branch", None)
                setattr(value, "Branch", self)

class BlockStatement:

    pass
class CatchBlock:

    pass
class Statement:

    pass
class gast_statements_ExceptionHandler(Statement):

    pass
class GASTClass:

    pass
class gast_types_TypeParameterClass(GASTClass):

    pass
class gast_types_GASTEnumeration(GASTClass):

    pass
class gast_types_GASTUnion(GASTClass):

    pass
class gast_types_GASTStruct(GASTClass):

    pass
class Package:

    pass
class gast_core_PackageAlias(Package):

    pass
class GlobalVariable:

    pass
class GlobalFunction:

    pass
class Delegate:

    pass
class Access:

    pass
class gast_accesses_FunctionAccess(Access):

    pass
class gast_accesses_VariableAccess(Access):

    def __init__(self, write: bool, gast_accesses_VariableAccess: "Variable" = None, Access310: "gast_functions_Function" = None, Access: "gast_core_Package" = None, Access91: "gast_core_Root" = None, Access235: "gast_types_GASTClass" = None):
        self.write = write
        self.gast_accesses_VariableAccess = gast_accesses_VariableAccess
        
        pass
    @property
    def write(self):
        return self.__write

    @write.setter
    def write(self, write: bool):
        self.__write = write


    @property
    def gast_accesses_VariableAccess(self):
        return self.__gast_accesses_VariableAccess

    @gast_accesses_VariableAccess.setter
    def gast_accesses_VariableAccess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_accesses_VariableAccess__gast_accesses_VariableAccess", None)
        self.__gast_accesses_VariableAccess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Variable272"):
                opp_val = getattr(old_value, "Variable272", None)
                if opp_val == self:
                    setattr(old_value, "Variable272", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable272"):
                opp_val = getattr(value, "Variable272", None)
                setattr(value, "Variable272", self)

class gast_accesses_TypeAccess(Access):

    pass
class gast_statements_Var:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class NamedModelElement:

    pass
class gast_core_Directory(NamedModelElement):

    def __init__(self, fullQualifiedPath: str, fileSystemPath: str, parentDirectory: set["Directory"] = None, subDirectory: "Directory" = None, directory: set["File"] = None, directories: "BasePath" = None):
        self.fullQualifiedPath = fullQualifiedPath
        self.fileSystemPath = fileSystemPath
        self.parentDirectory = parentDirectory if parentDirectory is not None else set()
        self.subDirectory = subDirectory
        self.directory = directory if directory is not None else set()
        self.directories = directories
        
        pass
    @property
    def fullQualifiedPath(self):
        return self.__fullQualifiedPath

    @fullQualifiedPath.setter
    def fullQualifiedPath(self, fullQualifiedPath: str):
        self.__fullQualifiedPath = fullQualifiedPath


    @property
    def fileSystemPath(self):
        return self.__fileSystemPath

    @fileSystemPath.setter
    def fileSystemPath(self, fileSystemPath: str):
        self.__fileSystemPath = fileSystemPath


    @property
    def parentDirectory(self):
        return self.__parentDirectory

    @parentDirectory.setter
    def parentDirectory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Directory__parentDirectory", None)
        self.__parentDirectory = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Directory126"):
                    opp_val = getattr(item, "Directory126", None)
                    
                    if opp_val == self:
                        setattr(item, "Directory126", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Directory126"):
                    opp_val = getattr(item, "Directory126", None)
                    
                    setattr(item, "Directory126", self)
                    

    @property
    def directories(self):
        return self.__directories

    @directories.setter
    def directories(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Directory__directories", None)
        self.__directories = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasePath131"):
                opp_val = getattr(old_value, "BasePath131", None)
                if opp_val == self:
                    setattr(old_value, "BasePath131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasePath131"):
                opp_val = getattr(value, "BasePath131", None)
                setattr(value, "BasePath131", self)

    @property
    def subDirectory(self):
        return self.__subDirectory

    @subDirectory.setter
    def subDirectory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Directory__subDirectory", None)
        self.__subDirectory = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Directory128"):
                opp_val = getattr(old_value, "Directory128", None)
                if opp_val == self:
                    setattr(old_value, "Directory128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Directory128"):
                opp_val = getattr(value, "Directory128", None)
                setattr(value, "Directory128", self)

    @property
    def directory(self):
        return self.__directory

    @directory.setter
    def directory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Directory__directory", None)
        self.__directory = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "File"):
                    opp_val = getattr(item, "File", None)
                    
                    if opp_val == self:
                        setattr(item, "File", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "File"):
                    opp_val = getattr(item, "File", None)
                    
                    setattr(item, "File", self)
                    

class gast_core_File(NamedModelElement):

    def __init__(self, sourceFile: bool, linesOfCode: int, size: str, fullQualifiedPath: str, assemblyFile: bool, fileSystemPath: str, gast_core_File: "Root" = None, gast_core_File135: set["GASTType"] = None, gast_core_File138: set["GASTType"] = None, gast_core_File141: set["GlobalVariable"] = None, gast_core_File144: set["GlobalFunction"] = None, gast_core_File147: set["GlobalFunction"] = None, gast_core_File150: set["GlobalVariable"] = None, gast_core_File153: set["Package"] = None, gast_core_File156: set["File"] = None, files: "Directory" = None):
        self.sourceFile = sourceFile
        self.linesOfCode = linesOfCode
        self.size = size
        self.fullQualifiedPath = fullQualifiedPath
        self.assemblyFile = assemblyFile
        self.fileSystemPath = fileSystemPath
        self.gast_core_File = gast_core_File
        self.gast_core_File135 = gast_core_File135 if gast_core_File135 is not None else set()
        self.gast_core_File138 = gast_core_File138 if gast_core_File138 is not None else set()
        self.gast_core_File141 = gast_core_File141 if gast_core_File141 is not None else set()
        self.gast_core_File144 = gast_core_File144 if gast_core_File144 is not None else set()
        self.gast_core_File147 = gast_core_File147 if gast_core_File147 is not None else set()
        self.gast_core_File150 = gast_core_File150 if gast_core_File150 is not None else set()
        self.gast_core_File153 = gast_core_File153 if gast_core_File153 is not None else set()
        self.gast_core_File156 = gast_core_File156 if gast_core_File156 is not None else set()
        self.files = files
        
        pass
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size


    @property
    def linesOfCode(self):
        return self.__linesOfCode

    @linesOfCode.setter
    def linesOfCode(self, linesOfCode: int):
        self.__linesOfCode = linesOfCode


    @property
    def fileSystemPath(self):
        return self.__fileSystemPath

    @fileSystemPath.setter
    def fileSystemPath(self, fileSystemPath: str):
        self.__fileSystemPath = fileSystemPath


    @property
    def fullQualifiedPath(self):
        return self.__fullQualifiedPath

    @fullQualifiedPath.setter
    def fullQualifiedPath(self, fullQualifiedPath: str):
        self.__fullQualifiedPath = fullQualifiedPath


    @property
    def assemblyFile(self):
        return self.__assemblyFile

    @assemblyFile.setter
    def assemblyFile(self, assemblyFile: bool):
        self.__assemblyFile = assemblyFile


    @property
    def sourceFile(self):
        return self.__sourceFile

    @sourceFile.setter
    def sourceFile(self, sourceFile: bool):
        self.__sourceFile = sourceFile


    @property
    def gast_core_File(self):
        return self.__gast_core_File

    @gast_core_File.setter
    def gast_core_File(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File", None)
        self.__gast_core_File = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Root133"):
                opp_val = getattr(old_value, "Root133", None)
                if opp_val == self:
                    setattr(old_value, "Root133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Root133"):
                opp_val = getattr(value, "Root133", None)
                setattr(value, "Root133", self)

    @property
    def gast_core_File138(self):
        return self.__gast_core_File138

    @gast_core_File138.setter
    def gast_core_File138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File138", None)
        self.__gast_core_File138 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTType139"):
                    opp_val = getattr(item, "GASTType139", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTType139", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTType139"):
                    opp_val = getattr(item, "GASTType139", None)
                    
                    setattr(item, "GASTType139", self)
                    

    @property
    def gast_core_File153(self):
        return self.__gast_core_File153

    @gast_core_File153.setter
    def gast_core_File153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File153", None)
        self.__gast_core_File153 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package154"):
                    opp_val = getattr(item, "Package154", None)
                    
                    if opp_val == self:
                        setattr(item, "Package154", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package154"):
                    opp_val = getattr(item, "Package154", None)
                    
                    setattr(item, "Package154", self)
                    

    @property
    def gast_core_File156(self):
        return self.__gast_core_File156

    @gast_core_File156.setter
    def gast_core_File156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File156", None)
        self.__gast_core_File156 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "File157"):
                    opp_val = getattr(item, "File157", None)
                    
                    if opp_val == self:
                        setattr(item, "File157", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "File157"):
                    opp_val = getattr(item, "File157", None)
                    
                    setattr(item, "File157", self)
                    

    @property
    def files(self):
        return self.__files

    @files.setter
    def files(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__files", None)
        self.__files = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Directory159"):
                opp_val = getattr(old_value, "Directory159", None)
                if opp_val == self:
                    setattr(old_value, "Directory159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Directory159"):
                opp_val = getattr(value, "Directory159", None)
                setattr(value, "Directory159", self)

    @property
    def gast_core_File135(self):
        return self.__gast_core_File135

    @gast_core_File135.setter
    def gast_core_File135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File135", None)
        self.__gast_core_File135 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTType136"):
                    opp_val = getattr(item, "GASTType136", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTType136", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTType136"):
                    opp_val = getattr(item, "GASTType136", None)
                    
                    setattr(item, "GASTType136", self)
                    

    @property
    def gast_core_File150(self):
        return self.__gast_core_File150

    @gast_core_File150.setter
    def gast_core_File150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File150", None)
        self.__gast_core_File150 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalVariable151"):
                    opp_val = getattr(item, "GlobalVariable151", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalVariable151", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalVariable151"):
                    opp_val = getattr(item, "GlobalVariable151", None)
                    
                    setattr(item, "GlobalVariable151", self)
                    

    @property
    def gast_core_File141(self):
        return self.__gast_core_File141

    @gast_core_File141.setter
    def gast_core_File141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File141", None)
        self.__gast_core_File141 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalVariable142"):
                    opp_val = getattr(item, "GlobalVariable142", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalVariable142", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalVariable142"):
                    opp_val = getattr(item, "GlobalVariable142", None)
                    
                    setattr(item, "GlobalVariable142", self)
                    

    @property
    def gast_core_File147(self):
        return self.__gast_core_File147

    @gast_core_File147.setter
    def gast_core_File147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File147", None)
        self.__gast_core_File147 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalFunction148"):
                    opp_val = getattr(item, "GlobalFunction148", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalFunction148", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalFunction148"):
                    opp_val = getattr(item, "GlobalFunction148", None)
                    
                    setattr(item, "GlobalFunction148", self)
                    

    @property
    def gast_core_File144(self):
        return self.__gast_core_File144

    @gast_core_File144.setter
    def gast_core_File144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File144", None)
        self.__gast_core_File144 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalFunction145"):
                    opp_val = getattr(item, "GlobalFunction145", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalFunction145", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalFunction145"):
                    opp_val = getattr(item, "GlobalFunction145", None)
                    
                    setattr(item, "GlobalFunction145", self)
                    

class gast_types_GASTType(NamedModelElement):

    def __init__(self, qualifiedName: str, referenceType: bool):
        self.qualifiedName = qualifiedName
        self.referenceType = referenceType
        
        pass
    @property
    def qualifiedName(self):
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName


    @property
    def referenceType(self):
        return self.__referenceType

    @referenceType.setter
    def referenceType(self, referenceType: bool):
        self.__referenceType = referenceType


class gast_core_Package(NamedModelElement):

    def __init__(self, linesOfComments: int, linesOfCode: int, qualifiedName: str, gast_core_Package60: set["GASTClass"] = None, gast_core_Package63: set["GASTClass"] = None, gast_core_Package66: set["GASTClass"] = None, gast_core_Package69: set["Access"] = None, surroundingPackage: set["Delegate"] = None, surroundingPackage72: set["GlobalFunction"] = None, surroundingPackage74: set["GlobalVariable"] = None, packages: "Root" = None, surroundingPackage78: set["GASTClass"] = None, surroundingPackage81: set["Package"] = None, gast_core_Package: set["GASTClass"] = None, gast_core_Package85: set["Package"] = None, surroundingPackage88: set["TypeAlias"] = None, subPackages: "Package" = None):
        self.linesOfComments = linesOfComments
        self.linesOfCode = linesOfCode
        self.qualifiedName = qualifiedName
        self.gast_core_Package60 = gast_core_Package60 if gast_core_Package60 is not None else set()
        self.gast_core_Package63 = gast_core_Package63 if gast_core_Package63 is not None else set()
        self.gast_core_Package66 = gast_core_Package66 if gast_core_Package66 is not None else set()
        self.gast_core_Package69 = gast_core_Package69 if gast_core_Package69 is not None else set()
        self.surroundingPackage = surroundingPackage if surroundingPackage is not None else set()
        self.surroundingPackage72 = surroundingPackage72 if surroundingPackage72 is not None else set()
        self.surroundingPackage74 = surroundingPackage74 if surroundingPackage74 is not None else set()
        self.packages = packages
        self.surroundingPackage78 = surroundingPackage78 if surroundingPackage78 is not None else set()
        self.surroundingPackage81 = surroundingPackage81 if surroundingPackage81 is not None else set()
        self.gast_core_Package = gast_core_Package if gast_core_Package is not None else set()
        self.gast_core_Package85 = gast_core_Package85 if gast_core_Package85 is not None else set()
        self.surroundingPackage88 = surroundingPackage88 if surroundingPackage88 is not None else set()
        self.subPackages = subPackages
        
        pass
    @property
    def linesOfComments(self):
        return self.__linesOfComments

    @linesOfComments.setter
    def linesOfComments(self, linesOfComments: int):
        self.__linesOfComments = linesOfComments


    @property
    def linesOfCode(self):
        return self.__linesOfCode

    @linesOfCode.setter
    def linesOfCode(self, linesOfCode: int):
        self.__linesOfCode = linesOfCode


    @property
    def qualifiedName(self):
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName


    @property
    def gast_core_Package63(self):
        return self.__gast_core_Package63

    @gast_core_Package63.setter
    def gast_core_Package63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__gast_core_Package63", None)
        self.__gast_core_Package63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass64"):
                    opp_val = getattr(item, "GASTClass64", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass64"):
                    opp_val = getattr(item, "GASTClass64", None)
                    
                    setattr(item, "GASTClass64", self)
                    

    @property
    def gast_core_Package85(self):
        return self.__gast_core_Package85

    @gast_core_Package85.setter
    def gast_core_Package85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__gast_core_Package85", None)
        self.__gast_core_Package85 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package86"):
                    opp_val = getattr(item, "Package86", None)
                    
                    if opp_val == self:
                        setattr(item, "Package86", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package86"):
                    opp_val = getattr(item, "Package86", None)
                    
                    setattr(item, "Package86", self)
                    

    @property
    def gast_core_Package69(self):
        return self.__gast_core_Package69

    @gast_core_Package69.setter
    def gast_core_Package69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__gast_core_Package69", None)
        self.__gast_core_Package69 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Access"):
                    opp_val = getattr(item, "Access", None)
                    
                    if opp_val == self:
                        setattr(item, "Access", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Access"):
                    opp_val = getattr(item, "Access", None)
                    
                    setattr(item, "Access", self)
                    

    @property
    def surroundingPackage74(self):
        return self.__surroundingPackage74

    @surroundingPackage74.setter
    def surroundingPackage74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__surroundingPackage74", None)
        self.__surroundingPackage74 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalVariable"):
                    opp_val = getattr(item, "GlobalVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalVariable"):
                    opp_val = getattr(item, "GlobalVariable", None)
                    
                    setattr(item, "GlobalVariable", self)
                    

    @property
    def gast_core_Package66(self):
        return self.__gast_core_Package66

    @gast_core_Package66.setter
    def gast_core_Package66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__gast_core_Package66", None)
        self.__gast_core_Package66 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass67"):
                    opp_val = getattr(item, "GASTClass67", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass67", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass67"):
                    opp_val = getattr(item, "GASTClass67", None)
                    
                    setattr(item, "GASTClass67", self)
                    

    @property
    def gast_core_Package(self):
        return self.__gast_core_Package

    @gast_core_Package.setter
    def gast_core_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__gast_core_Package", None)
        self.__gast_core_Package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass"):
                    opp_val = getattr(item, "GASTClass", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass"):
                    opp_val = getattr(item, "GASTClass", None)
                    
                    setattr(item, "GASTClass", self)
                    

    @property
    def gast_core_Package60(self):
        return self.__gast_core_Package60

    @gast_core_Package60.setter
    def gast_core_Package60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__gast_core_Package60", None)
        self.__gast_core_Package60 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass61"):
                    opp_val = getattr(item, "GASTClass61", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass61", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass61"):
                    opp_val = getattr(item, "GASTClass61", None)
                    
                    setattr(item, "GASTClass61", self)
                    

    @property
    def surroundingPackage(self):
        return self.__surroundingPackage

    @surroundingPackage.setter
    def surroundingPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__surroundingPackage", None)
        self.__surroundingPackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Delegate"):
                    opp_val = getattr(item, "Delegate", None)
                    
                    if opp_val == self:
                        setattr(item, "Delegate", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Delegate"):
                    opp_val = getattr(item, "Delegate", None)
                    
                    setattr(item, "Delegate", self)
                    

    @property
    def surroundingPackage88(self):
        return self.__surroundingPackage88

    @surroundingPackage88.setter
    def surroundingPackage88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__surroundingPackage88", None)
        self.__surroundingPackage88 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypeAlias"):
                    opp_val = getattr(item, "TypeAlias", None)
                    
                    if opp_val == self:
                        setattr(item, "TypeAlias", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypeAlias"):
                    opp_val = getattr(item, "TypeAlias", None)
                    
                    setattr(item, "TypeAlias", self)
                    

    @property
    def surroundingPackage72(self):
        return self.__surroundingPackage72

    @surroundingPackage72.setter
    def surroundingPackage72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__surroundingPackage72", None)
        self.__surroundingPackage72 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalFunction"):
                    opp_val = getattr(item, "GlobalFunction", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalFunction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalFunction"):
                    opp_val = getattr(item, "GlobalFunction", None)
                    
                    setattr(item, "GlobalFunction", self)
                    

    @property
    def subPackages(self):
        return self.__subPackages

    @subPackages.setter
    def subPackages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__subPackages", None)
        self.__subPackages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package83"):
                opp_val = getattr(old_value, "Package83", None)
                if opp_val == self:
                    setattr(old_value, "Package83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package83"):
                opp_val = getattr(value, "Package83", None)
                setattr(value, "Package83", self)

    @property
    def surroundingPackage81(self):
        return self.__surroundingPackage81

    @surroundingPackage81.setter
    def surroundingPackage81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__surroundingPackage81", None)
        self.__surroundingPackage81 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package"):
                    opp_val = getattr(item, "Package", None)
                    
                    if opp_val == self:
                        setattr(item, "Package", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package"):
                    opp_val = getattr(item, "Package", None)
                    
                    setattr(item, "Package", self)
                    

    @property
    def packages(self):
        return self.__packages

    @packages.setter
    def packages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__packages", None)
        self.__packages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Root76"):
                opp_val = getattr(old_value, "Root76", None)
                if opp_val == self:
                    setattr(old_value, "Root76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Root76"):
                opp_val = getattr(value, "Root76", None)
                setattr(value, "Root76", self)

    @property
    def surroundingPackage78(self):
        return self.__surroundingPackage78

    @surroundingPackage78.setter
    def surroundingPackage78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__surroundingPackage78", None)
        self.__surroundingPackage78 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass79"):
                    opp_val = getattr(item, "GASTClass79", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass79", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass79"):
                    opp_val = getattr(item, "GASTClass79", None)
                    
                    setattr(item, "GASTClass79", self)
                    

class gast_core_Identifier(ABC):

    def __init__(self, id: str):
        self.id = id
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    def idHasToBeUnique(self, gast_diagnostics, gast_context) :
        # TODO: Implement idHasToBeUnique method
        pass

class ModelAnnotation:

    pass
class Identifier:

    pass
class gast_core_ModelElement(Identifier):

    def __init__(self, status: str, sissyId: int, gast_core_ModelElement: set["ModelAnnotation"] = None):
        self.status = status
        self.sissyId = sissyId
        self.gast_core_ModelElement = gast_core_ModelElement if gast_core_ModelElement is not None else set()
        
        pass
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status


    @property
    def sissyId(self):
        return self.__sissyId

    @sissyId.setter
    def sissyId(self, sissyId: int):
        self.__sissyId = sissyId


    @property
    def gast_core_ModelElement(self):
        return self.__gast_core_ModelElement

    @gast_core_ModelElement.setter
    def gast_core_ModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_ModelElement__gast_core_ModelElement", None)
        self.__gast_core_ModelElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelAnnotation"):
                    opp_val = getattr(item, "ModelAnnotation", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelAnnotation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelAnnotation"):
                    opp_val = getattr(item, "ModelAnnotation", None)
                    
                    setattr(item, "ModelAnnotation", self)
                    

class Directory:

    pass
class Root:

    pass
class ModelElement:

    pass
class gast_core_GenericEntity(ModelElement):

    pass
class gast_core_Root(ModelElement):

    def __init__(self, linesOfComments: int, linesOfCode: int, root: set["Package"] = None, root112: set["Clone"] = None, gast_core_Root114: set["StructuralAbstraction"] = None, gast_core_Root116: set["GASTType"] = None, gast_core_Root118: set["ModelElement"] = None, gast_core_Root: set["Access"] = None, gast_core_Root93: set["GASTClass"] = None, gast_core_Root96: set["GASTClass"] = None, gast_core_Root99: set["GASTClass"] = None, gast_core_Root102: set["GASTClass"] = None, gast_core_Root107: set["GlobalVariable"] = None, root121: set["BasePath"] = None, root123: set["GlobalFunction"] = None, gast_core_Root105: set["ModelElement"] = None, ModelElement: "gast_core_Root" = None, ModelElement277: "gast_accesses_Access" = None, ModelElement119: "gast_core_Root" = None):
        self.linesOfComments = linesOfComments
        self.linesOfCode = linesOfCode
        self.root = root if root is not None else set()
        self.root112 = root112 if root112 is not None else set()
        self.gast_core_Root114 = gast_core_Root114 if gast_core_Root114 is not None else set()
        self.gast_core_Root116 = gast_core_Root116 if gast_core_Root116 is not None else set()
        self.gast_core_Root118 = gast_core_Root118 if gast_core_Root118 is not None else set()
        self.gast_core_Root = gast_core_Root if gast_core_Root is not None else set()
        self.gast_core_Root93 = gast_core_Root93 if gast_core_Root93 is not None else set()
        self.gast_core_Root96 = gast_core_Root96 if gast_core_Root96 is not None else set()
        self.gast_core_Root99 = gast_core_Root99 if gast_core_Root99 is not None else set()
        self.gast_core_Root102 = gast_core_Root102 if gast_core_Root102 is not None else set()
        self.gast_core_Root107 = gast_core_Root107 if gast_core_Root107 is not None else set()
        self.root121 = root121 if root121 is not None else set()
        self.root123 = root123 if root123 is not None else set()
        self.gast_core_Root105 = gast_core_Root105 if gast_core_Root105 is not None else set()
        
        pass
    @property
    def linesOfCode(self):
        return self.__linesOfCode

    @linesOfCode.setter
    def linesOfCode(self, linesOfCode: int):
        self.__linesOfCode = linesOfCode


    @property
    def linesOfComments(self):
        return self.__linesOfComments

    @linesOfComments.setter
    def linesOfComments(self, linesOfComments: int):
        self.__linesOfComments = linesOfComments


    @property
    def root112(self):
        return self.__root112

    @root112.setter
    def root112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__root112", None)
        self.__root112 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Clone"):
                    opp_val = getattr(item, "Clone", None)
                    
                    if opp_val == self:
                        setattr(item, "Clone", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Clone"):
                    opp_val = getattr(item, "Clone", None)
                    
                    setattr(item, "Clone", self)
                    

    @property
    def root123(self):
        return self.__root123

    @root123.setter
    def root123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__root123", None)
        self.__root123 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalFunction124"):
                    opp_val = getattr(item, "GlobalFunction124", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalFunction124", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalFunction124"):
                    opp_val = getattr(item, "GlobalFunction124", None)
                    
                    setattr(item, "GlobalFunction124", self)
                    

    @property
    def gast_core_Root102(self):
        return self.__gast_core_Root102

    @gast_core_Root102.setter
    def gast_core_Root102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root102", None)
        self.__gast_core_Root102 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass103"):
                    opp_val = getattr(item, "GASTClass103", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass103", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass103"):
                    opp_val = getattr(item, "GASTClass103", None)
                    
                    setattr(item, "GASTClass103", self)
                    

    @property
    def gast_core_Root105(self):
        return self.__gast_core_Root105

    @gast_core_Root105.setter
    def gast_core_Root105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root105", None)
        self.__gast_core_Root105 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelElement"):
                    opp_val = getattr(item, "ModelElement", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelElement"):
                    opp_val = getattr(item, "ModelElement", None)
                    
                    setattr(item, "ModelElement", self)
                    

    @property
    def gast_core_Root116(self):
        return self.__gast_core_Root116

    @gast_core_Root116.setter
    def gast_core_Root116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root116", None)
        self.__gast_core_Root116 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTType"):
                    opp_val = getattr(item, "GASTType", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTType"):
                    opp_val = getattr(item, "GASTType", None)
                    
                    setattr(item, "GASTType", self)
                    

    @property
    def gast_core_Root99(self):
        return self.__gast_core_Root99

    @gast_core_Root99.setter
    def gast_core_Root99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root99", None)
        self.__gast_core_Root99 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass100"):
                    opp_val = getattr(item, "GASTClass100", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass100", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass100"):
                    opp_val = getattr(item, "GASTClass100", None)
                    
                    setattr(item, "GASTClass100", self)
                    

    @property
    def gast_core_Root118(self):
        return self.__gast_core_Root118

    @gast_core_Root118.setter
    def gast_core_Root118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root118", None)
        self.__gast_core_Root118 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelElement119"):
                    opp_val = getattr(item, "ModelElement119", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelElement119", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelElement119"):
                    opp_val = getattr(item, "ModelElement119", None)
                    
                    setattr(item, "ModelElement119", self)
                    

    @property
    def gast_core_Root(self):
        return self.__gast_core_Root

    @gast_core_Root.setter
    def gast_core_Root(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root", None)
        self.__gast_core_Root = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Access91"):
                    opp_val = getattr(item, "Access91", None)
                    
                    if opp_val == self:
                        setattr(item, "Access91", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Access91"):
                    opp_val = getattr(item, "Access91", None)
                    
                    setattr(item, "Access91", self)
                    

    @property
    def root121(self):
        return self.__root121

    @root121.setter
    def root121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__root121", None)
        self.__root121 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasePath"):
                    opp_val = getattr(item, "BasePath", None)
                    
                    if opp_val == self:
                        setattr(item, "BasePath", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasePath"):
                    opp_val = getattr(item, "BasePath", None)
                    
                    setattr(item, "BasePath", self)
                    

    @property
    def gast_core_Root107(self):
        return self.__gast_core_Root107

    @gast_core_Root107.setter
    def gast_core_Root107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root107", None)
        self.__gast_core_Root107 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalVariable108"):
                    opp_val = getattr(item, "GlobalVariable108", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalVariable108", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalVariable108"):
                    opp_val = getattr(item, "GlobalVariable108", None)
                    
                    setattr(item, "GlobalVariable108", self)
                    

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__root", None)
        self.__root = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package110"):
                    opp_val = getattr(item, "Package110", None)
                    
                    if opp_val == self:
                        setattr(item, "Package110", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package110"):
                    opp_val = getattr(item, "Package110", None)
                    
                    setattr(item, "Package110", self)
                    

    @property
    def gast_core_Root93(self):
        return self.__gast_core_Root93

    @gast_core_Root93.setter
    def gast_core_Root93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root93", None)
        self.__gast_core_Root93 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass94"):
                    opp_val = getattr(item, "GASTClass94", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass94", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass94"):
                    opp_val = getattr(item, "GASTClass94", None)
                    
                    setattr(item, "GASTClass94", self)
                    

    @property
    def gast_core_Root114(self):
        return self.__gast_core_Root114

    @gast_core_Root114.setter
    def gast_core_Root114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root114", None)
        self.__gast_core_Root114 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StructuralAbstraction"):
                    opp_val = getattr(item, "StructuralAbstraction", None)
                    
                    if opp_val == self:
                        setattr(item, "StructuralAbstraction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StructuralAbstraction"):
                    opp_val = getattr(item, "StructuralAbstraction", None)
                    
                    setattr(item, "StructuralAbstraction", self)
                    

    @property
    def gast_core_Root96(self):
        return self.__gast_core_Root96

    @gast_core_Root96.setter
    def gast_core_Root96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root96", None)
        self.__gast_core_Root96 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass97"):
                    opp_val = getattr(item, "GASTClass97", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass97", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass97"):
                    opp_val = getattr(item, "GASTClass97", None)
                    
                    setattr(item, "GASTClass97", self)
                    

    def getPackageByQualifiedName(self, gast_qualifiedName) :
        # TODO: Implement getPackageByQualifiedName method
        pass

    def getPackageByName(self, gast_name) :
        # TODO: Implement getPackageByName method
        pass

class gast_core_SourceEntity(ModelElement):

    pass
class gast_core_NamedModelElement(ModelElement):

    def __init__(self, simpleName: str, ModelElement: "gast_core_Root" = None, ModelElement277: "gast_accesses_Access" = None, ModelElement119: "gast_core_Root" = None):
        self.simpleName = simpleName
        
        pass
    @property
    def simpleName(self):
        return self.__simpleName

    @simpleName.setter
    def simpleName(self, simpleName: str):
        self.__simpleName = simpleName


class gast_core_BasePath(ModelElement):

    def __init__(self, path: str, basePaths: "Root" = None, basePath: set["Directory"] = None, ModelElement: "gast_core_Root" = None, ModelElement277: "gast_accesses_Access" = None, ModelElement119: "gast_core_Root" = None):
        self.path = path
        self.basePaths = basePaths
        self.basePath = basePath if basePath is not None else set()
        
        pass
    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path


    @property
    def basePaths(self):
        return self.__basePaths

    @basePaths.setter
    def basePaths(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_BasePath__basePaths", None)
        self.__basePaths = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Root"):
                opp_val = getattr(old_value, "Root", None)
                if opp_val == self:
                    setattr(old_value, "Root", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Root"):
                opp_val = getattr(value, "Root", None)
                setattr(value, "Root", self)

    @property
    def basePath(self):
        return self.__basePath

    @basePath.setter
    def basePath(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_BasePath__basePath", None)
        self.__basePath = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Directory"):
                    opp_val = getattr(item, "Directory", None)
                    
                    if opp_val == self:
                        setattr(item, "Directory", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Directory"):
                    opp_val = getattr(item, "Directory", None)
                    
                    setattr(item, "Directory", self)
                    

class statements_FlowInstr:

    pass
class statements_Statement:

    pass
class gast_statements_JumpStatement(statements_Statement, statements_FlowInstr):

    def __init__(self, kind: str, gast_statements_JumpStatement: "GASTExpression" = None):
        self.kind = kind
        self.gast_statements_JumpStatement = gast_statements_JumpStatement
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def gast_statements_JumpStatement(self):
        return self.__gast_statements_JumpStatement

    @gast_statements_JumpStatement.setter
    def gast_statements_JumpStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_JumpStatement__gast_statements_JumpStatement", None)
        self.__gast_statements_JumpStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GASTExpression42"):
                opp_val = getattr(old_value, "GASTExpression42", None)
                if opp_val == self:
                    setattr(old_value, "GASTExpression42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTExpression42"):
                opp_val = getattr(value, "GASTExpression42", None)
                setattr(value, "GASTExpression42", self)

class Var:

    pass
class gast_statements_Param(Var):

    pass
class gast_statements_FlowInstr:

    def __init__(self, txt: str, gast_statements_FlowInstr: set["Var"] = None, gast_statements_FlowInstr50: set["Var"] = None, cfPrev: set["FlowInstr"] = None, cfnext: set["FlowInstr"] = None):
        self.txt = txt
        self.gast_statements_FlowInstr = gast_statements_FlowInstr if gast_statements_FlowInstr is not None else set()
        self.gast_statements_FlowInstr50 = gast_statements_FlowInstr50 if gast_statements_FlowInstr50 is not None else set()
        self.cfPrev = cfPrev if cfPrev is not None else set()
        self.cfnext = cfnext if cfnext is not None else set()
        
        pass
    @property
    def txt(self):
        return self.__txt

    @txt.setter
    def txt(self, txt: str):
        self.__txt = txt


    @property
    def gast_statements_FlowInstr50(self):
        return self.__gast_statements_FlowInstr50

    @gast_statements_FlowInstr50.setter
    def gast_statements_FlowInstr50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_FlowInstr__gast_statements_FlowInstr50", None)
        self.__gast_statements_FlowInstr50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Var51"):
                    opp_val = getattr(item, "Var51", None)
                    
                    if opp_val == self:
                        setattr(item, "Var51", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Var51"):
                    opp_val = getattr(item, "Var51", None)
                    
                    setattr(item, "Var51", self)
                    

    @property
    def cfPrev(self):
        return self.__cfPrev

    @cfPrev.setter
    def cfPrev(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_FlowInstr__cfPrev", None)
        self.__cfPrev = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FlowInstr"):
                    opp_val = getattr(item, "FlowInstr", None)
                    
                    if opp_val == self:
                        setattr(item, "FlowInstr", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FlowInstr"):
                    opp_val = getattr(item, "FlowInstr", None)
                    
                    setattr(item, "FlowInstr", self)
                    

    @property
    def gast_statements_FlowInstr(self):
        return self.__gast_statements_FlowInstr

    @gast_statements_FlowInstr.setter
    def gast_statements_FlowInstr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_FlowInstr__gast_statements_FlowInstr", None)
        self.__gast_statements_FlowInstr = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Var"):
                    opp_val = getattr(item, "Var", None)
                    
                    if opp_val == self:
                        setattr(item, "Var", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Var"):
                    opp_val = getattr(item, "Var", None)
                    
                    setattr(item, "Var", self)
                    

    @property
    def cfnext(self):
        return self.__cfnext

    @cfnext.setter
    def cfnext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_FlowInstr__cfnext", None)
        self.__cfnext = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FlowInstr54"):
                    opp_val = getattr(item, "FlowInstr54", None)
                    
                    if opp_val == self:
                        setattr(item, "FlowInstr54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FlowInstr54"):
                    opp_val = getattr(item, "FlowInstr54", None)
                    
                    setattr(item, "FlowInstr54", self)
                    

class FlowInstr:

    pass
class gast_statements_Exit(FlowInstr):

    def __init__(self, name: str, FlowInstr: "gast_statements_FlowInstr" = None, FlowInstr54: "gast_statements_FlowInstr" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class Exit:

    pass
class statements_BlockStatement:

    pass
class gast_statements_Methods(statements_BlockStatement, statements_FlowInstr):

    def __init__(self, methodName: str, gast_statements_Methods: "Exit" = None):
        self.methodName = methodName
        self.gast_statements_Methods = gast_statements_Methods
        
        pass
    @property
    def methodName(self):
        return self.__methodName

    @methodName.setter
    def methodName(self, methodName: str):
        self.__methodName = methodName


    @property
    def gast_statements_Methods(self):
        return self.__gast_statements_Methods

    @gast_statements_Methods.setter
    def gast_statements_Methods(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_Methods__gast_statements_Methods", None)
        self.__gast_statements_Methods = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Exit"):
                opp_val = getattr(old_value, "Exit", None)
                if opp_val == self:
                    setattr(old_value, "Exit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Exit"):
                opp_val = getattr(value, "Exit", None)
                setattr(value, "Exit", self)

class gast_statements_GASTBehaviour:

    pass
class gast_statements_SimpleStatement(statements_Statement, statements_FlowInstr):

    pass
class BranchStatement:

    pass
class CatchParameter:

    pass
class gast_statements_CatchBlock(BlockStatement):

    pass
class gast_statements_LoopStatement(Statement):

    def __init__(self, kind: str, gast_statements_LoopStatement: "GASTExpression" = None, gast_statements_LoopStatement33: "GASTExpression" = None, gast_statements_LoopStatement36: "GASTExpression" = None, loopstatement: "Statement" = None, Statement305: "gast_functions_Function" = None, Statement249: "gast_accesses_BaseAccess" = None, Statement247: "gast_accesses_BaseAccess" = None, Statement21: "gast_statements_BlockStatement" = None, Statement19: "gast_statements_Statement" = None, Statement: "gast_statements_Statement" = None, Statement174: "gast_annotations_CloneInstance" = None, Statement27: "gast_statements_Branch" = None, Statement39: "gast_statements_LoopStatement" = None, Statement16: "gast_statements_Statement" = None):
        self.kind = kind
        self.gast_statements_LoopStatement = gast_statements_LoopStatement
        self.gast_statements_LoopStatement33 = gast_statements_LoopStatement33
        self.gast_statements_LoopStatement36 = gast_statements_LoopStatement36
        self.loopstatement = loopstatement
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def loopstatement(self):
        return self.__loopstatement

    @loopstatement.setter
    def loopstatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_LoopStatement__loopstatement", None)
        self.__loopstatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Statement39"):
                opp_val = getattr(old_value, "Statement39", None)
                if opp_val == self:
                    setattr(old_value, "Statement39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Statement39"):
                opp_val = getattr(value, "Statement39", None)
                setattr(value, "Statement39", self)

    @property
    def gast_statements_LoopStatement(self):
        return self.__gast_statements_LoopStatement

    @gast_statements_LoopStatement.setter
    def gast_statements_LoopStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_LoopStatement__gast_statements_LoopStatement", None)
        self.__gast_statements_LoopStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GASTExpression31"):
                opp_val = getattr(old_value, "GASTExpression31", None)
                if opp_val == self:
                    setattr(old_value, "GASTExpression31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTExpression31"):
                opp_val = getattr(value, "GASTExpression31", None)
                setattr(value, "GASTExpression31", self)

    @property
    def gast_statements_LoopStatement33(self):
        return self.__gast_statements_LoopStatement33

    @gast_statements_LoopStatement33.setter
    def gast_statements_LoopStatement33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_LoopStatement__gast_statements_LoopStatement33", None)
        self.__gast_statements_LoopStatement33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GASTExpression34"):
                opp_val = getattr(old_value, "GASTExpression34", None)
                if opp_val == self:
                    setattr(old_value, "GASTExpression34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTExpression34"):
                opp_val = getattr(value, "GASTExpression34", None)
                setattr(value, "GASTExpression34", self)

    @property
    def gast_statements_LoopStatement36(self):
        return self.__gast_statements_LoopStatement36

    @gast_statements_LoopStatement36.setter
    def gast_statements_LoopStatement36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_LoopStatement__gast_statements_LoopStatement36", None)
        self.__gast_statements_LoopStatement36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GASTExpression37"):
                opp_val = getattr(old_value, "GASTExpression37", None)
                if opp_val == self:
                    setattr(old_value, "GASTExpression37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTExpression37"):
                opp_val = getattr(value, "GASTExpression37", None)
                setattr(value, "GASTExpression37", self)

class gast_statements_BranchStatement(Statement):

    pass
class gast_statements_GASTExpression(SourceEntity):

    pass
class GASTExpression:

    pass
class gast_statements_Branch(SourceEntity):

    pass
class Function:

    pass
class gast_functions_GlobalFunction(Function):

    def __init__(self, kind: str, globalFunctions: "Package" = None, globalFunctions294: "Root" = None, Function259: "gast_accesses_DeclarationTypeAccess" = None, Function318: "gast_variables_FormalParameter" = None, Function: "gast_statements_BlockStatement" = None, Function230: "gast_types_GASTClass" = None, Function209: "gast_types_GASTClass" = None, Function326: "gast_variables_LocalVariable" = None, Function262: "gast_accesses_DelegateAccess" = None, Function255: "gast_accesses_BaseAccess" = None, Function270: "gast_accesses_FunctionAccess" = None, Function282: "gast_functions_Delegate" = None):
        self.kind = kind
        self.globalFunctions = globalFunctions
        self.globalFunctions294 = globalFunctions294
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def globalFunctions(self):
        return self.__globalFunctions

    @globalFunctions.setter
    def globalFunctions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_GlobalFunction__globalFunctions", None)
        self.__globalFunctions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package292"):
                opp_val = getattr(old_value, "Package292", None)
                if opp_val == self:
                    setattr(old_value, "Package292", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package292"):
                opp_val = getattr(value, "Package292", None)
                setattr(value, "Package292", self)

    @property
    def globalFunctions294(self):
        return self.__globalFunctions294

    @globalFunctions294.setter
    def globalFunctions294(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_GlobalFunction__globalFunctions294", None)
        self.__globalFunctions294 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Root295"):
                opp_val = getattr(old_value, "Root295", None)
                if opp_val == self:
                    setattr(old_value, "Root295", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Root295"):
                opp_val = getattr(value, "Root295", None)
                setattr(value, "Root295", self)

class gast_statements_BlockStatement(Statement):

    def __init__(self, synchronized: bool, blockstatement: set["Statement"] = None, body23: "Function" = None, Statement305: "gast_functions_Function" = None, Statement249: "gast_accesses_BaseAccess" = None, Statement247: "gast_accesses_BaseAccess" = None, Statement21: "gast_statements_BlockStatement" = None, Statement19: "gast_statements_Statement" = None, Statement: "gast_statements_Statement" = None, Statement174: "gast_annotations_CloneInstance" = None, Statement27: "gast_statements_Branch" = None, Statement39: "gast_statements_LoopStatement" = None, Statement16: "gast_statements_Statement" = None):
        self.synchronized = synchronized
        self.blockstatement = blockstatement if blockstatement is not None else set()
        self.body23 = body23
        
        pass
    @property
    def synchronized(self):
        return self.__synchronized

    @synchronized.setter
    def synchronized(self, synchronized: bool):
        self.__synchronized = synchronized


    @property
    def blockstatement(self):
        return self.__blockstatement

    @blockstatement.setter
    def blockstatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_BlockStatement__blockstatement", None)
        self.__blockstatement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Statement21"):
                    opp_val = getattr(item, "Statement21", None)
                    
                    if opp_val == self:
                        setattr(item, "Statement21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Statement21"):
                    opp_val = getattr(item, "Statement21", None)
                    
                    setattr(item, "Statement21", self)
                    

    @property
    def body23(self):
        return self.__body23

    @body23.setter
    def body23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_BlockStatement__body23", None)
        self.__body23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Function"):
                opp_val = getattr(old_value, "Function", None)
                if opp_val == self:
                    setattr(old_value, "Function", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Function"):
                opp_val = getattr(value, "Function", None)
                setattr(value, "Function", self)

class LoopStatement:

    pass
class Branch:

    pass
class CloneInstance:

    pass