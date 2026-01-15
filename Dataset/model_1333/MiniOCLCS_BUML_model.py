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
CollectionKindCS: Enumeration = Enumeration(
    name="CollectionKindCS",
    literals={
            EnumerationLiteral(name="Collection")
    }
)

# Classes
minioclcs_RootCS = Class(name="minioclcs::RootCS")
CSTrace = Class(name="CSTrace")
minioclcs_ImportCS = Class(name="minioclcs::ImportCS")
minioclcs_PackageCS = Class(name="minioclcs::PackageCS")
minioclcs_ConstraintsDefCS = Class(name="minioclcs::ConstraintsDefCS")
minioclcs_ClassCS = Class(name="minioclcs::ClassCS")
minioclcs_PropertyCS = Class(name="minioclcs::PropertyCS")
minioclcs_OperationCS = Class(name="minioclcs::OperationCS")
minioclcs_MultiplicityCS = Class(name="minioclcs::MultiplicityCS")
minioclcs_ParameterCS = Class(name="minioclcs::ParameterCS")
minioclcs_ExpCS = Class(name="minioclcs::ExpCS")
minioclcs_PathNameCS = Class(name="minioclcs::PathNameCS")
minioclcs_InvariantCS = Class(name="minioclcs::InvariantCS")
minioclcs_EqualityExpCS = Class(name="minioclcs::EqualityExpCS")
ExpCS = Class(name="ExpCS")
minioclcs_CallExpCS = Class(name="minioclcs::CallExpCS")
EqualityExpCS = Class(name="EqualityExpCS")
minioclcs_NavigationExpCS = Class(name="minioclcs::NavigationExpCS")
minioclcs_PrimaryExpCS = Class(name="minioclcs::PrimaryExpCS")
CallExpCS = Class(name="CallExpCS")
minioclcs_SelfExpCS = Class(name="minioclcs::SelfExpCS")
PrimaryExpCS = Class(name="PrimaryExpCS")
minioclcs_LoopExpCS = Class(name="minioclcs::LoopExpCS")
NavigationExpCS = Class(name="NavigationExpCS")
minioclcs_IteratorVarCS = Class(name="minioclcs::IteratorVarCS")
minioclcs_CollectExpCS = Class(name="minioclcs::CollectExpCS")
LoopExpCS = Class(name="LoopExpCS")
minioclcs_IterateExpCS = Class(name="minioclcs::IterateExpCS")
minioclcs_AccVarCS = Class(name="minioclcs::AccVarCS")
minioclcs_NameExpCS = Class(name="minioclcs::NameExpCS")
minioclcs_RoundedBracketClauseCS = Class(name="minioclcs::RoundedBracketClauseCS")
minioclcs_LiteralExpCS = Class(name="minioclcs::LiteralExpCS")
minioclcs_IntLiteralExpCS = Class(name="minioclcs::IntLiteralExpCS")
LiteralExpCS = Class(name="LiteralExpCS")
minioclcs_BooleanLiteralExpCS = Class(name="minioclcs::BooleanLiteralExpCS")
minioclcs_NullLiteralExpCS = Class(name="minioclcs::NullLiteralExpCS")
minioclcs_CollectionLiteralExpCS = Class(name="minioclcs::CollectionLiteralExpCS")
minioclcs_CollectionLiteralPartCS = Class(name="minioclcs::CollectionLiteralPartCS")
minioclcs_LetExpCS = Class(name="minioclcs::LetExpCS")
minioclcs_LetVarCS = Class(name="minioclcs::LetVarCS")
minioclcs_PathElementCS = Class(name="minioclcs::PathElementCS")
minioclcs_EClass = Class(name="minioclcs::EClass")
minioclcs_BooleanExpCS = Class(name="minioclcs::BooleanExpCS")
BooleanLiteralExpCS = Class(name="BooleanLiteralExpCS")
minioclcs_EObject = Class(name="minioclcs::EObject")
minioclcs_CSTrace = Class(name="minioclcs::CSTrace", is_abstract=True)

# minioclcs_RootCS class attributes and methods

# CSTrace class attributes and methods

# minioclcs_ImportCS class attributes and methods
minioclcs_ImportCS_alias: Property = Property(name="alias", type=StringType)
minioclcs_ImportCS_uri: Property = Property(name="uri", type=StringType)
minioclcs_ImportCS.attributes={minioclcs_ImportCS_alias, minioclcs_ImportCS_uri}

# minioclcs_PackageCS class attributes and methods
minioclcs_PackageCS_name: Property = Property(name="name", type=StringType)
minioclcs_PackageCS.attributes={minioclcs_PackageCS_name}

# minioclcs_ConstraintsDefCS class attributes and methods

# minioclcs_ClassCS class attributes and methods
minioclcs_ClassCS_name: Property = Property(name="name", type=StringType)
minioclcs_ClassCS.attributes={minioclcs_ClassCS_name}

# minioclcs_PropertyCS class attributes and methods
minioclcs_PropertyCS_name: Property = Property(name="name", type=StringType)
minioclcs_PropertyCS.attributes={minioclcs_PropertyCS_name}

# minioclcs_OperationCS class attributes and methods
minioclcs_OperationCS_name: Property = Property(name="name", type=StringType)
minioclcs_OperationCS.attributes={minioclcs_OperationCS_name}

# minioclcs_MultiplicityCS class attributes and methods
minioclcs_MultiplicityCS_opt: Property = Property(name="opt", type=BooleanType)
minioclcs_MultiplicityCS_mult: Property = Property(name="mult", type=BooleanType)
minioclcs_MultiplicityCS_mandatory: Property = Property(name="mandatory", type=IntegerType)
minioclcs_MultiplicityCS_lowerInt: Property = Property(name="lowerInt", type=IntegerType)
minioclcs_MultiplicityCS_upperInt: Property = Property(name="upperInt", type=IntegerType)
minioclcs_MultiplicityCS_upperMult: Property = Property(name="upperMult", type=BooleanType)
minioclcs_MultiplicityCS.attributes={minioclcs_MultiplicityCS_mandatory, minioclcs_MultiplicityCS_opt, minioclcs_MultiplicityCS_upperInt, minioclcs_MultiplicityCS_upperMult, minioclcs_MultiplicityCS_mult, minioclcs_MultiplicityCS_lowerInt}

# minioclcs_ParameterCS class attributes and methods
minioclcs_ParameterCS_name: Property = Property(name="name", type=StringType)
minioclcs_ParameterCS.attributes={minioclcs_ParameterCS_name}

# minioclcs_ExpCS class attributes and methods

# minioclcs_PathNameCS class attributes and methods

# minioclcs_InvariantCS class attributes and methods

# minioclcs_EqualityExpCS class attributes and methods
minioclcs_EqualityExpCS_opName: Property = Property(name="opName", type=StringType)
minioclcs_EqualityExpCS.attributes={minioclcs_EqualityExpCS_opName}

# ExpCS class attributes and methods

# minioclcs_CallExpCS class attributes and methods

# EqualityExpCS class attributes and methods

# minioclcs_NavigationExpCS class attributes and methods

# minioclcs_PrimaryExpCS class attributes and methods

# CallExpCS class attributes and methods

# minioclcs_SelfExpCS class attributes and methods

# PrimaryExpCS class attributes and methods

# minioclcs_LoopExpCS class attributes and methods

# NavigationExpCS class attributes and methods

# minioclcs_IteratorVarCS class attributes and methods
minioclcs_IteratorVarCS_itName: Property = Property(name="itName", type=StringType)
minioclcs_IteratorVarCS.attributes={minioclcs_IteratorVarCS_itName}

# minioclcs_CollectExpCS class attributes and methods

# LoopExpCS class attributes and methods

# minioclcs_IterateExpCS class attributes and methods

# minioclcs_AccVarCS class attributes and methods
minioclcs_AccVarCS_accName: Property = Property(name="accName", type=StringType)
minioclcs_AccVarCS.attributes={minioclcs_AccVarCS_accName}

# minioclcs_NameExpCS class attributes and methods

# minioclcs_RoundedBracketClauseCS class attributes and methods

# minioclcs_LiteralExpCS class attributes and methods

# minioclcs_IntLiteralExpCS class attributes and methods
minioclcs_IntLiteralExpCS_intSymbol: Property = Property(name="intSymbol", type=IntegerType)
minioclcs_IntLiteralExpCS.attributes={minioclcs_IntLiteralExpCS_intSymbol}

# LiteralExpCS class attributes and methods

# minioclcs_BooleanLiteralExpCS class attributes and methods

# minioclcs_NullLiteralExpCS class attributes and methods

# minioclcs_CollectionLiteralExpCS class attributes and methods
minioclcs_CollectionLiteralExpCS_kind: Property = Property(name="kind", type=StringType)
minioclcs_CollectionLiteralExpCS.attributes={minioclcs_CollectionLiteralExpCS_kind}

# minioclcs_CollectionLiteralPartCS class attributes and methods

# minioclcs_LetExpCS class attributes and methods

# minioclcs_LetVarCS class attributes and methods
minioclcs_LetVarCS_name: Property = Property(name="name", type=StringType)
minioclcs_LetVarCS.attributes={minioclcs_LetVarCS_name}

# minioclcs_PathElementCS class attributes and methods

# minioclcs_EClass class attributes and methods

# minioclcs_BooleanExpCS class attributes and methods
minioclcs_BooleanExpCS_boolSymbol: Property = Property(name="boolSymbol", type=BooleanType)
minioclcs_BooleanExpCS.attributes={minioclcs_BooleanExpCS_boolSymbol}

# BooleanLiteralExpCS class attributes and methods

# minioclcs_EObject class attributes and methods

# minioclcs_CSTrace class attributes and methods

# Relationships
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="minioclcs_ImportCS", type=minioclcs_RootCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_RootCS", type=minioclcs_ImportCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packages1: BinaryAssociation = BinaryAssociation(
    name="packages1",
    ends={
        Property(name="minioclcs_PackageCS", type=minioclcs_RootCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_RootCS2", type=minioclcs_PackageCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints3: BinaryAssociation = BinaryAssociation(
    name="constraints3",
    ends={
        Property(name="minioclcs_ConstraintsDefCS", type=minioclcs_RootCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_RootCS4", type=minioclcs_ConstraintsDefCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packages6: BinaryAssociation = BinaryAssociation(
    name="packages6",
    ends={
        Property(name="minioclcs_PackageCS7", type=minioclcs_PackageCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_PackageCS5", type=minioclcs_PackageCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classes8: BinaryAssociation = BinaryAssociation(
    name="classes8",
    ends={
        Property(name="minioclcs_ClassCS", type=minioclcs_PackageCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_PackageCS9", type=minioclcs_ClassCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties12: BinaryAssociation = BinaryAssociation(
    name="properties12",
    ends={
        Property(name="minioclcs_PropertyCS", type=minioclcs_ClassCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_ClassCS13", type=minioclcs_PropertyCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations14: BinaryAssociation = BinaryAssociation(
    name="operations14",
    ends={
        Property(name="minioclcs_OperationCS", type=minioclcs_ClassCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_ClassCS15", type=minioclcs_OperationCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeRef16: BinaryAssociation = BinaryAssociation(
    name="typeRef16",
    ends={
        Property(name="minioclcs_PathNameCS18", type=minioclcs_PropertyCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_PropertyCS17", type=minioclcs_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multiplicity19: BinaryAssociation = BinaryAssociation(
    name="multiplicity19",
    ends={
        Property(name="minioclcs_MultiplicityCS", type=minioclcs_PropertyCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_PropertyCS20", type=minioclcs_MultiplicityCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
params21: BinaryAssociation = BinaryAssociation(
    name="params21",
    ends={
        Property(name="minioclcs_ParameterCS", type=minioclcs_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_OperationCS22", type=minioclcs_ParameterCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resultRef23: BinaryAssociation = BinaryAssociation(
    name="resultRef23",
    ends={
        Property(name="minioclcs_PathNameCS25", type=minioclcs_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_OperationCS24", type=minioclcs_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body26: BinaryAssociation = BinaryAssociation(
    name="body26",
    ends={
        Property(name="minioclcs_ExpCS", type=minioclcs_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_OperationCS27", type=minioclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeRef28: BinaryAssociation = BinaryAssociation(
    name="typeRef28",
    ends={
        Property(name="minioclcs_PathNameCS30", type=minioclcs_ParameterCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_ParameterCS29", type=minioclcs_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extends10: BinaryAssociation = BinaryAssociation(
    name="extends10",
    ends={
        Property(name="minioclcs_PathNameCS", type=minioclcs_ClassCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_ClassCS11", type=minioclcs_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeRef31: BinaryAssociation = BinaryAssociation(
    name="typeRef31",
    ends={
        Property(name="minioclcs_PathNameCS33", type=minioclcs_ConstraintsDefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_ConstraintsDefCS32", type=minioclcs_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
invariants34: BinaryAssociation = BinaryAssociation(
    name="invariants34",
    ends={
        Property(name="minioclcs_InvariantCS", type=minioclcs_ConstraintsDefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_ConstraintsDefCS35", type=minioclcs_InvariantCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp36: BinaryAssociation = BinaryAssociation(
    name="exp36",
    ends={
        Property(name="minioclcs_ExpCS38", type=minioclcs_InvariantCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_InvariantCS37", type=minioclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left40: BinaryAssociation = BinaryAssociation(
    name="left40",
    ends={
        Property(name="minioclcs_EqualityExpCS", type=minioclcs_EqualityExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_EqualityExpCS39", type=minioclcs_EqualityExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right41: BinaryAssociation = BinaryAssociation(
    name="right41",
    ends={
        Property(name="minioclcs_CallExpCS", type=minioclcs_EqualityExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_EqualityExpCS42", type=minioclcs_CallExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source44: BinaryAssociation = BinaryAssociation(
    name="source44",
    ends={
        Property(name="minioclcs_CallExpCS45", type=minioclcs_CallExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_CallExpCS43", type=minioclcs_CallExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
navExp46: BinaryAssociation = BinaryAssociation(
    name="navExp46",
    ends={
        Property(name="minioclcs_NavigationExpCS", type=minioclcs_CallExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_CallExpCS47", type=minioclcs_NavigationExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
itVar48: BinaryAssociation = BinaryAssociation(
    name="itVar48",
    ends={
        Property(name="minioclcs_IteratorVarCS", type=minioclcs_LoopExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_LoopExpCS", type=minioclcs_IteratorVarCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp49: BinaryAssociation = BinaryAssociation(
    name="exp49",
    ends={
        Property(name="minioclcs_ExpCS51", type=minioclcs_LoopExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_LoopExpCS50", type=minioclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
itType52: BinaryAssociation = BinaryAssociation(
    name="itType52",
    ends={
        Property(name="minioclcs_PathNameCS54", type=minioclcs_IteratorVarCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_IteratorVarCS53", type=minioclcs_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accVar55: BinaryAssociation = BinaryAssociation(
    name="accVar55",
    ends={
        Property(name="minioclcs_AccVarCS", type=minioclcs_IterateExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_IterateExpCS", type=minioclcs_AccVarCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accType56: BinaryAssociation = BinaryAssociation(
    name="accType56",
    ends={
        Property(name="minioclcs_PathNameCS58", type=minioclcs_AccVarCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_AccVarCS57", type=minioclcs_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accInitExp59: BinaryAssociation = BinaryAssociation(
    name="accInitExp59",
    ends={
        Property(name="minioclcs_ExpCS61", type=minioclcs_AccVarCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_AccVarCS60", type=minioclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expName62: BinaryAssociation = BinaryAssociation(
    name="expName62",
    ends={
        Property(name="minioclcs_PathNameCS63", type=minioclcs_NameExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_NameExpCS", type=minioclcs_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
roundedBrackets64: BinaryAssociation = BinaryAssociation(
    name="roundedBrackets64",
    ends={
        Property(name="minioclcs_RoundedBracketClauseCS", type=minioclcs_NameExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_NameExpCS65", type=minioclcs_RoundedBracketClauseCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args66: BinaryAssociation = BinaryAssociation(
    name="args66",
    ends={
        Property(name="minioclcs_ExpCS68", type=minioclcs_RoundedBracketClauseCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_RoundedBracketClauseCS67", type=minioclcs_ExpCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parts69: BinaryAssociation = BinaryAssociation(
    name="parts69",
    ends={
        Property(name="minioclcs_CollectionLiteralPartCS", type=minioclcs_CollectionLiteralExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_CollectionLiteralExpCS", type=minioclcs_CollectionLiteralPartCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
first70: BinaryAssociation = BinaryAssociation(
    name="first70",
    ends={
        Property(name="minioclcs_ExpCS72", type=minioclcs_CollectionLiteralPartCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_CollectionLiteralPartCS71", type=minioclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
last73: BinaryAssociation = BinaryAssociation(
    name="last73",
    ends={
        Property(name="minioclcs_ExpCS75", type=minioclcs_CollectionLiteralPartCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_CollectionLiteralPartCS74", type=minioclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
letVars76: BinaryAssociation = BinaryAssociation(
    name="letVars76",
    ends={
        Property(name="minioclcs_LetVarCS", type=minioclcs_LetExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_LetExpCS", type=minioclcs_LetVarCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inExp77: BinaryAssociation = BinaryAssociation(
    name="inExp77",
    ends={
        Property(name="minioclcs_ExpCS79", type=minioclcs_LetExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_LetExpCS78", type=minioclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeRef80: BinaryAssociation = BinaryAssociation(
    name="typeRef80",
    ends={
        Property(name="minioclcs_PathNameCS82", type=minioclcs_LetVarCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_LetVarCS81", type=minioclcs_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initExp83: BinaryAssociation = BinaryAssociation(
    name="initExp83",
    ends={
        Property(name="minioclcs_ExpCS85", type=minioclcs_LetVarCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_LetVarCS84", type=minioclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pathElements86: BinaryAssociation = BinaryAssociation(
    name="pathElements86",
    ends={
        Property(name="minioclcs_PathElementCS", type=minioclcs_PathNameCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_PathNameCS87", type=minioclcs_PathElementCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elementName88: BinaryAssociation = BinaryAssociation(
    name="elementName88",
    ends={
        Property(name="minioclcs_EClass", type=minioclcs_PathElementCS, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_PathElementCS89", type=minioclcs_EClass, multiplicity=Multiplicity(0, 1))
    }
)
ast90: BinaryAssociation = BinaryAssociation(
    name="ast90",
    ends={
        Property(name="minioclcs_EObject", type=minioclcs_CSTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="minioclcs_CSTrace", type=minioclcs_EObject, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_minioclcs_RootCS_CSTrace = Generalization(general=CSTrace, specific=minioclcs_RootCS)
gen_minioclcs_ImportCS_CSTrace = Generalization(general=CSTrace, specific=minioclcs_ImportCS)
gen_minioclcs_PackageCS_CSTrace = Generalization(general=CSTrace, specific=minioclcs_PackageCS)
gen_minioclcs_ClassCS_CSTrace = Generalization(general=CSTrace, specific=minioclcs_ClassCS)
gen_minioclcs_PropertyCS_CSTrace = Generalization(general=CSTrace, specific=minioclcs_PropertyCS)
gen_minioclcs_MultiplicityCS_CSTrace = Generalization(general=CSTrace, specific=minioclcs_MultiplicityCS)
gen_minioclcs_OperationCS_CSTrace = Generalization(general=CSTrace, specific=minioclcs_OperationCS)
gen_minioclcs_ParameterCS_CSTrace = Generalization(general=CSTrace, specific=minioclcs_ParameterCS)
gen_minioclcs_InvariantCS_CSTrace = Generalization(general=CSTrace, specific=minioclcs_InvariantCS)
gen_minioclcs_ExpCS_CSTrace = Generalization(general=CSTrace, specific=minioclcs_ExpCS)
gen_minioclcs_EqualityExpCS_ExpCS = Generalization(general=ExpCS, specific=minioclcs_EqualityExpCS)
gen_minioclcs_CallExpCS_EqualityExpCS = Generalization(general=EqualityExpCS, specific=minioclcs_CallExpCS)
gen_minioclcs_PrimaryExpCS_CallExpCS = Generalization(general=CallExpCS, specific=minioclcs_PrimaryExpCS)
gen_minioclcs_SelfExpCS_PrimaryExpCS = Generalization(general=PrimaryExpCS, specific=minioclcs_SelfExpCS)
gen_minioclcs_NavigationExpCS_CSTrace = Generalization(general=CSTrace, specific=minioclcs_NavigationExpCS)
gen_minioclcs_LoopExpCS_NavigationExpCS = Generalization(general=NavigationExpCS, specific=minioclcs_LoopExpCS)
gen_minioclcs_CollectExpCS_LoopExpCS = Generalization(general=LoopExpCS, specific=minioclcs_CollectExpCS)
gen_minioclcs_IteratorVarCS_CSTrace = Generalization(general=CSTrace, specific=minioclcs_IteratorVarCS)
gen_minioclcs_ConstraintsDefCS_CSTrace = Generalization(general=CSTrace, specific=minioclcs_ConstraintsDefCS)
gen_minioclcs_IterateExpCS_LoopExpCS = Generalization(general=LoopExpCS, specific=minioclcs_IterateExpCS)
gen_minioclcs_AccVarCS_CSTrace = Generalization(general=CSTrace, specific=minioclcs_AccVarCS)
gen_minioclcs_NameExpCS_PrimaryExpCS = Generalization(general=PrimaryExpCS, specific=minioclcs_NameExpCS)
gen_minioclcs_NameExpCS_NavigationExpCS = Generalization(general=NavigationExpCS, specific=minioclcs_NameExpCS)
gen_minioclcs_RoundedBracketClauseCS_CSTrace = Generalization(general=CSTrace, specific=minioclcs_RoundedBracketClauseCS)
gen_minioclcs_LiteralExpCS_PrimaryExpCS = Generalization(general=PrimaryExpCS, specific=minioclcs_LiteralExpCS)
gen_minioclcs_IntLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=minioclcs_IntLiteralExpCS)
gen_minioclcs_BooleanLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=minioclcs_BooleanLiteralExpCS)
gen_minioclcs_NullLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=minioclcs_NullLiteralExpCS)
gen_minioclcs_CollectionLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=minioclcs_CollectionLiteralExpCS)
gen_minioclcs_CollectionLiteralPartCS_CSTrace = Generalization(general=CSTrace, specific=minioclcs_CollectionLiteralPartCS)
gen_minioclcs_LetExpCS_PrimaryExpCS = Generalization(general=PrimaryExpCS, specific=minioclcs_LetExpCS)
gen_minioclcs_LetVarCS_CSTrace = Generalization(general=CSTrace, specific=minioclcs_LetVarCS)
gen_minioclcs_PathNameCS_CSTrace = Generalization(general=CSTrace, specific=minioclcs_PathNameCS)
gen_minioclcs_PathElementCS_CSTrace = Generalization(general=CSTrace, specific=minioclcs_PathElementCS)
gen_minioclcs_BooleanExpCS_BooleanLiteralExpCS = Generalization(general=BooleanLiteralExpCS, specific=minioclcs_BooleanExpCS)

# Domain Model
domain_model = DomainModel(
    name="minioclcs",
    types={minioclcs_RootCS, CSTrace, minioclcs_ImportCS, minioclcs_PackageCS, minioclcs_ConstraintsDefCS, minioclcs_ClassCS, minioclcs_PropertyCS, minioclcs_OperationCS, minioclcs_MultiplicityCS, minioclcs_ParameterCS, minioclcs_ExpCS, minioclcs_PathNameCS, minioclcs_InvariantCS, minioclcs_EqualityExpCS, ExpCS, minioclcs_CallExpCS, EqualityExpCS, minioclcs_NavigationExpCS, minioclcs_PrimaryExpCS, CallExpCS, minioclcs_SelfExpCS, PrimaryExpCS, minioclcs_LoopExpCS, NavigationExpCS, minioclcs_IteratorVarCS, minioclcs_CollectExpCS, LoopExpCS, minioclcs_IterateExpCS, minioclcs_AccVarCS, minioclcs_NameExpCS, minioclcs_RoundedBracketClauseCS, minioclcs_LiteralExpCS, minioclcs_IntLiteralExpCS, LiteralExpCS, minioclcs_BooleanLiteralExpCS, minioclcs_NullLiteralExpCS, minioclcs_CollectionLiteralExpCS, minioclcs_CollectionLiteralPartCS, minioclcs_LetExpCS, minioclcs_LetVarCS, minioclcs_PathElementCS, minioclcs_EClass, minioclcs_BooleanExpCS, BooleanLiteralExpCS, minioclcs_EObject, minioclcs_CSTrace, CollectionKindCS},
    associations={imports0, packages1, constraints3, packages6, classes8, properties12, operations14, typeRef16, multiplicity19, params21, resultRef23, body26, typeRef28, extends10, typeRef31, invariants34, exp36, left40, right41, source44, navExp46, itVar48, exp49, itType52, accVar55, accType56, accInitExp59, expName62, roundedBrackets64, args66, parts69, first70, last73, letVars76, inExp77, typeRef80, initExp83, pathElements86, elementName88, ast90},
    generalizations={gen_minioclcs_RootCS_CSTrace, gen_minioclcs_ImportCS_CSTrace, gen_minioclcs_PackageCS_CSTrace, gen_minioclcs_ClassCS_CSTrace, gen_minioclcs_PropertyCS_CSTrace, gen_minioclcs_MultiplicityCS_CSTrace, gen_minioclcs_OperationCS_CSTrace, gen_minioclcs_ParameterCS_CSTrace, gen_minioclcs_InvariantCS_CSTrace, gen_minioclcs_ExpCS_CSTrace, gen_minioclcs_EqualityExpCS_ExpCS, gen_minioclcs_CallExpCS_EqualityExpCS, gen_minioclcs_PrimaryExpCS_CallExpCS, gen_minioclcs_SelfExpCS_PrimaryExpCS, gen_minioclcs_NavigationExpCS_CSTrace, gen_minioclcs_LoopExpCS_NavigationExpCS, gen_minioclcs_CollectExpCS_LoopExpCS, gen_minioclcs_IteratorVarCS_CSTrace, gen_minioclcs_ConstraintsDefCS_CSTrace, gen_minioclcs_IterateExpCS_LoopExpCS, gen_minioclcs_AccVarCS_CSTrace, gen_minioclcs_NameExpCS_PrimaryExpCS, gen_minioclcs_NameExpCS_NavigationExpCS, gen_minioclcs_RoundedBracketClauseCS_CSTrace, gen_minioclcs_LiteralExpCS_PrimaryExpCS, gen_minioclcs_IntLiteralExpCS_LiteralExpCS, gen_minioclcs_BooleanLiteralExpCS_LiteralExpCS, gen_minioclcs_NullLiteralExpCS_LiteralExpCS, gen_minioclcs_CollectionLiteralExpCS_LiteralExpCS, gen_minioclcs_CollectionLiteralPartCS_CSTrace, gen_minioclcs_LetExpCS_PrimaryExpCS, gen_minioclcs_LetVarCS_CSTrace, gen_minioclcs_PathNameCS_CSTrace, gen_minioclcs_PathElementCS_CSTrace, gen_minioclcs_BooleanExpCS_BooleanLiteralExpCS},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)