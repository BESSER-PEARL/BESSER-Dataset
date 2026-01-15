from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class qvtrelationcs_Element:

    pass
class RootPackageCS:

    pass
class qvtrelationcs_TopLevelCS(RootPackageCS):

    pass
class qvtrelationcs_TypedRefCS:

    pass
class ExpCS:

    pass
class qvtrelationcs_Transformation:

    pass
class ClassCS:

    pass
class qvtrelationcs_TransformationCS(ClassCS):

    pass
class Relation:

    pass
class qvtrelationcs_Property:

    pass
class qvtrelationcs_PathNameCS:

    pass
class TemplateVariableCS:

    pass
class qvtrelationcs_TemplateCS(TemplateVariableCS, ExpCS):

    pass
class TypedElementCS:

    pass
class qvtrelationcs_QueryCS(TypedElementCS):

    pass
class qvtrelationcs_ParamDeclarationCS(TypedElementCS):

    pass
class qvtrelationcs_Namespace:

    pass
class NamedElementCS:

    pass
class qvtrelationcs_VarDeclarationIdCS(NamedElementCS):

    pass
class qvtrelationcs_RelationCS(NamedElementCS):

    def __init__(self, isDefault: bool, isTop: bool, qvtrelationcs_RelationCS: "Relation" = None, qvtrelationcs_RelationCS49: set["qvtrelationcs_VarDeclarationCS"] = None, qvtrelationcs_RelationCS51: set["qvtrelationcs_AbstractDomainCS"] = None, qvtrelationcs_RelationCS82: "qvtrelationcs_TransformationCS" = None, qvtrelationcs_RelationCS53: "qvtrelationcs_PatternCS" = None, qvtrelationcs_RelationCS56: "qvtrelationcs_PatternCS" = None):
        self.isDefault = isDefault
        self.isTop = isTop
        self.qvtrelationcs_RelationCS = qvtrelationcs_RelationCS
        self.qvtrelationcs_RelationCS49 = qvtrelationcs_RelationCS49 if qvtrelationcs_RelationCS49 is not None else set()
        self.qvtrelationcs_RelationCS51 = qvtrelationcs_RelationCS51 if qvtrelationcs_RelationCS51 is not None else set()
        self.qvtrelationcs_RelationCS82 = qvtrelationcs_RelationCS82
        self.qvtrelationcs_RelationCS53 = qvtrelationcs_RelationCS53
        self.qvtrelationcs_RelationCS56 = qvtrelationcs_RelationCS56
        
    @property
    def isTop(self) -> bool:
        return self.__isTop

    @isTop.setter
    def isTop(self, isTop: bool):
        self.__isTop = isTop

    @property
    def isDefault(self) -> bool:
        return self.__isDefault

    @isDefault.setter
    def isDefault(self, isDefault: bool):
        self.__isDefault = isDefault

    @property
    def qvtrelationcs_RelationCS49(self):
        return self.__qvtrelationcs_RelationCS49

    @qvtrelationcs_RelationCS49.setter
    def qvtrelationcs_RelationCS49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtrelationcs_RelationCS__qvtrelationcs_RelationCS49", None)
        self.__qvtrelationcs_RelationCS49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qvtrelationcs_VarDeclarationCS"):
                    opp_val = getattr(item, "qvtrelationcs_VarDeclarationCS", None)
                    
                    if opp_val == self:
                        setattr(item, "qvtrelationcs_VarDeclarationCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qvtrelationcs_VarDeclarationCS"):
                    opp_val = getattr(item, "qvtrelationcs_VarDeclarationCS", None)
                    
                    setattr(item, "qvtrelationcs_VarDeclarationCS", self)
                    

    @property
    def qvtrelationcs_RelationCS51(self):
        return self.__qvtrelationcs_RelationCS51

    @qvtrelationcs_RelationCS51.setter
    def qvtrelationcs_RelationCS51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtrelationcs_RelationCS__qvtrelationcs_RelationCS51", None)
        self.__qvtrelationcs_RelationCS51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qvtrelationcs_AbstractDomainCS"):
                    opp_val = getattr(item, "qvtrelationcs_AbstractDomainCS", None)
                    
                    if opp_val == self:
                        setattr(item, "qvtrelationcs_AbstractDomainCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qvtrelationcs_AbstractDomainCS"):
                    opp_val = getattr(item, "qvtrelationcs_AbstractDomainCS", None)
                    
                    setattr(item, "qvtrelationcs_AbstractDomainCS", self)
                    

    @property
    def qvtrelationcs_RelationCS(self):
        return self.__qvtrelationcs_RelationCS

    @qvtrelationcs_RelationCS.setter
    def qvtrelationcs_RelationCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtrelationcs_RelationCS__qvtrelationcs_RelationCS", None)
        self.__qvtrelationcs_RelationCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Relation"):
                opp_val = getattr(old_value, "Relation", None)
                if opp_val == self:
                    setattr(old_value, "Relation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Relation"):
                opp_val = getattr(value, "Relation", None)
                setattr(value, "Relation", self)

    @property
    def qvtrelationcs_RelationCS82(self):
        return self.__qvtrelationcs_RelationCS82

    @qvtrelationcs_RelationCS82.setter
    def qvtrelationcs_RelationCS82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtrelationcs_RelationCS__qvtrelationcs_RelationCS82", None)
        self.__qvtrelationcs_RelationCS82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qvtrelationcs_TransformationCS81"):
                opp_val = getattr(old_value, "qvtrelationcs_TransformationCS81", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qvtrelationcs_TransformationCS81"):
                opp_val = getattr(value, "qvtrelationcs_TransformationCS81", None)
                if opp_val is None:
                    setattr(value, "qvtrelationcs_TransformationCS81", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def qvtrelationcs_RelationCS53(self):
        return self.__qvtrelationcs_RelationCS53

    @qvtrelationcs_RelationCS53.setter
    def qvtrelationcs_RelationCS53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtrelationcs_RelationCS__qvtrelationcs_RelationCS53", None)
        self.__qvtrelationcs_RelationCS53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qvtrelationcs_PatternCS54"):
                opp_val = getattr(old_value, "qvtrelationcs_PatternCS54", None)
                if opp_val == self:
                    setattr(old_value, "qvtrelationcs_PatternCS54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qvtrelationcs_PatternCS54"):
                opp_val = getattr(value, "qvtrelationcs_PatternCS54", None)
                setattr(value, "qvtrelationcs_PatternCS54", self)

    @property
    def qvtrelationcs_RelationCS56(self):
        return self.__qvtrelationcs_RelationCS56

    @qvtrelationcs_RelationCS56.setter
    def qvtrelationcs_RelationCS56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtrelationcs_RelationCS__qvtrelationcs_RelationCS56", None)
        self.__qvtrelationcs_RelationCS56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qvtrelationcs_PatternCS57"):
                opp_val = getattr(old_value, "qvtrelationcs_PatternCS57", None)
                if opp_val == self:
                    setattr(old_value, "qvtrelationcs_PatternCS57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qvtrelationcs_PatternCS57"):
                opp_val = getattr(value, "qvtrelationcs_PatternCS57", None)
                setattr(value, "qvtrelationcs_PatternCS57", self)

class qvtrelationcs_ModelDeclCS(NamedElementCS):

    pass
class qvtrelationcs_Class:

    pass
class qvtrelationcs_ExpCS:

    pass
class qvtrelationcs_ElementTemplateCS(TemplateVariableCS):

    pass
class qvtrelationcs_TemplateVariableCS(NamedElementCS):

    pass
class TemplateCS:

    pass
class qvtrelationcs_ObjectTemplateCS(TemplateCS):

    pass
class qvtrelationcs_CollectionTemplateCS(TemplateCS):

    pass
class Nameable:

    pass
class ModelElementCS:

    pass
class qvtrelationcs_DefaultValueCS(ModelElementCS):

    pass
class qvtrelationcs_PatternCS(ModelElementCS):

    pass
class qvtrelationcs_PropertyTemplateCS(ModelElementCS):

    pass
class qvtrelationcs_PredicateCS(ModelElementCS):

    pass
class qvtrelationcs_UnitCS(ModelElementCS):

    pass
class qvtrelationcs_KeyDeclCS(ModelElementCS):

    pass
class qvtrelationcs_VarDeclarationCS(ModelElementCS):

    pass
class qvtrelationcs_AbstractDomainCS(ModelElementCS, Nameable):

    pass
class qvtrelationcs_DomainPatternCS(ModelElementCS):

    pass
class qvtrelationcs_TypedModel:

    pass
class AbstractDomainCS:

    pass
class qvtrelationcs_PrimitiveTypeDomainCS(TemplateVariableCS, AbstractDomainCS):

    pass
class qvtrelationcs_DomainCS(AbstractDomainCS):

    def __init__(self, implementedBy: str, isCheckonly: bool, isEnforce: bool, isReplace: bool, qvtrelationcs_DomainCS: "qvtrelationcs_TypedModel" = None, qvtrelationcs_DomainCS8: set["qvtrelationcs_DomainPatternCS"] = None, qvtrelationcs_DomainCS10: set["qvtrelationcs_DefaultValueCS"] = None, qvtrelationcs_DomainCS13: "qvtrelationcs_ExpCS" = None):
        self.implementedBy = implementedBy
        self.isCheckonly = isCheckonly
        self.isEnforce = isEnforce
        self.isReplace = isReplace
        self.qvtrelationcs_DomainCS = qvtrelationcs_DomainCS
        self.qvtrelationcs_DomainCS8 = qvtrelationcs_DomainCS8 if qvtrelationcs_DomainCS8 is not None else set()
        self.qvtrelationcs_DomainCS10 = qvtrelationcs_DomainCS10 if qvtrelationcs_DomainCS10 is not None else set()
        self.qvtrelationcs_DomainCS13 = qvtrelationcs_DomainCS13
        
    @property
    def isEnforce(self) -> bool:
        return self.__isEnforce

    @isEnforce.setter
    def isEnforce(self, isEnforce: bool):
        self.__isEnforce = isEnforce

    @property
    def isReplace(self) -> bool:
        return self.__isReplace

    @isReplace.setter
    def isReplace(self, isReplace: bool):
        self.__isReplace = isReplace

    @property
    def implementedBy(self) -> str:
        return self.__implementedBy

    @implementedBy.setter
    def implementedBy(self, implementedBy: str):
        self.__implementedBy = implementedBy

    @property
    def isCheckonly(self) -> bool:
        return self.__isCheckonly

    @isCheckonly.setter
    def isCheckonly(self, isCheckonly: bool):
        self.__isCheckonly = isCheckonly

    @property
    def qvtrelationcs_DomainCS8(self):
        return self.__qvtrelationcs_DomainCS8

    @qvtrelationcs_DomainCS8.setter
    def qvtrelationcs_DomainCS8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtrelationcs_DomainCS__qvtrelationcs_DomainCS8", None)
        self.__qvtrelationcs_DomainCS8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qvtrelationcs_DomainPatternCS"):
                    opp_val = getattr(item, "qvtrelationcs_DomainPatternCS", None)
                    
                    if opp_val == self:
                        setattr(item, "qvtrelationcs_DomainPatternCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qvtrelationcs_DomainPatternCS"):
                    opp_val = getattr(item, "qvtrelationcs_DomainPatternCS", None)
                    
                    setattr(item, "qvtrelationcs_DomainPatternCS", self)
                    

    @property
    def qvtrelationcs_DomainCS10(self):
        return self.__qvtrelationcs_DomainCS10

    @qvtrelationcs_DomainCS10.setter
    def qvtrelationcs_DomainCS10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtrelationcs_DomainCS__qvtrelationcs_DomainCS10", None)
        self.__qvtrelationcs_DomainCS10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qvtrelationcs_DefaultValueCS11"):
                    opp_val = getattr(item, "qvtrelationcs_DefaultValueCS11", None)
                    
                    if opp_val == self:
                        setattr(item, "qvtrelationcs_DefaultValueCS11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qvtrelationcs_DefaultValueCS11"):
                    opp_val = getattr(item, "qvtrelationcs_DefaultValueCS11", None)
                    
                    setattr(item, "qvtrelationcs_DefaultValueCS11", self)
                    

    @property
    def qvtrelationcs_DomainCS(self):
        return self.__qvtrelationcs_DomainCS

    @qvtrelationcs_DomainCS.setter
    def qvtrelationcs_DomainCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtrelationcs_DomainCS__qvtrelationcs_DomainCS", None)
        self.__qvtrelationcs_DomainCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qvtrelationcs_TypedModel"):
                opp_val = getattr(old_value, "qvtrelationcs_TypedModel", None)
                if opp_val == self:
                    setattr(old_value, "qvtrelationcs_TypedModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qvtrelationcs_TypedModel"):
                opp_val = getattr(value, "qvtrelationcs_TypedModel", None)
                setattr(value, "qvtrelationcs_TypedModel", self)

    @property
    def qvtrelationcs_DomainCS13(self):
        return self.__qvtrelationcs_DomainCS13

    @qvtrelationcs_DomainCS13.setter
    def qvtrelationcs_DomainCS13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtrelationcs_DomainCS__qvtrelationcs_DomainCS13", None)
        self.__qvtrelationcs_DomainCS13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qvtrelationcs_ExpCS14"):
                opp_val = getattr(old_value, "qvtrelationcs_ExpCS14", None)
                if opp_val == self:
                    setattr(old_value, "qvtrelationcs_ExpCS14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qvtrelationcs_ExpCS14"):
                opp_val = getattr(value, "qvtrelationcs_ExpCS14", None)
                setattr(value, "qvtrelationcs_ExpCS14", self)

class qvtrelationcs_Variable:

    pass