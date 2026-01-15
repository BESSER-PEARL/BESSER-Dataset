from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class TrgRenMapping:

    pass
class jointPackage_Ecore2Maude_TrgOpTypedMapping(TrgRenMapping):

    def __init__(self, to: str, atts: str, jointPackage_Ecore2Maude_TrgOpTypedMapping: "jointPackage_Ecore2Maude_TrgOperation" = None):
        self.to = to
        self.atts = atts
        self.jointPackage_Ecore2Maude_TrgOpTypedMapping = jointPackage_Ecore2Maude_TrgOpTypedMapping
        
    @property
    def atts(self) -> str:
        return self.__atts

    @atts.setter
    def atts(self, atts: str):
        self.__atts = atts

    @property
    def to(self) -> str:
        return self.__to

    @to.setter
    def to(self, to: str):
        self.__to = to

    @property
    def jointPackage_Ecore2Maude_TrgOpTypedMapping(self):
        return self.__jointPackage_Ecore2Maude_TrgOpTypedMapping

    @jointPackage_Ecore2Maude_TrgOpTypedMapping.setter
    def jointPackage_Ecore2Maude_TrgOpTypedMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_TrgOpTypedMapping__jointPackage_Ecore2Maude_TrgOpTypedMapping", None)
        self.__jointPackage_Ecore2Maude_TrgOpTypedMapping = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jointPackage_Ecore2Maude_TrgOperation150"):
                opp_val = getattr(old_value, "jointPackage_Ecore2Maude_TrgOperation150", None)
                if opp_val == self:
                    setattr(old_value, "jointPackage_Ecore2Maude_TrgOperation150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jointPackage_Ecore2Maude_TrgOperation150"):
                opp_val = getattr(value, "jointPackage_Ecore2Maude_TrgOperation150", None)
                setattr(value, "jointPackage_Ecore2Maude_TrgOperation150", self)

class jointPackage_Ecore2Maude_TrgSortMapping(TrgRenMapping):

    def __init__(self, to: str, jointPackage_Ecore2Maude_TrgSortMapping: "jointPackage_Ecore2Maude_TrgSort" = None):
        self.to = to
        self.jointPackage_Ecore2Maude_TrgSortMapping = jointPackage_Ecore2Maude_TrgSortMapping
        
    @property
    def to(self) -> str:
        return self.__to

    @to.setter
    def to(self, to: str):
        self.__to = to

    @property
    def jointPackage_Ecore2Maude_TrgSortMapping(self):
        return self.__jointPackage_Ecore2Maude_TrgSortMapping

    @jointPackage_Ecore2Maude_TrgSortMapping.setter
    def jointPackage_Ecore2Maude_TrgSortMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_TrgSortMapping__jointPackage_Ecore2Maude_TrgSortMapping", None)
        self.__jointPackage_Ecore2Maude_TrgSortMapping = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jointPackage_Ecore2Maude_TrgSort148"):
                opp_val = getattr(old_value, "jointPackage_Ecore2Maude_TrgSort148", None)
                if opp_val == self:
                    setattr(old_value, "jointPackage_Ecore2Maude_TrgSort148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jointPackage_Ecore2Maude_TrgSort148"):
                opp_val = getattr(value, "jointPackage_Ecore2Maude_TrgSort148", None)
                setattr(value, "jointPackage_Ecore2Maude_TrgSort148", self)

class TrgViewMapping:

    pass
class jointPackage_Ecore2Maude_TrgTermMapping(TrgViewMapping):

    pass
class jointPackage_Ecore2Maude_TrgViewMapping(ABC):

    pass
class jointPackage_Ecore2Maude_TrgLabelMapping(TrgRenMapping):

    def __init__(self, from: str, to: str):
        self.from = from
        self.to = to
        
    @property
    def from(self) -> str:
        return self.__from

    @from.setter
    def from(self, from: str):
        self.__from = from

    @property
    def to(self) -> str:
        return self.__to

    @to.setter
    def to(self, to: str):
        self.__to = to

class jointPackage_Ecore2Maude_TrgOpMapping(TrgRenMapping):

    def __init__(self, to: str, jointPackage_Ecore2Maude_TrgOpMapping: "jointPackage_Ecore2Maude_TrgOperation" = None):
        self.to = to
        self.jointPackage_Ecore2Maude_TrgOpMapping = jointPackage_Ecore2Maude_TrgOpMapping
        
    @property
    def to(self) -> str:
        return self.__to

    @to.setter
    def to(self, to: str):
        self.__to = to

    @property
    def jointPackage_Ecore2Maude_TrgOpMapping(self):
        return self.__jointPackage_Ecore2Maude_TrgOpMapping

    @jointPackage_Ecore2Maude_TrgOpMapping.setter
    def jointPackage_Ecore2Maude_TrgOpMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_TrgOpMapping__jointPackage_Ecore2Maude_TrgOpMapping", None)
        self.__jointPackage_Ecore2Maude_TrgOpMapping = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jointPackage_Ecore2Maude_TrgOperation152"):
                opp_val = getattr(old_value, "jointPackage_Ecore2Maude_TrgOperation152", None)
                if opp_val == self:
                    setattr(old_value, "jointPackage_Ecore2Maude_TrgOperation152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jointPackage_Ecore2Maude_TrgOperation152"):
                opp_val = getattr(value, "jointPackage_Ecore2Maude_TrgOperation152", None)
                setattr(value, "jointPackage_Ecore2Maude_TrgOperation152", self)

class TrgCondition:

    pass
class jointPackage_Ecore2Maude_TrgRewriteCond(TrgCondition):

    pass
class jointPackage_Ecore2Maude_TrgEquationalCond(TrgCondition):

    pass
class jointPackage_Ecore2Maude_TrgCondition(ABC):

    pass
class TrgTerm:

    pass
class jointPackage_Ecore2Maude_TrgRecTerm(TrgTerm):

    def __init__(self, op: str, jointPackage_Ecore2Maude_TrgRecTerm: set["jointPackage_Ecore2Maude_TrgTerm"] = None):
        self.op = op
        self.jointPackage_Ecore2Maude_TrgRecTerm = jointPackage_Ecore2Maude_TrgRecTerm if jointPackage_Ecore2Maude_TrgRecTerm is not None else set()
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def jointPackage_Ecore2Maude_TrgRecTerm(self):
        return self.__jointPackage_Ecore2Maude_TrgRecTerm

    @jointPackage_Ecore2Maude_TrgRecTerm.setter
    def jointPackage_Ecore2Maude_TrgRecTerm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_TrgRecTerm__jointPackage_Ecore2Maude_TrgRecTerm", None)
        self.__jointPackage_Ecore2Maude_TrgRecTerm = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jointPackage_Ecore2Maude_TrgTerm133"):
                    opp_val = getattr(item, "jointPackage_Ecore2Maude_TrgTerm133", None)
                    
                    if opp_val == self:
                        setattr(item, "jointPackage_Ecore2Maude_TrgTerm133", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jointPackage_Ecore2Maude_TrgTerm133"):
                    opp_val = getattr(item, "jointPackage_Ecore2Maude_TrgTerm133", None)
                    
                    setattr(item, "jointPackage_Ecore2Maude_TrgTerm133", self)
                    

class jointPackage_Ecore2Maude_TrgVariable(TrgTerm):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class jointPackage_Ecore2Maude_TrgConstant(TrgTerm):

    def __init__(self, op: str):
        self.op = op
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

class TrgType:

    pass
class jointPackage_Ecore2Maude_TrgType(ABC):

    def __init__(self, name: str, jointPackage_Ecore2Maude_TrgType131: "jointPackage_Ecore2Maude_TrgTerm" = None, jointPackage_Ecore2Maude_TrgType: "jointPackage_Ecore2Maude_TrgOperation" = None, jointPackage_Ecore2Maude_TrgType122: "jointPackage_Ecore2Maude_TrgOperation" = None):
        self.name = name
        self.jointPackage_Ecore2Maude_TrgType131 = jointPackage_Ecore2Maude_TrgType131
        self.jointPackage_Ecore2Maude_TrgType = jointPackage_Ecore2Maude_TrgType
        self.jointPackage_Ecore2Maude_TrgType122 = jointPackage_Ecore2Maude_TrgType122
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def jointPackage_Ecore2Maude_TrgType131(self):
        return self.__jointPackage_Ecore2Maude_TrgType131

    @jointPackage_Ecore2Maude_TrgType131.setter
    def jointPackage_Ecore2Maude_TrgType131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_TrgType__jointPackage_Ecore2Maude_TrgType131", None)
        self.__jointPackage_Ecore2Maude_TrgType131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jointPackage_Ecore2Maude_TrgTerm130"):
                opp_val = getattr(old_value, "jointPackage_Ecore2Maude_TrgTerm130", None)
                if opp_val == self:
                    setattr(old_value, "jointPackage_Ecore2Maude_TrgTerm130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jointPackage_Ecore2Maude_TrgTerm130"):
                opp_val = getattr(value, "jointPackage_Ecore2Maude_TrgTerm130", None)
                setattr(value, "jointPackage_Ecore2Maude_TrgTerm130", self)

    @property
    def jointPackage_Ecore2Maude_TrgType122(self):
        return self.__jointPackage_Ecore2Maude_TrgType122

    @jointPackage_Ecore2Maude_TrgType122.setter
    def jointPackage_Ecore2Maude_TrgType122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_TrgType__jointPackage_Ecore2Maude_TrgType122", None)
        self.__jointPackage_Ecore2Maude_TrgType122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jointPackage_Ecore2Maude_TrgOperation121"):
                opp_val = getattr(old_value, "jointPackage_Ecore2Maude_TrgOperation121", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jointPackage_Ecore2Maude_TrgOperation121"):
                opp_val = getattr(value, "jointPackage_Ecore2Maude_TrgOperation121", None)
                if opp_val is None:
                    setattr(value, "jointPackage_Ecore2Maude_TrgOperation121", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jointPackage_Ecore2Maude_TrgType(self):
        return self.__jointPackage_Ecore2Maude_TrgType

    @jointPackage_Ecore2Maude_TrgType.setter
    def jointPackage_Ecore2Maude_TrgType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_TrgType__jointPackage_Ecore2Maude_TrgType", None)
        self.__jointPackage_Ecore2Maude_TrgType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jointPackage_Ecore2Maude_TrgOperation"):
                opp_val = getattr(old_value, "jointPackage_Ecore2Maude_TrgOperation", None)
                if opp_val == self:
                    setattr(old_value, "jointPackage_Ecore2Maude_TrgOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jointPackage_Ecore2Maude_TrgOperation"):
                opp_val = getattr(value, "jointPackage_Ecore2Maude_TrgOperation", None)
                setattr(value, "jointPackage_Ecore2Maude_TrgOperation", self)

class TrgModElement:

    pass
class jointPackage_Ecore2Maude_TrgStatement(TrgModElement):

    def __init__(self, label: str, atts: str, jointPackage_Ecore2Maude_TrgStatement: set["jointPackage_Ecore2Maude_TrgCondition"] = None):
        self.label = label
        self.atts = atts
        self.jointPackage_Ecore2Maude_TrgStatement = jointPackage_Ecore2Maude_TrgStatement if jointPackage_Ecore2Maude_TrgStatement is not None else set()
        
    @property
    def atts(self) -> str:
        return self.__atts

    @atts.setter
    def atts(self, atts: str):
        self.__atts = atts

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def jointPackage_Ecore2Maude_TrgStatement(self):
        return self.__jointPackage_Ecore2Maude_TrgStatement

    @jointPackage_Ecore2Maude_TrgStatement.setter
    def jointPackage_Ecore2Maude_TrgStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_TrgStatement__jointPackage_Ecore2Maude_TrgStatement", None)
        self.__jointPackage_Ecore2Maude_TrgStatement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jointPackage_Ecore2Maude_TrgCondition"):
                    opp_val = getattr(item, "jointPackage_Ecore2Maude_TrgCondition", None)
                    
                    if opp_val == self:
                        setattr(item, "jointPackage_Ecore2Maude_TrgCondition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jointPackage_Ecore2Maude_TrgCondition"):
                    opp_val = getattr(item, "jointPackage_Ecore2Maude_TrgCondition", None)
                    
                    setattr(item, "jointPackage_Ecore2Maude_TrgCondition", self)
                    

class jointPackage_Ecore2Maude_TrgSubsortRel(TrgModElement):

    pass
class jointPackage_Ecore2Maude_TrgOperation(TrgModElement):

    def __init__(self, name: str, atts: str, jointPackage_Ecore2Maude_TrgOperation: "jointPackage_Ecore2Maude_TrgType" = None, jointPackage_Ecore2Maude_TrgOperation121: set["jointPackage_Ecore2Maude_TrgType"] = None, jointPackage_Ecore2Maude_TrgOperation152: "jointPackage_Ecore2Maude_TrgOpMapping" = None, jointPackage_Ecore2Maude_TrgOperation150: "jointPackage_Ecore2Maude_TrgOpTypedMapping" = None):
        self.name = name
        self.atts = atts
        self.jointPackage_Ecore2Maude_TrgOperation = jointPackage_Ecore2Maude_TrgOperation
        self.jointPackage_Ecore2Maude_TrgOperation121 = jointPackage_Ecore2Maude_TrgOperation121 if jointPackage_Ecore2Maude_TrgOperation121 is not None else set()
        self.jointPackage_Ecore2Maude_TrgOperation152 = jointPackage_Ecore2Maude_TrgOperation152
        self.jointPackage_Ecore2Maude_TrgOperation150 = jointPackage_Ecore2Maude_TrgOperation150
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def atts(self) -> str:
        return self.__atts

    @atts.setter
    def atts(self, atts: str):
        self.__atts = atts

    @property
    def jointPackage_Ecore2Maude_TrgOperation121(self):
        return self.__jointPackage_Ecore2Maude_TrgOperation121

    @jointPackage_Ecore2Maude_TrgOperation121.setter
    def jointPackage_Ecore2Maude_TrgOperation121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_TrgOperation__jointPackage_Ecore2Maude_TrgOperation121", None)
        self.__jointPackage_Ecore2Maude_TrgOperation121 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jointPackage_Ecore2Maude_TrgType122"):
                    opp_val = getattr(item, "jointPackage_Ecore2Maude_TrgType122", None)
                    
                    if opp_val == self:
                        setattr(item, "jointPackage_Ecore2Maude_TrgType122", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jointPackage_Ecore2Maude_TrgType122"):
                    opp_val = getattr(item, "jointPackage_Ecore2Maude_TrgType122", None)
                    
                    setattr(item, "jointPackage_Ecore2Maude_TrgType122", self)
                    

    @property
    def jointPackage_Ecore2Maude_TrgOperation(self):
        return self.__jointPackage_Ecore2Maude_TrgOperation

    @jointPackage_Ecore2Maude_TrgOperation.setter
    def jointPackage_Ecore2Maude_TrgOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_TrgOperation__jointPackage_Ecore2Maude_TrgOperation", None)
        self.__jointPackage_Ecore2Maude_TrgOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jointPackage_Ecore2Maude_TrgType"):
                opp_val = getattr(old_value, "jointPackage_Ecore2Maude_TrgType", None)
                if opp_val == self:
                    setattr(old_value, "jointPackage_Ecore2Maude_TrgType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jointPackage_Ecore2Maude_TrgType"):
                opp_val = getattr(value, "jointPackage_Ecore2Maude_TrgType", None)
                setattr(value, "jointPackage_Ecore2Maude_TrgType", self)

    @property
    def jointPackage_Ecore2Maude_TrgOperation152(self):
        return self.__jointPackage_Ecore2Maude_TrgOperation152

    @jointPackage_Ecore2Maude_TrgOperation152.setter
    def jointPackage_Ecore2Maude_TrgOperation152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_TrgOperation__jointPackage_Ecore2Maude_TrgOperation152", None)
        self.__jointPackage_Ecore2Maude_TrgOperation152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jointPackage_Ecore2Maude_TrgOpMapping"):
                opp_val = getattr(old_value, "jointPackage_Ecore2Maude_TrgOpMapping", None)
                if opp_val == self:
                    setattr(old_value, "jointPackage_Ecore2Maude_TrgOpMapping", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jointPackage_Ecore2Maude_TrgOpMapping"):
                opp_val = getattr(value, "jointPackage_Ecore2Maude_TrgOpMapping", None)
                setattr(value, "jointPackage_Ecore2Maude_TrgOpMapping", self)

    @property
    def jointPackage_Ecore2Maude_TrgOperation150(self):
        return self.__jointPackage_Ecore2Maude_TrgOperation150

    @jointPackage_Ecore2Maude_TrgOperation150.setter
    def jointPackage_Ecore2Maude_TrgOperation150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_TrgOperation__jointPackage_Ecore2Maude_TrgOperation150", None)
        self.__jointPackage_Ecore2Maude_TrgOperation150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jointPackage_Ecore2Maude_TrgOpTypedMapping"):
                opp_val = getattr(old_value, "jointPackage_Ecore2Maude_TrgOpTypedMapping", None)
                if opp_val == self:
                    setattr(old_value, "jointPackage_Ecore2Maude_TrgOpTypedMapping", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jointPackage_Ecore2Maude_TrgOpTypedMapping"):
                opp_val = getattr(value, "jointPackage_Ecore2Maude_TrgOpTypedMapping", None)
                setattr(value, "jointPackage_Ecore2Maude_TrgOpTypedMapping", self)

class jointPackage_Ecore2Maude_TrgModImportation(TrgModElement):

    pass
class TrgModule:

    pass
class jointPackage_Ecore2Maude_TrgSModule(TrgModule):

    pass
class jointPackage_Ecore2Maude_TrgFModule(TrgModule):

    pass
class jointPackage_Ecore2Maude_TrgKind(TrgType):

    pass
class jointPackage_Ecore2Maude_TrgRenMapping(TrgViewMapping):

    pass
class TrgModExpression:

    pass
class jointPackage_Ecore2Maude_TrgCompModExp(TrgModExpression):

    pass
class jointPackage_Ecore2Maude_TrgParameter(TrgModExpression):

    def __init__(self, label: str, jointPackage_Ecore2Maude_TrgParameter: "jointPackage_Ecore2Maude_TrgModExpression" = None, jointPackage_Ecore2Maude_TrgParameter104: "jointPackage_Ecore2Maude_TrgModule" = None):
        self.label = label
        self.jointPackage_Ecore2Maude_TrgParameter = jointPackage_Ecore2Maude_TrgParameter
        self.jointPackage_Ecore2Maude_TrgParameter104 = jointPackage_Ecore2Maude_TrgParameter104
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def jointPackage_Ecore2Maude_TrgParameter(self):
        return self.__jointPackage_Ecore2Maude_TrgParameter

    @jointPackage_Ecore2Maude_TrgParameter.setter
    def jointPackage_Ecore2Maude_TrgParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_TrgParameter__jointPackage_Ecore2Maude_TrgParameter", None)
        self.__jointPackage_Ecore2Maude_TrgParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jointPackage_Ecore2Maude_TrgModExpression98"):
                opp_val = getattr(old_value, "jointPackage_Ecore2Maude_TrgModExpression98", None)
                if opp_val == self:
                    setattr(old_value, "jointPackage_Ecore2Maude_TrgModExpression98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jointPackage_Ecore2Maude_TrgModExpression98"):
                opp_val = getattr(value, "jointPackage_Ecore2Maude_TrgModExpression98", None)
                setattr(value, "jointPackage_Ecore2Maude_TrgModExpression98", self)

    @property
    def jointPackage_Ecore2Maude_TrgParameter104(self):
        return self.__jointPackage_Ecore2Maude_TrgParameter104

    @jointPackage_Ecore2Maude_TrgParameter104.setter
    def jointPackage_Ecore2Maude_TrgParameter104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_TrgParameter__jointPackage_Ecore2Maude_TrgParameter104", None)
        self.__jointPackage_Ecore2Maude_TrgParameter104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jointPackage_Ecore2Maude_TrgModule103"):
                opp_val = getattr(old_value, "jointPackage_Ecore2Maude_TrgModule103", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jointPackage_Ecore2Maude_TrgModule103"):
                opp_val = getattr(value, "jointPackage_Ecore2Maude_TrgModule103", None)
                if opp_val is None:
                    setattr(value, "jointPackage_Ecore2Maude_TrgModule103", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jointPackage_Ecore2Maude_TrgRenModExp(TrgModExpression):

    pass
class jointPackage_Ecore2Maude_TrgTheoryIdModExp(TrgModExpression):

    pass
class jointPackage_Ecore2Maude_TrgModuleIdModExp(TrgModExpression):

    pass
class jointPackage_Ecore2Maude_TrgInstModExp(TrgModExpression):

    pass
class jointPackage_Ecore2Maude_TrgModExpression(ABC):

    pass
class TrgTheory:

    pass
class jointPackage_Ecore2Maude_TrgSTheory(TrgTheory):

    pass
class jointPackage_Ecore2Maude_TrgFTheory(TrgTheory):

    pass
class jointPackage_Ecore2Maude_TrgModElement(ABC):

    pass
class TrgMaudeTopEl:

    pass
class jointPackage_Ecore2Maude_TrgModule(TrgMaudeTopEl):

    pass
class jointPackage_Ecore2Maude_TrgView(TrgMaudeTopEl):

    pass
class jointPackage_Ecore2Maude_TrgTheory(TrgMaudeTopEl):

    pass
class jointPackage_Ecore2Maude_TrgSort(TrgType, TrgModElement):

    pass
class jointPackage_Ecore2Maude_TrgTerm(ABC):

    pass
class TrgStatement:

    pass
class jointPackage_Ecore2Maude_TrgEquation(TrgStatement):

    pass
class jointPackage_Ecore2Maude_TrgRule(TrgStatement):

    pass
class jointPackage_Ecore2Maude_TrgMembership(TrgStatement):

    pass
class jointPackage_Ecore2Maude_TrgMaudeTopEl(ABC):

    def __init__(self, name: str, jointPackage_Ecore2Maude_TrgMaudeTopEl: "jointPackage_Ecore2Maude_TrgMaudeSpec" = None, jointPackage_Ecore2Maude_TrgMaudeTopEl65: "jointPackage_Ecore2Maude_TrgMaudeSpec" = None):
        self.name = name
        self.jointPackage_Ecore2Maude_TrgMaudeTopEl = jointPackage_Ecore2Maude_TrgMaudeTopEl
        self.jointPackage_Ecore2Maude_TrgMaudeTopEl65 = jointPackage_Ecore2Maude_TrgMaudeTopEl65
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def jointPackage_Ecore2Maude_TrgMaudeTopEl65(self):
        return self.__jointPackage_Ecore2Maude_TrgMaudeTopEl65

    @jointPackage_Ecore2Maude_TrgMaudeTopEl65.setter
    def jointPackage_Ecore2Maude_TrgMaudeTopEl65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_TrgMaudeTopEl__jointPackage_Ecore2Maude_TrgMaudeTopEl65", None)
        self.__jointPackage_Ecore2Maude_TrgMaudeTopEl65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jointPackage_Ecore2Maude_TrgMaudeSpec64"):
                opp_val = getattr(old_value, "jointPackage_Ecore2Maude_TrgMaudeSpec64", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jointPackage_Ecore2Maude_TrgMaudeSpec64"):
                opp_val = getattr(value, "jointPackage_Ecore2Maude_TrgMaudeSpec64", None)
                if opp_val is None:
                    setattr(value, "jointPackage_Ecore2Maude_TrgMaudeSpec64", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jointPackage_Ecore2Maude_TrgMaudeTopEl(self):
        return self.__jointPackage_Ecore2Maude_TrgMaudeTopEl

    @jointPackage_Ecore2Maude_TrgMaudeTopEl.setter
    def jointPackage_Ecore2Maude_TrgMaudeTopEl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_TrgMaudeTopEl__jointPackage_Ecore2Maude_TrgMaudeTopEl", None)
        self.__jointPackage_Ecore2Maude_TrgMaudeTopEl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jointPackage_Ecore2Maude_TrgMaudeSpec"):
                opp_val = getattr(old_value, "jointPackage_Ecore2Maude_TrgMaudeSpec", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jointPackage_Ecore2Maude_TrgMaudeSpec"):
                opp_val = getattr(value, "jointPackage_Ecore2Maude_TrgMaudeSpec", None)
                if opp_val is None:
                    setattr(value, "jointPackage_Ecore2Maude_TrgMaudeSpec", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jointPackage_Ecore2Maude_TrgMaudeSpec:

    pass
class TrgEquationalCond:

    pass
class jointPackage_Ecore2Maude_TrgMatchingCond(TrgEquationalCond):

    pass
class jointPackage_Ecore2Maude_TrgBooleanCond(TrgEquationalCond):

    pass
class jointPackage_Ecore2Maude_TrgMembershipCond(TrgEquationalCond):

    pass
class SrcETypedElement:

    pass
class jointPackage_Ecore2Maude_SrcENamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class SrcEDataType:

    pass
class jointPackage_Ecore2Maude_SrcEEnum(SrcEDataType):

    def __init__(self, eEnum: set["jointPackage_Ecore2Maude_SrcEEnumLiteral"] = None, SrcEEnum: "jointPackage_Ecore2Maude_SrcEEnumLiteral" = None):
        self.eEnum = eEnum if eEnum is not None else set()
        self.SrcEEnum = SrcEEnum
        
    @property
    def eEnum(self):
        return self.__eEnum

    @eEnum.setter
    def eEnum(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEEnum__eEnum", None)
        self.__eEnum = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SrcEEnumLiteral"):
                    opp_val = getattr(item, "SrcEEnumLiteral", None)
                    
                    if opp_val == self:
                        setattr(item, "SrcEEnumLiteral", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SrcEEnumLiteral"):
                    opp_val = getattr(item, "SrcEEnumLiteral", None)
                    
                    setattr(item, "SrcEEnumLiteral", self)
                    

    @property
    def SrcEEnum(self):
        return self.__SrcEEnum

    @SrcEEnum.setter
    def SrcEEnum(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEEnum__SrcEEnum", None)
        self.__SrcEEnum = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eLiterals"):
                opp_val = getattr(old_value, "eLiterals", None)
                if opp_val == self:
                    setattr(old_value, "eLiterals", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eLiterals"):
                opp_val = getattr(value, "eLiterals", None)
                setattr(value, "eLiterals", self)

    def getEEnumLiteral(self, value: int) -> str:
        # TODO: Implement getEEnumLiteral method
        pass

    def getEEnumLiteral(self, name: str) -> str:
        # TODO: Implement getEEnumLiteral method
        pass

    def getEEnumLiteralByLiteral(self, literal: str) -> str:
        # TODO: Implement getEEnumLiteralByLiteral method
        pass

class jointPackage_Ecore2Maude_SrcEParameter(SrcETypedElement):

    pass
class SrcEClassifier:

    pass
class jointPackage_Ecore2Maude_SrcEClass(SrcEClassifier):

    def __init__(self, abstract: bool, interface: bool, eContainingClass32: set["jointPackage_Ecore2Maude_SrcEStructuralFeature"] = None, jointPackage_Ecore2Maude_SrcEClass: "jointPackage_Ecore2Maude_SrcEClass" = None, jointPackage_Ecore2Maude_SrcEClass4: set["jointPackage_Ecore2Maude_SrcEClass"] = None, eContainingClass: set["jointPackage_Ecore2Maude_SrcEOperation"] = None, jointPackage_Ecore2Maude_SrcEClass8: set["jointPackage_Ecore2Maude_SrcEAttribute"] = None, jointPackage_Ecore2Maude_SrcEClass11: set["jointPackage_Ecore2Maude_SrcEReference"] = None, jointPackage_Ecore2Maude_SrcEClass13: set["jointPackage_Ecore2Maude_SrcEReference"] = None, jointPackage_Ecore2Maude_SrcEClass16: set["jointPackage_Ecore2Maude_SrcEAttribute"] = None, jointPackage_Ecore2Maude_SrcEClass19: set["jointPackage_Ecore2Maude_SrcEReference"] = None, jointPackage_Ecore2Maude_SrcEClass22: set["jointPackage_Ecore2Maude_SrcEOperation"] = None, jointPackage_Ecore2Maude_SrcEClass24: set["jointPackage_Ecore2Maude_SrcEStructuralFeature"] = None, jointPackage_Ecore2Maude_SrcEClass27: "jointPackage_Ecore2Maude_SrcEClass" = None, jointPackage_Ecore2Maude_SrcEClass25: set["jointPackage_Ecore2Maude_SrcEClass"] = None, jointPackage_Ecore2Maude_SrcEClass29: "jointPackage_Ecore2Maude_SrcEAttribute" = None, SrcEClass: "jointPackage_Ecore2Maude_SrcEOperation" = None, SrcEClass59: "jointPackage_Ecore2Maude_SrcEStructuralFeature" = None, jointPackage_Ecore2Maude_SrcEClass54: "jointPackage_Ecore2Maude_SrcEReference" = None):
        self.abstract = abstract
        self.interface = interface
        self.eContainingClass32 = eContainingClass32 if eContainingClass32 is not None else set()
        self.jointPackage_Ecore2Maude_SrcEClass = jointPackage_Ecore2Maude_SrcEClass
        self.jointPackage_Ecore2Maude_SrcEClass4 = jointPackage_Ecore2Maude_SrcEClass4 if jointPackage_Ecore2Maude_SrcEClass4 is not None else set()
        self.eContainingClass = eContainingClass if eContainingClass is not None else set()
        self.jointPackage_Ecore2Maude_SrcEClass8 = jointPackage_Ecore2Maude_SrcEClass8 if jointPackage_Ecore2Maude_SrcEClass8 is not None else set()
        self.jointPackage_Ecore2Maude_SrcEClass11 = jointPackage_Ecore2Maude_SrcEClass11 if jointPackage_Ecore2Maude_SrcEClass11 is not None else set()
        self.jointPackage_Ecore2Maude_SrcEClass13 = jointPackage_Ecore2Maude_SrcEClass13 if jointPackage_Ecore2Maude_SrcEClass13 is not None else set()
        self.jointPackage_Ecore2Maude_SrcEClass16 = jointPackage_Ecore2Maude_SrcEClass16 if jointPackage_Ecore2Maude_SrcEClass16 is not None else set()
        self.jointPackage_Ecore2Maude_SrcEClass19 = jointPackage_Ecore2Maude_SrcEClass19 if jointPackage_Ecore2Maude_SrcEClass19 is not None else set()
        self.jointPackage_Ecore2Maude_SrcEClass22 = jointPackage_Ecore2Maude_SrcEClass22 if jointPackage_Ecore2Maude_SrcEClass22 is not None else set()
        self.jointPackage_Ecore2Maude_SrcEClass24 = jointPackage_Ecore2Maude_SrcEClass24 if jointPackage_Ecore2Maude_SrcEClass24 is not None else set()
        self.jointPackage_Ecore2Maude_SrcEClass27 = jointPackage_Ecore2Maude_SrcEClass27
        self.jointPackage_Ecore2Maude_SrcEClass25 = jointPackage_Ecore2Maude_SrcEClass25 if jointPackage_Ecore2Maude_SrcEClass25 is not None else set()
        self.jointPackage_Ecore2Maude_SrcEClass29 = jointPackage_Ecore2Maude_SrcEClass29
        self.SrcEClass = SrcEClass
        self.SrcEClass59 = SrcEClass59
        self.jointPackage_Ecore2Maude_SrcEClass54 = jointPackage_Ecore2Maude_SrcEClass54
        
    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def interface(self) -> bool:
        return self.__interface

    @interface.setter
    def interface(self, interface: bool):
        self.__interface = interface

    @property
    def jointPackage_Ecore2Maude_SrcEClass27(self):
        return self.__jointPackage_Ecore2Maude_SrcEClass27

    @jointPackage_Ecore2Maude_SrcEClass27.setter
    def jointPackage_Ecore2Maude_SrcEClass27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEClass__jointPackage_Ecore2Maude_SrcEClass27", None)
        self.__jointPackage_Ecore2Maude_SrcEClass27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jointPackage_Ecore2Maude_SrcEClass25"):
                opp_val = getattr(old_value, "jointPackage_Ecore2Maude_SrcEClass25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jointPackage_Ecore2Maude_SrcEClass25"):
                opp_val = getattr(value, "jointPackage_Ecore2Maude_SrcEClass25", None)
                if opp_val is None:
                    setattr(value, "jointPackage_Ecore2Maude_SrcEClass25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eContainingClass32(self):
        return self.__eContainingClass32

    @eContainingClass32.setter
    def eContainingClass32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEClass__eContainingClass32", None)
        self.__eContainingClass32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SrcEStructuralFeature"):
                    opp_val = getattr(item, "SrcEStructuralFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "SrcEStructuralFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SrcEStructuralFeature"):
                    opp_val = getattr(item, "SrcEStructuralFeature", None)
                    
                    setattr(item, "SrcEStructuralFeature", self)
                    

    @property
    def jointPackage_Ecore2Maude_SrcEClass29(self):
        return self.__jointPackage_Ecore2Maude_SrcEClass29

    @jointPackage_Ecore2Maude_SrcEClass29.setter
    def jointPackage_Ecore2Maude_SrcEClass29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEClass__jointPackage_Ecore2Maude_SrcEClass29", None)
        self.__jointPackage_Ecore2Maude_SrcEClass29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jointPackage_Ecore2Maude_SrcEAttribute30"):
                opp_val = getattr(old_value, "jointPackage_Ecore2Maude_SrcEAttribute30", None)
                if opp_val == self:
                    setattr(old_value, "jointPackage_Ecore2Maude_SrcEAttribute30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jointPackage_Ecore2Maude_SrcEAttribute30"):
                opp_val = getattr(value, "jointPackage_Ecore2Maude_SrcEAttribute30", None)
                setattr(value, "jointPackage_Ecore2Maude_SrcEAttribute30", self)

    @property
    def jointPackage_Ecore2Maude_SrcEClass24(self):
        return self.__jointPackage_Ecore2Maude_SrcEClass24

    @jointPackage_Ecore2Maude_SrcEClass24.setter
    def jointPackage_Ecore2Maude_SrcEClass24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEClass__jointPackage_Ecore2Maude_SrcEClass24", None)
        self.__jointPackage_Ecore2Maude_SrcEClass24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jointPackage_Ecore2Maude_SrcEStructuralFeature"):
                    opp_val = getattr(item, "jointPackage_Ecore2Maude_SrcEStructuralFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "jointPackage_Ecore2Maude_SrcEStructuralFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jointPackage_Ecore2Maude_SrcEStructuralFeature"):
                    opp_val = getattr(item, "jointPackage_Ecore2Maude_SrcEStructuralFeature", None)
                    
                    setattr(item, "jointPackage_Ecore2Maude_SrcEStructuralFeature", self)
                    

    @property
    def jointPackage_Ecore2Maude_SrcEClass(self):
        return self.__jointPackage_Ecore2Maude_SrcEClass

    @jointPackage_Ecore2Maude_SrcEClass.setter
    def jointPackage_Ecore2Maude_SrcEClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEClass__jointPackage_Ecore2Maude_SrcEClass", None)
        self.__jointPackage_Ecore2Maude_SrcEClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jointPackage_Ecore2Maude_SrcEClass4"):
                opp_val = getattr(old_value, "jointPackage_Ecore2Maude_SrcEClass4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jointPackage_Ecore2Maude_SrcEClass4"):
                opp_val = getattr(value, "jointPackage_Ecore2Maude_SrcEClass4", None)
                if opp_val is None:
                    setattr(value, "jointPackage_Ecore2Maude_SrcEClass4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jointPackage_Ecore2Maude_SrcEClass25(self):
        return self.__jointPackage_Ecore2Maude_SrcEClass25

    @jointPackage_Ecore2Maude_SrcEClass25.setter
    def jointPackage_Ecore2Maude_SrcEClass25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEClass__jointPackage_Ecore2Maude_SrcEClass25", None)
        self.__jointPackage_Ecore2Maude_SrcEClass25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jointPackage_Ecore2Maude_SrcEClass27"):
                    opp_val = getattr(item, "jointPackage_Ecore2Maude_SrcEClass27", None)
                    
                    if opp_val == self:
                        setattr(item, "jointPackage_Ecore2Maude_SrcEClass27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jointPackage_Ecore2Maude_SrcEClass27"):
                    opp_val = getattr(item, "jointPackage_Ecore2Maude_SrcEClass27", None)
                    
                    setattr(item, "jointPackage_Ecore2Maude_SrcEClass27", self)
                    

    @property
    def SrcEClass(self):
        return self.__SrcEClass

    @SrcEClass.setter
    def SrcEClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEClass__SrcEClass", None)
        self.__SrcEClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eOperations"):
                opp_val = getattr(old_value, "eOperations", None)
                if opp_val == self:
                    setattr(old_value, "eOperations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eOperations"):
                opp_val = getattr(value, "eOperations", None)
                setattr(value, "eOperations", self)

    @property
    def jointPackage_Ecore2Maude_SrcEClass4(self):
        return self.__jointPackage_Ecore2Maude_SrcEClass4

    @jointPackage_Ecore2Maude_SrcEClass4.setter
    def jointPackage_Ecore2Maude_SrcEClass4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEClass__jointPackage_Ecore2Maude_SrcEClass4", None)
        self.__jointPackage_Ecore2Maude_SrcEClass4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jointPackage_Ecore2Maude_SrcEClass"):
                    opp_val = getattr(item, "jointPackage_Ecore2Maude_SrcEClass", None)
                    
                    if opp_val == self:
                        setattr(item, "jointPackage_Ecore2Maude_SrcEClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jointPackage_Ecore2Maude_SrcEClass"):
                    opp_val = getattr(item, "jointPackage_Ecore2Maude_SrcEClass", None)
                    
                    setattr(item, "jointPackage_Ecore2Maude_SrcEClass", self)
                    

    @property
    def SrcEClass59(self):
        return self.__SrcEClass59

    @SrcEClass59.setter
    def SrcEClass59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEClass__SrcEClass59", None)
        self.__SrcEClass59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eStructuralFeatures"):
                opp_val = getattr(old_value, "eStructuralFeatures", None)
                if opp_val == self:
                    setattr(old_value, "eStructuralFeatures", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eStructuralFeatures"):
                opp_val = getattr(value, "eStructuralFeatures", None)
                setattr(value, "eStructuralFeatures", self)

    @property
    def jointPackage_Ecore2Maude_SrcEClass16(self):
        return self.__jointPackage_Ecore2Maude_SrcEClass16

    @jointPackage_Ecore2Maude_SrcEClass16.setter
    def jointPackage_Ecore2Maude_SrcEClass16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEClass__jointPackage_Ecore2Maude_SrcEClass16", None)
        self.__jointPackage_Ecore2Maude_SrcEClass16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jointPackage_Ecore2Maude_SrcEAttribute17"):
                    opp_val = getattr(item, "jointPackage_Ecore2Maude_SrcEAttribute17", None)
                    
                    if opp_val == self:
                        setattr(item, "jointPackage_Ecore2Maude_SrcEAttribute17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jointPackage_Ecore2Maude_SrcEAttribute17"):
                    opp_val = getattr(item, "jointPackage_Ecore2Maude_SrcEAttribute17", None)
                    
                    setattr(item, "jointPackage_Ecore2Maude_SrcEAttribute17", self)
                    

    @property
    def jointPackage_Ecore2Maude_SrcEClass11(self):
        return self.__jointPackage_Ecore2Maude_SrcEClass11

    @jointPackage_Ecore2Maude_SrcEClass11.setter
    def jointPackage_Ecore2Maude_SrcEClass11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEClass__jointPackage_Ecore2Maude_SrcEClass11", None)
        self.__jointPackage_Ecore2Maude_SrcEClass11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jointPackage_Ecore2Maude_SrcEReference"):
                    opp_val = getattr(item, "jointPackage_Ecore2Maude_SrcEReference", None)
                    
                    if opp_val == self:
                        setattr(item, "jointPackage_Ecore2Maude_SrcEReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jointPackage_Ecore2Maude_SrcEReference"):
                    opp_val = getattr(item, "jointPackage_Ecore2Maude_SrcEReference", None)
                    
                    setattr(item, "jointPackage_Ecore2Maude_SrcEReference", self)
                    

    @property
    def eContainingClass(self):
        return self.__eContainingClass

    @eContainingClass.setter
    def eContainingClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEClass__eContainingClass", None)
        self.__eContainingClass = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SrcEOperation"):
                    opp_val = getattr(item, "SrcEOperation", None)
                    
                    if opp_val == self:
                        setattr(item, "SrcEOperation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SrcEOperation"):
                    opp_val = getattr(item, "SrcEOperation", None)
                    
                    setattr(item, "SrcEOperation", self)
                    

    @property
    def jointPackage_Ecore2Maude_SrcEClass22(self):
        return self.__jointPackage_Ecore2Maude_SrcEClass22

    @jointPackage_Ecore2Maude_SrcEClass22.setter
    def jointPackage_Ecore2Maude_SrcEClass22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEClass__jointPackage_Ecore2Maude_SrcEClass22", None)
        self.__jointPackage_Ecore2Maude_SrcEClass22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jointPackage_Ecore2Maude_SrcEOperation"):
                    opp_val = getattr(item, "jointPackage_Ecore2Maude_SrcEOperation", None)
                    
                    if opp_val == self:
                        setattr(item, "jointPackage_Ecore2Maude_SrcEOperation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jointPackage_Ecore2Maude_SrcEOperation"):
                    opp_val = getattr(item, "jointPackage_Ecore2Maude_SrcEOperation", None)
                    
                    setattr(item, "jointPackage_Ecore2Maude_SrcEOperation", self)
                    

    @property
    def jointPackage_Ecore2Maude_SrcEClass8(self):
        return self.__jointPackage_Ecore2Maude_SrcEClass8

    @jointPackage_Ecore2Maude_SrcEClass8.setter
    def jointPackage_Ecore2Maude_SrcEClass8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEClass__jointPackage_Ecore2Maude_SrcEClass8", None)
        self.__jointPackage_Ecore2Maude_SrcEClass8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jointPackage_Ecore2Maude_SrcEAttribute9"):
                    opp_val = getattr(item, "jointPackage_Ecore2Maude_SrcEAttribute9", None)
                    
                    if opp_val == self:
                        setattr(item, "jointPackage_Ecore2Maude_SrcEAttribute9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jointPackage_Ecore2Maude_SrcEAttribute9"):
                    opp_val = getattr(item, "jointPackage_Ecore2Maude_SrcEAttribute9", None)
                    
                    setattr(item, "jointPackage_Ecore2Maude_SrcEAttribute9", self)
                    

    @property
    def jointPackage_Ecore2Maude_SrcEClass54(self):
        return self.__jointPackage_Ecore2Maude_SrcEClass54

    @jointPackage_Ecore2Maude_SrcEClass54.setter
    def jointPackage_Ecore2Maude_SrcEClass54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEClass__jointPackage_Ecore2Maude_SrcEClass54", None)
        self.__jointPackage_Ecore2Maude_SrcEClass54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jointPackage_Ecore2Maude_SrcEReference53"):
                opp_val = getattr(old_value, "jointPackage_Ecore2Maude_SrcEReference53", None)
                if opp_val == self:
                    setattr(old_value, "jointPackage_Ecore2Maude_SrcEReference53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jointPackage_Ecore2Maude_SrcEReference53"):
                opp_val = getattr(value, "jointPackage_Ecore2Maude_SrcEReference53", None)
                setattr(value, "jointPackage_Ecore2Maude_SrcEReference53", self)

    @property
    def jointPackage_Ecore2Maude_SrcEClass13(self):
        return self.__jointPackage_Ecore2Maude_SrcEClass13

    @jointPackage_Ecore2Maude_SrcEClass13.setter
    def jointPackage_Ecore2Maude_SrcEClass13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEClass__jointPackage_Ecore2Maude_SrcEClass13", None)
        self.__jointPackage_Ecore2Maude_SrcEClass13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jointPackage_Ecore2Maude_SrcEReference14"):
                    opp_val = getattr(item, "jointPackage_Ecore2Maude_SrcEReference14", None)
                    
                    if opp_val == self:
                        setattr(item, "jointPackage_Ecore2Maude_SrcEReference14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jointPackage_Ecore2Maude_SrcEReference14"):
                    opp_val = getattr(item, "jointPackage_Ecore2Maude_SrcEReference14", None)
                    
                    setattr(item, "jointPackage_Ecore2Maude_SrcEReference14", self)
                    

    @property
    def jointPackage_Ecore2Maude_SrcEClass19(self):
        return self.__jointPackage_Ecore2Maude_SrcEClass19

    @jointPackage_Ecore2Maude_SrcEClass19.setter
    def jointPackage_Ecore2Maude_SrcEClass19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEClass__jointPackage_Ecore2Maude_SrcEClass19", None)
        self.__jointPackage_Ecore2Maude_SrcEClass19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jointPackage_Ecore2Maude_SrcEReference20"):
                    opp_val = getattr(item, "jointPackage_Ecore2Maude_SrcEReference20", None)
                    
                    if opp_val == self:
                        setattr(item, "jointPackage_Ecore2Maude_SrcEReference20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jointPackage_Ecore2Maude_SrcEReference20"):
                    opp_val = getattr(item, "jointPackage_Ecore2Maude_SrcEReference20", None)
                    
                    setattr(item, "jointPackage_Ecore2Maude_SrcEReference20", self)
                    

    def getFeatureID(self, feature: SrcEStructuralFeature) -> int:
        # TODO: Implement getFeatureID method
        pass

    def isSuperTypeOf(self, someClass: str) -> bool:
        # TODO: Implement isSuperTypeOf method
        pass

    def getEStructuralFeature(self, featureName: str) -> SrcEStructuralFeature:
        # TODO: Implement getEStructuralFeature method
        pass

    def getFeatureCount(self) -> int:
        # TODO: Implement getFeatureCount method
        pass

    def getEStructuralFeature(self, featureID: int) -> SrcEStructuralFeature:
        # TODO: Implement getEStructuralFeature method
        pass

class jointPackage_Ecore2Maude_SrcEStructuralFeature(SrcETypedElement):

    def __init__(self, changeable: bool, volatile: bool, transient: bool, defaultValueLiteral: str, unsettable: bool, derived: bool, SrcEStructuralFeature: "jointPackage_Ecore2Maude_SrcEClass" = None, jointPackage_Ecore2Maude_SrcEStructuralFeature: "jointPackage_Ecore2Maude_SrcEClass" = None, eStructuralFeatures: "jointPackage_Ecore2Maude_SrcEClass" = None):
        self.changeable = changeable
        self.volatile = volatile
        self.transient = transient
        self.defaultValueLiteral = defaultValueLiteral
        self.unsettable = unsettable
        self.derived = derived
        self.SrcEStructuralFeature = SrcEStructuralFeature
        self.jointPackage_Ecore2Maude_SrcEStructuralFeature = jointPackage_Ecore2Maude_SrcEStructuralFeature
        self.eStructuralFeatures = eStructuralFeatures
        
    @property
    def transient(self) -> bool:
        return self.__transient

    @transient.setter
    def transient(self, transient: bool):
        self.__transient = transient

    @property
    def changeable(self) -> bool:
        return self.__changeable

    @changeable.setter
    def changeable(self, changeable: bool):
        self.__changeable = changeable

    @property
    def derived(self) -> bool:
        return self.__derived

    @derived.setter
    def derived(self, derived: bool):
        self.__derived = derived

    @property
    def defaultValueLiteral(self) -> str:
        return self.__defaultValueLiteral

    @defaultValueLiteral.setter
    def defaultValueLiteral(self, defaultValueLiteral: str):
        self.__defaultValueLiteral = defaultValueLiteral

    @property
    def volatile(self) -> bool:
        return self.__volatile

    @volatile.setter
    def volatile(self, volatile: bool):
        self.__volatile = volatile

    @property
    def unsettable(self) -> bool:
        return self.__unsettable

    @unsettable.setter
    def unsettable(self, unsettable: bool):
        self.__unsettable = unsettable

    @property
    def SrcEStructuralFeature(self):
        return self.__SrcEStructuralFeature

    @SrcEStructuralFeature.setter
    def SrcEStructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEStructuralFeature__SrcEStructuralFeature", None)
        self.__SrcEStructuralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eContainingClass32"):
                opp_val = getattr(old_value, "eContainingClass32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eContainingClass32"):
                opp_val = getattr(value, "eContainingClass32", None)
                if opp_val is None:
                    setattr(value, "eContainingClass32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eStructuralFeatures(self):
        return self.__eStructuralFeatures

    @eStructuralFeatures.setter
    def eStructuralFeatures(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEStructuralFeature__eStructuralFeatures", None)
        self.__eStructuralFeatures = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SrcEClass59"):
                opp_val = getattr(old_value, "SrcEClass59", None)
                if opp_val == self:
                    setattr(old_value, "SrcEClass59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SrcEClass59"):
                opp_val = getattr(value, "SrcEClass59", None)
                setattr(value, "SrcEClass59", self)

    @property
    def jointPackage_Ecore2Maude_SrcEStructuralFeature(self):
        return self.__jointPackage_Ecore2Maude_SrcEStructuralFeature

    @jointPackage_Ecore2Maude_SrcEStructuralFeature.setter
    def jointPackage_Ecore2Maude_SrcEStructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEStructuralFeature__jointPackage_Ecore2Maude_SrcEStructuralFeature", None)
        self.__jointPackage_Ecore2Maude_SrcEStructuralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jointPackage_Ecore2Maude_SrcEClass24"):
                opp_val = getattr(old_value, "jointPackage_Ecore2Maude_SrcEClass24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jointPackage_Ecore2Maude_SrcEClass24"):
                opp_val = getattr(value, "jointPackage_Ecore2Maude_SrcEClass24", None)
                if opp_val is None:
                    setattr(value, "jointPackage_Ecore2Maude_SrcEClass24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getFeatureID(self) -> int:
        # TODO: Implement getFeatureID method
        pass

class jointPackage_Ecore2Maude_SrcEOperation(SrcETypedElement):

    pass
class SrcENamedElement:

    pass
class jointPackage_Ecore2Maude_SrcETypedElement(SrcENamedElement):

    def __init__(self, ordered: bool, unique: bool, lowerBound: int, upperBound: int, many: bool, required: bool, jointPackage_Ecore2Maude_SrcETypedElement: "jointPackage_Ecore2Maude_SrcEClassifier" = None):
        self.ordered = ordered
        self.unique = unique
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.many = many
        self.required = required
        self.jointPackage_Ecore2Maude_SrcETypedElement = jointPackage_Ecore2Maude_SrcETypedElement
        
    @property
    def ordered(self) -> bool:
        return self.__ordered

    @ordered.setter
    def ordered(self, ordered: bool):
        self.__ordered = ordered

    @property
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

    @property
    def required(self) -> bool:
        return self.__required

    @required.setter
    def required(self, required: bool):
        self.__required = required

    @property
    def unique(self) -> bool:
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique

    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

    @property
    def upperBound(self) -> int:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound

    @property
    def jointPackage_Ecore2Maude_SrcETypedElement(self):
        return self.__jointPackage_Ecore2Maude_SrcETypedElement

    @jointPackage_Ecore2Maude_SrcETypedElement.setter
    def jointPackage_Ecore2Maude_SrcETypedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcETypedElement__jointPackage_Ecore2Maude_SrcETypedElement", None)
        self.__jointPackage_Ecore2Maude_SrcETypedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jointPackage_Ecore2Maude_SrcEClassifier61"):
                opp_val = getattr(old_value, "jointPackage_Ecore2Maude_SrcEClassifier61", None)
                if opp_val == self:
                    setattr(old_value, "jointPackage_Ecore2Maude_SrcEClassifier61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jointPackage_Ecore2Maude_SrcEClassifier61"):
                opp_val = getattr(value, "jointPackage_Ecore2Maude_SrcEClassifier61", None)
                setattr(value, "jointPackage_Ecore2Maude_SrcEClassifier61", self)

class jointPackage_Ecore2Maude_SrcEPackage(SrcENamedElement):

    def __init__(self, nsURI: str, nsPrefix: str, SrcEPackage: "jointPackage_Ecore2Maude_SrcEClassifier" = None, ePackage: set["jointPackage_Ecore2Maude_SrcEClassifier"] = None, SrcEPackage43: "jointPackage_Ecore2Maude_SrcEPackage" = None, eSuperPackage: set["jointPackage_Ecore2Maude_SrcEPackage"] = None, SrcEPackage46: "jointPackage_Ecore2Maude_SrcEPackage" = None, eSubpackages: "jointPackage_Ecore2Maude_SrcEPackage" = None):
        self.nsURI = nsURI
        self.nsPrefix = nsPrefix
        self.SrcEPackage = SrcEPackage
        self.ePackage = ePackage if ePackage is not None else set()
        self.SrcEPackage43 = SrcEPackage43
        self.eSuperPackage = eSuperPackage if eSuperPackage is not None else set()
        self.SrcEPackage46 = SrcEPackage46
        self.eSubpackages = eSubpackages
        
    @property
    def nsPrefix(self) -> str:
        return self.__nsPrefix

    @nsPrefix.setter
    def nsPrefix(self, nsPrefix: str):
        self.__nsPrefix = nsPrefix

    @property
    def nsURI(self) -> str:
        return self.__nsURI

    @nsURI.setter
    def nsURI(self, nsURI: str):
        self.__nsURI = nsURI

    @property
    def ePackage(self):
        return self.__ePackage

    @ePackage.setter
    def ePackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEPackage__ePackage", None)
        self.__ePackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SrcEClassifier"):
                    opp_val = getattr(item, "SrcEClassifier", None)
                    
                    if opp_val == self:
                        setattr(item, "SrcEClassifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SrcEClassifier"):
                    opp_val = getattr(item, "SrcEClassifier", None)
                    
                    setattr(item, "SrcEClassifier", self)
                    

    @property
    def eSuperPackage(self):
        return self.__eSuperPackage

    @eSuperPackage.setter
    def eSuperPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEPackage__eSuperPackage", None)
        self.__eSuperPackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SrcEPackage43"):
                    opp_val = getattr(item, "SrcEPackage43", None)
                    
                    if opp_val == self:
                        setattr(item, "SrcEPackage43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SrcEPackage43"):
                    opp_val = getattr(item, "SrcEPackage43", None)
                    
                    setattr(item, "SrcEPackage43", self)
                    

    @property
    def eSubpackages(self):
        return self.__eSubpackages

    @eSubpackages.setter
    def eSubpackages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEPackage__eSubpackages", None)
        self.__eSubpackages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SrcEPackage46"):
                opp_val = getattr(old_value, "SrcEPackage46", None)
                if opp_val == self:
                    setattr(old_value, "SrcEPackage46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SrcEPackage46"):
                opp_val = getattr(value, "SrcEPackage46", None)
                setattr(value, "SrcEPackage46", self)

    @property
    def SrcEPackage(self):
        return self.__SrcEPackage

    @SrcEPackage.setter
    def SrcEPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEPackage__SrcEPackage", None)
        self.__SrcEPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eClassifiers"):
                opp_val = getattr(old_value, "eClassifiers", None)
                if opp_val == self:
                    setattr(old_value, "eClassifiers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eClassifiers"):
                opp_val = getattr(value, "eClassifiers", None)
                setattr(value, "eClassifiers", self)

    @property
    def SrcEPackage43(self):
        return self.__SrcEPackage43

    @SrcEPackage43.setter
    def SrcEPackage43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEPackage__SrcEPackage43", None)
        self.__SrcEPackage43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eSuperPackage"):
                opp_val = getattr(old_value, "eSuperPackage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eSuperPackage"):
                opp_val = getattr(value, "eSuperPackage", None)
                if opp_val is None:
                    setattr(value, "eSuperPackage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SrcEPackage46(self):
        return self.__SrcEPackage46

    @SrcEPackage46.setter
    def SrcEPackage46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEPackage__SrcEPackage46", None)
        self.__SrcEPackage46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eSubpackages"):
                opp_val = getattr(old_value, "eSubpackages", None)
                if opp_val == self:
                    setattr(old_value, "eSubpackages", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eSubpackages"):
                opp_val = getattr(value, "eSubpackages", None)
                setattr(value, "eSubpackages", self)

    def getEClassifier(self, name: str) -> SrcEClassifier:
        # TODO: Implement getEClassifier method
        pass

class jointPackage_Ecore2Maude_SrcEEnumLiteral(SrcENamedElement):

    def __init__(self, value: int, literal: str, SrcEEnumLiteral: "jointPackage_Ecore2Maude_SrcEEnum" = None, eLiterals: "jointPackage_Ecore2Maude_SrcEEnum" = None):
        self.value = value
        self.literal = literal
        self.SrcEEnumLiteral = SrcEEnumLiteral
        self.eLiterals = eLiterals
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def literal(self) -> str:
        return self.__literal

    @literal.setter
    def literal(self, literal: str):
        self.__literal = literal

    @property
    def SrcEEnumLiteral(self):
        return self.__SrcEEnumLiteral

    @SrcEEnumLiteral.setter
    def SrcEEnumLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEEnumLiteral__SrcEEnumLiteral", None)
        self.__SrcEEnumLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eEnum"):
                opp_val = getattr(old_value, "eEnum", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eEnum"):
                opp_val = getattr(value, "eEnum", None)
                if opp_val is None:
                    setattr(value, "eEnum", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eLiterals(self):
        return self.__eLiterals

    @eLiterals.setter
    def eLiterals(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEEnumLiteral__eLiterals", None)
        self.__eLiterals = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SrcEEnum"):
                opp_val = getattr(old_value, "SrcEEnum", None)
                if opp_val == self:
                    setattr(old_value, "SrcEEnum", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SrcEEnum"):
                opp_val = getattr(value, "SrcEEnum", None)
                setattr(value, "SrcEEnum", self)

class jointPackage_Ecore2Maude_SrcEClassifier(SrcENamedElement):

    def __init__(self, instanceClassName: str, instanceTypeName: str, jointPackage_Ecore2Maude_SrcEClassifier: "jointPackage_Ecore2Maude_SrcEOperation" = None, eClassifiers: "jointPackage_Ecore2Maude_SrcEPackage" = None, SrcEClassifier: "jointPackage_Ecore2Maude_SrcEPackage" = None, jointPackage_Ecore2Maude_SrcEClassifier61: "jointPackage_Ecore2Maude_SrcETypedElement" = None):
        self.instanceClassName = instanceClassName
        self.instanceTypeName = instanceTypeName
        self.jointPackage_Ecore2Maude_SrcEClassifier = jointPackage_Ecore2Maude_SrcEClassifier
        self.eClassifiers = eClassifiers
        self.SrcEClassifier = SrcEClassifier
        self.jointPackage_Ecore2Maude_SrcEClassifier61 = jointPackage_Ecore2Maude_SrcEClassifier61
        
    @property
    def instanceTypeName(self) -> str:
        return self.__instanceTypeName

    @instanceTypeName.setter
    def instanceTypeName(self, instanceTypeName: str):
        self.__instanceTypeName = instanceTypeName

    @property
    def instanceClassName(self) -> str:
        return self.__instanceClassName

    @instanceClassName.setter
    def instanceClassName(self, instanceClassName: str):
        self.__instanceClassName = instanceClassName

    @property
    def SrcEClassifier(self):
        return self.__SrcEClassifier

    @SrcEClassifier.setter
    def SrcEClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEClassifier__SrcEClassifier", None)
        self.__SrcEClassifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ePackage"):
                opp_val = getattr(old_value, "ePackage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ePackage"):
                opp_val = getattr(value, "ePackage", None)
                if opp_val is None:
                    setattr(value, "ePackage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jointPackage_Ecore2Maude_SrcEClassifier(self):
        return self.__jointPackage_Ecore2Maude_SrcEClassifier

    @jointPackage_Ecore2Maude_SrcEClassifier.setter
    def jointPackage_Ecore2Maude_SrcEClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEClassifier__jointPackage_Ecore2Maude_SrcEClassifier", None)
        self.__jointPackage_Ecore2Maude_SrcEClassifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jointPackage_Ecore2Maude_SrcEOperation39"):
                opp_val = getattr(old_value, "jointPackage_Ecore2Maude_SrcEOperation39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jointPackage_Ecore2Maude_SrcEOperation39"):
                opp_val = getattr(value, "jointPackage_Ecore2Maude_SrcEOperation39", None)
                if opp_val is None:
                    setattr(value, "jointPackage_Ecore2Maude_SrcEOperation39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jointPackage_Ecore2Maude_SrcEClassifier61(self):
        return self.__jointPackage_Ecore2Maude_SrcEClassifier61

    @jointPackage_Ecore2Maude_SrcEClassifier61.setter
    def jointPackage_Ecore2Maude_SrcEClassifier61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEClassifier__jointPackage_Ecore2Maude_SrcEClassifier61", None)
        self.__jointPackage_Ecore2Maude_SrcEClassifier61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jointPackage_Ecore2Maude_SrcETypedElement"):
                opp_val = getattr(old_value, "jointPackage_Ecore2Maude_SrcETypedElement", None)
                if opp_val == self:
                    setattr(old_value, "jointPackage_Ecore2Maude_SrcETypedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jointPackage_Ecore2Maude_SrcETypedElement"):
                opp_val = getattr(value, "jointPackage_Ecore2Maude_SrcETypedElement", None)
                setattr(value, "jointPackage_Ecore2Maude_SrcETypedElement", self)

    @property
    def eClassifiers(self):
        return self.__eClassifiers

    @eClassifiers.setter
    def eClassifiers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEClassifier__eClassifiers", None)
        self.__eClassifiers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SrcEPackage"):
                opp_val = getattr(old_value, "SrcEPackage", None)
                if opp_val == self:
                    setattr(old_value, "SrcEPackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SrcEPackage"):
                opp_val = getattr(value, "SrcEPackage", None)
                setattr(value, "SrcEPackage", self)

    def getClassifierID(self) -> int:
        # TODO: Implement getClassifierID method
        pass

class jointPackage_Ecore2Maude_SrcEDataType(SrcEClassifier):

    def __init__(self, serializable: bool, jointPackage_Ecore2Maude_SrcEDataType: "jointPackage_Ecore2Maude_SrcEAttribute" = None):
        self.serializable = serializable
        self.jointPackage_Ecore2Maude_SrcEDataType = jointPackage_Ecore2Maude_SrcEDataType
        
    @property
    def serializable(self) -> bool:
        return self.__serializable

    @serializable.setter
    def serializable(self, serializable: bool):
        self.__serializable = serializable

    @property
    def jointPackage_Ecore2Maude_SrcEDataType(self):
        return self.__jointPackage_Ecore2Maude_SrcEDataType

    @jointPackage_Ecore2Maude_SrcEDataType.setter
    def jointPackage_Ecore2Maude_SrcEDataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEDataType__jointPackage_Ecore2Maude_SrcEDataType", None)
        self.__jointPackage_Ecore2Maude_SrcEDataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jointPackage_Ecore2Maude_SrcEAttribute"):
                opp_val = getattr(old_value, "jointPackage_Ecore2Maude_SrcEAttribute", None)
                if opp_val == self:
                    setattr(old_value, "jointPackage_Ecore2Maude_SrcEAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jointPackage_Ecore2Maude_SrcEAttribute"):
                opp_val = getattr(value, "jointPackage_Ecore2Maude_SrcEAttribute", None)
                setattr(value, "jointPackage_Ecore2Maude_SrcEAttribute", self)

class SrcEStructuralFeature:

    pass
class jointPackage_Ecore2Maude_SrcEReference(SrcEStructuralFeature):

    def __init__(self, containment: bool, container: bool, resolveProxies: bool, jointPackage_Ecore2Maude_SrcEReference: "jointPackage_Ecore2Maude_SrcEClass" = None, jointPackage_Ecore2Maude_SrcEReference14: "jointPackage_Ecore2Maude_SrcEClass" = None, jointPackage_Ecore2Maude_SrcEReference20: "jointPackage_Ecore2Maude_SrcEClass" = None, jointPackage_Ecore2Maude_SrcEReference51: "jointPackage_Ecore2Maude_SrcEReference" = None, jointPackage_Ecore2Maude_SrcEReference49: "jointPackage_Ecore2Maude_SrcEReference" = None, jointPackage_Ecore2Maude_SrcEReference53: "jointPackage_Ecore2Maude_SrcEClass" = None, jointPackage_Ecore2Maude_SrcEReference56: set["jointPackage_Ecore2Maude_SrcEAttribute"] = None):
        self.containment = containment
        self.container = container
        self.resolveProxies = resolveProxies
        self.jointPackage_Ecore2Maude_SrcEReference = jointPackage_Ecore2Maude_SrcEReference
        self.jointPackage_Ecore2Maude_SrcEReference14 = jointPackage_Ecore2Maude_SrcEReference14
        self.jointPackage_Ecore2Maude_SrcEReference20 = jointPackage_Ecore2Maude_SrcEReference20
        self.jointPackage_Ecore2Maude_SrcEReference51 = jointPackage_Ecore2Maude_SrcEReference51
        self.jointPackage_Ecore2Maude_SrcEReference49 = jointPackage_Ecore2Maude_SrcEReference49
        self.jointPackage_Ecore2Maude_SrcEReference53 = jointPackage_Ecore2Maude_SrcEReference53
        self.jointPackage_Ecore2Maude_SrcEReference56 = jointPackage_Ecore2Maude_SrcEReference56 if jointPackage_Ecore2Maude_SrcEReference56 is not None else set()
        
    @property
    def container(self) -> bool:
        return self.__container

    @container.setter
    def container(self, container: bool):
        self.__container = container

    @property
    def resolveProxies(self) -> bool:
        return self.__resolveProxies

    @resolveProxies.setter
    def resolveProxies(self, resolveProxies: bool):
        self.__resolveProxies = resolveProxies

    @property
    def containment(self) -> bool:
        return self.__containment

    @containment.setter
    def containment(self, containment: bool):
        self.__containment = containment

    @property
    def jointPackage_Ecore2Maude_SrcEReference51(self):
        return self.__jointPackage_Ecore2Maude_SrcEReference51

    @jointPackage_Ecore2Maude_SrcEReference51.setter
    def jointPackage_Ecore2Maude_SrcEReference51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEReference__jointPackage_Ecore2Maude_SrcEReference51", None)
        self.__jointPackage_Ecore2Maude_SrcEReference51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jointPackage_Ecore2Maude_SrcEReference49"):
                opp_val = getattr(old_value, "jointPackage_Ecore2Maude_SrcEReference49", None)
                if opp_val == self:
                    setattr(old_value, "jointPackage_Ecore2Maude_SrcEReference49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jointPackage_Ecore2Maude_SrcEReference49"):
                opp_val = getattr(value, "jointPackage_Ecore2Maude_SrcEReference49", None)
                setattr(value, "jointPackage_Ecore2Maude_SrcEReference49", self)

    @property
    def jointPackage_Ecore2Maude_SrcEReference20(self):
        return self.__jointPackage_Ecore2Maude_SrcEReference20

    @jointPackage_Ecore2Maude_SrcEReference20.setter
    def jointPackage_Ecore2Maude_SrcEReference20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEReference__jointPackage_Ecore2Maude_SrcEReference20", None)
        self.__jointPackage_Ecore2Maude_SrcEReference20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jointPackage_Ecore2Maude_SrcEClass19"):
                opp_val = getattr(old_value, "jointPackage_Ecore2Maude_SrcEClass19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jointPackage_Ecore2Maude_SrcEClass19"):
                opp_val = getattr(value, "jointPackage_Ecore2Maude_SrcEClass19", None)
                if opp_val is None:
                    setattr(value, "jointPackage_Ecore2Maude_SrcEClass19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jointPackage_Ecore2Maude_SrcEReference53(self):
        return self.__jointPackage_Ecore2Maude_SrcEReference53

    @jointPackage_Ecore2Maude_SrcEReference53.setter
    def jointPackage_Ecore2Maude_SrcEReference53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEReference__jointPackage_Ecore2Maude_SrcEReference53", None)
        self.__jointPackage_Ecore2Maude_SrcEReference53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jointPackage_Ecore2Maude_SrcEClass54"):
                opp_val = getattr(old_value, "jointPackage_Ecore2Maude_SrcEClass54", None)
                if opp_val == self:
                    setattr(old_value, "jointPackage_Ecore2Maude_SrcEClass54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jointPackage_Ecore2Maude_SrcEClass54"):
                opp_val = getattr(value, "jointPackage_Ecore2Maude_SrcEClass54", None)
                setattr(value, "jointPackage_Ecore2Maude_SrcEClass54", self)

    @property
    def jointPackage_Ecore2Maude_SrcEReference56(self):
        return self.__jointPackage_Ecore2Maude_SrcEReference56

    @jointPackage_Ecore2Maude_SrcEReference56.setter
    def jointPackage_Ecore2Maude_SrcEReference56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEReference__jointPackage_Ecore2Maude_SrcEReference56", None)
        self.__jointPackage_Ecore2Maude_SrcEReference56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jointPackage_Ecore2Maude_SrcEAttribute57"):
                    opp_val = getattr(item, "jointPackage_Ecore2Maude_SrcEAttribute57", None)
                    
                    if opp_val == self:
                        setattr(item, "jointPackage_Ecore2Maude_SrcEAttribute57", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jointPackage_Ecore2Maude_SrcEAttribute57"):
                    opp_val = getattr(item, "jointPackage_Ecore2Maude_SrcEAttribute57", None)
                    
                    setattr(item, "jointPackage_Ecore2Maude_SrcEAttribute57", self)
                    

    @property
    def jointPackage_Ecore2Maude_SrcEReference14(self):
        return self.__jointPackage_Ecore2Maude_SrcEReference14

    @jointPackage_Ecore2Maude_SrcEReference14.setter
    def jointPackage_Ecore2Maude_SrcEReference14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEReference__jointPackage_Ecore2Maude_SrcEReference14", None)
        self.__jointPackage_Ecore2Maude_SrcEReference14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jointPackage_Ecore2Maude_SrcEClass13"):
                opp_val = getattr(old_value, "jointPackage_Ecore2Maude_SrcEClass13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jointPackage_Ecore2Maude_SrcEClass13"):
                opp_val = getattr(value, "jointPackage_Ecore2Maude_SrcEClass13", None)
                if opp_val is None:
                    setattr(value, "jointPackage_Ecore2Maude_SrcEClass13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jointPackage_Ecore2Maude_SrcEReference(self):
        return self.__jointPackage_Ecore2Maude_SrcEReference

    @jointPackage_Ecore2Maude_SrcEReference.setter
    def jointPackage_Ecore2Maude_SrcEReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEReference__jointPackage_Ecore2Maude_SrcEReference", None)
        self.__jointPackage_Ecore2Maude_SrcEReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jointPackage_Ecore2Maude_SrcEClass11"):
                opp_val = getattr(old_value, "jointPackage_Ecore2Maude_SrcEClass11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jointPackage_Ecore2Maude_SrcEClass11"):
                opp_val = getattr(value, "jointPackage_Ecore2Maude_SrcEClass11", None)
                if opp_val is None:
                    setattr(value, "jointPackage_Ecore2Maude_SrcEClass11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jointPackage_Ecore2Maude_SrcEReference49(self):
        return self.__jointPackage_Ecore2Maude_SrcEReference49

    @jointPackage_Ecore2Maude_SrcEReference49.setter
    def jointPackage_Ecore2Maude_SrcEReference49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEReference__jointPackage_Ecore2Maude_SrcEReference49", None)
        self.__jointPackage_Ecore2Maude_SrcEReference49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jointPackage_Ecore2Maude_SrcEReference51"):
                opp_val = getattr(old_value, "jointPackage_Ecore2Maude_SrcEReference51", None)
                if opp_val == self:
                    setattr(old_value, "jointPackage_Ecore2Maude_SrcEReference51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jointPackage_Ecore2Maude_SrcEReference51"):
                opp_val = getattr(value, "jointPackage_Ecore2Maude_SrcEReference51", None)
                setattr(value, "jointPackage_Ecore2Maude_SrcEReference51", self)

class jointPackage_Ecore2Maude_SrcEAttribute(SrcEStructuralFeature):

    def __init__(self, iD: bool, jointPackage_Ecore2Maude_SrcEAttribute: "jointPackage_Ecore2Maude_SrcEDataType" = None, jointPackage_Ecore2Maude_SrcEAttribute9: "jointPackage_Ecore2Maude_SrcEClass" = None, jointPackage_Ecore2Maude_SrcEAttribute17: "jointPackage_Ecore2Maude_SrcEClass" = None, jointPackage_Ecore2Maude_SrcEAttribute30: "jointPackage_Ecore2Maude_SrcEClass" = None, jointPackage_Ecore2Maude_SrcEAttribute57: "jointPackage_Ecore2Maude_SrcEReference" = None):
        self.iD = iD
        self.jointPackage_Ecore2Maude_SrcEAttribute = jointPackage_Ecore2Maude_SrcEAttribute
        self.jointPackage_Ecore2Maude_SrcEAttribute9 = jointPackage_Ecore2Maude_SrcEAttribute9
        self.jointPackage_Ecore2Maude_SrcEAttribute17 = jointPackage_Ecore2Maude_SrcEAttribute17
        self.jointPackage_Ecore2Maude_SrcEAttribute30 = jointPackage_Ecore2Maude_SrcEAttribute30
        self.jointPackage_Ecore2Maude_SrcEAttribute57 = jointPackage_Ecore2Maude_SrcEAttribute57
        
    @property
    def iD(self) -> bool:
        return self.__iD

    @iD.setter
    def iD(self, iD: bool):
        self.__iD = iD

    @property
    def jointPackage_Ecore2Maude_SrcEAttribute9(self):
        return self.__jointPackage_Ecore2Maude_SrcEAttribute9

    @jointPackage_Ecore2Maude_SrcEAttribute9.setter
    def jointPackage_Ecore2Maude_SrcEAttribute9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEAttribute__jointPackage_Ecore2Maude_SrcEAttribute9", None)
        self.__jointPackage_Ecore2Maude_SrcEAttribute9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jointPackage_Ecore2Maude_SrcEClass8"):
                opp_val = getattr(old_value, "jointPackage_Ecore2Maude_SrcEClass8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jointPackage_Ecore2Maude_SrcEClass8"):
                opp_val = getattr(value, "jointPackage_Ecore2Maude_SrcEClass8", None)
                if opp_val is None:
                    setattr(value, "jointPackage_Ecore2Maude_SrcEClass8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jointPackage_Ecore2Maude_SrcEAttribute57(self):
        return self.__jointPackage_Ecore2Maude_SrcEAttribute57

    @jointPackage_Ecore2Maude_SrcEAttribute57.setter
    def jointPackage_Ecore2Maude_SrcEAttribute57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEAttribute__jointPackage_Ecore2Maude_SrcEAttribute57", None)
        self.__jointPackage_Ecore2Maude_SrcEAttribute57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jointPackage_Ecore2Maude_SrcEReference56"):
                opp_val = getattr(old_value, "jointPackage_Ecore2Maude_SrcEReference56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jointPackage_Ecore2Maude_SrcEReference56"):
                opp_val = getattr(value, "jointPackage_Ecore2Maude_SrcEReference56", None)
                if opp_val is None:
                    setattr(value, "jointPackage_Ecore2Maude_SrcEReference56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jointPackage_Ecore2Maude_SrcEAttribute17(self):
        return self.__jointPackage_Ecore2Maude_SrcEAttribute17

    @jointPackage_Ecore2Maude_SrcEAttribute17.setter
    def jointPackage_Ecore2Maude_SrcEAttribute17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEAttribute__jointPackage_Ecore2Maude_SrcEAttribute17", None)
        self.__jointPackage_Ecore2Maude_SrcEAttribute17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jointPackage_Ecore2Maude_SrcEClass16"):
                opp_val = getattr(old_value, "jointPackage_Ecore2Maude_SrcEClass16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jointPackage_Ecore2Maude_SrcEClass16"):
                opp_val = getattr(value, "jointPackage_Ecore2Maude_SrcEClass16", None)
                if opp_val is None:
                    setattr(value, "jointPackage_Ecore2Maude_SrcEClass16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jointPackage_Ecore2Maude_SrcEAttribute(self):
        return self.__jointPackage_Ecore2Maude_SrcEAttribute

    @jointPackage_Ecore2Maude_SrcEAttribute.setter
    def jointPackage_Ecore2Maude_SrcEAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEAttribute__jointPackage_Ecore2Maude_SrcEAttribute", None)
        self.__jointPackage_Ecore2Maude_SrcEAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jointPackage_Ecore2Maude_SrcEDataType"):
                opp_val = getattr(old_value, "jointPackage_Ecore2Maude_SrcEDataType", None)
                if opp_val == self:
                    setattr(old_value, "jointPackage_Ecore2Maude_SrcEDataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jointPackage_Ecore2Maude_SrcEDataType"):
                opp_val = getattr(value, "jointPackage_Ecore2Maude_SrcEDataType", None)
                setattr(value, "jointPackage_Ecore2Maude_SrcEDataType", self)

    @property
    def jointPackage_Ecore2Maude_SrcEAttribute30(self):
        return self.__jointPackage_Ecore2Maude_SrcEAttribute30

    @jointPackage_Ecore2Maude_SrcEAttribute30.setter
    def jointPackage_Ecore2Maude_SrcEAttribute30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEAttribute__jointPackage_Ecore2Maude_SrcEAttribute30", None)
        self.__jointPackage_Ecore2Maude_SrcEAttribute30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jointPackage_Ecore2Maude_SrcEClass29"):
                opp_val = getattr(old_value, "jointPackage_Ecore2Maude_SrcEClass29", None)
                if opp_val == self:
                    setattr(old_value, "jointPackage_Ecore2Maude_SrcEClass29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jointPackage_Ecore2Maude_SrcEClass29"):
                opp_val = getattr(value, "jointPackage_Ecore2Maude_SrcEClass29", None)
                setattr(value, "jointPackage_Ecore2Maude_SrcEClass29", self)

class jointPackage_Ecore2Maude_TrgEqualCond(TrgEquationalCond):

    pass
class jointPackage_Ecore2Maude_SrcEStringToStringMapEntry:

    def __init__(self, key: str, value: str, jointPackage_Ecore2Maude_SrcEStringToStringMapEntry: "jointPackage_Ecore2Maude_JointMM" = None):
        self.key = key
        self.value = value
        self.jointPackage_Ecore2Maude_SrcEStringToStringMapEntry = jointPackage_Ecore2Maude_SrcEStringToStringMapEntry
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def jointPackage_Ecore2Maude_SrcEStringToStringMapEntry(self):
        return self.__jointPackage_Ecore2Maude_SrcEStringToStringMapEntry

    @jointPackage_Ecore2Maude_SrcEStringToStringMapEntry.setter
    def jointPackage_Ecore2Maude_SrcEStringToStringMapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_Ecore2Maude_SrcEStringToStringMapEntry__jointPackage_Ecore2Maude_SrcEStringToStringMapEntry", None)
        self.__jointPackage_Ecore2Maude_SrcEStringToStringMapEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jointPackage_Ecore2Maude_JointMM"):
                opp_val = getattr(old_value, "jointPackage_Ecore2Maude_JointMM", None)
                if opp_val == self:
                    setattr(old_value, "jointPackage_Ecore2Maude_JointMM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jointPackage_Ecore2Maude_JointMM"):
                opp_val = getattr(value, "jointPackage_Ecore2Maude_JointMM", None)
                setattr(value, "jointPackage_Ecore2Maude_JointMM", self)

class jointPackage_Ecore2Maude_JointMM:

    pass