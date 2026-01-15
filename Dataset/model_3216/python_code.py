from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

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
class JumpStatementKind(Enum):
    JUMP = "JUMP"
    RETURN = "RETURN"
    THROW = "THROW"
class Status(Enum):
    NORMAL = "NORMAL"
    LIBRARY = "LIBRARY"
    IMPLICIT = "IMPLICIT"
    FAILEDDEP = "FAILEDDEP"


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
        
    @property
    def super(self) -> bool:
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
class gast_variables_LocalVariable(Variable):

    pass
class gast_variables_CatchParameter(Variable):

    def __init__(self, rethrown: bool, Variable305: "gast_accesses_VariableAccess", variables293: "gast_accesses_DeclarationTypeAccess"):
        self.rethrown = rethrown
        
    @property
    def rethrown(self) -> bool:
        return self.__rethrown

    @rethrown.setter
    def rethrown(self, rethrown: bool):
        self.__rethrown = rethrown

class gast_variables_FormalParameter(Variable):

    def __init__(self, passedByReference: bool, Function359: "Function" = None, Variable305: "gast_accesses_VariableAccess", variables293: "gast_accesses_DeclarationTypeAccess"):
        self.passedByReference = passedByReference
        self.Function359 = Function359
        
    @property
    def passedByReference(self) -> bool:
        return self.__passedByReference

    @passedByReference.setter
    def passedByReference(self, passedByReference: bool):
        self.__passedByReference = passedByReference

    @property
    def Function359(self):
        return self.__Function359

    @Function359.setter
    def Function359(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_variables_FormalParameter__Function359", None)
        self.__Function359 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "functions360"):
                opp_val = getattr(old_value, "functions360", None)
                if opp_val == self:
                    setattr(old_value, "functions360", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "functions360"):
                opp_val = getattr(value, "functions360", None)
                setattr(value, "functions360", self)

class gast_variables_GlobalVariable(Variable):

    pass
class CompositeAccess:

    pass
class TypeAccess:

    pass
class gast_accesses_DeclarationTypeAccess(TypeAccess):

    pass
class gast_accesses_InheritanceTypeAccess(TypeAccess):

    def __init__(self, implementationInheritance: bool):
        self.implementationInheritance = implementationInheritance
        
    @property
    def implementationInheritance(self) -> bool:
        return self.__implementationInheritance

    @implementationInheritance.setter
    def implementationInheritance(self, implementationInheritance: bool):
        self.__implementationInheritance = implementationInheritance

class gast_accesses_ThrowTypeAccess(TypeAccess):

    def __init__(self, declared: bool):
        self.declared = declared
        
    @property
    def declared(self) -> bool:
        return self.__declared

    @declared.setter
    def declared(self, declared: bool):
        self.__declared = declared

class gast_accesses_StaticTypeAccess(TypeAccess):

    pass
class gast_accesses_CastTypeAccess(TypeAccess):

    pass
class gast_accesses_RunTimeTypeAccess(TypeAccess):

    pass
class gast_accesses_ParameterInstantiationTypeAccess(TypeAccess):

    pass
class Property:

    pass
class InheritanceTypeAccess:

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
class gast_functions_GenericMethod(core_GenericEntity, functions_Method):

    pass
class gast_functions_GenericFunction(functions_GlobalFunction, core_GenericEntity):

    pass
class gast_functions_GenericConstructor(functions_Constructor, core_GenericEntity):

    pass
class Member:

    pass
class types_TypeDecorator:

    pass
class types_Member:

    pass
class gast_functions_Constructor(types_Member, functions_Function):

    def __init__(self, initializer: bool, GASTClass323: "GASTClass" = None):
        self.initializer = initializer
        self.GASTClass323 = GASTClass323
        
    @property
    def initializer(self) -> bool:
        return self.__initializer

    @initializer.setter
    def initializer(self, initializer: bool):
        self.__initializer = initializer

    @property
    def GASTClass323(self):
        return self.__GASTClass323

    @GASTClass323.setter
    def GASTClass323(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Constructor__GASTClass323", None)
        self.__GASTClass323 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types324"):
                opp_val = getattr(old_value, "types324", None)
                if opp_val == self:
                    setattr(old_value, "types324", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types324"):
                opp_val = getattr(value, "types324", None)
                setattr(value, "types324", self)

class gast_variables_Field(variables_Variable, types_Member):

    def __init__(self, propertyField: bool, GASTClass367: "GASTClass" = None):
        self.propertyField = propertyField
        self.GASTClass367 = GASTClass367
        
    @property
    def propertyField(self) -> bool:
        return self.__propertyField

    @propertyField.setter
    def propertyField(self, propertyField: bool):
        self.__propertyField = propertyField

    @property
    def GASTClass367(self):
        return self.__GASTClass367

    @GASTClass367.setter
    def GASTClass367(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_variables_Field__GASTClass367", None)
        self.__GASTClass367 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types368"):
                opp_val = getattr(old_value, "types368", None)
                if opp_val == self:
                    setattr(old_value, "types368", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types368"):
                opp_val = getattr(value, "types368", None)
                setattr(value, "types368", self)

class gast_variables_Property(types_Member, variables_Field):

    pass
class gast_functions_Destructor(types_Member, functions_Function):

    pass
class gast_functions_Method(types_Member, functions_Function):

    def __init__(self, propertyMethod: bool, gast_functions_Method: "Property" = None, GASTClass337: "GASTClass" = None):
        self.propertyMethod = propertyMethod
        self.gast_functions_Method = gast_functions_Method
        self.GASTClass337 = GASTClass337
        
    @property
    def propertyMethod(self) -> bool:
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
            if hasattr(old_value, "Property335"):
                opp_val = getattr(old_value, "Property335", None)
                if opp_val == self:
                    setattr(old_value, "Property335", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Property335"):
                opp_val = getattr(value, "Property335", None)
                setattr(value, "Property335", self)

    @property
    def GASTClass337(self):
        return self.__GASTClass337

    @GASTClass337.setter
    def GASTClass337(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Method__GASTClass337", None)
        self.__GASTClass337 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types338"):
                opp_val = getattr(old_value, "types338", None)
                if opp_val == self:
                    setattr(old_value, "types338", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types338"):
                opp_val = getattr(value, "types338", None)
                setattr(value, "types338", self)

class gast_types_GASTClass(types_Member, types_GASTType):

    def __init__(self, linesOfComments: int, local: bool, primitive: bool, interface: bool, anonymous: bool, inner: bool, TypeAlias219: set["TypeAlias"] = None, Delegate222: set["Delegate"] = None, Constructor: set["Constructor"] = None, Destructor: set["Destructor"] = None, Field: set["Field"] = None, Method: set["Method"] = None, Function233: "Function" = None, Package236: "Package" = None, GASTClass241: set["GASTClass"] = None, GASTClass244: "GASTClass" = None, gast_types_GASTClass: set["GASTClass"] = None, gast_types_GASTClass249: "Field" = None, GASTClass252: set["GASTClass"] = None, GASTClass255: "GASTClass" = None, gast_types_GASTClass258: set["Function"] = None, gast_types_GASTClass261: set["Property"] = None, gast_types_GASTClass263: set["Access"] = None, gast_types_GASTClass247: set["InheritanceTypeAccess"] = None, gast_types_GASTClass266: set["GASTClass"] = None):
        self.linesOfComments = linesOfComments
        self.local = local
        self.primitive = primitive
        self.interface = interface
        self.anonymous = anonymous
        self.inner = inner
        self.TypeAlias219 = TypeAlias219 if TypeAlias219 is not None else set()
        self.Delegate222 = Delegate222 if Delegate222 is not None else set()
        self.Constructor = Constructor if Constructor is not None else set()
        self.Destructor = Destructor if Destructor is not None else set()
        self.Field = Field if Field is not None else set()
        self.Method = Method if Method is not None else set()
        self.Function233 = Function233
        self.Package236 = Package236
        self.GASTClass241 = GASTClass241 if GASTClass241 is not None else set()
        self.GASTClass244 = GASTClass244
        self.gast_types_GASTClass = gast_types_GASTClass if gast_types_GASTClass is not None else set()
        self.gast_types_GASTClass249 = gast_types_GASTClass249
        self.GASTClass252 = GASTClass252 if GASTClass252 is not None else set()
        self.GASTClass255 = GASTClass255
        self.gast_types_GASTClass258 = gast_types_GASTClass258 if gast_types_GASTClass258 is not None else set()
        self.gast_types_GASTClass261 = gast_types_GASTClass261 if gast_types_GASTClass261 is not None else set()
        self.gast_types_GASTClass263 = gast_types_GASTClass263 if gast_types_GASTClass263 is not None else set()
        self.gast_types_GASTClass247 = gast_types_GASTClass247 if gast_types_GASTClass247 is not None else set()
        self.gast_types_GASTClass266 = gast_types_GASTClass266 if gast_types_GASTClass266 is not None else set()
        
    @property
    def linesOfComments(self) -> int:
        return self.__linesOfComments

    @linesOfComments.setter
    def linesOfComments(self, linesOfComments: int):
        self.__linesOfComments = linesOfComments

    @property
    def inner(self) -> bool:
        return self.__inner

    @inner.setter
    def inner(self, inner: bool):
        self.__inner = inner

    @property
    def interface(self) -> bool:
        return self.__interface

    @interface.setter
    def interface(self, interface: bool):
        self.__interface = interface

    @property
    def local(self) -> bool:
        return self.__local

    @local.setter
    def local(self, local: bool):
        self.__local = local

    @property
    def anonymous(self) -> bool:
        return self.__anonymous

    @anonymous.setter
    def anonymous(self, anonymous: bool):
        self.__anonymous = anonymous

    @property
    def primitive(self) -> bool:
        return self.__primitive

    @primitive.setter
    def primitive(self, primitive: bool):
        self.__primitive = primitive

    @property
    def gast_types_GASTClass249(self):
        return self.__gast_types_GASTClass249

    @gast_types_GASTClass249.setter
    def gast_types_GASTClass249(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__gast_types_GASTClass249", None)
        self.__gast_types_GASTClass249 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Field250"):
                opp_val = getattr(old_value, "Field250", None)
                if opp_val == self:
                    setattr(old_value, "Field250", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Field250"):
                opp_val = getattr(value, "Field250", None)
                setattr(value, "Field250", self)

    @property
    def GASTClass252(self):
        return self.__GASTClass252

    @GASTClass252.setter
    def GASTClass252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__GASTClass252", None)
        self.__GASTClass252 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "types253"):
                    opp_val = getattr(item, "types253", None)
                    
                    if opp_val == self:
                        setattr(item, "types253", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types253"):
                    opp_val = getattr(item, "types253", None)
                    
                    setattr(item, "types253", self)
                    

    @property
    def gast_types_GASTClass263(self):
        return self.__gast_types_GASTClass263

    @gast_types_GASTClass263.setter
    def gast_types_GASTClass263(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__gast_types_GASTClass263", None)
        self.__gast_types_GASTClass263 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Access264"):
                    opp_val = getattr(item, "Access264", None)
                    
                    if opp_val == self:
                        setattr(item, "Access264", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Access264"):
                    opp_val = getattr(item, "Access264", None)
                    
                    setattr(item, "Access264", self)
                    

    @property
    def Delegate222(self):
        return self.__Delegate222

    @Delegate222.setter
    def Delegate222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__Delegate222", None)
        self.__Delegate222 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "functions223"):
                    opp_val = getattr(item, "functions223", None)
                    
                    if opp_val == self:
                        setattr(item, "functions223", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "functions223"):
                    opp_val = getattr(item, "functions223", None)
                    
                    setattr(item, "functions223", self)
                    

    @property
    def Constructor(self):
        return self.__Constructor

    @Constructor.setter
    def Constructor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__Constructor", None)
        self.__Constructor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "functions225"):
                    opp_val = getattr(item, "functions225", None)
                    
                    if opp_val == self:
                        setattr(item, "functions225", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "functions225"):
                    opp_val = getattr(item, "functions225", None)
                    
                    setattr(item, "functions225", self)
                    

    @property
    def Function233(self):
        return self.__Function233

    @Function233.setter
    def Function233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__Function233", None)
        self.__Function233 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "functions234"):
                opp_val = getattr(old_value, "functions234", None)
                if opp_val == self:
                    setattr(old_value, "functions234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "functions234"):
                opp_val = getattr(value, "functions234", None)
                setattr(value, "functions234", self)

    @property
    def GASTClass244(self):
        return self.__GASTClass244

    @GASTClass244.setter
    def GASTClass244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__GASTClass244", None)
        self.__GASTClass244 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types245"):
                opp_val = getattr(old_value, "types245", None)
                if opp_val == self:
                    setattr(old_value, "types245", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types245"):
                opp_val = getattr(value, "types245", None)
                setattr(value, "types245", self)

    @property
    def Package236(self):
        return self.__Package236

    @Package236.setter
    def Package236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__Package236", None)
        self.__Package236 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core237"):
                opp_val = getattr(old_value, "core237", None)
                if opp_val == self:
                    setattr(old_value, "core237", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core237"):
                opp_val = getattr(value, "core237", None)
                setattr(value, "core237", self)

    @property
    def gast_types_GASTClass266(self):
        return self.__gast_types_GASTClass266

    @gast_types_GASTClass266.setter
    def gast_types_GASTClass266(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__gast_types_GASTClass266", None)
        self.__gast_types_GASTClass266 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass267"):
                    opp_val = getattr(item, "GASTClass267", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass267", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass267"):
                    opp_val = getattr(item, "GASTClass267", None)
                    
                    setattr(item, "GASTClass267", self)
                    

    @property
    def Destructor(self):
        return self.__Destructor

    @Destructor.setter
    def Destructor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__Destructor", None)
        self.__Destructor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "functions227"):
                    opp_val = getattr(item, "functions227", None)
                    
                    if opp_val == self:
                        setattr(item, "functions227", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "functions227"):
                    opp_val = getattr(item, "functions227", None)
                    
                    setattr(item, "functions227", self)
                    

    @property
    def TypeAlias219(self):
        return self.__TypeAlias219

    @TypeAlias219.setter
    def TypeAlias219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__TypeAlias219", None)
        self.__TypeAlias219 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "types220"):
                    opp_val = getattr(item, "types220", None)
                    
                    if opp_val == self:
                        setattr(item, "types220", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types220"):
                    opp_val = getattr(item, "types220", None)
                    
                    setattr(item, "types220", self)
                    

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
                if hasattr(item, "GASTClass239"):
                    opp_val = getattr(item, "GASTClass239", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass239", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass239"):
                    opp_val = getattr(item, "GASTClass239", None)
                    
                    setattr(item, "GASTClass239", self)
                    

    @property
    def Method(self):
        return self.__Method

    @Method.setter
    def Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__Method", None)
        self.__Method = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "functions231"):
                    opp_val = getattr(item, "functions231", None)
                    
                    if opp_val == self:
                        setattr(item, "functions231", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "functions231"):
                    opp_val = getattr(item, "functions231", None)
                    
                    setattr(item, "functions231", self)
                    

    @property
    def GASTClass241(self):
        return self.__GASTClass241

    @GASTClass241.setter
    def GASTClass241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__GASTClass241", None)
        self.__GASTClass241 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "types242"):
                    opp_val = getattr(item, "types242", None)
                    
                    if opp_val == self:
                        setattr(item, "types242", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types242"):
                    opp_val = getattr(item, "types242", None)
                    
                    setattr(item, "types242", self)
                    

    @property
    def gast_types_GASTClass247(self):
        return self.__gast_types_GASTClass247

    @gast_types_GASTClass247.setter
    def gast_types_GASTClass247(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__gast_types_GASTClass247", None)
        self.__gast_types_GASTClass247 = value if value is not None else set()
        
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
    def gast_types_GASTClass258(self):
        return self.__gast_types_GASTClass258

    @gast_types_GASTClass258.setter
    def gast_types_GASTClass258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__gast_types_GASTClass258", None)
        self.__gast_types_GASTClass258 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Function259"):
                    opp_val = getattr(item, "Function259", None)
                    
                    if opp_val == self:
                        setattr(item, "Function259", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Function259"):
                    opp_val = getattr(item, "Function259", None)
                    
                    setattr(item, "Function259", self)
                    

    @property
    def GASTClass255(self):
        return self.__GASTClass255

    @GASTClass255.setter
    def GASTClass255(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__GASTClass255", None)
        self.__GASTClass255 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types256"):
                opp_val = getattr(old_value, "types256", None)
                if opp_val == self:
                    setattr(old_value, "types256", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types256"):
                opp_val = getattr(value, "types256", None)
                setattr(value, "types256", self)

    @property
    def gast_types_GASTClass261(self):
        return self.__gast_types_GASTClass261

    @gast_types_GASTClass261.setter
    def gast_types_GASTClass261(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__gast_types_GASTClass261", None)
        self.__gast_types_GASTClass261 = value if value is not None else set()
        
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
    def Field(self):
        return self.__Field

    @Field.setter
    def Field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__Field", None)
        self.__Field = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "variables229"):
                    opp_val = getattr(item, "variables229", None)
                    
                    if opp_val == self:
                        setattr(item, "variables229", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "variables229"):
                    opp_val = getattr(item, "variables229", None)
                    
                    setattr(item, "variables229", self)
                    

class gast_functions_Delegate(types_Member, types_GASTType, functions_Function):

    def __init__(self, innerDelegate: bool, gast_functions_Delegate314: set["Function"] = None, GASTClass317: "GASTClass" = None, Package320: "Package" = None, gast_functions_Delegate: "GASTClass" = None):
        self.innerDelegate = innerDelegate
        self.gast_functions_Delegate314 = gast_functions_Delegate314 if gast_functions_Delegate314 is not None else set()
        self.GASTClass317 = GASTClass317
        self.Package320 = Package320
        self.gast_functions_Delegate = gast_functions_Delegate
        
    @property
    def innerDelegate(self) -> bool:
        return self.__innerDelegate

    @innerDelegate.setter
    def innerDelegate(self, innerDelegate: bool):
        self.__innerDelegate = innerDelegate

    @property
    def Package320(self):
        return self.__Package320

    @Package320.setter
    def Package320(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Delegate__Package320", None)
        self.__Package320 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core321"):
                opp_val = getattr(old_value, "core321", None)
                if opp_val == self:
                    setattr(old_value, "core321", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core321"):
                opp_val = getattr(value, "core321", None)
                setattr(value, "core321", self)

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
            if hasattr(old_value, "GASTClass312"):
                opp_val = getattr(old_value, "GASTClass312", None)
                if opp_val == self:
                    setattr(old_value, "GASTClass312", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTClass312"):
                opp_val = getattr(value, "GASTClass312", None)
                setattr(value, "GASTClass312", self)

    @property
    def GASTClass317(self):
        return self.__GASTClass317

    @GASTClass317.setter
    def GASTClass317(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Delegate__GASTClass317", None)
        self.__GASTClass317 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types318"):
                opp_val = getattr(old_value, "types318", None)
                if opp_val == self:
                    setattr(old_value, "types318", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types318"):
                opp_val = getattr(value, "types318", None)
                setattr(value, "types318", self)

    @property
    def gast_functions_Delegate314(self):
        return self.__gast_functions_Delegate314

    @gast_functions_Delegate314.setter
    def gast_functions_Delegate314(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Delegate__gast_functions_Delegate314", None)
        self.__gast_functions_Delegate314 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Function315"):
                    opp_val = getattr(item, "Function315", None)
                    
                    if opp_val == self:
                        setattr(item, "Function315", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Function315"):
                    opp_val = getattr(item, "Function315", None)
                    
                    setattr(item, "Function315", self)
                    

class gast_types_TypeAlias(types_Member, types_TypeDecorator):

    def __init__(self, innerTypeAlias: bool, gast_types_TypeAlias: "GASTType" = None, GASTClass210: "GASTClass" = None, Package213: "Package" = None):
        self.innerTypeAlias = innerTypeAlias
        self.gast_types_TypeAlias = gast_types_TypeAlias
        self.GASTClass210 = GASTClass210
        self.Package213 = Package213
        
    @property
    def innerTypeAlias(self) -> bool:
        return self.__innerTypeAlias

    @innerTypeAlias.setter
    def innerTypeAlias(self, innerTypeAlias: bool):
        self.__innerTypeAlias = innerTypeAlias

    @property
    def GASTClass210(self):
        return self.__GASTClass210

    @GASTClass210.setter
    def GASTClass210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_TypeAlias__GASTClass210", None)
        self.__GASTClass210 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types211"):
                opp_val = getattr(old_value, "types211", None)
                if opp_val == self:
                    setattr(old_value, "types211", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types211"):
                opp_val = getattr(value, "types211", None)
                setattr(value, "types211", self)

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
            if hasattr(old_value, "GASTType208"):
                opp_val = getattr(old_value, "GASTType208", None)
                if opp_val == self:
                    setattr(old_value, "GASTType208", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTType208"):
                opp_val = getattr(value, "GASTType208", None)
                setattr(value, "GASTType208", self)

    @property
    def Package213(self):
        return self.__Package213

    @Package213.setter
    def Package213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_TypeAlias__Package213", None)
        self.__Package213 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core214"):
                opp_val = getattr(old_value, "core214", None)
                if opp_val == self:
                    setattr(old_value, "core214", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core214"):
                opp_val = getattr(value, "core214", None)
                setattr(value, "core214", self)

class TypeDecorator:

    pass
class gast_types_GASTArray(TypeDecorator):

    def __init__(self, dimensions: int, gast_types_GASTArray: "GASTType" = None):
        self.dimensions = dimensions
        self.gast_types_GASTArray = gast_types_GASTArray
        
    @property
    def dimensions(self) -> int:
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
            if hasattr(old_value, "GASTType206"):
                opp_val = getattr(old_value, "GASTType206", None)
                if opp_val == self:
                    setattr(old_value, "GASTType206", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTType206"):
                opp_val = getattr(value, "GASTType206", None)
                setattr(value, "GASTType206", self)

class gast_types_Reference(TypeDecorator):

    def __init__(self, explicit: bool, gast_types_Reference: "GASTType" = None):
        self.explicit = explicit
        self.gast_types_Reference = gast_types_Reference
        
    @property
    def explicit(self) -> bool:
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
            if hasattr(old_value, "GASTType199"):
                opp_val = getattr(old_value, "GASTType199", None)
                if opp_val == self:
                    setattr(old_value, "GASTType199", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTType199"):
                opp_val = getattr(value, "GASTType199", None)
                setattr(value, "GASTType199", self)

class gast_annotations_ModelAnnotation(ABC):

    pass
class core_SourceEntity:

    pass
class core_NamedModelElement:

    pass
class gast_variables_Variable(core_NamedModelElement, core_SourceEntity):

    def __init__(self, const: bool, gast_variables_Variable: "GASTType" = None, DeclarationTypeAccess364: "DeclarationTypeAccess" = None):
        self.const = const
        self.gast_variables_Variable = gast_variables_Variable
        self.DeclarationTypeAccess364 = DeclarationTypeAccess364
        
    @property
    def const(self) -> bool:
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
            if hasattr(old_value, "GASTType362"):
                opp_val = getattr(old_value, "GASTType362", None)
                if opp_val == self:
                    setattr(old_value, "GASTType362", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTType362"):
                opp_val = getattr(value, "GASTType362", None)
                setattr(value, "GASTType362", self)

    @property
    def DeclarationTypeAccess364(self):
        return self.__DeclarationTypeAccess364

    @DeclarationTypeAccess364.setter
    def DeclarationTypeAccess364(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_variables_Variable__DeclarationTypeAccess364", None)
        self.__DeclarationTypeAccess364 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accesses365"):
                opp_val = getattr(old_value, "accesses365", None)
                if opp_val == self:
                    setattr(old_value, "accesses365", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accesses365"):
                opp_val = getattr(value, "accesses365", None)
                setattr(value, "accesses365", self)

class gast_functions_Function(core_NamedModelElement, core_SourceEntity):

    def __init__(self, numberOfStatements: int, maximumNestingLevel: int, linesOfComments: int, numberOfEdgesInCFG: int, numberOfNodesInCFG: int, operator: bool, linesOfCode: int, DeclarationTypeAccess: "DeclarationTypeAccess" = None, FormalParameter: set["FormalParameter"] = None, LocalVariable: set["LocalVariable"] = None, gast_functions_Function: set["Statement"] = None, gast_functions_Function348: set["ThrowTypeAccess"] = None, gast_functions_Function350: set["Access"] = None, BlockStatement353: "BlockStatement" = None, GASTClass356: set["GASTClass"] = None):
        self.numberOfStatements = numberOfStatements
        self.maximumNestingLevel = maximumNestingLevel
        self.linesOfComments = linesOfComments
        self.numberOfEdgesInCFG = numberOfEdgesInCFG
        self.numberOfNodesInCFG = numberOfNodesInCFG
        self.operator = operator
        self.linesOfCode = linesOfCode
        self.DeclarationTypeAccess = DeclarationTypeAccess
        self.FormalParameter = FormalParameter if FormalParameter is not None else set()
        self.LocalVariable = LocalVariable if LocalVariable is not None else set()
        self.gast_functions_Function = gast_functions_Function if gast_functions_Function is not None else set()
        self.gast_functions_Function348 = gast_functions_Function348 if gast_functions_Function348 is not None else set()
        self.gast_functions_Function350 = gast_functions_Function350 if gast_functions_Function350 is not None else set()
        self.BlockStatement353 = BlockStatement353
        self.GASTClass356 = GASTClass356 if GASTClass356 is not None else set()
        
    @property
    def numberOfStatements(self) -> int:
        return self.__numberOfStatements

    @numberOfStatements.setter
    def numberOfStatements(self, numberOfStatements: int):
        self.__numberOfStatements = numberOfStatements

    @property
    def numberOfEdgesInCFG(self) -> int:
        return self.__numberOfEdgesInCFG

    @numberOfEdgesInCFG.setter
    def numberOfEdgesInCFG(self, numberOfEdgesInCFG: int):
        self.__numberOfEdgesInCFG = numberOfEdgesInCFG

    @property
    def linesOfComments(self) -> int:
        return self.__linesOfComments

    @linesOfComments.setter
    def linesOfComments(self, linesOfComments: int):
        self.__linesOfComments = linesOfComments

    @property
    def linesOfCode(self) -> int:
        return self.__linesOfCode

    @linesOfCode.setter
    def linesOfCode(self, linesOfCode: int):
        self.__linesOfCode = linesOfCode

    @property
    def maximumNestingLevel(self) -> int:
        return self.__maximumNestingLevel

    @maximumNestingLevel.setter
    def maximumNestingLevel(self, maximumNestingLevel: int):
        self.__maximumNestingLevel = maximumNestingLevel

    @property
    def operator(self) -> bool:
        return self.__operator

    @operator.setter
    def operator(self, operator: bool):
        self.__operator = operator

    @property
    def numberOfNodesInCFG(self) -> int:
        return self.__numberOfNodesInCFG

    @numberOfNodesInCFG.setter
    def numberOfNodesInCFG(self, numberOfNodesInCFG: int):
        self.__numberOfNodesInCFG = numberOfNodesInCFG

    @property
    def gast_functions_Function350(self):
        return self.__gast_functions_Function350

    @gast_functions_Function350.setter
    def gast_functions_Function350(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Function__gast_functions_Function350", None)
        self.__gast_functions_Function350 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Access351"):
                    opp_val = getattr(item, "Access351", None)
                    
                    if opp_val == self:
                        setattr(item, "Access351", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Access351"):
                    opp_val = getattr(item, "Access351", None)
                    
                    setattr(item, "Access351", self)
                    

    @property
    def LocalVariable(self):
        return self.__LocalVariable

    @LocalVariable.setter
    def LocalVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Function__LocalVariable", None)
        self.__LocalVariable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "variables344"):
                    opp_val = getattr(item, "variables344", None)
                    
                    if opp_val == self:
                        setattr(item, "variables344", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "variables344"):
                    opp_val = getattr(item, "variables344", None)
                    
                    setattr(item, "variables344", self)
                    

    @property
    def gast_functions_Function348(self):
        return self.__gast_functions_Function348

    @gast_functions_Function348.setter
    def gast_functions_Function348(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Function__gast_functions_Function348", None)
        self.__gast_functions_Function348 = value if value is not None else set()
        
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
    def DeclarationTypeAccess(self):
        return self.__DeclarationTypeAccess

    @DeclarationTypeAccess.setter
    def DeclarationTypeAccess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Function__DeclarationTypeAccess", None)
        self.__DeclarationTypeAccess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accesses340"):
                opp_val = getattr(old_value, "accesses340", None)
                if opp_val == self:
                    setattr(old_value, "accesses340", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accesses340"):
                opp_val = getattr(value, "accesses340", None)
                setattr(value, "accesses340", self)

    @property
    def GASTClass356(self):
        return self.__GASTClass356

    @GASTClass356.setter
    def GASTClass356(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Function__GASTClass356", None)
        self.__GASTClass356 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "types357"):
                    opp_val = getattr(item, "types357", None)
                    
                    if opp_val == self:
                        setattr(item, "types357", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types357"):
                    opp_val = getattr(item, "types357", None)
                    
                    setattr(item, "types357", self)
                    

    @property
    def BlockStatement353(self):
        return self.__BlockStatement353

    @BlockStatement353.setter
    def BlockStatement353(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Function__BlockStatement353", None)
        self.__BlockStatement353 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statements354"):
                opp_val = getattr(old_value, "statements354", None)
                if opp_val == self:
                    setattr(old_value, "statements354", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statements354"):
                opp_val = getattr(value, "statements354", None)
                setattr(value, "statements354", self)

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
                if hasattr(item, "Statement346"):
                    opp_val = getattr(item, "Statement346", None)
                    
                    if opp_val == self:
                        setattr(item, "Statement346", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Statement346"):
                    opp_val = getattr(item, "Statement346", None)
                    
                    setattr(item, "Statement346", self)
                    

    @property
    def FormalParameter(self):
        return self.__FormalParameter

    @FormalParameter.setter
    def FormalParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Function__FormalParameter", None)
        self.__FormalParameter = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "variables342"):
                    opp_val = getattr(item, "variables342", None)
                    
                    if opp_val == self:
                        setattr(item, "variables342", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "variables342"):
                    opp_val = getattr(item, "variables342", None)
                    
                    setattr(item, "variables342", self)
                    

class core_ModelElement:

    pass
class annotations_ModelAnnotation:

    pass
class gast_annotations_Comment(annotations_ModelAnnotation, core_SourceEntity):

    def __init__(self, todo: bool, formal: bool, todoCount: int, texts: str):
        self.todo = todo
        self.formal = formal
        self.todoCount = todoCount
        self.texts = texts
        
    @property
    def formal(self) -> bool:
        return self.__formal

    @formal.setter
    def formal(self, formal: bool):
        self.__formal = formal

    @property
    def texts(self) -> str:
        return self.__texts

    @texts.setter
    def texts(self, texts: str):
        self.__texts = texts

    @property
    def todo(self) -> bool:
        return self.__todo

    @todo.setter
    def todo(self, todo: bool):
        self.__todo = todo

    @property
    def todoCount(self) -> int:
        return self.__todoCount

    @todoCount.setter
    def todoCount(self, todoCount: int):
        self.__todoCount = todoCount

    def OCLtodo(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement OCLtodo method
        pass

class gast_annotations_CloneInstance(core_ModelElement, annotations_ModelAnnotation):

    pass
class gast_annotations_StructuralAbstraction(core_NamedModelElement, annotations_ModelAnnotation):

    pass
class gast_annotations_Clone(core_ModelElement, annotations_ModelAnnotation):

    pass
class types_GASTClass:

    pass
class gast_types_GenericClass(types_GASTClass, core_GenericEntity):

    pass
class gast_annotations_Attribute(types_GASTClass, annotations_ModelAnnotation):

    pass
class Position:

    pass
class gast_core_Position:

    def __init__(self, endColumn: int, startColumn: int, endLine: int, startLine: int, gast_core_Position: "File" = None, gast_core_Position178: "File" = None, SourceEntity: "SourceEntity" = None):
        self.endColumn = endColumn
        self.startColumn = startColumn
        self.endLine = endLine
        self.startLine = startLine
        self.gast_core_Position = gast_core_Position
        self.gast_core_Position178 = gast_core_Position178
        self.SourceEntity = SourceEntity
        
    @property
    def startLine(self) -> int:
        return self.__startLine

    @startLine.setter
    def startLine(self, startLine: int):
        self.__startLine = startLine

    @property
    def endLine(self) -> int:
        return self.__endLine

    @endLine.setter
    def endLine(self, endLine: int):
        self.__endLine = endLine

    @property
    def startColumn(self) -> int:
        return self.__startColumn

    @startColumn.setter
    def startColumn(self, startColumn: int):
        self.__startColumn = startColumn

    @property
    def endColumn(self) -> int:
        return self.__endColumn

    @endColumn.setter
    def endColumn(self, endColumn: int):
        self.__endColumn = endColumn

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
            if hasattr(old_value, "File176"):
                opp_val = getattr(old_value, "File176", None)
                if opp_val == self:
                    setattr(old_value, "File176", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "File176"):
                opp_val = getattr(value, "File176", None)
                setattr(value, "File176", self)

    @property
    def gast_core_Position178(self):
        return self.__gast_core_Position178

    @gast_core_Position178.setter
    def gast_core_Position178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Position__gast_core_Position178", None)
        self.__gast_core_Position178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "File179"):
                opp_val = getattr(old_value, "File179", None)
                if opp_val == self:
                    setattr(old_value, "File179", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "File179"):
                opp_val = getattr(value, "File179", None)
                setattr(value, "File179", self)

    @property
    def SourceEntity(self):
        return self.__SourceEntity

    @SourceEntity.setter
    def SourceEntity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Position__SourceEntity", None)
        self.__SourceEntity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core181"):
                opp_val = getattr(old_value, "core181", None)
                if opp_val == self:
                    setattr(old_value, "core181", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core181"):
                opp_val = getattr(value, "core181", None)
                setattr(value, "core181", self)

    def EitherAssemblyFileOrSourceFileSet(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement EitherAssemblyFileOrSourceFileSet method
        pass

class File:

    pass
class GASTType:

    pass
class gast_types_TypeDecorator(GASTType):

    pass
class BasePath:

    pass
class StructuralAbstraction:

    pass
class gast_annotations_Subsystem(StructuralAbstraction):

    pass
class gast_annotations_Layer(StructuralAbstraction):

    pass
class Clone:

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
class GlobalFunction:

    pass
class Delegate:

    pass
class Access:

    pass
class gast_accesses_FunctionAccess(Access):

    pass
class gast_accesses_VariableAccess(Access):

    def __init__(self, write: bool, gast_accesses_VariableAccess: "Variable" = None, Access264: "gast_types_GASTClass", Access: "gast_core_Package", Access351: "gast_functions_Function", Access100: "gast_core_Root"):
        self.write = write
        self.gast_accesses_VariableAccess = gast_accesses_VariableAccess
        
    @property
    def write(self) -> bool:
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
            if hasattr(old_value, "Variable305"):
                opp_val = getattr(old_value, "Variable305", None)
                if opp_val == self:
                    setattr(old_value, "Variable305", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable305"):
                opp_val = getattr(value, "Variable305", None)
                setattr(value, "Variable305", self)

class gast_accesses_TypeAccess(Access):

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
class NamedModelElement:

    pass
class gast_core_Directory(NamedModelElement):

    def __init__(self, fullQualifiedPath: str, fileSystemPath: str, Directory136: set["Directory"] = None, Directory139: "Directory" = None, File: set["File"] = None, BasePath144: "BasePath" = None):
        self.fullQualifiedPath = fullQualifiedPath
        self.fileSystemPath = fileSystemPath
        self.Directory136 = Directory136 if Directory136 is not None else set()
        self.Directory139 = Directory139
        self.File = File if File is not None else set()
        self.BasePath144 = BasePath144
        
    @property
    def fullQualifiedPath(self) -> str:
        return self.__fullQualifiedPath

    @fullQualifiedPath.setter
    def fullQualifiedPath(self, fullQualifiedPath: str):
        self.__fullQualifiedPath = fullQualifiedPath

    @property
    def fileSystemPath(self) -> str:
        return self.__fileSystemPath

    @fileSystemPath.setter
    def fileSystemPath(self, fileSystemPath: str):
        self.__fileSystemPath = fileSystemPath

    @property
    def File(self):
        return self.__File

    @File.setter
    def File(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Directory__File", None)
        self.__File = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core142"):
                    opp_val = getattr(item, "core142", None)
                    
                    if opp_val == self:
                        setattr(item, "core142", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core142"):
                    opp_val = getattr(item, "core142", None)
                    
                    setattr(item, "core142", self)
                    

    @property
    def BasePath144(self):
        return self.__BasePath144

    @BasePath144.setter
    def BasePath144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Directory__BasePath144", None)
        self.__BasePath144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core145"):
                opp_val = getattr(old_value, "core145", None)
                if opp_val == self:
                    setattr(old_value, "core145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core145"):
                opp_val = getattr(value, "core145", None)
                setattr(value, "core145", self)

    @property
    def Directory136(self):
        return self.__Directory136

    @Directory136.setter
    def Directory136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Directory__Directory136", None)
        self.__Directory136 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core137"):
                    opp_val = getattr(item, "core137", None)
                    
                    if opp_val == self:
                        setattr(item, "core137", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core137"):
                    opp_val = getattr(item, "core137", None)
                    
                    setattr(item, "core137", self)
                    

    @property
    def Directory139(self):
        return self.__Directory139

    @Directory139.setter
    def Directory139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Directory__Directory139", None)
        self.__Directory139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core140"):
                opp_val = getattr(old_value, "core140", None)
                if opp_val == self:
                    setattr(old_value, "core140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core140"):
                opp_val = getattr(value, "core140", None)
                setattr(value, "core140", self)

class gast_core_File(NamedModelElement):

    def __init__(self, sourceFile: bool, assemblyFile: bool, size: str, fullQualifiedPath: str, fileSystemPath: str, linesOfCode: int, gast_core_File149: set["GASTType"] = None, gast_core_File152: set["GASTType"] = None, gast_core_File155: set["GlobalVariable"] = None, gast_core_File158: set["GlobalFunction"] = None, gast_core_File: "Root" = None, gast_core_File161: set["GlobalFunction"] = None, gast_core_File164: set["GlobalVariable"] = None, gast_core_File167: set["Package"] = None, gast_core_File170: set["File"] = None, Directory173: "Directory" = None):
        self.sourceFile = sourceFile
        self.assemblyFile = assemblyFile
        self.size = size
        self.fullQualifiedPath = fullQualifiedPath
        self.fileSystemPath = fileSystemPath
        self.linesOfCode = linesOfCode
        self.gast_core_File149 = gast_core_File149 if gast_core_File149 is not None else set()
        self.gast_core_File152 = gast_core_File152 if gast_core_File152 is not None else set()
        self.gast_core_File155 = gast_core_File155 if gast_core_File155 is not None else set()
        self.gast_core_File158 = gast_core_File158 if gast_core_File158 is not None else set()
        self.gast_core_File = gast_core_File
        self.gast_core_File161 = gast_core_File161 if gast_core_File161 is not None else set()
        self.gast_core_File164 = gast_core_File164 if gast_core_File164 is not None else set()
        self.gast_core_File167 = gast_core_File167 if gast_core_File167 is not None else set()
        self.gast_core_File170 = gast_core_File170 if gast_core_File170 is not None else set()
        self.Directory173 = Directory173
        
    @property
    def sourceFile(self) -> bool:
        return self.__sourceFile

    @sourceFile.setter
    def sourceFile(self, sourceFile: bool):
        self.__sourceFile = sourceFile

    @property
    def assemblyFile(self) -> bool:
        return self.__assemblyFile

    @assemblyFile.setter
    def assemblyFile(self, assemblyFile: bool):
        self.__assemblyFile = assemblyFile

    @property
    def fullQualifiedPath(self) -> str:
        return self.__fullQualifiedPath

    @fullQualifiedPath.setter
    def fullQualifiedPath(self, fullQualifiedPath: str):
        self.__fullQualifiedPath = fullQualifiedPath

    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def linesOfCode(self) -> int:
        return self.__linesOfCode

    @linesOfCode.setter
    def linesOfCode(self, linesOfCode: int):
        self.__linesOfCode = linesOfCode

    @property
    def fileSystemPath(self) -> str:
        return self.__fileSystemPath

    @fileSystemPath.setter
    def fileSystemPath(self, fileSystemPath: str):
        self.__fileSystemPath = fileSystemPath

    @property
    def gast_core_File170(self):
        return self.__gast_core_File170

    @gast_core_File170.setter
    def gast_core_File170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File170", None)
        self.__gast_core_File170 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "File171"):
                    opp_val = getattr(item, "File171", None)
                    
                    if opp_val == self:
                        setattr(item, "File171", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "File171"):
                    opp_val = getattr(item, "File171", None)
                    
                    setattr(item, "File171", self)
                    

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
            if hasattr(old_value, "Root147"):
                opp_val = getattr(old_value, "Root147", None)
                if opp_val == self:
                    setattr(old_value, "Root147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Root147"):
                opp_val = getattr(value, "Root147", None)
                setattr(value, "Root147", self)

    @property
    def gast_core_File155(self):
        return self.__gast_core_File155

    @gast_core_File155.setter
    def gast_core_File155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File155", None)
        self.__gast_core_File155 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalVariable156"):
                    opp_val = getattr(item, "GlobalVariable156", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalVariable156", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalVariable156"):
                    opp_val = getattr(item, "GlobalVariable156", None)
                    
                    setattr(item, "GlobalVariable156", self)
                    

    @property
    def gast_core_File164(self):
        return self.__gast_core_File164

    @gast_core_File164.setter
    def gast_core_File164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File164", None)
        self.__gast_core_File164 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalVariable165"):
                    opp_val = getattr(item, "GlobalVariable165", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalVariable165", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalVariable165"):
                    opp_val = getattr(item, "GlobalVariable165", None)
                    
                    setattr(item, "GlobalVariable165", self)
                    

    @property
    def gast_core_File167(self):
        return self.__gast_core_File167

    @gast_core_File167.setter
    def gast_core_File167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File167", None)
        self.__gast_core_File167 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package168"):
                    opp_val = getattr(item, "Package168", None)
                    
                    if opp_val == self:
                        setattr(item, "Package168", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package168"):
                    opp_val = getattr(item, "Package168", None)
                    
                    setattr(item, "Package168", self)
                    

    @property
    def Directory173(self):
        return self.__Directory173

    @Directory173.setter
    def Directory173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__Directory173", None)
        self.__Directory173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core174"):
                opp_val = getattr(old_value, "core174", None)
                if opp_val == self:
                    setattr(old_value, "core174", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core174"):
                opp_val = getattr(value, "core174", None)
                setattr(value, "core174", self)

    @property
    def gast_core_File152(self):
        return self.__gast_core_File152

    @gast_core_File152.setter
    def gast_core_File152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File152", None)
        self.__gast_core_File152 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTType153"):
                    opp_val = getattr(item, "GASTType153", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTType153", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTType153"):
                    opp_val = getattr(item, "GASTType153", None)
                    
                    setattr(item, "GASTType153", self)
                    

    @property
    def gast_core_File161(self):
        return self.__gast_core_File161

    @gast_core_File161.setter
    def gast_core_File161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File161", None)
        self.__gast_core_File161 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalFunction162"):
                    opp_val = getattr(item, "GlobalFunction162", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalFunction162", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalFunction162"):
                    opp_val = getattr(item, "GlobalFunction162", None)
                    
                    setattr(item, "GlobalFunction162", self)
                    

    @property
    def gast_core_File149(self):
        return self.__gast_core_File149

    @gast_core_File149.setter
    def gast_core_File149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File149", None)
        self.__gast_core_File149 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTType150"):
                    opp_val = getattr(item, "GASTType150", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTType150", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTType150"):
                    opp_val = getattr(item, "GASTType150", None)
                    
                    setattr(item, "GASTType150", self)
                    

    @property
    def gast_core_File158(self):
        return self.__gast_core_File158

    @gast_core_File158.setter
    def gast_core_File158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File158", None)
        self.__gast_core_File158 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalFunction159"):
                    opp_val = getattr(item, "GlobalFunction159", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalFunction159", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalFunction159"):
                    opp_val = getattr(item, "GlobalFunction159", None)
                    
                    setattr(item, "GlobalFunction159", self)
                    

class gast_types_GASTType(NamedModelElement):

    def __init__(self, qualifiedName: str, referenceType: bool):
        self.qualifiedName = qualifiedName
        self.referenceType = referenceType
        
    @property
    def referenceType(self) -> bool:
        return self.__referenceType

    @referenceType.setter
    def referenceType(self, referenceType: bool):
        self.__referenceType = referenceType

    @property
    def qualifiedName(self) -> str:
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName

class gast_core_Package(NamedModelElement):

    def __init__(self, linesOfComments: int, linesOfCode: int, qualifiedName: str, gast_core_Package: set["GASTClass"] = None, gast_core_Package68: set["GASTClass"] = None, gast_core_Package71: set["GASTClass"] = None, gast_core_Package74: set["GASTClass"] = None, gast_core_Package77: set["Access"] = None, Delegate: set["Delegate"] = None, GlobalFunction: set["GlobalFunction"] = None, GlobalVariable: set["GlobalVariable"] = None, Root84: "Root" = None, GASTClass87: set["GASTClass"] = None, Package: set["Package"] = None, Package91: "Package" = None, gast_core_Package94: set["Package"] = None, TypeAlias: set["TypeAlias"] = None):
        self.linesOfComments = linesOfComments
        self.linesOfCode = linesOfCode
        self.qualifiedName = qualifiedName
        self.gast_core_Package = gast_core_Package if gast_core_Package is not None else set()
        self.gast_core_Package68 = gast_core_Package68 if gast_core_Package68 is not None else set()
        self.gast_core_Package71 = gast_core_Package71 if gast_core_Package71 is not None else set()
        self.gast_core_Package74 = gast_core_Package74 if gast_core_Package74 is not None else set()
        self.gast_core_Package77 = gast_core_Package77 if gast_core_Package77 is not None else set()
        self.Delegate = Delegate if Delegate is not None else set()
        self.GlobalFunction = GlobalFunction if GlobalFunction is not None else set()
        self.GlobalVariable = GlobalVariable if GlobalVariable is not None else set()
        self.Root84 = Root84
        self.GASTClass87 = GASTClass87 if GASTClass87 is not None else set()
        self.Package = Package if Package is not None else set()
        self.Package91 = Package91
        self.gast_core_Package94 = gast_core_Package94 if gast_core_Package94 is not None else set()
        self.TypeAlias = TypeAlias if TypeAlias is not None else set()
        
    @property
    def linesOfComments(self) -> int:
        return self.__linesOfComments

    @linesOfComments.setter
    def linesOfComments(self, linesOfComments: int):
        self.__linesOfComments = linesOfComments

    @property
    def linesOfCode(self) -> int:
        return self.__linesOfCode

    @linesOfCode.setter
    def linesOfCode(self, linesOfCode: int):
        self.__linesOfCode = linesOfCode

    @property
    def qualifiedName(self) -> str:
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName

    @property
    def GlobalFunction(self):
        return self.__GlobalFunction

    @GlobalFunction.setter
    def GlobalFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__GlobalFunction", None)
        self.__GlobalFunction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "functions81"):
                    opp_val = getattr(item, "functions81", None)
                    
                    if opp_val == self:
                        setattr(item, "functions81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "functions81"):
                    opp_val = getattr(item, "functions81", None)
                    
                    setattr(item, "functions81", self)
                    

    @property
    def gast_core_Package68(self):
        return self.__gast_core_Package68

    @gast_core_Package68.setter
    def gast_core_Package68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__gast_core_Package68", None)
        self.__gast_core_Package68 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass69"):
                    opp_val = getattr(item, "GASTClass69", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass69", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass69"):
                    opp_val = getattr(item, "GASTClass69", None)
                    
                    setattr(item, "GASTClass69", self)
                    

    @property
    def Package(self):
        return self.__Package

    @Package.setter
    def Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__Package", None)
        self.__Package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core89"):
                    opp_val = getattr(item, "core89", None)
                    
                    if opp_val == self:
                        setattr(item, "core89", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core89"):
                    opp_val = getattr(item, "core89", None)
                    
                    setattr(item, "core89", self)
                    

    @property
    def GASTClass87(self):
        return self.__GASTClass87

    @GASTClass87.setter
    def GASTClass87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__GASTClass87", None)
        self.__GASTClass87 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "types"):
                    opp_val = getattr(item, "types", None)
                    
                    if opp_val == self:
                        setattr(item, "types", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types"):
                    opp_val = getattr(item, "types", None)
                    
                    setattr(item, "types", self)
                    

    @property
    def gast_core_Package74(self):
        return self.__gast_core_Package74

    @gast_core_Package74.setter
    def gast_core_Package74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__gast_core_Package74", None)
        self.__gast_core_Package74 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass75"):
                    opp_val = getattr(item, "GASTClass75", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass75", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass75"):
                    opp_val = getattr(item, "GASTClass75", None)
                    
                    setattr(item, "GASTClass75", self)
                    

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
                if hasattr(item, "GASTClass72"):
                    opp_val = getattr(item, "GASTClass72", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass72", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass72"):
                    opp_val = getattr(item, "GASTClass72", None)
                    
                    setattr(item, "GASTClass72", self)
                    

    @property
    def TypeAlias(self):
        return self.__TypeAlias

    @TypeAlias.setter
    def TypeAlias(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__TypeAlias", None)
        self.__TypeAlias = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "types97"):
                    opp_val = getattr(item, "types97", None)
                    
                    if opp_val == self:
                        setattr(item, "types97", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types97"):
                    opp_val = getattr(item, "types97", None)
                    
                    setattr(item, "types97", self)
                    

    @property
    def GlobalVariable(self):
        return self.__GlobalVariable

    @GlobalVariable.setter
    def GlobalVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__GlobalVariable", None)
        self.__GlobalVariable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "variables"):
                    opp_val = getattr(item, "variables", None)
                    
                    if opp_val == self:
                        setattr(item, "variables", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "variables"):
                    opp_val = getattr(item, "variables", None)
                    
                    setattr(item, "variables", self)
                    

    @property
    def gast_core_Package94(self):
        return self.__gast_core_Package94

    @gast_core_Package94.setter
    def gast_core_Package94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__gast_core_Package94", None)
        self.__gast_core_Package94 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package95"):
                    opp_val = getattr(item, "Package95", None)
                    
                    if opp_val == self:
                        setattr(item, "Package95", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package95"):
                    opp_val = getattr(item, "Package95", None)
                    
                    setattr(item, "Package95", self)
                    

    @property
    def Root84(self):
        return self.__Root84

    @Root84.setter
    def Root84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__Root84", None)
        self.__Root84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core85"):
                opp_val = getattr(old_value, "core85", None)
                if opp_val == self:
                    setattr(old_value, "core85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core85"):
                opp_val = getattr(value, "core85", None)
                setattr(value, "core85", self)

    @property
    def gast_core_Package77(self):
        return self.__gast_core_Package77

    @gast_core_Package77.setter
    def gast_core_Package77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__gast_core_Package77", None)
        self.__gast_core_Package77 = value if value is not None else set()
        
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
    def Delegate(self):
        return self.__Delegate

    @Delegate.setter
    def Delegate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__Delegate", None)
        self.__Delegate = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "functions79"):
                    opp_val = getattr(item, "functions79", None)
                    
                    if opp_val == self:
                        setattr(item, "functions79", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "functions79"):
                    opp_val = getattr(item, "functions79", None)
                    
                    setattr(item, "functions79", self)
                    

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
    def Package91(self):
        return self.__Package91

    @Package91.setter
    def Package91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__Package91", None)
        self.__Package91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core92"):
                opp_val = getattr(old_value, "core92", None)
                if opp_val == self:
                    setattr(old_value, "core92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core92"):
                opp_val = getattr(value, "core92", None)
                setattr(value, "core92", self)

class ModelAnnotation:

    pass
class Identifier:

    pass
class gast_core_ModelElement(Identifier):

    def __init__(self, status: str, sissyId: int, gast_core_ModelElement: set["ModelAnnotation"] = None):
        self.status = status
        self.sissyId = sissyId
        self.gast_core_ModelElement = gast_core_ModelElement if gast_core_ModelElement is not None else set()
        
    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def sissyId(self) -> int:
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
                    

class gast_core_Identifier(ABC):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    def idHasToBeUnique(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement idHasToBeUnique method
        pass

class Directory:

    pass
class Root:

    pass
class ModelElement:

    pass
class gast_core_GenericEntity(ModelElement):

    pass
class gast_core_NamedModelElement(ModelElement):

    def __init__(self, simpleName: str, ModelElement129: "gast_core_Root", ModelElement310: "gast_accesses_Access", ModelElement: "gast_core_Root"):
        self.simpleName = simpleName
        
    @property
    def simpleName(self) -> str:
        return self.__simpleName

    @simpleName.setter
    def simpleName(self, simpleName: str):
        self.__simpleName = simpleName

class gast_core_Root(ModelElement):

    def __init__(self, linesOfComments: int, linesOfCode: int, gast_core_Root: set["Access"] = None, gast_core_Root102: set["GASTClass"] = None, gast_core_Root105: set["GASTClass"] = None, gast_core_Root108: set["GASTClass"] = None, gast_core_Root111: set["GASTClass"] = None, gast_core_Root114: set["ModelElement"] = None, gast_core_Root116: set["GlobalVariable"] = None, Package119: set["Package"] = None, Clone: set["Clone"] = None, gast_core_Root124: set["StructuralAbstraction"] = None, gast_core_Root128: set["ModelElement"] = None, BasePath: set["BasePath"] = None, GlobalFunction133: set["GlobalFunction"] = None, gast_core_Root126: set["GASTType"] = None, ModelElement129: "gast_core_Root", ModelElement310: "gast_accesses_Access", ModelElement: "gast_core_Root"):
        self.linesOfComments = linesOfComments
        self.linesOfCode = linesOfCode
        self.gast_core_Root = gast_core_Root if gast_core_Root is not None else set()
        self.gast_core_Root102 = gast_core_Root102 if gast_core_Root102 is not None else set()
        self.gast_core_Root105 = gast_core_Root105 if gast_core_Root105 is not None else set()
        self.gast_core_Root108 = gast_core_Root108 if gast_core_Root108 is not None else set()
        self.gast_core_Root111 = gast_core_Root111 if gast_core_Root111 is not None else set()
        self.gast_core_Root114 = gast_core_Root114 if gast_core_Root114 is not None else set()
        self.gast_core_Root116 = gast_core_Root116 if gast_core_Root116 is not None else set()
        self.Package119 = Package119 if Package119 is not None else set()
        self.Clone = Clone if Clone is not None else set()
        self.gast_core_Root124 = gast_core_Root124 if gast_core_Root124 is not None else set()
        self.gast_core_Root128 = gast_core_Root128 if gast_core_Root128 is not None else set()
        self.BasePath = BasePath if BasePath is not None else set()
        self.GlobalFunction133 = GlobalFunction133 if GlobalFunction133 is not None else set()
        self.gast_core_Root126 = gast_core_Root126 if gast_core_Root126 is not None else set()
        
    @property
    def linesOfComments(self) -> int:
        return self.__linesOfComments

    @linesOfComments.setter
    def linesOfComments(self, linesOfComments: int):
        self.__linesOfComments = linesOfComments

    @property
    def linesOfCode(self) -> int:
        return self.__linesOfCode

    @linesOfCode.setter
    def linesOfCode(self, linesOfCode: int):
        self.__linesOfCode = linesOfCode

    @property
    def Clone(self):
        return self.__Clone

    @Clone.setter
    def Clone(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__Clone", None)
        self.__Clone = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "annotations122"):
                    opp_val = getattr(item, "annotations122", None)
                    
                    if opp_val == self:
                        setattr(item, "annotations122", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "annotations122"):
                    opp_val = getattr(item, "annotations122", None)
                    
                    setattr(item, "annotations122", self)
                    

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
                if hasattr(item, "GlobalVariable117"):
                    opp_val = getattr(item, "GlobalVariable117", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalVariable117", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalVariable117"):
                    opp_val = getattr(item, "GlobalVariable117", None)
                    
                    setattr(item, "GlobalVariable117", self)
                    

    @property
    def BasePath(self):
        return self.__BasePath

    @BasePath.setter
    def BasePath(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__BasePath", None)
        self.__BasePath = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core131"):
                    opp_val = getattr(item, "core131", None)
                    
                    if opp_val == self:
                        setattr(item, "core131", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core131"):
                    opp_val = getattr(item, "core131", None)
                    
                    setattr(item, "core131", self)
                    

    @property
    def gast_core_Root108(self):
        return self.__gast_core_Root108

    @gast_core_Root108.setter
    def gast_core_Root108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root108", None)
        self.__gast_core_Root108 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass109"):
                    opp_val = getattr(item, "GASTClass109", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass109", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass109"):
                    opp_val = getattr(item, "GASTClass109", None)
                    
                    setattr(item, "GASTClass109", self)
                    

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
                if hasattr(item, "GASTClass106"):
                    opp_val = getattr(item, "GASTClass106", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass106", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass106"):
                    opp_val = getattr(item, "GASTClass106", None)
                    
                    setattr(item, "GASTClass106", self)
                    

    @property
    def Package119(self):
        return self.__Package119

    @Package119.setter
    def Package119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__Package119", None)
        self.__Package119 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core120"):
                    opp_val = getattr(item, "core120", None)
                    
                    if opp_val == self:
                        setattr(item, "core120", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core120"):
                    opp_val = getattr(item, "core120", None)
                    
                    setattr(item, "core120", self)
                    

    @property
    def gast_core_Root126(self):
        return self.__gast_core_Root126

    @gast_core_Root126.setter
    def gast_core_Root126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root126", None)
        self.__gast_core_Root126 = value if value is not None else set()
        
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
    def GlobalFunction133(self):
        return self.__GlobalFunction133

    @GlobalFunction133.setter
    def GlobalFunction133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__GlobalFunction133", None)
        self.__GlobalFunction133 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "functions134"):
                    opp_val = getattr(item, "functions134", None)
                    
                    if opp_val == self:
                        setattr(item, "functions134", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "functions134"):
                    opp_val = getattr(item, "functions134", None)
                    
                    setattr(item, "functions134", self)
                    

    @property
    def gast_core_Root124(self):
        return self.__gast_core_Root124

    @gast_core_Root124.setter
    def gast_core_Root124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root124", None)
        self.__gast_core_Root124 = value if value is not None else set()
        
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
                if hasattr(item, "Access100"):
                    opp_val = getattr(item, "Access100", None)
                    
                    if opp_val == self:
                        setattr(item, "Access100", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Access100"):
                    opp_val = getattr(item, "Access100", None)
                    
                    setattr(item, "Access100", self)
                    

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
    def gast_core_Root111(self):
        return self.__gast_core_Root111

    @gast_core_Root111.setter
    def gast_core_Root111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root111", None)
        self.__gast_core_Root111 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass112"):
                    opp_val = getattr(item, "GASTClass112", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass112", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass112"):
                    opp_val = getattr(item, "GASTClass112", None)
                    
                    setattr(item, "GASTClass112", self)
                    

    @property
    def gast_core_Root128(self):
        return self.__gast_core_Root128

    @gast_core_Root128.setter
    def gast_core_Root128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root128", None)
        self.__gast_core_Root128 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelElement129"):
                    opp_val = getattr(item, "ModelElement129", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelElement129", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelElement129"):
                    opp_val = getattr(item, "ModelElement129", None)
                    
                    setattr(item, "ModelElement129", self)
                    

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
                    

    def getPackageByName(self, name: str) -> str:
        # TODO: Implement getPackageByName method
        pass

    def getPackageByQualifiedName(self, qualifiedName: str) -> str:
        # TODO: Implement getPackageByQualifiedName method
        pass

class gast_core_SourceEntity(ModelElement):

    pass
class gast_core_BasePath(ModelElement):

    def __init__(self, path: str, Root: "Root" = None, Directory: set["Directory"] = None, ModelElement129: "gast_core_Root", ModelElement310: "gast_accesses_Access", ModelElement: "gast_core_Root"):
        self.path = path
        self.Root = Root
        self.Directory = Directory if Directory is not None else set()
        
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def Root(self):
        return self.__Root

    @Root.setter
    def Root(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_BasePath__Root", None)
        self.__Root = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core"):
                opp_val = getattr(old_value, "core", None)
                if opp_val == self:
                    setattr(old_value, "core", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core"):
                opp_val = getattr(value, "core", None)
                setattr(value, "core", self)

    @property
    def Directory(self):
        return self.__Directory

    @Directory.setter
    def Directory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_BasePath__Directory", None)
        self.__Directory = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core64"):
                    opp_val = getattr(item, "core64", None)
                    
                    if opp_val == self:
                        setattr(item, "core64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core64"):
                    opp_val = getattr(item, "core64", None)
                    
                    setattr(item, "core64", self)
                    

class gast_statements_Var:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Var:

    pass
class gast_statements_Param(Var):

    pass
class gast_statements_FlowInstr:

    def __init__(self, txt: str, FlowInstr: set["FlowInstr"] = None, FlowInstr60: set["FlowInstr"] = None, gast_statements_FlowInstr: set["Var"] = None, gast_statements_FlowInstr55: set["Var"] = None):
        self.txt = txt
        self.FlowInstr = FlowInstr if FlowInstr is not None else set()
        self.FlowInstr60 = FlowInstr60 if FlowInstr60 is not None else set()
        self.gast_statements_FlowInstr = gast_statements_FlowInstr if gast_statements_FlowInstr is not None else set()
        self.gast_statements_FlowInstr55 = gast_statements_FlowInstr55 if gast_statements_FlowInstr55 is not None else set()
        
    @property
    def txt(self) -> str:
        return self.__txt

    @txt.setter
    def txt(self, txt: str):
        self.__txt = txt

    @property
    def gast_statements_FlowInstr55(self):
        return self.__gast_statements_FlowInstr55

    @gast_statements_FlowInstr55.setter
    def gast_statements_FlowInstr55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_FlowInstr__gast_statements_FlowInstr55", None)
        self.__gast_statements_FlowInstr55 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Var56"):
                    opp_val = getattr(item, "Var56", None)
                    
                    if opp_val == self:
                        setattr(item, "Var56", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Var56"):
                    opp_val = getattr(item, "Var56", None)
                    
                    setattr(item, "Var56", self)
                    

    @property
    def FlowInstr60(self):
        return self.__FlowInstr60

    @FlowInstr60.setter
    def FlowInstr60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_FlowInstr__FlowInstr60", None)
        self.__FlowInstr60 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statements61"):
                    opp_val = getattr(item, "statements61", None)
                    
                    if opp_val == self:
                        setattr(item, "statements61", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statements61"):
                    opp_val = getattr(item, "statements61", None)
                    
                    setattr(item, "statements61", self)
                    

    @property
    def FlowInstr(self):
        return self.__FlowInstr

    @FlowInstr.setter
    def FlowInstr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_FlowInstr__FlowInstr", None)
        self.__FlowInstr = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statements58"):
                    opp_val = getattr(item, "statements58", None)
                    
                    if opp_val == self:
                        setattr(item, "statements58", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statements58"):
                    opp_val = getattr(item, "statements58", None)
                    
                    setattr(item, "statements58", self)
                    

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
                    

class FlowInstr:

    pass
class gast_statements_Exit(FlowInstr):

    def __init__(self, name: str, statements61: "gast_statements_FlowInstr", statements58: "gast_statements_FlowInstr"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Exit:

    pass
class statements_BlockStatement:

    pass
class gast_statements_GASTBehaviour:

    pass
class statements_FlowInstr:

    pass
class gast_statements_Methods(statements_BlockStatement, statements_FlowInstr):

    def __init__(self, methodName: str, gast_statements_Methods: "Exit" = None):
        self.methodName = methodName
        self.gast_statements_Methods = gast_statements_Methods
        
    @property
    def methodName(self) -> str:
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

class statements_Statement:

    pass
class gast_statements_JumpStatement(statements_FlowInstr, statements_Statement):

    def __init__(self, kind: str, gast_statements_JumpStatement: "GASTExpression" = None):
        self.kind = kind
        self.gast_statements_JumpStatement = gast_statements_JumpStatement
        
    @property
    def kind(self) -> str:
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
            if hasattr(old_value, "GASTExpression47"):
                opp_val = getattr(old_value, "GASTExpression47", None)
                if opp_val == self:
                    setattr(old_value, "GASTExpression47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTExpression47"):
                opp_val = getattr(value, "GASTExpression47", None)
                setattr(value, "GASTExpression47", self)

class gast_statements_SimpleStatement(statements_FlowInstr, statements_Statement):

    pass
class CatchParameter:

    pass
class BranchStatement:

    pass
class Function:

    pass
class gast_functions_GlobalFunction(Function):

    def __init__(self, kind: str, Package329: "Package" = None, Root332: "Root" = None, functions291: "gast_accesses_DeclarationTypeAccess", Function295: "gast_accesses_DelegateAccess", Function303: "gast_accesses_FunctionAccess", Function315: "gast_functions_Delegate", functions234: "gast_types_GASTClass", functions371: "gast_variables_LocalVariable", functions360: "gast_variables_FormalParameter", Function259: "gast_types_GASTClass", functions: "gast_statements_BlockStatement", Function286: "gast_accesses_BaseAccess"):
        self.kind = kind
        self.Package329 = Package329
        self.Root332 = Root332
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def Package329(self):
        return self.__Package329

    @Package329.setter
    def Package329(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_GlobalFunction__Package329", None)
        self.__Package329 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core330"):
                opp_val = getattr(old_value, "core330", None)
                if opp_val == self:
                    setattr(old_value, "core330", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core330"):
                opp_val = getattr(value, "core330", None)
                setattr(value, "core330", self)

    @property
    def Root332(self):
        return self.__Root332

    @Root332.setter
    def Root332(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_GlobalFunction__Root332", None)
        self.__Root332 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core333"):
                opp_val = getattr(old_value, "core333", None)
                if opp_val == self:
                    setattr(old_value, "core333", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core333"):
                opp_val = getattr(value, "core333", None)
                setattr(value, "core333", self)

class GASTExpression:

    pass
class LoopStatement:

    pass
class Branch:

    pass
class SourceEntity:

    pass
class gast_statements_Branch(SourceEntity):

    pass
class gast_types_Member(SourceEntity):

    def __init__(self, visibility: str, abstract: bool, extern: bool, final: bool, internal: bool, introspectable: bool, override: bool, static: bool, typeParameterClassMember: bool, virtual: bool, gast_types_Member: "Member" = None, core181: "gast_core_Position"):
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
        
    @property
    def virtual(self) -> bool:
        return self.__virtual

    @virtual.setter
    def virtual(self, virtual: bool):
        self.__virtual = virtual

    @property
    def internal(self) -> bool:
        return self.__internal

    @internal.setter
    def internal(self, internal: bool):
        self.__internal = internal

    @property
    def typeParameterClassMember(self) -> bool:
        return self.__typeParameterClassMember

    @typeParameterClassMember.setter
    def typeParameterClassMember(self, typeParameterClassMember: bool):
        self.__typeParameterClassMember = typeParameterClassMember

    @property
    def introspectable(self) -> bool:
        return self.__introspectable

    @introspectable.setter
    def introspectable(self, introspectable: bool):
        self.__introspectable = introspectable

    @property
    def final(self) -> bool:
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def override(self) -> bool:
        return self.__override

    @override.setter
    def override(self, override: bool):
        self.__override = override

    @property
    def extern(self) -> bool:
        return self.__extern

    @extern.setter
    def extern(self, extern: bool):
        self.__extern = extern

    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

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

    def getSurroundingClass(self) -> str:
        # TODO: Implement getSurroundingClass method
        pass

class gast_statements_GASTExpression(SourceEntity):

    pass
class gast_accesses_BaseAccess(SourceEntity):

    pass
class gast_statements_Statement(SourceEntity):

    def __init__(self, numberOfNodesInCFG: int, numberOfStatements: int, maximumNestingLevel: int, numberOfComments: int, linesOfCode: int, numberOfEdgesInCFG: int, BaseAccess: set["BaseAccess"] = None, CloneInstance: "CloneInstance" = None, Branch: "Branch" = None, BlockStatement9: "BlockStatement" = None, gast_statements_Statement: "Statement" = None, LoopStatement: "LoopStatement" = None, gast_statements_Statement16: set["Statement"] = None, gast_statements_Statement19: set["Statement"] = None, core181: "gast_core_Position"):
        self.numberOfNodesInCFG = numberOfNodesInCFG
        self.numberOfStatements = numberOfStatements
        self.maximumNestingLevel = maximumNestingLevel
        self.numberOfComments = numberOfComments
        self.linesOfCode = linesOfCode
        self.numberOfEdgesInCFG = numberOfEdgesInCFG
        self.BaseAccess = BaseAccess if BaseAccess is not None else set()
        self.CloneInstance = CloneInstance
        self.Branch = Branch
        self.BlockStatement9 = BlockStatement9
        self.gast_statements_Statement = gast_statements_Statement
        self.LoopStatement = LoopStatement
        self.gast_statements_Statement16 = gast_statements_Statement16 if gast_statements_Statement16 is not None else set()
        self.gast_statements_Statement19 = gast_statements_Statement19 if gast_statements_Statement19 is not None else set()
        
    @property
    def linesOfCode(self) -> int:
        return self.__linesOfCode

    @linesOfCode.setter
    def linesOfCode(self, linesOfCode: int):
        self.__linesOfCode = linesOfCode

    @property
    def numberOfEdgesInCFG(self) -> int:
        return self.__numberOfEdgesInCFG

    @numberOfEdgesInCFG.setter
    def numberOfEdgesInCFG(self, numberOfEdgesInCFG: int):
        self.__numberOfEdgesInCFG = numberOfEdgesInCFG

    @property
    def maximumNestingLevel(self) -> int:
        return self.__maximumNestingLevel

    @maximumNestingLevel.setter
    def maximumNestingLevel(self, maximumNestingLevel: int):
        self.__maximumNestingLevel = maximumNestingLevel

    @property
    def numberOfComments(self) -> int:
        return self.__numberOfComments

    @numberOfComments.setter
    def numberOfComments(self, numberOfComments: int):
        self.__numberOfComments = numberOfComments

    @property
    def numberOfNodesInCFG(self) -> int:
        return self.__numberOfNodesInCFG

    @numberOfNodesInCFG.setter
    def numberOfNodesInCFG(self, numberOfNodesInCFG: int):
        self.__numberOfNodesInCFG = numberOfNodesInCFG

    @property
    def numberOfStatements(self) -> int:
        return self.__numberOfStatements

    @numberOfStatements.setter
    def numberOfStatements(self, numberOfStatements: int):
        self.__numberOfStatements = numberOfStatements

    @property
    def CloneInstance(self):
        return self.__CloneInstance

    @CloneInstance.setter
    def CloneInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_Statement__CloneInstance", None)
        self.__CloneInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "annotations"):
                opp_val = getattr(old_value, "annotations", None)
                if opp_val == self:
                    setattr(old_value, "annotations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "annotations"):
                opp_val = getattr(value, "annotations", None)
                setattr(value, "annotations", self)

    @property
    def Branch(self):
        return self.__Branch

    @Branch.setter
    def Branch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_Statement__Branch", None)
        self.__Branch = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statements12"):
                opp_val = getattr(old_value, "statements12", None)
                if opp_val == self:
                    setattr(old_value, "statements12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statements12"):
                opp_val = getattr(value, "statements12", None)
                setattr(value, "statements12", self)

    @property
    def BaseAccess(self):
        return self.__BaseAccess

    @BaseAccess.setter
    def BaseAccess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_Statement__BaseAccess", None)
        self.__BaseAccess = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "accesses"):
                    opp_val = getattr(item, "accesses", None)
                    
                    if opp_val == self:
                        setattr(item, "accesses", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "accesses"):
                    opp_val = getattr(item, "accesses", None)
                    
                    setattr(item, "accesses", self)
                    

    @property
    def LoopStatement(self):
        return self.__LoopStatement

    @LoopStatement.setter
    def LoopStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_Statement__LoopStatement", None)
        self.__LoopStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statements14"):
                opp_val = getattr(old_value, "statements14", None)
                if opp_val == self:
                    setattr(old_value, "statements14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statements14"):
                opp_val = getattr(value, "statements14", None)
                setattr(value, "statements14", self)

    @property
    def gast_statements_Statement19(self):
        return self.__gast_statements_Statement19

    @gast_statements_Statement19.setter
    def gast_statements_Statement19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_Statement__gast_statements_Statement19", None)
        self.__gast_statements_Statement19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Statement20"):
                    opp_val = getattr(item, "Statement20", None)
                    
                    if opp_val == self:
                        setattr(item, "Statement20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Statement20"):
                    opp_val = getattr(item, "Statement20", None)
                    
                    setattr(item, "Statement20", self)
                    

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
    def BlockStatement9(self):
        return self.__BlockStatement9

    @BlockStatement9.setter
    def BlockStatement9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_Statement__BlockStatement9", None)
        self.__BlockStatement9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statements"):
                opp_val = getattr(old_value, "statements", None)
                if opp_val == self:
                    setattr(old_value, "statements", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statements"):
                opp_val = getattr(value, "statements", None)
                setattr(value, "statements", self)

    @property
    def gast_statements_Statement16(self):
        return self.__gast_statements_Statement16

    @gast_statements_Statement16.setter
    def gast_statements_Statement16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_Statement__gast_statements_Statement16", None)
        self.__gast_statements_Statement16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Statement17"):
                    opp_val = getattr(item, "Statement17", None)
                    
                    if opp_val == self:
                        setattr(item, "Statement17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Statement17"):
                    opp_val = getattr(item, "Statement17", None)
                    
                    setattr(item, "Statement17", self)
                    

class BlockStatement:

    pass
class gast_statements_CatchBlock(BlockStatement):

    pass
class CatchBlock:

    pass
class Statement:

    pass
class gast_statements_LoopStatement(Statement):

    def __init__(self, kind: str, gast_statements_LoopStatement: "GASTExpression" = None, gast_statements_LoopStatement37: "GASTExpression" = None, gast_statements_LoopStatement40: "GASTExpression" = None, Statement43: "Statement" = None, Statement280: "gast_accesses_BaseAccess", Statement17: "gast_statements_Statement", Statement20: "gast_statements_Statement", statements278: "gast_accesses_BaseAccess", statements194: "gast_annotations_CloneInstance", Statement346: "gast_functions_Function", Statement: "gast_statements_Statement", statements44: "gast_statements_LoopStatement", statements30: "gast_statements_Branch", statements23: "gast_statements_BlockStatement"):
        self.kind = kind
        self.gast_statements_LoopStatement = gast_statements_LoopStatement
        self.gast_statements_LoopStatement37 = gast_statements_LoopStatement37
        self.gast_statements_LoopStatement40 = gast_statements_LoopStatement40
        self.Statement43 = Statement43
        
    @property
    def kind(self) -> str:
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
            if hasattr(old_value, "GASTExpression35"):
                opp_val = getattr(old_value, "GASTExpression35", None)
                if opp_val == self:
                    setattr(old_value, "GASTExpression35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTExpression35"):
                opp_val = getattr(value, "GASTExpression35", None)
                setattr(value, "GASTExpression35", self)

    @property
    def gast_statements_LoopStatement40(self):
        return self.__gast_statements_LoopStatement40

    @gast_statements_LoopStatement40.setter
    def gast_statements_LoopStatement40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_LoopStatement__gast_statements_LoopStatement40", None)
        self.__gast_statements_LoopStatement40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GASTExpression41"):
                opp_val = getattr(old_value, "GASTExpression41", None)
                if opp_val == self:
                    setattr(old_value, "GASTExpression41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTExpression41"):
                opp_val = getattr(value, "GASTExpression41", None)
                setattr(value, "GASTExpression41", self)

    @property
    def gast_statements_LoopStatement37(self):
        return self.__gast_statements_LoopStatement37

    @gast_statements_LoopStatement37.setter
    def gast_statements_LoopStatement37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_LoopStatement__gast_statements_LoopStatement37", None)
        self.__gast_statements_LoopStatement37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GASTExpression38"):
                opp_val = getattr(old_value, "GASTExpression38", None)
                if opp_val == self:
                    setattr(old_value, "GASTExpression38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTExpression38"):
                opp_val = getattr(value, "GASTExpression38", None)
                setattr(value, "GASTExpression38", self)

    @property
    def Statement43(self):
        return self.__Statement43

    @Statement43.setter
    def Statement43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_LoopStatement__Statement43", None)
        self.__Statement43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statements44"):
                opp_val = getattr(old_value, "statements44", None)
                if opp_val == self:
                    setattr(old_value, "statements44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statements44"):
                opp_val = getattr(value, "statements44", None)
                setattr(value, "statements44", self)

class gast_statements_BranchStatement(Statement):

    pass
class gast_statements_BlockStatement(Statement):

    def __init__(self, synchronized: bool, Statement22: set["Statement"] = None, Function: "Function" = None, Statement280: "gast_accesses_BaseAccess", Statement17: "gast_statements_Statement", Statement20: "gast_statements_Statement", statements278: "gast_accesses_BaseAccess", statements194: "gast_annotations_CloneInstance", Statement346: "gast_functions_Function", Statement: "gast_statements_Statement", statements44: "gast_statements_LoopStatement", statements30: "gast_statements_Branch", statements23: "gast_statements_BlockStatement"):
        self.synchronized = synchronized
        self.Statement22 = Statement22 if Statement22 is not None else set()
        self.Function = Function
        
    @property
    def synchronized(self) -> bool:
        return self.__synchronized

    @synchronized.setter
    def synchronized(self, synchronized: bool):
        self.__synchronized = synchronized

    @property
    def Function(self):
        return self.__Function

    @Function.setter
    def Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_BlockStatement__Function", None)
        self.__Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "functions"):
                opp_val = getattr(old_value, "functions", None)
                if opp_val == self:
                    setattr(old_value, "functions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "functions"):
                opp_val = getattr(value, "functions", None)
                setattr(value, "functions", self)

    @property
    def Statement22(self):
        return self.__Statement22

    @Statement22.setter
    def Statement22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_BlockStatement__Statement22", None)
        self.__Statement22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statements23"):
                    opp_val = getattr(item, "statements23", None)
                    
                    if opp_val == self:
                        setattr(item, "statements23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statements23"):
                    opp_val = getattr(item, "statements23", None)
                    
                    setattr(item, "statements23", self)
                    

class gast_statements_ExceptionHandler(Statement):

    pass
class CloneInstance:

    pass
class BaseAccess:

    pass
class gast_accesses_CompositeAccess(BaseAccess):

    pass
class gast_accesses_Access(BaseAccess):

    pass