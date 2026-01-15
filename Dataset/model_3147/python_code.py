from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class AttributeCS:

    pass
class PackageCS:

    pass
class oclstdlibcs_LibPackageCS(PackageCS):

    pass
class oclstdlibcs_Precedence:

    pass
class Nameable:

    pass
class RootPackageCS:

    pass
class oclstdlibcs_LibRootPackageCS(RootPackageCS):

    pass
class oclstdlibcs_ParameterCS:

    pass
class StructuredClassCS:

    pass
class oclstdlibcs_LibClassCS(StructuredClassCS):

    pass
class ElementCS:

    pass
class oclstdlibcs_JavaImplementationCS(ElementCS):

    pass
class NamedElementCS:

    pass
class oclstdlibcs_PrecedenceCS(NamedElementCS):

    def __init__(self, isRightAssociative: bool, oclstdlibcs_PrecedenceCS: "oclstdlibcs_LibPackageCS" = None):
        self.isRightAssociative = isRightAssociative
        self.oclstdlibcs_PrecedenceCS = oclstdlibcs_PrecedenceCS
        
    @property
    def isRightAssociative(self) -> bool:
        return self.__isRightAssociative

    @isRightAssociative.setter
    def isRightAssociative(self, isRightAssociative: bool):
        self.__isRightAssociative = isRightAssociative

    @property
    def oclstdlibcs_PrecedenceCS(self):
        return self.__oclstdlibcs_PrecedenceCS

    @oclstdlibcs_PrecedenceCS.setter
    def oclstdlibcs_PrecedenceCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oclstdlibcs_PrecedenceCS__oclstdlibcs_PrecedenceCS", None)
        self.__oclstdlibcs_PrecedenceCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oclstdlibcs_LibPackageCS"):
                opp_val = getattr(old_value, "oclstdlibcs_LibPackageCS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oclstdlibcs_LibPackageCS"):
                opp_val = getattr(value, "oclstdlibcs_LibPackageCS", None)
                if opp_val is None:
                    setattr(value, "oclstdlibcs_LibPackageCS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class oclstdlibcs_JavaClassCS(NamedElementCS):

    pass
class ConstraintCS:

    pass
class oclstdlibcs_LibConstraintCS(ConstraintCS):

    pass
class JavaImplementationCS:

    pass
class oclstdlibcs_LibPropertyCS(AttributeCS, JavaImplementationCS):

    def __init__(self, isStatic: str):
        self.isStatic = isStatic
        
    @property
    def isStatic(self) -> str:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: str):
        self.__isStatic = isStatic

class OperationCS:

    pass
class oclstdlibcs_LibOperationCS(OperationCS, JavaImplementationCS):

    def __init__(self, isInvalidating: str, isStatic: str, isValidating: str, oclstdlibcs_LibOperationCS: "oclstdlibcs_Precedence" = None):
        self.isInvalidating = isInvalidating
        self.isStatic = isStatic
        self.isValidating = isValidating
        self.oclstdlibcs_LibOperationCS = oclstdlibcs_LibOperationCS
        
    @property
    def isValidating(self) -> str:
        return self.__isValidating

    @isValidating.setter
    def isValidating(self, isValidating: str):
        self.__isValidating = isValidating

    @property
    def isStatic(self) -> str:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: str):
        self.__isStatic = isStatic

    @property
    def isInvalidating(self) -> str:
        return self.__isInvalidating

    @isInvalidating.setter
    def isInvalidating(self, isInvalidating: str):
        self.__isInvalidating = isInvalidating

    @property
    def oclstdlibcs_LibOperationCS(self):
        return self.__oclstdlibcs_LibOperationCS

    @oclstdlibcs_LibOperationCS.setter
    def oclstdlibcs_LibOperationCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oclstdlibcs_LibOperationCS__oclstdlibcs_LibOperationCS", None)
        self.__oclstdlibcs_LibOperationCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oclstdlibcs_Precedence"):
                opp_val = getattr(old_value, "oclstdlibcs_Precedence", None)
                if opp_val == self:
                    setattr(old_value, "oclstdlibcs_Precedence", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oclstdlibcs_Precedence"):
                opp_val = getattr(value, "oclstdlibcs_Precedence", None)
                setattr(value, "oclstdlibcs_Precedence", self)

class oclstdlibcs_LibIterationCS(OperationCS, JavaImplementationCS):

    def __init__(self, isInvalidating: str, isValidating: str, oclstdlibcs_LibIterationCS: set["oclstdlibcs_ParameterCS"] = None, oclstdlibcs_LibIterationCS4: set["oclstdlibcs_ParameterCS"] = None):
        self.isInvalidating = isInvalidating
        self.isValidating = isValidating
        self.oclstdlibcs_LibIterationCS = oclstdlibcs_LibIterationCS if oclstdlibcs_LibIterationCS is not None else set()
        self.oclstdlibcs_LibIterationCS4 = oclstdlibcs_LibIterationCS4 if oclstdlibcs_LibIterationCS4 is not None else set()
        
    @property
    def isInvalidating(self) -> str:
        return self.__isInvalidating

    @isInvalidating.setter
    def isInvalidating(self, isInvalidating: str):
        self.__isInvalidating = isInvalidating

    @property
    def isValidating(self) -> str:
        return self.__isValidating

    @isValidating.setter
    def isValidating(self, isValidating: str):
        self.__isValidating = isValidating

    @property
    def oclstdlibcs_LibIterationCS4(self):
        return self.__oclstdlibcs_LibIterationCS4

    @oclstdlibcs_LibIterationCS4.setter
    def oclstdlibcs_LibIterationCS4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oclstdlibcs_LibIterationCS__oclstdlibcs_LibIterationCS4", None)
        self.__oclstdlibcs_LibIterationCS4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "oclstdlibcs_ParameterCS5"):
                    opp_val = getattr(item, "oclstdlibcs_ParameterCS5", None)
                    
                    if opp_val == self:
                        setattr(item, "oclstdlibcs_ParameterCS5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "oclstdlibcs_ParameterCS5"):
                    opp_val = getattr(item, "oclstdlibcs_ParameterCS5", None)
                    
                    setattr(item, "oclstdlibcs_ParameterCS5", self)
                    

    @property
    def oclstdlibcs_LibIterationCS(self):
        return self.__oclstdlibcs_LibIterationCS

    @oclstdlibcs_LibIterationCS.setter
    def oclstdlibcs_LibIterationCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oclstdlibcs_LibIterationCS__oclstdlibcs_LibIterationCS", None)
        self.__oclstdlibcs_LibIterationCS = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "oclstdlibcs_ParameterCS"):
                    opp_val = getattr(item, "oclstdlibcs_ParameterCS", None)
                    
                    if opp_val == self:
                        setattr(item, "oclstdlibcs_ParameterCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "oclstdlibcs_ParameterCS"):
                    opp_val = getattr(item, "oclstdlibcs_ParameterCS", None)
                    
                    setattr(item, "oclstdlibcs_ParameterCS", self)
                    

class oclstdlibcs_LibCoercionCS(OperationCS, JavaImplementationCS):

    pass
class oclstdlibcs_MetaclassNameCS(ElementCS, Nameable):

    def __init__(self, name: str, oclstdlibcs_MetaclassNameCS: "oclstdlibcs_LibClassCS" = None):
        self.name = name
        self.oclstdlibcs_MetaclassNameCS = oclstdlibcs_MetaclassNameCS
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def oclstdlibcs_MetaclassNameCS(self):
        return self.__oclstdlibcs_MetaclassNameCS

    @oclstdlibcs_MetaclassNameCS.setter
    def oclstdlibcs_MetaclassNameCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oclstdlibcs_MetaclassNameCS__oclstdlibcs_MetaclassNameCS", None)
        self.__oclstdlibcs_MetaclassNameCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oclstdlibcs_LibClassCS"):
                opp_val = getattr(old_value, "oclstdlibcs_LibClassCS", None)
                if opp_val == self:
                    setattr(old_value, "oclstdlibcs_LibClassCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oclstdlibcs_LibClassCS"):
                opp_val = getattr(value, "oclstdlibcs_LibClassCS", None)
                setattr(value, "oclstdlibcs_LibClassCS", self)
