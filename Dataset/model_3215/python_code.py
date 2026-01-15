from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class LoopStatementKind(Enum):
    FOREACH = "FOREACH"
    WHILE = "WHILE"
    DOWHILE = "DOWHILE"
    FOR = "FOR"
class Visibilities(Enum):
    VISIBILITYPRIVAT = "VISIBILITYPRIVAT"
    VISIBILITYSTRICTPROTECTED = "VISIBILITYSTRICTPROTECTED"
    VISIBILITYPUBLIC = "VISIBILITYPUBLIC"
    VISIBILITYPACKAGE = "VISIBILITYPACKAGE"
    VISIBILITYPROTECTED = "VISIBILITYPROTECTED"
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
class FormalParameter:

    pass
class DeclarationTypeAccess:

    pass
class functions_Constructor:

    pass
class functions_Method:

    pass
class ThrowTypeAccess:

    pass
class LocalVariable:

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

class Variable:

    pass
class gast_variables_CatchParameter(Variable):

    def __init__(self, rethrown: bool, Variable296: "gast_accesses_VariableAccess", variables284: "gast_accesses_DeclarationTypeAccess"):
        self.rethrown = rethrown
        
    @property
    def rethrown(self) -> bool:
        return self.__rethrown

    @rethrown.setter
    def rethrown(self, rethrown: bool):
        self.__rethrown = rethrown

class gast_variables_LocalVariable(Variable):

    pass
class gast_variables_GlobalVariable(Variable):

    pass
class gast_variables_FormalParameter(Variable):

    def __init__(self, passedByReference: bool, Function350: "Function" = None, Variable296: "gast_accesses_VariableAccess", variables284: "gast_accesses_DeclarationTypeAccess"):
        self.passedByReference = passedByReference
        self.Function350 = Function350
        
    @property
    def passedByReference(self) -> bool:
        return self.__passedByReference

    @passedByReference.setter
    def passedByReference(self, passedByReference: bool):
        self.__passedByReference = passedByReference

    @property
    def Function350(self):
        return self.__Function350

    @Function350.setter
    def Function350(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_variables_FormalParameter__Function350", None)
        self.__Function350 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "functions351"):
                opp_val = getattr(old_value, "functions351", None)
                if opp_val == self:
                    setattr(old_value, "functions351", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "functions351"):
                opp_val = getattr(value, "functions351", None)
                setattr(value, "functions351", self)

class FunctionAccess:

    pass
class gast_accesses_DelegateAccess(FunctionAccess):

    pass
class CompositeAccess:

    pass
class InheritanceTypeAccess:

    pass
class TypeAccess:

    pass
class gast_accesses_DeclarationTypeAccess(TypeAccess):

    pass
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
class gast_accesses_InheritanceTypeAccess(TypeAccess):

    def __init__(self, implementationInheritance: bool):
        self.implementationInheritance = implementationInheritance
        
    @property
    def implementationInheritance(self) -> bool:
        return self.__implementationInheritance

    @implementationInheritance.setter
    def implementationInheritance(self, implementationInheritance: bool):
        self.__implementationInheritance = implementationInheritance

class gast_accesses_ParameterInstantiationTypeAccess(TypeAccess):

    pass
class Property:

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
class gast_functions_GenericFunction(core_GenericEntity, functions_GlobalFunction):

    pass
class gast_functions_GenericConstructor(core_GenericEntity, functions_Constructor):

    pass
class gast_functions_GenericMethod(core_GenericEntity, functions_Method):

    pass
class types_TypeDecorator:

    pass
class types_Member:

    pass
class gast_functions_Destructor(types_Member, functions_Function):

    pass
class gast_types_GASTClass(types_Member, types_GASTType):

    def __init__(self, linesOfComments: int, local: bool, primitive: bool, interface: bool, anonymous: bool, inner: bool, TypeAlias210: set["TypeAlias"] = None, Function224: "Function" = None, Package227: "Package" = None, gast_types_GASTClass: set["GASTClass"] = None, GASTClass232: set["GASTClass"] = None, Delegate213: set["Delegate"] = None, Constructor: set["Constructor"] = None, Destructor: set["Destructor"] = None, Field: set["Field"] = None, Method: set["Method"] = None, gast_types_GASTClass249: set["Function"] = None, gast_types_GASTClass252: set["Property"] = None, gast_types_GASTClass254: set["Access"] = None, gast_types_GASTClass257: set["GASTClass"] = None, GASTClass235: "GASTClass" = None, gast_types_GASTClass238: set["InheritanceTypeAccess"] = None, gast_types_GASTClass240: "Field" = None, GASTClass243: set["GASTClass"] = None, GASTClass246: "GASTClass" = None):
        self.linesOfComments = linesOfComments
        self.local = local
        self.primitive = primitive
        self.interface = interface
        self.anonymous = anonymous
        self.inner = inner
        self.TypeAlias210 = TypeAlias210 if TypeAlias210 is not None else set()
        self.Function224 = Function224
        self.Package227 = Package227
        self.gast_types_GASTClass = gast_types_GASTClass if gast_types_GASTClass is not None else set()
        self.GASTClass232 = GASTClass232 if GASTClass232 is not None else set()
        self.Delegate213 = Delegate213 if Delegate213 is not None else set()
        self.Constructor = Constructor if Constructor is not None else set()
        self.Destructor = Destructor if Destructor is not None else set()
        self.Field = Field if Field is not None else set()
        self.Method = Method if Method is not None else set()
        self.gast_types_GASTClass249 = gast_types_GASTClass249 if gast_types_GASTClass249 is not None else set()
        self.gast_types_GASTClass252 = gast_types_GASTClass252 if gast_types_GASTClass252 is not None else set()
        self.gast_types_GASTClass254 = gast_types_GASTClass254 if gast_types_GASTClass254 is not None else set()
        self.gast_types_GASTClass257 = gast_types_GASTClass257 if gast_types_GASTClass257 is not None else set()
        self.GASTClass235 = GASTClass235
        self.gast_types_GASTClass238 = gast_types_GASTClass238 if gast_types_GASTClass238 is not None else set()
        self.gast_types_GASTClass240 = gast_types_GASTClass240
        self.GASTClass243 = GASTClass243 if GASTClass243 is not None else set()
        self.GASTClass246 = GASTClass246
        
    @property
    def anonymous(self) -> bool:
        return self.__anonymous

    @anonymous.setter
    def anonymous(self, anonymous: bool):
        self.__anonymous = anonymous

    @property
    def local(self) -> bool:
        return self.__local

    @local.setter
    def local(self, local: bool):
        self.__local = local

    @property
    def primitive(self) -> bool:
        return self.__primitive

    @primitive.setter
    def primitive(self, primitive: bool):
        self.__primitive = primitive

    @property
    def interface(self) -> bool:
        return self.__interface

    @interface.setter
    def interface(self, interface: bool):
        self.__interface = interface

    @property
    def inner(self) -> bool:
        return self.__inner

    @inner.setter
    def inner(self, inner: bool):
        self.__inner = inner

    @property
    def linesOfComments(self) -> int:
        return self.__linesOfComments

    @linesOfComments.setter
    def linesOfComments(self, linesOfComments: int):
        self.__linesOfComments = linesOfComments

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
                if hasattr(item, "functions222"):
                    opp_val = getattr(item, "functions222", None)
                    
                    if opp_val == self:
                        setattr(item, "functions222", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "functions222"):
                    opp_val = getattr(item, "functions222", None)
                    
                    setattr(item, "functions222", self)
                    

    @property
    def gast_types_GASTClass240(self):
        return self.__gast_types_GASTClass240

    @gast_types_GASTClass240.setter
    def gast_types_GASTClass240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__gast_types_GASTClass240", None)
        self.__gast_types_GASTClass240 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Field241"):
                opp_val = getattr(old_value, "Field241", None)
                if opp_val == self:
                    setattr(old_value, "Field241", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Field241"):
                opp_val = getattr(value, "Field241", None)
                setattr(value, "Field241", self)

    @property
    def gast_types_GASTClass257(self):
        return self.__gast_types_GASTClass257

    @gast_types_GASTClass257.setter
    def gast_types_GASTClass257(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__gast_types_GASTClass257", None)
        self.__gast_types_GASTClass257 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass258"):
                    opp_val = getattr(item, "GASTClass258", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass258", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass258"):
                    opp_val = getattr(item, "GASTClass258", None)
                    
                    setattr(item, "GASTClass258", self)
                    

    @property
    def GASTClass235(self):
        return self.__GASTClass235

    @GASTClass235.setter
    def GASTClass235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__GASTClass235", None)
        self.__GASTClass235 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types236"):
                opp_val = getattr(old_value, "types236", None)
                if opp_val == self:
                    setattr(old_value, "types236", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types236"):
                opp_val = getattr(value, "types236", None)
                setattr(value, "types236", self)

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
                if hasattr(item, "functions216"):
                    opp_val = getattr(item, "functions216", None)
                    
                    if opp_val == self:
                        setattr(item, "functions216", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "functions216"):
                    opp_val = getattr(item, "functions216", None)
                    
                    setattr(item, "functions216", self)
                    

    @property
    def gast_types_GASTClass252(self):
        return self.__gast_types_GASTClass252

    @gast_types_GASTClass252.setter
    def gast_types_GASTClass252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__gast_types_GASTClass252", None)
        self.__gast_types_GASTClass252 = value if value is not None else set()
        
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
    def gast_types_GASTClass238(self):
        return self.__gast_types_GASTClass238

    @gast_types_GASTClass238.setter
    def gast_types_GASTClass238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__gast_types_GASTClass238", None)
        self.__gast_types_GASTClass238 = value if value is not None else set()
        
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
    def Delegate213(self):
        return self.__Delegate213

    @Delegate213.setter
    def Delegate213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__Delegate213", None)
        self.__Delegate213 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "functions214"):
                    opp_val = getattr(item, "functions214", None)
                    
                    if opp_val == self:
                        setattr(item, "functions214", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "functions214"):
                    opp_val = getattr(item, "functions214", None)
                    
                    setattr(item, "functions214", self)
                    

    @property
    def GASTClass243(self):
        return self.__GASTClass243

    @GASTClass243.setter
    def GASTClass243(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__GASTClass243", None)
        self.__GASTClass243 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "types244"):
                    opp_val = getattr(item, "types244", None)
                    
                    if opp_val == self:
                        setattr(item, "types244", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types244"):
                    opp_val = getattr(item, "types244", None)
                    
                    setattr(item, "types244", self)
                    

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
                if hasattr(item, "variables220"):
                    opp_val = getattr(item, "variables220", None)
                    
                    if opp_val == self:
                        setattr(item, "variables220", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "variables220"):
                    opp_val = getattr(item, "variables220", None)
                    
                    setattr(item, "variables220", self)
                    

    @property
    def gast_types_GASTClass249(self):
        return self.__gast_types_GASTClass249

    @gast_types_GASTClass249.setter
    def gast_types_GASTClass249(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__gast_types_GASTClass249", None)
        self.__gast_types_GASTClass249 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Function250"):
                    opp_val = getattr(item, "Function250", None)
                    
                    if opp_val == self:
                        setattr(item, "Function250", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Function250"):
                    opp_val = getattr(item, "Function250", None)
                    
                    setattr(item, "Function250", self)
                    

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
                if hasattr(item, "GASTClass230"):
                    opp_val = getattr(item, "GASTClass230", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass230", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass230"):
                    opp_val = getattr(item, "GASTClass230", None)
                    
                    setattr(item, "GASTClass230", self)
                    

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
                if hasattr(item, "functions218"):
                    opp_val = getattr(item, "functions218", None)
                    
                    if opp_val == self:
                        setattr(item, "functions218", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "functions218"):
                    opp_val = getattr(item, "functions218", None)
                    
                    setattr(item, "functions218", self)
                    

    @property
    def GASTClass232(self):
        return self.__GASTClass232

    @GASTClass232.setter
    def GASTClass232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__GASTClass232", None)
        self.__GASTClass232 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "types233"):
                    opp_val = getattr(item, "types233", None)
                    
                    if opp_val == self:
                        setattr(item, "types233", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types233"):
                    opp_val = getattr(item, "types233", None)
                    
                    setattr(item, "types233", self)
                    

    @property
    def Function224(self):
        return self.__Function224

    @Function224.setter
    def Function224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__Function224", None)
        self.__Function224 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "functions225"):
                opp_val = getattr(old_value, "functions225", None)
                if opp_val == self:
                    setattr(old_value, "functions225", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "functions225"):
                opp_val = getattr(value, "functions225", None)
                setattr(value, "functions225", self)

    @property
    def gast_types_GASTClass254(self):
        return self.__gast_types_GASTClass254

    @gast_types_GASTClass254.setter
    def gast_types_GASTClass254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__gast_types_GASTClass254", None)
        self.__gast_types_GASTClass254 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Access255"):
                    opp_val = getattr(item, "Access255", None)
                    
                    if opp_val == self:
                        setattr(item, "Access255", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Access255"):
                    opp_val = getattr(item, "Access255", None)
                    
                    setattr(item, "Access255", self)
                    

    @property
    def TypeAlias210(self):
        return self.__TypeAlias210

    @TypeAlias210.setter
    def TypeAlias210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__TypeAlias210", None)
        self.__TypeAlias210 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "types211"):
                    opp_val = getattr(item, "types211", None)
                    
                    if opp_val == self:
                        setattr(item, "types211", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types211"):
                    opp_val = getattr(item, "types211", None)
                    
                    setattr(item, "types211", self)
                    

    @property
    def Package227(self):
        return self.__Package227

    @Package227.setter
    def Package227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__Package227", None)
        self.__Package227 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core228"):
                opp_val = getattr(old_value, "core228", None)
                if opp_val == self:
                    setattr(old_value, "core228", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core228"):
                opp_val = getattr(value, "core228", None)
                setattr(value, "core228", self)

    @property
    def GASTClass246(self):
        return self.__GASTClass246

    @GASTClass246.setter
    def GASTClass246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__GASTClass246", None)
        self.__GASTClass246 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types247"):
                opp_val = getattr(old_value, "types247", None)
                if opp_val == self:
                    setattr(old_value, "types247", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types247"):
                opp_val = getattr(value, "types247", None)
                setattr(value, "types247", self)

class gast_functions_Delegate(types_Member, functions_Function, types_GASTType):

    def __init__(self, innerDelegate: bool, Package311: "Package" = None, gast_functions_Delegate: "GASTClass" = None, gast_functions_Delegate305: set["Function"] = None, GASTClass308: "GASTClass" = None):
        self.innerDelegate = innerDelegate
        self.Package311 = Package311
        self.gast_functions_Delegate = gast_functions_Delegate
        self.gast_functions_Delegate305 = gast_functions_Delegate305 if gast_functions_Delegate305 is not None else set()
        self.GASTClass308 = GASTClass308
        
    @property
    def innerDelegate(self) -> bool:
        return self.__innerDelegate

    @innerDelegate.setter
    def innerDelegate(self, innerDelegate: bool):
        self.__innerDelegate = innerDelegate

    @property
    def Package311(self):
        return self.__Package311

    @Package311.setter
    def Package311(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Delegate__Package311", None)
        self.__Package311 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core312"):
                opp_val = getattr(old_value, "core312", None)
                if opp_val == self:
                    setattr(old_value, "core312", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core312"):
                opp_val = getattr(value, "core312", None)
                setattr(value, "core312", self)

    @property
    def gast_functions_Delegate305(self):
        return self.__gast_functions_Delegate305

    @gast_functions_Delegate305.setter
    def gast_functions_Delegate305(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Delegate__gast_functions_Delegate305", None)
        self.__gast_functions_Delegate305 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Function306"):
                    opp_val = getattr(item, "Function306", None)
                    
                    if opp_val == self:
                        setattr(item, "Function306", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Function306"):
                    opp_val = getattr(item, "Function306", None)
                    
                    setattr(item, "Function306", self)
                    

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
            if hasattr(old_value, "GASTClass303"):
                opp_val = getattr(old_value, "GASTClass303", None)
                if opp_val == self:
                    setattr(old_value, "GASTClass303", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTClass303"):
                opp_val = getattr(value, "GASTClass303", None)
                setattr(value, "GASTClass303", self)

    @property
    def GASTClass308(self):
        return self.__GASTClass308

    @GASTClass308.setter
    def GASTClass308(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Delegate__GASTClass308", None)
        self.__GASTClass308 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types309"):
                opp_val = getattr(old_value, "types309", None)
                if opp_val == self:
                    setattr(old_value, "types309", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types309"):
                opp_val = getattr(value, "types309", None)
                setattr(value, "types309", self)

class gast_variables_Property(types_Member, variables_Field):

    pass
class gast_variables_Field(variables_Variable, types_Member):

    def __init__(self, propertyField: bool, GASTClass358: "GASTClass" = None):
        self.propertyField = propertyField
        self.GASTClass358 = GASTClass358
        
    @property
    def propertyField(self) -> bool:
        return self.__propertyField

    @propertyField.setter
    def propertyField(self, propertyField: bool):
        self.__propertyField = propertyField

    @property
    def GASTClass358(self):
        return self.__GASTClass358

    @GASTClass358.setter
    def GASTClass358(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_variables_Field__GASTClass358", None)
        self.__GASTClass358 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types359"):
                opp_val = getattr(old_value, "types359", None)
                if opp_val == self:
                    setattr(old_value, "types359", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types359"):
                opp_val = getattr(value, "types359", None)
                setattr(value, "types359", self)

class gast_functions_Method(types_Member, functions_Function):

    def __init__(self, propertyMethod: bool, gast_functions_Method: "Property" = None, GASTClass328: "GASTClass" = None):
        self.propertyMethod = propertyMethod
        self.gast_functions_Method = gast_functions_Method
        self.GASTClass328 = GASTClass328
        
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
            if hasattr(old_value, "Property326"):
                opp_val = getattr(old_value, "Property326", None)
                if opp_val == self:
                    setattr(old_value, "Property326", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Property326"):
                opp_val = getattr(value, "Property326", None)
                setattr(value, "Property326", self)

    @property
    def GASTClass328(self):
        return self.__GASTClass328

    @GASTClass328.setter
    def GASTClass328(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Method__GASTClass328", None)
        self.__GASTClass328 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types329"):
                opp_val = getattr(old_value, "types329", None)
                if opp_val == self:
                    setattr(old_value, "types329", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types329"):
                opp_val = getattr(value, "types329", None)
                setattr(value, "types329", self)

class gast_functions_Constructor(types_Member, functions_Function):

    def __init__(self, initializer: bool, GASTClass314: "GASTClass" = None):
        self.initializer = initializer
        self.GASTClass314 = GASTClass314
        
    @property
    def initializer(self) -> bool:
        return self.__initializer

    @initializer.setter
    def initializer(self, initializer: bool):
        self.__initializer = initializer

    @property
    def GASTClass314(self):
        return self.__GASTClass314

    @GASTClass314.setter
    def GASTClass314(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Constructor__GASTClass314", None)
        self.__GASTClass314 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types315"):
                opp_val = getattr(old_value, "types315", None)
                if opp_val == self:
                    setattr(old_value, "types315", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types315"):
                opp_val = getattr(value, "types315", None)
                setattr(value, "types315", self)

class gast_types_TypeAlias(types_Member, types_TypeDecorator):

    def __init__(self, innerTypeAlias: bool, GASTClass201: "GASTClass" = None, Package204: "Package" = None, gast_types_TypeAlias: "GASTType" = None):
        self.innerTypeAlias = innerTypeAlias
        self.GASTClass201 = GASTClass201
        self.Package204 = Package204
        self.gast_types_TypeAlias = gast_types_TypeAlias
        
    @property
    def innerTypeAlias(self) -> bool:
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
            if hasattr(old_value, "GASTType199"):
                opp_val = getattr(old_value, "GASTType199", None)
                if opp_val == self:
                    setattr(old_value, "GASTType199", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTType199"):
                opp_val = getattr(value, "GASTType199", None)
                setattr(value, "GASTType199", self)

    @property
    def Package204(self):
        return self.__Package204

    @Package204.setter
    def Package204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_TypeAlias__Package204", None)
        self.__Package204 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core205"):
                opp_val = getattr(old_value, "core205", None)
                if opp_val == self:
                    setattr(old_value, "core205", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core205"):
                opp_val = getattr(value, "core205", None)
                setattr(value, "core205", self)

    @property
    def GASTClass201(self):
        return self.__GASTClass201

    @GASTClass201.setter
    def GASTClass201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_TypeAlias__GASTClass201", None)
        self.__GASTClass201 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types202"):
                opp_val = getattr(old_value, "types202", None)
                if opp_val == self:
                    setattr(old_value, "types202", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types202"):
                opp_val = getattr(value, "types202", None)
                setattr(value, "types202", self)

class Member:

    pass
class TypeDecorator:

    pass
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
            if hasattr(old_value, "GASTType190"):
                opp_val = getattr(old_value, "GASTType190", None)
                if opp_val == self:
                    setattr(old_value, "GASTType190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTType190"):
                opp_val = getattr(value, "GASTType190", None)
                setattr(value, "GASTType190", self)

class gast_annotations_ModelAnnotation(ABC):

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
            if hasattr(old_value, "GASTType197"):
                opp_val = getattr(old_value, "GASTType197", None)
                if opp_val == self:
                    setattr(old_value, "GASTType197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTType197"):
                opp_val = getattr(value, "GASTType197", None)
                setattr(value, "GASTType197", self)

class core_ModelElement:

    pass
class annotations_ModelAnnotation:

    pass
class gast_annotations_Clone(core_ModelElement, annotations_ModelAnnotation):

    pass
class gast_annotations_CloneInstance(core_ModelElement, annotations_ModelAnnotation):

    pass
class types_GASTClass:

    pass
class gast_types_GenericClass(core_GenericEntity, types_GASTClass):

    pass
class gast_annotations_Attribute(types_GASTClass, annotations_ModelAnnotation):

    pass
class core_SourceEntity:

    pass
class gast_annotations_Comment(core_SourceEntity, annotations_ModelAnnotation):

    def __init__(self, todo: bool, formal: bool, todoCount: int, texts: str):
        self.todo = todo
        self.formal = formal
        self.todoCount = todoCount
        self.texts = texts
        
    @property
    def todoCount(self) -> int:
        return self.__todoCount

    @todoCount.setter
    def todoCount(self, todoCount: int):
        self.__todoCount = todoCount

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
    def formal(self) -> bool:
        return self.__formal

    @formal.setter
    def formal(self, formal: bool):
        self.__formal = formal

    def OCLtodo(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement OCLtodo method
        pass

class core_NamedModelElement:

    pass
class gast_variables_Variable(core_SourceEntity, core_NamedModelElement):

    def __init__(self, const: bool, gast_variables_Variable: "GASTType" = None, DeclarationTypeAccess355: "DeclarationTypeAccess" = None):
        self.const = const
        self.gast_variables_Variable = gast_variables_Variable
        self.DeclarationTypeAccess355 = DeclarationTypeAccess355
        
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
            if hasattr(old_value, "GASTType353"):
                opp_val = getattr(old_value, "GASTType353", None)
                if opp_val == self:
                    setattr(old_value, "GASTType353", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTType353"):
                opp_val = getattr(value, "GASTType353", None)
                setattr(value, "GASTType353", self)

    @property
    def DeclarationTypeAccess355(self):
        return self.__DeclarationTypeAccess355

    @DeclarationTypeAccess355.setter
    def DeclarationTypeAccess355(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_variables_Variable__DeclarationTypeAccess355", None)
        self.__DeclarationTypeAccess355 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accesses356"):
                opp_val = getattr(old_value, "accesses356", None)
                if opp_val == self:
                    setattr(old_value, "accesses356", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accesses356"):
                opp_val = getattr(value, "accesses356", None)
                setattr(value, "accesses356", self)

class gast_functions_Function(core_SourceEntity, core_NamedModelElement):

    def __init__(self, numberOfStatements: int, maximumNestingLevel: int, linesOfComments: int, linesOfCode: int, numberOfEdgesInCFG: int, numberOfNodesInCFG: int, operator: bool, LocalVariable: set["LocalVariable"] = None, gast_functions_Function: set["Statement"] = None, gast_functions_Function339: set["ThrowTypeAccess"] = None, gast_functions_Function341: set["Access"] = None, DeclarationTypeAccess: "DeclarationTypeAccess" = None, FormalParameter: set["FormalParameter"] = None, BlockStatement344: "BlockStatement" = None, GASTClass347: set["GASTClass"] = None):
        self.numberOfStatements = numberOfStatements
        self.maximumNestingLevel = maximumNestingLevel
        self.linesOfComments = linesOfComments
        self.linesOfCode = linesOfCode
        self.numberOfEdgesInCFG = numberOfEdgesInCFG
        self.numberOfNodesInCFG = numberOfNodesInCFG
        self.operator = operator
        self.LocalVariable = LocalVariable if LocalVariable is not None else set()
        self.gast_functions_Function = gast_functions_Function if gast_functions_Function is not None else set()
        self.gast_functions_Function339 = gast_functions_Function339 if gast_functions_Function339 is not None else set()
        self.gast_functions_Function341 = gast_functions_Function341 if gast_functions_Function341 is not None else set()
        self.DeclarationTypeAccess = DeclarationTypeAccess
        self.FormalParameter = FormalParameter if FormalParameter is not None else set()
        self.BlockStatement344 = BlockStatement344
        self.GASTClass347 = GASTClass347 if GASTClass347 is not None else set()
        
    @property
    def numberOfNodesInCFG(self) -> int:
        return self.__numberOfNodesInCFG

    @numberOfNodesInCFG.setter
    def numberOfNodesInCFG(self, numberOfNodesInCFG: int):
        self.__numberOfNodesInCFG = numberOfNodesInCFG

    @property
    def operator(self) -> bool:
        return self.__operator

    @operator.setter
    def operator(self, operator: bool):
        self.__operator = operator

    @property
    def numberOfStatements(self) -> int:
        return self.__numberOfStatements

    @numberOfStatements.setter
    def numberOfStatements(self, numberOfStatements: int):
        self.__numberOfStatements = numberOfStatements

    @property
    def maximumNestingLevel(self) -> int:
        return self.__maximumNestingLevel

    @maximumNestingLevel.setter
    def maximumNestingLevel(self, maximumNestingLevel: int):
        self.__maximumNestingLevel = maximumNestingLevel

    @property
    def linesOfComments(self) -> int:
        return self.__linesOfComments

    @linesOfComments.setter
    def linesOfComments(self, linesOfComments: int):
        self.__linesOfComments = linesOfComments

    @property
    def numberOfEdgesInCFG(self) -> int:
        return self.__numberOfEdgesInCFG

    @numberOfEdgesInCFG.setter
    def numberOfEdgesInCFG(self, numberOfEdgesInCFG: int):
        self.__numberOfEdgesInCFG = numberOfEdgesInCFG

    @property
    def linesOfCode(self) -> int:
        return self.__linesOfCode

    @linesOfCode.setter
    def linesOfCode(self, linesOfCode: int):
        self.__linesOfCode = linesOfCode

    @property
    def GASTClass347(self):
        return self.__GASTClass347

    @GASTClass347.setter
    def GASTClass347(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Function__GASTClass347", None)
        self.__GASTClass347 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "types348"):
                    opp_val = getattr(item, "types348", None)
                    
                    if opp_val == self:
                        setattr(item, "types348", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types348"):
                    opp_val = getattr(item, "types348", None)
                    
                    setattr(item, "types348", self)
                    

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
                if hasattr(item, "Statement337"):
                    opp_val = getattr(item, "Statement337", None)
                    
                    if opp_val == self:
                        setattr(item, "Statement337", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Statement337"):
                    opp_val = getattr(item, "Statement337", None)
                    
                    setattr(item, "Statement337", self)
                    

    @property
    def gast_functions_Function339(self):
        return self.__gast_functions_Function339

    @gast_functions_Function339.setter
    def gast_functions_Function339(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Function__gast_functions_Function339", None)
        self.__gast_functions_Function339 = value if value is not None else set()
        
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
                if hasattr(item, "variables333"):
                    opp_val = getattr(item, "variables333", None)
                    
                    if opp_val == self:
                        setattr(item, "variables333", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "variables333"):
                    opp_val = getattr(item, "variables333", None)
                    
                    setattr(item, "variables333", self)
                    

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
            if hasattr(old_value, "accesses331"):
                opp_val = getattr(old_value, "accesses331", None)
                if opp_val == self:
                    setattr(old_value, "accesses331", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accesses331"):
                opp_val = getattr(value, "accesses331", None)
                setattr(value, "accesses331", self)

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
                if hasattr(item, "variables335"):
                    opp_val = getattr(item, "variables335", None)
                    
                    if opp_val == self:
                        setattr(item, "variables335", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "variables335"):
                    opp_val = getattr(item, "variables335", None)
                    
                    setattr(item, "variables335", self)
                    

    @property
    def gast_functions_Function341(self):
        return self.__gast_functions_Function341

    @gast_functions_Function341.setter
    def gast_functions_Function341(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Function__gast_functions_Function341", None)
        self.__gast_functions_Function341 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Access342"):
                    opp_val = getattr(item, "Access342", None)
                    
                    if opp_val == self:
                        setattr(item, "Access342", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Access342"):
                    opp_val = getattr(item, "Access342", None)
                    
                    setattr(item, "Access342", self)
                    

    @property
    def BlockStatement344(self):
        return self.__BlockStatement344

    @BlockStatement344.setter
    def BlockStatement344(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Function__BlockStatement344", None)
        self.__BlockStatement344 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statements345"):
                opp_val = getattr(old_value, "statements345", None)
                if opp_val == self:
                    setattr(old_value, "statements345", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statements345"):
                opp_val = getattr(value, "statements345", None)
                setattr(value, "statements345", self)

class gast_annotations_StructuralAbstraction(annotations_ModelAnnotation, core_NamedModelElement):

    pass
class gast_core_Position:

    def __init__(self, endLine: int, startLine: int, endColumn: int, startColumn: int, gast_core_Position: "File" = None, gast_core_Position169: "File" = None, SourceEntity: "SourceEntity" = None):
        self.endLine = endLine
        self.startLine = startLine
        self.endColumn = endColumn
        self.startColumn = startColumn
        self.gast_core_Position = gast_core_Position
        self.gast_core_Position169 = gast_core_Position169
        self.SourceEntity = SourceEntity
        
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
    def endLine(self) -> int:
        return self.__endLine

    @endLine.setter
    def endLine(self, endLine: int):
        self.__endLine = endLine

    @property
    def startLine(self) -> int:
        return self.__startLine

    @startLine.setter
    def startLine(self, startLine: int):
        self.__startLine = startLine

    @property
    def gast_core_Position169(self):
        return self.__gast_core_Position169

    @gast_core_Position169.setter
    def gast_core_Position169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Position__gast_core_Position169", None)
        self.__gast_core_Position169 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "File170"):
                opp_val = getattr(old_value, "File170", None)
                if opp_val == self:
                    setattr(old_value, "File170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "File170"):
                opp_val = getattr(value, "File170", None)
                setattr(value, "File170", self)

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
            if hasattr(old_value, "core172"):
                opp_val = getattr(old_value, "core172", None)
                if opp_val == self:
                    setattr(old_value, "core172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core172"):
                opp_val = getattr(value, "core172", None)
                setattr(value, "core172", self)

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
            if hasattr(old_value, "File167"):
                opp_val = getattr(old_value, "File167", None)
                if opp_val == self:
                    setattr(old_value, "File167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "File167"):
                opp_val = getattr(value, "File167", None)
                setattr(value, "File167", self)

    def EitherAssemblyFileOrSourceFileSet(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement EitherAssemblyFileOrSourceFileSet method
        pass

class Position:

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
class Package:

    pass
class gast_core_PackageAlias(Package):

    pass
class TypeParameterClass:

    pass
class TypeAlias:

    pass
class Delegate:

    pass
class Access:

    pass
class gast_accesses_VariableAccess(Access):

    def __init__(self, write: bool, gast_accesses_VariableAccess: "Variable" = None, Access91: "gast_core_Root", Access342: "gast_functions_Function", Access255: "gast_types_GASTClass", Access: "gast_core_Package"):
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
            if hasattr(old_value, "Variable296"):
                opp_val = getattr(old_value, "Variable296", None)
                if opp_val == self:
                    setattr(old_value, "Variable296", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable296"):
                opp_val = getattr(value, "Variable296", None)
                setattr(value, "Variable296", self)

class gast_accesses_TypeAccess(Access):

    pass
class gast_accesses_FunctionAccess(Access):

    pass
class GlobalVariable:

    pass
class GlobalFunction:

    pass
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
                    

class Directory:

    pass
class GASTClass:

    pass
class gast_types_GASTEnumeration(GASTClass):

    pass
class gast_types_TypeParameterClass(GASTClass):

    pass
class gast_types_GASTStruct(GASTClass):

    pass
class gast_types_GASTUnion(GASTClass):

    pass
class NamedModelElement:

    pass
class gast_core_File(NamedModelElement):

    def __init__(self, sourceFile: bool, linesOfCode: int, size: str, fullQualifiedPath: str, fileSystemPath: str, assemblyFile: bool, gast_core_File: "Root" = None, gast_core_File152: set["GlobalFunction"] = None, gast_core_File155: set["GlobalVariable"] = None, gast_core_File158: set["Package"] = None, gast_core_File161: set["File"] = None, gast_core_File140: set["GASTType"] = None, gast_core_File143: set["GASTType"] = None, gast_core_File146: set["GlobalVariable"] = None, gast_core_File149: set["GlobalFunction"] = None, Directory164: "Directory" = None):
        self.sourceFile = sourceFile
        self.linesOfCode = linesOfCode
        self.size = size
        self.fullQualifiedPath = fullQualifiedPath
        self.fileSystemPath = fileSystemPath
        self.assemblyFile = assemblyFile
        self.gast_core_File = gast_core_File
        self.gast_core_File152 = gast_core_File152 if gast_core_File152 is not None else set()
        self.gast_core_File155 = gast_core_File155 if gast_core_File155 is not None else set()
        self.gast_core_File158 = gast_core_File158 if gast_core_File158 is not None else set()
        self.gast_core_File161 = gast_core_File161 if gast_core_File161 is not None else set()
        self.gast_core_File140 = gast_core_File140 if gast_core_File140 is not None else set()
        self.gast_core_File143 = gast_core_File143 if gast_core_File143 is not None else set()
        self.gast_core_File146 = gast_core_File146 if gast_core_File146 is not None else set()
        self.gast_core_File149 = gast_core_File149 if gast_core_File149 is not None else set()
        self.Directory164 = Directory164
        
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
    def gast_core_File143(self):
        return self.__gast_core_File143

    @gast_core_File143.setter
    def gast_core_File143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File143", None)
        self.__gast_core_File143 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTType144"):
                    opp_val = getattr(item, "GASTType144", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTType144", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTType144"):
                    opp_val = getattr(item, "GASTType144", None)
                    
                    setattr(item, "GASTType144", self)
                    

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
                if hasattr(item, "Package159"):
                    opp_val = getattr(item, "Package159", None)
                    
                    if opp_val == self:
                        setattr(item, "Package159", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package159"):
                    opp_val = getattr(item, "Package159", None)
                    
                    setattr(item, "Package159", self)
                    

    @property
    def Directory164(self):
        return self.__Directory164

    @Directory164.setter
    def Directory164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__Directory164", None)
        self.__Directory164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core165"):
                opp_val = getattr(old_value, "core165", None)
                if opp_val == self:
                    setattr(old_value, "core165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core165"):
                opp_val = getattr(value, "core165", None)
                setattr(value, "core165", self)

    @property
    def gast_core_File140(self):
        return self.__gast_core_File140

    @gast_core_File140.setter
    def gast_core_File140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File140", None)
        self.__gast_core_File140 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTType141"):
                    opp_val = getattr(item, "GASTType141", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTType141", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTType141"):
                    opp_val = getattr(item, "GASTType141", None)
                    
                    setattr(item, "GASTType141", self)
                    

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
                if hasattr(item, "File162"):
                    opp_val = getattr(item, "File162", None)
                    
                    if opp_val == self:
                        setattr(item, "File162", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "File162"):
                    opp_val = getattr(item, "File162", None)
                    
                    setattr(item, "File162", self)
                    

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
                if hasattr(item, "GlobalFunction153"):
                    opp_val = getattr(item, "GlobalFunction153", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalFunction153", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalFunction153"):
                    opp_val = getattr(item, "GlobalFunction153", None)
                    
                    setattr(item, "GlobalFunction153", self)
                    

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
            if hasattr(old_value, "Root138"):
                opp_val = getattr(old_value, "Root138", None)
                if opp_val == self:
                    setattr(old_value, "Root138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Root138"):
                opp_val = getattr(value, "Root138", None)
                setattr(value, "Root138", self)

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
                if hasattr(item, "GlobalFunction150"):
                    opp_val = getattr(item, "GlobalFunction150", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalFunction150", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalFunction150"):
                    opp_val = getattr(item, "GlobalFunction150", None)
                    
                    setattr(item, "GlobalFunction150", self)
                    

    @property
    def gast_core_File146(self):
        return self.__gast_core_File146

    @gast_core_File146.setter
    def gast_core_File146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File146", None)
        self.__gast_core_File146 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalVariable147"):
                    opp_val = getattr(item, "GlobalVariable147", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalVariable147", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalVariable147"):
                    opp_val = getattr(item, "GlobalVariable147", None)
                    
                    setattr(item, "GlobalVariable147", self)
                    

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

class gast_core_Directory(NamedModelElement):

    def __init__(self, fileSystemPath: str, fullQualifiedPath: str, Directory127: set["Directory"] = None, Directory130: "Directory" = None, File: set["File"] = None, BasePath135: "BasePath" = None):
        self.fileSystemPath = fileSystemPath
        self.fullQualifiedPath = fullQualifiedPath
        self.Directory127 = Directory127 if Directory127 is not None else set()
        self.Directory130 = Directory130
        self.File = File if File is not None else set()
        self.BasePath135 = BasePath135
        
    @property
    def fileSystemPath(self) -> str:
        return self.__fileSystemPath

    @fileSystemPath.setter
    def fileSystemPath(self, fileSystemPath: str):
        self.__fileSystemPath = fileSystemPath

    @property
    def fullQualifiedPath(self) -> str:
        return self.__fullQualifiedPath

    @fullQualifiedPath.setter
    def fullQualifiedPath(self, fullQualifiedPath: str):
        self.__fullQualifiedPath = fullQualifiedPath

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
                if hasattr(item, "core133"):
                    opp_val = getattr(item, "core133", None)
                    
                    if opp_val == self:
                        setattr(item, "core133", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core133"):
                    opp_val = getattr(item, "core133", None)
                    
                    setattr(item, "core133", self)
                    

    @property
    def Directory130(self):
        return self.__Directory130

    @Directory130.setter
    def Directory130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Directory__Directory130", None)
        self.__Directory130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core131"):
                opp_val = getattr(old_value, "core131", None)
                if opp_val == self:
                    setattr(old_value, "core131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core131"):
                opp_val = getattr(value, "core131", None)
                setattr(value, "core131", self)

    @property
    def Directory127(self):
        return self.__Directory127

    @Directory127.setter
    def Directory127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Directory__Directory127", None)
        self.__Directory127 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core128"):
                    opp_val = getattr(item, "core128", None)
                    
                    if opp_val == self:
                        setattr(item, "core128", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core128"):
                    opp_val = getattr(item, "core128", None)
                    
                    setattr(item, "core128", self)
                    

    @property
    def BasePath135(self):
        return self.__BasePath135

    @BasePath135.setter
    def BasePath135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Directory__BasePath135", None)
        self.__BasePath135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core136"):
                opp_val = getattr(old_value, "core136", None)
                if opp_val == self:
                    setattr(old_value, "core136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core136"):
                opp_val = getattr(value, "core136", None)
                setattr(value, "core136", self)

class gast_core_Package(NamedModelElement):

    def __init__(self, linesOfComments: int, linesOfCode: int, qualifiedName: str, gast_core_Package: set["GASTClass"] = None, gast_core_Package59: set["GASTClass"] = None, GlobalFunction: set["GlobalFunction"] = None, GlobalVariable: set["GlobalVariable"] = None, Root75: "Root" = None, gast_core_Package62: set["GASTClass"] = None, gast_core_Package65: set["GASTClass"] = None, gast_core_Package68: set["Access"] = None, Delegate: set["Delegate"] = None, gast_core_Package85: set["Package"] = None, TypeAlias: set["TypeAlias"] = None, GASTClass78: set["GASTClass"] = None, Package: set["Package"] = None, Package82: "Package" = None):
        self.linesOfComments = linesOfComments
        self.linesOfCode = linesOfCode
        self.qualifiedName = qualifiedName
        self.gast_core_Package = gast_core_Package if gast_core_Package is not None else set()
        self.gast_core_Package59 = gast_core_Package59 if gast_core_Package59 is not None else set()
        self.GlobalFunction = GlobalFunction if GlobalFunction is not None else set()
        self.GlobalVariable = GlobalVariable if GlobalVariable is not None else set()
        self.Root75 = Root75
        self.gast_core_Package62 = gast_core_Package62 if gast_core_Package62 is not None else set()
        self.gast_core_Package65 = gast_core_Package65 if gast_core_Package65 is not None else set()
        self.gast_core_Package68 = gast_core_Package68 if gast_core_Package68 is not None else set()
        self.Delegate = Delegate if Delegate is not None else set()
        self.gast_core_Package85 = gast_core_Package85 if gast_core_Package85 is not None else set()
        self.TypeAlias = TypeAlias if TypeAlias is not None else set()
        self.GASTClass78 = GASTClass78 if GASTClass78 is not None else set()
        self.Package = Package if Package is not None else set()
        self.Package82 = Package82
        
    @property
    def qualifiedName(self) -> str:
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName

    @property
    def linesOfCode(self) -> int:
        return self.__linesOfCode

    @linesOfCode.setter
    def linesOfCode(self, linesOfCode: int):
        self.__linesOfCode = linesOfCode

    @property
    def linesOfComments(self) -> int:
        return self.__linesOfComments

    @linesOfComments.setter
    def linesOfComments(self, linesOfComments: int):
        self.__linesOfComments = linesOfComments

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
    def Package82(self):
        return self.__Package82

    @Package82.setter
    def Package82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__Package82", None)
        self.__Package82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core83"):
                opp_val = getattr(old_value, "core83", None)
                if opp_val == self:
                    setattr(old_value, "core83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core83"):
                opp_val = getattr(value, "core83", None)
                setattr(value, "core83", self)

    @property
    def GASTClass78(self):
        return self.__GASTClass78

    @GASTClass78.setter
    def GASTClass78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__GASTClass78", None)
        self.__GASTClass78 = value if value is not None else set()
        
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
                if hasattr(item, "types88"):
                    opp_val = getattr(item, "types88", None)
                    
                    if opp_val == self:
                        setattr(item, "types88", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types88"):
                    opp_val = getattr(item, "types88", None)
                    
                    setattr(item, "types88", self)
                    

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
    def gast_core_Package62(self):
        return self.__gast_core_Package62

    @gast_core_Package62.setter
    def gast_core_Package62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__gast_core_Package62", None)
        self.__gast_core_Package62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass63"):
                    opp_val = getattr(item, "GASTClass63", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass63"):
                    opp_val = getattr(item, "GASTClass63", None)
                    
                    setattr(item, "GASTClass63", self)
                    

    @property
    def gast_core_Package65(self):
        return self.__gast_core_Package65

    @gast_core_Package65.setter
    def gast_core_Package65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__gast_core_Package65", None)
        self.__gast_core_Package65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass66"):
                    opp_val = getattr(item, "GASTClass66", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass66", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass66"):
                    opp_val = getattr(item, "GASTClass66", None)
                    
                    setattr(item, "GASTClass66", self)
                    

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
                if hasattr(item, "functions72"):
                    opp_val = getattr(item, "functions72", None)
                    
                    if opp_val == self:
                        setattr(item, "functions72", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "functions72"):
                    opp_val = getattr(item, "functions72", None)
                    
                    setattr(item, "functions72", self)
                    

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
                if hasattr(item, "core80"):
                    opp_val = getattr(item, "core80", None)
                    
                    if opp_val == self:
                        setattr(item, "core80", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core80"):
                    opp_val = getattr(item, "core80", None)
                    
                    setattr(item, "core80", self)
                    

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
                if hasattr(item, "functions70"):
                    opp_val = getattr(item, "functions70", None)
                    
                    if opp_val == self:
                        setattr(item, "functions70", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "functions70"):
                    opp_val = getattr(item, "functions70", None)
                    
                    setattr(item, "functions70", self)
                    

    @property
    def gast_core_Package59(self):
        return self.__gast_core_Package59

    @gast_core_Package59.setter
    def gast_core_Package59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__gast_core_Package59", None)
        self.__gast_core_Package59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass60"):
                    opp_val = getattr(item, "GASTClass60", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass60", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass60"):
                    opp_val = getattr(item, "GASTClass60", None)
                    
                    setattr(item, "GASTClass60", self)
                    

    @property
    def Root75(self):
        return self.__Root75

    @Root75.setter
    def Root75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__Root75", None)
        self.__Root75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core76"):
                opp_val = getattr(old_value, "core76", None)
                if opp_val == self:
                    setattr(old_value, "core76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core76"):
                opp_val = getattr(value, "core76", None)
                setattr(value, "core76", self)

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
                    

class Root:

    pass
class ModelElement:

    pass
class gast_core_NamedModelElement(ModelElement):

    def __init__(self, simpleName: str, ModelElement120: "gast_core_Root", ModelElement301: "gast_accesses_Access", ModelElement: "gast_core_Root"):
        self.simpleName = simpleName
        
    @property
    def simpleName(self) -> str:
        return self.__simpleName

    @simpleName.setter
    def simpleName(self, simpleName: str):
        self.__simpleName = simpleName

class gast_core_GenericEntity(ModelElement):

    pass
class gast_core_Root(ModelElement):

    def __init__(self, linesOfComments: int, linesOfCode: int, gast_core_Root: set["Access"] = None, gast_core_Root93: set["GASTClass"] = None, gast_core_Root107: set["GlobalVariable"] = None, Package110: set["Package"] = None, Clone: set["Clone"] = None, gast_core_Root115: set["StructuralAbstraction"] = None, gast_core_Root117: set["GASTType"] = None, gast_core_Root119: set["ModelElement"] = None, BasePath: set["BasePath"] = None, gast_core_Root96: set["GASTClass"] = None, gast_core_Root99: set["GASTClass"] = None, gast_core_Root102: set["GASTClass"] = None, gast_core_Root105: set["ModelElement"] = None, GlobalFunction124: set["GlobalFunction"] = None, ModelElement120: "gast_core_Root", ModelElement301: "gast_accesses_Access", ModelElement: "gast_core_Root"):
        self.linesOfComments = linesOfComments
        self.linesOfCode = linesOfCode
        self.gast_core_Root = gast_core_Root if gast_core_Root is not None else set()
        self.gast_core_Root93 = gast_core_Root93 if gast_core_Root93 is not None else set()
        self.gast_core_Root107 = gast_core_Root107 if gast_core_Root107 is not None else set()
        self.Package110 = Package110 if Package110 is not None else set()
        self.Clone = Clone if Clone is not None else set()
        self.gast_core_Root115 = gast_core_Root115 if gast_core_Root115 is not None else set()
        self.gast_core_Root117 = gast_core_Root117 if gast_core_Root117 is not None else set()
        self.gast_core_Root119 = gast_core_Root119 if gast_core_Root119 is not None else set()
        self.BasePath = BasePath if BasePath is not None else set()
        self.gast_core_Root96 = gast_core_Root96 if gast_core_Root96 is not None else set()
        self.gast_core_Root99 = gast_core_Root99 if gast_core_Root99 is not None else set()
        self.gast_core_Root102 = gast_core_Root102 if gast_core_Root102 is not None else set()
        self.gast_core_Root105 = gast_core_Root105 if gast_core_Root105 is not None else set()
        self.GlobalFunction124 = GlobalFunction124 if GlobalFunction124 is not None else set()
        
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
                if hasattr(item, "core122"):
                    opp_val = getattr(item, "core122", None)
                    
                    if opp_val == self:
                        setattr(item, "core122", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core122"):
                    opp_val = getattr(item, "core122", None)
                    
                    setattr(item, "core122", self)
                    

    @property
    def gast_core_Root115(self):
        return self.__gast_core_Root115

    @gast_core_Root115.setter
    def gast_core_Root115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root115", None)
        self.__gast_core_Root115 = value if value is not None else set()
        
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
    def GlobalFunction124(self):
        return self.__GlobalFunction124

    @GlobalFunction124.setter
    def GlobalFunction124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__GlobalFunction124", None)
        self.__GlobalFunction124 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "functions125"):
                    opp_val = getattr(item, "functions125", None)
                    
                    if opp_val == self:
                        setattr(item, "functions125", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "functions125"):
                    opp_val = getattr(item, "functions125", None)
                    
                    setattr(item, "functions125", self)
                    

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
                if hasattr(item, "annotations113"):
                    opp_val = getattr(item, "annotations113", None)
                    
                    if opp_val == self:
                        setattr(item, "annotations113", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "annotations113"):
                    opp_val = getattr(item, "annotations113", None)
                    
                    setattr(item, "annotations113", self)
                    

    @property
    def Package110(self):
        return self.__Package110

    @Package110.setter
    def Package110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__Package110", None)
        self.__Package110 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core111"):
                    opp_val = getattr(item, "core111", None)
                    
                    if opp_val == self:
                        setattr(item, "core111", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core111"):
                    opp_val = getattr(item, "core111", None)
                    
                    setattr(item, "core111", self)
                    

    @property
    def gast_core_Root119(self):
        return self.__gast_core_Root119

    @gast_core_Root119.setter
    def gast_core_Root119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root119", None)
        self.__gast_core_Root119 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelElement120"):
                    opp_val = getattr(item, "ModelElement120", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelElement120", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelElement120"):
                    opp_val = getattr(item, "ModelElement120", None)
                    
                    setattr(item, "ModelElement120", self)
                    

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
    def gast_core_Root117(self):
        return self.__gast_core_Root117

    @gast_core_Root117.setter
    def gast_core_Root117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root117", None)
        self.__gast_core_Root117 = value if value is not None else set()
        
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
                    

    def getPackageByName(self, name: str) -> str:
        # TODO: Implement getPackageByName method
        pass

    def getPackageByQualifiedName(self, qualifiedName: str) -> str:
        # TODO: Implement getPackageByQualifiedName method
        pass

class gast_core_SourceEntity(ModelElement):

    pass
class gast_core_BasePath(ModelElement):

    def __init__(self, path: str, Root: "Root" = None, Directory: set["Directory"] = None, ModelElement120: "gast_core_Root", ModelElement301: "gast_accesses_Access", ModelElement: "gast_core_Root"):
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
                if hasattr(item, "core55"):
                    opp_val = getattr(item, "core55", None)
                    
                    if opp_val == self:
                        setattr(item, "core55", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core55"):
                    opp_val = getattr(item, "core55", None)
                    
                    setattr(item, "core55", self)
                    

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

class gast_statements_Exit:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Exit:

    pass
class gast_statements_GASTBehaviour:

    pass
class CatchParameter:

    pass
class LoopStatement:

    pass
class Branch:

    pass
class BranchStatement:

    pass
class GASTExpression:

    pass
class Function:

    pass
class gast_functions_GlobalFunction(Function):

    def __init__(self, kind: str, Root323: "Root" = None, Package320: "Package" = None, functions225: "gast_types_GASTClass", Function277: "gast_accesses_BaseAccess", Function294: "gast_accesses_FunctionAccess", functions362: "gast_variables_LocalVariable", functions282: "gast_accesses_DeclarationTypeAccess", Function286: "gast_accesses_DelegateAccess", Function306: "gast_functions_Delegate", functions351: "gast_variables_FormalParameter", functions: "gast_statements_BlockStatement", Function250: "gast_types_GASTClass"):
        self.kind = kind
        self.Root323 = Root323
        self.Package320 = Package320
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def Package320(self):
        return self.__Package320

    @Package320.setter
    def Package320(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_GlobalFunction__Package320", None)
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
    def Root323(self):
        return self.__Root323

    @Root323.setter
    def Root323(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_GlobalFunction__Root323", None)
        self.__Root323 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core324"):
                opp_val = getattr(old_value, "core324", None)
                if opp_val == self:
                    setattr(old_value, "core324", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core324"):
                opp_val = getattr(value, "core324", None)
                setattr(value, "core324", self)

class CloneInstance:

    pass
class BaseAccess:

    pass
class gast_accesses_Access(BaseAccess):

    pass
class gast_accesses_CompositeAccess(BaseAccess):

    pass
class SourceEntity:

    pass
class gast_statements_Branch(SourceEntity):

    pass
class gast_types_Member(SourceEntity):

    def __init__(self, visibility: str, abstract: bool, extern: bool, final: bool, internal: bool, introspectable: bool, override: bool, static: bool, typeParameterClassMember: bool, virtual: bool, gast_types_Member: "Member" = None, core172: "gast_core_Position"):
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
    def final(self) -> bool:
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final

    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def internal(self) -> bool:
        return self.__internal

    @internal.setter
    def internal(self, internal: bool):
        self.__internal = internal

    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def extern(self) -> bool:
        return self.__extern

    @extern.setter
    def extern(self, extern: bool):
        self.__extern = extern

    @property
    def override(self) -> bool:
        return self.__override

    @override.setter
    def override(self, override: bool):
        self.__override = override

    @property
    def introspectable(self) -> bool:
        return self.__introspectable

    @introspectable.setter
    def introspectable(self, introspectable: bool):
        self.__introspectable = introspectable

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def typeParameterClassMember(self) -> bool:
        return self.__typeParameterClassMember

    @typeParameterClassMember.setter
    def typeParameterClassMember(self, typeParameterClassMember: bool):
        self.__typeParameterClassMember = typeParameterClassMember

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

    def __init__(self, numberOfStatements: int, maximumNestingLevel: int, numberOfComments: int, linesOfCode: int, numberOfEdgesInCFG: int, numberOfNodesInCFG: int, BaseAccess: set["BaseAccess"] = None, CloneInstance: "CloneInstance" = None, BlockStatement9: "BlockStatement" = None, gast_statements_Statement: "Statement" = None, Branch: "Branch" = None, LoopStatement: "LoopStatement" = None, gast_statements_Statement16: set["Statement"] = None, gast_statements_Statement19: set["Statement"] = None, core172: "gast_core_Position"):
        self.numberOfStatements = numberOfStatements
        self.maximumNestingLevel = maximumNestingLevel
        self.numberOfComments = numberOfComments
        self.linesOfCode = linesOfCode
        self.numberOfEdgesInCFG = numberOfEdgesInCFG
        self.numberOfNodesInCFG = numberOfNodesInCFG
        self.BaseAccess = BaseAccess if BaseAccess is not None else set()
        self.CloneInstance = CloneInstance
        self.BlockStatement9 = BlockStatement9
        self.gast_statements_Statement = gast_statements_Statement
        self.Branch = Branch
        self.LoopStatement = LoopStatement
        self.gast_statements_Statement16 = gast_statements_Statement16 if gast_statements_Statement16 is not None else set()
        self.gast_statements_Statement19 = gast_statements_Statement19 if gast_statements_Statement19 is not None else set()
        
    @property
    def numberOfComments(self) -> int:
        return self.__numberOfComments

    @numberOfComments.setter
    def numberOfComments(self, numberOfComments: int):
        self.__numberOfComments = numberOfComments

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
    def numberOfNodesInCFG(self) -> int:
        return self.__numberOfNodesInCFG

    @numberOfNodesInCFG.setter
    def numberOfNodesInCFG(self, numberOfNodesInCFG: int):
        self.__numberOfNodesInCFG = numberOfNodesInCFG

    @property
    def maximumNestingLevel(self) -> int:
        return self.__maximumNestingLevel

    @maximumNestingLevel.setter
    def maximumNestingLevel(self, maximumNestingLevel: int):
        self.__maximumNestingLevel = maximumNestingLevel

    @property
    def numberOfStatements(self) -> int:
        return self.__numberOfStatements

    @numberOfStatements.setter
    def numberOfStatements(self, numberOfStatements: int):
        self.__numberOfStatements = numberOfStatements

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
                    

class BlockStatement:

    pass
class gast_statements_Methods(BlockStatement):

    def __init__(self, methodName: str, gast_statements_Methods: "Exit" = None, statements345: "gast_functions_Function", statements: "gast_statements_Statement", BlockStatement51: "gast_statements_GASTBehaviour", BlockStatement5: "gast_statements_ExceptionHandler", BlockStatement: "gast_statements_ExceptionHandler"):
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

class gast_statements_CatchBlock(BlockStatement):

    pass
class CatchBlock:

    pass
class Statement:

    pass
class gast_statements_JumpStatement(Statement):

    def __init__(self, kind: str, gast_statements_JumpStatement: "GASTExpression" = None, statements44: "gast_statements_LoopStatement", Statement17: "gast_statements_Statement", statements30: "gast_statements_Branch", Statement20: "gast_statements_Statement", Statement: "gast_statements_Statement", Statement337: "gast_functions_Function", Statement271: "gast_accesses_BaseAccess", statements269: "gast_accesses_BaseAccess", statements185: "gast_annotations_CloneInstance", statements23: "gast_statements_BlockStatement"):
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

class gast_statements_SimpleStatement(Statement):

    pass
class gast_statements_LoopStatement(Statement):

    def __init__(self, kind: str, gast_statements_LoopStatement: "GASTExpression" = None, gast_statements_LoopStatement37: "GASTExpression" = None, gast_statements_LoopStatement40: "GASTExpression" = None, Statement43: "Statement" = None, statements44: "gast_statements_LoopStatement", Statement17: "gast_statements_Statement", statements30: "gast_statements_Branch", Statement20: "gast_statements_Statement", Statement: "gast_statements_Statement", Statement337: "gast_functions_Function", Statement271: "gast_accesses_BaseAccess", statements269: "gast_accesses_BaseAccess", statements185: "gast_annotations_CloneInstance", statements23: "gast_statements_BlockStatement"):
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

class gast_statements_BranchStatement(Statement):

    pass
class gast_statements_BlockStatement(Statement):

    def __init__(self, synchronized: bool, Statement22: set["Statement"] = None, Function: "Function" = None, statements44: "gast_statements_LoopStatement", Statement17: "gast_statements_Statement", statements30: "gast_statements_Branch", Statement20: "gast_statements_Statement", Statement: "gast_statements_Statement", Statement337: "gast_functions_Function", Statement271: "gast_accesses_BaseAccess", statements269: "gast_accesses_BaseAccess", statements185: "gast_annotations_CloneInstance", statements23: "gast_statements_BlockStatement"):
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