####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Enumerations
SeverityKind: Enumeration = Enumeration(
    name="SeverityKind",
    literals={
            EnumerationLiteral(name="error"),
			EnumerationLiteral(name="warning"),
			EnumerationLiteral(name="fatal")
    }
)

# Classes
ImperativeOCL_AssertExp = Class(name="ImperativeOCL::AssertExp")
LogExp = Class(name="LogExp")
ImperativeOCL_AltExp = Class(name="ImperativeOCL::AltExp")
ImperativeExpression = Class(name="ImperativeExpression")
OclExpression = Class(name="OclExpression")
Type = Class(name="Type")
Variable = Class(name="Variable")
ImperativeOCL_ComputeExp = Class(name="ImperativeOCL::ComputeExp")
ImperativeOCL_AssignExp = Class(name="ImperativeOCL::AssignExp")
ImperativeOCL_BlockExp = Class(name="ImperativeOCL::BlockExp")
ImperativeOCL_BreakExp = Class(name="ImperativeOCL::BreakExp")
ImperativeOCL_CatchExp = Class(name="ImperativeOCL::CatchExp")
CollectionType = Class(name="CollectionType")
ImperativeOCL_ForExp = Class(name="ImperativeOCL::ForExp")
ImperativeLoopExp = Class(name="ImperativeLoopExp")
ImperativeOCL_ImperativeExpression = Class(name="ImperativeOCL::ImperativeExpression", is_abstract=True)
ImperativeOCL_ImperativeIterateExp = Class(name="ImperativeOCL::ImperativeIterateExp")
ImperativeOCL_ImperativeLoopExp = Class(name="ImperativeOCL::ImperativeLoopExp", is_abstract=True)
LoopExp = Class(name="LoopExp")
ImperativeOCL_ContinueExp = Class(name="ImperativeOCL::ContinueExp")
ImperativeOCL_DictLiteralExp = Class(name="ImperativeOCL::DictLiteralExp")
LiteralExp = Class(name="LiteralExp")
DictLiteralPart = Class(name="DictLiteralPart")
ImperativeOCL_DictLiteralPart = Class(name="ImperativeOCL::DictLiteralPart")
Element = Class(name="Element")
DictLiteralExp = Class(name="DictLiteralExp")
ImperativeOCL_DictionaryType = Class(name="ImperativeOCL::DictionaryType")
ImperativeOCL_LogExp = Class(name="ImperativeOCL::LogExp")
OperationCallExp = Class(name="OperationCallExp")
ImperativeOCL_RaiseExp = Class(name="ImperativeOCL::RaiseExp")
ImperativeOCL_ReturnExp = Class(name="ImperativeOCL::ReturnExp")
ImperativeOCL_InstantiationExp = Class(name="ImperativeOCL::InstantiationExp")
Class_ = Class(name="Class")
Operation = Class(name="Operation")
ImperativeOCL_ListLiteralExp = Class(name="ImperativeOCL::ListLiteralExp")
ImperativeOCL_ListType = Class(name="ImperativeOCL::ListType")
ImperativeOCL_Typedef = Class(name="ImperativeOCL::Typedef")
ImperativeOCL_UnlinkExp = Class(name="ImperativeOCL::UnlinkExp")
ImperativeOCL_SwitchExp = Class(name="ImperativeOCL::SwitchExp")
AltExp = Class(name="AltExp")
ImperativeOCL_TryExp = Class(name="ImperativeOCL::TryExp")
CatchExp = Class(name="CatchExp")
ImperativeOCL_VariableInitExp = Class(name="ImperativeOCL::VariableInitExp")
ImperativeOCL_WhileExp = Class(name="ImperativeOCL::WhileExp")

# ImperativeOCL_AssertExp class attributes and methods
ImperativeOCL_AssertExp_severity: Property = Property(name="severity", type=StringType)
ImperativeOCL_AssertExp.attributes={ImperativeOCL_AssertExp_severity}

# LogExp class attributes and methods

# ImperativeOCL_AltExp class attributes and methods

# ImperativeExpression class attributes and methods

# OclExpression class attributes and methods

# Type class attributes and methods

# Variable class attributes and methods

# ImperativeOCL_ComputeExp class attributes and methods

# ImperativeOCL_AssignExp class attributes and methods
ImperativeOCL_AssignExp_isReset: Property = Property(name="isReset", type=StringType)
ImperativeOCL_AssignExp.attributes={ImperativeOCL_AssignExp_isReset}

# ImperativeOCL_BlockExp class attributes and methods

# ImperativeOCL_BreakExp class attributes and methods

# ImperativeOCL_CatchExp class attributes and methods

# CollectionType class attributes and methods

# ImperativeOCL_ForExp class attributes and methods

# ImperativeLoopExp class attributes and methods

# ImperativeOCL_ImperativeExpression class attributes and methods

# ImperativeOCL_ImperativeIterateExp class attributes and methods

# ImperativeOCL_ImperativeLoopExp class attributes and methods

# LoopExp class attributes and methods

# ImperativeOCL_ContinueExp class attributes and methods

# ImperativeOCL_DictLiteralExp class attributes and methods

# LiteralExp class attributes and methods

# DictLiteralPart class attributes and methods

# ImperativeOCL_DictLiteralPart class attributes and methods

# Element class attributes and methods

# DictLiteralExp class attributes and methods

# ImperativeOCL_DictionaryType class attributes and methods

# ImperativeOCL_LogExp class attributes and methods

# OperationCallExp class attributes and methods

# ImperativeOCL_RaiseExp class attributes and methods

# ImperativeOCL_ReturnExp class attributes and methods

# ImperativeOCL_InstantiationExp class attributes and methods

# Class class attributes and methods

# Operation class attributes and methods

# ImperativeOCL_ListLiteralExp class attributes and methods

# ImperativeOCL_ListType class attributes and methods

# ImperativeOCL_Typedef class attributes and methods

# ImperativeOCL_UnlinkExp class attributes and methods

# ImperativeOCL_SwitchExp class attributes and methods

# AltExp class attributes and methods

# ImperativeOCL_TryExp class attributes and methods

# CatchExp class attributes and methods

# ImperativeOCL_VariableInitExp class attributes and methods
ImperativeOCL_VariableInitExp_withResult: Property = Property(name="withResult", type=StringType)
ImperativeOCL_VariableInitExp.attributes={ImperativeOCL_VariableInitExp_withResult}

# ImperativeOCL_WhileExp class attributes and methods

# Relationships
body0: BinaryAssociation = BinaryAssociation(
    name="body0",
    ends={
        Property(name="ImperativeOCL_AltExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="OclExpression", type=ImperativeOCL_AltExp, multiplicity=Multiplicity(1, 1))
    }
)
condition1: BinaryAssociation = BinaryAssociation(
    name="condition1",
    ends={
        Property(name="OclExpression3", type=ImperativeOCL_AltExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_AltExp2", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
assertion4: BinaryAssociation = BinaryAssociation(
    name="assertion4",
    ends={
        Property(name="OclExpression5", type=ImperativeOCL_AssertExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_AssertExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
log6: BinaryAssociation = BinaryAssociation(
    name="log6",
    ends={
        Property(name="LogExp", type=ImperativeOCL_AssertExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_AssertExp7", type=LogExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body18: BinaryAssociation = BinaryAssociation(
    name="body18",
    ends={
        Property(name="OclExpression19", type=ImperativeOCL_CatchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_CatchExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exception20: BinaryAssociation = BinaryAssociation(
    name="exception20",
    ends={
        Property(name="Type", type=ImperativeOCL_CatchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_CatchExp21", type=Type, multiplicity=Multiplicity(1, 9999))
    }
)
exceptionVariable22: BinaryAssociation = BinaryAssociation(
    name="exceptionVariable22",
    ends={
        Property(name="Variable", type=ImperativeOCL_CatchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_CatchExp23", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body24: BinaryAssociation = BinaryAssociation(
    name="body24",
    ends={
        Property(name="OclExpression25", type=ImperativeOCL_ComputeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_ComputeExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
defaultValue8: BinaryAssociation = BinaryAssociation(
    name="defaultValue8",
    ends={
        Property(name="OclExpression9", type=ImperativeOCL_AssignExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_AssignExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left10: BinaryAssociation = BinaryAssociation(
    name="left10",
    ends={
        Property(name="OclExpression12", type=ImperativeOCL_AssignExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_AssignExp11", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value13: BinaryAssociation = BinaryAssociation(
    name="value13",
    ends={
        Property(name="OclExpression15", type=ImperativeOCL_AssignExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_AssignExp14", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body16: BinaryAssociation = BinaryAssociation(
    name="body16",
    ends={
        Property(name="OclExpression17", type=ImperativeOCL_BlockExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_BlockExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyType37: BinaryAssociation = BinaryAssociation(
    name="keyType37",
    ends={
        Property(name="Type38", type=ImperativeOCL_DictionaryType, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_DictionaryType", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
target39: BinaryAssociation = BinaryAssociation(
    name="target39",
    ends={
        Property(name="Variable40", type=ImperativeOCL_ImperativeIterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_ImperativeIterateExp", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition41: BinaryAssociation = BinaryAssociation(
    name="condition41",
    ends={
        Property(name="OclExpression42", type=ImperativeOCL_ImperativeLoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_ImperativeLoopExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnedElement26: BinaryAssociation = BinaryAssociation(
    name="returnedElement26",
    ends={
        Property(name="Variable28", type=ImperativeOCL_ComputeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_ComputeExp27", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
part29: BinaryAssociation = BinaryAssociation(
    name="part29",
    ends={
        Property(name="DictLiteralPart", type=ImperativeOCL_DictLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="partOwner", type=DictLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key30: BinaryAssociation = BinaryAssociation(
    name="key30",
    ends={
        Property(name="OclExpression31", type=ImperativeOCL_DictLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_DictLiteralPart", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value32: BinaryAssociation = BinaryAssociation(
    name="value32",
    ends={
        Property(name="OclExpression34", type=ImperativeOCL_DictLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_DictLiteralPart33", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
partOwner35: BinaryAssociation = BinaryAssociation(
    name="partOwner35",
    ends={
        Property(name="DictLiteralExp", type=ImperativeOCL_DictLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_DictLiteralPart36", type=DictLiteralExp, multiplicity=Multiplicity(1, 1))
    }
)
condition54: BinaryAssociation = BinaryAssociation(
    name="condition54",
    ends={
        Property(name="OclExpression55", type=ImperativeOCL_LogExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_LogExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
argument56: BinaryAssociation = BinaryAssociation(
    name="argument56",
    ends={
        Property(name="OclExpression57", type=ImperativeOCL_RaiseExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_RaiseExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exception58: BinaryAssociation = BinaryAssociation(
    name="exception58",
    ends={
        Property(name="Type60", type=ImperativeOCL_RaiseExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_RaiseExp59", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
argument43: BinaryAssociation = BinaryAssociation(
    name="argument43",
    ends={
        Property(name="OclExpression44", type=ImperativeOCL_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_InstantiationExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extent45: BinaryAssociation = BinaryAssociation(
    name="extent45",
    ends={
        Property(name="Variable47", type=ImperativeOCL_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_InstantiationExp46", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
instantiatedClass48: BinaryAssociation = BinaryAssociation(
    name="instantiatedClass48",
    ends={
        Property(name="Class", type=ImperativeOCL_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_InstantiationExp49", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
initializationOperation50: BinaryAssociation = BinaryAssociation(
    name="initializationOperation50",
    ends={
        Property(name="Operation", type=ImperativeOCL_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_InstantiationExp51", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
element52: BinaryAssociation = BinaryAssociation(
    name="element52",
    ends={
        Property(name="OclExpression53", type=ImperativeOCL_ListLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_ListLiteralExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tryBody68: BinaryAssociation = BinaryAssociation(
    name="tryBody68",
    ends={
        Property(name="OclExpression70", type=ImperativeOCL_TryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_TryExp69", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
base71: BinaryAssociation = BinaryAssociation(
    name="base71",
    ends={
        Property(name="Type72", type=ImperativeOCL_Typedef, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_Typedef", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
condition73: BinaryAssociation = BinaryAssociation(
    name="condition73",
    ends={
        Property(name="OclExpression75", type=ImperativeOCL_Typedef, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_Typedef74", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
item76: BinaryAssociation = BinaryAssociation(
    name="item76",
    ends={
        Property(name="OclExpression77", type=ImperativeOCL_UnlinkExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_UnlinkExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value61: BinaryAssociation = BinaryAssociation(
    name="value61",
    ends={
        Property(name="OclExpression62", type=ImperativeOCL_ReturnExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_ReturnExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target78: BinaryAssociation = BinaryAssociation(
    name="target78",
    ends={
        Property(name="OclExpression80", type=ImperativeOCL_UnlinkExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_UnlinkExp79", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
alternativePart63: BinaryAssociation = BinaryAssociation(
    name="alternativePart63",
    ends={
        Property(name="AltExp", type=ImperativeOCL_SwitchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_SwitchExp", type=AltExp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elsePart64: BinaryAssociation = BinaryAssociation(
    name="elsePart64",
    ends={
        Property(name="OclExpression66", type=ImperativeOCL_SwitchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_SwitchExp65", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exceptClause67: BinaryAssociation = BinaryAssociation(
    name="exceptClause67",
    ends={
        Property(name="CatchExp", type=ImperativeOCL_TryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_TryExp", type=CatchExp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredVariable81: BinaryAssociation = BinaryAssociation(
    name="referredVariable81",
    ends={
        Property(name="Variable82", type=ImperativeOCL_VariableInitExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_VariableInitExp", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body83: BinaryAssociation = BinaryAssociation(
    name="body83",
    ends={
        Property(name="OclExpression84", type=ImperativeOCL_WhileExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_WhileExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition85: BinaryAssociation = BinaryAssociation(
    name="condition85",
    ends={
        Property(name="OclExpression87", type=ImperativeOCL_WhileExp, multiplicity=Multiplicity(1, 1)),
        Property(name="ImperativeOCL_WhileExp86", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_ImperativeOCL_AssertExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_AssertExp)
gen_ImperativeOCL_AltExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_AltExp)
gen_ImperativeOCL_ComputeExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_ComputeExp)
gen_ImperativeOCL_AssignExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_AssignExp)
gen_ImperativeOCL_BlockExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_BlockExp)
gen_ImperativeOCL_BreakExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_BreakExp)
gen_ImperativeOCL_CatchExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_CatchExp)
gen_ImperativeOCL_DictionaryType_CollectionType = Generalization(general=CollectionType, specific=ImperativeOCL_DictionaryType)
gen_ImperativeOCL_ForExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=ImperativeOCL_ForExp)
gen_ImperativeOCL_ImperativeExpression_OclExpression = Generalization(general=OclExpression, specific=ImperativeOCL_ImperativeExpression)
gen_ImperativeOCL_ImperativeIterateExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=ImperativeOCL_ImperativeIterateExp)
gen_ImperativeOCL_ImperativeLoopExp_LoopExp = Generalization(general=LoopExp, specific=ImperativeOCL_ImperativeLoopExp)
gen_ImperativeOCL_ImperativeLoopExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_ImperativeLoopExp)
gen_ImperativeOCL_ContinueExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_ContinueExp)
gen_ImperativeOCL_DictLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=ImperativeOCL_DictLiteralExp)
gen_ImperativeOCL_DictLiteralPart_Element = Generalization(general=Element, specific=ImperativeOCL_DictLiteralPart)
gen_ImperativeOCL_ListType_CollectionType = Generalization(general=CollectionType, specific=ImperativeOCL_ListType)
gen_ImperativeOCL_LogExp_OperationCallExp = Generalization(general=OperationCallExp, specific=ImperativeOCL_LogExp)
gen_ImperativeOCL_LogExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_LogExp)
gen_ImperativeOCL_RaiseExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_RaiseExp)
gen_ImperativeOCL_InstantiationExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_InstantiationExp)
gen_ImperativeOCL_ListLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=ImperativeOCL_ListLiteralExp)
gen_ImperativeOCL_Typedef_Class = Generalization(general=Class_, specific=ImperativeOCL_Typedef)
gen_ImperativeOCL_UnlinkExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_UnlinkExp)
gen_ImperativeOCL_ReturnExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_ReturnExp)
gen_ImperativeOCL_SwitchExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_SwitchExp)
gen_ImperativeOCL_TryExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_TryExp)
gen_ImperativeOCL_VariableInitExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_VariableInitExp)
gen_ImperativeOCL_WhileExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=ImperativeOCL_WhileExp)

# Domain Model
domain_model = DomainModel(
    name="ImperativeOCL",
    types={ImperativeOCL_AssertExp, LogExp, ImperativeOCL_AltExp, ImperativeExpression, OclExpression, Type, Variable, ImperativeOCL_ComputeExp, ImperativeOCL_AssignExp, ImperativeOCL_BlockExp, ImperativeOCL_BreakExp, ImperativeOCL_CatchExp, CollectionType, ImperativeOCL_ForExp, ImperativeLoopExp, ImperativeOCL_ImperativeExpression, ImperativeOCL_ImperativeIterateExp, ImperativeOCL_ImperativeLoopExp, LoopExp, ImperativeOCL_ContinueExp, ImperativeOCL_DictLiteralExp, LiteralExp, DictLiteralPart, ImperativeOCL_DictLiteralPart, Element, DictLiteralExp, ImperativeOCL_DictionaryType, ImperativeOCL_LogExp, OperationCallExp, ImperativeOCL_RaiseExp, ImperativeOCL_ReturnExp, ImperativeOCL_InstantiationExp, Class_, Operation, ImperativeOCL_ListLiteralExp, ImperativeOCL_ListType, ImperativeOCL_Typedef, ImperativeOCL_UnlinkExp, ImperativeOCL_SwitchExp, AltExp, ImperativeOCL_TryExp, CatchExp, ImperativeOCL_VariableInitExp, ImperativeOCL_WhileExp, SeverityKind},
    associations={body0, condition1, assertion4, log6, body18, exception20, exceptionVariable22, body24, defaultValue8, left10, value13, body16, keyType37, target39, condition41, returnedElement26, part29, key30, value32, partOwner35, condition54, argument56, exception58, argument43, extent45, instantiatedClass48, initializationOperation50, element52, tryBody68, base71, condition73, item76, value61, target78, alternativePart63, elsePart64, exceptClause67, referredVariable81, body83, condition85},
    generalizations={gen_ImperativeOCL_AssertExp_ImperativeExpression, gen_ImperativeOCL_AltExp_ImperativeExpression, gen_ImperativeOCL_ComputeExp_ImperativeExpression, gen_ImperativeOCL_AssignExp_ImperativeExpression, gen_ImperativeOCL_BlockExp_ImperativeExpression, gen_ImperativeOCL_BreakExp_ImperativeExpression, gen_ImperativeOCL_CatchExp_ImperativeExpression, gen_ImperativeOCL_DictionaryType_CollectionType, gen_ImperativeOCL_ForExp_ImperativeLoopExp, gen_ImperativeOCL_ImperativeExpression_OclExpression, gen_ImperativeOCL_ImperativeIterateExp_ImperativeLoopExp, gen_ImperativeOCL_ImperativeLoopExp_LoopExp, gen_ImperativeOCL_ImperativeLoopExp_ImperativeExpression, gen_ImperativeOCL_ContinueExp_ImperativeExpression, gen_ImperativeOCL_DictLiteralExp_LiteralExp, gen_ImperativeOCL_DictLiteralPart_Element, gen_ImperativeOCL_ListType_CollectionType, gen_ImperativeOCL_LogExp_OperationCallExp, gen_ImperativeOCL_LogExp_ImperativeExpression, gen_ImperativeOCL_RaiseExp_ImperativeExpression, gen_ImperativeOCL_InstantiationExp_ImperativeExpression, gen_ImperativeOCL_ListLiteralExp_LiteralExp, gen_ImperativeOCL_Typedef_Class, gen_ImperativeOCL_UnlinkExp_ImperativeExpression, gen_ImperativeOCL_ReturnExp_ImperativeExpression, gen_ImperativeOCL_SwitchExp_ImperativeExpression, gen_ImperativeOCL_TryExp_ImperativeExpression, gen_ImperativeOCL_VariableInitExp_ImperativeExpression, gen_ImperativeOCL_WhileExp_ImperativeExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)