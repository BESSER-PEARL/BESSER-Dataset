from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class TransformationCS:

    pass
class UnitCS:

    pass
class cst_OCLExpressionCS:

    pass
class WhereCS:

    pass
class RelationCS:

    pass
class QueryCS:

    pass
class KeyDeclCS:

    pass
class ModelDeclCS:

    pass
class cst_qvtrelation_EStructuralFeature:

    pass
class cst_AbstractDomainCS:

    pass
class cst_TemplateVariableCS:

    pass
class qvtrelation_cst_TemplateCS(cst_TemplateVariableCS, cst_OCLExpressionCS):

    pass
class qvtrelation_cst_PrimitiveTypeDomainCS(cst_AbstractDomainCS, cst_TemplateVariableCS):

    pass
class TypeCS:

    pass
class cst_qvtrelation_EClass:

    pass
class WhenCS:

    pass
class VarDeclarationCS:

    pass
class ParamDeclarationCS:

    pass
class AbstractDomainCS:

    pass
class qvtrelation_cst_DomainCS(AbstractDomainCS):

    def __init__(self, replace: bool, checkonly: bool, enforce: bool, qvtrelation_cst_DomainCS: "IdentifierCS" = None, qvtrelation_cst_DomainCS12: "TemplateCS" = None, qvtrelation_cst_DomainCS14: set["DefaultValueCS"] = None, qvtrelation_cst_DomainCS16: "OperationCallExpCS" = None, AbstractDomainCS: "qvtrelation_cst_RelationCS"):
        self.replace = replace
        self.checkonly = checkonly
        self.enforce = enforce
        self.qvtrelation_cst_DomainCS = qvtrelation_cst_DomainCS
        self.qvtrelation_cst_DomainCS12 = qvtrelation_cst_DomainCS12
        self.qvtrelation_cst_DomainCS14 = qvtrelation_cst_DomainCS14 if qvtrelation_cst_DomainCS14 is not None else set()
        self.qvtrelation_cst_DomainCS16 = qvtrelation_cst_DomainCS16
        
    @property
    def enforce(self) -> bool:
        return self.__enforce

    @enforce.setter
    def enforce(self, enforce: bool):
        self.__enforce = enforce

    @property
    def replace(self) -> bool:
        return self.__replace

    @replace.setter
    def replace(self, replace: bool):
        self.__replace = replace

    @property
    def checkonly(self) -> bool:
        return self.__checkonly

    @checkonly.setter
    def checkonly(self, checkonly: bool):
        self.__checkonly = checkonly

    @property
    def qvtrelation_cst_DomainCS16(self):
        return self.__qvtrelation_cst_DomainCS16

    @qvtrelation_cst_DomainCS16.setter
    def qvtrelation_cst_DomainCS16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtrelation_cst_DomainCS__qvtrelation_cst_DomainCS16", None)
        self.__qvtrelation_cst_DomainCS16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationCallExpCS"):
                opp_val = getattr(old_value, "OperationCallExpCS", None)
                if opp_val == self:
                    setattr(old_value, "OperationCallExpCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationCallExpCS"):
                opp_val = getattr(value, "OperationCallExpCS", None)
                setattr(value, "OperationCallExpCS", self)

    @property
    def qvtrelation_cst_DomainCS(self):
        return self.__qvtrelation_cst_DomainCS

    @qvtrelation_cst_DomainCS.setter
    def qvtrelation_cst_DomainCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtrelation_cst_DomainCS__qvtrelation_cst_DomainCS", None)
        self.__qvtrelation_cst_DomainCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IdentifierCS10"):
                opp_val = getattr(old_value, "IdentifierCS10", None)
                if opp_val == self:
                    setattr(old_value, "IdentifierCS10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IdentifierCS10"):
                opp_val = getattr(value, "IdentifierCS10", None)
                setattr(value, "IdentifierCS10", self)

    @property
    def qvtrelation_cst_DomainCS14(self):
        return self.__qvtrelation_cst_DomainCS14

    @qvtrelation_cst_DomainCS14.setter
    def qvtrelation_cst_DomainCS14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtrelation_cst_DomainCS__qvtrelation_cst_DomainCS14", None)
        self.__qvtrelation_cst_DomainCS14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DefaultValueCS"):
                    opp_val = getattr(item, "DefaultValueCS", None)
                    
                    if opp_val == self:
                        setattr(item, "DefaultValueCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DefaultValueCS"):
                    opp_val = getattr(item, "DefaultValueCS", None)
                    
                    setattr(item, "DefaultValueCS", self)
                    

    @property
    def qvtrelation_cst_DomainCS12(self):
        return self.__qvtrelation_cst_DomainCS12

    @qvtrelation_cst_DomainCS12.setter
    def qvtrelation_cst_DomainCS12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtrelation_cst_DomainCS__qvtrelation_cst_DomainCS12", None)
        self.__qvtrelation_cst_DomainCS12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TemplateCS"):
                opp_val = getattr(old_value, "TemplateCS", None)
                if opp_val == self:
                    setattr(old_value, "TemplateCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TemplateCS"):
                opp_val = getattr(value, "TemplateCS", None)
                setattr(value, "TemplateCS", self)

class OCLExpressionCS:

    pass
class IdentifierCS:

    pass
class cst_qvtrelation_EClassifier:

    pass
class IdentifiedCS:

    pass
class qvtrelation_cst_TemplateVariableCS(IdentifiedCS):

    pass
class PropertyTemplateCS:

    pass
class TemplateCS:

    pass
class qvtrelation_cst_CollectionTemplateCS(TemplateCS):

    pass
class qvtrelation_cst_ObjectTemplateCS(TemplateCS):

    pass
class CSTNode:

    pass
class qvtrelation_cst_TransformationCS(CSTNode):

    pass
class qvtrelation_cst_WhereCS(CSTNode):

    pass
class qvtrelation_cst_UnitCS(CSTNode):

    pass
class qvtrelation_cst_QueryCS(CSTNode):

    pass
class qvtrelation_cst_PropertyTemplateCS(CSTNode):

    def __init__(self, opposite: bool, qvtrelation_cst_PropertyTemplateCS: "IdentifiedCS" = None, qvtrelation_cst_PropertyTemplateCS36: "OCLExpressionCS" = None, qvtrelation_cst_PropertyTemplateCS39: "cst_qvtrelation_EStructuralFeature" = None):
        self.opposite = opposite
        self.qvtrelation_cst_PropertyTemplateCS = qvtrelation_cst_PropertyTemplateCS
        self.qvtrelation_cst_PropertyTemplateCS36 = qvtrelation_cst_PropertyTemplateCS36
        self.qvtrelation_cst_PropertyTemplateCS39 = qvtrelation_cst_PropertyTemplateCS39
        
    @property
    def opposite(self) -> bool:
        return self.__opposite

    @opposite.setter
    def opposite(self, opposite: bool):
        self.__opposite = opposite

    @property
    def qvtrelation_cst_PropertyTemplateCS36(self):
        return self.__qvtrelation_cst_PropertyTemplateCS36

    @qvtrelation_cst_PropertyTemplateCS36.setter
    def qvtrelation_cst_PropertyTemplateCS36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtrelation_cst_PropertyTemplateCS__qvtrelation_cst_PropertyTemplateCS36", None)
        self.__qvtrelation_cst_PropertyTemplateCS36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCLExpressionCS37"):
                opp_val = getattr(old_value, "OCLExpressionCS37", None)
                if opp_val == self:
                    setattr(old_value, "OCLExpressionCS37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCLExpressionCS37"):
                opp_val = getattr(value, "OCLExpressionCS37", None)
                setattr(value, "OCLExpressionCS37", self)

    @property
    def qvtrelation_cst_PropertyTemplateCS(self):
        return self.__qvtrelation_cst_PropertyTemplateCS

    @qvtrelation_cst_PropertyTemplateCS.setter
    def qvtrelation_cst_PropertyTemplateCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtrelation_cst_PropertyTemplateCS__qvtrelation_cst_PropertyTemplateCS", None)
        self.__qvtrelation_cst_PropertyTemplateCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IdentifiedCS34"):
                opp_val = getattr(old_value, "IdentifiedCS34", None)
                if opp_val == self:
                    setattr(old_value, "IdentifiedCS34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IdentifiedCS34"):
                opp_val = getattr(value, "IdentifiedCS34", None)
                setattr(value, "IdentifiedCS34", self)

    @property
    def qvtrelation_cst_PropertyTemplateCS39(self):
        return self.__qvtrelation_cst_PropertyTemplateCS39

    @qvtrelation_cst_PropertyTemplateCS39.setter
    def qvtrelation_cst_PropertyTemplateCS39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtrelation_cst_PropertyTemplateCS__qvtrelation_cst_PropertyTemplateCS39", None)
        self.__qvtrelation_cst_PropertyTemplateCS39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cst_qvtrelation_EStructuralFeature"):
                opp_val = getattr(old_value, "cst_qvtrelation_EStructuralFeature", None)
                if opp_val == self:
                    setattr(old_value, "cst_qvtrelation_EStructuralFeature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cst_qvtrelation_EStructuralFeature"):
                opp_val = getattr(value, "cst_qvtrelation_EStructuralFeature", None)
                setattr(value, "cst_qvtrelation_EStructuralFeature", self)

class qvtrelation_cst_ParamDeclarationCS(CSTNode):

    pass
class qvtrelation_cst_WhenCS(CSTNode):

    pass
class qvtrelation_cst_RelationCS(CSTNode):

    def __init__(self, top: bool, qvtrelation_cst_RelationCS: "IdentifierCS" = None, qvtrelation_cst_RelationCS53: "IdentifierCS" = None, qvtrelation_cst_RelationCS56: set["VarDeclarationCS"] = None, qvtrelation_cst_RelationCS58: set["AbstractDomainCS"] = None, qvtrelation_cst_RelationCS60: "WhenCS" = None, qvtrelation_cst_RelationCS62: "WhereCS" = None):
        self.top = top
        self.qvtrelation_cst_RelationCS = qvtrelation_cst_RelationCS
        self.qvtrelation_cst_RelationCS53 = qvtrelation_cst_RelationCS53
        self.qvtrelation_cst_RelationCS56 = qvtrelation_cst_RelationCS56 if qvtrelation_cst_RelationCS56 is not None else set()
        self.qvtrelation_cst_RelationCS58 = qvtrelation_cst_RelationCS58 if qvtrelation_cst_RelationCS58 is not None else set()
        self.qvtrelation_cst_RelationCS60 = qvtrelation_cst_RelationCS60
        self.qvtrelation_cst_RelationCS62 = qvtrelation_cst_RelationCS62
        
    @property
    def top(self) -> bool:
        return self.__top

    @top.setter
    def top(self, top: bool):
        self.__top = top

    @property
    def qvtrelation_cst_RelationCS62(self):
        return self.__qvtrelation_cst_RelationCS62

    @qvtrelation_cst_RelationCS62.setter
    def qvtrelation_cst_RelationCS62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtrelation_cst_RelationCS__qvtrelation_cst_RelationCS62", None)
        self.__qvtrelation_cst_RelationCS62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WhereCS"):
                opp_val = getattr(old_value, "WhereCS", None)
                if opp_val == self:
                    setattr(old_value, "WhereCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WhereCS"):
                opp_val = getattr(value, "WhereCS", None)
                setattr(value, "WhereCS", self)

    @property
    def qvtrelation_cst_RelationCS56(self):
        return self.__qvtrelation_cst_RelationCS56

    @qvtrelation_cst_RelationCS56.setter
    def qvtrelation_cst_RelationCS56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtrelation_cst_RelationCS__qvtrelation_cst_RelationCS56", None)
        self.__qvtrelation_cst_RelationCS56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VarDeclarationCS"):
                    opp_val = getattr(item, "VarDeclarationCS", None)
                    
                    if opp_val == self:
                        setattr(item, "VarDeclarationCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VarDeclarationCS"):
                    opp_val = getattr(item, "VarDeclarationCS", None)
                    
                    setattr(item, "VarDeclarationCS", self)
                    

    @property
    def qvtrelation_cst_RelationCS60(self):
        return self.__qvtrelation_cst_RelationCS60

    @qvtrelation_cst_RelationCS60.setter
    def qvtrelation_cst_RelationCS60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtrelation_cst_RelationCS__qvtrelation_cst_RelationCS60", None)
        self.__qvtrelation_cst_RelationCS60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WhenCS"):
                opp_val = getattr(old_value, "WhenCS", None)
                if opp_val == self:
                    setattr(old_value, "WhenCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WhenCS"):
                opp_val = getattr(value, "WhenCS", None)
                setattr(value, "WhenCS", self)

    @property
    def qvtrelation_cst_RelationCS(self):
        return self.__qvtrelation_cst_RelationCS

    @qvtrelation_cst_RelationCS.setter
    def qvtrelation_cst_RelationCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtrelation_cst_RelationCS__qvtrelation_cst_RelationCS", None)
        self.__qvtrelation_cst_RelationCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IdentifierCS51"):
                opp_val = getattr(old_value, "IdentifierCS51", None)
                if opp_val == self:
                    setattr(old_value, "IdentifierCS51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IdentifierCS51"):
                opp_val = getattr(value, "IdentifierCS51", None)
                setattr(value, "IdentifierCS51", self)

    @property
    def qvtrelation_cst_RelationCS53(self):
        return self.__qvtrelation_cst_RelationCS53

    @qvtrelation_cst_RelationCS53.setter
    def qvtrelation_cst_RelationCS53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtrelation_cst_RelationCS__qvtrelation_cst_RelationCS53", None)
        self.__qvtrelation_cst_RelationCS53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IdentifierCS54"):
                opp_val = getattr(old_value, "IdentifierCS54", None)
                if opp_val == self:
                    setattr(old_value, "IdentifierCS54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IdentifierCS54"):
                opp_val = getattr(value, "IdentifierCS54", None)
                setattr(value, "IdentifierCS54", self)

    @property
    def qvtrelation_cst_RelationCS58(self):
        return self.__qvtrelation_cst_RelationCS58

    @qvtrelation_cst_RelationCS58.setter
    def qvtrelation_cst_RelationCS58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtrelation_cst_RelationCS__qvtrelation_cst_RelationCS58", None)
        self.__qvtrelation_cst_RelationCS58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractDomainCS"):
                    opp_val = getattr(item, "AbstractDomainCS", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractDomainCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractDomainCS"):
                    opp_val = getattr(item, "AbstractDomainCS", None)
                    
                    setattr(item, "AbstractDomainCS", self)
                    

class qvtrelation_cst_VarDeclarationCS(CSTNode):

    pass
class qvtrelation_cst_DefaultValueCS(CSTNode):

    pass
class qvtrelation_cst_TopLevelCS(CSTNode):

    pass
class qvtrelation_cst_AbstractDomainCS(CSTNode):

    pass
class qvtrelation_cst_ModelDeclCS(CSTNode):

    pass
class PathNameCS:

    pass
class qvtrelation_cst_KeyDeclCS(CSTNode):

    pass
class OperationCallExpCS:

    pass
class DefaultValueCS:

    pass