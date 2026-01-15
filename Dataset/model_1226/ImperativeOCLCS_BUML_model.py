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

# Classes
imperativeoclcs_AssignStatementCS = Class(name="imperativeoclcs::AssignStatementCS")
imperativeoclcs_AssertExpCS = Class(name="imperativeoclcs::AssertExpCS")
StatementCS = Class(name="StatementCS")
imperativeoclcs_ExpCS = Class(name="imperativeoclcs::ExpCS")
imperativeoclcs_LogExpCS = Class(name="imperativeoclcs::LogExpCS")
imperativeoclcs_InstantiationExpCS = Class(name="imperativeoclcs::InstantiationExpCS")
imperativeoclcs_BlockExpCS = Class(name="imperativeoclcs::BlockExpCS")
imperativeoclcs_DictLiteralExpCS = Class(name="imperativeoclcs::DictLiteralExpCS")
ExpCS = Class(name="ExpCS")
imperativeoclcs_DictLiteralPartCS = Class(name="imperativeoclcs::DictLiteralPartCS")
ElementCS = Class(name="ElementCS")
imperativeoclcs_PrimitiveLiteralExpCS = Class(name="imperativeoclcs::PrimitiveLiteralExpCS")
imperativeoclcs_DictTypeCS = Class(name="imperativeoclcs::DictTypeCS")
TypedRefCS = Class(name="TypedRefCS")
imperativeoclcs_TypedRefCS = Class(name="imperativeoclcs::TypedRefCS")
imperativeoclcs_ComputeExpCS = Class(name="imperativeoclcs::ComputeExpCS")
ExpressionBlockCS = Class(name="ExpressionBlockCS")
imperativeoclcs_VariableCS = Class(name="imperativeoclcs::VariableCS")
imperativeoclcs_ImperativeIterateExpCS = Class(name="imperativeoclcs::ImperativeIterateExpCS")
ImperativeLoopExpCS = Class(name="ImperativeLoopExpCS")
imperativeoclcs_ImperativeLoopExpCS = Class(name="imperativeoclcs::ImperativeLoopExpCS")
CallExpCS = Class(name="CallExpCS")
imperativeoclcs_TypeCS = Class(name="imperativeoclcs::TypeCS")
imperativeoclcs_DoExpCS = Class(name="imperativeoclcs::DoExpCS")
imperativeoclcs_ExceptCS = Class(name="imperativeoclcs::ExceptCS")
imperativeoclcs_Type = Class(name="imperativeoclcs::Type")
imperativeoclcs_ExpressionBlockCS = Class(name="imperativeoclcs::ExpressionBlockCS")
imperativeoclcs_ExpressionStatementCS = Class(name="imperativeoclcs::ExpressionStatementCS")
imperativeoclcs_ForExpCS = Class(name="imperativeoclcs::ForExpCS")
imperativeoclcs_ListTypeCS = Class(name="imperativeoclcs::ListTypeCS")
imperativeoclcs_ListLiteralExpCS = Class(name="imperativeoclcs::ListLiteralExpCS")
imperativeoclcs_CollectionLiteralPartCS = Class(name="imperativeoclcs::CollectionLiteralPartCS")
imperativeoclcs_QuitExpCS = Class(name="imperativeoclcs::QuitExpCS")
imperativeoclcs_RaiseExpCS = Class(name="imperativeoclcs::RaiseExpCS")
imperativeoclcs_ReturnExpCS = Class(name="imperativeoclcs::ReturnExpCS")
imperativeoclcs_StatementCS = Class(name="imperativeoclcs::StatementCS", is_abstract=True)
imperativeoclcs_SwitchAltCS = Class(name="imperativeoclcs::SwitchAltCS")
imperativeoclcs_SwitchExpCS = Class(name="imperativeoclcs::SwitchExpCS")
imperativeoclcs_TryExpCS = Class(name="imperativeoclcs::TryExpCS")
imperativeoclcs_VariableInitializationCS = Class(name="imperativeoclcs::VariableInitializationCS")
imperativeoclcs_WhileExpCS = Class(name="imperativeoclcs::WhileExpCS")

# imperativeoclcs_AssignStatementCS class attributes and methods
imperativeoclcs_AssignStatementCS_incremental: Property = Property(name="incremental", type=BooleanType)
imperativeoclcs_AssignStatementCS.attributes={imperativeoclcs_AssignStatementCS_incremental}

# imperativeoclcs_AssertExpCS class attributes and methods
imperativeoclcs_AssertExpCS_severity: Property = Property(name="severity", type=StringType)
imperativeoclcs_AssertExpCS.attributes={imperativeoclcs_AssertExpCS_severity}

# StatementCS class attributes and methods

# imperativeoclcs_ExpCS class attributes and methods

# imperativeoclcs_LogExpCS class attributes and methods

# imperativeoclcs_InstantiationExpCS class attributes and methods

# imperativeoclcs_BlockExpCS class attributes and methods

# imperativeoclcs_DictLiteralExpCS class attributes and methods

# ExpCS class attributes and methods

# imperativeoclcs_DictLiteralPartCS class attributes and methods

# ElementCS class attributes and methods

# imperativeoclcs_PrimitiveLiteralExpCS class attributes and methods

# imperativeoclcs_DictTypeCS class attributes and methods

# TypedRefCS class attributes and methods

# imperativeoclcs_TypedRefCS class attributes and methods

# imperativeoclcs_ComputeExpCS class attributes and methods

# ExpressionBlockCS class attributes and methods

# imperativeoclcs_VariableCS class attributes and methods

# imperativeoclcs_ImperativeIterateExpCS class attributes and methods

# ImperativeLoopExpCS class attributes and methods

# imperativeoclcs_ImperativeLoopExpCS class attributes and methods

# CallExpCS class attributes and methods

# imperativeoclcs_TypeCS class attributes and methods

# imperativeoclcs_DoExpCS class attributes and methods

# imperativeoclcs_ExceptCS class attributes and methods

# imperativeoclcs_Type class attributes and methods

# imperativeoclcs_ExpressionBlockCS class attributes and methods

# imperativeoclcs_ExpressionStatementCS class attributes and methods

# imperativeoclcs_ForExpCS class attributes and methods

# imperativeoclcs_ListTypeCS class attributes and methods

# imperativeoclcs_ListLiteralExpCS class attributes and methods

# imperativeoclcs_CollectionLiteralPartCS class attributes and methods

# imperativeoclcs_QuitExpCS class attributes and methods
imperativeoclcs_QuitExpCS_keyword: Property = Property(name="keyword", type=StringType)
imperativeoclcs_QuitExpCS.attributes={imperativeoclcs_QuitExpCS_keyword}

# imperativeoclcs_RaiseExpCS class attributes and methods

# imperativeoclcs_ReturnExpCS class attributes and methods

# imperativeoclcs_StatementCS class attributes and methods

# imperativeoclcs_SwitchAltCS class attributes and methods
imperativeoclcs_SwitchAltCS_keyword: Property = Property(name="keyword", type=StringType)
imperativeoclcs_SwitchAltCS.attributes={imperativeoclcs_SwitchAltCS_keyword}

# imperativeoclcs_SwitchExpCS class attributes and methods

# imperativeoclcs_TryExpCS class attributes and methods

# imperativeoclcs_VariableInitializationCS class attributes and methods
imperativeoclcs_VariableInitializationCS_simpleNameCS: Property = Property(name="simpleNameCS", type=StringType)
imperativeoclcs_VariableInitializationCS_withResult: Property = Property(name="withResult", type=BooleanType)
imperativeoclcs_VariableInitializationCS.attributes={imperativeoclcs_VariableInitializationCS_withResult, imperativeoclcs_VariableInitializationCS_simpleNameCS}

# imperativeoclcs_WhileExpCS class attributes and methods

# Relationships
assertion0: BinaryAssociation = BinaryAssociation(
    name="assertion0",
    ends={
        Property(name="imperativeoclcs_ExpCS", type=imperativeoclcs_AssertExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeoclcs_AssertExpCS", type=imperativeoclcs_ExpCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
log1: BinaryAssociation = BinaryAssociation(
    name="log1",
    ends={
        Property(name="imperativeoclcs_LogExpCS", type=imperativeoclcs_AssertExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeoclcs_AssertExpCS2", type=imperativeoclcs_LogExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lValueCS3: BinaryAssociation = BinaryAssociation(
    name="lValueCS3",
    ends={
        Property(name="imperativeoclcs_ExpCS4", type=imperativeoclcs_AssignStatementCS, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeoclcs_AssignStatementCS", type=imperativeoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
oclExpressionCS5: BinaryAssociation = BinaryAssociation(
    name="oclExpressionCS5",
    ends={
        Property(name="imperativeoclcs_ExpCS7", type=imperativeoclcs_AssignStatementCS, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeoclcs_AssignStatementCS6", type=imperativeoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions8: BinaryAssociation = BinaryAssociation(
    name="expressions8",
    ends={
        Property(name="imperativeoclcs_ExpCS9", type=imperativeoclcs_BlockExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeoclcs_BlockExpCS", type=imperativeoclcs_ExpCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedParts10: BinaryAssociation = BinaryAssociation(
    name="ownedParts10",
    ends={
        Property(name="imperativeoclcs_DictLiteralPartCS", type=imperativeoclcs_DictLiteralExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeoclcs_DictLiteralExpCS", type=imperativeoclcs_DictLiteralPartCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key11: BinaryAssociation = BinaryAssociation(
    name="key11",
    ends={
        Property(name="imperativeoclcs_PrimitiveLiteralExpCS", type=imperativeoclcs_DictLiteralPartCS, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeoclcs_DictLiteralPartCS12", type=imperativeoclcs_PrimitiveLiteralExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value13: BinaryAssociation = BinaryAssociation(
    name="value13",
    ends={
        Property(name="imperativeoclcs_ExpCS15", type=imperativeoclcs_DictLiteralPartCS, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeoclcs_DictLiteralPartCS14", type=imperativeoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
keyType16: BinaryAssociation = BinaryAssociation(
    name="keyType16",
    ends={
        Property(name="imperativeoclcs_TypedRefCS", type=imperativeoclcs_DictTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeoclcs_DictTypeCS", type=imperativeoclcs_TypedRefCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
valueType17: BinaryAssociation = BinaryAssociation(
    name="valueType17",
    ends={
        Property(name="imperativeoclcs_TypedRefCS19", type=imperativeoclcs_DictTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeoclcs_DictTypeCS18", type=imperativeoclcs_TypedRefCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnedElement20: BinaryAssociation = BinaryAssociation(
    name="returnedElement20",
    ends={
        Property(name="imperativeoclcs_VariableCS", type=imperativeoclcs_ComputeExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeoclcs_ComputeExpCS", type=imperativeoclcs_VariableCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target21: BinaryAssociation = BinaryAssociation(
    name="target21",
    ends={
        Property(name="imperativeoclcs_VariableCS22", type=imperativeoclcs_ImperativeIterateExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeoclcs_ImperativeIterateExpCS", type=imperativeoclcs_VariableCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition23: BinaryAssociation = BinaryAssociation(
    name="condition23",
    ends={
        Property(name="imperativeoclcs_ExpCS24", type=imperativeoclcs_ImperativeLoopExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeoclcs_ImperativeLoopExpCS", type=imperativeoclcs_ExpCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value45: BinaryAssociation = BinaryAssociation(
    name="value45",
    ends={
        Property(name="imperativeoclcs_ExpCS46", type=imperativeoclcs_QuitExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeoclcs_QuitExpCS", type=imperativeoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeSpecCS25: BinaryAssociation = BinaryAssociation(
    name="typeSpecCS25",
    ends={
        Property(name="imperativeoclcs_TypeCS", type=imperativeoclcs_InstantiationExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeoclcs_InstantiationExpCS", type=imperativeoclcs_TypeCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments26: BinaryAssociation = BinaryAssociation(
    name="arguments26",
    ends={
        Property(name="imperativeoclcs_ExpCS28", type=imperativeoclcs_InstantiationExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeoclcs_InstantiationExpCS27", type=imperativeoclcs_ExpCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition29: BinaryAssociation = BinaryAssociation(
    name="condition29",
    ends={
        Property(name="imperativeoclcs_ExpCS30", type=imperativeoclcs_DoExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeoclcs_DoExpCS", type=imperativeoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
except31: BinaryAssociation = BinaryAssociation(
    name="except31",
    ends={
        Property(name="imperativeoclcs_Type", type=imperativeoclcs_ExceptCS, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeoclcs_ExceptCS", type=imperativeoclcs_Type, multiplicity=Multiplicity(0, 9999))
    }
)
body32: BinaryAssociation = BinaryAssociation(
    name="body32",
    ends={
        Property(name="imperativeoclcs_ExpCS34", type=imperativeoclcs_ExceptCS, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeoclcs_ExceptCS33", type=imperativeoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body35: BinaryAssociation = BinaryAssociation(
    name="body35",
    ends={
        Property(name="imperativeoclcs_ExpCS36", type=imperativeoclcs_ExpressionBlockCS, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeoclcs_ExpressionBlockCS", type=imperativeoclcs_ExpCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
oclExpressionCS37: BinaryAssociation = BinaryAssociation(
    name="oclExpressionCS37",
    ends={
        Property(name="imperativeoclcs_ExpCS38", type=imperativeoclcs_ExpressionStatementCS, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeoclcs_ExpressionStatementCS", type=imperativeoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type39: BinaryAssociation = BinaryAssociation(
    name="type39",
    ends={
        Property(name="imperativeoclcs_TypedRefCS40", type=imperativeoclcs_ListTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeoclcs_ListTypeCS", type=imperativeoclcs_TypedRefCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedParts41: BinaryAssociation = BinaryAssociation(
    name="ownedParts41",
    ends={
        Property(name="imperativeoclcs_CollectionLiteralPartCS", type=imperativeoclcs_ListLiteralExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeoclcs_ListLiteralExpCS", type=imperativeoclcs_CollectionLiteralPartCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition42: BinaryAssociation = BinaryAssociation(
    name="condition42",
    ends={
        Property(name="imperativeoclcs_ExpCS44", type=imperativeoclcs_LogExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeoclcs_LogExpCS43", type=imperativeoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value47: BinaryAssociation = BinaryAssociation(
    name="value47",
    ends={
        Property(name="imperativeoclcs_ExpCS48", type=imperativeoclcs_ReturnExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeoclcs_ReturnExpCS", type=imperativeoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition49: BinaryAssociation = BinaryAssociation(
    name="condition49",
    ends={
        Property(name="imperativeoclcs_ExpCS50", type=imperativeoclcs_SwitchAltCS, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeoclcs_SwitchAltCS", type=imperativeoclcs_ExpCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body51: BinaryAssociation = BinaryAssociation(
    name="body51",
    ends={
        Property(name="imperativeoclcs_ExpCS53", type=imperativeoclcs_SwitchAltCS, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeoclcs_SwitchAltCS52", type=imperativeoclcs_ExpCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
alternativePart54: BinaryAssociation = BinaryAssociation(
    name="alternativePart54",
    ends={
        Property(name="imperativeoclcs_SwitchAltCS55", type=imperativeoclcs_SwitchExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeoclcs_SwitchExpCS", type=imperativeoclcs_SwitchAltCS, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elsePart56: BinaryAssociation = BinaryAssociation(
    name="elsePart56",
    ends={
        Property(name="imperativeoclcs_ExpCS58", type=imperativeoclcs_SwitchExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeoclcs_SwitchExpCS57", type=imperativeoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
catch59: BinaryAssociation = BinaryAssociation(
    name="catch59",
    ends={
        Property(name="imperativeoclcs_ExceptCS60", type=imperativeoclcs_TryExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeoclcs_TryExpCS", type=imperativeoclcs_ExceptCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
oclExpressionCS61: BinaryAssociation = BinaryAssociation(
    name="oclExpressionCS61",
    ends={
        Property(name="imperativeoclcs_ExpCS62", type=imperativeoclcs_VariableInitializationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeoclcs_VariableInitializationCS", type=imperativeoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeCS63: BinaryAssociation = BinaryAssociation(
    name="typeCS63",
    ends={
        Property(name="imperativeoclcs_TypeCS65", type=imperativeoclcs_VariableInitializationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeoclcs_VariableInitializationCS64", type=imperativeoclcs_TypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition66: BinaryAssociation = BinaryAssociation(
    name="condition66",
    ends={
        Property(name="imperativeoclcs_ExpCS67", type=imperativeoclcs_WhileExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeoclcs_WhileExpCS", type=imperativeoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resultVar68: BinaryAssociation = BinaryAssociation(
    name="resultVar68",
    ends={
        Property(name="imperativeoclcs_VariableCS70", type=imperativeoclcs_WhileExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeoclcs_WhileExpCS69", type=imperativeoclcs_VariableCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_imperativeoclcs_AssertExpCS_StatementCS = Generalization(general=StatementCS, specific=imperativeoclcs_AssertExpCS)
gen_imperativeoclcs_InstantiationExpCS_StatementCS = Generalization(general=StatementCS, specific=imperativeoclcs_InstantiationExpCS)
gen_imperativeoclcs_AssignStatementCS_StatementCS = Generalization(general=StatementCS, specific=imperativeoclcs_AssignStatementCS)
gen_imperativeoclcs_BlockExpCS_StatementCS = Generalization(general=StatementCS, specific=imperativeoclcs_BlockExpCS)
gen_imperativeoclcs_DictLiteralExpCS_ExpCS = Generalization(general=ExpCS, specific=imperativeoclcs_DictLiteralExpCS)
gen_imperativeoclcs_DictLiteralPartCS_ElementCS = Generalization(general=ElementCS, specific=imperativeoclcs_DictLiteralPartCS)
gen_imperativeoclcs_DictTypeCS_TypedRefCS = Generalization(general=TypedRefCS, specific=imperativeoclcs_DictTypeCS)
gen_imperativeoclcs_ComputeExpCS_ExpressionBlockCS = Generalization(general=ExpressionBlockCS, specific=imperativeoclcs_ComputeExpCS)
gen_imperativeoclcs_ImperativeIterateExpCS_ImperativeLoopExpCS = Generalization(general=ImperativeLoopExpCS, specific=imperativeoclcs_ImperativeIterateExpCS)
gen_imperativeoclcs_ImperativeLoopExpCS_CallExpCS = Generalization(general=CallExpCS, specific=imperativeoclcs_ImperativeLoopExpCS)
gen_imperativeoclcs_ImperativeLoopExpCS_StatementCS = Generalization(general=StatementCS, specific=imperativeoclcs_ImperativeLoopExpCS)
gen_imperativeoclcs_DoExpCS_ExpressionBlockCS = Generalization(general=ExpressionBlockCS, specific=imperativeoclcs_DoExpCS)
gen_imperativeoclcs_ExceptCS_ElementCS = Generalization(general=ElementCS, specific=imperativeoclcs_ExceptCS)
gen_imperativeoclcs_ExpressionBlockCS_ExpCS = Generalization(general=ExpCS, specific=imperativeoclcs_ExpressionBlockCS)
gen_imperativeoclcs_ExpressionStatementCS_StatementCS = Generalization(general=StatementCS, specific=imperativeoclcs_ExpressionStatementCS)
gen_imperativeoclcs_ForExpCS_ImperativeLoopExpCS = Generalization(general=ImperativeLoopExpCS, specific=imperativeoclcs_ForExpCS)
gen_imperativeoclcs_ListTypeCS_TypedRefCS = Generalization(general=TypedRefCS, specific=imperativeoclcs_ListTypeCS)
gen_imperativeoclcs_ListLiteralExpCS_ExpCS = Generalization(general=ExpCS, specific=imperativeoclcs_ListLiteralExpCS)
gen_imperativeoclcs_LogExpCS_CallExpCS = Generalization(general=CallExpCS, specific=imperativeoclcs_LogExpCS)
gen_imperativeoclcs_QuitExpCS_StatementCS = Generalization(general=StatementCS, specific=imperativeoclcs_QuitExpCS)
gen_imperativeoclcs_RaiseExpCS_StatementCS = Generalization(general=StatementCS, specific=imperativeoclcs_RaiseExpCS)
gen_imperativeoclcs_ReturnExpCS_ExpCS = Generalization(general=ExpCS, specific=imperativeoclcs_ReturnExpCS)
gen_imperativeoclcs_StatementCS_ExpCS = Generalization(general=ExpCS, specific=imperativeoclcs_StatementCS)
gen_imperativeoclcs_SwitchAltCS_StatementCS = Generalization(general=StatementCS, specific=imperativeoclcs_SwitchAltCS)
gen_imperativeoclcs_SwitchExpCS_StatementCS = Generalization(general=StatementCS, specific=imperativeoclcs_SwitchExpCS)
gen_imperativeoclcs_TryExpCS_ExpressionBlockCS = Generalization(general=ExpressionBlockCS, specific=imperativeoclcs_TryExpCS)
gen_imperativeoclcs_VariableInitializationCS_StatementCS = Generalization(general=StatementCS, specific=imperativeoclcs_VariableInitializationCS)
gen_imperativeoclcs_WhileExpCS_ExpressionBlockCS = Generalization(general=ExpressionBlockCS, specific=imperativeoclcs_WhileExpCS)

# Domain Model
domain_model = DomainModel(
    name="imperativeoclcs",
    types={imperativeoclcs_AssignStatementCS, imperativeoclcs_AssertExpCS, StatementCS, imperativeoclcs_ExpCS, imperativeoclcs_LogExpCS, imperativeoclcs_InstantiationExpCS, imperativeoclcs_BlockExpCS, imperativeoclcs_DictLiteralExpCS, ExpCS, imperativeoclcs_DictLiteralPartCS, ElementCS, imperativeoclcs_PrimitiveLiteralExpCS, imperativeoclcs_DictTypeCS, TypedRefCS, imperativeoclcs_TypedRefCS, imperativeoclcs_ComputeExpCS, ExpressionBlockCS, imperativeoclcs_VariableCS, imperativeoclcs_ImperativeIterateExpCS, ImperativeLoopExpCS, imperativeoclcs_ImperativeLoopExpCS, CallExpCS, imperativeoclcs_TypeCS, imperativeoclcs_DoExpCS, imperativeoclcs_ExceptCS, imperativeoclcs_Type, imperativeoclcs_ExpressionBlockCS, imperativeoclcs_ExpressionStatementCS, imperativeoclcs_ForExpCS, imperativeoclcs_ListTypeCS, imperativeoclcs_ListLiteralExpCS, imperativeoclcs_CollectionLiteralPartCS, imperativeoclcs_QuitExpCS, imperativeoclcs_RaiseExpCS, imperativeoclcs_ReturnExpCS, imperativeoclcs_StatementCS, imperativeoclcs_SwitchAltCS, imperativeoclcs_SwitchExpCS, imperativeoclcs_TryExpCS, imperativeoclcs_VariableInitializationCS, imperativeoclcs_WhileExpCS},
    associations={assertion0, log1, lValueCS3, oclExpressionCS5, expressions8, ownedParts10, key11, value13, keyType16, valueType17, returnedElement20, target21, condition23, value45, typeSpecCS25, arguments26, condition29, except31, body32, body35, oclExpressionCS37, type39, ownedParts41, condition42, value47, condition49, body51, alternativePart54, elsePart56, catch59, oclExpressionCS61, typeCS63, condition66, resultVar68},
    generalizations={gen_imperativeoclcs_AssertExpCS_StatementCS, gen_imperativeoclcs_InstantiationExpCS_StatementCS, gen_imperativeoclcs_AssignStatementCS_StatementCS, gen_imperativeoclcs_BlockExpCS_StatementCS, gen_imperativeoclcs_DictLiteralExpCS_ExpCS, gen_imperativeoclcs_DictLiteralPartCS_ElementCS, gen_imperativeoclcs_DictTypeCS_TypedRefCS, gen_imperativeoclcs_ComputeExpCS_ExpressionBlockCS, gen_imperativeoclcs_ImperativeIterateExpCS_ImperativeLoopExpCS, gen_imperativeoclcs_ImperativeLoopExpCS_CallExpCS, gen_imperativeoclcs_ImperativeLoopExpCS_StatementCS, gen_imperativeoclcs_DoExpCS_ExpressionBlockCS, gen_imperativeoclcs_ExceptCS_ElementCS, gen_imperativeoclcs_ExpressionBlockCS_ExpCS, gen_imperativeoclcs_ExpressionStatementCS_StatementCS, gen_imperativeoclcs_ForExpCS_ImperativeLoopExpCS, gen_imperativeoclcs_ListTypeCS_TypedRefCS, gen_imperativeoclcs_ListLiteralExpCS_ExpCS, gen_imperativeoclcs_LogExpCS_CallExpCS, gen_imperativeoclcs_QuitExpCS_StatementCS, gen_imperativeoclcs_RaiseExpCS_StatementCS, gen_imperativeoclcs_ReturnExpCS_ExpCS, gen_imperativeoclcs_StatementCS_ExpCS, gen_imperativeoclcs_SwitchAltCS_StatementCS, gen_imperativeoclcs_SwitchExpCS_StatementCS, gen_imperativeoclcs_TryExpCS_ExpressionBlockCS, gen_imperativeoclcs_VariableInitializationCS_StatementCS, gen_imperativeoclcs_WhileExpCS_ExpressionBlockCS},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)