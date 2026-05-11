from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class GlobalFunctionKind(Enum):
    NORMAL = "NORMAL"
    UNITINITIALIZER = "UNITINITIALIZER"
    UNITFINALIZER = "UNITFINALIZER"
class Visibilities(Enum):
    VISIBILITYSTRICTPROTECTED = "VISIBILITYSTRICTPROTECTED"
    VISIBILITYPUBLIC = "VISIBILITYPUBLIC"
    VISIBILITYPACKAGE = "VISIBILITYPACKAGE"
    VISIBILITYPROTECTED = "VISIBILITYPROTECTED"
    VISIBILITYPRIVAT = "VISIBILITYPRIVAT"
class JumpStatementKind(Enum):
    JUMP = "JUMP"
    RETURN = "RETURN"
    THROW = "THROW"
class Status(Enum):
    NORMAL = "NORMAL"
    LIBRARY = "LIBRARY"
    IMPLICIT = "IMPLICIT"
    FAILEDDEP = "FAILEDDEP"
class LoopStatementKind(Enum):
    FOREACH = "FOREACH"
    WHILE = "WHILE"
    DOWHILE = "DOWHILE"
    FOR = "FOR"


############################################
# Definition of Classes
############################################

class variables_Variable:

    pass
class variables_Field:

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
class gast_variables_FormalParameter(Variable):

    def __init__(self, passedByReference: bool, formalParameters: "Function" = None, Variable: "gast_accesses_DeclarationTypeAccess" = None, Variable258: "gast_accesses_VariableAccess" = None):
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
            if hasattr(old_value, "Function304"):
                opp_val = getattr(old_value, "Function304", None)
                if opp_val == self:
                    setattr(old_value, "Function304", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Function304"):
                opp_val = getattr(value, "Function304", None)
                setattr(value, "Function304", self)

class gast_variables_LocalVariable(Variable):

    pass
class gast_variables_CatchParameter(Variable):

    def __init__(self, rethrown: bool, Variable: "gast_accesses_DeclarationTypeAccess" = None, Variable258: "gast_accesses_VariableAccess" = None):
        self.rethrown = rethrown
        
        pass
    @property
    def rethrown(self):
        return self.__rethrown

    @rethrown.setter
    def rethrown(self, rethrown: bool):
        self.__rethrown = rethrown


class CompositeAccess:

    pass
class Property:

    pass
class InheritanceTypeAccess:

    pass
class TypeAccess:

    pass
class gast_accesses_StaticTypeAccess(TypeAccess):

    pass
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


class gast_accesses_DeclarationTypeAccess(TypeAccess):

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


class gast_accesses_CastTypeAccess(TypeAccess):

    pass
class gast_accesses_ParameterInstantiationTypeAccess(TypeAccess):

    pass
class gast_accesses_RunTimeTypeAccess(TypeAccess):

    pass
class Method:

    pass
class Field:

    pass
class Destructor:

    pass
class Constructor:

    pass
class types_GASTType:

    pass
class core_GenericEntity:

    pass
class gast_functions_GenericConstructor(functions_Constructor, core_GenericEntity):

    pass
class gast_functions_GenericMethod(functions_Method, core_GenericEntity):

    pass
class gast_functions_GenericFunction(functions_GlobalFunction, core_GenericEntity):

    pass
class Member:

    pass
class types_TypeDecorator:

    pass
class types_Member:

    pass
class gast_variables_Field(variables_Variable, types_Member):

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
            if hasattr(old_value, "GASTClass310"):
                opp_val = getattr(old_value, "GASTClass310", None)
                if opp_val == self:
                    setattr(old_value, "GASTClass310", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTClass310"):
                opp_val = getattr(value, "GASTClass310", None)
                setattr(value, "GASTClass310", self)

class gast_functions_Delegate(functions_Function, types_Member, types_GASTType):

    def __init__(self, innerDelegate: bool, gast_functions_Delegate: "GASTClass" = None, gast_functions_Delegate267: set["Function"] = None, innerDelegates: "GASTClass" = None, delegates: "Package" = None):
        self.innerDelegate = innerDelegate
        self.gast_functions_Delegate = gast_functions_Delegate
        self.gast_functions_Delegate267 = gast_functions_Delegate267 if gast_functions_Delegate267 is not None else set()
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
            if hasattr(old_value, "Package272"):
                opp_val = getattr(old_value, "Package272", None)
                if opp_val == self:
                    setattr(old_value, "Package272", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package272"):
                opp_val = getattr(value, "Package272", None)
                setattr(value, "Package272", self)

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
            if hasattr(old_value, "GASTClass270"):
                opp_val = getattr(old_value, "GASTClass270", None)
                if opp_val == self:
                    setattr(old_value, "GASTClass270", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTClass270"):
                opp_val = getattr(value, "GASTClass270", None)
                setattr(value, "GASTClass270", self)

    @property
    def gast_functions_Delegate267(self):
        return self.__gast_functions_Delegate267

    @gast_functions_Delegate267.setter
    def gast_functions_Delegate267(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Delegate__gast_functions_Delegate267", None)
        self.__gast_functions_Delegate267 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Function268"):
                    opp_val = getattr(item, "Function268", None)
                    
                    if opp_val == self:
                        setattr(item, "Function268", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Function268"):
                    opp_val = getattr(item, "Function268", None)
                    
                    setattr(item, "Function268", self)
                    

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
            if hasattr(old_value, "GASTClass265"):
                opp_val = getattr(old_value, "GASTClass265", None)
                if opp_val == self:
                    setattr(old_value, "GASTClass265", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTClass265"):
                opp_val = getattr(value, "GASTClass265", None)
                setattr(value, "GASTClass265", self)

class gast_functions_Destructor(functions_Function, types_Member):

    pass
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
            if hasattr(old_value, "Property283"):
                opp_val = getattr(old_value, "Property283", None)
                if opp_val == self:
                    setattr(old_value, "Property283", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Property283"):
                opp_val = getattr(value, "Property283", None)
                setattr(value, "Property283", self)

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
            if hasattr(old_value, "GASTClass285"):
                opp_val = getattr(old_value, "GASTClass285", None)
                if opp_val == self:
                    setattr(old_value, "GASTClass285", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTClass285"):
                opp_val = getattr(value, "GASTClass285", None)
                setattr(value, "GASTClass285", self)

class gast_types_GASTClass(types_Member, types_GASTType):

    def __init__(self, linesOfComments: int, local: bool, primitive: bool, interface: bool, anonymous: bool, inner: bool, surroundingClass: set["TypeAlias"] = None, surroundingClass184: set["Delegate"] = None, surroundingClass187: set["Constructor"] = None, surroundingClass189: set["Destructor"] = None, surroundingClass191: set["Field"] = None, surroundingClass193: set["Method"] = None, localClasses: "Function" = None, classes: "Package" = None, gast_types_GASTClass: set["GASTClass"] = None, surroundingClass201: set["GASTClass"] = None, innerClasses: "GASTClass" = None, gast_types_GASTClass206: set["InheritanceTypeAccess"] = None, gast_types_GASTClass208: "Field" = None, gastClass: set["GASTClass"] = None, friendClasses: "GASTClass" = None, gast_types_GASTClass215: set["Function"] = None, gast_types_GASTClass218: set["Property"] = None, gast_types_GASTClass220: set["Access"] = None, gast_types_GASTClass223: set["GASTClass"] = None):
        self.linesOfComments = linesOfComments
        self.local = local
        self.primitive = primitive
        self.interface = interface
        self.anonymous = anonymous
        self.inner = inner
        self.surroundingClass = surroundingClass if surroundingClass is not None else set()
        self.surroundingClass184 = surroundingClass184 if surroundingClass184 is not None else set()
        self.surroundingClass187 = surroundingClass187 if surroundingClass187 is not None else set()
        self.surroundingClass189 = surroundingClass189 if surroundingClass189 is not None else set()
        self.surroundingClass191 = surroundingClass191 if surroundingClass191 is not None else set()
        self.surroundingClass193 = surroundingClass193 if surroundingClass193 is not None else set()
        self.localClasses = localClasses
        self.classes = classes
        self.gast_types_GASTClass = gast_types_GASTClass if gast_types_GASTClass is not None else set()
        self.surroundingClass201 = surroundingClass201 if surroundingClass201 is not None else set()
        self.innerClasses = innerClasses
        self.gast_types_GASTClass206 = gast_types_GASTClass206 if gast_types_GASTClass206 is not None else set()
        self.gast_types_GASTClass208 = gast_types_GASTClass208
        self.gastClass = gastClass if gastClass is not None else set()
        self.friendClasses = friendClasses
        self.gast_types_GASTClass215 = gast_types_GASTClass215 if gast_types_GASTClass215 is not None else set()
        self.gast_types_GASTClass218 = gast_types_GASTClass218 if gast_types_GASTClass218 is not None else set()
        self.gast_types_GASTClass220 = gast_types_GASTClass220 if gast_types_GASTClass220 is not None else set()
        self.gast_types_GASTClass223 = gast_types_GASTClass223 if gast_types_GASTClass223 is not None else set()
        
        pass
    @property
    def anonymous(self):
        return self.__anonymous

    @anonymous.setter
    def anonymous(self, anonymous: bool):
        self.__anonymous = anonymous


    @property
    def interface(self):
        return self.__interface

    @interface.setter
    def interface(self, interface: bool):
        self.__interface = interface


    @property
    def linesOfComments(self):
        return self.__linesOfComments

    @linesOfComments.setter
    def linesOfComments(self, linesOfComments: int):
        self.__linesOfComments = linesOfComments


    @property
    def primitive(self):
        return self.__primitive

    @primitive.setter
    def primitive(self, primitive: bool):
        self.__primitive = primitive


    @property
    def local(self):
        return self.__local

    @local.setter
    def local(self, local: bool):
        self.__local = local


    @property
    def inner(self):
        return self.__inner

    @inner.setter
    def inner(self, inner: bool):
        self.__inner = inner


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
                if hasattr(item, "GASTClass211"):
                    opp_val = getattr(item, "GASTClass211", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass211", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass211"):
                    opp_val = getattr(item, "GASTClass211", None)
                    
                    setattr(item, "GASTClass211", self)
                    

    @property
    def surroundingClass187(self):
        return self.__surroundingClass187

    @surroundingClass187.setter
    def surroundingClass187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__surroundingClass187", None)
        self.__surroundingClass187 = value if value is not None else set()
        
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
    def gast_types_GASTClass218(self):
        return self.__gast_types_GASTClass218

    @gast_types_GASTClass218.setter
    def gast_types_GASTClass218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__gast_types_GASTClass218", None)
        self.__gast_types_GASTClass218 = value if value is not None else set()
        
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
                    

    @property
    def surroundingClass189(self):
        return self.__surroundingClass189

    @surroundingClass189.setter
    def surroundingClass189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__surroundingClass189", None)
        self.__surroundingClass189 = value if value is not None else set()
        
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
                if hasattr(item, "GASTClass199"):
                    opp_val = getattr(item, "GASTClass199", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass199", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass199"):
                    opp_val = getattr(item, "GASTClass199", None)
                    
                    setattr(item, "GASTClass199", self)
                    

    @property
    def gast_types_GASTClass223(self):
        return self.__gast_types_GASTClass223

    @gast_types_GASTClass223.setter
    def gast_types_GASTClass223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__gast_types_GASTClass223", None)
        self.__gast_types_GASTClass223 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass224"):
                    opp_val = getattr(item, "GASTClass224", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass224", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass224"):
                    opp_val = getattr(item, "GASTClass224", None)
                    
                    setattr(item, "GASTClass224", self)
                    

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
            if hasattr(old_value, "Function195"):
                opp_val = getattr(old_value, "Function195", None)
                if opp_val == self:
                    setattr(old_value, "Function195", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Function195"):
                opp_val = getattr(value, "Function195", None)
                setattr(value, "Function195", self)

    @property
    def surroundingClass193(self):
        return self.__surroundingClass193

    @surroundingClass193.setter
    def surroundingClass193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__surroundingClass193", None)
        self.__surroundingClass193 = value if value is not None else set()
        
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
    def gast_types_GASTClass215(self):
        return self.__gast_types_GASTClass215

    @gast_types_GASTClass215.setter
    def gast_types_GASTClass215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__gast_types_GASTClass215", None)
        self.__gast_types_GASTClass215 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Function216"):
                    opp_val = getattr(item, "Function216", None)
                    
                    if opp_val == self:
                        setattr(item, "Function216", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Function216"):
                    opp_val = getattr(item, "Function216", None)
                    
                    setattr(item, "Function216", self)
                    

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
            if hasattr(old_value, "GASTClass204"):
                opp_val = getattr(old_value, "GASTClass204", None)
                if opp_val == self:
                    setattr(old_value, "GASTClass204", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTClass204"):
                opp_val = getattr(value, "GASTClass204", None)
                setattr(value, "GASTClass204", self)

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
                if hasattr(item, "GASTClass202"):
                    opp_val = getattr(item, "GASTClass202", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass202", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass202"):
                    opp_val = getattr(item, "GASTClass202", None)
                    
                    setattr(item, "GASTClass202", self)
                    

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
            if hasattr(old_value, "Package197"):
                opp_val = getattr(old_value, "Package197", None)
                if opp_val == self:
                    setattr(old_value, "Package197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package197"):
                opp_val = getattr(value, "Package197", None)
                setattr(value, "Package197", self)

    @property
    def surroundingClass191(self):
        return self.__surroundingClass191

    @surroundingClass191.setter
    def surroundingClass191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__surroundingClass191", None)
        self.__surroundingClass191 = value if value is not None else set()
        
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
    def surroundingClass184(self):
        return self.__surroundingClass184

    @surroundingClass184.setter
    def surroundingClass184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__surroundingClass184", None)
        self.__surroundingClass184 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Delegate185"):
                    opp_val = getattr(item, "Delegate185", None)
                    
                    if opp_val == self:
                        setattr(item, "Delegate185", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Delegate185"):
                    opp_val = getattr(item, "Delegate185", None)
                    
                    setattr(item, "Delegate185", self)
                    

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
                if hasattr(item, "TypeAlias182"):
                    opp_val = getattr(item, "TypeAlias182", None)
                    
                    if opp_val == self:
                        setattr(item, "TypeAlias182", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypeAlias182"):
                    opp_val = getattr(item, "TypeAlias182", None)
                    
                    setattr(item, "TypeAlias182", self)
                    

    @property
    def gast_types_GASTClass206(self):
        return self.__gast_types_GASTClass206

    @gast_types_GASTClass206.setter
    def gast_types_GASTClass206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__gast_types_GASTClass206", None)
        self.__gast_types_GASTClass206 = value if value is not None else set()
        
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
    def friendClasses(self):
        return self.__friendClasses

    @friendClasses.setter
    def friendClasses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__friendClasses", None)
        self.__friendClasses = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GASTClass213"):
                opp_val = getattr(old_value, "GASTClass213", None)
                if opp_val == self:
                    setattr(old_value, "GASTClass213", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTClass213"):
                opp_val = getattr(value, "GASTClass213", None)
                setattr(value, "GASTClass213", self)

    @property
    def gast_types_GASTClass208(self):
        return self.__gast_types_GASTClass208

    @gast_types_GASTClass208.setter
    def gast_types_GASTClass208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__gast_types_GASTClass208", None)
        self.__gast_types_GASTClass208 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Field209"):
                opp_val = getattr(old_value, "Field209", None)
                if opp_val == self:
                    setattr(old_value, "Field209", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Field209"):
                opp_val = getattr(value, "Field209", None)
                setattr(value, "Field209", self)

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
                if hasattr(item, "Access221"):
                    opp_val = getattr(item, "Access221", None)
                    
                    if opp_val == self:
                        setattr(item, "Access221", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Access221"):
                    opp_val = getattr(item, "Access221", None)
                    
                    setattr(item, "Access221", self)
                    

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
            if hasattr(old_value, "GASTClass274"):
                opp_val = getattr(old_value, "GASTClass274", None)
                if opp_val == self:
                    setattr(old_value, "GASTClass274", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTClass274"):
                opp_val = getattr(value, "GASTClass274", None)
                setattr(value, "GASTClass274", self)

class gast_variables_Property(types_Member, variables_Field):

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
    def gast_types_TypeAlias(self):
        return self.__gast_types_TypeAlias

    @gast_types_TypeAlias.setter
    def gast_types_TypeAlias(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_TypeAlias__gast_types_TypeAlias", None)
        self.__gast_types_TypeAlias = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GASTType173"):
                opp_val = getattr(old_value, "GASTType173", None)
                if opp_val == self:
                    setattr(old_value, "GASTType173", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTType173"):
                opp_val = getattr(value, "GASTType173", None)
                setattr(value, "GASTType173", self)

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
            if hasattr(old_value, "Package177"):
                opp_val = getattr(old_value, "Package177", None)
                if opp_val == self:
                    setattr(old_value, "Package177", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package177"):
                opp_val = getattr(value, "Package177", None)
                setattr(value, "Package177", self)

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
            if hasattr(old_value, "GASTClass175"):
                opp_val = getattr(old_value, "GASTClass175", None)
                if opp_val == self:
                    setattr(old_value, "GASTClass175", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTClass175"):
                opp_val = getattr(value, "GASTClass175", None)
                setattr(value, "GASTClass175", self)

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
            if hasattr(old_value, "GASTType171"):
                opp_val = getattr(old_value, "GASTType171", None)
                if opp_val == self:
                    setattr(old_value, "GASTType171", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTType171"):
                opp_val = getattr(value, "GASTType171", None)
                setattr(value, "GASTType171", self)

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
            if hasattr(old_value, "GASTType164"):
                opp_val = getattr(old_value, "GASTType164", None)
                if opp_val == self:
                    setattr(old_value, "GASTType164", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTType164"):
                opp_val = getattr(value, "GASTType164", None)
                setattr(value, "GASTType164", self)

class gast_annotations_ModelAnnotation(ABC):

    pass
class core_SourceEntity:

    pass
class core_NamedModelElement:

    pass
class gast_variables_Variable(core_NamedModelElement, core_SourceEntity):

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
    def surroundingVariable(self):
        return self.__surroundingVariable

    @surroundingVariable.setter
    def surroundingVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_variables_Variable__surroundingVariable", None)
        self.__surroundingVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DeclarationTypeAccess308"):
                opp_val = getattr(old_value, "DeclarationTypeAccess308", None)
                if opp_val == self:
                    setattr(old_value, "DeclarationTypeAccess308", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DeclarationTypeAccess308"):
                opp_val = getattr(value, "DeclarationTypeAccess308", None)
                setattr(value, "DeclarationTypeAccess308", self)

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
            if hasattr(old_value, "GASTType306"):
                opp_val = getattr(old_value, "GASTType306", None)
                if opp_val == self:
                    setattr(old_value, "GASTType306", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTType306"):
                opp_val = getattr(value, "GASTType306", None)
                setattr(value, "GASTType306", self)

class gast_functions_Function(core_NamedModelElement, core_SourceEntity):

    def __init__(self, numberOfStatements: int, maximumNestingLevel: int, linesOfComments: int, linesOfCode: int, numberOfEdgesInCFG: int, numberOfNodesInCFG: int, operator: bool, function: "DeclarationTypeAccess" = None, surroundingFunction: set["FormalParameter"] = None, surroundingFunction289: set["LocalVariable"] = None, gast_functions_Function: set["Statement"] = None, gast_functions_Function293: set["ThrowTypeAccess"] = None, gast_functions_Function295: set["Access"] = None, surroundingFunction298: "BlockStatement" = None, surroundingFunction301: set["GASTClass"] = None):
        self.numberOfStatements = numberOfStatements
        self.maximumNestingLevel = maximumNestingLevel
        self.linesOfComments = linesOfComments
        self.linesOfCode = linesOfCode
        self.numberOfEdgesInCFG = numberOfEdgesInCFG
        self.numberOfNodesInCFG = numberOfNodesInCFG
        self.operator = operator
        self.function = function
        self.surroundingFunction = surroundingFunction if surroundingFunction is not None else set()
        self.surroundingFunction289 = surroundingFunction289 if surroundingFunction289 is not None else set()
        self.gast_functions_Function = gast_functions_Function if gast_functions_Function is not None else set()
        self.gast_functions_Function293 = gast_functions_Function293 if gast_functions_Function293 is not None else set()
        self.gast_functions_Function295 = gast_functions_Function295 if gast_functions_Function295 is not None else set()
        self.surroundingFunction298 = surroundingFunction298
        self.surroundingFunction301 = surroundingFunction301 if surroundingFunction301 is not None else set()
        
        pass
    @property
    def numberOfNodesInCFG(self):
        return self.__numberOfNodesInCFG

    @numberOfNodesInCFG.setter
    def numberOfNodesInCFG(self, numberOfNodesInCFG: int):
        self.__numberOfNodesInCFG = numberOfNodesInCFG


    @property
    def linesOfCode(self):
        return self.__linesOfCode

    @linesOfCode.setter
    def linesOfCode(self, linesOfCode: int):
        self.__linesOfCode = linesOfCode


    @property
    def numberOfEdgesInCFG(self):
        return self.__numberOfEdgesInCFG

    @numberOfEdgesInCFG.setter
    def numberOfEdgesInCFG(self, numberOfEdgesInCFG: int):
        self.__numberOfEdgesInCFG = numberOfEdgesInCFG


    @property
    def maximumNestingLevel(self):
        return self.__maximumNestingLevel

    @maximumNestingLevel.setter
    def maximumNestingLevel(self, maximumNestingLevel: int):
        self.__maximumNestingLevel = maximumNestingLevel


    @property
    def numberOfStatements(self):
        return self.__numberOfStatements

    @numberOfStatements.setter
    def numberOfStatements(self, numberOfStatements: int):
        self.__numberOfStatements = numberOfStatements


    @property
    def linesOfComments(self):
        return self.__linesOfComments

    @linesOfComments.setter
    def linesOfComments(self, linesOfComments: int):
        self.__linesOfComments = linesOfComments


    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: bool):
        self.__operator = operator


    @property
    def surroundingFunction298(self):
        return self.__surroundingFunction298

    @surroundingFunction298.setter
    def surroundingFunction298(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Function__surroundingFunction298", None)
        self.__surroundingFunction298 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BlockStatement299"):
                opp_val = getattr(old_value, "BlockStatement299", None)
                if opp_val == self:
                    setattr(old_value, "BlockStatement299", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BlockStatement299"):
                opp_val = getattr(value, "BlockStatement299", None)
                setattr(value, "BlockStatement299", self)

    @property
    def surroundingFunction289(self):
        return self.__surroundingFunction289

    @surroundingFunction289.setter
    def surroundingFunction289(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Function__surroundingFunction289", None)
        self.__surroundingFunction289 = value if value is not None else set()
        
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
    def gast_functions_Function293(self):
        return self.__gast_functions_Function293

    @gast_functions_Function293.setter
    def gast_functions_Function293(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Function__gast_functions_Function293", None)
        self.__gast_functions_Function293 = value if value is not None else set()
        
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
                if hasattr(item, "Statement291"):
                    opp_val = getattr(item, "Statement291", None)
                    
                    if opp_val == self:
                        setattr(item, "Statement291", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Statement291"):
                    opp_val = getattr(item, "Statement291", None)
                    
                    setattr(item, "Statement291", self)
                    

    @property
    def gast_functions_Function295(self):
        return self.__gast_functions_Function295

    @gast_functions_Function295.setter
    def gast_functions_Function295(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Function__gast_functions_Function295", None)
        self.__gast_functions_Function295 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Access296"):
                    opp_val = getattr(item, "Access296", None)
                    
                    if opp_val == self:
                        setattr(item, "Access296", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Access296"):
                    opp_val = getattr(item, "Access296", None)
                    
                    setattr(item, "Access296", self)
                    

    @property
    def surroundingFunction301(self):
        return self.__surroundingFunction301

    @surroundingFunction301.setter
    def surroundingFunction301(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Function__surroundingFunction301", None)
        self.__surroundingFunction301 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass302"):
                    opp_val = getattr(item, "GASTClass302", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass302", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass302"):
                    opp_val = getattr(item, "GASTClass302", None)
                    
                    setattr(item, "GASTClass302", self)
                    

class annotations_ModelAnnotation:

    pass
class gast_annotations_Comment(annotations_ModelAnnotation, core_SourceEntity):

    def __init__(self, todo: bool, formal: bool, todoCount: int, texts: str):
        self.todo = todo
        self.formal = formal
        self.todoCount = todoCount
        self.texts = texts
        
        pass
    @property
    def formal(self):
        return self.__formal

    @formal.setter
    def formal(self, formal: bool):
        self.__formal = formal


    @property
    def todoCount(self):
        return self.__todoCount

    @todoCount.setter
    def todoCount(self, todoCount: int):
        self.__todoCount = todoCount


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


    def OCLtodo(self, gast_diagnostics, gast_context) :
        # TODO: Implement OCLtodo method
        pass

class gast_annotations_StructuralAbstraction(core_NamedModelElement, annotations_ModelAnnotation):

    pass
class types_GASTClass:

    pass
class gast_types_GenericClass(core_GenericEntity, types_GASTClass):

    pass
class gast_annotations_Attribute(annotations_ModelAnnotation, types_GASTClass):

    pass
class Position:

    pass
class gast_core_Position:

    def __init__(self, endColumn: int, startColumn: int, endLine: int, startLine: int, gast_core_Position: "File" = None, gast_core_Position149: "File" = None, position: "SourceEntity" = None):
        self.endColumn = endColumn
        self.startColumn = startColumn
        self.endLine = endLine
        self.startLine = startLine
        self.gast_core_Position = gast_core_Position
        self.gast_core_Position149 = gast_core_Position149
        self.position = position
        
        pass
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
    def gast_core_Position149(self):
        return self.__gast_core_Position149

    @gast_core_Position149.setter
    def gast_core_Position149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Position__gast_core_Position149", None)
        self.__gast_core_Position149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "File150"):
                opp_val = getattr(old_value, "File150", None)
                if opp_val == self:
                    setattr(old_value, "File150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "File150"):
                opp_val = getattr(value, "File150", None)
                setattr(value, "File150", self)

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
    def gast_core_Position(self):
        return self.__gast_core_Position

    @gast_core_Position.setter
    def gast_core_Position(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Position__gast_core_Position", None)
        self.__gast_core_Position = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "File147"):
                opp_val = getattr(old_value, "File147", None)
                if opp_val == self:
                    setattr(old_value, "File147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "File147"):
                opp_val = getattr(value, "File147", None)
                setattr(value, "File147", self)

    def EitherAssemblyFileOrSourceFileSet(self, gast_context, gast_diagnostics) :
        # TODO: Implement EitherAssemblyFileOrSourceFileSet method
        pass

class core_ModelElement:

    pass
class gast_annotations_CloneInstance(core_ModelElement, annotations_ModelAnnotation):

    pass
class gast_annotations_Clone(core_ModelElement, annotations_ModelAnnotation):

    pass
class File:

    pass
class BasePath:

    pass
class StructuralAbstraction:

    pass
class gast_annotations_Layer(StructuralAbstraction):

    pass
class gast_annotations_Subsystem(StructuralAbstraction):

    pass
class Clone:

    pass
class GASTType:

    pass
class gast_types_TypeDecorator(GASTType):

    pass
class TypeParameterClass:

    pass
class TypeAlias:

    pass
class Package:

    pass
class gast_core_PackageAlias(Package):

    pass
class GlobalVariable:

    pass
class Delegate:

    pass
class Access:

    pass
class gast_accesses_FunctionAccess(Access):

    pass
class gast_accesses_TypeAccess(Access):

    pass
class gast_accesses_VariableAccess(Access):

    def __init__(self, write: bool, gast_accesses_VariableAccess: "Variable" = None, Access77: "gast_core_Root" = None, Access221: "gast_types_GASTClass" = None, Access296: "gast_functions_Function" = None, Access: "gast_core_Package" = None):
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
            if hasattr(old_value, "Variable258"):
                opp_val = getattr(old_value, "Variable258", None)
                if opp_val == self:
                    setattr(old_value, "Variable258", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable258"):
                opp_val = getattr(value, "Variable258", None)
                setattr(value, "Variable258", self)

class GASTClass:

    pass
class gast_types_GASTStruct(GASTClass):

    pass
class gast_types_GASTUnion(GASTClass):

    pass
class gast_types_TypeParameterClass(GASTClass):

    pass
class gast_types_GASTEnumeration(GASTClass):

    pass
class NamedModelElement:

    pass
class gast_core_File(NamedModelElement):

    def __init__(self, sourceFile: bool, assemblyFile: bool, linesOfCode: int, size: str, fullQualifiedPath: str, fileSystemPath: str, gast_core_File: "Root" = None, files: "Directory" = None, gast_core_File121: set["GASTType"] = None, gast_core_File124: set["GASTType"] = None, gast_core_File127: set["GlobalVariable"] = None, gast_core_File130: set["GlobalFunction"] = None, gast_core_File133: set["GlobalFunction"] = None, gast_core_File136: set["GlobalVariable"] = None, gast_core_File139: set["Package"] = None, gast_core_File142: set["File"] = None):
        self.sourceFile = sourceFile
        self.assemblyFile = assemblyFile
        self.linesOfCode = linesOfCode
        self.size = size
        self.fullQualifiedPath = fullQualifiedPath
        self.fileSystemPath = fileSystemPath
        self.gast_core_File = gast_core_File
        self.files = files
        self.gast_core_File121 = gast_core_File121 if gast_core_File121 is not None else set()
        self.gast_core_File124 = gast_core_File124 if gast_core_File124 is not None else set()
        self.gast_core_File127 = gast_core_File127 if gast_core_File127 is not None else set()
        self.gast_core_File130 = gast_core_File130 if gast_core_File130 is not None else set()
        self.gast_core_File133 = gast_core_File133 if gast_core_File133 is not None else set()
        self.gast_core_File136 = gast_core_File136 if gast_core_File136 is not None else set()
        self.gast_core_File139 = gast_core_File139 if gast_core_File139 is not None else set()
        self.gast_core_File142 = gast_core_File142 if gast_core_File142 is not None else set()
        
        pass
    @property
    def sourceFile(self):
        return self.__sourceFile

    @sourceFile.setter
    def sourceFile(self, sourceFile: bool):
        self.__sourceFile = sourceFile


    @property
    def fileSystemPath(self):
        return self.__fileSystemPath

    @fileSystemPath.setter
    def fileSystemPath(self, fileSystemPath: str):
        self.__fileSystemPath = fileSystemPath


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
    def files(self):
        return self.__files

    @files.setter
    def files(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__files", None)
        self.__files = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Directory145"):
                opp_val = getattr(old_value, "Directory145", None)
                if opp_val == self:
                    setattr(old_value, "Directory145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Directory145"):
                opp_val = getattr(value, "Directory145", None)
                setattr(value, "Directory145", self)

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
            if hasattr(old_value, "Root119"):
                opp_val = getattr(old_value, "Root119", None)
                if opp_val == self:
                    setattr(old_value, "Root119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Root119"):
                opp_val = getattr(value, "Root119", None)
                setattr(value, "Root119", self)

    @property
    def gast_core_File139(self):
        return self.__gast_core_File139

    @gast_core_File139.setter
    def gast_core_File139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File139", None)
        self.__gast_core_File139 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package140"):
                    opp_val = getattr(item, "Package140", None)
                    
                    if opp_val == self:
                        setattr(item, "Package140", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package140"):
                    opp_val = getattr(item, "Package140", None)
                    
                    setattr(item, "Package140", self)
                    

    @property
    def gast_core_File124(self):
        return self.__gast_core_File124

    @gast_core_File124.setter
    def gast_core_File124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File124", None)
        self.__gast_core_File124 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTType125"):
                    opp_val = getattr(item, "GASTType125", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTType125", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTType125"):
                    opp_val = getattr(item, "GASTType125", None)
                    
                    setattr(item, "GASTType125", self)
                    

    @property
    def gast_core_File127(self):
        return self.__gast_core_File127

    @gast_core_File127.setter
    def gast_core_File127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File127", None)
        self.__gast_core_File127 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalVariable128"):
                    opp_val = getattr(item, "GlobalVariable128", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalVariable128", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalVariable128"):
                    opp_val = getattr(item, "GlobalVariable128", None)
                    
                    setattr(item, "GlobalVariable128", self)
                    

    @property
    def gast_core_File142(self):
        return self.__gast_core_File142

    @gast_core_File142.setter
    def gast_core_File142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File142", None)
        self.__gast_core_File142 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "File143"):
                    opp_val = getattr(item, "File143", None)
                    
                    if opp_val == self:
                        setattr(item, "File143", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "File143"):
                    opp_val = getattr(item, "File143", None)
                    
                    setattr(item, "File143", self)
                    

    @property
    def gast_core_File130(self):
        return self.__gast_core_File130

    @gast_core_File130.setter
    def gast_core_File130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File130", None)
        self.__gast_core_File130 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalFunction131"):
                    opp_val = getattr(item, "GlobalFunction131", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalFunction131", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalFunction131"):
                    opp_val = getattr(item, "GlobalFunction131", None)
                    
                    setattr(item, "GlobalFunction131", self)
                    

    @property
    def gast_core_File136(self):
        return self.__gast_core_File136

    @gast_core_File136.setter
    def gast_core_File136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File136", None)
        self.__gast_core_File136 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalVariable137"):
                    opp_val = getattr(item, "GlobalVariable137", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalVariable137", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalVariable137"):
                    opp_val = getattr(item, "GlobalVariable137", None)
                    
                    setattr(item, "GlobalVariable137", self)
                    

    @property
    def gast_core_File133(self):
        return self.__gast_core_File133

    @gast_core_File133.setter
    def gast_core_File133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File133", None)
        self.__gast_core_File133 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalFunction134"):
                    opp_val = getattr(item, "GlobalFunction134", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalFunction134", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalFunction134"):
                    opp_val = getattr(item, "GlobalFunction134", None)
                    
                    setattr(item, "GlobalFunction134", self)
                    

    @property
    def gast_core_File121(self):
        return self.__gast_core_File121

    @gast_core_File121.setter
    def gast_core_File121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File121", None)
        self.__gast_core_File121 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTType122"):
                    opp_val = getattr(item, "GASTType122", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTType122", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTType122"):
                    opp_val = getattr(item, "GASTType122", None)
                    
                    setattr(item, "GASTType122", self)
                    

class gast_types_GASTType(NamedModelElement):

    def __init__(self, referenceType: bool, qualifiedName: str):
        self.referenceType = referenceType
        self.qualifiedName = qualifiedName
        
        pass
    @property
    def referenceType(self):
        return self.__referenceType

    @referenceType.setter
    def referenceType(self, referenceType: bool):
        self.__referenceType = referenceType


    @property
    def qualifiedName(self):
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName


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
    def subDirectory(self):
        return self.__subDirectory

    @subDirectory.setter
    def subDirectory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Directory__subDirectory", None)
        self.__subDirectory = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Directory114"):
                opp_val = getattr(old_value, "Directory114", None)
                if opp_val == self:
                    setattr(old_value, "Directory114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Directory114"):
                opp_val = getattr(value, "Directory114", None)
                setattr(value, "Directory114", self)

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
            if hasattr(old_value, "BasePath117"):
                opp_val = getattr(old_value, "BasePath117", None)
                if opp_val == self:
                    setattr(old_value, "BasePath117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasePath117"):
                opp_val = getattr(value, "BasePath117", None)
                setattr(value, "BasePath117", self)

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
                if hasattr(item, "Directory112"):
                    opp_val = getattr(item, "Directory112", None)
                    
                    if opp_val == self:
                        setattr(item, "Directory112", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Directory112"):
                    opp_val = getattr(item, "Directory112", None)
                    
                    setattr(item, "Directory112", self)
                    

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
                    

class gast_core_Package(NamedModelElement):

    def __init__(self, linesOfComments: int, linesOfCode: int, qualifiedName: str, gast_core_Package: set["GASTClass"] = None, gast_core_Package46: set["GASTClass"] = None, gast_core_Package49: set["GASTClass"] = None, gast_core_Package52: set["GASTClass"] = None, gast_core_Package55: set["Access"] = None, surroundingPackage: set["Delegate"] = None, surroundingPackage58: set["GlobalFunction"] = None, surroundingPackage60: set["GlobalVariable"] = None, packages: "Root" = None, surroundingPackage64: set["GASTClass"] = None, surroundingPackage67: set["Package"] = None, subPackages: "Package" = None, gast_core_Package71: set["Package"] = None, surroundingPackage74: set["TypeAlias"] = None):
        self.linesOfComments = linesOfComments
        self.linesOfCode = linesOfCode
        self.qualifiedName = qualifiedName
        self.gast_core_Package = gast_core_Package if gast_core_Package is not None else set()
        self.gast_core_Package46 = gast_core_Package46 if gast_core_Package46 is not None else set()
        self.gast_core_Package49 = gast_core_Package49 if gast_core_Package49 is not None else set()
        self.gast_core_Package52 = gast_core_Package52 if gast_core_Package52 is not None else set()
        self.gast_core_Package55 = gast_core_Package55 if gast_core_Package55 is not None else set()
        self.surroundingPackage = surroundingPackage if surroundingPackage is not None else set()
        self.surroundingPackage58 = surroundingPackage58 if surroundingPackage58 is not None else set()
        self.surroundingPackage60 = surroundingPackage60 if surroundingPackage60 is not None else set()
        self.packages = packages
        self.surroundingPackage64 = surroundingPackage64 if surroundingPackage64 is not None else set()
        self.surroundingPackage67 = surroundingPackage67 if surroundingPackage67 is not None else set()
        self.subPackages = subPackages
        self.gast_core_Package71 = gast_core_Package71 if gast_core_Package71 is not None else set()
        self.surroundingPackage74 = surroundingPackage74 if surroundingPackage74 is not None else set()
        
        pass
    @property
    def qualifiedName(self):
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName


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
    def gast_core_Package49(self):
        return self.__gast_core_Package49

    @gast_core_Package49.setter
    def gast_core_Package49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__gast_core_Package49", None)
        self.__gast_core_Package49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass50"):
                    opp_val = getattr(item, "GASTClass50", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass50"):
                    opp_val = getattr(item, "GASTClass50", None)
                    
                    setattr(item, "GASTClass50", self)
                    

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
    def surroundingPackage60(self):
        return self.__surroundingPackage60

    @surroundingPackage60.setter
    def surroundingPackage60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__surroundingPackage60", None)
        self.__surroundingPackage60 = value if value is not None else set()
        
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
    def subPackages(self):
        return self.__subPackages

    @subPackages.setter
    def subPackages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__subPackages", None)
        self.__subPackages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package69"):
                opp_val = getattr(old_value, "Package69", None)
                if opp_val == self:
                    setattr(old_value, "Package69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package69"):
                opp_val = getattr(value, "Package69", None)
                setattr(value, "Package69", self)

    @property
    def surroundingPackage67(self):
        return self.__surroundingPackage67

    @surroundingPackage67.setter
    def surroundingPackage67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__surroundingPackage67", None)
        self.__surroundingPackage67 = value if value is not None else set()
        
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
    def gast_core_Package46(self):
        return self.__gast_core_Package46

    @gast_core_Package46.setter
    def gast_core_Package46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__gast_core_Package46", None)
        self.__gast_core_Package46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass47"):
                    opp_val = getattr(item, "GASTClass47", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass47"):
                    opp_val = getattr(item, "GASTClass47", None)
                    
                    setattr(item, "GASTClass47", self)
                    

    @property
    def gast_core_Package71(self):
        return self.__gast_core_Package71

    @gast_core_Package71.setter
    def gast_core_Package71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__gast_core_Package71", None)
        self.__gast_core_Package71 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package72"):
                    opp_val = getattr(item, "Package72", None)
                    
                    if opp_val == self:
                        setattr(item, "Package72", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package72"):
                    opp_val = getattr(item, "Package72", None)
                    
                    setattr(item, "Package72", self)
                    

    @property
    def gast_core_Package52(self):
        return self.__gast_core_Package52

    @gast_core_Package52.setter
    def gast_core_Package52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__gast_core_Package52", None)
        self.__gast_core_Package52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass53"):
                    opp_val = getattr(item, "GASTClass53", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass53"):
                    opp_val = getattr(item, "GASTClass53", None)
                    
                    setattr(item, "GASTClass53", self)
                    

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
    def surroundingPackage64(self):
        return self.__surroundingPackage64

    @surroundingPackage64.setter
    def surroundingPackage64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__surroundingPackage64", None)
        self.__surroundingPackage64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass65"):
                    opp_val = getattr(item, "GASTClass65", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass65", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass65"):
                    opp_val = getattr(item, "GASTClass65", None)
                    
                    setattr(item, "GASTClass65", self)
                    

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
    def packages(self):
        return self.__packages

    @packages.setter
    def packages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__packages", None)
        self.__packages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Root62"):
                opp_val = getattr(old_value, "Root62", None)
                if opp_val == self:
                    setattr(old_value, "Root62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Root62"):
                opp_val = getattr(value, "Root62", None)
                setattr(value, "Root62", self)

    @property
    def gast_core_Package55(self):
        return self.__gast_core_Package55

    @gast_core_Package55.setter
    def gast_core_Package55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__gast_core_Package55", None)
        self.__gast_core_Package55 = value if value is not None else set()
        
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
    def surroundingPackage58(self):
        return self.__surroundingPackage58

    @surroundingPackage58.setter
    def surroundingPackage58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__surroundingPackage58", None)
        self.__surroundingPackage58 = value if value is not None else set()
        
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
                    

class GlobalFunction:

    pass
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


    def idHasToBeUnique(self, gast_context, gast_diagnostics) :
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
    def sissyId(self):
        return self.__sissyId

    @sissyId.setter
    def sissyId(self, sissyId: int):
        self.__sissyId = sissyId


    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status


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
class gast_core_NamedModelElement(ModelElement):

    def __init__(self, simpleName: str, ModelElement263: "gast_accesses_Access" = None, ModelElement105: "gast_core_Root" = None, ModelElement: "gast_core_Root" = None):
        self.simpleName = simpleName
        
        pass
    @property
    def simpleName(self):
        return self.__simpleName

    @simpleName.setter
    def simpleName(self, simpleName: str):
        self.__simpleName = simpleName


class gast_core_Root(ModelElement):

    def __init__(self, linesOfComments: int, linesOfCode: int, gast_core_Root82: set["GASTClass"] = None, gast_core_Root85: set["GASTClass"] = None, gast_core_Root88: set["GASTClass"] = None, gast_core_Root91: set["ModelElement"] = None, gast_core_Root93: set["GlobalVariable"] = None, root: set["Package"] = None, root98: set["Clone"] = None, gast_core_Root100: set["StructuralAbstraction"] = None, gast_core_Root102: set["GASTType"] = None, gast_core_Root104: set["ModelElement"] = None, root107: set["BasePath"] = None, root109: set["GlobalFunction"] = None, gast_core_Root: set["Access"] = None, gast_core_Root79: set["GASTClass"] = None, ModelElement263: "gast_accesses_Access" = None, ModelElement105: "gast_core_Root" = None, ModelElement: "gast_core_Root" = None):
        self.linesOfComments = linesOfComments
        self.linesOfCode = linesOfCode
        self.gast_core_Root82 = gast_core_Root82 if gast_core_Root82 is not None else set()
        self.gast_core_Root85 = gast_core_Root85 if gast_core_Root85 is not None else set()
        self.gast_core_Root88 = gast_core_Root88 if gast_core_Root88 is not None else set()
        self.gast_core_Root91 = gast_core_Root91 if gast_core_Root91 is not None else set()
        self.gast_core_Root93 = gast_core_Root93 if gast_core_Root93 is not None else set()
        self.root = root if root is not None else set()
        self.root98 = root98 if root98 is not None else set()
        self.gast_core_Root100 = gast_core_Root100 if gast_core_Root100 is not None else set()
        self.gast_core_Root102 = gast_core_Root102 if gast_core_Root102 is not None else set()
        self.gast_core_Root104 = gast_core_Root104 if gast_core_Root104 is not None else set()
        self.root107 = root107 if root107 is not None else set()
        self.root109 = root109 if root109 is not None else set()
        self.gast_core_Root = gast_core_Root if gast_core_Root is not None else set()
        self.gast_core_Root79 = gast_core_Root79 if gast_core_Root79 is not None else set()
        
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
                if hasattr(item, "Access77"):
                    opp_val = getattr(item, "Access77", None)
                    
                    if opp_val == self:
                        setattr(item, "Access77", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Access77"):
                    opp_val = getattr(item, "Access77", None)
                    
                    setattr(item, "Access77", self)
                    

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
    def root109(self):
        return self.__root109

    @root109.setter
    def root109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__root109", None)
        self.__root109 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalFunction110"):
                    opp_val = getattr(item, "GlobalFunction110", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalFunction110", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalFunction110"):
                    opp_val = getattr(item, "GlobalFunction110", None)
                    
                    setattr(item, "GlobalFunction110", self)
                    

    @property
    def gast_core_Root85(self):
        return self.__gast_core_Root85

    @gast_core_Root85.setter
    def gast_core_Root85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root85", None)
        self.__gast_core_Root85 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass86"):
                    opp_val = getattr(item, "GASTClass86", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass86", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass86"):
                    opp_val = getattr(item, "GASTClass86", None)
                    
                    setattr(item, "GASTClass86", self)
                    

    @property
    def gast_core_Root91(self):
        return self.__gast_core_Root91

    @gast_core_Root91.setter
    def gast_core_Root91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root91", None)
        self.__gast_core_Root91 = value if value is not None else set()
        
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
                if hasattr(item, "Package96"):
                    opp_val = getattr(item, "Package96", None)
                    
                    if opp_val == self:
                        setattr(item, "Package96", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package96"):
                    opp_val = getattr(item, "Package96", None)
                    
                    setattr(item, "Package96", self)
                    

    @property
    def gast_core_Root79(self):
        return self.__gast_core_Root79

    @gast_core_Root79.setter
    def gast_core_Root79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root79", None)
        self.__gast_core_Root79 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass80"):
                    opp_val = getattr(item, "GASTClass80", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass80", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass80"):
                    opp_val = getattr(item, "GASTClass80", None)
                    
                    setattr(item, "GASTClass80", self)
                    

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
                if hasattr(item, "GlobalVariable94"):
                    opp_val = getattr(item, "GlobalVariable94", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalVariable94", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalVariable94"):
                    opp_val = getattr(item, "GlobalVariable94", None)
                    
                    setattr(item, "GlobalVariable94", self)
                    

    @property
    def gast_core_Root82(self):
        return self.__gast_core_Root82

    @gast_core_Root82.setter
    def gast_core_Root82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root82", None)
        self.__gast_core_Root82 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass83"):
                    opp_val = getattr(item, "GASTClass83", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass83", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass83"):
                    opp_val = getattr(item, "GASTClass83", None)
                    
                    setattr(item, "GASTClass83", self)
                    

    @property
    def root107(self):
        return self.__root107

    @root107.setter
    def root107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__root107", None)
        self.__root107 = value if value is not None else set()
        
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
    def gast_core_Root88(self):
        return self.__gast_core_Root88

    @gast_core_Root88.setter
    def gast_core_Root88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root88", None)
        self.__gast_core_Root88 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass89"):
                    opp_val = getattr(item, "GASTClass89", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass89", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass89"):
                    opp_val = getattr(item, "GASTClass89", None)
                    
                    setattr(item, "GASTClass89", self)
                    

    @property
    def gast_core_Root104(self):
        return self.__gast_core_Root104

    @gast_core_Root104.setter
    def gast_core_Root104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root104", None)
        self.__gast_core_Root104 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelElement105"):
                    opp_val = getattr(item, "ModelElement105", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelElement105", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelElement105"):
                    opp_val = getattr(item, "ModelElement105", None)
                    
                    setattr(item, "ModelElement105", self)
                    

    @property
    def root98(self):
        return self.__root98

    @root98.setter
    def root98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__root98", None)
        self.__root98 = value if value is not None else set()
        
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
    def gast_core_Root100(self):
        return self.__gast_core_Root100

    @gast_core_Root100.setter
    def gast_core_Root100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root100", None)
        self.__gast_core_Root100 = value if value is not None else set()
        
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
                    

    def getPackageByName(self, gast_name) :
        # TODO: Implement getPackageByName method
        pass

    def getPackageByQualifiedName(self, gast_qualifiedName) :
        # TODO: Implement getPackageByQualifiedName method
        pass

class gast_core_GenericEntity(ModelElement):

    pass
class gast_core_SourceEntity(ModelElement):

    pass
class gast_core_BasePath(ModelElement):

    def __init__(self, path: str, basePaths: "Root" = None, basePath: set["Directory"] = None, ModelElement263: "gast_accesses_Access" = None, ModelElement105: "gast_core_Root" = None, ModelElement: "gast_core_Root" = None):
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
                    

class gast_statements_GASTBehaviour:

    pass
class CatchParameter:

    pass
class BranchStatement:

    pass
class GASTExpression:

    pass
class Function:

    pass
class gast_functions_GlobalFunction(Function):

    def __init__(self, kind: str, globalFunctions: "Package" = None, globalFunctions280: "Root" = None, Function216: "gast_types_GASTClass" = None, Function245: "gast_accesses_DeclarationTypeAccess" = None, Function248: "gast_accesses_DelegateAccess" = None, Function195: "gast_types_GASTClass" = None, Function241: "gast_accesses_BaseAccess" = None, Function256: "gast_accesses_FunctionAccess" = None, Function268: "gast_functions_Delegate" = None, Function: "gast_statements_BlockStatement" = None, Function312: "gast_variables_LocalVariable" = None, Function304: "gast_variables_FormalParameter" = None):
        self.kind = kind
        self.globalFunctions = globalFunctions
        self.globalFunctions280 = globalFunctions280
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def globalFunctions280(self):
        return self.__globalFunctions280

    @globalFunctions280.setter
    def globalFunctions280(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_GlobalFunction__globalFunctions280", None)
        self.__globalFunctions280 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Root281"):
                opp_val = getattr(old_value, "Root281", None)
                if opp_val == self:
                    setattr(old_value, "Root281", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Root281"):
                opp_val = getattr(value, "Root281", None)
                setattr(value, "Root281", self)

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
            if hasattr(old_value, "Package278"):
                opp_val = getattr(old_value, "Package278", None)
                if opp_val == self:
                    setattr(old_value, "Package278", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package278"):
                opp_val = getattr(value, "Package278", None)
                setattr(value, "Package278", self)

class LoopStatement:

    pass
class CloneInstance:

    pass
class BaseAccess:

    pass
class gast_accesses_CompositeAccess(BaseAccess):

    pass
class gast_accesses_Access(BaseAccess):

    pass
class SourceEntity:

    pass
class gast_statements_GASTExpression(SourceEntity):

    pass
class gast_accesses_BaseAccess(SourceEntity):

    pass
class gast_types_Member(SourceEntity):

    def __init__(self, visibility: str, abstract: bool, extern: bool, final: bool, internal: bool, introspectable: bool, override: bool, static: bool, typeParameterClassMember: bool, virtual: bool, gast_types_Member: "Member" = None, SourceEntity: "gast_core_Position" = None):
        self.visibility = visibility
        self.abstract = abstract
        self.extern = extern
        self.final = final
        self.internal = internal
        self.introspectable = introspectable
        self.override = override
        self.static = static
        self.typeParameterClassMember = typeParameterClassMember
        self.virtual = virtual
        self.gast_types_Member = gast_types_Member
        
        pass
    @property
    def static(self):
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static


    @property
    def internal(self):
        return self.__internal

    @internal.setter
    def internal(self, internal: bool):
        self.__internal = internal


    @property
    def abstract(self):
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract


    @property
    def final(self):
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final


    @property
    def introspectable(self):
        return self.__introspectable

    @introspectable.setter
    def introspectable(self, introspectable: bool):
        self.__introspectable = introspectable


    @property
    def extern(self):
        return self.__extern

    @extern.setter
    def extern(self, extern: bool):
        self.__extern = extern


    @property
    def override(self):
        return self.__override

    @override.setter
    def override(self, override: bool):
        self.__override = override


    @property
    def typeParameterClassMember(self):
        return self.__typeParameterClassMember

    @typeParameterClassMember.setter
    def typeParameterClassMember(self, typeParameterClassMember: bool):
        self.__typeParameterClassMember = typeParameterClassMember


    @property
    def visibility(self):
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility


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

class gast_statements_Branch(SourceEntity):

    pass
class gast_statements_Statement(SourceEntity):

    def __init__(self, numberOfStatements: int, maximumNestingLevel: int, numberOfComments: int, linesOfCode: int, numberOfEdgesInCFG: int, numberOfNodesInCFG: int, parentStatement: set["BaseAccess"] = None, statements: "CloneInstance" = None, statements9: "BlockStatement" = None, gast_statements_Statement: "Statement" = None, statement: "Branch" = None, body: "LoopStatement" = None, SourceEntity: "gast_core_Position" = None):
        self.numberOfStatements = numberOfStatements
        self.maximumNestingLevel = maximumNestingLevel
        self.numberOfComments = numberOfComments
        self.linesOfCode = linesOfCode
        self.numberOfEdgesInCFG = numberOfEdgesInCFG
        self.numberOfNodesInCFG = numberOfNodesInCFG
        self.parentStatement = parentStatement if parentStatement is not None else set()
        self.statements = statements
        self.statements9 = statements9
        self.gast_statements_Statement = gast_statements_Statement
        self.statement = statement
        self.body = body
        
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
    def numberOfNodesInCFG(self):
        return self.__numberOfNodesInCFG

    @numberOfNodesInCFG.setter
    def numberOfNodesInCFG(self, numberOfNodesInCFG: int):
        self.__numberOfNodesInCFG = numberOfNodesInCFG


    @property
    def numberOfComments(self):
        return self.__numberOfComments

    @numberOfComments.setter
    def numberOfComments(self, numberOfComments: int):
        self.__numberOfComments = numberOfComments


    @property
    def numberOfStatements(self):
        return self.__numberOfStatements

    @numberOfStatements.setter
    def numberOfStatements(self, numberOfStatements: int):
        self.__numberOfStatements = numberOfStatements


    @property
    def numberOfEdgesInCFG(self):
        return self.__numberOfEdgesInCFG

    @numberOfEdgesInCFG.setter
    def numberOfEdgesInCFG(self, numberOfEdgesInCFG: int):
        self.__numberOfEdgesInCFG = numberOfEdgesInCFG


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
                    

class BlockStatement:

    pass
class gast_statements_CatchBlock(BlockStatement):

    pass
class CatchBlock:

    pass
class Statement:

    pass
class gast_statements_JumpStatement(Statement):

    def __init__(self, kind: str, gast_statements_JumpStatement: "GASTExpression" = None, Statement160: "gast_annotations_CloneInstance" = None, Statement235: "gast_accesses_BaseAccess" = None, Statement233: "gast_accesses_BaseAccess" = None, Statement15: "gast_statements_BlockStatement" = None, Statement: "gast_statements_Statement" = None, Statement21: "gast_statements_Branch" = None, Statement33: "gast_statements_LoopStatement" = None, Statement291: "gast_functions_Function" = None):
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
            if hasattr(old_value, "GASTExpression36"):
                opp_val = getattr(old_value, "GASTExpression36", None)
                if opp_val == self:
                    setattr(old_value, "GASTExpression36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTExpression36"):
                opp_val = getattr(value, "GASTExpression36", None)
                setattr(value, "GASTExpression36", self)

class gast_statements_SimpleStatement(Statement):

    pass
class gast_statements_LoopStatement(Statement):

    def __init__(self, kind: str, gast_statements_LoopStatement27: "GASTExpression" = None, gast_statements_LoopStatement: "GASTExpression" = None, gast_statements_LoopStatement30: "GASTExpression" = None, loopstatement: "Statement" = None, Statement160: "gast_annotations_CloneInstance" = None, Statement235: "gast_accesses_BaseAccess" = None, Statement233: "gast_accesses_BaseAccess" = None, Statement15: "gast_statements_BlockStatement" = None, Statement: "gast_statements_Statement" = None, Statement21: "gast_statements_Branch" = None, Statement33: "gast_statements_LoopStatement" = None, Statement291: "gast_functions_Function" = None):
        self.kind = kind
        self.gast_statements_LoopStatement27 = gast_statements_LoopStatement27
        self.gast_statements_LoopStatement = gast_statements_LoopStatement
        self.gast_statements_LoopStatement30 = gast_statements_LoopStatement30
        self.loopstatement = loopstatement
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


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
            if hasattr(old_value, "GASTExpression25"):
                opp_val = getattr(old_value, "GASTExpression25", None)
                if opp_val == self:
                    setattr(old_value, "GASTExpression25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTExpression25"):
                opp_val = getattr(value, "GASTExpression25", None)
                setattr(value, "GASTExpression25", self)

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
            if hasattr(old_value, "Statement33"):
                opp_val = getattr(old_value, "Statement33", None)
                if opp_val == self:
                    setattr(old_value, "Statement33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Statement33"):
                opp_val = getattr(value, "Statement33", None)
                setattr(value, "Statement33", self)

    @property
    def gast_statements_LoopStatement30(self):
        return self.__gast_statements_LoopStatement30

    @gast_statements_LoopStatement30.setter
    def gast_statements_LoopStatement30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_LoopStatement__gast_statements_LoopStatement30", None)
        self.__gast_statements_LoopStatement30 = value
        
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
    def gast_statements_LoopStatement27(self):
        return self.__gast_statements_LoopStatement27

    @gast_statements_LoopStatement27.setter
    def gast_statements_LoopStatement27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_LoopStatement__gast_statements_LoopStatement27", None)
        self.__gast_statements_LoopStatement27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GASTExpression28"):
                opp_val = getattr(old_value, "GASTExpression28", None)
                if opp_val == self:
                    setattr(old_value, "GASTExpression28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTExpression28"):
                opp_val = getattr(value, "GASTExpression28", None)
                setattr(value, "GASTExpression28", self)

class gast_statements_BlockStatement(Statement):

    def __init__(self, synchronized: bool, blockstatement: set["Statement"] = None, body17: "Function" = None, Statement160: "gast_annotations_CloneInstance" = None, Statement235: "gast_accesses_BaseAccess" = None, Statement233: "gast_accesses_BaseAccess" = None, Statement15: "gast_statements_BlockStatement" = None, Statement: "gast_statements_Statement" = None, Statement21: "gast_statements_Branch" = None, Statement33: "gast_statements_LoopStatement" = None, Statement291: "gast_functions_Function" = None):
        self.synchronized = synchronized
        self.blockstatement = blockstatement if blockstatement is not None else set()
        self.body17 = body17
        
        pass
    @property
    def synchronized(self):
        return self.__synchronized

    @synchronized.setter
    def synchronized(self, synchronized: bool):
        self.__synchronized = synchronized


    @property
    def body17(self):
        return self.__body17

    @body17.setter
    def body17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_BlockStatement__body17", None)
        self.__body17 = value
        
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
                if hasattr(item, "Statement15"):
                    opp_val = getattr(item, "Statement15", None)
                    
                    if opp_val == self:
                        setattr(item, "Statement15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Statement15"):
                    opp_val = getattr(item, "Statement15", None)
                    
                    setattr(item, "Statement15", self)
                    

class gast_statements_BranchStatement(Statement):

    pass
class gast_statements_ExceptionHandler(Statement):

    pass
class Branch:

    pass