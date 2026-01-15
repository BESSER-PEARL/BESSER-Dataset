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
miniOCL_RootCS = Class(name="miniOCL::RootCS")
miniOCL_PackageCS = Class(name="miniOCL::PackageCS")
miniOCL_ConstraintCS = Class(name="miniOCL::ConstraintCS")
miniOCL_ClassCS = Class(name="miniOCL::ClassCS")
miniOCL_PathNameCS = Class(name="miniOCL::PathNameCS")
miniOCL_PropertyCS = Class(name="miniOCL::PropertyCS")
miniOCL_OperationCS = Class(name="miniOCL::OperationCS")
miniOCL_ParameterCS = Class(name="miniOCL::ParameterCS")
miniOCL_ExpCS = Class(name="miniOCL::ExpCS")
miniOCL_InvariantCS = Class(name="miniOCL::InvariantCS")
miniOCL_LogicExpCS = Class(name="miniOCL::LogicExpCS")
ExpCS = Class(name="ExpCS")
miniOCL_CallExpCS = Class(name="miniOCL::CallExpCS")
LogicExpCS = Class(name="LogicExpCS")
miniOCL_NavigationExpCS = Class(name="miniOCL::NavigationExpCS")
miniOCL_PrimaryExpCS = Class(name="miniOCL::PrimaryExpCS")
CallExpCS = Class(name="CallExpCS")
PrimaryExpCS = Class(name="PrimaryExpCS")
miniOCL_NameExpCS = Class(name="miniOCL::NameExpCS")
NavigationExpCS = Class(name="NavigationExpCS")
miniOCL_RoundedBracketClauseCS = Class(name="miniOCL::RoundedBracketClauseCS")
miniOCL_LoopExpCS = Class(name="miniOCL::LoopExpCS")
miniOCL_IteratorVarCS = Class(name="miniOCL::IteratorVarCS")
miniOCL_CollectExpCS = Class(name="miniOCL::CollectExpCS")
LoopExpCS = Class(name="LoopExpCS")
miniOCL_IterateExpCS = Class(name="miniOCL::IterateExpCS")
miniOCL_AccVarCS = Class(name="miniOCL::AccVarCS")
miniOCL_LiteralExpCS = Class(name="miniOCL::LiteralExpCS")
miniOCL_IntLiteralExpCS = Class(name="miniOCL::IntLiteralExpCS")
LiteralExpCS = Class(name="LiteralExpCS")
miniOCL_StringLiteralExpCS = Class(name="miniOCL::StringLiteralExpCS")
miniOCL_BooleanLiteralExpCS = Class(name="miniOCL::BooleanLiteralExpCS")
miniOCL_PathCS = Class(name="miniOCL::PathCS")
miniOCL_PathVariableCS = Class(name="miniOCL::PathVariableCS")
PathCS = Class(name="PathCS")
miniOCL_PathElementCS = Class(name="miniOCL::PathElementCS")
miniOCL_EStructuralFeature = Class(name="miniOCL::EStructuralFeature")
miniOCL_BooleanExpCS = Class(name="miniOCL::BooleanExpCS")
BooleanLiteralExpCS = Class(name="BooleanLiteralExpCS")
miniOCL_ExistsExpCS = Class(name="miniOCL::ExistsExpCS")
miniOCL_NavigationNameExpCS = Class(name="miniOCL::NavigationNameExpCS")
miniOCL_NavigationPathNameCS = Class(name="miniOCL::NavigationPathNameCS")
miniOCL_NavigationPathCS = Class(name="miniOCL::NavigationPathCS")
miniOCL_NavigationPathVariableCS = Class(name="miniOCL::NavigationPathVariableCS")
NavigationPathCS = Class(name="NavigationPathCS")
miniOCL_NavigationPathElementCS = Class(name="miniOCL::NavigationPathElementCS")
miniOCL_ForAllExpCS = Class(name="miniOCL::ForAllExpCS")

# miniOCL_RootCS class attributes and methods

# miniOCL_PackageCS class attributes and methods
miniOCL_PackageCS_name: Property = Property(name="name", type=StringType)
miniOCL_PackageCS.attributes={miniOCL_PackageCS_name}

# miniOCL_ConstraintCS class attributes and methods

# miniOCL_ClassCS class attributes and methods
miniOCL_ClassCS_name: Property = Property(name="name", type=StringType)
miniOCL_ClassCS.attributes={miniOCL_ClassCS_name}

# miniOCL_PathNameCS class attributes and methods

# miniOCL_PropertyCS class attributes and methods
miniOCL_PropertyCS_name: Property = Property(name="name", type=StringType)
miniOCL_PropertyCS.attributes={miniOCL_PropertyCS_name}

# miniOCL_OperationCS class attributes and methods
miniOCL_OperationCS_name: Property = Property(name="name", type=StringType)
miniOCL_OperationCS.attributes={miniOCL_OperationCS_name}

# miniOCL_ParameterCS class attributes and methods
miniOCL_ParameterCS_name: Property = Property(name="name", type=StringType)
miniOCL_ParameterCS.attributes={miniOCL_ParameterCS_name}

# miniOCL_ExpCS class attributes and methods

# miniOCL_InvariantCS class attributes and methods

# miniOCL_LogicExpCS class attributes and methods
miniOCL_LogicExpCS_op: Property = Property(name="op", type=StringType)
miniOCL_LogicExpCS.attributes={miniOCL_LogicExpCS_op}

# ExpCS class attributes and methods

# miniOCL_CallExpCS class attributes and methods

# LogicExpCS class attributes and methods

# miniOCL_NavigationExpCS class attributes and methods

# miniOCL_PrimaryExpCS class attributes and methods

# CallExpCS class attributes and methods

# PrimaryExpCS class attributes and methods

# miniOCL_NameExpCS class attributes and methods

# NavigationExpCS class attributes and methods

# miniOCL_RoundedBracketClauseCS class attributes and methods

# miniOCL_LoopExpCS class attributes and methods
miniOCL_LoopExpCS_logicOp: Property = Property(name="logicOp", type=StringType)
miniOCL_LoopExpCS.attributes={miniOCL_LoopExpCS_logicOp}

# miniOCL_IteratorVarCS class attributes and methods
miniOCL_IteratorVarCS_itName: Property = Property(name="itName", type=StringType)
miniOCL_IteratorVarCS.attributes={miniOCL_IteratorVarCS_itName}

# miniOCL_CollectExpCS class attributes and methods

# LoopExpCS class attributes and methods

# miniOCL_IterateExpCS class attributes and methods

# miniOCL_AccVarCS class attributes and methods
miniOCL_AccVarCS_accVarName: Property = Property(name="accVarName", type=StringType)
miniOCL_AccVarCS.attributes={miniOCL_AccVarCS_accVarName}

# miniOCL_LiteralExpCS class attributes and methods

# miniOCL_IntLiteralExpCS class attributes and methods
miniOCL_IntLiteralExpCS_intSymbol: Property = Property(name="intSymbol", type=IntegerType)
miniOCL_IntLiteralExpCS.attributes={miniOCL_IntLiteralExpCS_intSymbol}

# LiteralExpCS class attributes and methods

# miniOCL_StringLiteralExpCS class attributes and methods
miniOCL_StringLiteralExpCS_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
miniOCL_StringLiteralExpCS.attributes={miniOCL_StringLiteralExpCS_stringSymbol}

# miniOCL_BooleanLiteralExpCS class attributes and methods

# miniOCL_PathCS class attributes and methods

# miniOCL_PathVariableCS class attributes and methods
miniOCL_PathVariableCS_varName: Property = Property(name="varName", type=StringType)
miniOCL_PathVariableCS.attributes={miniOCL_PathVariableCS_varName}

# PathCS class attributes and methods

# miniOCL_PathElementCS class attributes and methods

# miniOCL_EStructuralFeature class attributes and methods

# miniOCL_BooleanExpCS class attributes and methods
miniOCL_BooleanExpCS_boolSymbol: Property = Property(name="boolSymbol", type=BooleanType)
miniOCL_BooleanExpCS.attributes={miniOCL_BooleanExpCS_boolSymbol}

# BooleanLiteralExpCS class attributes and methods

# miniOCL_ExistsExpCS class attributes and methods

# miniOCL_NavigationNameExpCS class attributes and methods

# miniOCL_NavigationPathNameCS class attributes and methods

# miniOCL_NavigationPathCS class attributes and methods

# miniOCL_NavigationPathVariableCS class attributes and methods
miniOCL_NavigationPathVariableCS_varName: Property = Property(name="varName", type=StringType)
miniOCL_NavigationPathVariableCS.attributes={miniOCL_NavigationPathVariableCS_varName}

# NavigationPathCS class attributes and methods

# miniOCL_NavigationPathElementCS class attributes and methods

# miniOCL_ForAllExpCS class attributes and methods

# Relationships
packages0: BinaryAssociation = BinaryAssociation(
    name="packages0",
    ends={
        Property(name="miniOCL_PackageCS", type=miniOCL_RootCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_RootCS", type=miniOCL_PackageCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contraints1: BinaryAssociation = BinaryAssociation(
    name="contraints1",
    ends={
        Property(name="miniOCL_ConstraintCS", type=miniOCL_RootCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_RootCS2", type=miniOCL_ConstraintCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packages4: BinaryAssociation = BinaryAssociation(
    name="packages4",
    ends={
        Property(name="miniOCL_PackageCS5", type=miniOCL_PackageCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_PackageCS3", type=miniOCL_PackageCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classes6: BinaryAssociation = BinaryAssociation(
    name="classes6",
    ends={
        Property(name="miniOCL_ClassCS", type=miniOCL_PackageCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_PackageCS7", type=miniOCL_ClassCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extends8: BinaryAssociation = BinaryAssociation(
    name="extends8",
    ends={
        Property(name="miniOCL_PathNameCS", type=miniOCL_ClassCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_ClassCS9", type=miniOCL_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties10: BinaryAssociation = BinaryAssociation(
    name="properties10",
    ends={
        Property(name="miniOCL_PropertyCS", type=miniOCL_ClassCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_ClassCS11", type=miniOCL_PropertyCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations12: BinaryAssociation = BinaryAssociation(
    name="operations12",
    ends={
        Property(name="miniOCL_OperationCS", type=miniOCL_ClassCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_ClassCS13", type=miniOCL_OperationCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeRef14: BinaryAssociation = BinaryAssociation(
    name="typeRef14",
    ends={
        Property(name="miniOCL_PathNameCS16", type=miniOCL_PropertyCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_PropertyCS15", type=miniOCL_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
params17: BinaryAssociation = BinaryAssociation(
    name="params17",
    ends={
        Property(name="miniOCL_ParameterCS", type=miniOCL_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_OperationCS18", type=miniOCL_ParameterCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resultRef19: BinaryAssociation = BinaryAssociation(
    name="resultRef19",
    ends={
        Property(name="miniOCL_PathNameCS21", type=miniOCL_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_OperationCS20", type=miniOCL_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body22: BinaryAssociation = BinaryAssociation(
    name="body22",
    ends={
        Property(name="miniOCL_ExpCS", type=miniOCL_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_OperationCS23", type=miniOCL_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeRef24: BinaryAssociation = BinaryAssociation(
    name="typeRef24",
    ends={
        Property(name="miniOCL_PathNameCS26", type=miniOCL_ParameterCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_ParameterCS25", type=miniOCL_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeRef27: BinaryAssociation = BinaryAssociation(
    name="typeRef27",
    ends={
        Property(name="miniOCL_PathNameCS29", type=miniOCL_ConstraintCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_ConstraintCS28", type=miniOCL_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
invariants30: BinaryAssociation = BinaryAssociation(
    name="invariants30",
    ends={
        Property(name="miniOCL_InvariantCS", type=miniOCL_ConstraintCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_ConstraintCS31", type=miniOCL_InvariantCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp32: BinaryAssociation = BinaryAssociation(
    name="exp32",
    ends={
        Property(name="miniOCL_ExpCS34", type=miniOCL_InvariantCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_InvariantCS33", type=miniOCL_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left36: BinaryAssociation = BinaryAssociation(
    name="left36",
    ends={
        Property(name="miniOCL_LogicExpCS", type=miniOCL_LogicExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_LogicExpCS35", type=miniOCL_LogicExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right37: BinaryAssociation = BinaryAssociation(
    name="right37",
    ends={
        Property(name="miniOCL_CallExpCS", type=miniOCL_LogicExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_LogicExpCS38", type=miniOCL_CallExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source40: BinaryAssociation = BinaryAssociation(
    name="source40",
    ends={
        Property(name="miniOCL_CallExpCS41", type=miniOCL_CallExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_CallExpCS39", type=miniOCL_CallExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
navExp42: BinaryAssociation = BinaryAssociation(
    name="navExp42",
    ends={
        Property(name="miniOCL_NavigationExpCS", type=miniOCL_CallExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_CallExpCS43", type=miniOCL_NavigationExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expName44: BinaryAssociation = BinaryAssociation(
    name="expName44",
    ends={
        Property(name="miniOCL_PathNameCS45", type=miniOCL_NameExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_NameExpCS", type=miniOCL_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
roundedBrackets46: BinaryAssociation = BinaryAssociation(
    name="roundedBrackets46",
    ends={
        Property(name="miniOCL_RoundedBracketClauseCS", type=miniOCL_NameExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_NameExpCS47", type=miniOCL_RoundedBracketClauseCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
itVar51: BinaryAssociation = BinaryAssociation(
    name="itVar51",
    ends={
        Property(name="miniOCL_IteratorVarCS", type=miniOCL_LoopExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_LoopExpCS", type=miniOCL_IteratorVarCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp52: BinaryAssociation = BinaryAssociation(
    name="exp52",
    ends={
        Property(name="miniOCL_ExpCS54", type=miniOCL_LoopExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_LoopExpCS53", type=miniOCL_ExpCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
itType55: BinaryAssociation = BinaryAssociation(
    name="itType55",
    ends={
        Property(name="miniOCL_PathNameCS57", type=miniOCL_IteratorVarCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_IteratorVarCS56", type=miniOCL_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accVar58: BinaryAssociation = BinaryAssociation(
    name="accVar58",
    ends={
        Property(name="miniOCL_AccVarCS", type=miniOCL_IterateExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_IterateExpCS", type=miniOCL_AccVarCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accType59: BinaryAssociation = BinaryAssociation(
    name="accType59",
    ends={
        Property(name="miniOCL_PathNameCS61", type=miniOCL_AccVarCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_AccVarCS60", type=miniOCL_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accInitExp62: BinaryAssociation = BinaryAssociation(
    name="accInitExp62",
    ends={
        Property(name="miniOCL_ExpCS64", type=miniOCL_AccVarCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_AccVarCS63", type=miniOCL_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args65: BinaryAssociation = BinaryAssociation(
    name="args65",
    ends={
        Property(name="miniOCL_ExpCS67", type=miniOCL_RoundedBracketClauseCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_RoundedBracketClauseCS66", type=miniOCL_ExpCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
callExp48: BinaryAssociation = BinaryAssociation(
    name="callExp48",
    ends={
        Property(name="miniOCL_CallExpCS50", type=miniOCL_NameExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_NameExpCS49", type=miniOCL_CallExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pathName70: BinaryAssociation = BinaryAssociation(
    name="pathName70",
    ends={
        Property(name="miniOCL_EStructuralFeature", type=miniOCL_PathElementCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_PathElementCS", type=miniOCL_EStructuralFeature, multiplicity=Multiplicity(0, 1))
    }
)
accVars71: BinaryAssociation = BinaryAssociation(
    name="accVars71",
    ends={
        Property(name="miniOCL_AccVarCS72", type=miniOCL_ExistsExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_ExistsExpCS", type=miniOCL_AccVarCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expName73: BinaryAssociation = BinaryAssociation(
    name="expName73",
    ends={
        Property(name="miniOCL_NavigationPathNameCS", type=miniOCL_NavigationNameExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_NavigationNameExpCS", type=miniOCL_NavigationPathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
roundedBrackets74: BinaryAssociation = BinaryAssociation(
    name="roundedBrackets74",
    ends={
        Property(name="miniOCL_RoundedBracketClauseCS76", type=miniOCL_NavigationNameExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_NavigationNameExpCS75", type=miniOCL_RoundedBracketClauseCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
path68: BinaryAssociation = BinaryAssociation(
    name="path68",
    ends={
        Property(name="miniOCL_PathCS", type=miniOCL_PathNameCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_PathNameCS69", type=miniOCL_PathCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
callExp77: BinaryAssociation = BinaryAssociation(
    name="callExp77",
    ends={
        Property(name="miniOCL_CallExpCS79", type=miniOCL_NavigationNameExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_NavigationNameExpCS78", type=miniOCL_CallExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
path80: BinaryAssociation = BinaryAssociation(
    name="path80",
    ends={
        Property(name="miniOCL_NavigationPathCS", type=miniOCL_NavigationPathNameCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_NavigationPathNameCS81", type=miniOCL_NavigationPathCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pathName82: BinaryAssociation = BinaryAssociation(
    name="pathName82",
    ends={
        Property(name="miniOCL_EStructuralFeature83", type=miniOCL_NavigationPathElementCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_NavigationPathElementCS", type=miniOCL_EStructuralFeature, multiplicity=Multiplicity(0, 1))
    }
)
accVars84: BinaryAssociation = BinaryAssociation(
    name="accVars84",
    ends={
        Property(name="miniOCL_AccVarCS85", type=miniOCL_ForAllExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="miniOCL_ForAllExpCS", type=miniOCL_AccVarCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_miniOCL_LogicExpCS_ExpCS = Generalization(general=ExpCS, specific=miniOCL_LogicExpCS)
gen_miniOCL_CallExpCS_LogicExpCS = Generalization(general=LogicExpCS, specific=miniOCL_CallExpCS)
gen_miniOCL_PrimaryExpCS_CallExpCS = Generalization(general=CallExpCS, specific=miniOCL_PrimaryExpCS)
gen_miniOCL_NavigationExpCS_PrimaryExpCS = Generalization(general=PrimaryExpCS, specific=miniOCL_NavigationExpCS)
gen_miniOCL_NameExpCS_NavigationExpCS = Generalization(general=NavigationExpCS, specific=miniOCL_NameExpCS)
gen_miniOCL_LoopExpCS_NavigationExpCS = Generalization(general=NavigationExpCS, specific=miniOCL_LoopExpCS)
gen_miniOCL_CollectExpCS_LoopExpCS = Generalization(general=LoopExpCS, specific=miniOCL_CollectExpCS)
gen_miniOCL_IterateExpCS_LoopExpCS = Generalization(general=LoopExpCS, specific=miniOCL_IterateExpCS)
gen_miniOCL_LiteralExpCS_PrimaryExpCS = Generalization(general=PrimaryExpCS, specific=miniOCL_LiteralExpCS)
gen_miniOCL_IntLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=miniOCL_IntLiteralExpCS)
gen_miniOCL_StringLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=miniOCL_StringLiteralExpCS)
gen_miniOCL_BooleanLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=miniOCL_BooleanLiteralExpCS)
gen_miniOCL_PathVariableCS_PathCS = Generalization(general=PathCS, specific=miniOCL_PathVariableCS)
gen_miniOCL_PathElementCS_PathCS = Generalization(general=PathCS, specific=miniOCL_PathElementCS)
gen_miniOCL_BooleanExpCS_BooleanLiteralExpCS = Generalization(general=BooleanLiteralExpCS, specific=miniOCL_BooleanExpCS)
gen_miniOCL_ExistsExpCS_LoopExpCS = Generalization(general=LoopExpCS, specific=miniOCL_ExistsExpCS)
gen_miniOCL_NavigationNameExpCS_NavigationExpCS = Generalization(general=NavigationExpCS, specific=miniOCL_NavigationNameExpCS)
gen_miniOCL_NavigationPathVariableCS_NavigationPathCS = Generalization(general=NavigationPathCS, specific=miniOCL_NavigationPathVariableCS)
gen_miniOCL_NavigationPathElementCS_NavigationPathCS = Generalization(general=NavigationPathCS, specific=miniOCL_NavigationPathElementCS)
gen_miniOCL_ForAllExpCS_LoopExpCS = Generalization(general=LoopExpCS, specific=miniOCL_ForAllExpCS)

# Domain Model
domain_model = DomainModel(
    name="miniOCL",
    types={miniOCL_RootCS, miniOCL_PackageCS, miniOCL_ConstraintCS, miniOCL_ClassCS, miniOCL_PathNameCS, miniOCL_PropertyCS, miniOCL_OperationCS, miniOCL_ParameterCS, miniOCL_ExpCS, miniOCL_InvariantCS, miniOCL_LogicExpCS, ExpCS, miniOCL_CallExpCS, LogicExpCS, miniOCL_NavigationExpCS, miniOCL_PrimaryExpCS, CallExpCS, PrimaryExpCS, miniOCL_NameExpCS, NavigationExpCS, miniOCL_RoundedBracketClauseCS, miniOCL_LoopExpCS, miniOCL_IteratorVarCS, miniOCL_CollectExpCS, LoopExpCS, miniOCL_IterateExpCS, miniOCL_AccVarCS, miniOCL_LiteralExpCS, miniOCL_IntLiteralExpCS, LiteralExpCS, miniOCL_StringLiteralExpCS, miniOCL_BooleanLiteralExpCS, miniOCL_PathCS, miniOCL_PathVariableCS, PathCS, miniOCL_PathElementCS, miniOCL_EStructuralFeature, miniOCL_BooleanExpCS, BooleanLiteralExpCS, miniOCL_ExistsExpCS, miniOCL_NavigationNameExpCS, miniOCL_NavigationPathNameCS, miniOCL_NavigationPathCS, miniOCL_NavigationPathVariableCS, NavigationPathCS, miniOCL_NavigationPathElementCS, miniOCL_ForAllExpCS},
    associations={packages0, contraints1, packages4, classes6, extends8, properties10, operations12, typeRef14, params17, resultRef19, body22, typeRef24, typeRef27, invariants30, exp32, left36, right37, source40, navExp42, expName44, roundedBrackets46, itVar51, exp52, itType55, accVar58, accType59, accInitExp62, args65, callExp48, pathName70, accVars71, expName73, roundedBrackets74, path68, callExp77, path80, pathName82, accVars84},
    generalizations={gen_miniOCL_LogicExpCS_ExpCS, gen_miniOCL_CallExpCS_LogicExpCS, gen_miniOCL_PrimaryExpCS_CallExpCS, gen_miniOCL_NavigationExpCS_PrimaryExpCS, gen_miniOCL_NameExpCS_NavigationExpCS, gen_miniOCL_LoopExpCS_NavigationExpCS, gen_miniOCL_CollectExpCS_LoopExpCS, gen_miniOCL_IterateExpCS_LoopExpCS, gen_miniOCL_LiteralExpCS_PrimaryExpCS, gen_miniOCL_IntLiteralExpCS_LiteralExpCS, gen_miniOCL_StringLiteralExpCS_LiteralExpCS, gen_miniOCL_BooleanLiteralExpCS_LiteralExpCS, gen_miniOCL_PathVariableCS_PathCS, gen_miniOCL_PathElementCS_PathCS, gen_miniOCL_BooleanExpCS_BooleanLiteralExpCS, gen_miniOCL_ExistsExpCS_LoopExpCS, gen_miniOCL_NavigationNameExpCS_NavigationExpCS, gen_miniOCL_NavigationPathVariableCS_NavigationPathCS, gen_miniOCL_NavigationPathElementCS_NavigationPathCS, gen_miniOCL_ForAllExpCS_LoopExpCS},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)