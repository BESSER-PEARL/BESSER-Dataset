from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class RangeConstraint:

    pass
class adb_ParameterEffectiveValue:

    pass
class adb_AttributeDesignator:

    pass
class Range:

    pass
class adb_ExplicitRange(Range):

    pass
class adb_EntityRange(Range):

    pass
class Interval:

    pass
class adb_ArrayComponentAssociation:

    def __init__(self, box: bool, adb_ArrayComponentAssociation: "adb_NamedArrayAggregate" = None, adb_ArrayComponentAssociation545: "adb_DiscreteChoiceList" = None, adb_ArrayComponentAssociation548: "adb_Expression" = None):
        self.box = box
        self.adb_ArrayComponentAssociation = adb_ArrayComponentAssociation
        self.adb_ArrayComponentAssociation545 = adb_ArrayComponentAssociation545
        self.adb_ArrayComponentAssociation548 = adb_ArrayComponentAssociation548
        
    @property
    def box(self) -> bool:
        return self.__box

    @box.setter
    def box(self, box: bool):
        self.__box = box

    @property
    def adb_ArrayComponentAssociation(self):
        return self.__adb_ArrayComponentAssociation

    @adb_ArrayComponentAssociation.setter
    def adb_ArrayComponentAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_ArrayComponentAssociation__adb_ArrayComponentAssociation", None)
        self.__adb_ArrayComponentAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_NamedArrayAggregate"):
                opp_val = getattr(old_value, "adb_NamedArrayAggregate", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_NamedArrayAggregate"):
                opp_val = getattr(value, "adb_NamedArrayAggregate", None)
                if opp_val is None:
                    setattr(value, "adb_NamedArrayAggregate", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def adb_ArrayComponentAssociation545(self):
        return self.__adb_ArrayComponentAssociation545

    @adb_ArrayComponentAssociation545.setter
    def adb_ArrayComponentAssociation545(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_ArrayComponentAssociation__adb_ArrayComponentAssociation545", None)
        self.__adb_ArrayComponentAssociation545 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_DiscreteChoiceList546"):
                opp_val = getattr(old_value, "adb_DiscreteChoiceList546", None)
                if opp_val == self:
                    setattr(old_value, "adb_DiscreteChoiceList546", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_DiscreteChoiceList546"):
                opp_val = getattr(value, "adb_DiscreteChoiceList546", None)
                setattr(value, "adb_DiscreteChoiceList546", self)

    @property
    def adb_ArrayComponentAssociation548(self):
        return self.__adb_ArrayComponentAssociation548

    @adb_ArrayComponentAssociation548.setter
    def adb_ArrayComponentAssociation548(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_ArrayComponentAssociation__adb_ArrayComponentAssociation548", None)
        self.__adb_ArrayComponentAssociation548 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_Expression549"):
                opp_val = getattr(old_value, "adb_Expression549", None)
                if opp_val == self:
                    setattr(old_value, "adb_Expression549", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_Expression549"):
                opp_val = getattr(value, "adb_Expression549", None)
                setattr(value, "adb_Expression549", self)

class adb_ParameterAssociation:

    def __init__(self, selectorName: str, adb_ParameterAssociation: "adb_PrimaryName" = None, adb_ParameterAssociation563: "adb_ParameterEffectiveValue" = None):
        self.selectorName = selectorName
        self.adb_ParameterAssociation = adb_ParameterAssociation
        self.adb_ParameterAssociation563 = adb_ParameterAssociation563
        
    @property
    def selectorName(self) -> str:
        return self.__selectorName

    @selectorName.setter
    def selectorName(self, selectorName: str):
        self.__selectorName = selectorName

    @property
    def adb_ParameterAssociation563(self):
        return self.__adb_ParameterAssociation563

    @adb_ParameterAssociation563.setter
    def adb_ParameterAssociation563(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_ParameterAssociation__adb_ParameterAssociation563", None)
        self.__adb_ParameterAssociation563 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_ParameterEffectiveValue"):
                opp_val = getattr(old_value, "adb_ParameterEffectiveValue", None)
                if opp_val == self:
                    setattr(old_value, "adb_ParameterEffectiveValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_ParameterEffectiveValue"):
                opp_val = getattr(value, "adb_ParameterEffectiveValue", None)
                setattr(value, "adb_ParameterEffectiveValue", self)

    @property
    def adb_ParameterAssociation(self):
        return self.__adb_ParameterAssociation

    @adb_ParameterAssociation.setter
    def adb_ParameterAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_ParameterAssociation__adb_ParameterAssociation", None)
        self.__adb_ParameterAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_PrimaryName553"):
                opp_val = getattr(old_value, "adb_PrimaryName553", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_PrimaryName553"):
                opp_val = getattr(value, "adb_PrimaryName553", None)
                if opp_val is None:
                    setattr(value, "adb_PrimaryName553", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class adb_PrimaryName:

    pass
class adb_AncestorPart:

    pass
class RecordComponentAssociation:

    pass
class adb_UninitializedComponents(RecordComponentAssociation):

    def __init__(self, box: bool):
        self.box = box
        
    @property
    def box(self) -> bool:
        return self.__box

    @box.setter
    def box(self, box: bool):
        self.__box = box

class adb_InitializedComponents(RecordComponentAssociation):

    pass
class adb_RecordComponentAssociation:

    pass
class ArrayAggregate:

    pass
class adb_NamedArrayAggregate(ArrayAggregate):

    pass
class adb_PositionalArrayAggregate(ArrayAggregate):

    def __init__(self, othersBox: bool, adb_PositionalArrayAggregate: set["adb_Expression"] = None, adb_PositionalArrayAggregate541: "adb_Expression" = None):
        self.othersBox = othersBox
        self.adb_PositionalArrayAggregate = adb_PositionalArrayAggregate if adb_PositionalArrayAggregate is not None else set()
        self.adb_PositionalArrayAggregate541 = adb_PositionalArrayAggregate541
        
    @property
    def othersBox(self) -> bool:
        return self.__othersBox

    @othersBox.setter
    def othersBox(self, othersBox: bool):
        self.__othersBox = othersBox

    @property
    def adb_PositionalArrayAggregate(self):
        return self.__adb_PositionalArrayAggregate

    @adb_PositionalArrayAggregate.setter
    def adb_PositionalArrayAggregate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_PositionalArrayAggregate__adb_PositionalArrayAggregate", None)
        self.__adb_PositionalArrayAggregate = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adb_Expression539"):
                    opp_val = getattr(item, "adb_Expression539", None)
                    
                    if opp_val == self:
                        setattr(item, "adb_Expression539", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adb_Expression539"):
                    opp_val = getattr(item, "adb_Expression539", None)
                    
                    setattr(item, "adb_Expression539", self)
                    

    @property
    def adb_PositionalArrayAggregate541(self):
        return self.__adb_PositionalArrayAggregate541

    @adb_PositionalArrayAggregate541.setter
    def adb_PositionalArrayAggregate541(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_PositionalArrayAggregate__adb_PositionalArrayAggregate541", None)
        self.__adb_PositionalArrayAggregate541 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_Expression542"):
                opp_val = getattr(old_value, "adb_Expression542", None)
                if opp_val == self:
                    setattr(old_value, "adb_Expression542", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_Expression542"):
                opp_val = getattr(value, "adb_Expression542", None)
                setattr(value, "adb_Expression542", self)

class Qualifier:

    pass
class ParenthesizedExpression:

    pass
class adb_Aggregate(ParenthesizedExpression, Qualifier):

    pass
class adb_ComponentChoiceList:

    def __init__(self, componentSelectorName: str, others: bool, adb_ComponentChoiceList: "adb_RecordComponentAssociation" = None):
        self.componentSelectorName = componentSelectorName
        self.others = others
        self.adb_ComponentChoiceList = adb_ComponentChoiceList
        
    @property
    def others(self) -> bool:
        return self.__others

    @others.setter
    def others(self, others: bool):
        self.__others = others

    @property
    def componentSelectorName(self) -> str:
        return self.__componentSelectorName

    @componentSelectorName.setter
    def componentSelectorName(self, componentSelectorName: str):
        self.__componentSelectorName = componentSelectorName

    @property
    def adb_ComponentChoiceList(self):
        return self.__adb_ComponentChoiceList

    @adb_ComponentChoiceList.setter
    def adb_ComponentChoiceList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_ComponentChoiceList__adb_ComponentChoiceList", None)
        self.__adb_ComponentChoiceList = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_RecordComponentAssociation531"):
                opp_val = getattr(old_value, "adb_RecordComponentAssociation531", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_RecordComponentAssociation531"):
                opp_val = getattr(value, "adb_RecordComponentAssociation531", None)
                if opp_val is None:
                    setattr(value, "adb_RecordComponentAssociation531", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class adb_DiscriminantSelectors:

    def __init__(self, discriminantSelectorName: str, adb_DiscriminantSelectors: "adb_DiscriminantAssociation" = None):
        self.discriminantSelectorName = discriminantSelectorName
        self.adb_DiscriminantSelectors = adb_DiscriminantSelectors
        
    @property
    def discriminantSelectorName(self) -> str:
        return self.__discriminantSelectorName

    @discriminantSelectorName.setter
    def discriminantSelectorName(self, discriminantSelectorName: str):
        self.__discriminantSelectorName = discriminantSelectorName

    @property
    def adb_DiscriminantSelectors(self):
        return self.__adb_DiscriminantSelectors

    @adb_DiscriminantSelectors.setter
    def adb_DiscriminantSelectors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_DiscriminantSelectors__adb_DiscriminantSelectors", None)
        self.__adb_DiscriminantSelectors = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_DiscriminantAssociation525"):
                opp_val = getattr(old_value, "adb_DiscriminantAssociation525", None)
                if opp_val == self:
                    setattr(old_value, "adb_DiscriminantAssociation525", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_DiscriminantAssociation525"):
                opp_val = getattr(value, "adb_DiscriminantAssociation525", None)
                setattr(value, "adb_DiscriminantAssociation525", self)

class RecordAggregate:

    pass
class adb_RecordComponentAssociationList(RecordAggregate):

    def __init__(self, nullRecord: bool, adb_RecordComponentAssociationList: set["adb_RecordComponentAssociation"] = None, adb_RecordComponentAssociationList537: "adb_ExtensionAggregate" = None):
        self.nullRecord = nullRecord
        self.adb_RecordComponentAssociationList = adb_RecordComponentAssociationList if adb_RecordComponentAssociationList is not None else set()
        self.adb_RecordComponentAssociationList537 = adb_RecordComponentAssociationList537
        
    @property
    def nullRecord(self) -> bool:
        return self.__nullRecord

    @nullRecord.setter
    def nullRecord(self, nullRecord: bool):
        self.__nullRecord = nullRecord

    @property
    def adb_RecordComponentAssociationList(self):
        return self.__adb_RecordComponentAssociationList

    @adb_RecordComponentAssociationList.setter
    def adb_RecordComponentAssociationList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_RecordComponentAssociationList__adb_RecordComponentAssociationList", None)
        self.__adb_RecordComponentAssociationList = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adb_RecordComponentAssociation"):
                    opp_val = getattr(item, "adb_RecordComponentAssociation", None)
                    
                    if opp_val == self:
                        setattr(item, "adb_RecordComponentAssociation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adb_RecordComponentAssociation"):
                    opp_val = getattr(item, "adb_RecordComponentAssociation", None)
                    
                    setattr(item, "adb_RecordComponentAssociation", self)
                    

    @property
    def adb_RecordComponentAssociationList537(self):
        return self.__adb_RecordComponentAssociationList537

    @adb_RecordComponentAssociationList537.setter
    def adb_RecordComponentAssociationList537(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_RecordComponentAssociationList__adb_RecordComponentAssociationList537", None)
        self.__adb_RecordComponentAssociationList537 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_ExtensionAggregate536"):
                opp_val = getattr(old_value, "adb_ExtensionAggregate536", None)
                if opp_val == self:
                    setattr(old_value, "adb_ExtensionAggregate536", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_ExtensionAggregate536"):
                opp_val = getattr(value, "adb_ExtensionAggregate536", None)
                setattr(value, "adb_ExtensionAggregate536", self)

class Aggregate:

    pass
class adb_ArrayAggregate(Aggregate):

    pass
class adb_ExtensionAggregate(Aggregate):

    pass
class adb_RecordAggregate(Aggregate):

    pass
class adb_DiscriminantAssociation:

    pass
class CompositeConstraint:

    pass
class adb_DiscriminantConstraint(CompositeConstraint):

    pass
class adb_CompositeConstraint:

    pass
class ScalarConstraint:

    pass
class adb_RangeConstraint(ScalarConstraint):

    pass
class adb_DeltaConstraint(ScalarConstraint):

    pass
class adb_DigitsConstraint(ScalarConstraint):

    pass
class adb_ScalarConstraint:

    pass
class adb_IndexConstraint(CompositeConstraint):

    pass
class adb_OptConstraint:

    pass
class DiscreteRange:

    pass
class DiscreteSubtypeDefinition:

    pass
class adb_DiscreteRange(DiscreteSubtypeDefinition):

    pass
class adb_Qualifier:

    pass
class adb_EObject:

    pass
class Primary:

    pass
class adb_ParenthesizedExpression(Primary):

    pass
class adb_QualifiedName(Primary):

    pass
class adb_Allocator(Primary):

    pass
class adb_StringLiteral(Primary):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class adb_Null(Primary):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class adb_NumericLiteral(Primary):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class adb_Primary:

    pass
class adb_Factor:

    def __init__(self, abs: bool, not: bool, adb_Factor: "adb_Term" = None, adb_Factor493: "adb_Primary" = None, adb_Factor495: "adb_Primary" = None):
        self.abs = abs
        self.not = not
        self.adb_Factor = adb_Factor
        self.adb_Factor493 = adb_Factor493
        self.adb_Factor495 = adb_Factor495
        
    @property
    def not(self) -> bool:
        return self.__not

    @not.setter
    def not(self, not: bool):
        self.__not = not

    @property
    def abs(self) -> bool:
        return self.__abs

    @abs.setter
    def abs(self, abs: bool):
        self.__abs = abs

    @property
    def adb_Factor495(self):
        return self.__adb_Factor495

    @adb_Factor495.setter
    def adb_Factor495(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Factor__adb_Factor495", None)
        self.__adb_Factor495 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_Primary496"):
                opp_val = getattr(old_value, "adb_Primary496", None)
                if opp_val == self:
                    setattr(old_value, "adb_Primary496", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_Primary496"):
                opp_val = getattr(value, "adb_Primary496", None)
                setattr(value, "adb_Primary496", self)

    @property
    def adb_Factor493(self):
        return self.__adb_Factor493

    @adb_Factor493.setter
    def adb_Factor493(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Factor__adb_Factor493", None)
        self.__adb_Factor493 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_Primary"):
                opp_val = getattr(old_value, "adb_Primary", None)
                if opp_val == self:
                    setattr(old_value, "adb_Primary", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_Primary"):
                opp_val = getattr(value, "adb_Primary", None)
                setattr(value, "adb_Primary", self)

    @property
    def adb_Factor(self):
        return self.__adb_Factor

    @adb_Factor.setter
    def adb_Factor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Factor__adb_Factor", None)
        self.__adb_Factor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_Term491"):
                opp_val = getattr(old_value, "adb_Term491", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_Term491"):
                opp_val = getattr(value, "adb_Term491", None)
                if opp_val is None:
                    setattr(value, "adb_Term491", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class adb_Interval:

    pass
class adb_Membership:

    def __init__(self, not: bool, adb_Membership: "adb_Relation" = None, adb_Membership487: "adb_Interval" = None):
        self.not = not
        self.adb_Membership = adb_Membership
        self.adb_Membership487 = adb_Membership487
        
    @property
    def not(self) -> bool:
        return self.__not

    @not.setter
    def not(self, not: bool):
        self.__not = not

    @property
    def adb_Membership(self):
        return self.__adb_Membership

    @adb_Membership.setter
    def adb_Membership(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Membership__adb_Membership", None)
        self.__adb_Membership = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_Relation485"):
                opp_val = getattr(old_value, "adb_Relation485", None)
                if opp_val == self:
                    setattr(old_value, "adb_Relation485", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_Relation485"):
                opp_val = getattr(value, "adb_Relation485", None)
                setattr(value, "adb_Relation485", self)

    @property
    def adb_Membership487(self):
        return self.__adb_Membership487

    @adb_Membership487.setter
    def adb_Membership487(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Membership__adb_Membership487", None)
        self.__adb_Membership487 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_Interval"):
                opp_val = getattr(old_value, "adb_Interval", None)
                if opp_val == self:
                    setattr(old_value, "adb_Interval", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_Interval"):
                opp_val = getattr(value, "adb_Interval", None)
                setattr(value, "adb_Interval", self)

class adb_Relation:

    def __init__(self, relationalOperator: str, adb_Relation: "adb_Expression" = None, adb_Relation479: "adb_SimpleExpression" = None, adb_Relation482: "adb_SimpleExpression" = None, adb_Relation485: "adb_Membership" = None):
        self.relationalOperator = relationalOperator
        self.adb_Relation = adb_Relation
        self.adb_Relation479 = adb_Relation479
        self.adb_Relation482 = adb_Relation482
        self.adb_Relation485 = adb_Relation485
        
    @property
    def relationalOperator(self) -> str:
        return self.__relationalOperator

    @relationalOperator.setter
    def relationalOperator(self, relationalOperator: str):
        self.__relationalOperator = relationalOperator

    @property
    def adb_Relation479(self):
        return self.__adb_Relation479

    @adb_Relation479.setter
    def adb_Relation479(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Relation__adb_Relation479", None)
        self.__adb_Relation479 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_SimpleExpression480"):
                opp_val = getattr(old_value, "adb_SimpleExpression480", None)
                if opp_val == self:
                    setattr(old_value, "adb_SimpleExpression480", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_SimpleExpression480"):
                opp_val = getattr(value, "adb_SimpleExpression480", None)
                setattr(value, "adb_SimpleExpression480", self)

    @property
    def adb_Relation482(self):
        return self.__adb_Relation482

    @adb_Relation482.setter
    def adb_Relation482(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Relation__adb_Relation482", None)
        self.__adb_Relation482 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_SimpleExpression483"):
                opp_val = getattr(old_value, "adb_SimpleExpression483", None)
                if opp_val == self:
                    setattr(old_value, "adb_SimpleExpression483", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_SimpleExpression483"):
                opp_val = getattr(value, "adb_SimpleExpression483", None)
                setattr(value, "adb_SimpleExpression483", self)

    @property
    def adb_Relation(self):
        return self.__adb_Relation

    @adb_Relation.setter
    def adb_Relation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Relation__adb_Relation", None)
        self.__adb_Relation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_Expression477"):
                opp_val = getattr(old_value, "adb_Expression477", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_Expression477"):
                opp_val = getattr(value, "adb_Expression477", None)
                if opp_val is None:
                    setattr(value, "adb_Expression477", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def adb_Relation485(self):
        return self.__adb_Relation485

    @adb_Relation485.setter
    def adb_Relation485(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Relation__adb_Relation485", None)
        self.__adb_Relation485 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_Membership"):
                opp_val = getattr(old_value, "adb_Membership", None)
                if opp_val == self:
                    setattr(old_value, "adb_Membership", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_Membership"):
                opp_val = getattr(value, "adb_Membership", None)
                setattr(value, "adb_Membership", self)

class ParameterEffectiveValue:

    pass
class AncestorPart:

    pass
class adb_Term:

    def __init__(self, multiplyingOperators: str, adb_Term: "adb_SimpleExpression" = None, adb_Term491: set["adb_Factor"] = None):
        self.multiplyingOperators = multiplyingOperators
        self.adb_Term = adb_Term
        self.adb_Term491 = adb_Term491 if adb_Term491 is not None else set()
        
    @property
    def multiplyingOperators(self) -> str:
        return self.__multiplyingOperators

    @multiplyingOperators.setter
    def multiplyingOperators(self, multiplyingOperators: str):
        self.__multiplyingOperators = multiplyingOperators

    @property
    def adb_Term491(self):
        return self.__adb_Term491

    @adb_Term491.setter
    def adb_Term491(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Term__adb_Term491", None)
        self.__adb_Term491 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adb_Factor"):
                    opp_val = getattr(item, "adb_Factor", None)
                    
                    if opp_val == self:
                        setattr(item, "adb_Factor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adb_Factor"):
                    opp_val = getattr(item, "adb_Factor", None)
                    
                    setattr(item, "adb_Factor", self)
                    

    @property
    def adb_Term(self):
        return self.__adb_Term

    @adb_Term.setter
    def adb_Term(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Term__adb_Term", None)
        self.__adb_Term = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_SimpleExpression489"):
                opp_val = getattr(old_value, "adb_SimpleExpression489", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_SimpleExpression489"):
                opp_val = getattr(value, "adb_SimpleExpression489", None)
                if opp_val is None:
                    setattr(value, "adb_SimpleExpression489", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class EntryIndex:

    pass
class RealTypeDefinition:

    pass
class adb_FixedPointDefinition(RealTypeDefinition):

    pass
class adb_FloatingPointDefinition(RealTypeDefinition):

    pass
class adb_RealRangeSpecification:

    pass
class adb_DiscreteChoice:

    pass
class DiscreteChoice:

    pass
class adb_Range(Interval, RangeConstraint, DiscreteChoice, ParameterEffectiveValue, DiscreteRange):

    pass
class ExplicitGenericActualParameter:

    pass
class adb_Variant:

    pass
class adb_ModClause:

    pass
class ComponentItem:

    pass
class adb_ComponentClause:

    def __init__(self, localName: str, adb_ComponentClause: "adb_AspectClause" = None, adb_ComponentClause446: "adb_Expression" = None, adb_ComponentClause449: "adb_SimpleExpression" = None, adb_ComponentClause452: "adb_SimpleExpression" = None):
        self.localName = localName
        self.adb_ComponentClause = adb_ComponentClause
        self.adb_ComponentClause446 = adb_ComponentClause446
        self.adb_ComponentClause449 = adb_ComponentClause449
        self.adb_ComponentClause452 = adb_ComponentClause452
        
    @property
    def localName(self) -> str:
        return self.__localName

    @localName.setter
    def localName(self, localName: str):
        self.__localName = localName

    @property
    def adb_ComponentClause449(self):
        return self.__adb_ComponentClause449

    @adb_ComponentClause449.setter
    def adb_ComponentClause449(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_ComponentClause__adb_ComponentClause449", None)
        self.__adb_ComponentClause449 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_SimpleExpression450"):
                opp_val = getattr(old_value, "adb_SimpleExpression450", None)
                if opp_val == self:
                    setattr(old_value, "adb_SimpleExpression450", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_SimpleExpression450"):
                opp_val = getattr(value, "adb_SimpleExpression450", None)
                setattr(value, "adb_SimpleExpression450", self)

    @property
    def adb_ComponentClause446(self):
        return self.__adb_ComponentClause446

    @adb_ComponentClause446.setter
    def adb_ComponentClause446(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_ComponentClause__adb_ComponentClause446", None)
        self.__adb_ComponentClause446 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_Expression447"):
                opp_val = getattr(old_value, "adb_Expression447", None)
                if opp_val == self:
                    setattr(old_value, "adb_Expression447", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_Expression447"):
                opp_val = getattr(value, "adb_Expression447", None)
                setattr(value, "adb_Expression447", self)

    @property
    def adb_ComponentClause452(self):
        return self.__adb_ComponentClause452

    @adb_ComponentClause452.setter
    def adb_ComponentClause452(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_ComponentClause__adb_ComponentClause452", None)
        self.__adb_ComponentClause452 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_SimpleExpression453"):
                opp_val = getattr(old_value, "adb_SimpleExpression453", None)
                if opp_val == self:
                    setattr(old_value, "adb_SimpleExpression453", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_SimpleExpression453"):
                opp_val = getattr(value, "adb_SimpleExpression453", None)
                setattr(value, "adb_SimpleExpression453", self)

    @property
    def adb_ComponentClause(self):
        return self.__adb_ComponentClause

    @adb_ComponentClause.setter
    def adb_ComponentClause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_ComponentClause__adb_ComponentClause", None)
        self.__adb_ComponentClause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_AspectClause441"):
                opp_val = getattr(old_value, "adb_AspectClause441", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_AspectClause441"):
                opp_val = getattr(value, "adb_AspectClause441", None)
                if opp_val is None:
                    setattr(value, "adb_AspectClause441", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class adb_ComponentItem:

    pass
class adb_ComponentList:

    pass
class adb_VariantPart:

    def __init__(self, name: str, adb_VariantPart: "adb_OptVariantPart" = None, adb_VariantPart455: set["adb_Variant"] = None):
        self.name = name
        self.adb_VariantPart = adb_VariantPart
        self.adb_VariantPart455 = adb_VariantPart455 if adb_VariantPart455 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def adb_VariantPart455(self):
        return self.__adb_VariantPart455

    @adb_VariantPart455.setter
    def adb_VariantPart455(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_VariantPart__adb_VariantPart455", None)
        self.__adb_VariantPart455 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adb_Variant"):
                    opp_val = getattr(item, "adb_Variant", None)
                    
                    if opp_val == self:
                        setattr(item, "adb_Variant", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adb_Variant"):
                    opp_val = getattr(item, "adb_Variant", None)
                    
                    setattr(item, "adb_Variant", self)
                    

    @property
    def adb_VariantPart(self):
        return self.__adb_VariantPart

    @adb_VariantPart.setter
    def adb_VariantPart(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_VariantPart__adb_VariantPart", None)
        self.__adb_VariantPart = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_OptVariantPart427"):
                opp_val = getattr(old_value, "adb_OptVariantPart427", None)
                if opp_val == self:
                    setattr(old_value, "adb_OptVariantPart427", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_OptVariantPart427"):
                opp_val = getattr(value, "adb_OptVariantPart427", None)
                setattr(value, "adb_OptVariantPart427", self)

class adb_OptVariantPart:

    pass
class adb_SimpleExpression:

    def __init__(self, unaryAddingOperator: str, binaryAddingOperators: str, adb_SimpleExpression415: "adb_SignedIntegerTypeDefinition" = None, adb_SimpleExpression: "adb_SignedIntegerTypeDefinition" = None, adb_SimpleExpression450: "adb_ComponentClause" = None, adb_SimpleExpression453: "adb_ComponentClause" = None, adb_SimpleExpression470: "adb_RealRangeSpecification" = None, adb_SimpleExpression473: "adb_RealRangeSpecification" = None, adb_SimpleExpression489: set["adb_Term"] = None, adb_SimpleExpression480: "adb_Relation" = None, adb_SimpleExpression483: "adb_Relation" = None, adb_SimpleExpression514: "adb_DigitsConstraint" = None, adb_SimpleExpression518: "adb_DeltaConstraint" = None, adb_SimpleExpression572: "adb_ExplicitRange" = None, adb_SimpleExpression575: "adb_ExplicitRange" = None):
        self.unaryAddingOperator = unaryAddingOperator
        self.binaryAddingOperators = binaryAddingOperators
        self.adb_SimpleExpression415 = adb_SimpleExpression415
        self.adb_SimpleExpression = adb_SimpleExpression
        self.adb_SimpleExpression450 = adb_SimpleExpression450
        self.adb_SimpleExpression453 = adb_SimpleExpression453
        self.adb_SimpleExpression470 = adb_SimpleExpression470
        self.adb_SimpleExpression473 = adb_SimpleExpression473
        self.adb_SimpleExpression489 = adb_SimpleExpression489 if adb_SimpleExpression489 is not None else set()
        self.adb_SimpleExpression480 = adb_SimpleExpression480
        self.adb_SimpleExpression483 = adb_SimpleExpression483
        self.adb_SimpleExpression514 = adb_SimpleExpression514
        self.adb_SimpleExpression518 = adb_SimpleExpression518
        self.adb_SimpleExpression572 = adb_SimpleExpression572
        self.adb_SimpleExpression575 = adb_SimpleExpression575
        
    @property
    def binaryAddingOperators(self) -> str:
        return self.__binaryAddingOperators

    @binaryAddingOperators.setter
    def binaryAddingOperators(self, binaryAddingOperators: str):
        self.__binaryAddingOperators = binaryAddingOperators

    @property
    def unaryAddingOperator(self) -> str:
        return self.__unaryAddingOperator

    @unaryAddingOperator.setter
    def unaryAddingOperator(self, unaryAddingOperator: str):
        self.__unaryAddingOperator = unaryAddingOperator

    @property
    def adb_SimpleExpression473(self):
        return self.__adb_SimpleExpression473

    @adb_SimpleExpression473.setter
    def adb_SimpleExpression473(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_SimpleExpression__adb_SimpleExpression473", None)
        self.__adb_SimpleExpression473 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_RealRangeSpecification472"):
                opp_val = getattr(old_value, "adb_RealRangeSpecification472", None)
                if opp_val == self:
                    setattr(old_value, "adb_RealRangeSpecification472", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_RealRangeSpecification472"):
                opp_val = getattr(value, "adb_RealRangeSpecification472", None)
                setattr(value, "adb_RealRangeSpecification472", self)

    @property
    def adb_SimpleExpression489(self):
        return self.__adb_SimpleExpression489

    @adb_SimpleExpression489.setter
    def adb_SimpleExpression489(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_SimpleExpression__adb_SimpleExpression489", None)
        self.__adb_SimpleExpression489 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adb_Term"):
                    opp_val = getattr(item, "adb_Term", None)
                    
                    if opp_val == self:
                        setattr(item, "adb_Term", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adb_Term"):
                    opp_val = getattr(item, "adb_Term", None)
                    
                    setattr(item, "adb_Term", self)
                    

    @property
    def adb_SimpleExpression514(self):
        return self.__adb_SimpleExpression514

    @adb_SimpleExpression514.setter
    def adb_SimpleExpression514(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_SimpleExpression__adb_SimpleExpression514", None)
        self.__adb_SimpleExpression514 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_DigitsConstraint"):
                opp_val = getattr(old_value, "adb_DigitsConstraint", None)
                if opp_val == self:
                    setattr(old_value, "adb_DigitsConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_DigitsConstraint"):
                opp_val = getattr(value, "adb_DigitsConstraint", None)
                setattr(value, "adb_DigitsConstraint", self)

    @property
    def adb_SimpleExpression450(self):
        return self.__adb_SimpleExpression450

    @adb_SimpleExpression450.setter
    def adb_SimpleExpression450(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_SimpleExpression__adb_SimpleExpression450", None)
        self.__adb_SimpleExpression450 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_ComponentClause449"):
                opp_val = getattr(old_value, "adb_ComponentClause449", None)
                if opp_val == self:
                    setattr(old_value, "adb_ComponentClause449", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_ComponentClause449"):
                opp_val = getattr(value, "adb_ComponentClause449", None)
                setattr(value, "adb_ComponentClause449", self)

    @property
    def adb_SimpleExpression575(self):
        return self.__adb_SimpleExpression575

    @adb_SimpleExpression575.setter
    def adb_SimpleExpression575(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_SimpleExpression__adb_SimpleExpression575", None)
        self.__adb_SimpleExpression575 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_ExplicitRange574"):
                opp_val = getattr(old_value, "adb_ExplicitRange574", None)
                if opp_val == self:
                    setattr(old_value, "adb_ExplicitRange574", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_ExplicitRange574"):
                opp_val = getattr(value, "adb_ExplicitRange574", None)
                setattr(value, "adb_ExplicitRange574", self)

    @property
    def adb_SimpleExpression415(self):
        return self.__adb_SimpleExpression415

    @adb_SimpleExpression415.setter
    def adb_SimpleExpression415(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_SimpleExpression__adb_SimpleExpression415", None)
        self.__adb_SimpleExpression415 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_SignedIntegerTypeDefinition414"):
                opp_val = getattr(old_value, "adb_SignedIntegerTypeDefinition414", None)
                if opp_val == self:
                    setattr(old_value, "adb_SignedIntegerTypeDefinition414", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_SignedIntegerTypeDefinition414"):
                opp_val = getattr(value, "adb_SignedIntegerTypeDefinition414", None)
                setattr(value, "adb_SignedIntegerTypeDefinition414", self)

    @property
    def adb_SimpleExpression453(self):
        return self.__adb_SimpleExpression453

    @adb_SimpleExpression453.setter
    def adb_SimpleExpression453(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_SimpleExpression__adb_SimpleExpression453", None)
        self.__adb_SimpleExpression453 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_ComponentClause452"):
                opp_val = getattr(old_value, "adb_ComponentClause452", None)
                if opp_val == self:
                    setattr(old_value, "adb_ComponentClause452", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_ComponentClause452"):
                opp_val = getattr(value, "adb_ComponentClause452", None)
                setattr(value, "adb_ComponentClause452", self)

    @property
    def adb_SimpleExpression572(self):
        return self.__adb_SimpleExpression572

    @adb_SimpleExpression572.setter
    def adb_SimpleExpression572(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_SimpleExpression__adb_SimpleExpression572", None)
        self.__adb_SimpleExpression572 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_ExplicitRange"):
                opp_val = getattr(old_value, "adb_ExplicitRange", None)
                if opp_val == self:
                    setattr(old_value, "adb_ExplicitRange", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_ExplicitRange"):
                opp_val = getattr(value, "adb_ExplicitRange", None)
                setattr(value, "adb_ExplicitRange", self)

    @property
    def adb_SimpleExpression518(self):
        return self.__adb_SimpleExpression518

    @adb_SimpleExpression518.setter
    def adb_SimpleExpression518(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_SimpleExpression__adb_SimpleExpression518", None)
        self.__adb_SimpleExpression518 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_DeltaConstraint"):
                opp_val = getattr(old_value, "adb_DeltaConstraint", None)
                if opp_val == self:
                    setattr(old_value, "adb_DeltaConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_DeltaConstraint"):
                opp_val = getattr(value, "adb_DeltaConstraint", None)
                setattr(value, "adb_DeltaConstraint", self)

    @property
    def adb_SimpleExpression483(self):
        return self.__adb_SimpleExpression483

    @adb_SimpleExpression483.setter
    def adb_SimpleExpression483(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_SimpleExpression__adb_SimpleExpression483", None)
        self.__adb_SimpleExpression483 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_Relation482"):
                opp_val = getattr(old_value, "adb_Relation482", None)
                if opp_val == self:
                    setattr(old_value, "adb_Relation482", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_Relation482"):
                opp_val = getattr(value, "adb_Relation482", None)
                setattr(value, "adb_Relation482", self)

    @property
    def adb_SimpleExpression480(self):
        return self.__adb_SimpleExpression480

    @adb_SimpleExpression480.setter
    def adb_SimpleExpression480(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_SimpleExpression__adb_SimpleExpression480", None)
        self.__adb_SimpleExpression480 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_Relation479"):
                opp_val = getattr(old_value, "adb_Relation479", None)
                if opp_val == self:
                    setattr(old_value, "adb_Relation479", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_Relation479"):
                opp_val = getattr(value, "adb_Relation479", None)
                setattr(value, "adb_Relation479", self)

    @property
    def adb_SimpleExpression(self):
        return self.__adb_SimpleExpression

    @adb_SimpleExpression.setter
    def adb_SimpleExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_SimpleExpression__adb_SimpleExpression", None)
        self.__adb_SimpleExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_SignedIntegerTypeDefinition"):
                opp_val = getattr(old_value, "adb_SignedIntegerTypeDefinition", None)
                if opp_val == self:
                    setattr(old_value, "adb_SignedIntegerTypeDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_SignedIntegerTypeDefinition"):
                opp_val = getattr(value, "adb_SignedIntegerTypeDefinition", None)
                setattr(value, "adb_SignedIntegerTypeDefinition", self)

    @property
    def adb_SimpleExpression470(self):
        return self.__adb_SimpleExpression470

    @adb_SimpleExpression470.setter
    def adb_SimpleExpression470(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_SimpleExpression__adb_SimpleExpression470", None)
        self.__adb_SimpleExpression470 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_RealRangeSpecification469"):
                opp_val = getattr(old_value, "adb_RealRangeSpecification469", None)
                if opp_val == self:
                    setattr(old_value, "adb_RealRangeSpecification469", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_RealRangeSpecification469"):
                opp_val = getattr(value, "adb_RealRangeSpecification469", None)
                setattr(value, "adb_RealRangeSpecification469", self)

class IntegerTypeDefinition:

    pass
class adb_SignedIntegerTypeDefinition(IntegerTypeDefinition):

    pass
class adb_ModularTypeDefinition(IntegerTypeDefinition):

    pass
class adb_ParameterSpecification:

    pass
class ArrayIndexes:

    pass
class adb_ConstrainedIndexes(ArrayIndexes):

    pass
class adb_UnconstrainedIndexes(ArrayIndexes):

    pass
class adb_ComponentDefinition:

    def __init__(self, aliased: bool, adb_ComponentDefinition370: "adb_AnonymousAccessDefinition" = None, adb_ComponentDefinition: "adb_ArrayTypeDefinition" = None, adb_ComponentDefinition367: "adb_SubtypeIndication" = None, adb_ComponentDefinition432: "adb_ComponentDeclaration" = None):
        self.aliased = aliased
        self.adb_ComponentDefinition370 = adb_ComponentDefinition370
        self.adb_ComponentDefinition = adb_ComponentDefinition
        self.adb_ComponentDefinition367 = adb_ComponentDefinition367
        self.adb_ComponentDefinition432 = adb_ComponentDefinition432
        
    @property
    def aliased(self) -> bool:
        return self.__aliased

    @aliased.setter
    def aliased(self, aliased: bool):
        self.__aliased = aliased

    @property
    def adb_ComponentDefinition(self):
        return self.__adb_ComponentDefinition

    @adb_ComponentDefinition.setter
    def adb_ComponentDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_ComponentDefinition__adb_ComponentDefinition", None)
        self.__adb_ComponentDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_ArrayTypeDefinition361"):
                opp_val = getattr(old_value, "adb_ArrayTypeDefinition361", None)
                if opp_val == self:
                    setattr(old_value, "adb_ArrayTypeDefinition361", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_ArrayTypeDefinition361"):
                opp_val = getattr(value, "adb_ArrayTypeDefinition361", None)
                setattr(value, "adb_ArrayTypeDefinition361", self)

    @property
    def adb_ComponentDefinition367(self):
        return self.__adb_ComponentDefinition367

    @adb_ComponentDefinition367.setter
    def adb_ComponentDefinition367(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_ComponentDefinition__adb_ComponentDefinition367", None)
        self.__adb_ComponentDefinition367 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_SubtypeIndication368"):
                opp_val = getattr(old_value, "adb_SubtypeIndication368", None)
                if opp_val == self:
                    setattr(old_value, "adb_SubtypeIndication368", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_SubtypeIndication368"):
                opp_val = getattr(value, "adb_SubtypeIndication368", None)
                setattr(value, "adb_SubtypeIndication368", self)

    @property
    def adb_ComponentDefinition432(self):
        return self.__adb_ComponentDefinition432

    @adb_ComponentDefinition432.setter
    def adb_ComponentDefinition432(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_ComponentDefinition__adb_ComponentDefinition432", None)
        self.__adb_ComponentDefinition432 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_ComponentDeclaration431"):
                opp_val = getattr(old_value, "adb_ComponentDeclaration431", None)
                if opp_val == self:
                    setattr(old_value, "adb_ComponentDeclaration431", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_ComponentDeclaration431"):
                opp_val = getattr(value, "adb_ComponentDeclaration431", None)
                setattr(value, "adb_ComponentDeclaration431", self)

    @property
    def adb_ComponentDefinition370(self):
        return self.__adb_ComponentDefinition370

    @adb_ComponentDefinition370.setter
    def adb_ComponentDefinition370(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_ComponentDefinition__adb_ComponentDefinition370", None)
        self.__adb_ComponentDefinition370 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_AnonymousAccessDefinition371"):
                opp_val = getattr(old_value, "adb_AnonymousAccessDefinition371", None)
                if opp_val == self:
                    setattr(old_value, "adb_AnonymousAccessDefinition371", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_AnonymousAccessDefinition371"):
                opp_val = getattr(value, "adb_AnonymousAccessDefinition371", None)
                setattr(value, "adb_AnonymousAccessDefinition371", self)

class adb_ArrayIndexes:

    pass
class ReturnSubtypeIndication:

    pass
class NotNullAccessDefinition:

    pass
class adb_AccessToDataInstance(NotNullAccessDefinition):

    def __init__(self, constant: str, adb_AccessToDataInstance: "adb_Name" = None):
        self.constant = constant
        self.adb_AccessToDataInstance = adb_AccessToDataInstance
        
    @property
    def constant(self) -> str:
        return self.__constant

    @constant.setter
    def constant(self, constant: str):
        self.__constant = constant

    @property
    def adb_AccessToDataInstance(self):
        return self.__adb_AccessToDataInstance

    @adb_AccessToDataInstance.setter
    def adb_AccessToDataInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_AccessToDataInstance__adb_AccessToDataInstance", None)
        self.__adb_AccessToDataInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_Name379"):
                opp_val = getattr(old_value, "adb_Name379", None)
                if opp_val == self:
                    setattr(old_value, "adb_Name379", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_Name379"):
                opp_val = getattr(value, "adb_Name379", None)
                setattr(value, "adb_Name379", self)

class AccessSpecification:

    pass
class adb_AccessToDataDefinition(AccessSpecification):

    def __init__(self, generalAccessModifier: str, adb_AccessToDataDefinition: "adb_SubtypeIndication" = None):
        self.generalAccessModifier = generalAccessModifier
        self.adb_AccessToDataDefinition = adb_AccessToDataDefinition
        
    @property
    def generalAccessModifier(self) -> str:
        return self.__generalAccessModifier

    @generalAccessModifier.setter
    def generalAccessModifier(self, generalAccessModifier: str):
        self.__generalAccessModifier = generalAccessModifier

    @property
    def adb_AccessToDataDefinition(self):
        return self.__adb_AccessToDataDefinition

    @adb_AccessToDataDefinition.setter
    def adb_AccessToDataDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_AccessToDataDefinition__adb_AccessToDataDefinition", None)
        self.__adb_AccessToDataDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_SubtypeIndication357"):
                opp_val = getattr(old_value, "adb_SubtypeIndication357", None)
                if opp_val == self:
                    setattr(old_value, "adb_SubtypeIndication357", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_SubtypeIndication357"):
                opp_val = getattr(value, "adb_SubtypeIndication357", None)
                setattr(value, "adb_SubtypeIndication357", self)

class adb_AccessToSubprogramDefinition(NotNullAccessDefinition, AccessSpecification):

    def __init__(self, protected: bool, adb_AccessToSubprogramDefinition354: "adb_ParameterAndResultProfile" = None, adb_AccessToSubprogramDefinition: "adb_FormalPart" = None):
        self.protected = protected
        self.adb_AccessToSubprogramDefinition354 = adb_AccessToSubprogramDefinition354
        self.adb_AccessToSubprogramDefinition = adb_AccessToSubprogramDefinition
        
    @property
    def protected(self) -> bool:
        return self.__protected

    @protected.setter
    def protected(self, protected: bool):
        self.__protected = protected

    @property
    def adb_AccessToSubprogramDefinition(self):
        return self.__adb_AccessToSubprogramDefinition

    @adb_AccessToSubprogramDefinition.setter
    def adb_AccessToSubprogramDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_AccessToSubprogramDefinition__adb_AccessToSubprogramDefinition", None)
        self.__adb_AccessToSubprogramDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_FormalPart352"):
                opp_val = getattr(old_value, "adb_FormalPart352", None)
                if opp_val == self:
                    setattr(old_value, "adb_FormalPart352", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_FormalPart352"):
                opp_val = getattr(value, "adb_FormalPart352", None)
                setattr(value, "adb_FormalPart352", self)

    @property
    def adb_AccessToSubprogramDefinition354(self):
        return self.__adb_AccessToSubprogramDefinition354

    @adb_AccessToSubprogramDefinition354.setter
    def adb_AccessToSubprogramDefinition354(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_AccessToSubprogramDefinition__adb_AccessToSubprogramDefinition354", None)
        self.__adb_AccessToSubprogramDefinition354 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_ParameterAndResultProfile355"):
                opp_val = getattr(old_value, "adb_ParameterAndResultProfile355", None)
                if opp_val == self:
                    setattr(old_value, "adb_ParameterAndResultProfile355", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_ParameterAndResultProfile355"):
                opp_val = getattr(value, "adb_ParameterAndResultProfile355", None)
                setattr(value, "adb_ParameterAndResultProfile355", self)

class TypeDefinition:

    pass
class adb_IntegerTypeDefinition(TypeDefinition):

    pass
class adb_EnumerationTypeDefinition(TypeDefinition):

    def __init__(self, enumerationliteralspecifications: str):
        self.enumerationliteralspecifications = enumerationliteralspecifications
        
    @property
    def enumerationliteralspecifications(self) -> str:
        return self.__enumerationliteralspecifications

    @enumerationliteralspecifications.setter
    def enumerationliteralspecifications(self, enumerationliteralspecifications: str):
        self.__enumerationliteralspecifications = enumerationliteralspecifications

class adb_RealTypeDefinition(TypeDefinition):

    pass
class adb_DerivedTypeDefinition(TypeDefinition):

    def __init__(self, abstract: str, limited: str, adb_DerivedTypeDefinition: "adb_SubtypeIndication" = None, adb_DerivedTypeDefinition341: "adb_InterfaceList" = None, adb_DerivedTypeDefinition344: "adb_RecordExtensionPart" = None):
        self.abstract = abstract
        self.limited = limited
        self.adb_DerivedTypeDefinition = adb_DerivedTypeDefinition
        self.adb_DerivedTypeDefinition341 = adb_DerivedTypeDefinition341
        self.adb_DerivedTypeDefinition344 = adb_DerivedTypeDefinition344
        
    @property
    def limited(self) -> str:
        return self.__limited

    @limited.setter
    def limited(self, limited: str):
        self.__limited = limited

    @property
    def abstract(self) -> str:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: str):
        self.__abstract = abstract

    @property
    def adb_DerivedTypeDefinition344(self):
        return self.__adb_DerivedTypeDefinition344

    @adb_DerivedTypeDefinition344.setter
    def adb_DerivedTypeDefinition344(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_DerivedTypeDefinition__adb_DerivedTypeDefinition344", None)
        self.__adb_DerivedTypeDefinition344 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_RecordExtensionPart"):
                opp_val = getattr(old_value, "adb_RecordExtensionPart", None)
                if opp_val == self:
                    setattr(old_value, "adb_RecordExtensionPart", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_RecordExtensionPart"):
                opp_val = getattr(value, "adb_RecordExtensionPart", None)
                setattr(value, "adb_RecordExtensionPart", self)

    @property
    def adb_DerivedTypeDefinition(self):
        return self.__adb_DerivedTypeDefinition

    @adb_DerivedTypeDefinition.setter
    def adb_DerivedTypeDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_DerivedTypeDefinition__adb_DerivedTypeDefinition", None)
        self.__adb_DerivedTypeDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_SubtypeIndication339"):
                opp_val = getattr(old_value, "adb_SubtypeIndication339", None)
                if opp_val == self:
                    setattr(old_value, "adb_SubtypeIndication339", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_SubtypeIndication339"):
                opp_val = getattr(value, "adb_SubtypeIndication339", None)
                setattr(value, "adb_SubtypeIndication339", self)

    @property
    def adb_DerivedTypeDefinition341(self):
        return self.__adb_DerivedTypeDefinition341

    @adb_DerivedTypeDefinition341.setter
    def adb_DerivedTypeDefinition341(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_DerivedTypeDefinition__adb_DerivedTypeDefinition341", None)
        self.__adb_DerivedTypeDefinition341 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_InterfaceList342"):
                opp_val = getattr(old_value, "adb_InterfaceList342", None)
                if opp_val == self:
                    setattr(old_value, "adb_InterfaceList342", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_InterfaceList342"):
                opp_val = getattr(value, "adb_InterfaceList342", None)
                setattr(value, "adb_InterfaceList342", self)

class adb_RecordTypeDefinition(TypeDefinition):

    def __init__(self, abstract: bool, tagged: bool, limited: bool, adb_RecordTypeDefinition: "adb_RecordDefinition" = None):
        self.abstract = abstract
        self.tagged = tagged
        self.limited = limited
        self.adb_RecordTypeDefinition = adb_RecordTypeDefinition
        
    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def tagged(self) -> bool:
        return self.__tagged

    @tagged.setter
    def tagged(self, tagged: bool):
        self.__tagged = tagged

    @property
    def limited(self) -> bool:
        return self.__limited

    @limited.setter
    def limited(self, limited: bool):
        self.__limited = limited

    @property
    def adb_RecordTypeDefinition(self):
        return self.__adb_RecordTypeDefinition

    @adb_RecordTypeDefinition.setter
    def adb_RecordTypeDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_RecordTypeDefinition__adb_RecordTypeDefinition", None)
        self.__adb_RecordTypeDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_RecordDefinition419"):
                opp_val = getattr(old_value, "adb_RecordDefinition419", None)
                if opp_val == self:
                    setattr(old_value, "adb_RecordDefinition419", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_RecordDefinition419"):
                opp_val = getattr(value, "adb_RecordDefinition419", None)
                setattr(value, "adb_RecordDefinition419", self)

class adb_AccessSpecification:

    pass
class adb_RecordDefinition:

    def __init__(self, null: str, adb_RecordDefinition: "adb_RecordExtensionPart" = None, adb_RecordDefinition419: "adb_RecordTypeDefinition" = None, adb_RecordDefinition421: "adb_ComponentList" = None):
        self.null = null
        self.adb_RecordDefinition = adb_RecordDefinition
        self.adb_RecordDefinition419 = adb_RecordDefinition419
        self.adb_RecordDefinition421 = adb_RecordDefinition421
        
    @property
    def null(self) -> str:
        return self.__null

    @null.setter
    def null(self, null: str):
        self.__null = null

    @property
    def adb_RecordDefinition419(self):
        return self.__adb_RecordDefinition419

    @adb_RecordDefinition419.setter
    def adb_RecordDefinition419(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_RecordDefinition__adb_RecordDefinition419", None)
        self.__adb_RecordDefinition419 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_RecordTypeDefinition"):
                opp_val = getattr(old_value, "adb_RecordTypeDefinition", None)
                if opp_val == self:
                    setattr(old_value, "adb_RecordTypeDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_RecordTypeDefinition"):
                opp_val = getattr(value, "adb_RecordTypeDefinition", None)
                setattr(value, "adb_RecordTypeDefinition", self)

    @property
    def adb_RecordDefinition421(self):
        return self.__adb_RecordDefinition421

    @adb_RecordDefinition421.setter
    def adb_RecordDefinition421(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_RecordDefinition__adb_RecordDefinition421", None)
        self.__adb_RecordDefinition421 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_ComponentList"):
                opp_val = getattr(old_value, "adb_ComponentList", None)
                if opp_val == self:
                    setattr(old_value, "adb_ComponentList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_ComponentList"):
                opp_val = getattr(value, "adb_ComponentList", None)
                setattr(value, "adb_ComponentList", self)

    @property
    def adb_RecordDefinition(self):
        return self.__adb_RecordDefinition

    @adb_RecordDefinition.setter
    def adb_RecordDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_RecordDefinition__adb_RecordDefinition", None)
        self.__adb_RecordDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_RecordExtensionPart346"):
                opp_val = getattr(old_value, "adb_RecordExtensionPart346", None)
                if opp_val == self:
                    setattr(old_value, "adb_RecordExtensionPart346", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_RecordExtensionPart346"):
                opp_val = getattr(value, "adb_RecordExtensionPart346", None)
                setattr(value, "adb_RecordExtensionPart346", self)

class adb_RecordExtensionPart:

    pass
class adb_DiscriminantSpecification:

    pass
class DiscriminantPart:

    pass
class adb_UnknownDiscriminantPart(DiscriminantPart):

    def __init__(self, box: bool):
        self.box = box
        
    @property
    def box(self) -> bool:
        return self.__box

    @box.setter
    def box(self, box: bool):
        self.__box = box

class adb_ExplicitGenericActualParameter:

    pass
class adb_NotNullAccessDefinition:

    pass
class AbortStatement:

    pass
class adb_TaskNames(AbortStatement):

    pass
class adb_TriggeringStatement:

    pass
class adb_AbortablePart:

    pass
class adb_TriggeringAlternative:

    pass
class SelectAlternative:

    pass
class adb_AcceptAlternative(SelectAlternative):

    pass
class adb_EntryCallAlternative:

    pass
class adb_DelayAlternative(SelectAlternative):

    pass
class adb_GuardedAlternative:

    pass
class adb_SelectAlternative:

    pass
class adb_Guard:

    pass
class SelectStatement:

    pass
class adb_ConditionalEntryCall(SelectStatement):

    pass
class adb_TimedEntryCall(SelectStatement):

    pass
class adb_AsynchronousSelect(SelectStatement):

    pass
class adb_EntryBarrier:

    pass
class adb_SelectiveAccept(SelectStatement):

    pass
class adb_EntryBodyFormalPart:

    pass
class adb_EntryIndexSpecification:

    def __init__(self, name: str, adb_EntryIndexSpecification: "adb_EntryBodyFormalPart" = None, adb_EntryIndexSpecification251: "adb_DiscreteSubtypeDefinition" = None):
        self.name = name
        self.adb_EntryIndexSpecification = adb_EntryIndexSpecification
        self.adb_EntryIndexSpecification251 = adb_EntryIndexSpecification251
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def adb_EntryIndexSpecification(self):
        return self.__adb_EntryIndexSpecification

    @adb_EntryIndexSpecification.setter
    def adb_EntryIndexSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_EntryIndexSpecification__adb_EntryIndexSpecification", None)
        self.__adb_EntryIndexSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_EntryBodyFormalPart243"):
                opp_val = getattr(old_value, "adb_EntryBodyFormalPart243", None)
                if opp_val == self:
                    setattr(old_value, "adb_EntryBodyFormalPart243", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_EntryBodyFormalPart243"):
                opp_val = getattr(value, "adb_EntryBodyFormalPart243", None)
                setattr(value, "adb_EntryBodyFormalPart243", self)

    @property
    def adb_EntryIndexSpecification251(self):
        return self.__adb_EntryIndexSpecification251

    @adb_EntryIndexSpecification251.setter
    def adb_EntryIndexSpecification251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_EntryIndexSpecification__adb_EntryIndexSpecification251", None)
        self.__adb_EntryIndexSpecification251 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_DiscreteSubtypeDefinition252"):
                opp_val = getattr(old_value, "adb_DiscreteSubtypeDefinition252", None)
                if opp_val == self:
                    setattr(old_value, "adb_DiscreteSubtypeDefinition252", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_DiscreteSubtypeDefinition252"):
                opp_val = getattr(value, "adb_DiscreteSubtypeDefinition252", None)
                setattr(value, "adb_DiscreteSubtypeDefinition252", self)

class adb_EntryIndex:

    pass
class adb_ProtectedOperationItem:

    pass
class TriggeringStatement:

    pass
class adb_ReturnSubtypeIndication:

    pass
class adb_LoopParameterSpecification:

    def __init__(self, identifier: str, adb_LoopParameterSpecification196: "adb_DiscreteSubtypeDefinition" = None, adb_LoopParameterSpecification: "adb_IterationScheme" = None):
        self.identifier = identifier
        self.adb_LoopParameterSpecification196 = adb_LoopParameterSpecification196
        self.adb_LoopParameterSpecification = adb_LoopParameterSpecification
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def adb_LoopParameterSpecification(self):
        return self.__adb_LoopParameterSpecification

    @adb_LoopParameterSpecification.setter
    def adb_LoopParameterSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_LoopParameterSpecification__adb_LoopParameterSpecification", None)
        self.__adb_LoopParameterSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_IterationScheme194"):
                opp_val = getattr(old_value, "adb_IterationScheme194", None)
                if opp_val == self:
                    setattr(old_value, "adb_IterationScheme194", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_IterationScheme194"):
                opp_val = getattr(value, "adb_IterationScheme194", None)
                setattr(value, "adb_IterationScheme194", self)

    @property
    def adb_LoopParameterSpecification196(self):
        return self.__adb_LoopParameterSpecification196

    @adb_LoopParameterSpecification196.setter
    def adb_LoopParameterSpecification196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_LoopParameterSpecification__adb_LoopParameterSpecification196", None)
        self.__adb_LoopParameterSpecification196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_DiscreteSubtypeDefinition197"):
                opp_val = getattr(old_value, "adb_DiscreteSubtypeDefinition197", None)
                if opp_val == self:
                    setattr(old_value, "adb_DiscreteSubtypeDefinition197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_DiscreteSubtypeDefinition197"):
                opp_val = getattr(value, "adb_DiscreteSubtypeDefinition197", None)
                setattr(value, "adb_DiscreteSubtypeDefinition197", self)

class adb_IterationScheme:

    pass
class CompoundStatement:

    pass
class adb_ExtendedReturnStatement(CompoundStatement):

    def __init__(self, identifier: str, adb_ExtendedReturnStatement: "adb_ReturnSubtypeIndication" = None, adb_ExtendedReturnStatement209: "adb_Expression" = None, adb_ExtendedReturnStatement212: "adb_HandledSequenceOfStatements" = None):
        self.identifier = identifier
        self.adb_ExtendedReturnStatement = adb_ExtendedReturnStatement
        self.adb_ExtendedReturnStatement209 = adb_ExtendedReturnStatement209
        self.adb_ExtendedReturnStatement212 = adb_ExtendedReturnStatement212
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def adb_ExtendedReturnStatement209(self):
        return self.__adb_ExtendedReturnStatement209

    @adb_ExtendedReturnStatement209.setter
    def adb_ExtendedReturnStatement209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_ExtendedReturnStatement__adb_ExtendedReturnStatement209", None)
        self.__adb_ExtendedReturnStatement209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_Expression210"):
                opp_val = getattr(old_value, "adb_Expression210", None)
                if opp_val == self:
                    setattr(old_value, "adb_Expression210", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_Expression210"):
                opp_val = getattr(value, "adb_Expression210", None)
                setattr(value, "adb_Expression210", self)

    @property
    def adb_ExtendedReturnStatement(self):
        return self.__adb_ExtendedReturnStatement

    @adb_ExtendedReturnStatement.setter
    def adb_ExtendedReturnStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_ExtendedReturnStatement__adb_ExtendedReturnStatement", None)
        self.__adb_ExtendedReturnStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_ReturnSubtypeIndication"):
                opp_val = getattr(old_value, "adb_ReturnSubtypeIndication", None)
                if opp_val == self:
                    setattr(old_value, "adb_ReturnSubtypeIndication", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_ReturnSubtypeIndication"):
                opp_val = getattr(value, "adb_ReturnSubtypeIndication", None)
                setattr(value, "adb_ReturnSubtypeIndication", self)

    @property
    def adb_ExtendedReturnStatement212(self):
        return self.__adb_ExtendedReturnStatement212

    @adb_ExtendedReturnStatement212.setter
    def adb_ExtendedReturnStatement212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_ExtendedReturnStatement__adb_ExtendedReturnStatement212", None)
        self.__adb_ExtendedReturnStatement212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_HandledSequenceOfStatements213"):
                opp_val = getattr(old_value, "adb_HandledSequenceOfStatements213", None)
                if opp_val == self:
                    setattr(old_value, "adb_HandledSequenceOfStatements213", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_HandledSequenceOfStatements213"):
                opp_val = getattr(value, "adb_HandledSequenceOfStatements213", None)
                setattr(value, "adb_HandledSequenceOfStatements213", self)

class adb_SelectStatement(CompoundStatement):

    pass
class adb_AcceptStatement(CompoundStatement):

    def __init__(self, entryidentifier: str, adb_AcceptStatement: "adb_EntryDeclaration" = None, adb_AcceptStatement229: "adb_EntryIndex" = None, adb_AcceptStatement231: "adb_FormalPart" = None, adb_AcceptStatement234: "adb_HandledSequenceOfStatements" = None, adb_AcceptStatement278: "adb_AcceptAlternative" = None):
        self.entryidentifier = entryidentifier
        self.adb_AcceptStatement = adb_AcceptStatement
        self.adb_AcceptStatement229 = adb_AcceptStatement229
        self.adb_AcceptStatement231 = adb_AcceptStatement231
        self.adb_AcceptStatement234 = adb_AcceptStatement234
        self.adb_AcceptStatement278 = adb_AcceptStatement278
        
    @property
    def entryidentifier(self) -> str:
        return self.__entryidentifier

    @entryidentifier.setter
    def entryidentifier(self, entryidentifier: str):
        self.__entryidentifier = entryidentifier

    @property
    def adb_AcceptStatement234(self):
        return self.__adb_AcceptStatement234

    @adb_AcceptStatement234.setter
    def adb_AcceptStatement234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_AcceptStatement__adb_AcceptStatement234", None)
        self.__adb_AcceptStatement234 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_HandledSequenceOfStatements235"):
                opp_val = getattr(old_value, "adb_HandledSequenceOfStatements235", None)
                if opp_val == self:
                    setattr(old_value, "adb_HandledSequenceOfStatements235", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_HandledSequenceOfStatements235"):
                opp_val = getattr(value, "adb_HandledSequenceOfStatements235", None)
                setattr(value, "adb_HandledSequenceOfStatements235", self)

    @property
    def adb_AcceptStatement(self):
        return self.__adb_AcceptStatement

    @adb_AcceptStatement.setter
    def adb_AcceptStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_AcceptStatement__adb_AcceptStatement", None)
        self.__adb_AcceptStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_EntryDeclaration227"):
                opp_val = getattr(old_value, "adb_EntryDeclaration227", None)
                if opp_val == self:
                    setattr(old_value, "adb_EntryDeclaration227", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_EntryDeclaration227"):
                opp_val = getattr(value, "adb_EntryDeclaration227", None)
                setattr(value, "adb_EntryDeclaration227", self)

    @property
    def adb_AcceptStatement278(self):
        return self.__adb_AcceptStatement278

    @adb_AcceptStatement278.setter
    def adb_AcceptStatement278(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_AcceptStatement__adb_AcceptStatement278", None)
        self.__adb_AcceptStatement278 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_AcceptAlternative"):
                opp_val = getattr(old_value, "adb_AcceptAlternative", None)
                if opp_val == self:
                    setattr(old_value, "adb_AcceptAlternative", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_AcceptAlternative"):
                opp_val = getattr(value, "adb_AcceptAlternative", None)
                setattr(value, "adb_AcceptAlternative", self)

    @property
    def adb_AcceptStatement231(self):
        return self.__adb_AcceptStatement231

    @adb_AcceptStatement231.setter
    def adb_AcceptStatement231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_AcceptStatement__adb_AcceptStatement231", None)
        self.__adb_AcceptStatement231 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_FormalPart232"):
                opp_val = getattr(old_value, "adb_FormalPart232", None)
                if opp_val == self:
                    setattr(old_value, "adb_FormalPart232", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_FormalPart232"):
                opp_val = getattr(value, "adb_FormalPart232", None)
                setattr(value, "adb_FormalPart232", self)

    @property
    def adb_AcceptStatement229(self):
        return self.__adb_AcceptStatement229

    @adb_AcceptStatement229.setter
    def adb_AcceptStatement229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_AcceptStatement__adb_AcceptStatement229", None)
        self.__adb_AcceptStatement229 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_EntryIndex"):
                opp_val = getattr(old_value, "adb_EntryIndex", None)
                if opp_val == self:
                    setattr(old_value, "adb_EntryIndex", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_EntryIndex"):
                opp_val = getattr(value, "adb_EntryIndex", None)
                setattr(value, "adb_EntryIndex", self)

class adb_IfStatement(CompoundStatement):

    pass
class adb_LoopStatement(CompoundStatement):

    def __init__(self, name: str, sameName: str, adb_LoopStatement199: "adb_ExitStatement" = None, adb_LoopStatement: "adb_IterationScheme" = None, adb_LoopStatement188: "adb_SequenceOfStatements" = None):
        self.name = name
        self.sameName = sameName
        self.adb_LoopStatement199 = adb_LoopStatement199
        self.adb_LoopStatement = adb_LoopStatement
        self.adb_LoopStatement188 = adb_LoopStatement188
        
    @property
    def sameName(self) -> str:
        return self.__sameName

    @sameName.setter
    def sameName(self, sameName: str):
        self.__sameName = sameName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def adb_LoopStatement188(self):
        return self.__adb_LoopStatement188

    @adb_LoopStatement188.setter
    def adb_LoopStatement188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_LoopStatement__adb_LoopStatement188", None)
        self.__adb_LoopStatement188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_SequenceOfStatements189"):
                opp_val = getattr(old_value, "adb_SequenceOfStatements189", None)
                if opp_val == self:
                    setattr(old_value, "adb_SequenceOfStatements189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_SequenceOfStatements189"):
                opp_val = getattr(value, "adb_SequenceOfStatements189", None)
                setattr(value, "adb_SequenceOfStatements189", self)

    @property
    def adb_LoopStatement199(self):
        return self.__adb_LoopStatement199

    @adb_LoopStatement199.setter
    def adb_LoopStatement199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_LoopStatement__adb_LoopStatement199", None)
        self.__adb_LoopStatement199 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_ExitStatement"):
                opp_val = getattr(old_value, "adb_ExitStatement", None)
                if opp_val == self:
                    setattr(old_value, "adb_ExitStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_ExitStatement"):
                opp_val = getattr(value, "adb_ExitStatement", None)
                setattr(value, "adb_ExitStatement", self)

    @property
    def adb_LoopStatement(self):
        return self.__adb_LoopStatement

    @adb_LoopStatement.setter
    def adb_LoopStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_LoopStatement__adb_LoopStatement", None)
        self.__adb_LoopStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_IterationScheme"):
                opp_val = getattr(old_value, "adb_IterationScheme", None)
                if opp_val == self:
                    setattr(old_value, "adb_IterationScheme", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_IterationScheme"):
                opp_val = getattr(value, "adb_IterationScheme", None)
                setattr(value, "adb_IterationScheme", self)

class adb_DiscreteChoiceList:

    pass
class adb_CaseStatementAlternative:

    pass
class adb_CaseStatement(CompoundStatement):

    pass
class adb_PragmaArgumentAssociation:

    def __init__(self, name: str, adb_PragmaArgumentAssociation: "adb_Pragma" = None, adb_PragmaArgumentAssociation149: "adb_Expression" = None):
        self.name = name
        self.adb_PragmaArgumentAssociation = adb_PragmaArgumentAssociation
        self.adb_PragmaArgumentAssociation149 = adb_PragmaArgumentAssociation149
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def adb_PragmaArgumentAssociation(self):
        return self.__adb_PragmaArgumentAssociation

    @adb_PragmaArgumentAssociation.setter
    def adb_PragmaArgumentAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_PragmaArgumentAssociation__adb_PragmaArgumentAssociation", None)
        self.__adb_PragmaArgumentAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_Pragma147"):
                opp_val = getattr(old_value, "adb_Pragma147", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_Pragma147"):
                opp_val = getattr(value, "adb_Pragma147", None)
                if opp_val is None:
                    setattr(value, "adb_Pragma147", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def adb_PragmaArgumentAssociation149(self):
        return self.__adb_PragmaArgumentAssociation149

    @adb_PragmaArgumentAssociation149.setter
    def adb_PragmaArgumentAssociation149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_PragmaArgumentAssociation__adb_PragmaArgumentAssociation149", None)
        self.__adb_PragmaArgumentAssociation149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_Expression150"):
                opp_val = getattr(old_value, "adb_Expression150", None)
                if opp_val == self:
                    setattr(old_value, "adb_Expression150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_Expression150"):
                opp_val = getattr(value, "adb_Expression150", None)
                setattr(value, "adb_Expression150", self)

class ObjectDeclaration:

    pass
class adb_SingleProtectedDeclaration(ObjectDeclaration):

    def __init__(self, name: str, adb_SingleProtectedDeclaration: "adb_InterfaceList" = None, adb_SingleProtectedDeclaration144: "adb_ProtectedDefinition" = None):
        self.name = name
        self.adb_SingleProtectedDeclaration = adb_SingleProtectedDeclaration
        self.adb_SingleProtectedDeclaration144 = adb_SingleProtectedDeclaration144
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def adb_SingleProtectedDeclaration(self):
        return self.__adb_SingleProtectedDeclaration

    @adb_SingleProtectedDeclaration.setter
    def adb_SingleProtectedDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_SingleProtectedDeclaration__adb_SingleProtectedDeclaration", None)
        self.__adb_SingleProtectedDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_InterfaceList142"):
                opp_val = getattr(old_value, "adb_InterfaceList142", None)
                if opp_val == self:
                    setattr(old_value, "adb_InterfaceList142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_InterfaceList142"):
                opp_val = getattr(value, "adb_InterfaceList142", None)
                setattr(value, "adb_InterfaceList142", self)

    @property
    def adb_SingleProtectedDeclaration144(self):
        return self.__adb_SingleProtectedDeclaration144

    @adb_SingleProtectedDeclaration144.setter
    def adb_SingleProtectedDeclaration144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_SingleProtectedDeclaration__adb_SingleProtectedDeclaration144", None)
        self.__adb_SingleProtectedDeclaration144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_ProtectedDefinition145"):
                opp_val = getattr(old_value, "adb_ProtectedDefinition145", None)
                if opp_val == self:
                    setattr(old_value, "adb_ProtectedDefinition145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_ProtectedDefinition145"):
                opp_val = getattr(value, "adb_ProtectedDefinition145", None)
                setattr(value, "adb_ProtectedDefinition145", self)

class adb_FormalPackageActualPart:

    def __init__(self, box: bool, adb_FormalPackageActualPart117: set["adb_FormalPackageAssociation"] = None, adb_FormalPackageActualPart: "adb_FormalPackageDeclaration" = None, adb_FormalPackageActualPart114: "adb_GenericActualPart" = None):
        self.box = box
        self.adb_FormalPackageActualPart117 = adb_FormalPackageActualPart117 if adb_FormalPackageActualPart117 is not None else set()
        self.adb_FormalPackageActualPart = adb_FormalPackageActualPart
        self.adb_FormalPackageActualPart114 = adb_FormalPackageActualPart114
        
    @property
    def box(self) -> bool:
        return self.__box

    @box.setter
    def box(self, box: bool):
        self.__box = box

    @property
    def adb_FormalPackageActualPart(self):
        return self.__adb_FormalPackageActualPart

    @adb_FormalPackageActualPart.setter
    def adb_FormalPackageActualPart(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_FormalPackageActualPart__adb_FormalPackageActualPart", None)
        self.__adb_FormalPackageActualPart = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_FormalPackageDeclaration"):
                opp_val = getattr(old_value, "adb_FormalPackageDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "adb_FormalPackageDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_FormalPackageDeclaration"):
                opp_val = getattr(value, "adb_FormalPackageDeclaration", None)
                setattr(value, "adb_FormalPackageDeclaration", self)

    @property
    def adb_FormalPackageActualPart114(self):
        return self.__adb_FormalPackageActualPart114

    @adb_FormalPackageActualPart114.setter
    def adb_FormalPackageActualPart114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_FormalPackageActualPart__adb_FormalPackageActualPart114", None)
        self.__adb_FormalPackageActualPart114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_GenericActualPart115"):
                opp_val = getattr(old_value, "adb_GenericActualPart115", None)
                if opp_val == self:
                    setattr(old_value, "adb_GenericActualPart115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_GenericActualPart115"):
                opp_val = getattr(value, "adb_GenericActualPart115", None)
                setattr(value, "adb_GenericActualPart115", self)

    @property
    def adb_FormalPackageActualPart117(self):
        return self.__adb_FormalPackageActualPart117

    @adb_FormalPackageActualPart117.setter
    def adb_FormalPackageActualPart117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_FormalPackageActualPart__adb_FormalPackageActualPart117", None)
        self.__adb_FormalPackageActualPart117 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adb_FormalPackageAssociation"):
                    opp_val = getattr(item, "adb_FormalPackageAssociation", None)
                    
                    if opp_val == self:
                        setattr(item, "adb_FormalPackageAssociation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adb_FormalPackageAssociation"):
                    opp_val = getattr(item, "adb_FormalPackageAssociation", None)
                    
                    setattr(item, "adb_FormalPackageAssociation", self)
                    

class adb_DataInstanceDeclaration(ObjectDeclaration):

    def __init__(self, aliased: bool, constant: bool, adb_DataInstanceDeclaration137: "adb_AnonymousAccessDefinition" = None, adb_DataInstanceDeclaration140: "adb_ArrayTypeDefinition" = None, adb_DataInstanceDeclaration: "adb_DefiningIdentifierList" = None, adb_DataInstanceDeclaration128: "adb_SubtypeIndication" = None, adb_DataInstanceDeclaration131: "adb_Expression" = None, adb_DataInstanceDeclaration134: "adb_Name" = None):
        self.aliased = aliased
        self.constant = constant
        self.adb_DataInstanceDeclaration137 = adb_DataInstanceDeclaration137
        self.adb_DataInstanceDeclaration140 = adb_DataInstanceDeclaration140
        self.adb_DataInstanceDeclaration = adb_DataInstanceDeclaration
        self.adb_DataInstanceDeclaration128 = adb_DataInstanceDeclaration128
        self.adb_DataInstanceDeclaration131 = adb_DataInstanceDeclaration131
        self.adb_DataInstanceDeclaration134 = adb_DataInstanceDeclaration134
        
    @property
    def aliased(self) -> bool:
        return self.__aliased

    @aliased.setter
    def aliased(self, aliased: bool):
        self.__aliased = aliased

    @property
    def constant(self) -> bool:
        return self.__constant

    @constant.setter
    def constant(self, constant: bool):
        self.__constant = constant

    @property
    def adb_DataInstanceDeclaration131(self):
        return self.__adb_DataInstanceDeclaration131

    @adb_DataInstanceDeclaration131.setter
    def adb_DataInstanceDeclaration131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_DataInstanceDeclaration__adb_DataInstanceDeclaration131", None)
        self.__adb_DataInstanceDeclaration131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_Expression132"):
                opp_val = getattr(old_value, "adb_Expression132", None)
                if opp_val == self:
                    setattr(old_value, "adb_Expression132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_Expression132"):
                opp_val = getattr(value, "adb_Expression132", None)
                setattr(value, "adb_Expression132", self)

    @property
    def adb_DataInstanceDeclaration(self):
        return self.__adb_DataInstanceDeclaration

    @adb_DataInstanceDeclaration.setter
    def adb_DataInstanceDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_DataInstanceDeclaration__adb_DataInstanceDeclaration", None)
        self.__adb_DataInstanceDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_DefiningIdentifierList126"):
                opp_val = getattr(old_value, "adb_DefiningIdentifierList126", None)
                if opp_val == self:
                    setattr(old_value, "adb_DefiningIdentifierList126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_DefiningIdentifierList126"):
                opp_val = getattr(value, "adb_DefiningIdentifierList126", None)
                setattr(value, "adb_DefiningIdentifierList126", self)

    @property
    def adb_DataInstanceDeclaration134(self):
        return self.__adb_DataInstanceDeclaration134

    @adb_DataInstanceDeclaration134.setter
    def adb_DataInstanceDeclaration134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_DataInstanceDeclaration__adb_DataInstanceDeclaration134", None)
        self.__adb_DataInstanceDeclaration134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_Name135"):
                opp_val = getattr(old_value, "adb_Name135", None)
                if opp_val == self:
                    setattr(old_value, "adb_Name135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_Name135"):
                opp_val = getattr(value, "adb_Name135", None)
                setattr(value, "adb_Name135", self)

    @property
    def adb_DataInstanceDeclaration137(self):
        return self.__adb_DataInstanceDeclaration137

    @adb_DataInstanceDeclaration137.setter
    def adb_DataInstanceDeclaration137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_DataInstanceDeclaration__adb_DataInstanceDeclaration137", None)
        self.__adb_DataInstanceDeclaration137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_AnonymousAccessDefinition138"):
                opp_val = getattr(old_value, "adb_AnonymousAccessDefinition138", None)
                if opp_val == self:
                    setattr(old_value, "adb_AnonymousAccessDefinition138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_AnonymousAccessDefinition138"):
                opp_val = getattr(value, "adb_AnonymousAccessDefinition138", None)
                setattr(value, "adb_AnonymousAccessDefinition138", self)

    @property
    def adb_DataInstanceDeclaration128(self):
        return self.__adb_DataInstanceDeclaration128

    @adb_DataInstanceDeclaration128.setter
    def adb_DataInstanceDeclaration128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_DataInstanceDeclaration__adb_DataInstanceDeclaration128", None)
        self.__adb_DataInstanceDeclaration128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_SubtypeIndication129"):
                opp_val = getattr(old_value, "adb_SubtypeIndication129", None)
                if opp_val == self:
                    setattr(old_value, "adb_SubtypeIndication129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_SubtypeIndication129"):
                opp_val = getattr(value, "adb_SubtypeIndication129", None)
                setattr(value, "adb_SubtypeIndication129", self)

    @property
    def adb_DataInstanceDeclaration140(self):
        return self.__adb_DataInstanceDeclaration140

    @adb_DataInstanceDeclaration140.setter
    def adb_DataInstanceDeclaration140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_DataInstanceDeclaration__adb_DataInstanceDeclaration140", None)
        self.__adb_DataInstanceDeclaration140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_ArrayTypeDefinition"):
                opp_val = getattr(old_value, "adb_ArrayTypeDefinition", None)
                if opp_val == self:
                    setattr(old_value, "adb_ArrayTypeDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_ArrayTypeDefinition"):
                opp_val = getattr(value, "adb_ArrayTypeDefinition", None)
                setattr(value, "adb_ArrayTypeDefinition", self)

class adb_GenericAssociation:

    def __init__(self, selectorName: str, adb_GenericAssociation: "adb_FormalPackageAssociation" = None, adb_GenericAssociation314: "adb_GenericActualPart" = None, adb_GenericAssociation316: "adb_ExplicitGenericActualParameter" = None):
        self.selectorName = selectorName
        self.adb_GenericAssociation = adb_GenericAssociation
        self.adb_GenericAssociation314 = adb_GenericAssociation314
        self.adb_GenericAssociation316 = adb_GenericAssociation316
        
    @property
    def selectorName(self) -> str:
        return self.__selectorName

    @selectorName.setter
    def selectorName(self, selectorName: str):
        self.__selectorName = selectorName

    @property
    def adb_GenericAssociation316(self):
        return self.__adb_GenericAssociation316

    @adb_GenericAssociation316.setter
    def adb_GenericAssociation316(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_GenericAssociation__adb_GenericAssociation316", None)
        self.__adb_GenericAssociation316 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_ExplicitGenericActualParameter"):
                opp_val = getattr(old_value, "adb_ExplicitGenericActualParameter", None)
                if opp_val == self:
                    setattr(old_value, "adb_ExplicitGenericActualParameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_ExplicitGenericActualParameter"):
                opp_val = getattr(value, "adb_ExplicitGenericActualParameter", None)
                setattr(value, "adb_ExplicitGenericActualParameter", self)

    @property
    def adb_GenericAssociation314(self):
        return self.__adb_GenericAssociation314

    @adb_GenericAssociation314.setter
    def adb_GenericAssociation314(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_GenericAssociation__adb_GenericAssociation314", None)
        self.__adb_GenericAssociation314 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_GenericActualPart313"):
                opp_val = getattr(old_value, "adb_GenericActualPart313", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_GenericActualPart313"):
                opp_val = getattr(value, "adb_GenericActualPart313", None)
                if opp_val is None:
                    setattr(value, "adb_GenericActualPart313", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def adb_GenericAssociation(self):
        return self.__adb_GenericAssociation

    @adb_GenericAssociation.setter
    def adb_GenericAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_GenericAssociation__adb_GenericAssociation", None)
        self.__adb_GenericAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_FormalPackageAssociation119"):
                opp_val = getattr(old_value, "adb_FormalPackageAssociation119", None)
                if opp_val == self:
                    setattr(old_value, "adb_FormalPackageAssociation119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_FormalPackageAssociation119"):
                opp_val = getattr(value, "adb_FormalPackageAssociation119", None)
                setattr(value, "adb_FormalPackageAssociation119", self)

class adb_FormalPackageAssociation:

    def __init__(self, genericFormalParameterSelectorName: str, adb_FormalPackageAssociation: "adb_FormalPackageActualPart" = None, adb_FormalPackageAssociation119: "adb_GenericAssociation" = None):
        self.genericFormalParameterSelectorName = genericFormalParameterSelectorName
        self.adb_FormalPackageAssociation = adb_FormalPackageAssociation
        self.adb_FormalPackageAssociation119 = adb_FormalPackageAssociation119
        
    @property
    def genericFormalParameterSelectorName(self) -> str:
        return self.__genericFormalParameterSelectorName

    @genericFormalParameterSelectorName.setter
    def genericFormalParameterSelectorName(self, genericFormalParameterSelectorName: str):
        self.__genericFormalParameterSelectorName = genericFormalParameterSelectorName

    @property
    def adb_FormalPackageAssociation119(self):
        return self.__adb_FormalPackageAssociation119

    @adb_FormalPackageAssociation119.setter
    def adb_FormalPackageAssociation119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_FormalPackageAssociation__adb_FormalPackageAssociation119", None)
        self.__adb_FormalPackageAssociation119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_GenericAssociation"):
                opp_val = getattr(old_value, "adb_GenericAssociation", None)
                if opp_val == self:
                    setattr(old_value, "adb_GenericAssociation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_GenericAssociation"):
                opp_val = getattr(value, "adb_GenericAssociation", None)
                setattr(value, "adb_GenericAssociation", self)

    @property
    def adb_FormalPackageAssociation(self):
        return self.__adb_FormalPackageAssociation

    @adb_FormalPackageAssociation.setter
    def adb_FormalPackageAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_FormalPackageAssociation__adb_FormalPackageAssociation", None)
        self.__adb_FormalPackageAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_FormalPackageActualPart117"):
                opp_val = getattr(old_value, "adb_FormalPackageActualPart117", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_FormalPackageActualPart117"):
                opp_val = getattr(value, "adb_FormalPackageActualPart117", None)
                if opp_val is None:
                    setattr(value, "adb_FormalPackageActualPart117", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class FormalTypeDefinition:

    pass
class adb_FormalDerivedTypeDefinition(FormalTypeDefinition):

    def __init__(self, absract: str, limited: bool, synchronized: bool, adb_FormalDerivedTypeDefinition: "adb_Name" = None, adb_FormalDerivedTypeDefinition106: "adb_InterfaceList" = None):
        self.absract = absract
        self.limited = limited
        self.synchronized = synchronized
        self.adb_FormalDerivedTypeDefinition = adb_FormalDerivedTypeDefinition
        self.adb_FormalDerivedTypeDefinition106 = adb_FormalDerivedTypeDefinition106
        
    @property
    def limited(self) -> bool:
        return self.__limited

    @limited.setter
    def limited(self, limited: bool):
        self.__limited = limited

    @property
    def synchronized(self) -> bool:
        return self.__synchronized

    @synchronized.setter
    def synchronized(self, synchronized: bool):
        self.__synchronized = synchronized

    @property
    def absract(self) -> str:
        return self.__absract

    @absract.setter
    def absract(self, absract: str):
        self.__absract = absract

    @property
    def adb_FormalDerivedTypeDefinition106(self):
        return self.__adb_FormalDerivedTypeDefinition106

    @adb_FormalDerivedTypeDefinition106.setter
    def adb_FormalDerivedTypeDefinition106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_FormalDerivedTypeDefinition__adb_FormalDerivedTypeDefinition106", None)
        self.__adb_FormalDerivedTypeDefinition106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_InterfaceList107"):
                opp_val = getattr(old_value, "adb_InterfaceList107", None)
                if opp_val == self:
                    setattr(old_value, "adb_InterfaceList107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_InterfaceList107"):
                opp_val = getattr(value, "adb_InterfaceList107", None)
                setattr(value, "adb_InterfaceList107", self)

    @property
    def adb_FormalDerivedTypeDefinition(self):
        return self.__adb_FormalDerivedTypeDefinition

    @adb_FormalDerivedTypeDefinition.setter
    def adb_FormalDerivedTypeDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_FormalDerivedTypeDefinition__adb_FormalDerivedTypeDefinition", None)
        self.__adb_FormalDerivedTypeDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_Name104"):
                opp_val = getattr(old_value, "adb_Name104", None)
                if opp_val == self:
                    setattr(old_value, "adb_Name104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_Name104"):
                opp_val = getattr(value, "adb_Name104", None)
                setattr(value, "adb_Name104", self)

class adb_AccessTypeDefinition(TypeDefinition, FormalTypeDefinition):

    pass
class adb_ArrayTypeDefinition(TypeDefinition, FormalTypeDefinition):

    pass
class adb_InterfaceTypeDefinition(TypeDefinition, FormalTypeDefinition):

    def __init__(self, limited: bool, task: bool, protected: bool, synchro: bool, adb_InterfaceTypeDefinition: "adb_InterfaceList" = None):
        self.limited = limited
        self.task = task
        self.protected = protected
        self.synchro = synchro
        self.adb_InterfaceTypeDefinition = adb_InterfaceTypeDefinition
        
    @property
    def task(self) -> bool:
        return self.__task

    @task.setter
    def task(self, task: bool):
        self.__task = task

    @property
    def protected(self) -> bool:
        return self.__protected

    @protected.setter
    def protected(self, protected: bool):
        self.__protected = protected

    @property
    def synchro(self) -> bool:
        return self.__synchro

    @synchro.setter
    def synchro(self, synchro: bool):
        self.__synchro = synchro

    @property
    def limited(self) -> bool:
        return self.__limited

    @limited.setter
    def limited(self, limited: bool):
        self.__limited = limited

    @property
    def adb_InterfaceTypeDefinition(self):
        return self.__adb_InterfaceTypeDefinition

    @adb_InterfaceTypeDefinition.setter
    def adb_InterfaceTypeDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_InterfaceTypeDefinition__adb_InterfaceTypeDefinition", None)
        self.__adb_InterfaceTypeDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_InterfaceList337"):
                opp_val = getattr(old_value, "adb_InterfaceList337", None)
                if opp_val == self:
                    setattr(old_value, "adb_InterfaceList337", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_InterfaceList337"):
                opp_val = getattr(value, "adb_InterfaceList337", None)
                setattr(value, "adb_InterfaceList337", self)

class adb_FormalPrivateTypeDefinition(FormalTypeDefinition):

    def __init__(self, abstract: bool, tagged: bool, limited: bool):
        self.abstract = abstract
        self.tagged = tagged
        self.limited = limited
        
    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def limited(self) -> bool:
        return self.__limited

    @limited.setter
    def limited(self, limited: bool):
        self.__limited = limited

    @property
    def tagged(self) -> bool:
        return self.__tagged

    @tagged.setter
    def tagged(self, tagged: bool):
        self.__tagged = tagged

class adb_FormalTypeDefinition:

    pass
class adb_SubprogramDefault:

    def __init__(self, defaultName: str, adb_SubprogramDefault: "adb_FormalSubprogramDeclaration" = None):
        self.defaultName = defaultName
        self.adb_SubprogramDefault = adb_SubprogramDefault
        
    @property
    def defaultName(self) -> str:
        return self.__defaultName

    @defaultName.setter
    def defaultName(self, defaultName: str):
        self.__defaultName = defaultName

    @property
    def adb_SubprogramDefault(self):
        return self.__adb_SubprogramDefault

    @adb_SubprogramDefault.setter
    def adb_SubprogramDefault(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_SubprogramDefault__adb_SubprogramDefault", None)
        self.__adb_SubprogramDefault = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_FormalSubprogramDeclaration111"):
                opp_val = getattr(old_value, "adb_FormalSubprogramDeclaration111", None)
                if opp_val == self:
                    setattr(old_value, "adb_FormalSubprogramDeclaration111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_FormalSubprogramDeclaration111"):
                opp_val = getattr(value, "adb_FormalSubprogramDeclaration111", None)
                setattr(value, "adb_FormalSubprogramDeclaration111", self)

class adb_DefiningIdentifierList:

    def __init__(self, name: str, adb_DefiningIdentifierList: "adb_FormalObjectDeclaration" = None, adb_DefiningIdentifierList121: "adb_ExceptionDeclaration" = None, adb_DefiningIdentifierList126: "adb_DataInstanceDeclaration" = None, adb_DefiningIdentifierList154: "adb_NumberDeclaration" = None, adb_DefiningIdentifierList321: "adb_DiscriminantSpecification" = None, adb_DefiningIdentifierList396: "adb_ParameterSpecification" = None, adb_DefiningIdentifierList429: "adb_ComponentDeclaration" = None):
        self.name = name
        self.adb_DefiningIdentifierList = adb_DefiningIdentifierList
        self.adb_DefiningIdentifierList121 = adb_DefiningIdentifierList121
        self.adb_DefiningIdentifierList126 = adb_DefiningIdentifierList126
        self.adb_DefiningIdentifierList154 = adb_DefiningIdentifierList154
        self.adb_DefiningIdentifierList321 = adb_DefiningIdentifierList321
        self.adb_DefiningIdentifierList396 = adb_DefiningIdentifierList396
        self.adb_DefiningIdentifierList429 = adb_DefiningIdentifierList429
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def adb_DefiningIdentifierList121(self):
        return self.__adb_DefiningIdentifierList121

    @adb_DefiningIdentifierList121.setter
    def adb_DefiningIdentifierList121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_DefiningIdentifierList__adb_DefiningIdentifierList121", None)
        self.__adb_DefiningIdentifierList121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_ExceptionDeclaration"):
                opp_val = getattr(old_value, "adb_ExceptionDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "adb_ExceptionDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_ExceptionDeclaration"):
                opp_val = getattr(value, "adb_ExceptionDeclaration", None)
                setattr(value, "adb_ExceptionDeclaration", self)

    @property
    def adb_DefiningIdentifierList429(self):
        return self.__adb_DefiningIdentifierList429

    @adb_DefiningIdentifierList429.setter
    def adb_DefiningIdentifierList429(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_DefiningIdentifierList__adb_DefiningIdentifierList429", None)
        self.__adb_DefiningIdentifierList429 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_ComponentDeclaration"):
                opp_val = getattr(old_value, "adb_ComponentDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "adb_ComponentDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_ComponentDeclaration"):
                opp_val = getattr(value, "adb_ComponentDeclaration", None)
                setattr(value, "adb_ComponentDeclaration", self)

    @property
    def adb_DefiningIdentifierList396(self):
        return self.__adb_DefiningIdentifierList396

    @adb_DefiningIdentifierList396.setter
    def adb_DefiningIdentifierList396(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_DefiningIdentifierList__adb_DefiningIdentifierList396", None)
        self.__adb_DefiningIdentifierList396 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_ParameterSpecification395"):
                opp_val = getattr(old_value, "adb_ParameterSpecification395", None)
                if opp_val == self:
                    setattr(old_value, "adb_ParameterSpecification395", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_ParameterSpecification395"):
                opp_val = getattr(value, "adb_ParameterSpecification395", None)
                setattr(value, "adb_ParameterSpecification395", self)

    @property
    def adb_DefiningIdentifierList321(self):
        return self.__adb_DefiningIdentifierList321

    @adb_DefiningIdentifierList321.setter
    def adb_DefiningIdentifierList321(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_DefiningIdentifierList__adb_DefiningIdentifierList321", None)
        self.__adb_DefiningIdentifierList321 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_DiscriminantSpecification320"):
                opp_val = getattr(old_value, "adb_DiscriminantSpecification320", None)
                if opp_val == self:
                    setattr(old_value, "adb_DiscriminantSpecification320", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_DiscriminantSpecification320"):
                opp_val = getattr(value, "adb_DiscriminantSpecification320", None)
                setattr(value, "adb_DiscriminantSpecification320", self)

    @property
    def adb_DefiningIdentifierList126(self):
        return self.__adb_DefiningIdentifierList126

    @adb_DefiningIdentifierList126.setter
    def adb_DefiningIdentifierList126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_DefiningIdentifierList__adb_DefiningIdentifierList126", None)
        self.__adb_DefiningIdentifierList126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_DataInstanceDeclaration"):
                opp_val = getattr(old_value, "adb_DataInstanceDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "adb_DataInstanceDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_DataInstanceDeclaration"):
                opp_val = getattr(value, "adb_DataInstanceDeclaration", None)
                setattr(value, "adb_DataInstanceDeclaration", self)

    @property
    def adb_DefiningIdentifierList(self):
        return self.__adb_DefiningIdentifierList

    @adb_DefiningIdentifierList.setter
    def adb_DefiningIdentifierList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_DefiningIdentifierList__adb_DefiningIdentifierList", None)
        self.__adb_DefiningIdentifierList = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_FormalObjectDeclaration"):
                opp_val = getattr(old_value, "adb_FormalObjectDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "adb_FormalObjectDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_FormalObjectDeclaration"):
                opp_val = getattr(value, "adb_FormalObjectDeclaration", None)
                setattr(value, "adb_FormalObjectDeclaration", self)

    @property
    def adb_DefiningIdentifierList154(self):
        return self.__adb_DefiningIdentifierList154

    @adb_DefiningIdentifierList154.setter
    def adb_DefiningIdentifierList154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_DefiningIdentifierList__adb_DefiningIdentifierList154", None)
        self.__adb_DefiningIdentifierList154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_NumberDeclaration"):
                opp_val = getattr(old_value, "adb_NumberDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "adb_NumberDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_NumberDeclaration"):
                opp_val = getattr(value, "adb_NumberDeclaration", None)
                setattr(value, "adb_NumberDeclaration", self)

class GenericFormalParameterDeclaration:

    pass
class adb_FormalPackageDeclaration(GenericFormalParameterDeclaration):

    def __init__(self, name: str, genericPackageName: str, adb_FormalPackageDeclaration: "adb_FormalPackageActualPart" = None):
        self.name = name
        self.genericPackageName = genericPackageName
        self.adb_FormalPackageDeclaration = adb_FormalPackageDeclaration
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def genericPackageName(self) -> str:
        return self.__genericPackageName

    @genericPackageName.setter
    def genericPackageName(self, genericPackageName: str):
        self.__genericPackageName = genericPackageName

    @property
    def adb_FormalPackageDeclaration(self):
        return self.__adb_FormalPackageDeclaration

    @adb_FormalPackageDeclaration.setter
    def adb_FormalPackageDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_FormalPackageDeclaration__adb_FormalPackageDeclaration", None)
        self.__adb_FormalPackageDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_FormalPackageActualPart"):
                opp_val = getattr(old_value, "adb_FormalPackageActualPart", None)
                if opp_val == self:
                    setattr(old_value, "adb_FormalPackageActualPart", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_FormalPackageActualPart"):
                opp_val = getattr(value, "adb_FormalPackageActualPart", None)
                setattr(value, "adb_FormalPackageActualPart", self)

class adb_FormalSubprogramDeclaration(GenericFormalParameterDeclaration):

    def __init__(self, abstract: str, adb_FormalSubprogramDeclaration: "adb_SubprogramSpecification" = None, adb_FormalSubprogramDeclaration111: "adb_SubprogramDefault" = None):
        self.abstract = abstract
        self.adb_FormalSubprogramDeclaration = adb_FormalSubprogramDeclaration
        self.adb_FormalSubprogramDeclaration111 = adb_FormalSubprogramDeclaration111
        
    @property
    def abstract(self) -> str:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: str):
        self.__abstract = abstract

    @property
    def adb_FormalSubprogramDeclaration(self):
        return self.__adb_FormalSubprogramDeclaration

    @adb_FormalSubprogramDeclaration.setter
    def adb_FormalSubprogramDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_FormalSubprogramDeclaration__adb_FormalSubprogramDeclaration", None)
        self.__adb_FormalSubprogramDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_SubprogramSpecification109"):
                opp_val = getattr(old_value, "adb_SubprogramSpecification109", None)
                if opp_val == self:
                    setattr(old_value, "adb_SubprogramSpecification109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_SubprogramSpecification109"):
                opp_val = getattr(value, "adb_SubprogramSpecification109", None)
                setattr(value, "adb_SubprogramSpecification109", self)

    @property
    def adb_FormalSubprogramDeclaration111(self):
        return self.__adb_FormalSubprogramDeclaration111

    @adb_FormalSubprogramDeclaration111.setter
    def adb_FormalSubprogramDeclaration111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_FormalSubprogramDeclaration__adb_FormalSubprogramDeclaration111", None)
        self.__adb_FormalSubprogramDeclaration111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_SubprogramDefault"):
                opp_val = getattr(old_value, "adb_SubprogramDefault", None)
                if opp_val == self:
                    setattr(old_value, "adb_SubprogramDefault", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_SubprogramDefault"):
                opp_val = getattr(value, "adb_SubprogramDefault", None)
                setattr(value, "adb_SubprogramDefault", self)

class adb_FormalTypeDeclaration(GenericFormalParameterDeclaration):

    def __init__(self, identifier: str, adb_FormalTypeDeclaration: "adb_DiscriminantPart" = None, adb_FormalTypeDeclaration102: "adb_FormalTypeDefinition" = None):
        self.identifier = identifier
        self.adb_FormalTypeDeclaration = adb_FormalTypeDeclaration
        self.adb_FormalTypeDeclaration102 = adb_FormalTypeDeclaration102
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def adb_FormalTypeDeclaration102(self):
        return self.__adb_FormalTypeDeclaration102

    @adb_FormalTypeDeclaration102.setter
    def adb_FormalTypeDeclaration102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_FormalTypeDeclaration__adb_FormalTypeDeclaration102", None)
        self.__adb_FormalTypeDeclaration102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_FormalTypeDefinition"):
                opp_val = getattr(old_value, "adb_FormalTypeDefinition", None)
                if opp_val == self:
                    setattr(old_value, "adb_FormalTypeDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_FormalTypeDefinition"):
                opp_val = getattr(value, "adb_FormalTypeDefinition", None)
                setattr(value, "adb_FormalTypeDefinition", self)

    @property
    def adb_FormalTypeDeclaration(self):
        return self.__adb_FormalTypeDeclaration

    @adb_FormalTypeDeclaration.setter
    def adb_FormalTypeDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_FormalTypeDeclaration__adb_FormalTypeDeclaration", None)
        self.__adb_FormalTypeDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_DiscriminantPart100"):
                opp_val = getattr(old_value, "adb_DiscriminantPart100", None)
                if opp_val == self:
                    setattr(old_value, "adb_DiscriminantPart100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_DiscriminantPart100"):
                opp_val = getattr(value, "adb_DiscriminantPart100", None)
                setattr(value, "adb_DiscriminantPart100", self)

class adb_FormalObjectDeclaration(GenericFormalParameterDeclaration):

    pass
class adb_GenericItem:

    pass
class SimpleStatement:

    pass
class adb_AssignmentStatement(SimpleStatement):

    pass
class adb_DelayStatement(TriggeringStatement, SimpleStatement):

    def __init__(self, until: str, adb_DelayStatement: "adb_Expression" = None, adb_DelayStatement280: "adb_DelayAlternative" = None):
        self.until = until
        self.adb_DelayStatement = adb_DelayStatement
        self.adb_DelayStatement280 = adb_DelayStatement280
        
    @property
    def until(self) -> str:
        return self.__until

    @until.setter
    def until(self, until: str):
        self.__until = until

    @property
    def adb_DelayStatement280(self):
        return self.__adb_DelayStatement280

    @adb_DelayStatement280.setter
    def adb_DelayStatement280(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_DelayStatement__adb_DelayStatement280", None)
        self.__adb_DelayStatement280 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_DelayAlternative"):
                opp_val = getattr(old_value, "adb_DelayAlternative", None)
                if opp_val == self:
                    setattr(old_value, "adb_DelayAlternative", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_DelayAlternative"):
                opp_val = getattr(value, "adb_DelayAlternative", None)
                setattr(value, "adb_DelayAlternative", self)

    @property
    def adb_DelayStatement(self):
        return self.__adb_DelayStatement

    @adb_DelayStatement.setter
    def adb_DelayStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_DelayStatement__adb_DelayStatement", None)
        self.__adb_DelayStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_Expression256"):
                opp_val = getattr(old_value, "adb_Expression256", None)
                if opp_val == self:
                    setattr(old_value, "adb_Expression256", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_Expression256"):
                opp_val = getattr(value, "adb_Expression256", None)
                setattr(value, "adb_Expression256", self)

class adb_ExitStatement(SimpleStatement):

    pass
class adb_ProcedureOrEntryCallStatement(TriggeringStatement, SimpleStatement):

    pass
class adb_RequeueStatement(SimpleStatement):

    def __init__(self, abort: bool, adb_RequeueStatement: "adb_Name" = None):
        self.abort = abort
        self.adb_RequeueStatement = adb_RequeueStatement
        
    @property
    def abort(self) -> bool:
        return self.__abort

    @abort.setter
    def abort(self, abort: bool):
        self.__abort = abort

    @property
    def adb_RequeueStatement(self):
        return self.__adb_RequeueStatement

    @adb_RequeueStatement.setter
    def adb_RequeueStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_RequeueStatement__adb_RequeueStatement", None)
        self.__adb_RequeueStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_Name254"):
                opp_val = getattr(old_value, "adb_Name254", None)
                if opp_val == self:
                    setattr(old_value, "adb_Name254", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_Name254"):
                opp_val = getattr(value, "adb_Name254", None)
                setattr(value, "adb_Name254", self)

class adb_GotoStatement(SimpleStatement):

    def __init__(self, labelId: str):
        self.labelId = labelId
        
    @property
    def labelId(self) -> str:
        return self.__labelId

    @labelId.setter
    def labelId(self, labelId: str):
        self.__labelId = labelId

class adb_SimpleReturnStatement(SimpleStatement):

    pass
class adb_AbortStatement(SimpleStatement):

    pass
class adb_RaiseStatement(SimpleStatement):

    pass
class adb_NullStatement(SimpleStatement):

    def __init__(self, null: bool):
        self.null = null
        
    @property
    def null(self) -> bool:
        return self.__null

    @null.setter
    def null(self, null: bool):
        self.__null = null

class adb_Expression(DiscreteChoice, AncestorPart, ParameterEffectiveValue, EntryIndex, ExplicitGenericActualParameter):

    def __init__(self, booleanOperator: str, adb_Expression: "adb_FormalObjectDeclaration" = None, adb_Expression132: "adb_DataInstanceDeclaration" = None, adb_Expression157: "adb_NumberDeclaration" = None, adb_Expression162: "adb_AssignmentStatement" = None, adb_Expression150: "adb_PragmaArgumentAssociation" = None, adb_Expression178: "adb_CaseStatement" = None, adb_Expression164: "adb_IfStatement" = None, adb_Expression170: "adb_IfStatement" = None, adb_Expression202: "adb_ExitStatement" = None, adb_Expression192: "adb_IterationScheme" = None, adb_Expression210: "adb_ExtendedReturnStatement" = None, adb_Expression206: "adb_SimpleReturnStatement" = None, adb_Expression249: "adb_EntryBarrier" = None, adb_Expression256: "adb_DelayStatement" = None, adb_Expression273: "adb_Guard" = None, adb_Expression311: "adb_RaiseStatement" = None, adb_Expression332: "adb_DiscriminantSpecification" = None, adb_Expression411: "adb_ParameterSpecification" = None, adb_Expression417: "adb_ModularTypeDefinition" = None, adb_Expression435: "adb_ComponentDeclaration" = None, adb_Expression437: "adb_AspectClause" = None, adb_Expression444: "adb_ModClause" = None, adb_Expression447: "adb_ComponentClause" = None, adb_Expression465: "adb_RealTypeDefinition" = None, adb_Expression475: "adb_FixedPointDefinition" = None, adb_Expression477: set["adb_Relation"] = None, adb_Expression528: "adb_DiscriminantAssociation" = None, adb_Expression539: "adb_PositionalArrayAggregate" = None, adb_Expression533: "adb_InitializedComponents" = None, adb_Expression542: "adb_PositionalArrayAggregate" = None, adb_Expression549: "adb_ArrayComponentAssociation" = None, adb_Expression570: "adb_EntityRange" = None):
        self.booleanOperator = booleanOperator
        self.adb_Expression = adb_Expression
        self.adb_Expression132 = adb_Expression132
        self.adb_Expression157 = adb_Expression157
        self.adb_Expression162 = adb_Expression162
        self.adb_Expression150 = adb_Expression150
        self.adb_Expression178 = adb_Expression178
        self.adb_Expression164 = adb_Expression164
        self.adb_Expression170 = adb_Expression170
        self.adb_Expression202 = adb_Expression202
        self.adb_Expression192 = adb_Expression192
        self.adb_Expression210 = adb_Expression210
        self.adb_Expression206 = adb_Expression206
        self.adb_Expression249 = adb_Expression249
        self.adb_Expression256 = adb_Expression256
        self.adb_Expression273 = adb_Expression273
        self.adb_Expression311 = adb_Expression311
        self.adb_Expression332 = adb_Expression332
        self.adb_Expression411 = adb_Expression411
        self.adb_Expression417 = adb_Expression417
        self.adb_Expression435 = adb_Expression435
        self.adb_Expression437 = adb_Expression437
        self.adb_Expression444 = adb_Expression444
        self.adb_Expression447 = adb_Expression447
        self.adb_Expression465 = adb_Expression465
        self.adb_Expression475 = adb_Expression475
        self.adb_Expression477 = adb_Expression477 if adb_Expression477 is not None else set()
        self.adb_Expression528 = adb_Expression528
        self.adb_Expression539 = adb_Expression539
        self.adb_Expression533 = adb_Expression533
        self.adb_Expression542 = adb_Expression542
        self.adb_Expression549 = adb_Expression549
        self.adb_Expression570 = adb_Expression570
        
    @property
    def booleanOperator(self) -> str:
        return self.__booleanOperator

    @booleanOperator.setter
    def booleanOperator(self, booleanOperator: str):
        self.__booleanOperator = booleanOperator

    @property
    def adb_Expression332(self):
        return self.__adb_Expression332

    @adb_Expression332.setter
    def adb_Expression332(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Expression__adb_Expression332", None)
        self.__adb_Expression332 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_DiscriminantSpecification331"):
                opp_val = getattr(old_value, "adb_DiscriminantSpecification331", None)
                if opp_val == self:
                    setattr(old_value, "adb_DiscriminantSpecification331", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_DiscriminantSpecification331"):
                opp_val = getattr(value, "adb_DiscriminantSpecification331", None)
                setattr(value, "adb_DiscriminantSpecification331", self)

    @property
    def adb_Expression178(self):
        return self.__adb_Expression178

    @adb_Expression178.setter
    def adb_Expression178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Expression__adb_Expression178", None)
        self.__adb_Expression178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_CaseStatement"):
                opp_val = getattr(old_value, "adb_CaseStatement", None)
                if opp_val == self:
                    setattr(old_value, "adb_CaseStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_CaseStatement"):
                opp_val = getattr(value, "adb_CaseStatement", None)
                setattr(value, "adb_CaseStatement", self)

    @property
    def adb_Expression164(self):
        return self.__adb_Expression164

    @adb_Expression164.setter
    def adb_Expression164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Expression__adb_Expression164", None)
        self.__adb_Expression164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_IfStatement"):
                opp_val = getattr(old_value, "adb_IfStatement", None)
                if opp_val == self:
                    setattr(old_value, "adb_IfStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_IfStatement"):
                opp_val = getattr(value, "adb_IfStatement", None)
                setattr(value, "adb_IfStatement", self)

    @property
    def adb_Expression539(self):
        return self.__adb_Expression539

    @adb_Expression539.setter
    def adb_Expression539(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Expression__adb_Expression539", None)
        self.__adb_Expression539 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_PositionalArrayAggregate"):
                opp_val = getattr(old_value, "adb_PositionalArrayAggregate", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_PositionalArrayAggregate"):
                opp_val = getattr(value, "adb_PositionalArrayAggregate", None)
                if opp_val is None:
                    setattr(value, "adb_PositionalArrayAggregate", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def adb_Expression549(self):
        return self.__adb_Expression549

    @adb_Expression549.setter
    def adb_Expression549(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Expression__adb_Expression549", None)
        self.__adb_Expression549 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_ArrayComponentAssociation548"):
                opp_val = getattr(old_value, "adb_ArrayComponentAssociation548", None)
                if opp_val == self:
                    setattr(old_value, "adb_ArrayComponentAssociation548", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_ArrayComponentAssociation548"):
                opp_val = getattr(value, "adb_ArrayComponentAssociation548", None)
                setattr(value, "adb_ArrayComponentAssociation548", self)

    @property
    def adb_Expression256(self):
        return self.__adb_Expression256

    @adb_Expression256.setter
    def adb_Expression256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Expression__adb_Expression256", None)
        self.__adb_Expression256 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_DelayStatement"):
                opp_val = getattr(old_value, "adb_DelayStatement", None)
                if opp_val == self:
                    setattr(old_value, "adb_DelayStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_DelayStatement"):
                opp_val = getattr(value, "adb_DelayStatement", None)
                setattr(value, "adb_DelayStatement", self)

    @property
    def adb_Expression411(self):
        return self.__adb_Expression411

    @adb_Expression411.setter
    def adb_Expression411(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Expression__adb_Expression411", None)
        self.__adb_Expression411 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_ParameterSpecification410"):
                opp_val = getattr(old_value, "adb_ParameterSpecification410", None)
                if opp_val == self:
                    setattr(old_value, "adb_ParameterSpecification410", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_ParameterSpecification410"):
                opp_val = getattr(value, "adb_ParameterSpecification410", None)
                setattr(value, "adb_ParameterSpecification410", self)

    @property
    def adb_Expression437(self):
        return self.__adb_Expression437

    @adb_Expression437.setter
    def adb_Expression437(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Expression__adb_Expression437", None)
        self.__adb_Expression437 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_AspectClause"):
                opp_val = getattr(old_value, "adb_AspectClause", None)
                if opp_val == self:
                    setattr(old_value, "adb_AspectClause", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_AspectClause"):
                opp_val = getattr(value, "adb_AspectClause", None)
                setattr(value, "adb_AspectClause", self)

    @property
    def adb_Expression542(self):
        return self.__adb_Expression542

    @adb_Expression542.setter
    def adb_Expression542(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Expression__adb_Expression542", None)
        self.__adb_Expression542 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_PositionalArrayAggregate541"):
                opp_val = getattr(old_value, "adb_PositionalArrayAggregate541", None)
                if opp_val == self:
                    setattr(old_value, "adb_PositionalArrayAggregate541", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_PositionalArrayAggregate541"):
                opp_val = getattr(value, "adb_PositionalArrayAggregate541", None)
                setattr(value, "adb_PositionalArrayAggregate541", self)

    @property
    def adb_Expression528(self):
        return self.__adb_Expression528

    @adb_Expression528.setter
    def adb_Expression528(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Expression__adb_Expression528", None)
        self.__adb_Expression528 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_DiscriminantAssociation527"):
                opp_val = getattr(old_value, "adb_DiscriminantAssociation527", None)
                if opp_val == self:
                    setattr(old_value, "adb_DiscriminantAssociation527", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_DiscriminantAssociation527"):
                opp_val = getattr(value, "adb_DiscriminantAssociation527", None)
                setattr(value, "adb_DiscriminantAssociation527", self)

    @property
    def adb_Expression132(self):
        return self.__adb_Expression132

    @adb_Expression132.setter
    def adb_Expression132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Expression__adb_Expression132", None)
        self.__adb_Expression132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_DataInstanceDeclaration131"):
                opp_val = getattr(old_value, "adb_DataInstanceDeclaration131", None)
                if opp_val == self:
                    setattr(old_value, "adb_DataInstanceDeclaration131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_DataInstanceDeclaration131"):
                opp_val = getattr(value, "adb_DataInstanceDeclaration131", None)
                setattr(value, "adb_DataInstanceDeclaration131", self)

    @property
    def adb_Expression150(self):
        return self.__adb_Expression150

    @adb_Expression150.setter
    def adb_Expression150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Expression__adb_Expression150", None)
        self.__adb_Expression150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_PragmaArgumentAssociation149"):
                opp_val = getattr(old_value, "adb_PragmaArgumentAssociation149", None)
                if opp_val == self:
                    setattr(old_value, "adb_PragmaArgumentAssociation149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_PragmaArgumentAssociation149"):
                opp_val = getattr(value, "adb_PragmaArgumentAssociation149", None)
                setattr(value, "adb_PragmaArgumentAssociation149", self)

    @property
    def adb_Expression157(self):
        return self.__adb_Expression157

    @adb_Expression157.setter
    def adb_Expression157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Expression__adb_Expression157", None)
        self.__adb_Expression157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_NumberDeclaration156"):
                opp_val = getattr(old_value, "adb_NumberDeclaration156", None)
                if opp_val == self:
                    setattr(old_value, "adb_NumberDeclaration156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_NumberDeclaration156"):
                opp_val = getattr(value, "adb_NumberDeclaration156", None)
                setattr(value, "adb_NumberDeclaration156", self)

    @property
    def adb_Expression(self):
        return self.__adb_Expression

    @adb_Expression.setter
    def adb_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Expression__adb_Expression", None)
        self.__adb_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_FormalObjectDeclaration98"):
                opp_val = getattr(old_value, "adb_FormalObjectDeclaration98", None)
                if opp_val == self:
                    setattr(old_value, "adb_FormalObjectDeclaration98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_FormalObjectDeclaration98"):
                opp_val = getattr(value, "adb_FormalObjectDeclaration98", None)
                setattr(value, "adb_FormalObjectDeclaration98", self)

    @property
    def adb_Expression444(self):
        return self.__adb_Expression444

    @adb_Expression444.setter
    def adb_Expression444(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Expression__adb_Expression444", None)
        self.__adb_Expression444 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_ModClause443"):
                opp_val = getattr(old_value, "adb_ModClause443", None)
                if opp_val == self:
                    setattr(old_value, "adb_ModClause443", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_ModClause443"):
                opp_val = getattr(value, "adb_ModClause443", None)
                setattr(value, "adb_ModClause443", self)

    @property
    def adb_Expression447(self):
        return self.__adb_Expression447

    @adb_Expression447.setter
    def adb_Expression447(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Expression__adb_Expression447", None)
        self.__adb_Expression447 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_ComponentClause446"):
                opp_val = getattr(old_value, "adb_ComponentClause446", None)
                if opp_val == self:
                    setattr(old_value, "adb_ComponentClause446", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_ComponentClause446"):
                opp_val = getattr(value, "adb_ComponentClause446", None)
                setattr(value, "adb_ComponentClause446", self)

    @property
    def adb_Expression210(self):
        return self.__adb_Expression210

    @adb_Expression210.setter
    def adb_Expression210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Expression__adb_Expression210", None)
        self.__adb_Expression210 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_ExtendedReturnStatement209"):
                opp_val = getattr(old_value, "adb_ExtendedReturnStatement209", None)
                if opp_val == self:
                    setattr(old_value, "adb_ExtendedReturnStatement209", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_ExtendedReturnStatement209"):
                opp_val = getattr(value, "adb_ExtendedReturnStatement209", None)
                setattr(value, "adb_ExtendedReturnStatement209", self)

    @property
    def adb_Expression311(self):
        return self.__adb_Expression311

    @adb_Expression311.setter
    def adb_Expression311(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Expression__adb_Expression311", None)
        self.__adb_Expression311 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_RaiseStatement310"):
                opp_val = getattr(old_value, "adb_RaiseStatement310", None)
                if opp_val == self:
                    setattr(old_value, "adb_RaiseStatement310", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_RaiseStatement310"):
                opp_val = getattr(value, "adb_RaiseStatement310", None)
                setattr(value, "adb_RaiseStatement310", self)

    @property
    def adb_Expression475(self):
        return self.__adb_Expression475

    @adb_Expression475.setter
    def adb_Expression475(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Expression__adb_Expression475", None)
        self.__adb_Expression475 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_FixedPointDefinition"):
                opp_val = getattr(old_value, "adb_FixedPointDefinition", None)
                if opp_val == self:
                    setattr(old_value, "adb_FixedPointDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_FixedPointDefinition"):
                opp_val = getattr(value, "adb_FixedPointDefinition", None)
                setattr(value, "adb_FixedPointDefinition", self)

    @property
    def adb_Expression249(self):
        return self.__adb_Expression249

    @adb_Expression249.setter
    def adb_Expression249(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Expression__adb_Expression249", None)
        self.__adb_Expression249 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_EntryBarrier248"):
                opp_val = getattr(old_value, "adb_EntryBarrier248", None)
                if opp_val == self:
                    setattr(old_value, "adb_EntryBarrier248", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_EntryBarrier248"):
                opp_val = getattr(value, "adb_EntryBarrier248", None)
                setattr(value, "adb_EntryBarrier248", self)

    @property
    def adb_Expression202(self):
        return self.__adb_Expression202

    @adb_Expression202.setter
    def adb_Expression202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Expression__adb_Expression202", None)
        self.__adb_Expression202 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_ExitStatement201"):
                opp_val = getattr(old_value, "adb_ExitStatement201", None)
                if opp_val == self:
                    setattr(old_value, "adb_ExitStatement201", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_ExitStatement201"):
                opp_val = getattr(value, "adb_ExitStatement201", None)
                setattr(value, "adb_ExitStatement201", self)

    @property
    def adb_Expression570(self):
        return self.__adb_Expression570

    @adb_Expression570.setter
    def adb_Expression570(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Expression__adb_Expression570", None)
        self.__adb_Expression570 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_EntityRange569"):
                opp_val = getattr(old_value, "adb_EntityRange569", None)
                if opp_val == self:
                    setattr(old_value, "adb_EntityRange569", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_EntityRange569"):
                opp_val = getattr(value, "adb_EntityRange569", None)
                setattr(value, "adb_EntityRange569", self)

    @property
    def adb_Expression192(self):
        return self.__adb_Expression192

    @adb_Expression192.setter
    def adb_Expression192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Expression__adb_Expression192", None)
        self.__adb_Expression192 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_IterationScheme191"):
                opp_val = getattr(old_value, "adb_IterationScheme191", None)
                if opp_val == self:
                    setattr(old_value, "adb_IterationScheme191", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_IterationScheme191"):
                opp_val = getattr(value, "adb_IterationScheme191", None)
                setattr(value, "adb_IterationScheme191", self)

    @property
    def adb_Expression533(self):
        return self.__adb_Expression533

    @adb_Expression533.setter
    def adb_Expression533(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Expression__adb_Expression533", None)
        self.__adb_Expression533 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_InitializedComponents"):
                opp_val = getattr(old_value, "adb_InitializedComponents", None)
                if opp_val == self:
                    setattr(old_value, "adb_InitializedComponents", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_InitializedComponents"):
                opp_val = getattr(value, "adb_InitializedComponents", None)
                setattr(value, "adb_InitializedComponents", self)

    @property
    def adb_Expression465(self):
        return self.__adb_Expression465

    @adb_Expression465.setter
    def adb_Expression465(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Expression__adb_Expression465", None)
        self.__adb_Expression465 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_RealTypeDefinition"):
                opp_val = getattr(old_value, "adb_RealTypeDefinition", None)
                if opp_val == self:
                    setattr(old_value, "adb_RealTypeDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_RealTypeDefinition"):
                opp_val = getattr(value, "adb_RealTypeDefinition", None)
                setattr(value, "adb_RealTypeDefinition", self)

    @property
    def adb_Expression162(self):
        return self.__adb_Expression162

    @adb_Expression162.setter
    def adb_Expression162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Expression__adb_Expression162", None)
        self.__adb_Expression162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_AssignmentStatement161"):
                opp_val = getattr(old_value, "adb_AssignmentStatement161", None)
                if opp_val == self:
                    setattr(old_value, "adb_AssignmentStatement161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_AssignmentStatement161"):
                opp_val = getattr(value, "adb_AssignmentStatement161", None)
                setattr(value, "adb_AssignmentStatement161", self)

    @property
    def adb_Expression273(self):
        return self.__adb_Expression273

    @adb_Expression273.setter
    def adb_Expression273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Expression__adb_Expression273", None)
        self.__adb_Expression273 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_Guard272"):
                opp_val = getattr(old_value, "adb_Guard272", None)
                if opp_val == self:
                    setattr(old_value, "adb_Guard272", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_Guard272"):
                opp_val = getattr(value, "adb_Guard272", None)
                setattr(value, "adb_Guard272", self)

    @property
    def adb_Expression206(self):
        return self.__adb_Expression206

    @adb_Expression206.setter
    def adb_Expression206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Expression__adb_Expression206", None)
        self.__adb_Expression206 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_SimpleReturnStatement"):
                opp_val = getattr(old_value, "adb_SimpleReturnStatement", None)
                if opp_val == self:
                    setattr(old_value, "adb_SimpleReturnStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_SimpleReturnStatement"):
                opp_val = getattr(value, "adb_SimpleReturnStatement", None)
                setattr(value, "adb_SimpleReturnStatement", self)

    @property
    def adb_Expression435(self):
        return self.__adb_Expression435

    @adb_Expression435.setter
    def adb_Expression435(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Expression__adb_Expression435", None)
        self.__adb_Expression435 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_ComponentDeclaration434"):
                opp_val = getattr(old_value, "adb_ComponentDeclaration434", None)
                if opp_val == self:
                    setattr(old_value, "adb_ComponentDeclaration434", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_ComponentDeclaration434"):
                opp_val = getattr(value, "adb_ComponentDeclaration434", None)
                setattr(value, "adb_ComponentDeclaration434", self)

    @property
    def adb_Expression417(self):
        return self.__adb_Expression417

    @adb_Expression417.setter
    def adb_Expression417(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Expression__adb_Expression417", None)
        self.__adb_Expression417 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_ModularTypeDefinition"):
                opp_val = getattr(old_value, "adb_ModularTypeDefinition", None)
                if opp_val == self:
                    setattr(old_value, "adb_ModularTypeDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_ModularTypeDefinition"):
                opp_val = getattr(value, "adb_ModularTypeDefinition", None)
                setattr(value, "adb_ModularTypeDefinition", self)

    @property
    def adb_Expression170(self):
        return self.__adb_Expression170

    @adb_Expression170.setter
    def adb_Expression170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Expression__adb_Expression170", None)
        self.__adb_Expression170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_IfStatement169"):
                opp_val = getattr(old_value, "adb_IfStatement169", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_IfStatement169"):
                opp_val = getattr(value, "adb_IfStatement169", None)
                if opp_val is None:
                    setattr(value, "adb_IfStatement169", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def adb_Expression477(self):
        return self.__adb_Expression477

    @adb_Expression477.setter
    def adb_Expression477(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Expression__adb_Expression477", None)
        self.__adb_Expression477 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adb_Relation"):
                    opp_val = getattr(item, "adb_Relation", None)
                    
                    if opp_val == self:
                        setattr(item, "adb_Relation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adb_Relation"):
                    opp_val = getattr(item, "adb_Relation", None)
                    
                    setattr(item, "adb_Relation", self)
                    

class adb_AnonymousAccessDefinition(ReturnSubtypeIndication):

    pass
class adb_OptNullExclusion:

    def __init__(self, not_null: str, adb_OptNullExclusion: "adb_FormalObjectDeclaration" = None, adb_OptNullExclusion324: "adb_DiscriminantSpecification" = None, adb_OptNullExclusion348: "adb_AccessTypeDefinition" = None, adb_OptNullExclusion374: "adb_AnonymousAccessDefinition" = None, adb_OptNullExclusion385: "adb_ParameterAndResultProfile" = None, adb_OptNullExclusion402: "adb_ParameterSpecification" = None, adb_OptNullExclusion508: "adb_SubtypeIndication" = None):
        self.not_null = not_null
        self.adb_OptNullExclusion = adb_OptNullExclusion
        self.adb_OptNullExclusion324 = adb_OptNullExclusion324
        self.adb_OptNullExclusion348 = adb_OptNullExclusion348
        self.adb_OptNullExclusion374 = adb_OptNullExclusion374
        self.adb_OptNullExclusion385 = adb_OptNullExclusion385
        self.adb_OptNullExclusion402 = adb_OptNullExclusion402
        self.adb_OptNullExclusion508 = adb_OptNullExclusion508
        
    @property
    def not_null(self) -> str:
        return self.__not_null

    @not_null.setter
    def not_null(self, not_null: str):
        self.__not_null = not_null

    @property
    def adb_OptNullExclusion348(self):
        return self.__adb_OptNullExclusion348

    @adb_OptNullExclusion348.setter
    def adb_OptNullExclusion348(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_OptNullExclusion__adb_OptNullExclusion348", None)
        self.__adb_OptNullExclusion348 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_AccessTypeDefinition"):
                opp_val = getattr(old_value, "adb_AccessTypeDefinition", None)
                if opp_val == self:
                    setattr(old_value, "adb_AccessTypeDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_AccessTypeDefinition"):
                opp_val = getattr(value, "adb_AccessTypeDefinition", None)
                setattr(value, "adb_AccessTypeDefinition", self)

    @property
    def adb_OptNullExclusion508(self):
        return self.__adb_OptNullExclusion508

    @adb_OptNullExclusion508.setter
    def adb_OptNullExclusion508(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_OptNullExclusion__adb_OptNullExclusion508", None)
        self.__adb_OptNullExclusion508 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_SubtypeIndication507"):
                opp_val = getattr(old_value, "adb_SubtypeIndication507", None)
                if opp_val == self:
                    setattr(old_value, "adb_SubtypeIndication507", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_SubtypeIndication507"):
                opp_val = getattr(value, "adb_SubtypeIndication507", None)
                setattr(value, "adb_SubtypeIndication507", self)

    @property
    def adb_OptNullExclusion(self):
        return self.__adb_OptNullExclusion

    @adb_OptNullExclusion.setter
    def adb_OptNullExclusion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_OptNullExclusion__adb_OptNullExclusion", None)
        self.__adb_OptNullExclusion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_FormalObjectDeclaration91"):
                opp_val = getattr(old_value, "adb_FormalObjectDeclaration91", None)
                if opp_val == self:
                    setattr(old_value, "adb_FormalObjectDeclaration91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_FormalObjectDeclaration91"):
                opp_val = getattr(value, "adb_FormalObjectDeclaration91", None)
                setattr(value, "adb_FormalObjectDeclaration91", self)

    @property
    def adb_OptNullExclusion324(self):
        return self.__adb_OptNullExclusion324

    @adb_OptNullExclusion324.setter
    def adb_OptNullExclusion324(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_OptNullExclusion__adb_OptNullExclusion324", None)
        self.__adb_OptNullExclusion324 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_DiscriminantSpecification323"):
                opp_val = getattr(old_value, "adb_DiscriminantSpecification323", None)
                if opp_val == self:
                    setattr(old_value, "adb_DiscriminantSpecification323", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_DiscriminantSpecification323"):
                opp_val = getattr(value, "adb_DiscriminantSpecification323", None)
                setattr(value, "adb_DiscriminantSpecification323", self)

    @property
    def adb_OptNullExclusion374(self):
        return self.__adb_OptNullExclusion374

    @adb_OptNullExclusion374.setter
    def adb_OptNullExclusion374(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_OptNullExclusion__adb_OptNullExclusion374", None)
        self.__adb_OptNullExclusion374 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_AnonymousAccessDefinition373"):
                opp_val = getattr(old_value, "adb_AnonymousAccessDefinition373", None)
                if opp_val == self:
                    setattr(old_value, "adb_AnonymousAccessDefinition373", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_AnonymousAccessDefinition373"):
                opp_val = getattr(value, "adb_AnonymousAccessDefinition373", None)
                setattr(value, "adb_AnonymousAccessDefinition373", self)

    @property
    def adb_OptNullExclusion402(self):
        return self.__adb_OptNullExclusion402

    @adb_OptNullExclusion402.setter
    def adb_OptNullExclusion402(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_OptNullExclusion__adb_OptNullExclusion402", None)
        self.__adb_OptNullExclusion402 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_ParameterSpecification401"):
                opp_val = getattr(old_value, "adb_ParameterSpecification401", None)
                if opp_val == self:
                    setattr(old_value, "adb_ParameterSpecification401", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_ParameterSpecification401"):
                opp_val = getattr(value, "adb_ParameterSpecification401", None)
                setattr(value, "adb_ParameterSpecification401", self)

    @property
    def adb_OptNullExclusion385(self):
        return self.__adb_OptNullExclusion385

    @adb_OptNullExclusion385.setter
    def adb_OptNullExclusion385(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_OptNullExclusion__adb_OptNullExclusion385", None)
        self.__adb_OptNullExclusion385 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_ParameterAndResultProfile384"):
                opp_val = getattr(old_value, "adb_ParameterAndResultProfile384", None)
                if opp_val == self:
                    setattr(old_value, "adb_ParameterAndResultProfile384", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_ParameterAndResultProfile384"):
                opp_val = getattr(value, "adb_ParameterAndResultProfile384", None)
                setattr(value, "adb_ParameterAndResultProfile384", self)

class adb_Mode:

    def __init__(self, in: bool, out: bool, adb_Mode: "adb_FormalObjectDeclaration" = None, adb_Mode399: "adb_ParameterSpecification" = None):
        self.in = in
        self.out = out
        self.adb_Mode = adb_Mode
        self.adb_Mode399 = adb_Mode399
        
    @property
    def out(self) -> bool:
        return self.__out

    @out.setter
    def out(self, out: bool):
        self.__out = out

    @property
    def in(self) -> bool:
        return self.__in

    @in.setter
    def in(self, in: bool):
        self.__in = in

    @property
    def adb_Mode(self):
        return self.__adb_Mode

    @adb_Mode.setter
    def adb_Mode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Mode__adb_Mode", None)
        self.__adb_Mode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_FormalObjectDeclaration89"):
                opp_val = getattr(old_value, "adb_FormalObjectDeclaration89", None)
                if opp_val == self:
                    setattr(old_value, "adb_FormalObjectDeclaration89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_FormalObjectDeclaration89"):
                opp_val = getattr(value, "adb_FormalObjectDeclaration89", None)
                setattr(value, "adb_FormalObjectDeclaration89", self)

    @property
    def adb_Mode399(self):
        return self.__adb_Mode399

    @adb_Mode399.setter
    def adb_Mode399(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Mode__adb_Mode399", None)
        self.__adb_Mode399 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_ParameterSpecification398"):
                opp_val = getattr(old_value, "adb_ParameterSpecification398", None)
                if opp_val == self:
                    setattr(old_value, "adb_ParameterSpecification398", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_ParameterSpecification398"):
                opp_val = getattr(value, "adb_ParameterSpecification398", None)
                setattr(value, "adb_ParameterSpecification398", self)

class AbortablePart:

    pass
class HandledSequenceOfStatements:

    pass
class adb_Label:

    def __init__(self, identifier: str, adb_Label: "adb_LabelisableStatement" = None):
        self.identifier = identifier
        self.adb_Label = adb_Label
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def adb_Label(self):
        return self.__adb_Label

    @adb_Label.setter
    def adb_Label(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Label__adb_Label", None)
        self.__adb_Label = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_LabelisableStatement82"):
                opp_val = getattr(old_value, "adb_LabelisableStatement82", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_LabelisableStatement82"):
                opp_val = getattr(value, "adb_LabelisableStatement82", None)
                if opp_val is None:
                    setattr(value, "adb_LabelisableStatement82", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Body:

    pass
class adb_BodyStub(Body):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class adb_ProperBody(Body):

    pass
class adb_SequenceOfStatements(AbortablePart, HandledSequenceOfStatements):

    pass
class adb_ExceptionHandler:

    def __init__(self, name: str, adb_ExceptionHandler78: "adb_SequenceOfStatements" = None, adb_ExceptionHandler: set["adb_ExceptionChoice"] = None, adb_ExceptionHandler75: "adb_SequenceOfStatements" = None):
        self.name = name
        self.adb_ExceptionHandler78 = adb_ExceptionHandler78
        self.adb_ExceptionHandler = adb_ExceptionHandler if adb_ExceptionHandler is not None else set()
        self.adb_ExceptionHandler75 = adb_ExceptionHandler75
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def adb_ExceptionHandler75(self):
        return self.__adb_ExceptionHandler75

    @adb_ExceptionHandler75.setter
    def adb_ExceptionHandler75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_ExceptionHandler__adb_ExceptionHandler75", None)
        self.__adb_ExceptionHandler75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_SequenceOfStatements"):
                opp_val = getattr(old_value, "adb_SequenceOfStatements", None)
                if opp_val == self:
                    setattr(old_value, "adb_SequenceOfStatements", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_SequenceOfStatements"):
                opp_val = getattr(value, "adb_SequenceOfStatements", None)
                setattr(value, "adb_SequenceOfStatements", self)

    @property
    def adb_ExceptionHandler78(self):
        return self.__adb_ExceptionHandler78

    @adb_ExceptionHandler78.setter
    def adb_ExceptionHandler78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_ExceptionHandler__adb_ExceptionHandler78", None)
        self.__adb_ExceptionHandler78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_SequenceOfStatements77"):
                opp_val = getattr(old_value, "adb_SequenceOfStatements77", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_SequenceOfStatements77"):
                opp_val = getattr(value, "adb_SequenceOfStatements77", None)
                if opp_val is None:
                    setattr(value, "adb_SequenceOfStatements77", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def adb_ExceptionHandler(self):
        return self.__adb_ExceptionHandler

    @adb_ExceptionHandler.setter
    def adb_ExceptionHandler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_ExceptionHandler__adb_ExceptionHandler", None)
        self.__adb_ExceptionHandler = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adb_ExceptionChoice73"):
                    opp_val = getattr(item, "adb_ExceptionChoice73", None)
                    
                    if opp_val == self:
                        setattr(item, "adb_ExceptionChoice73", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adb_ExceptionChoice73"):
                    opp_val = getattr(item, "adb_ExceptionChoice73", None)
                    
                    setattr(item, "adb_ExceptionChoice73", self)
                    

class Statement:

    pass
class adb_CompoundStatement(Statement):

    pass
class adb_SimpleStatement(Statement):

    pass
class adb_Statement:

    pass
class adb_LabelisableStatement:

    pass
class BodyStub:

    pass
class adb_PackageBodyStub(BodyStub):

    pass
class adb_TaskBodyStub(BodyStub):

    pass
class adb_ProtectedBodyStub(BodyStub):

    pass
class ProtectedElementDeclaration:

    pass
class adb_ComponentDeclaration(ProtectedElementDeclaration, ComponentItem):

    pass
class adb_ProtectedOperationDeclaration(ProtectedElementDeclaration):

    pass
class adb_ProtectedElementDeclaration:

    pass
class adb_Name(Interval):

    def __init__(self, name: str, adb_Name: "adb_ExceptionChoice" = None, adb_Name94: "adb_FormalObjectDeclaration" = None, adb_Name104: "adb_FormalDerivedTypeDefinition" = None, adb_Name124: "adb_ExceptionDeclaration" = None, adb_Name135: "adb_DataInstanceDeclaration" = None, adb_Name159: "adb_AssignmentStatement" = None, adb_Name204: "adb_ProcedureOrEntryCallStatement" = None, adb_Name254: "adb_RequeueStatement" = None, adb_Name308: "adb_RaiseStatement" = None, adb_Name305: "adb_TaskNames" = None, adb_Name329: "adb_DiscriminantSpecification" = None, adb_Name335: "adb_InterfaceList" = None, adb_Name363: "adb_UnconstrainedIndexes" = None, adb_Name379: "adb_AccessToDataInstance" = None, adb_Name388: "adb_ParameterAndResultProfile" = None, adb_Name405: "adb_ParameterSpecification" = None, adb_Name498: "adb_QualifiedName" = None, adb_Name502: "adb_Allocator" = None, adb_Name551: "adb_PrimaryName" = None, adb_Name567: "adb_EntityRange" = None, adb_Name559: "adb_PrimaryName" = None):
        self.name = name
        self.adb_Name = adb_Name
        self.adb_Name94 = adb_Name94
        self.adb_Name104 = adb_Name104
        self.adb_Name124 = adb_Name124
        self.adb_Name135 = adb_Name135
        self.adb_Name159 = adb_Name159
        self.adb_Name204 = adb_Name204
        self.adb_Name254 = adb_Name254
        self.adb_Name308 = adb_Name308
        self.adb_Name305 = adb_Name305
        self.adb_Name329 = adb_Name329
        self.adb_Name335 = adb_Name335
        self.adb_Name363 = adb_Name363
        self.adb_Name379 = adb_Name379
        self.adb_Name388 = adb_Name388
        self.adb_Name405 = adb_Name405
        self.adb_Name498 = adb_Name498
        self.adb_Name502 = adb_Name502
        self.adb_Name551 = adb_Name551
        self.adb_Name567 = adb_Name567
        self.adb_Name559 = adb_Name559
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def adb_Name388(self):
        return self.__adb_Name388

    @adb_Name388.setter
    def adb_Name388(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Name__adb_Name388", None)
        self.__adb_Name388 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_ParameterAndResultProfile387"):
                opp_val = getattr(old_value, "adb_ParameterAndResultProfile387", None)
                if opp_val == self:
                    setattr(old_value, "adb_ParameterAndResultProfile387", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_ParameterAndResultProfile387"):
                opp_val = getattr(value, "adb_ParameterAndResultProfile387", None)
                setattr(value, "adb_ParameterAndResultProfile387", self)

    @property
    def adb_Name94(self):
        return self.__adb_Name94

    @adb_Name94.setter
    def adb_Name94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Name__adb_Name94", None)
        self.__adb_Name94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_FormalObjectDeclaration93"):
                opp_val = getattr(old_value, "adb_FormalObjectDeclaration93", None)
                if opp_val == self:
                    setattr(old_value, "adb_FormalObjectDeclaration93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_FormalObjectDeclaration93"):
                opp_val = getattr(value, "adb_FormalObjectDeclaration93", None)
                setattr(value, "adb_FormalObjectDeclaration93", self)

    @property
    def adb_Name204(self):
        return self.__adb_Name204

    @adb_Name204.setter
    def adb_Name204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Name__adb_Name204", None)
        self.__adb_Name204 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_ProcedureOrEntryCallStatement"):
                opp_val = getattr(old_value, "adb_ProcedureOrEntryCallStatement", None)
                if opp_val == self:
                    setattr(old_value, "adb_ProcedureOrEntryCallStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_ProcedureOrEntryCallStatement"):
                opp_val = getattr(value, "adb_ProcedureOrEntryCallStatement", None)
                setattr(value, "adb_ProcedureOrEntryCallStatement", self)

    @property
    def adb_Name335(self):
        return self.__adb_Name335

    @adb_Name335.setter
    def adb_Name335(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Name__adb_Name335", None)
        self.__adb_Name335 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_InterfaceList334"):
                opp_val = getattr(old_value, "adb_InterfaceList334", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_InterfaceList334"):
                opp_val = getattr(value, "adb_InterfaceList334", None)
                if opp_val is None:
                    setattr(value, "adb_InterfaceList334", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def adb_Name254(self):
        return self.__adb_Name254

    @adb_Name254.setter
    def adb_Name254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Name__adb_Name254", None)
        self.__adb_Name254 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_RequeueStatement"):
                opp_val = getattr(old_value, "adb_RequeueStatement", None)
                if opp_val == self:
                    setattr(old_value, "adb_RequeueStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_RequeueStatement"):
                opp_val = getattr(value, "adb_RequeueStatement", None)
                setattr(value, "adb_RequeueStatement", self)

    @property
    def adb_Name559(self):
        return self.__adb_Name559

    @adb_Name559.setter
    def adb_Name559(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Name__adb_Name559", None)
        self.__adb_Name559 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_PrimaryName558"):
                opp_val = getattr(old_value, "adb_PrimaryName558", None)
                if opp_val == self:
                    setattr(old_value, "adb_PrimaryName558", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_PrimaryName558"):
                opp_val = getattr(value, "adb_PrimaryName558", None)
                setattr(value, "adb_PrimaryName558", self)

    @property
    def adb_Name363(self):
        return self.__adb_Name363

    @adb_Name363.setter
    def adb_Name363(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Name__adb_Name363", None)
        self.__adb_Name363 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_UnconstrainedIndexes"):
                opp_val = getattr(old_value, "adb_UnconstrainedIndexes", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_UnconstrainedIndexes"):
                opp_val = getattr(value, "adb_UnconstrainedIndexes", None)
                if opp_val is None:
                    setattr(value, "adb_UnconstrainedIndexes", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def adb_Name329(self):
        return self.__adb_Name329

    @adb_Name329.setter
    def adb_Name329(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Name__adb_Name329", None)
        self.__adb_Name329 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_DiscriminantSpecification328"):
                opp_val = getattr(old_value, "adb_DiscriminantSpecification328", None)
                if opp_val == self:
                    setattr(old_value, "adb_DiscriminantSpecification328", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_DiscriminantSpecification328"):
                opp_val = getattr(value, "adb_DiscriminantSpecification328", None)
                setattr(value, "adb_DiscriminantSpecification328", self)

    @property
    def adb_Name498(self):
        return self.__adb_Name498

    @adb_Name498.setter
    def adb_Name498(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Name__adb_Name498", None)
        self.__adb_Name498 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_QualifiedName"):
                opp_val = getattr(old_value, "adb_QualifiedName", None)
                if opp_val == self:
                    setattr(old_value, "adb_QualifiedName", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_QualifiedName"):
                opp_val = getattr(value, "adb_QualifiedName", None)
                setattr(value, "adb_QualifiedName", self)

    @property
    def adb_Name(self):
        return self.__adb_Name

    @adb_Name.setter
    def adb_Name(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Name__adb_Name", None)
        self.__adb_Name = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_ExceptionChoice"):
                opp_val = getattr(old_value, "adb_ExceptionChoice", None)
                if opp_val == self:
                    setattr(old_value, "adb_ExceptionChoice", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_ExceptionChoice"):
                opp_val = getattr(value, "adb_ExceptionChoice", None)
                setattr(value, "adb_ExceptionChoice", self)

    @property
    def adb_Name104(self):
        return self.__adb_Name104

    @adb_Name104.setter
    def adb_Name104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Name__adb_Name104", None)
        self.__adb_Name104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_FormalDerivedTypeDefinition"):
                opp_val = getattr(old_value, "adb_FormalDerivedTypeDefinition", None)
                if opp_val == self:
                    setattr(old_value, "adb_FormalDerivedTypeDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_FormalDerivedTypeDefinition"):
                opp_val = getattr(value, "adb_FormalDerivedTypeDefinition", None)
                setattr(value, "adb_FormalDerivedTypeDefinition", self)

    @property
    def adb_Name308(self):
        return self.__adb_Name308

    @adb_Name308.setter
    def adb_Name308(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Name__adb_Name308", None)
        self.__adb_Name308 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_RaiseStatement"):
                opp_val = getattr(old_value, "adb_RaiseStatement", None)
                if opp_val == self:
                    setattr(old_value, "adb_RaiseStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_RaiseStatement"):
                opp_val = getattr(value, "adb_RaiseStatement", None)
                setattr(value, "adb_RaiseStatement", self)

    @property
    def adb_Name567(self):
        return self.__adb_Name567

    @adb_Name567.setter
    def adb_Name567(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Name__adb_Name567", None)
        self.__adb_Name567 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_EntityRange"):
                opp_val = getattr(old_value, "adb_EntityRange", None)
                if opp_val == self:
                    setattr(old_value, "adb_EntityRange", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_EntityRange"):
                opp_val = getattr(value, "adb_EntityRange", None)
                setattr(value, "adb_EntityRange", self)

    @property
    def adb_Name124(self):
        return self.__adb_Name124

    @adb_Name124.setter
    def adb_Name124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Name__adb_Name124", None)
        self.__adb_Name124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_ExceptionDeclaration123"):
                opp_val = getattr(old_value, "adb_ExceptionDeclaration123", None)
                if opp_val == self:
                    setattr(old_value, "adb_ExceptionDeclaration123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_ExceptionDeclaration123"):
                opp_val = getattr(value, "adb_ExceptionDeclaration123", None)
                setattr(value, "adb_ExceptionDeclaration123", self)

    @property
    def adb_Name405(self):
        return self.__adb_Name405

    @adb_Name405.setter
    def adb_Name405(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Name__adb_Name405", None)
        self.__adb_Name405 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_ParameterSpecification404"):
                opp_val = getattr(old_value, "adb_ParameterSpecification404", None)
                if opp_val == self:
                    setattr(old_value, "adb_ParameterSpecification404", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_ParameterSpecification404"):
                opp_val = getattr(value, "adb_ParameterSpecification404", None)
                setattr(value, "adb_ParameterSpecification404", self)

    @property
    def adb_Name305(self):
        return self.__adb_Name305

    @adb_Name305.setter
    def adb_Name305(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Name__adb_Name305", None)
        self.__adb_Name305 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_TaskNames"):
                opp_val = getattr(old_value, "adb_TaskNames", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_TaskNames"):
                opp_val = getattr(value, "adb_TaskNames", None)
                if opp_val is None:
                    setattr(value, "adb_TaskNames", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def adb_Name502(self):
        return self.__adb_Name502

    @adb_Name502.setter
    def adb_Name502(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Name__adb_Name502", None)
        self.__adb_Name502 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_Allocator"):
                opp_val = getattr(old_value, "adb_Allocator", None)
                if opp_val == self:
                    setattr(old_value, "adb_Allocator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_Allocator"):
                opp_val = getattr(value, "adb_Allocator", None)
                setattr(value, "adb_Allocator", self)

    @property
    def adb_Name135(self):
        return self.__adb_Name135

    @adb_Name135.setter
    def adb_Name135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Name__adb_Name135", None)
        self.__adb_Name135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_DataInstanceDeclaration134"):
                opp_val = getattr(old_value, "adb_DataInstanceDeclaration134", None)
                if opp_val == self:
                    setattr(old_value, "adb_DataInstanceDeclaration134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_DataInstanceDeclaration134"):
                opp_val = getattr(value, "adb_DataInstanceDeclaration134", None)
                setattr(value, "adb_DataInstanceDeclaration134", self)

    @property
    def adb_Name159(self):
        return self.__adb_Name159

    @adb_Name159.setter
    def adb_Name159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Name__adb_Name159", None)
        self.__adb_Name159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_AssignmentStatement"):
                opp_val = getattr(old_value, "adb_AssignmentStatement", None)
                if opp_val == self:
                    setattr(old_value, "adb_AssignmentStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_AssignmentStatement"):
                opp_val = getattr(value, "adb_AssignmentStatement", None)
                setattr(value, "adb_AssignmentStatement", self)

    @property
    def adb_Name379(self):
        return self.__adb_Name379

    @adb_Name379.setter
    def adb_Name379(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Name__adb_Name379", None)
        self.__adb_Name379 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_AccessToDataInstance"):
                opp_val = getattr(old_value, "adb_AccessToDataInstance", None)
                if opp_val == self:
                    setattr(old_value, "adb_AccessToDataInstance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_AccessToDataInstance"):
                opp_val = getattr(value, "adb_AccessToDataInstance", None)
                setattr(value, "adb_AccessToDataInstance", self)

    @property
    def adb_Name551(self):
        return self.__adb_Name551

    @adb_Name551.setter
    def adb_Name551(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Name__adb_Name551", None)
        self.__adb_Name551 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_PrimaryName"):
                opp_val = getattr(old_value, "adb_PrimaryName", None)
                if opp_val == self:
                    setattr(old_value, "adb_PrimaryName", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_PrimaryName"):
                opp_val = getattr(value, "adb_PrimaryName", None)
                setattr(value, "adb_PrimaryName", self)

class adb_ExceptionChoice:

    def __init__(self, others: bool, adb_ExceptionChoice: "adb_Name" = None, adb_ExceptionChoice73: "adb_ExceptionHandler" = None):
        self.others = others
        self.adb_ExceptionChoice = adb_ExceptionChoice
        self.adb_ExceptionChoice73 = adb_ExceptionChoice73
        
    @property
    def others(self) -> bool:
        return self.__others

    @others.setter
    def others(self, others: bool):
        self.__others = others

    @property
    def adb_ExceptionChoice73(self):
        return self.__adb_ExceptionChoice73

    @adb_ExceptionChoice73.setter
    def adb_ExceptionChoice73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_ExceptionChoice__adb_ExceptionChoice73", None)
        self.__adb_ExceptionChoice73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_ExceptionHandler"):
                opp_val = getattr(old_value, "adb_ExceptionHandler", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_ExceptionHandler"):
                opp_val = getattr(value, "adb_ExceptionHandler", None)
                if opp_val is None:
                    setattr(value, "adb_ExceptionHandler", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def adb_ExceptionChoice(self):
        return self.__adb_ExceptionChoice

    @adb_ExceptionChoice.setter
    def adb_ExceptionChoice(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_ExceptionChoice__adb_ExceptionChoice", None)
        self.__adb_ExceptionChoice = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_Name"):
                opp_val = getattr(old_value, "adb_Name", None)
                if opp_val == self:
                    setattr(old_value, "adb_Name", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_Name"):
                opp_val = getattr(value, "adb_Name", None)
                setattr(value, "adb_Name", self)

class adb_ParameterAndResultProfile:

    pass
class SubprogramSpecification:

    pass
class adb_FunctionSpecification(SubprogramSpecification):

    pass
class adb_ProcedureSpecification(SubprogramSpecification):

    pass
class adb_FormalPart:

    pass
class adb_DiscreteSubtypeDefinition:

    pass
class ProtectedOperationDeclaration:

    pass
class TaskItem:

    pass
class adb_EntryDeclaration(TaskItem, ProtectedOperationDeclaration):

    def __init__(self, name: str, adb_EntryDeclaration56: "adb_FormalPart" = None, adb_EntryDeclaration: "adb_OverridingIndicator" = None, adb_EntryDeclaration54: "adb_DiscreteSubtypeDefinition" = None, adb_EntryDeclaration227: "adb_AcceptStatement" = None, adb_EntryDeclaration237: "adb_EntryBody" = None):
        self.name = name
        self.adb_EntryDeclaration56 = adb_EntryDeclaration56
        self.adb_EntryDeclaration = adb_EntryDeclaration
        self.adb_EntryDeclaration54 = adb_EntryDeclaration54
        self.adb_EntryDeclaration227 = adb_EntryDeclaration227
        self.adb_EntryDeclaration237 = adb_EntryDeclaration237
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def adb_EntryDeclaration(self):
        return self.__adb_EntryDeclaration

    @adb_EntryDeclaration.setter
    def adb_EntryDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_EntryDeclaration__adb_EntryDeclaration", None)
        self.__adb_EntryDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_OverridingIndicator52"):
                opp_val = getattr(old_value, "adb_OverridingIndicator52", None)
                if opp_val == self:
                    setattr(old_value, "adb_OverridingIndicator52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_OverridingIndicator52"):
                opp_val = getattr(value, "adb_OverridingIndicator52", None)
                setattr(value, "adb_OverridingIndicator52", self)

    @property
    def adb_EntryDeclaration54(self):
        return self.__adb_EntryDeclaration54

    @adb_EntryDeclaration54.setter
    def adb_EntryDeclaration54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_EntryDeclaration__adb_EntryDeclaration54", None)
        self.__adb_EntryDeclaration54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_DiscreteSubtypeDefinition"):
                opp_val = getattr(old_value, "adb_DiscreteSubtypeDefinition", None)
                if opp_val == self:
                    setattr(old_value, "adb_DiscreteSubtypeDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_DiscreteSubtypeDefinition"):
                opp_val = getattr(value, "adb_DiscreteSubtypeDefinition", None)
                setattr(value, "adb_DiscreteSubtypeDefinition", self)

    @property
    def adb_EntryDeclaration237(self):
        return self.__adb_EntryDeclaration237

    @adb_EntryDeclaration237.setter
    def adb_EntryDeclaration237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_EntryDeclaration__adb_EntryDeclaration237", None)
        self.__adb_EntryDeclaration237 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_EntryBody"):
                opp_val = getattr(old_value, "adb_EntryBody", None)
                if opp_val == self:
                    setattr(old_value, "adb_EntryBody", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_EntryBody"):
                opp_val = getattr(value, "adb_EntryBody", None)
                setattr(value, "adb_EntryBody", self)

    @property
    def adb_EntryDeclaration227(self):
        return self.__adb_EntryDeclaration227

    @adb_EntryDeclaration227.setter
    def adb_EntryDeclaration227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_EntryDeclaration__adb_EntryDeclaration227", None)
        self.__adb_EntryDeclaration227 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_AcceptStatement"):
                opp_val = getattr(old_value, "adb_AcceptStatement", None)
                if opp_val == self:
                    setattr(old_value, "adb_AcceptStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_AcceptStatement"):
                opp_val = getattr(value, "adb_AcceptStatement", None)
                setattr(value, "adb_AcceptStatement", self)

    @property
    def adb_EntryDeclaration56(self):
        return self.__adb_EntryDeclaration56

    @adb_EntryDeclaration56.setter
    def adb_EntryDeclaration56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_EntryDeclaration__adb_EntryDeclaration56", None)
        self.__adb_EntryDeclaration56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_FormalPart"):
                opp_val = getattr(old_value, "adb_FormalPart", None)
                if opp_val == self:
                    setattr(old_value, "adb_FormalPart", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_FormalPart"):
                opp_val = getattr(value, "adb_FormalPart", None)
                setattr(value, "adb_FormalPart", self)

class adb_TaskItem:

    pass
class adb_SubtypeIndication(ReturnSubtypeIndication, DiscreteSubtypeDefinition, DiscreteRange, DiscreteChoice):

    def __init__(self, subtypeMark: str, adb_SubtypeIndication: "adb_PrivateExtensionDeclaration" = None, adb_SubtypeIndication129: "adb_DataInstanceDeclaration" = None, adb_SubtypeIndication152: "adb_SubtypeDeclaration" = None, adb_SubtypeIndication339: "adb_DerivedTypeDefinition" = None, adb_SubtypeIndication357: "adb_AccessToDataDefinition" = None, adb_SubtypeIndication368: "adb_ComponentDefinition" = None, adb_SubtypeIndication507: "adb_OptNullExclusion" = None, adb_SubtypeIndication510: "adb_OptConstraint" = None):
        self.subtypeMark = subtypeMark
        self.adb_SubtypeIndication = adb_SubtypeIndication
        self.adb_SubtypeIndication129 = adb_SubtypeIndication129
        self.adb_SubtypeIndication152 = adb_SubtypeIndication152
        self.adb_SubtypeIndication339 = adb_SubtypeIndication339
        self.adb_SubtypeIndication357 = adb_SubtypeIndication357
        self.adb_SubtypeIndication368 = adb_SubtypeIndication368
        self.adb_SubtypeIndication507 = adb_SubtypeIndication507
        self.adb_SubtypeIndication510 = adb_SubtypeIndication510
        
    @property
    def subtypeMark(self) -> str:
        return self.__subtypeMark

    @subtypeMark.setter
    def subtypeMark(self, subtypeMark: str):
        self.__subtypeMark = subtypeMark

    @property
    def adb_SubtypeIndication507(self):
        return self.__adb_SubtypeIndication507

    @adb_SubtypeIndication507.setter
    def adb_SubtypeIndication507(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_SubtypeIndication__adb_SubtypeIndication507", None)
        self.__adb_SubtypeIndication507 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_OptNullExclusion508"):
                opp_val = getattr(old_value, "adb_OptNullExclusion508", None)
                if opp_val == self:
                    setattr(old_value, "adb_OptNullExclusion508", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_OptNullExclusion508"):
                opp_val = getattr(value, "adb_OptNullExclusion508", None)
                setattr(value, "adb_OptNullExclusion508", self)

    @property
    def adb_SubtypeIndication(self):
        return self.__adb_SubtypeIndication

    @adb_SubtypeIndication.setter
    def adb_SubtypeIndication(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_SubtypeIndication__adb_SubtypeIndication", None)
        self.__adb_SubtypeIndication = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_PrivateExtensionDeclaration47"):
                opp_val = getattr(old_value, "adb_PrivateExtensionDeclaration47", None)
                if opp_val == self:
                    setattr(old_value, "adb_PrivateExtensionDeclaration47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_PrivateExtensionDeclaration47"):
                opp_val = getattr(value, "adb_PrivateExtensionDeclaration47", None)
                setattr(value, "adb_PrivateExtensionDeclaration47", self)

    @property
    def adb_SubtypeIndication129(self):
        return self.__adb_SubtypeIndication129

    @adb_SubtypeIndication129.setter
    def adb_SubtypeIndication129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_SubtypeIndication__adb_SubtypeIndication129", None)
        self.__adb_SubtypeIndication129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_DataInstanceDeclaration128"):
                opp_val = getattr(old_value, "adb_DataInstanceDeclaration128", None)
                if opp_val == self:
                    setattr(old_value, "adb_DataInstanceDeclaration128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_DataInstanceDeclaration128"):
                opp_val = getattr(value, "adb_DataInstanceDeclaration128", None)
                setattr(value, "adb_DataInstanceDeclaration128", self)

    @property
    def adb_SubtypeIndication357(self):
        return self.__adb_SubtypeIndication357

    @adb_SubtypeIndication357.setter
    def adb_SubtypeIndication357(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_SubtypeIndication__adb_SubtypeIndication357", None)
        self.__adb_SubtypeIndication357 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_AccessToDataDefinition"):
                opp_val = getattr(old_value, "adb_AccessToDataDefinition", None)
                if opp_val == self:
                    setattr(old_value, "adb_AccessToDataDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_AccessToDataDefinition"):
                opp_val = getattr(value, "adb_AccessToDataDefinition", None)
                setattr(value, "adb_AccessToDataDefinition", self)

    @property
    def adb_SubtypeIndication510(self):
        return self.__adb_SubtypeIndication510

    @adb_SubtypeIndication510.setter
    def adb_SubtypeIndication510(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_SubtypeIndication__adb_SubtypeIndication510", None)
        self.__adb_SubtypeIndication510 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_OptConstraint"):
                opp_val = getattr(old_value, "adb_OptConstraint", None)
                if opp_val == self:
                    setattr(old_value, "adb_OptConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_OptConstraint"):
                opp_val = getattr(value, "adb_OptConstraint", None)
                setattr(value, "adb_OptConstraint", self)

    @property
    def adb_SubtypeIndication368(self):
        return self.__adb_SubtypeIndication368

    @adb_SubtypeIndication368.setter
    def adb_SubtypeIndication368(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_SubtypeIndication__adb_SubtypeIndication368", None)
        self.__adb_SubtypeIndication368 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_ComponentDefinition367"):
                opp_val = getattr(old_value, "adb_ComponentDefinition367", None)
                if opp_val == self:
                    setattr(old_value, "adb_ComponentDefinition367", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_ComponentDefinition367"):
                opp_val = getattr(value, "adb_ComponentDefinition367", None)
                setattr(value, "adb_ComponentDefinition367", self)

    @property
    def adb_SubtypeIndication152(self):
        return self.__adb_SubtypeIndication152

    @adb_SubtypeIndication152.setter
    def adb_SubtypeIndication152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_SubtypeIndication__adb_SubtypeIndication152", None)
        self.__adb_SubtypeIndication152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_SubtypeDeclaration"):
                opp_val = getattr(old_value, "adb_SubtypeDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "adb_SubtypeDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_SubtypeDeclaration"):
                opp_val = getattr(value, "adb_SubtypeDeclaration", None)
                setattr(value, "adb_SubtypeDeclaration", self)

    @property
    def adb_SubtypeIndication339(self):
        return self.__adb_SubtypeIndication339

    @adb_SubtypeIndication339.setter
    def adb_SubtypeIndication339(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_SubtypeIndication__adb_SubtypeIndication339", None)
        self.__adb_SubtypeIndication339 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_DerivedTypeDefinition"):
                opp_val = getattr(old_value, "adb_DerivedTypeDefinition", None)
                if opp_val == self:
                    setattr(old_value, "adb_DerivedTypeDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_DerivedTypeDefinition"):
                opp_val = getattr(value, "adb_DerivedTypeDefinition", None)
                setattr(value, "adb_DerivedTypeDefinition", self)

class adb_ProtectedDefinition:

    pass
class adb_DiscriminantPart:

    pass
class adb_TypeDefinition:

    pass
class FullTypeDeclaration:

    pass
class adb_ProtectedTypeDeclaration(FullTypeDeclaration):

    pass
class adb_FullDataTypeDeclaration(FullTypeDeclaration):

    pass
class NewTypeDeclaration:

    pass
class adb_PrivateTypeDeclaration(NewTypeDeclaration):

    def __init__(self, abstract: bool, tagged: bool, limited: bool, adb_PrivateTypeDeclaration: "adb_DiscriminantPart" = None):
        self.abstract = abstract
        self.tagged = tagged
        self.limited = limited
        self.adb_PrivateTypeDeclaration = adb_PrivateTypeDeclaration
        
    @property
    def tagged(self) -> bool:
        return self.__tagged

    @tagged.setter
    def tagged(self, tagged: bool):
        self.__tagged = tagged

    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def limited(self) -> bool:
        return self.__limited

    @limited.setter
    def limited(self, limited: bool):
        self.__limited = limited

    @property
    def adb_PrivateTypeDeclaration(self):
        return self.__adb_PrivateTypeDeclaration

    @adb_PrivateTypeDeclaration.setter
    def adb_PrivateTypeDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_PrivateTypeDeclaration__adb_PrivateTypeDeclaration", None)
        self.__adb_PrivateTypeDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_DiscriminantPart43"):
                opp_val = getattr(old_value, "adb_DiscriminantPart43", None)
                if opp_val == self:
                    setattr(old_value, "adb_DiscriminantPart43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_DiscriminantPart43"):
                opp_val = getattr(value, "adb_DiscriminantPart43", None)
                setattr(value, "adb_DiscriminantPart43", self)

class adb_IncompleteTypeDeclaration(NewTypeDeclaration):

    def __init__(self, tagged: bool, adb_IncompleteTypeDeclaration: "adb_DiscriminantPart" = None):
        self.tagged = tagged
        self.adb_IncompleteTypeDeclaration = adb_IncompleteTypeDeclaration
        
    @property
    def tagged(self) -> bool:
        return self.__tagged

    @tagged.setter
    def tagged(self, tagged: bool):
        self.__tagged = tagged

    @property
    def adb_IncompleteTypeDeclaration(self):
        return self.__adb_IncompleteTypeDeclaration

    @adb_IncompleteTypeDeclaration.setter
    def adb_IncompleteTypeDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_IncompleteTypeDeclaration__adb_IncompleteTypeDeclaration", None)
        self.__adb_IncompleteTypeDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_DiscriminantPart"):
                opp_val = getattr(old_value, "adb_DiscriminantPart", None)
                if opp_val == self:
                    setattr(old_value, "adb_DiscriminantPart", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_DiscriminantPart"):
                opp_val = getattr(value, "adb_DiscriminantPart", None)
                setattr(value, "adb_DiscriminantPart", self)

class adb_FullTypeDeclaration(NewTypeDeclaration):

    pass
class TypeDeclaration:

    pass
class adb_SubtypeDeclaration(TypeDeclaration):

    pass
class adb_NewTypeDeclaration(TypeDeclaration):

    pass
class adb_PrivateExtensionDeclaration(NewTypeDeclaration):

    def __init__(self, abstract: bool, limited: bool, synchronized: bool, adb_PrivateExtensionDeclaration: "adb_DiscriminantPart" = None, adb_PrivateExtensionDeclaration47: "adb_SubtypeIndication" = None, adb_PrivateExtensionDeclaration49: "adb_InterfaceList" = None):
        self.abstract = abstract
        self.limited = limited
        self.synchronized = synchronized
        self.adb_PrivateExtensionDeclaration = adb_PrivateExtensionDeclaration
        self.adb_PrivateExtensionDeclaration47 = adb_PrivateExtensionDeclaration47
        self.adb_PrivateExtensionDeclaration49 = adb_PrivateExtensionDeclaration49
        
    @property
    def limited(self) -> bool:
        return self.__limited

    @limited.setter
    def limited(self, limited: bool):
        self.__limited = limited

    @property
    def synchronized(self) -> bool:
        return self.__synchronized

    @synchronized.setter
    def synchronized(self, synchronized: bool):
        self.__synchronized = synchronized

    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def adb_PrivateExtensionDeclaration(self):
        return self.__adb_PrivateExtensionDeclaration

    @adb_PrivateExtensionDeclaration.setter
    def adb_PrivateExtensionDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_PrivateExtensionDeclaration__adb_PrivateExtensionDeclaration", None)
        self.__adb_PrivateExtensionDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_DiscriminantPart45"):
                opp_val = getattr(old_value, "adb_DiscriminantPart45", None)
                if opp_val == self:
                    setattr(old_value, "adb_DiscriminantPart45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_DiscriminantPart45"):
                opp_val = getattr(value, "adb_DiscriminantPart45", None)
                setattr(value, "adb_DiscriminantPart45", self)

    @property
    def adb_PrivateExtensionDeclaration47(self):
        return self.__adb_PrivateExtensionDeclaration47

    @adb_PrivateExtensionDeclaration47.setter
    def adb_PrivateExtensionDeclaration47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_PrivateExtensionDeclaration__adb_PrivateExtensionDeclaration47", None)
        self.__adb_PrivateExtensionDeclaration47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_SubtypeIndication"):
                opp_val = getattr(old_value, "adb_SubtypeIndication", None)
                if opp_val == self:
                    setattr(old_value, "adb_SubtypeIndication", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_SubtypeIndication"):
                opp_val = getattr(value, "adb_SubtypeIndication", None)
                setattr(value, "adb_SubtypeIndication", self)

    @property
    def adb_PrivateExtensionDeclaration49(self):
        return self.__adb_PrivateExtensionDeclaration49

    @adb_PrivateExtensionDeclaration49.setter
    def adb_PrivateExtensionDeclaration49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_PrivateExtensionDeclaration__adb_PrivateExtensionDeclaration49", None)
        self.__adb_PrivateExtensionDeclaration49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_InterfaceList50"):
                opp_val = getattr(old_value, "adb_InterfaceList50", None)
                if opp_val == self:
                    setattr(old_value, "adb_InterfaceList50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_InterfaceList50"):
                opp_val = getattr(value, "adb_InterfaceList50", None)
                setattr(value, "adb_InterfaceList50", self)

class adb_KnownDiscriminantPart(DiscriminantPart):

    pass
class DeclarativeItem:

    pass
class adb_Body(DeclarativeItem):

    pass
class adb_HandledSequenceOfStatements:

    pass
class adb_DeclarativeItem:

    pass
class adb_DeclarativeBlock:

    pass
class adb_TaskDefinition:

    pass
class adb_InterfaceList:

    pass
class adb_BasicDeclarativeItem(DeclarativeItem):

    pass
class adb_GenericActualPart:

    pass
class adb_OverridingIndicator:

    def __init__(self, not: bool, adb_OverridingIndicator: "adb_GenericInstantiation" = None, adb_OverridingIndicator52: "adb_EntryDeclaration" = None, adb_OverridingIndicator67: "adb_SubprogramSpecification" = None):
        self.not = not
        self.adb_OverridingIndicator = adb_OverridingIndicator
        self.adb_OverridingIndicator52 = adb_OverridingIndicator52
        self.adb_OverridingIndicator67 = adb_OverridingIndicator67
        
    @property
    def not(self) -> bool:
        return self.__not

    @not.setter
    def not(self, not: bool):
        self.__not = not

    @property
    def adb_OverridingIndicator(self):
        return self.__adb_OverridingIndicator

    @adb_OverridingIndicator.setter
    def adb_OverridingIndicator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_OverridingIndicator__adb_OverridingIndicator", None)
        self.__adb_OverridingIndicator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_GenericInstantiation"):
                opp_val = getattr(old_value, "adb_GenericInstantiation", None)
                if opp_val == self:
                    setattr(old_value, "adb_GenericInstantiation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_GenericInstantiation"):
                opp_val = getattr(value, "adb_GenericInstantiation", None)
                setattr(value, "adb_GenericInstantiation", self)

    @property
    def adb_OverridingIndicator67(self):
        return self.__adb_OverridingIndicator67

    @adb_OverridingIndicator67.setter
    def adb_OverridingIndicator67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_OverridingIndicator__adb_OverridingIndicator67", None)
        self.__adb_OverridingIndicator67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_SubprogramSpecification66"):
                opp_val = getattr(old_value, "adb_SubprogramSpecification66", None)
                if opp_val == self:
                    setattr(old_value, "adb_SubprogramSpecification66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_SubprogramSpecification66"):
                opp_val = getattr(value, "adb_SubprogramSpecification66", None)
                setattr(value, "adb_SubprogramSpecification66", self)

    @property
    def adb_OverridingIndicator52(self):
        return self.__adb_OverridingIndicator52

    @adb_OverridingIndicator52.setter
    def adb_OverridingIndicator52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_OverridingIndicator__adb_OverridingIndicator52", None)
        self.__adb_OverridingIndicator52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_EntryDeclaration"):
                opp_val = getattr(old_value, "adb_EntryDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "adb_EntryDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_EntryDeclaration"):
                opp_val = getattr(value, "adb_EntryDeclaration", None)
                setattr(value, "adb_EntryDeclaration", self)

class adb_LibrarySpecification:

    pass
class ProtectedOperationItem:

    pass
class ProperBody:

    pass
class adb_ProtectedBody(ProperBody):

    def __init__(self, identifier: str, idTask: str, adb_ProtectedBody: set["adb_ProtectedOperationItem"] = None):
        self.identifier = identifier
        self.idTask = idTask
        self.adb_ProtectedBody = adb_ProtectedBody if adb_ProtectedBody is not None else set()
        
    @property
    def idTask(self) -> str:
        return self.__idTask

    @idTask.setter
    def idTask(self, idTask: str):
        self.__idTask = idTask

    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def adb_ProtectedBody(self):
        return self.__adb_ProtectedBody

    @adb_ProtectedBody.setter
    def adb_ProtectedBody(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_ProtectedBody__adb_ProtectedBody", None)
        self.__adb_ProtectedBody = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adb_ProtectedOperationItem"):
                    opp_val = getattr(item, "adb_ProtectedOperationItem", None)
                    
                    if opp_val == self:
                        setattr(item, "adb_ProtectedOperationItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adb_ProtectedOperationItem"):
                    opp_val = getattr(item, "adb_ProtectedOperationItem", None)
                    
                    setattr(item, "adb_ProtectedOperationItem", self)
                    

class DeclarativeBlock:

    pass
class adb_EntryBody(DeclarativeBlock, ProtectedOperationItem):

    def __init__(self, endid: str, adb_EntryBody: "adb_EntryDeclaration" = None, adb_EntryBody239: "adb_EntryBodyFormalPart" = None, adb_EntryBody241: "adb_EntryBarrier" = None):
        self.endid = endid
        self.adb_EntryBody = adb_EntryBody
        self.adb_EntryBody239 = adb_EntryBody239
        self.adb_EntryBody241 = adb_EntryBody241
        
    @property
    def endid(self) -> str:
        return self.__endid

    @endid.setter
    def endid(self, endid: str):
        self.__endid = endid

    @property
    def adb_EntryBody239(self):
        return self.__adb_EntryBody239

    @adb_EntryBody239.setter
    def adb_EntryBody239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_EntryBody__adb_EntryBody239", None)
        self.__adb_EntryBody239 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_EntryBodyFormalPart"):
                opp_val = getattr(old_value, "adb_EntryBodyFormalPart", None)
                if opp_val == self:
                    setattr(old_value, "adb_EntryBodyFormalPart", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_EntryBodyFormalPart"):
                opp_val = getattr(value, "adb_EntryBodyFormalPart", None)
                setattr(value, "adb_EntryBodyFormalPart", self)

    @property
    def adb_EntryBody241(self):
        return self.__adb_EntryBody241

    @adb_EntryBody241.setter
    def adb_EntryBody241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_EntryBody__adb_EntryBody241", None)
        self.__adb_EntryBody241 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_EntryBarrier"):
                opp_val = getattr(old_value, "adb_EntryBarrier", None)
                if opp_val == self:
                    setattr(old_value, "adb_EntryBarrier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_EntryBarrier"):
                opp_val = getattr(value, "adb_EntryBarrier", None)
                setattr(value, "adb_EntryBarrier", self)

    @property
    def adb_EntryBody(self):
        return self.__adb_EntryBody

    @adb_EntryBody.setter
    def adb_EntryBody(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_EntryBody__adb_EntryBody", None)
        self.__adb_EntryBody = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_EntryDeclaration237"):
                opp_val = getattr(old_value, "adb_EntryDeclaration237", None)
                if opp_val == self:
                    setattr(old_value, "adb_EntryDeclaration237", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_EntryDeclaration237"):
                opp_val = getattr(value, "adb_EntryDeclaration237", None)
                setattr(value, "adb_EntryDeclaration237", self)

class adb_TaskBody(DeclarativeBlock, ProperBody):

    pass
class adb_BlockStatement(DeclarativeBlock, CompoundStatement):

    def __init__(self, blockStatementIdentifier: str):
        self.blockStatementIdentifier = blockStatementIdentifier
        
    @property
    def blockStatementIdentifier(self) -> str:
        return self.__blockStatementIdentifier

    @blockStatementIdentifier.setter
    def blockStatementIdentifier(self, blockStatementIdentifier: str):
        self.__blockStatementIdentifier = blockStatementIdentifier

class BasicDeclaration:

    pass
class adb_TypeDeclaration(BasicDeclaration):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class adb_TaskDeclaration(BasicDeclaration):

    def __init__(self, name: str, adb_TaskDeclaration32: "adb_InterfaceList" = None, adb_TaskDeclaration34: "adb_TaskDefinition" = None, adb_TaskDeclaration37: "adb_TaskDeclaration" = None, adb_TaskDeclaration35: "adb_TaskDeclaration" = None, adb_TaskDeclaration: "adb_KnownDiscriminantPart" = None, adb_TaskDeclaration221: "adb_TaskBody" = None, adb_TaskDeclaration224: "adb_TaskBody" = None):
        self.name = name
        self.adb_TaskDeclaration32 = adb_TaskDeclaration32
        self.adb_TaskDeclaration34 = adb_TaskDeclaration34
        self.adb_TaskDeclaration37 = adb_TaskDeclaration37
        self.adb_TaskDeclaration35 = adb_TaskDeclaration35
        self.adb_TaskDeclaration = adb_TaskDeclaration
        self.adb_TaskDeclaration221 = adb_TaskDeclaration221
        self.adb_TaskDeclaration224 = adb_TaskDeclaration224
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def adb_TaskDeclaration35(self):
        return self.__adb_TaskDeclaration35

    @adb_TaskDeclaration35.setter
    def adb_TaskDeclaration35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_TaskDeclaration__adb_TaskDeclaration35", None)
        self.__adb_TaskDeclaration35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_TaskDeclaration37"):
                opp_val = getattr(old_value, "adb_TaskDeclaration37", None)
                if opp_val == self:
                    setattr(old_value, "adb_TaskDeclaration37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_TaskDeclaration37"):
                opp_val = getattr(value, "adb_TaskDeclaration37", None)
                setattr(value, "adb_TaskDeclaration37", self)

    @property
    def adb_TaskDeclaration224(self):
        return self.__adb_TaskDeclaration224

    @adb_TaskDeclaration224.setter
    def adb_TaskDeclaration224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_TaskDeclaration__adb_TaskDeclaration224", None)
        self.__adb_TaskDeclaration224 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_TaskBody223"):
                opp_val = getattr(old_value, "adb_TaskBody223", None)
                if opp_val == self:
                    setattr(old_value, "adb_TaskBody223", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_TaskBody223"):
                opp_val = getattr(value, "adb_TaskBody223", None)
                setattr(value, "adb_TaskBody223", self)

    @property
    def adb_TaskDeclaration34(self):
        return self.__adb_TaskDeclaration34

    @adb_TaskDeclaration34.setter
    def adb_TaskDeclaration34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_TaskDeclaration__adb_TaskDeclaration34", None)
        self.__adb_TaskDeclaration34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_TaskDefinition"):
                opp_val = getattr(old_value, "adb_TaskDefinition", None)
                if opp_val == self:
                    setattr(old_value, "adb_TaskDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_TaskDefinition"):
                opp_val = getattr(value, "adb_TaskDefinition", None)
                setattr(value, "adb_TaskDefinition", self)

    @property
    def adb_TaskDeclaration(self):
        return self.__adb_TaskDeclaration

    @adb_TaskDeclaration.setter
    def adb_TaskDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_TaskDeclaration__adb_TaskDeclaration", None)
        self.__adb_TaskDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_KnownDiscriminantPart"):
                opp_val = getattr(old_value, "adb_KnownDiscriminantPart", None)
                if opp_val == self:
                    setattr(old_value, "adb_KnownDiscriminantPart", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_KnownDiscriminantPart"):
                opp_val = getattr(value, "adb_KnownDiscriminantPart", None)
                setattr(value, "adb_KnownDiscriminantPart", self)

    @property
    def adb_TaskDeclaration37(self):
        return self.__adb_TaskDeclaration37

    @adb_TaskDeclaration37.setter
    def adb_TaskDeclaration37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_TaskDeclaration__adb_TaskDeclaration37", None)
        self.__adb_TaskDeclaration37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_TaskDeclaration35"):
                opp_val = getattr(old_value, "adb_TaskDeclaration35", None)
                if opp_val == self:
                    setattr(old_value, "adb_TaskDeclaration35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_TaskDeclaration35"):
                opp_val = getattr(value, "adb_TaskDeclaration35", None)
                setattr(value, "adb_TaskDeclaration35", self)

    @property
    def adb_TaskDeclaration32(self):
        return self.__adb_TaskDeclaration32

    @adb_TaskDeclaration32.setter
    def adb_TaskDeclaration32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_TaskDeclaration__adb_TaskDeclaration32", None)
        self.__adb_TaskDeclaration32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_InterfaceList"):
                opp_val = getattr(old_value, "adb_InterfaceList", None)
                if opp_val == self:
                    setattr(old_value, "adb_InterfaceList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_InterfaceList"):
                opp_val = getattr(value, "adb_InterfaceList", None)
                setattr(value, "adb_InterfaceList", self)

    @property
    def adb_TaskDeclaration221(self):
        return self.__adb_TaskDeclaration221

    @adb_TaskDeclaration221.setter
    def adb_TaskDeclaration221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_TaskDeclaration__adb_TaskDeclaration221", None)
        self.__adb_TaskDeclaration221 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_TaskBody"):
                opp_val = getattr(old_value, "adb_TaskBody", None)
                if opp_val == self:
                    setattr(old_value, "adb_TaskBody", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_TaskBody"):
                opp_val = getattr(value, "adb_TaskBody", None)
                setattr(value, "adb_TaskBody", self)

class adb_SubprogramDeclaration(BasicDeclaration, ProtectedOperationItem, ProtectedOperationDeclaration):

    def __init__(self, abstract: bool, renamedName: str, null: bool, adb_SubprogramDeclaration: "adb_SubprogramSpecification" = None):
        self.abstract = abstract
        self.renamedName = renamedName
        self.null = null
        self.adb_SubprogramDeclaration = adb_SubprogramDeclaration
        
    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def renamedName(self) -> str:
        return self.__renamedName

    @renamedName.setter
    def renamedName(self, renamedName: str):
        self.__renamedName = renamedName

    @property
    def null(self) -> bool:
        return self.__null

    @null.setter
    def null(self, null: bool):
        self.__null = null

    @property
    def adb_SubprogramDeclaration(self):
        return self.__adb_SubprogramDeclaration

    @adb_SubprogramDeclaration.setter
    def adb_SubprogramDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_SubprogramDeclaration__adb_SubprogramDeclaration", None)
        self.__adb_SubprogramDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_SubprogramSpecification64"):
                opp_val = getattr(old_value, "adb_SubprogramSpecification64", None)
                if opp_val == self:
                    setattr(old_value, "adb_SubprogramSpecification64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_SubprogramSpecification64"):
                opp_val = getattr(value, "adb_SubprogramSpecification64", None)
                setattr(value, "adb_SubprogramSpecification64", self)

class adb_ObjectDeclaration(BasicDeclaration):

    pass
class adb_NumberDeclaration(BasicDeclaration):

    pass
class adb_ExceptionDeclaration(BasicDeclaration):

    pass
class LibraryUnitSpecification:

    pass
class adb_GenericInstantiation(BasicDeclaration, LibraryUnitSpecification):

    def __init__(self, name: str, genericName: str, adb_GenericInstantiation: "adb_OverridingIndicator" = None, adb_GenericInstantiation20: "adb_GenericActualPart" = None):
        self.name = name
        self.genericName = genericName
        self.adb_GenericInstantiation = adb_GenericInstantiation
        self.adb_GenericInstantiation20 = adb_GenericInstantiation20
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def genericName(self) -> str:
        return self.__genericName

    @genericName.setter
    def genericName(self, genericName: str):
        self.__genericName = genericName

    @property
    def adb_GenericInstantiation20(self):
        return self.__adb_GenericInstantiation20

    @adb_GenericInstantiation20.setter
    def adb_GenericInstantiation20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_GenericInstantiation__adb_GenericInstantiation20", None)
        self.__adb_GenericInstantiation20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_GenericActualPart"):
                opp_val = getattr(old_value, "adb_GenericActualPart", None)
                if opp_val == self:
                    setattr(old_value, "adb_GenericActualPart", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_GenericActualPart"):
                opp_val = getattr(value, "adb_GenericActualPart", None)
                setattr(value, "adb_GenericActualPart", self)

    @property
    def adb_GenericInstantiation(self):
        return self.__adb_GenericInstantiation

    @adb_GenericInstantiation.setter
    def adb_GenericInstantiation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_GenericInstantiation__adb_GenericInstantiation", None)
        self.__adb_GenericInstantiation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_OverridingIndicator"):
                opp_val = getattr(old_value, "adb_OverridingIndicator", None)
                if opp_val == self:
                    setattr(old_value, "adb_OverridingIndicator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_OverridingIndicator"):
                opp_val = getattr(value, "adb_OverridingIndicator", None)
                setattr(value, "adb_OverridingIndicator", self)

class adb_PackageDeclaration(BasicDeclaration, LibraryUnitSpecification):

    def __init__(self, name: str, adb_PackageDeclaration: "adb_PackageBody" = None, adb_PackageDeclaration217: "adb_PackageBody" = None):
        self.name = name
        self.adb_PackageDeclaration = adb_PackageDeclaration
        self.adb_PackageDeclaration217 = adb_PackageDeclaration217
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def adb_PackageDeclaration(self):
        return self.__adb_PackageDeclaration

    @adb_PackageDeclaration.setter
    def adb_PackageDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_PackageDeclaration__adb_PackageDeclaration", None)
        self.__adb_PackageDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_PackageBody"):
                opp_val = getattr(old_value, "adb_PackageBody", None)
                if opp_val == self:
                    setattr(old_value, "adb_PackageBody", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_PackageBody"):
                opp_val = getattr(value, "adb_PackageBody", None)
                setattr(value, "adb_PackageBody", self)

    @property
    def adb_PackageDeclaration217(self):
        return self.__adb_PackageDeclaration217

    @adb_PackageDeclaration217.setter
    def adb_PackageDeclaration217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_PackageDeclaration__adb_PackageDeclaration217", None)
        self.__adb_PackageDeclaration217 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_PackageBody216"):
                opp_val = getattr(old_value, "adb_PackageBody216", None)
                if opp_val == self:
                    setattr(old_value, "adb_PackageBody216", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_PackageBody216"):
                opp_val = getattr(value, "adb_PackageBody216", None)
                setattr(value, "adb_PackageBody216", self)

class adb_LibraryUnitSpecification:

    pass
class Unit:

    pass
class adb_PackageBody(DeclarativeBlock, Unit, ProperBody):

    pass
class adb_SubprogramBody(DeclarativeBlock, Unit, ProperBody, ProtectedOperationItem):

    def __init__(self, endname: str, adb_SubprogramBody: "adb_SubprogramSpecification" = None):
        self.endname = endname
        self.adb_SubprogramBody = adb_SubprogramBody
        
    @property
    def endname(self) -> str:
        return self.__endname

    @endname.setter
    def endname(self, endname: str):
        self.__endname = endname

    @property
    def adb_SubprogramBody(self):
        return self.__adb_SubprogramBody

    @adb_SubprogramBody.setter
    def adb_SubprogramBody(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_SubprogramBody__adb_SubprogramBody", None)
        self.__adb_SubprogramBody = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_SubprogramSpecification"):
                opp_val = getattr(old_value, "adb_SubprogramSpecification", None)
                if opp_val == self:
                    setattr(old_value, "adb_SubprogramSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_SubprogramSpecification"):
                opp_val = getattr(value, "adb_SubprogramSpecification", None)
                setattr(value, "adb_SubprogramSpecification", self)

class adb_SeparateSubunit(Unit):

    def __init__(self, parentUnitName: str, adb_SeparateSubunit: "adb_ProperBody" = None):
        self.parentUnitName = parentUnitName
        self.adb_SeparateSubunit = adb_SeparateSubunit
        
    @property
    def parentUnitName(self) -> str:
        return self.__parentUnitName

    @parentUnitName.setter
    def parentUnitName(self, parentUnitName: str):
        self.__parentUnitName = parentUnitName

    @property
    def adb_SeparateSubunit(self):
        return self.__adb_SeparateSubunit

    @adb_SeparateSubunit.setter
    def adb_SeparateSubunit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_SeparateSubunit__adb_SeparateSubunit", None)
        self.__adb_SeparateSubunit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_ProperBody"):
                opp_val = getattr(old_value, "adb_ProperBody", None)
                if opp_val == self:
                    setattr(old_value, "adb_ProperBody", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_ProperBody"):
                opp_val = getattr(value, "adb_ProperBody", None)
                setattr(value, "adb_ProperBody", self)

class adb_GenericItems:

    pass
class adb_GenericDeclaration(BasicDeclaration, LibraryUnitSpecification):

    pass
class adb_PackageSpecification:

    def __init__(self, endname: str, adb_PackageSpecification: "adb_PackageDefinition" = None, adb_PackageSpecification24: set["adb_BasicDeclarativeItem"] = None, adb_PackageSpecification22: set["adb_BasicDeclarativeItem"] = None):
        self.endname = endname
        self.adb_PackageSpecification = adb_PackageSpecification
        self.adb_PackageSpecification24 = adb_PackageSpecification24 if adb_PackageSpecification24 is not None else set()
        self.adb_PackageSpecification22 = adb_PackageSpecification22 if adb_PackageSpecification22 is not None else set()
        
    @property
    def endname(self) -> str:
        return self.__endname

    @endname.setter
    def endname(self, endname: str):
        self.__endname = endname

    @property
    def adb_PackageSpecification24(self):
        return self.__adb_PackageSpecification24

    @adb_PackageSpecification24.setter
    def adb_PackageSpecification24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_PackageSpecification__adb_PackageSpecification24", None)
        self.__adb_PackageSpecification24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adb_BasicDeclarativeItem25"):
                    opp_val = getattr(item, "adb_BasicDeclarativeItem25", None)
                    
                    if opp_val == self:
                        setattr(item, "adb_BasicDeclarativeItem25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adb_BasicDeclarativeItem25"):
                    opp_val = getattr(item, "adb_BasicDeclarativeItem25", None)
                    
                    setattr(item, "adb_BasicDeclarativeItem25", self)
                    

    @property
    def adb_PackageSpecification(self):
        return self.__adb_PackageSpecification

    @adb_PackageSpecification.setter
    def adb_PackageSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_PackageSpecification__adb_PackageSpecification", None)
        self.__adb_PackageSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_PackageDefinition"):
                opp_val = getattr(old_value, "adb_PackageDefinition", None)
                if opp_val == self:
                    setattr(old_value, "adb_PackageDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_PackageDefinition"):
                opp_val = getattr(value, "adb_PackageDefinition", None)
                setattr(value, "adb_PackageDefinition", self)

    @property
    def adb_PackageSpecification22(self):
        return self.__adb_PackageSpecification22

    @adb_PackageSpecification22.setter
    def adb_PackageSpecification22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_PackageSpecification__adb_PackageSpecification22", None)
        self.__adb_PackageSpecification22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adb_BasicDeclarativeItem"):
                    opp_val = getattr(item, "adb_BasicDeclarativeItem", None)
                    
                    if opp_val == self:
                        setattr(item, "adb_BasicDeclarativeItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adb_BasicDeclarativeItem"):
                    opp_val = getattr(item, "adb_BasicDeclarativeItem", None)
                    
                    setattr(item, "adb_BasicDeclarativeItem", self)
                    

class LibrarySpecification:

    pass
class adb_SubprogramSpecification(LibraryUnitSpecification, LibrarySpecification, BodyStub):

    pass
class PackageDeclaration:

    pass
class adb_Renaming(PackageDeclaration):

    def __init__(self, renamed: str):
        self.renamed = renamed
        
    @property
    def renamed(self) -> str:
        return self.__renamed

    @renamed.setter
    def renamed(self, renamed: str):
        self.__renamed = renamed

class adb_PackageDefinition(PackageDeclaration, LibrarySpecification):

    pass
class ContextItem:

    pass
class adb_WithClause(ContextItem):

    def __init__(self, limited: bool, private: bool, adb_WithClause: set["adb_LibraryUnitDeclaration"] = None):
        self.limited = limited
        self.private = private
        self.adb_WithClause = adb_WithClause if adb_WithClause is not None else set()
        
    @property
    def limited(self) -> bool:
        return self.__limited

    @limited.setter
    def limited(self, limited: bool):
        self.__limited = limited

    @property
    def private(self) -> bool:
        return self.__private

    @private.setter
    def private(self, private: bool):
        self.__private = private

    @property
    def adb_WithClause(self):
        return self.__adb_WithClause

    @adb_WithClause.setter
    def adb_WithClause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_WithClause__adb_WithClause", None)
        self.__adb_WithClause = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adb_LibraryUnitDeclaration"):
                    opp_val = getattr(item, "adb_LibraryUnitDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "adb_LibraryUnitDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adb_LibraryUnitDeclaration"):
                    opp_val = getattr(item, "adb_LibraryUnitDeclaration", None)
                    
                    setattr(item, "adb_LibraryUnitDeclaration", self)
                    

class adb_ContextItem:

    pass
class adb_Unit:

    pass
class adb_ContextClause:

    pass
class UseClause:

    pass
class adb_UseTypeClause(UseClause):

    def __init__(self, typesNames: str, useTypeRefs: str):
        self.typesNames = typesNames
        self.useTypeRefs = useTypeRefs
        
    @property
    def typesNames(self) -> str:
        return self.__typesNames

    @typesNames.setter
    def typesNames(self, typesNames: str):
        self.__typesNames = typesNames

    @property
    def useTypeRefs(self) -> str:
        return self.__useTypeRefs

    @useTypeRefs.setter
    def useTypeRefs(self, useTypeRefs: str):
        self.__useTypeRefs = useTypeRefs

class adb_UsePackageClause(UseClause):

    pass
class GenericItem:

    pass
class adb_GenericFormalParameterDeclaration(GenericItem):

    pass
class BasicDeclarativeItem:

    pass
class adb_BasicDeclaration(BasicDeclarativeItem):

    pass
class adb_AspectClause(ProtectedOperationItem, ComponentItem, BasicDeclarativeItem, ProtectedOperationDeclaration, TaskItem):

    def __init__(self, name: str, adb_AspectClause439: "adb_ModClause" = None, adb_AspectClause441: set["adb_ComponentClause"] = None, adb_AspectClause: "adb_Expression" = None):
        self.name = name
        self.adb_AspectClause439 = adb_AspectClause439
        self.adb_AspectClause441 = adb_AspectClause441 if adb_AspectClause441 is not None else set()
        self.adb_AspectClause = adb_AspectClause
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def adb_AspectClause439(self):
        return self.__adb_AspectClause439

    @adb_AspectClause439.setter
    def adb_AspectClause439(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_AspectClause__adb_AspectClause439", None)
        self.__adb_AspectClause439 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_ModClause"):
                opp_val = getattr(old_value, "adb_ModClause", None)
                if opp_val == self:
                    setattr(old_value, "adb_ModClause", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_ModClause"):
                opp_val = getattr(value, "adb_ModClause", None)
                setattr(value, "adb_ModClause", self)

    @property
    def adb_AspectClause441(self):
        return self.__adb_AspectClause441

    @adb_AspectClause441.setter
    def adb_AspectClause441(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_AspectClause__adb_AspectClause441", None)
        self.__adb_AspectClause441 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adb_ComponentClause"):
                    opp_val = getattr(item, "adb_ComponentClause", None)
                    
                    if opp_val == self:
                        setattr(item, "adb_ComponentClause", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adb_ComponentClause"):
                    opp_val = getattr(item, "adb_ComponentClause", None)
                    
                    setattr(item, "adb_ComponentClause", self)
                    

    @property
    def adb_AspectClause(self):
        return self.__adb_AspectClause

    @adb_AspectClause.setter
    def adb_AspectClause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_AspectClause__adb_AspectClause", None)
        self.__adb_AspectClause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_Expression437"):
                opp_val = getattr(old_value, "adb_Expression437", None)
                if opp_val == self:
                    setattr(old_value, "adb_Expression437", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_Expression437"):
                opp_val = getattr(value, "adb_Expression437", None)
                setattr(value, "adb_Expression437", self)

class adb_Pragma(Statement, ContextItem, BasicDeclarativeItem):

    def __init__(self, name: str, adb_Pragma: "adb_CompilationUnit" = None, adb_Pragma147: set["adb_PragmaArgumentAssociation"] = None):
        self.name = name
        self.adb_Pragma = adb_Pragma
        self.adb_Pragma147 = adb_Pragma147 if adb_Pragma147 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def adb_Pragma(self):
        return self.__adb_Pragma

    @adb_Pragma.setter
    def adb_Pragma(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Pragma__adb_Pragma", None)
        self.__adb_Pragma = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_CompilationUnit6"):
                opp_val = getattr(old_value, "adb_CompilationUnit6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_CompilationUnit6"):
                opp_val = getattr(value, "adb_CompilationUnit6", None)
                if opp_val is None:
                    setattr(value, "adb_CompilationUnit6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def adb_Pragma147(self):
        return self.__adb_Pragma147

    @adb_Pragma147.setter
    def adb_Pragma147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_Pragma__adb_Pragma147", None)
        self.__adb_Pragma147 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adb_PragmaArgumentAssociation"):
                    opp_val = getattr(item, "adb_PragmaArgumentAssociation", None)
                    
                    if opp_val == self:
                        setattr(item, "adb_PragmaArgumentAssociation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adb_PragmaArgumentAssociation"):
                    opp_val = getattr(item, "adb_PragmaArgumentAssociation", None)
                    
                    setattr(item, "adb_PragmaArgumentAssociation", self)
                    

class adb_UseClause(GenericItem, ContextItem, BasicDeclarativeItem):

    pass
class adb_LibraryUnitDeclaration(Unit):

    def __init__(self, private: bool, adb_LibraryUnitDeclaration: "adb_WithClause" = None, adb_LibraryUnitDeclaration11: "adb_UsePackageClause" = None, adb_LibraryUnitDeclaration13: "adb_LibraryUnitSpecification" = None):
        self.private = private
        self.adb_LibraryUnitDeclaration = adb_LibraryUnitDeclaration
        self.adb_LibraryUnitDeclaration11 = adb_LibraryUnitDeclaration11
        self.adb_LibraryUnitDeclaration13 = adb_LibraryUnitDeclaration13
        
    @property
    def private(self) -> bool:
        return self.__private

    @private.setter
    def private(self, private: bool):
        self.__private = private

    @property
    def adb_LibraryUnitDeclaration(self):
        return self.__adb_LibraryUnitDeclaration

    @adb_LibraryUnitDeclaration.setter
    def adb_LibraryUnitDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_LibraryUnitDeclaration__adb_LibraryUnitDeclaration", None)
        self.__adb_LibraryUnitDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_WithClause"):
                opp_val = getattr(old_value, "adb_WithClause", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_WithClause"):
                opp_val = getattr(value, "adb_WithClause", None)
                if opp_val is None:
                    setattr(value, "adb_WithClause", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def adb_LibraryUnitDeclaration11(self):
        return self.__adb_LibraryUnitDeclaration11

    @adb_LibraryUnitDeclaration11.setter
    def adb_LibraryUnitDeclaration11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_LibraryUnitDeclaration__adb_LibraryUnitDeclaration11", None)
        self.__adb_LibraryUnitDeclaration11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_UsePackageClause"):
                opp_val = getattr(old_value, "adb_UsePackageClause", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_UsePackageClause"):
                opp_val = getattr(value, "adb_UsePackageClause", None)
                if opp_val is None:
                    setattr(value, "adb_UsePackageClause", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def adb_LibraryUnitDeclaration13(self):
        return self.__adb_LibraryUnitDeclaration13

    @adb_LibraryUnitDeclaration13.setter
    def adb_LibraryUnitDeclaration13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adb_LibraryUnitDeclaration__adb_LibraryUnitDeclaration13", None)
        self.__adb_LibraryUnitDeclaration13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adb_LibraryUnitSpecification"):
                opp_val = getattr(old_value, "adb_LibraryUnitSpecification", None)
                if opp_val == self:
                    setattr(old_value, "adb_LibraryUnitSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adb_LibraryUnitSpecification"):
                opp_val = getattr(value, "adb_LibraryUnitSpecification", None)
                setattr(value, "adb_LibraryUnitSpecification", self)

class adb_CompilationUnit:

    pass
class adb_Compilation:

    pass