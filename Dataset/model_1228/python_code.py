from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class cst_IHasName:

    pass
class cst_CSTNode:

    pass
class qvtcore_cst_QueryCS(cst_IHasName, cst_CSTNode):

    pass
class DirectionCS:

    pass
class qvtcore_cst_TransformationCS(cst_CSTNode, cst_IHasName):

    pass
class QueryCS:

    pass
class TransformationCS:

    pass
class RealizeableVariableCS:

    pass
class qvtcore_cst_UnrealizedVariableCS(RealizeableVariableCS):

    pass
class qvtcore_cst_RealizedVariableCS(RealizeableVariableCS):

    pass
class ParamDeclarationCS:

    pass
class UnrealizedVariableCS:

    pass
class TypeCS:

    pass
class DomainCS:

    pass
class MappingCS:

    pass
class OperationCallExpCS:

    pass
class CSTNode:

    pass
class qvtcore_cst_TopLevelCS(CSTNode):

    pass
class qvtcore_cst_ParamDeclarationCS(CSTNode):

    pass
class qvtcore_cst_PatternCS(CSTNode):

    pass
class qvtcore_cst_EnforcementOperationCS(CSTNode):

    def __init__(self, deletion: bool, qvtcore_cst_EnforcementOperationCS: "OperationCallExpCS" = None):
        self.deletion = deletion
        self.qvtcore_cst_EnforcementOperationCS = qvtcore_cst_EnforcementOperationCS
        
    @property
    def deletion(self) -> bool:
        return self.__deletion

    @deletion.setter
    def deletion(self, deletion: bool):
        self.__deletion = deletion

    @property
    def qvtcore_cst_EnforcementOperationCS(self):
        return self.__qvtcore_cst_EnforcementOperationCS

    @qvtcore_cst_EnforcementOperationCS.setter
    def qvtcore_cst_EnforcementOperationCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtcore_cst_EnforcementOperationCS__qvtcore_cst_EnforcementOperationCS", None)
        self.__qvtcore_cst_EnforcementOperationCS = value
        
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

class AreaCS:

    pass
class qvtcore_cst_DomainCS(AreaCS):

    def __init__(self, check: bool, enforce: bool):
        self.check = check
        self.enforce = enforce
        
    @property
    def enforce(self) -> bool:
        return self.__enforce

    @enforce.setter
    def enforce(self, enforce: bool):
        self.__enforce = enforce

    @property
    def check(self) -> bool:
        return self.__check

    @check.setter
    def check(self, check: bool):
        self.__check = check

class IdentifierCS:

    pass
class PathNameCS:

    pass
class RealizedVariableCS:

    pass
class EnforcementOperationCS:

    pass
class PatternCS:

    pass
class qvtcore_cst_GuardPatternCS(PatternCS):

    pass
class qvtcore_cst_BottomPatternCS(PatternCS):

    pass
class OCLExpressionCS:

    pass
class qvtcore_cst_AssignmentCS(OCLExpressionCS):

    def __init__(self, default: bool, qvtcore_cst_AssignmentCS: "OCLExpressionCS" = None, qvtcore_cst_AssignmentCS5: "OCLExpressionCS" = None, OCLExpressionCS31: "qvtcore_cst_PatternCS", OCLExpressionCS37: "qvtcore_cst_QueryCS", OCLExpressionCS: "qvtcore_cst_AssignmentCS", OCLExpressionCS6: "qvtcore_cst_AssignmentCS"):
        self.default = default
        self.qvtcore_cst_AssignmentCS = qvtcore_cst_AssignmentCS
        self.qvtcore_cst_AssignmentCS5 = qvtcore_cst_AssignmentCS5
        
    @property
    def default(self) -> bool:
        return self.__default

    @default.setter
    def default(self, default: bool):
        self.__default = default

    @property
    def qvtcore_cst_AssignmentCS5(self):
        return self.__qvtcore_cst_AssignmentCS5

    @qvtcore_cst_AssignmentCS5.setter
    def qvtcore_cst_AssignmentCS5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtcore_cst_AssignmentCS__qvtcore_cst_AssignmentCS5", None)
        self.__qvtcore_cst_AssignmentCS5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCLExpressionCS6"):
                opp_val = getattr(old_value, "OCLExpressionCS6", None)
                if opp_val == self:
                    setattr(old_value, "OCLExpressionCS6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCLExpressionCS6"):
                opp_val = getattr(value, "OCLExpressionCS6", None)
                setattr(value, "OCLExpressionCS6", self)

    @property
    def qvtcore_cst_AssignmentCS(self):
        return self.__qvtcore_cst_AssignmentCS

    @qvtcore_cst_AssignmentCS.setter
    def qvtcore_cst_AssignmentCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtcore_cst_AssignmentCS__qvtcore_cst_AssignmentCS", None)
        self.__qvtcore_cst_AssignmentCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCLExpressionCS"):
                opp_val = getattr(old_value, "OCLExpressionCS", None)
                if opp_val == self:
                    setattr(old_value, "OCLExpressionCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCLExpressionCS"):
                opp_val = getattr(value, "OCLExpressionCS", None)
                setattr(value, "OCLExpressionCS", self)

class BottomPatternCS:

    pass
class GuardPatternCS:

    pass
class IdentifiedCS:

    pass
class qvtcore_cst_RealizeableVariableCS(IdentifiedCS):

    pass
class qvtcore_cst_MappingCS(IdentifiedCS):

    pass
class qvtcore_cst_DirectionCS(IdentifiedCS):

    pass
class qvtcore_cst_AreaCS(IdentifiedCS):

    pass