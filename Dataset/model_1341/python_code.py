from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class completeoclcs_Property:

    pass
class completeoclcs_Operation:

    pass
class completeoclcs_VariableCS:

    pass
class FeatureContextDeclCS:

    pass
class ExpCS:

    pass
class completeoclcs_OCLMessageArgCS(ExpCS):

    pass
class completeoclcs_PropertyContextDeclCS(FeatureContextDeclCS):

    pass
class completeoclcs_PathNameCS:

    pass
class MorePivotable:

    pass
class ModelElementCS:

    pass
class completeoclcs_PathNameDeclCS(ModelElementCS, MorePivotable):

    pass
class completeoclcs_Package:

    pass
class completeoclcs_ExpSpecificationCS:

    pass
class TypedElementCS:

    pass
class PathNameDeclCS:

    pass
class completeoclcs_PackageDeclarationCS(PathNameDeclCS):

    pass
class completeoclcs_ContextDeclCS(PathNameDeclCS):

    pass
class completeoclcs_TypedRefCS:

    pass
class completeoclcs_ParameterCS:

    pass
class DefCS:

    pass
class completeoclcs_DefPropertyCS(DefCS):

    pass
class completeoclcs_DefCS(TypedElementCS):

    def __init__(self, isStatic: bool, DefCS: "completeoclcs_ClassifierContextDeclCS" = None, completeoclcs_DefCS: "completeoclcs_ExpSpecificationCS" = None, ownedDefinitions: "completeoclcs_ClassifierContextDeclCS" = None):
        self.isStatic = isStatic
        self.DefCS = DefCS
        self.completeoclcs_DefCS = completeoclcs_DefCS
        self.ownedDefinitions = ownedDefinitions
        
    @property
    def isStatic(self) -> bool:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: bool):
        self.__isStatic = isStatic

    @property
    def completeoclcs_DefCS(self):
        return self.__completeoclcs_DefCS

    @completeoclcs_DefCS.setter
    def completeoclcs_DefCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_completeoclcs_DefCS__completeoclcs_DefCS", None)
        self.__completeoclcs_DefCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "completeoclcs_ExpSpecificationCS"):
                opp_val = getattr(old_value, "completeoclcs_ExpSpecificationCS", None)
                if opp_val == self:
                    setattr(old_value, "completeoclcs_ExpSpecificationCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "completeoclcs_ExpSpecificationCS"):
                opp_val = getattr(value, "completeoclcs_ExpSpecificationCS", None)
                setattr(value, "completeoclcs_ExpSpecificationCS", self)

    @property
    def ownedDefinitions(self):
        return self.__ownedDefinitions

    @ownedDefinitions.setter
    def ownedDefinitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_completeoclcs_DefCS__ownedDefinitions", None)
        self.__ownedDefinitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassifierContextDeclCS"):
                opp_val = getattr(old_value, "ClassifierContextDeclCS", None)
                if opp_val == self:
                    setattr(old_value, "ClassifierContextDeclCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassifierContextDeclCS"):
                opp_val = getattr(value, "ClassifierContextDeclCS", None)
                setattr(value, "ClassifierContextDeclCS", self)

    @property
    def DefCS(self):
        return self.__DefCS

    @DefCS.setter
    def DefCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_completeoclcs_DefCS__DefCS", None)
        self.__DefCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningClassifierContextDecl"):
                opp_val = getattr(old_value, "owningClassifierContextDecl", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningClassifierContextDecl"):
                opp_val = getattr(value, "owningClassifierContextDecl", None)
                if opp_val is None:
                    setattr(value, "owningClassifierContextDecl", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class TemplateableElementCS:

    pass
class completeoclcs_OperationContextDeclCS(FeatureContextDeclCS, TemplateableElementCS):

    pass
class completeoclcs_DefOperationCS(DefCS, TemplateableElementCS):

    pass
class ContextDeclCS:

    pass
class completeoclcs_FeatureContextDeclCS(ContextDeclCS):

    pass
class completeoclcs_ClassifierContextDeclCS(ContextDeclCS, TemplateableElementCS):

    def __init__(self, selfName: str, completeoclcs_ClassifierContextDeclCS: set["completeoclcs_ConstraintCS"] = None, completeoclcs_ClassifierContextDeclCS3: "completeoclcs_Class" = None, owningClassifierContextDecl: set["completeoclcs_DefCS"] = None, ClassifierContextDeclCS: "completeoclcs_DefCS" = None):
        self.selfName = selfName
        self.completeoclcs_ClassifierContextDeclCS = completeoclcs_ClassifierContextDeclCS if completeoclcs_ClassifierContextDeclCS is not None else set()
        self.completeoclcs_ClassifierContextDeclCS3 = completeoclcs_ClassifierContextDeclCS3
        self.owningClassifierContextDecl = owningClassifierContextDecl if owningClassifierContextDecl is not None else set()
        self.ClassifierContextDeclCS = ClassifierContextDeclCS
        
    @property
    def selfName(self) -> str:
        return self.__selfName

    @selfName.setter
    def selfName(self, selfName: str):
        self.__selfName = selfName

    @property
    def owningClassifierContextDecl(self):
        return self.__owningClassifierContextDecl

    @owningClassifierContextDecl.setter
    def owningClassifierContextDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_completeoclcs_ClassifierContextDeclCS__owningClassifierContextDecl", None)
        self.__owningClassifierContextDecl = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DefCS"):
                    opp_val = getattr(item, "DefCS", None)
                    
                    if opp_val == self:
                        setattr(item, "DefCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DefCS"):
                    opp_val = getattr(item, "DefCS", None)
                    
                    setattr(item, "DefCS", self)
                    

    @property
    def completeoclcs_ClassifierContextDeclCS(self):
        return self.__completeoclcs_ClassifierContextDeclCS

    @completeoclcs_ClassifierContextDeclCS.setter
    def completeoclcs_ClassifierContextDeclCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_completeoclcs_ClassifierContextDeclCS__completeoclcs_ClassifierContextDeclCS", None)
        self.__completeoclcs_ClassifierContextDeclCS = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "completeoclcs_ConstraintCS"):
                    opp_val = getattr(item, "completeoclcs_ConstraintCS", None)
                    
                    if opp_val == self:
                        setattr(item, "completeoclcs_ConstraintCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "completeoclcs_ConstraintCS"):
                    opp_val = getattr(item, "completeoclcs_ConstraintCS", None)
                    
                    setattr(item, "completeoclcs_ConstraintCS", self)
                    

    @property
    def ClassifierContextDeclCS(self):
        return self.__ClassifierContextDeclCS

    @ClassifierContextDeclCS.setter
    def ClassifierContextDeclCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_completeoclcs_ClassifierContextDeclCS__ClassifierContextDeclCS", None)
        self.__ClassifierContextDeclCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedDefinitions"):
                opp_val = getattr(old_value, "ownedDefinitions", None)
                if opp_val == self:
                    setattr(old_value, "ownedDefinitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedDefinitions"):
                opp_val = getattr(value, "ownedDefinitions", None)
                setattr(value, "ownedDefinitions", self)

    @property
    def completeoclcs_ClassifierContextDeclCS3(self):
        return self.__completeoclcs_ClassifierContextDeclCS3

    @completeoclcs_ClassifierContextDeclCS3.setter
    def completeoclcs_ClassifierContextDeclCS3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_completeoclcs_ClassifierContextDeclCS__completeoclcs_ClassifierContextDeclCS3", None)
        self.__completeoclcs_ClassifierContextDeclCS3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "completeoclcs_Class"):
                opp_val = getattr(old_value, "completeoclcs_Class", None)
                if opp_val == self:
                    setattr(old_value, "completeoclcs_Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "completeoclcs_Class"):
                opp_val = getattr(value, "completeoclcs_Class", None)
                setattr(value, "completeoclcs_Class", self)

class RootCS:

    pass
class NamespaceCS:

    pass
class completeoclcs_CompleteOCLDocumentCS(RootCS, NamespaceCS):

    pass
class completeoclcs_Class:

    pass
class completeoclcs_ConstraintCS:

    pass