from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Visibilities(Enum):
    VISIBILITYPUBLIC = "VISIBILITYPUBLIC"
    VISIBILITYPACKAGE = "VISIBILITYPACKAGE"
    VISIBILITYPROTECTED = "VISIBILITYPROTECTED"
    VISIBILITYPRIVAT = "VISIBILITYPRIVAT"
    VISIBILITYSTRICTPROTECTED = "VISIBILITYSTRICTPROTECTED"
class GlobalFunctionKind(Enum):
    NORMAL = "NORMAL"
    UNITINITIALIZER = "UNITINITIALIZER"
    UNITFINALIZER = "UNITFINALIZER"
class JumpStatementKind(Enum):
    JUMP = "JUMP"
    RETURN = "RETURN"
    THROW = "THROW"
class LoopStatementKind(Enum):
    FOREACH = "FOREACH"
    WHILE = "WHILE"
    DOWHILE = "DOWHILE"
    FOR = "FOR"
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
class DeclarationTypeAccess:

    pass
class functions_Constructor:

    pass
class functions_Method:

    pass
class LocalVariable:

    pass
class FormalParameter:

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
class gast_variables_LocalVariable(Variable):

    pass
class gast_variables_CatchParameter(Variable):

    def __init__(self, rethrown: bool, variables277: "gast_accesses_DeclarationTypeAccess", Variable289: "gast_accesses_VariableAccess"):
        self.rethrown = rethrown
        
    @property
    def rethrown(self) -> bool:
        return self.__rethrown

    @rethrown.setter
    def rethrown(self, rethrown: bool):
        self.__rethrown = rethrown

class gast_variables_GlobalVariable(Variable):

    pass
class gast_variables_FormalParameter(Variable):

    def __init__(self, passedByReference: bool, Function343: "Function" = None, variables277: "gast_accesses_DeclarationTypeAccess", Variable289: "gast_accesses_VariableAccess"):
        self.passedByReference = passedByReference
        self.Function343 = Function343
        
    @property
    def passedByReference(self) -> bool:
        return self.__passedByReference

    @passedByReference.setter
    def passedByReference(self, passedByReference: bool):
        self.__passedByReference = passedByReference

    @property
    def Function343(self):
        return self.__Function343

    @Function343.setter
    def Function343(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_variables_FormalParameter__Function343", None)
        self.__Function343 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "functions344"):
                opp_val = getattr(old_value, "functions344", None)
                if opp_val == self:
                    setattr(old_value, "functions344", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "functions344"):
                opp_val = getattr(value, "functions344", None)
                setattr(value, "functions344", self)

class CompositeAccess:

    pass
class FunctionAccess:

    pass
class gast_accesses_DelegateAccess(FunctionAccess):

    pass
class TypeAccess:

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

class gast_accesses_DeclarationTypeAccess(TypeAccess):

    pass
class gast_accesses_RunTimeTypeAccess(TypeAccess):

    pass
class gast_accesses_StaticTypeAccess(TypeAccess):

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
class gast_accesses_CastTypeAccess(TypeAccess):

    pass
class InheritanceTypeAccess:

    pass
class Constructor:

    pass
class types_GASTType:

    pass
class core_GenericEntity:

    pass
class gast_functions_GenericMethod(functions_Method, core_GenericEntity):

    pass
class gast_functions_GenericFunction(functions_GlobalFunction, core_GenericEntity):

    pass
class gast_functions_GenericConstructor(functions_Constructor, core_GenericEntity):

    pass
class Method:

    pass
class Field:

    pass
class Destructor:

    pass
class types_TypeDecorator:

    pass
class types_Member:

    pass
class gast_variables_Field(variables_Variable, types_Member):

    def __init__(self, propertyField: bool, GASTClass351: "GASTClass" = None):
        self.propertyField = propertyField
        self.GASTClass351 = GASTClass351
        
    @property
    def propertyField(self) -> bool:
        return self.__propertyField

    @propertyField.setter
    def propertyField(self, propertyField: bool):
        self.__propertyField = propertyField

    @property
    def GASTClass351(self):
        return self.__GASTClass351

    @GASTClass351.setter
    def GASTClass351(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_variables_Field__GASTClass351", None)
        self.__GASTClass351 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types352"):
                opp_val = getattr(old_value, "types352", None)
                if opp_val == self:
                    setattr(old_value, "types352", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types352"):
                opp_val = getattr(value, "types352", None)
                setattr(value, "types352", self)

class gast_functions_Constructor(functions_Function, types_Member):

    def __init__(self, initializer: bool, GASTClass307: "GASTClass" = None):
        self.initializer = initializer
        self.GASTClass307 = GASTClass307
        
    @property
    def initializer(self) -> bool:
        return self.__initializer

    @initializer.setter
    def initializer(self, initializer: bool):
        self.__initializer = initializer

    @property
    def GASTClass307(self):
        return self.__GASTClass307

    @GASTClass307.setter
    def GASTClass307(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Constructor__GASTClass307", None)
        self.__GASTClass307 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types308"):
                opp_val = getattr(old_value, "types308", None)
                if opp_val == self:
                    setattr(old_value, "types308", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types308"):
                opp_val = getattr(value, "types308", None)
                setattr(value, "types308", self)

class gast_types_GASTClass(types_Member, types_GASTType):

    def __init__(self, linesOfComments: int, local: bool, primitive: bool, interface: bool, anonymous: bool, inner: bool, Destructor: set["Destructor"] = None, Field: set["Field"] = None, Method: set["Method"] = None, TypeAlias203: set["TypeAlias"] = None, Delegate206: set["Delegate"] = None, Constructor: set["Constructor"] = None, gast_types_GASTClass231: set["InheritanceTypeAccess"] = None, gast_types_GASTClass233: "Field" = None, GASTClass236: set["GASTClass"] = None, Function217: "Function" = None, Package220: "Package" = None, gast_types_GASTClass: set["GASTClass"] = None, GASTClass225: set["GASTClass"] = None, GASTClass228: "GASTClass" = None, GASTClass239: "GASTClass" = None, gast_types_GASTClass242: set["Function"] = None, gast_types_GASTClass245: set["Property"] = None, gast_types_GASTClass247: set["Access"] = None, gast_types_GASTClass250: set["GASTClass"] = None):
        self.linesOfComments = linesOfComments
        self.local = local
        self.primitive = primitive
        self.interface = interface
        self.anonymous = anonymous
        self.inner = inner
        self.Destructor = Destructor if Destructor is not None else set()
        self.Field = Field if Field is not None else set()
        self.Method = Method if Method is not None else set()
        self.TypeAlias203 = TypeAlias203 if TypeAlias203 is not None else set()
        self.Delegate206 = Delegate206 if Delegate206 is not None else set()
        self.Constructor = Constructor if Constructor is not None else set()
        self.gast_types_GASTClass231 = gast_types_GASTClass231 if gast_types_GASTClass231 is not None else set()
        self.gast_types_GASTClass233 = gast_types_GASTClass233
        self.GASTClass236 = GASTClass236 if GASTClass236 is not None else set()
        self.Function217 = Function217
        self.Package220 = Package220
        self.gast_types_GASTClass = gast_types_GASTClass if gast_types_GASTClass is not None else set()
        self.GASTClass225 = GASTClass225 if GASTClass225 is not None else set()
        self.GASTClass228 = GASTClass228
        self.GASTClass239 = GASTClass239
        self.gast_types_GASTClass242 = gast_types_GASTClass242 if gast_types_GASTClass242 is not None else set()
        self.gast_types_GASTClass245 = gast_types_GASTClass245 if gast_types_GASTClass245 is not None else set()
        self.gast_types_GASTClass247 = gast_types_GASTClass247 if gast_types_GASTClass247 is not None else set()
        self.gast_types_GASTClass250 = gast_types_GASTClass250 if gast_types_GASTClass250 is not None else set()
        
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
    def linesOfComments(self) -> int:
        return self.__linesOfComments

    @linesOfComments.setter
    def linesOfComments(self, linesOfComments: int):
        self.__linesOfComments = linesOfComments

    @property
    def primitive(self) -> bool:
        return self.__primitive

    @primitive.setter
    def primitive(self, primitive: bool):
        self.__primitive = primitive

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
                if hasattr(item, "variables213"):
                    opp_val = getattr(item, "variables213", None)
                    
                    if opp_val == self:
                        setattr(item, "variables213", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "variables213"):
                    opp_val = getattr(item, "variables213", None)
                    
                    setattr(item, "variables213", self)
                    

    @property
    def Delegate206(self):
        return self.__Delegate206

    @Delegate206.setter
    def Delegate206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__Delegate206", None)
        self.__Delegate206 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "functions207"):
                    opp_val = getattr(item, "functions207", None)
                    
                    if opp_val == self:
                        setattr(item, "functions207", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "functions207"):
                    opp_val = getattr(item, "functions207", None)
                    
                    setattr(item, "functions207", self)
                    

    @property
    def TypeAlias203(self):
        return self.__TypeAlias203

    @TypeAlias203.setter
    def TypeAlias203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__TypeAlias203", None)
        self.__TypeAlias203 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "types204"):
                    opp_val = getattr(item, "types204", None)
                    
                    if opp_val == self:
                        setattr(item, "types204", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types204"):
                    opp_val = getattr(item, "types204", None)
                    
                    setattr(item, "types204", self)
                    

    @property
    def GASTClass228(self):
        return self.__GASTClass228

    @GASTClass228.setter
    def GASTClass228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__GASTClass228", None)
        self.__GASTClass228 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types229"):
                opp_val = getattr(old_value, "types229", None)
                if opp_val == self:
                    setattr(old_value, "types229", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types229"):
                opp_val = getattr(value, "types229", None)
                setattr(value, "types229", self)

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
                if hasattr(item, "Access248"):
                    opp_val = getattr(item, "Access248", None)
                    
                    if opp_val == self:
                        setattr(item, "Access248", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Access248"):
                    opp_val = getattr(item, "Access248", None)
                    
                    setattr(item, "Access248", self)
                    

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
                if hasattr(item, "functions209"):
                    opp_val = getattr(item, "functions209", None)
                    
                    if opp_val == self:
                        setattr(item, "functions209", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "functions209"):
                    opp_val = getattr(item, "functions209", None)
                    
                    setattr(item, "functions209", self)
                    

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
                if hasattr(item, "functions215"):
                    opp_val = getattr(item, "functions215", None)
                    
                    if opp_val == self:
                        setattr(item, "functions215", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "functions215"):
                    opp_val = getattr(item, "functions215", None)
                    
                    setattr(item, "functions215", self)
                    

    @property
    def gast_types_GASTClass231(self):
        return self.__gast_types_GASTClass231

    @gast_types_GASTClass231.setter
    def gast_types_GASTClass231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__gast_types_GASTClass231", None)
        self.__gast_types_GASTClass231 = value if value is not None else set()
        
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
    def gast_types_GASTClass250(self):
        return self.__gast_types_GASTClass250

    @gast_types_GASTClass250.setter
    def gast_types_GASTClass250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__gast_types_GASTClass250", None)
        self.__gast_types_GASTClass250 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass251"):
                    opp_val = getattr(item, "GASTClass251", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass251", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass251"):
                    opp_val = getattr(item, "GASTClass251", None)
                    
                    setattr(item, "GASTClass251", self)
                    

    @property
    def gast_types_GASTClass245(self):
        return self.__gast_types_GASTClass245

    @gast_types_GASTClass245.setter
    def gast_types_GASTClass245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__gast_types_GASTClass245", None)
        self.__gast_types_GASTClass245 = value if value is not None else set()
        
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
                if hasattr(item, "functions211"):
                    opp_val = getattr(item, "functions211", None)
                    
                    if opp_val == self:
                        setattr(item, "functions211", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "functions211"):
                    opp_val = getattr(item, "functions211", None)
                    
                    setattr(item, "functions211", self)
                    

    @property
    def Function217(self):
        return self.__Function217

    @Function217.setter
    def Function217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__Function217", None)
        self.__Function217 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "functions218"):
                opp_val = getattr(old_value, "functions218", None)
                if opp_val == self:
                    setattr(old_value, "functions218", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "functions218"):
                opp_val = getattr(value, "functions218", None)
                setattr(value, "functions218", self)

    @property
    def GASTClass225(self):
        return self.__GASTClass225

    @GASTClass225.setter
    def GASTClass225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__GASTClass225", None)
        self.__GASTClass225 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "types226"):
                    opp_val = getattr(item, "types226", None)
                    
                    if opp_val == self:
                        setattr(item, "types226", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types226"):
                    opp_val = getattr(item, "types226", None)
                    
                    setattr(item, "types226", self)
                    

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
                if hasattr(item, "GASTClass223"):
                    opp_val = getattr(item, "GASTClass223", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass223", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass223"):
                    opp_val = getattr(item, "GASTClass223", None)
                    
                    setattr(item, "GASTClass223", self)
                    

    @property
    def Package220(self):
        return self.__Package220

    @Package220.setter
    def Package220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__Package220", None)
        self.__Package220 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core221"):
                opp_val = getattr(old_value, "core221", None)
                if opp_val == self:
                    setattr(old_value, "core221", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core221"):
                opp_val = getattr(value, "core221", None)
                setattr(value, "core221", self)

    @property
    def GASTClass239(self):
        return self.__GASTClass239

    @GASTClass239.setter
    def GASTClass239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__GASTClass239", None)
        self.__GASTClass239 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types240"):
                opp_val = getattr(old_value, "types240", None)
                if opp_val == self:
                    setattr(old_value, "types240", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types240"):
                opp_val = getattr(value, "types240", None)
                setattr(value, "types240", self)

    @property
    def gast_types_GASTClass242(self):
        return self.__gast_types_GASTClass242

    @gast_types_GASTClass242.setter
    def gast_types_GASTClass242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__gast_types_GASTClass242", None)
        self.__gast_types_GASTClass242 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Function243"):
                    opp_val = getattr(item, "Function243", None)
                    
                    if opp_val == self:
                        setattr(item, "Function243", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Function243"):
                    opp_val = getattr(item, "Function243", None)
                    
                    setattr(item, "Function243", self)
                    

    @property
    def GASTClass236(self):
        return self.__GASTClass236

    @GASTClass236.setter
    def GASTClass236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__GASTClass236", None)
        self.__GASTClass236 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "types237"):
                    opp_val = getattr(item, "types237", None)
                    
                    if opp_val == self:
                        setattr(item, "types237", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types237"):
                    opp_val = getattr(item, "types237", None)
                    
                    setattr(item, "types237", self)
                    

    @property
    def gast_types_GASTClass233(self):
        return self.__gast_types_GASTClass233

    @gast_types_GASTClass233.setter
    def gast_types_GASTClass233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_GASTClass__gast_types_GASTClass233", None)
        self.__gast_types_GASTClass233 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Field234"):
                opp_val = getattr(old_value, "Field234", None)
                if opp_val == self:
                    setattr(old_value, "Field234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Field234"):
                opp_val = getattr(value, "Field234", None)
                setattr(value, "Field234", self)

class gast_functions_Destructor(functions_Function, types_Member):

    pass
class gast_functions_Method(functions_Function, types_Member):

    def __init__(self, propertyMethod: bool, gast_functions_Method: "Property" = None, GASTClass321: "GASTClass" = None):
        self.propertyMethod = propertyMethod
        self.gast_functions_Method = gast_functions_Method
        self.GASTClass321 = GASTClass321
        
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
            if hasattr(old_value, "Property319"):
                opp_val = getattr(old_value, "Property319", None)
                if opp_val == self:
                    setattr(old_value, "Property319", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Property319"):
                opp_val = getattr(value, "Property319", None)
                setattr(value, "Property319", self)

    @property
    def GASTClass321(self):
        return self.__GASTClass321

    @GASTClass321.setter
    def GASTClass321(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Method__GASTClass321", None)
        self.__GASTClass321 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types322"):
                opp_val = getattr(old_value, "types322", None)
                if opp_val == self:
                    setattr(old_value, "types322", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types322"):
                opp_val = getattr(value, "types322", None)
                setattr(value, "types322", self)

class gast_functions_Delegate(functions_Function, types_Member, types_GASTType):

    def __init__(self, innerDelegate: bool, gast_functions_Delegate: "GASTClass" = None, gast_functions_Delegate298: set["Function"] = None, GASTClass301: "GASTClass" = None, Package304: "Package" = None):
        self.innerDelegate = innerDelegate
        self.gast_functions_Delegate = gast_functions_Delegate
        self.gast_functions_Delegate298 = gast_functions_Delegate298 if gast_functions_Delegate298 is not None else set()
        self.GASTClass301 = GASTClass301
        self.Package304 = Package304
        
    @property
    def innerDelegate(self) -> bool:
        return self.__innerDelegate

    @innerDelegate.setter
    def innerDelegate(self, innerDelegate: bool):
        self.__innerDelegate = innerDelegate

    @property
    def Package304(self):
        return self.__Package304

    @Package304.setter
    def Package304(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Delegate__Package304", None)
        self.__Package304 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core305"):
                opp_val = getattr(old_value, "core305", None)
                if opp_val == self:
                    setattr(old_value, "core305", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core305"):
                opp_val = getattr(value, "core305", None)
                setattr(value, "core305", self)

    @property
    def gast_functions_Delegate298(self):
        return self.__gast_functions_Delegate298

    @gast_functions_Delegate298.setter
    def gast_functions_Delegate298(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Delegate__gast_functions_Delegate298", None)
        self.__gast_functions_Delegate298 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Function299"):
                    opp_val = getattr(item, "Function299", None)
                    
                    if opp_val == self:
                        setattr(item, "Function299", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Function299"):
                    opp_val = getattr(item, "Function299", None)
                    
                    setattr(item, "Function299", self)
                    

    @property
    def GASTClass301(self):
        return self.__GASTClass301

    @GASTClass301.setter
    def GASTClass301(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Delegate__GASTClass301", None)
        self.__GASTClass301 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types302"):
                opp_val = getattr(old_value, "types302", None)
                if opp_val == self:
                    setattr(old_value, "types302", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types302"):
                opp_val = getattr(value, "types302", None)
                setattr(value, "types302", self)

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
            if hasattr(old_value, "GASTClass296"):
                opp_val = getattr(old_value, "GASTClass296", None)
                if opp_val == self:
                    setattr(old_value, "GASTClass296", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTClass296"):
                opp_val = getattr(value, "GASTClass296", None)
                setattr(value, "GASTClass296", self)

class gast_variables_Property(types_Member, variables_Field):

    pass
class gast_types_TypeAlias(types_Member, types_TypeDecorator):

    def __init__(self, innerTypeAlias: bool, Package197: "Package" = None, gast_types_TypeAlias: "GASTType" = None, GASTClass194: "GASTClass" = None):
        self.innerTypeAlias = innerTypeAlias
        self.Package197 = Package197
        self.gast_types_TypeAlias = gast_types_TypeAlias
        self.GASTClass194 = GASTClass194
        
    @property
    def innerTypeAlias(self) -> bool:
        return self.__innerTypeAlias

    @innerTypeAlias.setter
    def innerTypeAlias(self, innerTypeAlias: bool):
        self.__innerTypeAlias = innerTypeAlias

    @property
    def Package197(self):
        return self.__Package197

    @Package197.setter
    def Package197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_TypeAlias__Package197", None)
        self.__Package197 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core198"):
                opp_val = getattr(old_value, "core198", None)
                if opp_val == self:
                    setattr(old_value, "core198", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core198"):
                opp_val = getattr(value, "core198", None)
                setattr(value, "core198", self)

    @property
    def GASTClass194(self):
        return self.__GASTClass194

    @GASTClass194.setter
    def GASTClass194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_types_TypeAlias__GASTClass194", None)
        self.__GASTClass194 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types195"):
                opp_val = getattr(old_value, "types195", None)
                if opp_val == self:
                    setattr(old_value, "types195", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types195"):
                opp_val = getattr(value, "types195", None)
                setattr(value, "types195", self)

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
            if hasattr(old_value, "GASTType192"):
                opp_val = getattr(old_value, "GASTType192", None)
                if opp_val == self:
                    setattr(old_value, "GASTType192", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTType192"):
                opp_val = getattr(value, "GASTType192", None)
                setattr(value, "GASTType192", self)

class Member:

    pass
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
            if hasattr(old_value, "GASTType190"):
                opp_val = getattr(old_value, "GASTType190", None)
                if opp_val == self:
                    setattr(old_value, "GASTType190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTType190"):
                opp_val = getattr(value, "GASTType190", None)
                setattr(value, "GASTType190", self)

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
            if hasattr(old_value, "GASTType183"):
                opp_val = getattr(old_value, "GASTType183", None)
                if opp_val == self:
                    setattr(old_value, "GASTType183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTType183"):
                opp_val = getattr(value, "GASTType183", None)
                setattr(value, "GASTType183", self)

class gast_annotations_ModelAnnotation(ABC):

    pass
class core_ModelElement:

    pass
class annotations_ModelAnnotation:

    pass
class gast_annotations_CloneInstance(core_ModelElement, annotations_ModelAnnotation):

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
class core_SourceEntity:

    pass
class gast_annotations_Comment(core_SourceEntity, annotations_ModelAnnotation):

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
    def todoCount(self) -> int:
        return self.__todoCount

    @todoCount.setter
    def todoCount(self, todoCount: int):
        self.__todoCount = todoCount

    @property
    def todo(self) -> bool:
        return self.__todo

    @todo.setter
    def todo(self, todo: bool):
        self.__todo = todo

    @property
    def texts(self) -> str:
        return self.__texts

    @texts.setter
    def texts(self, texts: str):
        self.__texts = texts

    def OCLtodo(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement OCLtodo method
        pass

class core_NamedModelElement:

    pass
class gast_functions_Function(core_SourceEntity, core_NamedModelElement):

    def __init__(self, maximumNestingLevel: int, linesOfComments: int, linesOfCode: int, numberOfEdgesInCFG: int, numberOfStatements: int, numberOfNodesInCFG: int, operator: bool, FormalParameter: set["FormalParameter"] = None, LocalVariable: set["LocalVariable"] = None, DeclarationTypeAccess: "DeclarationTypeAccess" = None, gast_functions_Function: set["Statement"] = None, gast_functions_Function332: set["ThrowTypeAccess"] = None, gast_functions_Function334: set["Access"] = None, BlockStatement337: "BlockStatement" = None, GASTClass340: set["GASTClass"] = None):
        self.maximumNestingLevel = maximumNestingLevel
        self.linesOfComments = linesOfComments
        self.linesOfCode = linesOfCode
        self.numberOfEdgesInCFG = numberOfEdgesInCFG
        self.numberOfStatements = numberOfStatements
        self.numberOfNodesInCFG = numberOfNodesInCFG
        self.operator = operator
        self.FormalParameter = FormalParameter if FormalParameter is not None else set()
        self.LocalVariable = LocalVariable if LocalVariable is not None else set()
        self.DeclarationTypeAccess = DeclarationTypeAccess
        self.gast_functions_Function = gast_functions_Function if gast_functions_Function is not None else set()
        self.gast_functions_Function332 = gast_functions_Function332 if gast_functions_Function332 is not None else set()
        self.gast_functions_Function334 = gast_functions_Function334 if gast_functions_Function334 is not None else set()
        self.BlockStatement337 = BlockStatement337
        self.GASTClass340 = GASTClass340 if GASTClass340 is not None else set()
        
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
    def operator(self) -> bool:
        return self.__operator

    @operator.setter
    def operator(self, operator: bool):
        self.__operator = operator

    @property
    def linesOfComments(self) -> int:
        return self.__linesOfComments

    @linesOfComments.setter
    def linesOfComments(self, linesOfComments: int):
        self.__linesOfComments = linesOfComments

    @property
    def numberOfStatements(self) -> int:
        return self.__numberOfStatements

    @numberOfStatements.setter
    def numberOfStatements(self, numberOfStatements: int):
        self.__numberOfStatements = numberOfStatements

    @property
    def numberOfNodesInCFG(self) -> int:
        return self.__numberOfNodesInCFG

    @numberOfNodesInCFG.setter
    def numberOfNodesInCFG(self, numberOfNodesInCFG: int):
        self.__numberOfNodesInCFG = numberOfNodesInCFG

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
                if hasattr(item, "variables326"):
                    opp_val = getattr(item, "variables326", None)
                    
                    if opp_val == self:
                        setattr(item, "variables326", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "variables326"):
                    opp_val = getattr(item, "variables326", None)
                    
                    setattr(item, "variables326", self)
                    

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
            if hasattr(old_value, "accesses324"):
                opp_val = getattr(old_value, "accesses324", None)
                if opp_val == self:
                    setattr(old_value, "accesses324", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accesses324"):
                opp_val = getattr(value, "accesses324", None)
                setattr(value, "accesses324", self)

    @property
    def gast_functions_Function334(self):
        return self.__gast_functions_Function334

    @gast_functions_Function334.setter
    def gast_functions_Function334(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Function__gast_functions_Function334", None)
        self.__gast_functions_Function334 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Access335"):
                    opp_val = getattr(item, "Access335", None)
                    
                    if opp_val == self:
                        setattr(item, "Access335", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Access335"):
                    opp_val = getattr(item, "Access335", None)
                    
                    setattr(item, "Access335", self)
                    

    @property
    def gast_functions_Function332(self):
        return self.__gast_functions_Function332

    @gast_functions_Function332.setter
    def gast_functions_Function332(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Function__gast_functions_Function332", None)
        self.__gast_functions_Function332 = value if value is not None else set()
        
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
    def GASTClass340(self):
        return self.__GASTClass340

    @GASTClass340.setter
    def GASTClass340(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Function__GASTClass340", None)
        self.__GASTClass340 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "types341"):
                    opp_val = getattr(item, "types341", None)
                    
                    if opp_val == self:
                        setattr(item, "types341", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types341"):
                    opp_val = getattr(item, "types341", None)
                    
                    setattr(item, "types341", self)
                    

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
                if hasattr(item, "variables328"):
                    opp_val = getattr(item, "variables328", None)
                    
                    if opp_val == self:
                        setattr(item, "variables328", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "variables328"):
                    opp_val = getattr(item, "variables328", None)
                    
                    setattr(item, "variables328", self)
                    

    @property
    def BlockStatement337(self):
        return self.__BlockStatement337

    @BlockStatement337.setter
    def BlockStatement337(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_Function__BlockStatement337", None)
        self.__BlockStatement337 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statements338"):
                opp_val = getattr(old_value, "statements338", None)
                if opp_val == self:
                    setattr(old_value, "statements338", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statements338"):
                opp_val = getattr(value, "statements338", None)
                setattr(value, "statements338", self)

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
                if hasattr(item, "Statement330"):
                    opp_val = getattr(item, "Statement330", None)
                    
                    if opp_val == self:
                        setattr(item, "Statement330", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Statement330"):
                    opp_val = getattr(item, "Statement330", None)
                    
                    setattr(item, "Statement330", self)
                    

class gast_variables_Variable(core_SourceEntity, core_NamedModelElement):

    def __init__(self, const: bool, gast_variables_Variable: "GASTType" = None, DeclarationTypeAccess348: "DeclarationTypeAccess" = None):
        self.const = const
        self.gast_variables_Variable = gast_variables_Variable
        self.DeclarationTypeAccess348 = DeclarationTypeAccess348
        
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
            if hasattr(old_value, "GASTType346"):
                opp_val = getattr(old_value, "GASTType346", None)
                if opp_val == self:
                    setattr(old_value, "GASTType346", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTType346"):
                opp_val = getattr(value, "GASTType346", None)
                setattr(value, "GASTType346", self)

    @property
    def DeclarationTypeAccess348(self):
        return self.__DeclarationTypeAccess348

    @DeclarationTypeAccess348.setter
    def DeclarationTypeAccess348(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_variables_Variable__DeclarationTypeAccess348", None)
        self.__DeclarationTypeAccess348 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accesses349"):
                opp_val = getattr(old_value, "accesses349", None)
                if opp_val == self:
                    setattr(old_value, "accesses349", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accesses349"):
                opp_val = getattr(value, "accesses349", None)
                setattr(value, "accesses349", self)

class gast_annotations_StructuralAbstraction(core_NamedModelElement, annotations_ModelAnnotation):

    pass
class gast_core_Position:

    def __init__(self, endColumn: int, startColumn: int, endLine: int, startLine: int, gast_core_Position: "File" = None, gast_core_Position162: "File" = None, SourceEntity: "SourceEntity" = None):
        self.endColumn = endColumn
        self.startColumn = startColumn
        self.endLine = endLine
        self.startLine = startLine
        self.gast_core_Position = gast_core_Position
        self.gast_core_Position162 = gast_core_Position162
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
    def gast_core_Position(self):
        return self.__gast_core_Position

    @gast_core_Position.setter
    def gast_core_Position(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Position__gast_core_Position", None)
        self.__gast_core_Position = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "File160"):
                opp_val = getattr(old_value, "File160", None)
                if opp_val == self:
                    setattr(old_value, "File160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "File160"):
                opp_val = getattr(value, "File160", None)
                setattr(value, "File160", self)

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
    def gast_core_Position162(self):
        return self.__gast_core_Position162

    @gast_core_Position162.setter
    def gast_core_Position162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Position__gast_core_Position162", None)
        self.__gast_core_Position162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "File163"):
                opp_val = getattr(old_value, "File163", None)
                if opp_val == self:
                    setattr(old_value, "File163", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "File163"):
                opp_val = getattr(value, "File163", None)
                setattr(value, "File163", self)

    def EitherAssemblyFileOrSourceFileSet(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement EitherAssemblyFileOrSourceFileSet method
        pass

class BasePath:

    pass
class GASTType:

    pass
class gast_types_TypeDecorator(GASTType):

    pass
class File:

    pass
class StructuralAbstraction:

    pass
class gast_annotations_Subsystem(StructuralAbstraction):

    pass
class gast_annotations_Layer(StructuralAbstraction):

    pass
class Clone:

    pass
class TypeAlias:

    pass
class Package:

    pass
class gast_core_PackageAlias(Package):

    pass
class GlobalVariable:

    pass
class TypeParameterClass:

    pass
class GASTClass:

    pass
class gast_types_GASTStruct(GASTClass):

    pass
class gast_types_GASTEnumeration(GASTClass):

    pass
class gast_types_GASTUnion(GASTClass):

    pass
class gast_types_TypeParameterClass(GASTClass):

    pass
class NamedModelElement:

    pass
class gast_core_Directory(NamedModelElement):

    def __init__(self, fileSystemPath: str, fullQualifiedPath: str, Directory120: set["Directory"] = None, Directory123: "Directory" = None, File: set["File"] = None, BasePath128: "BasePath" = None):
        self.fileSystemPath = fileSystemPath
        self.fullQualifiedPath = fullQualifiedPath
        self.Directory120 = Directory120 if Directory120 is not None else set()
        self.Directory123 = Directory123
        self.File = File if File is not None else set()
        self.BasePath128 = BasePath128
        
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
                if hasattr(item, "core126"):
                    opp_val = getattr(item, "core126", None)
                    
                    if opp_val == self:
                        setattr(item, "core126", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core126"):
                    opp_val = getattr(item, "core126", None)
                    
                    setattr(item, "core126", self)
                    

    @property
    def Directory120(self):
        return self.__Directory120

    @Directory120.setter
    def Directory120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Directory__Directory120", None)
        self.__Directory120 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core121"):
                    opp_val = getattr(item, "core121", None)
                    
                    if opp_val == self:
                        setattr(item, "core121", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core121"):
                    opp_val = getattr(item, "core121", None)
                    
                    setattr(item, "core121", self)
                    

    @property
    def BasePath128(self):
        return self.__BasePath128

    @BasePath128.setter
    def BasePath128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Directory__BasePath128", None)
        self.__BasePath128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core129"):
                opp_val = getattr(old_value, "core129", None)
                if opp_val == self:
                    setattr(old_value, "core129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core129"):
                opp_val = getattr(value, "core129", None)
                setattr(value, "core129", self)

    @property
    def Directory123(self):
        return self.__Directory123

    @Directory123.setter
    def Directory123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Directory__Directory123", None)
        self.__Directory123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core124"):
                opp_val = getattr(old_value, "core124", None)
                if opp_val == self:
                    setattr(old_value, "core124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core124"):
                opp_val = getattr(value, "core124", None)
                setattr(value, "core124", self)

class gast_core_File(NamedModelElement):

    def __init__(self, size: str, fullQualifiedPath: str, sourceFile: bool, assemblyFile: bool, linesOfCode: int, fileSystemPath: str, gast_core_File145: set["GlobalFunction"] = None, gast_core_File148: set["GlobalVariable"] = None, gast_core_File: "Root" = None, gast_core_File133: set["GASTType"] = None, gast_core_File136: set["GASTType"] = None, gast_core_File139: set["GlobalVariable"] = None, gast_core_File142: set["GlobalFunction"] = None, gast_core_File151: set["Package"] = None, gast_core_File154: set["File"] = None, Directory157: "Directory" = None):
        self.size = size
        self.fullQualifiedPath = fullQualifiedPath
        self.sourceFile = sourceFile
        self.assemblyFile = assemblyFile
        self.linesOfCode = linesOfCode
        self.fileSystemPath = fileSystemPath
        self.gast_core_File145 = gast_core_File145 if gast_core_File145 is not None else set()
        self.gast_core_File148 = gast_core_File148 if gast_core_File148 is not None else set()
        self.gast_core_File = gast_core_File
        self.gast_core_File133 = gast_core_File133 if gast_core_File133 is not None else set()
        self.gast_core_File136 = gast_core_File136 if gast_core_File136 is not None else set()
        self.gast_core_File139 = gast_core_File139 if gast_core_File139 is not None else set()
        self.gast_core_File142 = gast_core_File142 if gast_core_File142 is not None else set()
        self.gast_core_File151 = gast_core_File151 if gast_core_File151 is not None else set()
        self.gast_core_File154 = gast_core_File154 if gast_core_File154 is not None else set()
        self.Directory157 = Directory157
        
    @property
    def fileSystemPath(self) -> str:
        return self.__fileSystemPath

    @fileSystemPath.setter
    def fileSystemPath(self, fileSystemPath: str):
        self.__fileSystemPath = fileSystemPath

    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def sourceFile(self) -> bool:
        return self.__sourceFile

    @sourceFile.setter
    def sourceFile(self, sourceFile: bool):
        self.__sourceFile = sourceFile

    @property
    def fullQualifiedPath(self) -> str:
        return self.__fullQualifiedPath

    @fullQualifiedPath.setter
    def fullQualifiedPath(self, fullQualifiedPath: str):
        self.__fullQualifiedPath = fullQualifiedPath

    @property
    def linesOfCode(self) -> int:
        return self.__linesOfCode

    @linesOfCode.setter
    def linesOfCode(self, linesOfCode: int):
        self.__linesOfCode = linesOfCode

    @property
    def assemblyFile(self) -> bool:
        return self.__assemblyFile

    @assemblyFile.setter
    def assemblyFile(self, assemblyFile: bool):
        self.__assemblyFile = assemblyFile

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
                if hasattr(item, "GASTType137"):
                    opp_val = getattr(item, "GASTType137", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTType137", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTType137"):
                    opp_val = getattr(item, "GASTType137", None)
                    
                    setattr(item, "GASTType137", self)
                    

    @property
    def gast_core_File151(self):
        return self.__gast_core_File151

    @gast_core_File151.setter
    def gast_core_File151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File151", None)
        self.__gast_core_File151 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package152"):
                    opp_val = getattr(item, "Package152", None)
                    
                    if opp_val == self:
                        setattr(item, "Package152", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package152"):
                    opp_val = getattr(item, "Package152", None)
                    
                    setattr(item, "Package152", self)
                    

    @property
    def gast_core_File148(self):
        return self.__gast_core_File148

    @gast_core_File148.setter
    def gast_core_File148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File148", None)
        self.__gast_core_File148 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalVariable149"):
                    opp_val = getattr(item, "GlobalVariable149", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalVariable149", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalVariable149"):
                    opp_val = getattr(item, "GlobalVariable149", None)
                    
                    setattr(item, "GlobalVariable149", self)
                    

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
            if hasattr(old_value, "Root131"):
                opp_val = getattr(old_value, "Root131", None)
                if opp_val == self:
                    setattr(old_value, "Root131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Root131"):
                opp_val = getattr(value, "Root131", None)
                setattr(value, "Root131", self)

    @property
    def gast_core_File154(self):
        return self.__gast_core_File154

    @gast_core_File154.setter
    def gast_core_File154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File154", None)
        self.__gast_core_File154 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "File155"):
                    opp_val = getattr(item, "File155", None)
                    
                    if opp_val == self:
                        setattr(item, "File155", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "File155"):
                    opp_val = getattr(item, "File155", None)
                    
                    setattr(item, "File155", self)
                    

    @property
    def Directory157(self):
        return self.__Directory157

    @Directory157.setter
    def Directory157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__Directory157", None)
        self.__Directory157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core158"):
                opp_val = getattr(old_value, "core158", None)
                if opp_val == self:
                    setattr(old_value, "core158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core158"):
                opp_val = getattr(value, "core158", None)
                setattr(value, "core158", self)

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
                if hasattr(item, "GASTType134"):
                    opp_val = getattr(item, "GASTType134", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTType134", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTType134"):
                    opp_val = getattr(item, "GASTType134", None)
                    
                    setattr(item, "GASTType134", self)
                    

    @property
    def gast_core_File145(self):
        return self.__gast_core_File145

    @gast_core_File145.setter
    def gast_core_File145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_File__gast_core_File145", None)
        self.__gast_core_File145 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalFunction146"):
                    opp_val = getattr(item, "GlobalFunction146", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalFunction146", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalFunction146"):
                    opp_val = getattr(item, "GlobalFunction146", None)
                    
                    setattr(item, "GlobalFunction146", self)
                    

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
                if hasattr(item, "GlobalFunction143"):
                    opp_val = getattr(item, "GlobalFunction143", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalFunction143", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalFunction143"):
                    opp_val = getattr(item, "GlobalFunction143", None)
                    
                    setattr(item, "GlobalFunction143", self)
                    

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
                if hasattr(item, "GlobalVariable140"):
                    opp_val = getattr(item, "GlobalVariable140", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalVariable140", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalVariable140"):
                    opp_val = getattr(item, "GlobalVariable140", None)
                    
                    setattr(item, "GlobalVariable140", self)
                    

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

    def __init__(self, linesOfComments: int, linesOfCode: int, qualifiedName: str, gast_core_Package58: set["GASTClass"] = None, gast_core_Package61: set["Access"] = None, Delegate: set["Delegate"] = None, gast_core_Package: set["GASTClass"] = None, gast_core_Package52: set["GASTClass"] = None, gast_core_Package55: set["GASTClass"] = None, TypeAlias: set["TypeAlias"] = None, GlobalFunction: set["GlobalFunction"] = None, GlobalVariable: set["GlobalVariable"] = None, Root68: "Root" = None, GASTClass71: set["GASTClass"] = None, Package: set["Package"] = None, Package75: "Package" = None, gast_core_Package78: set["Package"] = None):
        self.linesOfComments = linesOfComments
        self.linesOfCode = linesOfCode
        self.qualifiedName = qualifiedName
        self.gast_core_Package58 = gast_core_Package58 if gast_core_Package58 is not None else set()
        self.gast_core_Package61 = gast_core_Package61 if gast_core_Package61 is not None else set()
        self.Delegate = Delegate if Delegate is not None else set()
        self.gast_core_Package = gast_core_Package if gast_core_Package is not None else set()
        self.gast_core_Package52 = gast_core_Package52 if gast_core_Package52 is not None else set()
        self.gast_core_Package55 = gast_core_Package55 if gast_core_Package55 is not None else set()
        self.TypeAlias = TypeAlias if TypeAlias is not None else set()
        self.GlobalFunction = GlobalFunction if GlobalFunction is not None else set()
        self.GlobalVariable = GlobalVariable if GlobalVariable is not None else set()
        self.Root68 = Root68
        self.GASTClass71 = GASTClass71 if GASTClass71 is not None else set()
        self.Package = Package if Package is not None else set()
        self.Package75 = Package75
        self.gast_core_Package78 = gast_core_Package78 if gast_core_Package78 is not None else set()
        
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
                if hasattr(item, "core73"):
                    opp_val = getattr(item, "core73", None)
                    
                    if opp_val == self:
                        setattr(item, "core73", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core73"):
                    opp_val = getattr(item, "core73", None)
                    
                    setattr(item, "core73", self)
                    

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
                if hasattr(item, "functions65"):
                    opp_val = getattr(item, "functions65", None)
                    
                    if opp_val == self:
                        setattr(item, "functions65", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "functions65"):
                    opp_val = getattr(item, "functions65", None)
                    
                    setattr(item, "functions65", self)
                    

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
    def Root68(self):
        return self.__Root68

    @Root68.setter
    def Root68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__Root68", None)
        self.__Root68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core69"):
                opp_val = getattr(old_value, "core69", None)
                if opp_val == self:
                    setattr(old_value, "core69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core69"):
                opp_val = getattr(value, "core69", None)
                setattr(value, "core69", self)

    @property
    def gast_core_Package58(self):
        return self.__gast_core_Package58

    @gast_core_Package58.setter
    def gast_core_Package58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__gast_core_Package58", None)
        self.__gast_core_Package58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass59"):
                    opp_val = getattr(item, "GASTClass59", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass59", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass59"):
                    opp_val = getattr(item, "GASTClass59", None)
                    
                    setattr(item, "GASTClass59", self)
                    

    @property
    def GASTClass71(self):
        return self.__GASTClass71

    @GASTClass71.setter
    def GASTClass71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__GASTClass71", None)
        self.__GASTClass71 = value if value is not None else set()
        
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
                if hasattr(item, "GASTClass56"):
                    opp_val = getattr(item, "GASTClass56", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass56", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass56"):
                    opp_val = getattr(item, "GASTClass56", None)
                    
                    setattr(item, "GASTClass56", self)
                    

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
                if hasattr(item, "types81"):
                    opp_val = getattr(item, "types81", None)
                    
                    if opp_val == self:
                        setattr(item, "types81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types81"):
                    opp_val = getattr(item, "types81", None)
                    
                    setattr(item, "types81", self)
                    

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
    def gast_core_Package61(self):
        return self.__gast_core_Package61

    @gast_core_Package61.setter
    def gast_core_Package61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__gast_core_Package61", None)
        self.__gast_core_Package61 = value if value is not None else set()
        
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
                if hasattr(item, "functions63"):
                    opp_val = getattr(item, "functions63", None)
                    
                    if opp_val == self:
                        setattr(item, "functions63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "functions63"):
                    opp_val = getattr(item, "functions63", None)
                    
                    setattr(item, "functions63", self)
                    

    @property
    def gast_core_Package78(self):
        return self.__gast_core_Package78

    @gast_core_Package78.setter
    def gast_core_Package78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__gast_core_Package78", None)
        self.__gast_core_Package78 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package79"):
                    opp_val = getattr(item, "Package79", None)
                    
                    if opp_val == self:
                        setattr(item, "Package79", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package79"):
                    opp_val = getattr(item, "Package79", None)
                    
                    setattr(item, "Package79", self)
                    

    @property
    def Package75(self):
        return self.__Package75

    @Package75.setter
    def Package75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Package__Package75", None)
        self.__Package75 = value
        
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

class GlobalFunction:

    pass
class Delegate:

    pass
class Access:

    pass
class gast_accesses_VariableAccess(Access):

    def __init__(self, write: bool, gast_accesses_VariableAccess: "Variable" = None, Access: "gast_core_Package", Access248: "gast_types_GASTClass", Access84: "gast_core_Root", Access335: "gast_functions_Function"):
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
            if hasattr(old_value, "Variable289"):
                opp_val = getattr(old_value, "Variable289", None)
                if opp_val == self:
                    setattr(old_value, "Variable289", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable289"):
                opp_val = getattr(value, "Variable289", None)
                setattr(value, "Variable289", self)

class gast_accesses_TypeAccess(Access):

    pass
class gast_accesses_FunctionAccess(Access):

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
class Root:

    pass
class ModelElement:

    pass
class gast_core_NamedModelElement(ModelElement):

    def __init__(self, simpleName: str, ModelElement113: "gast_core_Root", ModelElement294: "gast_accesses_Access", ModelElement: "gast_core_Root"):
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

    def __init__(self, linesOfComments: int, linesOfCode: int, gast_core_Root100: set["GlobalVariable"] = None, Package103: set["Package"] = None, Clone: set["Clone"] = None, gast_core_Root108: set["StructuralAbstraction"] = None, gast_core_Root: set["Access"] = None, gast_core_Root86: set["GASTClass"] = None, gast_core_Root89: set["GASTClass"] = None, gast_core_Root92: set["GASTClass"] = None, gast_core_Root95: set["GASTClass"] = None, gast_core_Root98: set["ModelElement"] = None, gast_core_Root110: set["GASTType"] = None, gast_core_Root112: set["ModelElement"] = None, BasePath: set["BasePath"] = None, GlobalFunction117: set["GlobalFunction"] = None, ModelElement113: "gast_core_Root", ModelElement294: "gast_accesses_Access", ModelElement: "gast_core_Root"):
        self.linesOfComments = linesOfComments
        self.linesOfCode = linesOfCode
        self.gast_core_Root100 = gast_core_Root100 if gast_core_Root100 is not None else set()
        self.Package103 = Package103 if Package103 is not None else set()
        self.Clone = Clone if Clone is not None else set()
        self.gast_core_Root108 = gast_core_Root108 if gast_core_Root108 is not None else set()
        self.gast_core_Root = gast_core_Root if gast_core_Root is not None else set()
        self.gast_core_Root86 = gast_core_Root86 if gast_core_Root86 is not None else set()
        self.gast_core_Root89 = gast_core_Root89 if gast_core_Root89 is not None else set()
        self.gast_core_Root92 = gast_core_Root92 if gast_core_Root92 is not None else set()
        self.gast_core_Root95 = gast_core_Root95 if gast_core_Root95 is not None else set()
        self.gast_core_Root98 = gast_core_Root98 if gast_core_Root98 is not None else set()
        self.gast_core_Root110 = gast_core_Root110 if gast_core_Root110 is not None else set()
        self.gast_core_Root112 = gast_core_Root112 if gast_core_Root112 is not None else set()
        self.BasePath = BasePath if BasePath is not None else set()
        self.GlobalFunction117 = GlobalFunction117 if GlobalFunction117 is not None else set()
        
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
    def GlobalFunction117(self):
        return self.__GlobalFunction117

    @GlobalFunction117.setter
    def GlobalFunction117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__GlobalFunction117", None)
        self.__GlobalFunction117 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "functions118"):
                    opp_val = getattr(item, "functions118", None)
                    
                    if opp_val == self:
                        setattr(item, "functions118", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "functions118"):
                    opp_val = getattr(item, "functions118", None)
                    
                    setattr(item, "functions118", self)
                    

    @property
    def gast_core_Root98(self):
        return self.__gast_core_Root98

    @gast_core_Root98.setter
    def gast_core_Root98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root98", None)
        self.__gast_core_Root98 = value if value is not None else set()
        
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
                if hasattr(item, "annotations106"):
                    opp_val = getattr(item, "annotations106", None)
                    
                    if opp_val == self:
                        setattr(item, "annotations106", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "annotations106"):
                    opp_val = getattr(item, "annotations106", None)
                    
                    setattr(item, "annotations106", self)
                    

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
                if hasattr(item, "core115"):
                    opp_val = getattr(item, "core115", None)
                    
                    if opp_val == self:
                        setattr(item, "core115", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core115"):
                    opp_val = getattr(item, "core115", None)
                    
                    setattr(item, "core115", self)
                    

    @property
    def gast_core_Root92(self):
        return self.__gast_core_Root92

    @gast_core_Root92.setter
    def gast_core_Root92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root92", None)
        self.__gast_core_Root92 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass93"):
                    opp_val = getattr(item, "GASTClass93", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass93", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass93"):
                    opp_val = getattr(item, "GASTClass93", None)
                    
                    setattr(item, "GASTClass93", self)
                    

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
    def gast_core_Root112(self):
        return self.__gast_core_Root112

    @gast_core_Root112.setter
    def gast_core_Root112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root112", None)
        self.__gast_core_Root112 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelElement113"):
                    opp_val = getattr(item, "ModelElement113", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelElement113", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelElement113"):
                    opp_val = getattr(item, "ModelElement113", None)
                    
                    setattr(item, "ModelElement113", self)
                    

    @property
    def gast_core_Root110(self):
        return self.__gast_core_Root110

    @gast_core_Root110.setter
    def gast_core_Root110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root110", None)
        self.__gast_core_Root110 = value if value is not None else set()
        
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
                if hasattr(item, "GlobalVariable101"):
                    opp_val = getattr(item, "GlobalVariable101", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalVariable101", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalVariable101"):
                    opp_val = getattr(item, "GlobalVariable101", None)
                    
                    setattr(item, "GlobalVariable101", self)
                    

    @property
    def gast_core_Root86(self):
        return self.__gast_core_Root86

    @gast_core_Root86.setter
    def gast_core_Root86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root86", None)
        self.__gast_core_Root86 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass87"):
                    opp_val = getattr(item, "GASTClass87", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass87", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass87"):
                    opp_val = getattr(item, "GASTClass87", None)
                    
                    setattr(item, "GASTClass87", self)
                    

    @property
    def gast_core_Root95(self):
        return self.__gast_core_Root95

    @gast_core_Root95.setter
    def gast_core_Root95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root95", None)
        self.__gast_core_Root95 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass96"):
                    opp_val = getattr(item, "GASTClass96", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass96", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass96"):
                    opp_val = getattr(item, "GASTClass96", None)
                    
                    setattr(item, "GASTClass96", self)
                    

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
                if hasattr(item, "Access84"):
                    opp_val = getattr(item, "Access84", None)
                    
                    if opp_val == self:
                        setattr(item, "Access84", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Access84"):
                    opp_val = getattr(item, "Access84", None)
                    
                    setattr(item, "Access84", self)
                    

    @property
    def gast_core_Root89(self):
        return self.__gast_core_Root89

    @gast_core_Root89.setter
    def gast_core_Root89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__gast_core_Root89", None)
        self.__gast_core_Root89 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GASTClass90"):
                    opp_val = getattr(item, "GASTClass90", None)
                    
                    if opp_val == self:
                        setattr(item, "GASTClass90", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GASTClass90"):
                    opp_val = getattr(item, "GASTClass90", None)
                    
                    setattr(item, "GASTClass90", self)
                    

    @property
    def Package103(self):
        return self.__Package103

    @Package103.setter
    def Package103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_core_Root__Package103", None)
        self.__Package103 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core104"):
                    opp_val = getattr(item, "core104", None)
                    
                    if opp_val == self:
                        setattr(item, "core104", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core104"):
                    opp_val = getattr(item, "core104", None)
                    
                    setattr(item, "core104", self)
                    

    def getPackageByQualifiedName(self, qualifiedName: str) -> str:
        # TODO: Implement getPackageByQualifiedName method
        pass

    def getPackageByName(self, name: str) -> str:
        # TODO: Implement getPackageByName method
        pass

class gast_core_SourceEntity(ModelElement):

    pass
class gast_core_BasePath(ModelElement):

    def __init__(self, path: str, Root: "Root" = None, Directory: set["Directory"] = None, ModelElement113: "gast_core_Root", ModelElement294: "gast_accesses_Access", ModelElement: "gast_core_Root"):
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
                if hasattr(item, "core48"):
                    opp_val = getattr(item, "core48", None)
                    
                    if opp_val == self:
                        setattr(item, "core48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core48"):
                    opp_val = getattr(item, "core48", None)
                    
                    setattr(item, "core48", self)
                    

class gast_statements_GASTBehaviour:

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

class CatchParameter:

    pass
class BranchStatement:

    pass
class GASTExpression:

    pass
class Function:

    pass
class gast_functions_GlobalFunction(Function):

    def __init__(self, kind: str, Package313: "Package" = None, Root316: "Root" = None, functions355: "gast_variables_LocalVariable", Function287: "gast_accesses_FunctionAccess", functions344: "gast_variables_FormalParameter", Function243: "gast_types_GASTClass", functions218: "gast_types_GASTClass", Function279: "gast_accesses_DelegateAccess", functions275: "gast_accesses_DeclarationTypeAccess", functions: "gast_statements_BlockStatement", Function270: "gast_accesses_BaseAccess", Function299: "gast_functions_Delegate"):
        self.kind = kind
        self.Package313 = Package313
        self.Root316 = Root316
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def Package313(self):
        return self.__Package313

    @Package313.setter
    def Package313(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_GlobalFunction__Package313", None)
        self.__Package313 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core314"):
                opp_val = getattr(old_value, "core314", None)
                if opp_val == self:
                    setattr(old_value, "core314", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core314"):
                opp_val = getattr(value, "core314", None)
                setattr(value, "core314", self)

    @property
    def Root316(self):
        return self.__Root316

    @Root316.setter
    def Root316(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_functions_GlobalFunction__Root316", None)
        self.__Root316 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core317"):
                opp_val = getattr(old_value, "core317", None)
                if opp_val == self:
                    setattr(old_value, "core317", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core317"):
                opp_val = getattr(value, "core317", None)
                setattr(value, "core317", self)

class BlockStatement:

    pass
class gast_statements_CatchBlock(BlockStatement):

    pass
class LoopStatement:

    pass
class Branch:

    pass
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
class gast_statements_GASTExpression(SourceEntity):

    pass
class gast_types_Member(SourceEntity):

    def __init__(self, visibility: str, abstract: bool, extern: bool, final: bool, internal: bool, introspectable: bool, override: bool, static: bool, typeParameterClassMember: bool, virtual: bool, gast_types_Member: "Member" = None, core165: "gast_core_Position"):
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
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

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
    def final(self) -> bool:
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final

    @property
    def typeParameterClassMember(self) -> bool:
        return self.__typeParameterClassMember

    @typeParameterClassMember.setter
    def typeParameterClassMember(self, typeParameterClassMember: bool):
        self.__typeParameterClassMember = typeParameterClassMember

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def virtual(self) -> bool:
        return self.__virtual

    @virtual.setter
    def virtual(self, virtual: bool):
        self.__virtual = virtual

    @property
    def introspectable(self) -> bool:
        return self.__introspectable

    @introspectable.setter
    def introspectable(self, introspectable: bool):
        self.__introspectable = introspectable

    @property
    def internal(self) -> bool:
        return self.__internal

    @internal.setter
    def internal(self, internal: bool):
        self.__internal = internal

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

class gast_statements_Branch(SourceEntity):

    pass
class gast_accesses_BaseAccess(SourceEntity):

    pass
class gast_statements_Statement(SourceEntity):

    def __init__(self, numberOfStatements: int, maximumNestingLevel: int, numberOfComments: int, linesOfCode: int, numberOfEdgesInCFG: int, numberOfNodesInCFG: int, BaseAccess: set["BaseAccess"] = None, CloneInstance: "CloneInstance" = None, BlockStatement9: "BlockStatement" = None, gast_statements_Statement: "Statement" = None, Branch: "Branch" = None, LoopStatement: "LoopStatement" = None, core165: "gast_core_Position"):
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
        
    @property
    def numberOfEdgesInCFG(self) -> int:
        return self.__numberOfEdgesInCFG

    @numberOfEdgesInCFG.setter
    def numberOfEdgesInCFG(self, numberOfEdgesInCFG: int):
        self.__numberOfEdgesInCFG = numberOfEdgesInCFG

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
    def linesOfCode(self) -> int:
        return self.__linesOfCode

    @linesOfCode.setter
    def linesOfCode(self, linesOfCode: int):
        self.__linesOfCode = linesOfCode

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

class CatchBlock:

    pass
class Statement:

    pass
class gast_statements_BlockStatement(Statement):

    def __init__(self, synchronized: bool, Statement16: set["Statement"] = None, Function: "Function" = None, statements38: "gast_statements_LoopStatement", statements178: "gast_annotations_CloneInstance", Statement330: "gast_functions_Function", statements262: "gast_accesses_BaseAccess", Statement: "gast_statements_Statement", statements24: "gast_statements_Branch", Statement264: "gast_accesses_BaseAccess", statements17: "gast_statements_BlockStatement"):
        self.synchronized = synchronized
        self.Statement16 = Statement16 if Statement16 is not None else set()
        self.Function = Function
        
    @property
    def synchronized(self) -> bool:
        return self.__synchronized

    @synchronized.setter
    def synchronized(self, synchronized: bool):
        self.__synchronized = synchronized

    @property
    def Statement16(self):
        return self.__Statement16

    @Statement16.setter
    def Statement16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_BlockStatement__Statement16", None)
        self.__Statement16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statements17"):
                    opp_val = getattr(item, "statements17", None)
                    
                    if opp_val == self:
                        setattr(item, "statements17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statements17"):
                    opp_val = getattr(item, "statements17", None)
                    
                    setattr(item, "statements17", self)
                    

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

class gast_statements_JumpStatement(Statement):

    def __init__(self, kind: str, gast_statements_JumpStatement: "GASTExpression" = None, statements38: "gast_statements_LoopStatement", statements178: "gast_annotations_CloneInstance", Statement330: "gast_functions_Function", statements262: "gast_accesses_BaseAccess", Statement: "gast_statements_Statement", statements24: "gast_statements_Branch", Statement264: "gast_accesses_BaseAccess", statements17: "gast_statements_BlockStatement"):
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
            if hasattr(old_value, "GASTExpression41"):
                opp_val = getattr(old_value, "GASTExpression41", None)
                if opp_val == self:
                    setattr(old_value, "GASTExpression41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTExpression41"):
                opp_val = getattr(value, "GASTExpression41", None)
                setattr(value, "GASTExpression41", self)

class gast_statements_LoopStatement(Statement):

    def __init__(self, kind: str, gast_statements_LoopStatement: "GASTExpression" = None, gast_statements_LoopStatement31: "GASTExpression" = None, gast_statements_LoopStatement34: "GASTExpression" = None, Statement37: "Statement" = None, statements38: "gast_statements_LoopStatement", statements178: "gast_annotations_CloneInstance", Statement330: "gast_functions_Function", statements262: "gast_accesses_BaseAccess", Statement: "gast_statements_Statement", statements24: "gast_statements_Branch", Statement264: "gast_accesses_BaseAccess", statements17: "gast_statements_BlockStatement"):
        self.kind = kind
        self.gast_statements_LoopStatement = gast_statements_LoopStatement
        self.gast_statements_LoopStatement31 = gast_statements_LoopStatement31
        self.gast_statements_LoopStatement34 = gast_statements_LoopStatement34
        self.Statement37 = Statement37
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def gast_statements_LoopStatement31(self):
        return self.__gast_statements_LoopStatement31

    @gast_statements_LoopStatement31.setter
    def gast_statements_LoopStatement31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_LoopStatement__gast_statements_LoopStatement31", None)
        self.__gast_statements_LoopStatement31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GASTExpression32"):
                opp_val = getattr(old_value, "GASTExpression32", None)
                if opp_val == self:
                    setattr(old_value, "GASTExpression32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTExpression32"):
                opp_val = getattr(value, "GASTExpression32", None)
                setattr(value, "GASTExpression32", self)

    @property
    def Statement37(self):
        return self.__Statement37

    @Statement37.setter
    def Statement37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_LoopStatement__Statement37", None)
        self.__Statement37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statements38"):
                opp_val = getattr(old_value, "statements38", None)
                if opp_val == self:
                    setattr(old_value, "statements38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statements38"):
                opp_val = getattr(value, "statements38", None)
                setattr(value, "statements38", self)

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
            if hasattr(old_value, "GASTExpression29"):
                opp_val = getattr(old_value, "GASTExpression29", None)
                if opp_val == self:
                    setattr(old_value, "GASTExpression29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GASTExpression29"):
                opp_val = getattr(value, "GASTExpression29", None)
                setattr(value, "GASTExpression29", self)

    @property
    def gast_statements_LoopStatement34(self):
        return self.__gast_statements_LoopStatement34

    @gast_statements_LoopStatement34.setter
    def gast_statements_LoopStatement34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gast_statements_LoopStatement__gast_statements_LoopStatement34", None)
        self.__gast_statements_LoopStatement34 = value
        
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

class gast_statements_SimpleStatement(Statement):

    pass
class gast_statements_BranchStatement(Statement):

    pass
class gast_statements_ExceptionHandler(Statement):

    pass