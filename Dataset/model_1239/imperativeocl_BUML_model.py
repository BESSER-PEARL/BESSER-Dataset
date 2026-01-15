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
imperativeocl_AssignExp = Class(name="imperativeocl::AssignExp")
ImperativeExpression = Class(name="ImperativeExpression")
imperativeocl_BlockExp = Class(name="imperativeocl::BlockExp")
imperativeocl_SwitchExp = Class(name="imperativeocl::SwitchExp")
CallExp = Class(name="CallExp")
imperativeocl_AltExp = Class(name="imperativeocl::AltExp")
imperativeocl_VariableInitExp = Class(name="imperativeocl::VariableInitExp")
imperativeocl_Variable = Class(name="imperativeocl::Variable")
imperativeocl_WhileExp = Class(name="imperativeocl::WhileExp")
imperativeocl_ComputeExp = Class(name="imperativeocl::ComputeExp")
imperativeocl_OclExpression = Class(name="imperativeocl::OclExpression")
imperativeocl_UnlinkExp = Class(name="imperativeocl::UnlinkExp")
imperativeocl_ReturnExp = Class(name="imperativeocl::ReturnExp")
imperativeocl_BreakExp = Class(name="imperativeocl::BreakExp")
imperativeocl_TryExp = Class(name="imperativeocl::TryExp")
imperativeocl_CatchExp = Class(name="imperativeocl::CatchExp")
imperativeocl_RaiseExp = Class(name="imperativeocl::RaiseExp")
imperativeocl_Type = Class(name="imperativeocl::Type")
imperativeocl_ContinueExp = Class(name="imperativeocl::ContinueExp")
imperativeocl_ForExp = Class(name="imperativeocl::ForExp")
ImperativeLoopExp = Class(name="ImperativeLoopExp")
imperativeocl_Typedef = Class(name="imperativeocl::Typedef")
Class_ = Class(name="Class")
imperativeocl_InstantiationExp = Class(name="imperativeocl::InstantiationExp")
imperativeocl_Class = Class(name="imperativeocl::Class")
imperativeocl_DictionaryType = Class(name="imperativeocl::DictionaryType")
CollectionType = Class(name="CollectionType")
imperativeocl_DictLiteralExp = Class(name="imperativeocl::DictLiteralExp")
LiteralExp = Class(name="LiteralExp")
imperativeocl_DictLiteralPart = Class(name="imperativeocl::DictLiteralPart")
Element = Class(name="Element")
imperativeocl_TemplateParameterType = Class(name="imperativeocl::TemplateParameterType")
Type = Class(name="Type")
imperativeocl_LogExp = Class(name="imperativeocl::LogExp")
OperationCallExp = Class(name="OperationCallExp")
imperativeocl_AssertExp = Class(name="imperativeocl::AssertExp")
imperativeocl_ImperativeLoopExp = Class(name="imperativeocl::ImperativeLoopExp", is_abstract=True)
LoopExp = Class(name="LoopExp")
imperativeocl_ImperativeIterateExp = Class(name="imperativeocl::ImperativeIterateExp")
imperativeocl_ImperativeExpression = Class(name="imperativeocl::ImperativeExpression", is_abstract=True)
OclExpression = Class(name="OclExpression")
imperativeocl_UnpackExp = Class(name="imperativeocl::UnpackExp")
imperativeocl_OrderedTupleType = Class(name="imperativeocl::OrderedTupleType")
imperativeocl_OrderedTupleLiteralExp = Class(name="imperativeocl::OrderedTupleLiteralExp")
imperativeocl_OrderedTupleLiteralPart = Class(name="imperativeocl::OrderedTupleLiteralPart")
imperativeocl_ListType = Class(name="imperativeocl::ListType")

# imperativeocl_AssignExp class attributes and methods
imperativeocl_AssignExp_isReset: Property = Property(name="isReset", type=StringType)
imperativeocl_AssignExp.attributes={imperativeocl_AssignExp_isReset}

# ImperativeExpression class attributes and methods

# imperativeocl_BlockExp class attributes and methods

# imperativeocl_SwitchExp class attributes and methods

# CallExp class attributes and methods

# imperativeocl_AltExp class attributes and methods

# imperativeocl_VariableInitExp class attributes and methods
imperativeocl_VariableInitExp_withResult: Property = Property(name="withResult", type=StringType)
imperativeocl_VariableInitExp.attributes={imperativeocl_VariableInitExp_withResult}

# imperativeocl_Variable class attributes and methods

# imperativeocl_WhileExp class attributes and methods

# imperativeocl_ComputeExp class attributes and methods

# imperativeocl_OclExpression class attributes and methods

# imperativeocl_UnlinkExp class attributes and methods

# imperativeocl_ReturnExp class attributes and methods

# imperativeocl_BreakExp class attributes and methods

# imperativeocl_TryExp class attributes and methods

# imperativeocl_CatchExp class attributes and methods

# imperativeocl_RaiseExp class attributes and methods

# imperativeocl_Type class attributes and methods

# imperativeocl_ContinueExp class attributes and methods

# imperativeocl_ForExp class attributes and methods

# ImperativeLoopExp class attributes and methods

# imperativeocl_Typedef class attributes and methods

# Class class attributes and methods

# imperativeocl_InstantiationExp class attributes and methods

# imperativeocl_Class class attributes and methods

# imperativeocl_DictionaryType class attributes and methods

# CollectionType class attributes and methods

# imperativeocl_DictLiteralExp class attributes and methods

# LiteralExp class attributes and methods

# imperativeocl_DictLiteralPart class attributes and methods

# Element class attributes and methods

# imperativeocl_TemplateParameterType class attributes and methods
imperativeocl_TemplateParameterType_specification: Property = Property(name="specification", type=StringType)
imperativeocl_TemplateParameterType.attributes={imperativeocl_TemplateParameterType_specification}

# Type class attributes and methods

# imperativeocl_LogExp class attributes and methods

# OperationCallExp class attributes and methods

# imperativeocl_AssertExp class attributes and methods
imperativeocl_AssertExp_severity: Property = Property(name="severity", type=StringType)
imperativeocl_AssertExp.attributes={imperativeocl_AssertExp_severity}

# imperativeocl_ImperativeLoopExp class attributes and methods

# LoopExp class attributes and methods

# imperativeocl_ImperativeIterateExp class attributes and methods

# imperativeocl_ImperativeExpression class attributes and methods

# OclExpression class attributes and methods

# imperativeocl_UnpackExp class attributes and methods

# imperativeocl_OrderedTupleType class attributes and methods

# imperativeocl_OrderedTupleLiteralExp class attributes and methods

# imperativeocl_OrderedTupleLiteralPart class attributes and methods

# imperativeocl_ListType class attributes and methods

# Relationships
left1: BinaryAssociation = BinaryAssociation(
    name="left1",
    ends={
        Property(name="imperativeocl_OclExpression3", type=imperativeocl_AssignExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_AssignExp2", type=imperativeocl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
defaultValue4: BinaryAssociation = BinaryAssociation(
    name="defaultValue4",
    ends={
        Property(name="imperativeocl_OclExpression6", type=imperativeocl_AssignExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_AssignExp5", type=imperativeocl_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body7: BinaryAssociation = BinaryAssociation(
    name="body7",
    ends={
        Property(name="imperativeocl_OclExpression8", type=imperativeocl_BlockExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_BlockExp", type=imperativeocl_OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
alternativePart9: BinaryAssociation = BinaryAssociation(
    name="alternativePart9",
    ends={
        Property(name="imperativeocl_AltExp", type=imperativeocl_SwitchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_SwitchExp", type=imperativeocl_AltExp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elsePart10: BinaryAssociation = BinaryAssociation(
    name="elsePart10",
    ends={
        Property(name="imperativeocl_OclExpression12", type=imperativeocl_SwitchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_SwitchExp11", type=imperativeocl_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referredVariable13: BinaryAssociation = BinaryAssociation(
    name="referredVariable13",
    ends={
        Property(name="imperativeocl_Variable", type=imperativeocl_VariableInitExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_VariableInitExp", type=imperativeocl_Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition14: BinaryAssociation = BinaryAssociation(
    name="condition14",
    ends={
        Property(name="imperativeocl_OclExpression15", type=imperativeocl_WhileExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_WhileExp", type=imperativeocl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body16: BinaryAssociation = BinaryAssociation(
    name="body16",
    ends={
        Property(name="imperativeocl_OclExpression18", type=imperativeocl_WhileExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_WhileExp17", type=imperativeocl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnedElement19: BinaryAssociation = BinaryAssociation(
    name="returnedElement19",
    ends={
        Property(name="imperativeocl_Variable20", type=imperativeocl_ComputeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_ComputeExp", type=imperativeocl_Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value0: BinaryAssociation = BinaryAssociation(
    name="value0",
    ends={
        Property(name="imperativeocl_OclExpression", type=imperativeocl_AssignExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_AssignExp", type=imperativeocl_OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition24: BinaryAssociation = BinaryAssociation(
    name="condition24",
    ends={
        Property(name="imperativeocl_OclExpression26", type=imperativeocl_AltExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_AltExp25", type=imperativeocl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body27: BinaryAssociation = BinaryAssociation(
    name="body27",
    ends={
        Property(name="imperativeocl_OclExpression29", type=imperativeocl_AltExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_AltExp28", type=imperativeocl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target30: BinaryAssociation = BinaryAssociation(
    name="target30",
    ends={
        Property(name="imperativeocl_OclExpression31", type=imperativeocl_UnlinkExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_UnlinkExp", type=imperativeocl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
item32: BinaryAssociation = BinaryAssociation(
    name="item32",
    ends={
        Property(name="imperativeocl_OclExpression34", type=imperativeocl_UnlinkExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_UnlinkExp33", type=imperativeocl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value35: BinaryAssociation = BinaryAssociation(
    name="value35",
    ends={
        Property(name="imperativeocl_OclExpression36", type=imperativeocl_ReturnExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_ReturnExp", type=imperativeocl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tryBody37: BinaryAssociation = BinaryAssociation(
    name="tryBody37",
    ends={
        Property(name="imperativeocl_OclExpression38", type=imperativeocl_TryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_TryExp", type=imperativeocl_OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
catchClause39: BinaryAssociation = BinaryAssociation(
    name="catchClause39",
    ends={
        Property(name="imperativeocl_CatchExp", type=imperativeocl_TryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_TryExp40", type=imperativeocl_CatchExp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exception41: BinaryAssociation = BinaryAssociation(
    name="exception41",
    ends={
        Property(name="imperativeocl_Type", type=imperativeocl_RaiseExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_RaiseExp", type=imperativeocl_Type, multiplicity=Multiplicity(1, 1))
    }
)
argument42: BinaryAssociation = BinaryAssociation(
    name="argument42",
    ends={
        Property(name="imperativeocl_OclExpression44", type=imperativeocl_RaiseExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_RaiseExp43", type=imperativeocl_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body21: BinaryAssociation = BinaryAssociation(
    name="body21",
    ends={
        Property(name="imperativeocl_OclExpression23", type=imperativeocl_ComputeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_ComputeExp22", type=imperativeocl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
instantiatedClass50: BinaryAssociation = BinaryAssociation(
    name="instantiatedClass50",
    ends={
        Property(name="imperativeocl_Class", type=imperativeocl_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_InstantiationExp", type=imperativeocl_Class, multiplicity=Multiplicity(1, 1))
    }
)
extent51: BinaryAssociation = BinaryAssociation(
    name="extent51",
    ends={
        Property(name="imperativeocl_Variable53", type=imperativeocl_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_InstantiationExp52", type=imperativeocl_Variable, multiplicity=Multiplicity(0, 1))
    }
)
argument54: BinaryAssociation = BinaryAssociation(
    name="argument54",
    ends={
        Property(name="imperativeocl_OclExpression56", type=imperativeocl_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_InstantiationExp55", type=imperativeocl_OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyType57: BinaryAssociation = BinaryAssociation(
    name="keyType57",
    ends={
        Property(name="imperativeocl_Type58", type=imperativeocl_DictionaryType, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_DictionaryType", type=imperativeocl_Type, multiplicity=Multiplicity(0, 1))
    }
)
part59: BinaryAssociation = BinaryAssociation(
    name="part59",
    ends={
        Property(name="imperativeocl_DictLiteralPart", type=imperativeocl_DictLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_DictLiteralExp", type=imperativeocl_DictLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key60: BinaryAssociation = BinaryAssociation(
    name="key60",
    ends={
        Property(name="imperativeocl_OclExpression62", type=imperativeocl_DictLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_DictLiteralPart61", type=imperativeocl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value63: BinaryAssociation = BinaryAssociation(
    name="value63",
    ends={
        Property(name="imperativeocl_OclExpression65", type=imperativeocl_DictLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_DictLiteralPart64", type=imperativeocl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition66: BinaryAssociation = BinaryAssociation(
    name="condition66",
    ends={
        Property(name="imperativeocl_OclExpression67", type=imperativeocl_LogExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_LogExp", type=imperativeocl_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
log68: BinaryAssociation = BinaryAssociation(
    name="log68",
    ends={
        Property(name="imperativeocl_LogExp69", type=imperativeocl_AssertExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_AssertExp", type=imperativeocl_LogExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base45: BinaryAssociation = BinaryAssociation(
    name="base45",
    ends={
        Property(name="imperativeocl_Type46", type=imperativeocl_Typedef, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_Typedef", type=imperativeocl_Type, multiplicity=Multiplicity(1, 1))
    }
)
condition47: BinaryAssociation = BinaryAssociation(
    name="condition47",
    ends={
        Property(name="imperativeocl_OclExpression49", type=imperativeocl_Typedef, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_Typedef48", type=imperativeocl_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition73: BinaryAssociation = BinaryAssociation(
    name="condition73",
    ends={
        Property(name="imperativeocl_OclExpression74", type=imperativeocl_ImperativeLoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_ImperativeLoopExp", type=imperativeocl_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target75: BinaryAssociation = BinaryAssociation(
    name="target75",
    ends={
        Property(name="imperativeocl_Variable76", type=imperativeocl_ImperativeIterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_ImperativeIterateExp", type=imperativeocl_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetVariable77: BinaryAssociation = BinaryAssociation(
    name="targetVariable77",
    ends={
        Property(name="imperativeocl_Variable78", type=imperativeocl_UnpackExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_UnpackExp", type=imperativeocl_Variable, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
source79: BinaryAssociation = BinaryAssociation(
    name="source79",
    ends={
        Property(name="imperativeocl_OclExpression81", type=imperativeocl_UnpackExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_UnpackExp80", type=imperativeocl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementType82: BinaryAssociation = BinaryAssociation(
    name="elementType82",
    ends={
        Property(name="imperativeocl_Type83", type=imperativeocl_OrderedTupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_OrderedTupleType", type=imperativeocl_Type, multiplicity=Multiplicity(0, 9999))
    }
)
part84: BinaryAssociation = BinaryAssociation(
    name="part84",
    ends={
        Property(name="imperativeocl_OrderedTupleLiteralPart", type=imperativeocl_OrderedTupleLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_OrderedTupleLiteralExp", type=imperativeocl_OrderedTupleLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value85: BinaryAssociation = BinaryAssociation(
    name="value85",
    ends={
        Property(name="imperativeocl_OclExpression87", type=imperativeocl_OrderedTupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_OrderedTupleLiteralPart86", type=imperativeocl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
assertion70: BinaryAssociation = BinaryAssociation(
    name="assertion70",
    ends={
        Property(name="imperativeocl_OclExpression72", type=imperativeocl_AssertExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_AssertExp71", type=imperativeocl_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exception91: BinaryAssociation = BinaryAssociation(
    name="exception91",
    ends={
        Property(name="imperativeocl_Type93", type=imperativeocl_CatchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_CatchExp92", type=imperativeocl_Type, multiplicity=Multiplicity(0, 9999))
    }
)
body88: BinaryAssociation = BinaryAssociation(
    name="body88",
    ends={
        Property(name="imperativeocl_OclExpression90", type=imperativeocl_CatchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_CatchExp89", type=imperativeocl_OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_imperativeocl_AssignExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_AssignExp)
gen_imperativeocl_BlockExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_BlockExp)
gen_imperativeocl_SwitchExp_CallExp = Generalization(general=CallExp, specific=imperativeocl_SwitchExp)
gen_imperativeocl_SwitchExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_SwitchExp)
gen_imperativeocl_VariableInitExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_VariableInitExp)
gen_imperativeocl_WhileExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_WhileExp)
gen_imperativeocl_ComputeExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_ComputeExp)
gen_imperativeocl_UnlinkExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_UnlinkExp)
gen_imperativeocl_ReturnExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_ReturnExp)
gen_imperativeocl_BreakExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_BreakExp)
gen_imperativeocl_TryExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_TryExp)
gen_imperativeocl_RaiseExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_RaiseExp)
gen_imperativeocl_ContinueExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_ContinueExp)
gen_imperativeocl_ForExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=imperativeocl_ForExp)
gen_imperativeocl_Typedef_Class = Generalization(general=Class_, specific=imperativeocl_Typedef)
gen_imperativeocl_AltExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_AltExp)
gen_imperativeocl_InstantiationExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_InstantiationExp)
gen_imperativeocl_DictionaryType_CollectionType = Generalization(general=CollectionType, specific=imperativeocl_DictionaryType)
gen_imperativeocl_DictLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=imperativeocl_DictLiteralExp)
gen_imperativeocl_DictLiteralPart_Element = Generalization(general=Element, specific=imperativeocl_DictLiteralPart)
gen_imperativeocl_TemplateParameterType_Type = Generalization(general=Type, specific=imperativeocl_TemplateParameterType)
gen_imperativeocl_LogExp_OperationCallExp = Generalization(general=OperationCallExp, specific=imperativeocl_LogExp)
gen_imperativeocl_LogExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_LogExp)
gen_imperativeocl_AssertExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_AssertExp)
gen_imperativeocl_ImperativeLoopExp_LoopExp = Generalization(general=LoopExp, specific=imperativeocl_ImperativeLoopExp)
gen_imperativeocl_ImperativeLoopExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_ImperativeLoopExp)
gen_imperativeocl_ImperativeIterateExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=imperativeocl_ImperativeIterateExp)
gen_imperativeocl_ImperativeExpression_OclExpression = Generalization(general=OclExpression, specific=imperativeocl_ImperativeExpression)
gen_imperativeocl_UnpackExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_UnpackExp)
gen_imperativeocl_OrderedTupleType_Class = Generalization(general=Class_, specific=imperativeocl_OrderedTupleType)
gen_imperativeocl_OrderedTupleLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=imperativeocl_OrderedTupleLiteralExp)
gen_imperativeocl_OrderedTupleLiteralPart_Element = Generalization(general=Element, specific=imperativeocl_OrderedTupleLiteralPart)
gen_imperativeocl_ListType_CollectionType = Generalization(general=CollectionType, specific=imperativeocl_ListType)
gen_imperativeocl_CatchExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_CatchExp)

# Domain Model
domain_model = DomainModel(
    name="imperativeocl",
    types={imperativeocl_AssignExp, ImperativeExpression, imperativeocl_BlockExp, imperativeocl_SwitchExp, CallExp, imperativeocl_AltExp, imperativeocl_VariableInitExp, imperativeocl_Variable, imperativeocl_WhileExp, imperativeocl_ComputeExp, imperativeocl_OclExpression, imperativeocl_UnlinkExp, imperativeocl_ReturnExp, imperativeocl_BreakExp, imperativeocl_TryExp, imperativeocl_CatchExp, imperativeocl_RaiseExp, imperativeocl_Type, imperativeocl_ContinueExp, imperativeocl_ForExp, ImperativeLoopExp, imperativeocl_Typedef, Class_, imperativeocl_InstantiationExp, imperativeocl_Class, imperativeocl_DictionaryType, CollectionType, imperativeocl_DictLiteralExp, LiteralExp, imperativeocl_DictLiteralPart, Element, imperativeocl_TemplateParameterType, Type, imperativeocl_LogExp, OperationCallExp, imperativeocl_AssertExp, imperativeocl_ImperativeLoopExp, LoopExp, imperativeocl_ImperativeIterateExp, imperativeocl_ImperativeExpression, OclExpression, imperativeocl_UnpackExp, imperativeocl_OrderedTupleType, imperativeocl_OrderedTupleLiteralExp, imperativeocl_OrderedTupleLiteralPart, imperativeocl_ListType, SeverityKind},
    associations={left1, defaultValue4, body7, alternativePart9, elsePart10, referredVariable13, condition14, body16, returnedElement19, value0, condition24, body27, target30, item32, value35, tryBody37, catchClause39, exception41, argument42, body21, instantiatedClass50, extent51, argument54, keyType57, part59, key60, value63, condition66, log68, base45, condition47, condition73, target75, targetVariable77, source79, elementType82, part84, value85, assertion70, exception91, body88},
    generalizations={gen_imperativeocl_AssignExp_ImperativeExpression, gen_imperativeocl_BlockExp_ImperativeExpression, gen_imperativeocl_SwitchExp_CallExp, gen_imperativeocl_SwitchExp_ImperativeExpression, gen_imperativeocl_VariableInitExp_ImperativeExpression, gen_imperativeocl_WhileExp_ImperativeExpression, gen_imperativeocl_ComputeExp_ImperativeExpression, gen_imperativeocl_UnlinkExp_ImperativeExpression, gen_imperativeocl_ReturnExp_ImperativeExpression, gen_imperativeocl_BreakExp_ImperativeExpression, gen_imperativeocl_TryExp_ImperativeExpression, gen_imperativeocl_RaiseExp_ImperativeExpression, gen_imperativeocl_ContinueExp_ImperativeExpression, gen_imperativeocl_ForExp_ImperativeLoopExp, gen_imperativeocl_Typedef_Class, gen_imperativeocl_AltExp_ImperativeExpression, gen_imperativeocl_InstantiationExp_ImperativeExpression, gen_imperativeocl_DictionaryType_CollectionType, gen_imperativeocl_DictLiteralExp_LiteralExp, gen_imperativeocl_DictLiteralPart_Element, gen_imperativeocl_TemplateParameterType_Type, gen_imperativeocl_LogExp_OperationCallExp, gen_imperativeocl_LogExp_ImperativeExpression, gen_imperativeocl_AssertExp_ImperativeExpression, gen_imperativeocl_ImperativeLoopExp_LoopExp, gen_imperativeocl_ImperativeLoopExp_ImperativeExpression, gen_imperativeocl_ImperativeIterateExp_ImperativeLoopExp, gen_imperativeocl_ImperativeExpression_OclExpression, gen_imperativeocl_UnpackExp_ImperativeExpression, gen_imperativeocl_OrderedTupleType_Class, gen_imperativeocl_OrderedTupleLiteralExp_LiteralExp, gen_imperativeocl_OrderedTupleLiteralPart_Element, gen_imperativeocl_ListType_CollectionType, gen_imperativeocl_CatchExp_ImperativeExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)