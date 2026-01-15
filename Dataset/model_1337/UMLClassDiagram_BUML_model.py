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
PrimitiveDataType: Enumeration = Enumeration(
    name="PrimitiveDataType",
    literals={
            EnumerationLiteral(name="Boolean"),
			EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="String"),
			EnumerationLiteral(name="Double"),
			EnumerationLiteral(name="Date")
    }
)

VisbilityType: Enumeration = Enumeration(
    name="VisbilityType",
    literals={
            EnumerationLiteral(name="private"),
			EnumerationLiteral(name="public"),
			EnumerationLiteral(name="protected"),
			EnumerationLiteral(name="package")
    }
)

ScopeType: Enumeration = Enumeration(
    name="ScopeType",
    literals={
            EnumerationLiteral(name="instance"),
			EnumerationLiteral(name="classifier")
    }
)

OperatorType: Enumeration = Enumeration(
    name="OperatorType",
    literals={
            EnumerationLiteral(name="multiply"),
			EnumerationLiteral(name="divide"),
			EnumerationLiteral(name="module"),
			EnumerationLiteral(name="not"),
			EnumerationLiteral(name="or"),
			EnumerationLiteral(name="and"),
			EnumerationLiteral(name="lt"),
			EnumerationLiteral(name="lte"),
			EnumerationLiteral(name="gt"),
			EnumerationLiteral(name="gte"),
			EnumerationLiteral(name="equals"),
			EnumerationLiteral(name="distinct"),
			EnumerationLiteral(name="negative"),
			EnumerationLiteral(name="add"),
			EnumerationLiteral(name="subtract")
    }
)

# Classes
umlclassdiagram_PathNameCS = Class(name="umlclassdiagram::PathNameCS")
umlclassdiagram_PropertyCS = Class(name="umlclassdiagram::PropertyCS")
umlclassdiagram_RootCS = Class(name="umlclassdiagram::RootCS")
umlclassdiagram_PackageCS = Class(name="umlclassdiagram::PackageCS")
umlclassdiagram_ConstraintCS = Class(name="umlclassdiagram::ConstraintCS")
umlclassdiagram_ClassCS = Class(name="umlclassdiagram::ClassCS")
umlclassdiagram_CallExpCS = Class(name="umlclassdiagram::CallExpCS")
LogicExpCS = Class(name="LogicExpCS")
umlclassdiagram_OperationCS = Class(name="umlclassdiagram::OperationCS")
umlclassdiagram_ParameterCS = Class(name="umlclassdiagram::ParameterCS")
umlclassdiagram_ExpCS = Class(name="umlclassdiagram::ExpCS")
umlclassdiagram_InvariantCS = Class(name="umlclassdiagram::InvariantCS")
umlclassdiagram_LogicExpCS = Class(name="umlclassdiagram::LogicExpCS")
ExpCS = Class(name="ExpCS")
umlclassdiagram_NavigationExpCS = Class(name="umlclassdiagram::NavigationExpCS")
umlclassdiagram_PrimaryExpCS = Class(name="umlclassdiagram::PrimaryExpCS")
CallExpCS = Class(name="CallExpCS")
PrimaryExpCS = Class(name="PrimaryExpCS")
umlclassdiagram_NameExpCS = Class(name="umlclassdiagram::NameExpCS")
NavigationExpCS = Class(name="NavigationExpCS")
umlclassdiagram_RoundedBracketClauseCS = Class(name="umlclassdiagram::RoundedBracketClauseCS")
umlclassdiagram_LoopExpCS = Class(name="umlclassdiagram::LoopExpCS")
umlclassdiagram_IteratorVarCS = Class(name="umlclassdiagram::IteratorVarCS")
umlclassdiagram_CollectExpCS = Class(name="umlclassdiagram::CollectExpCS")
LoopExpCS = Class(name="LoopExpCS")
umlclassdiagram_IterateExpCS = Class(name="umlclassdiagram::IterateExpCS")
umlclassdiagram_AccVarCS = Class(name="umlclassdiagram::AccVarCS")
umlclassdiagram_NavigationPathCS = Class(name="umlclassdiagram::NavigationPathCS")
umlclassdiagram_LiteralExpCS = Class(name="umlclassdiagram::LiteralExpCS")
umlclassdiagram_IntLiteralExpCS = Class(name="umlclassdiagram::IntLiteralExpCS")
LiteralExpCS = Class(name="LiteralExpCS")
umlclassdiagram_StringLiteralExpCS = Class(name="umlclassdiagram::StringLiteralExpCS")
umlclassdiagram_BooleanLiteralExpCS = Class(name="umlclassdiagram::BooleanLiteralExpCS")
umlclassdiagram_PathCS = Class(name="umlclassdiagram::PathCS")
umlclassdiagram_PathVariableCS = Class(name="umlclassdiagram::PathVariableCS")
PathCS = Class(name="PathCS")
umlclassdiagram_PathElementCS = Class(name="umlclassdiagram::PathElementCS")
umlclassdiagram_Feature = Class(name="umlclassdiagram::Feature", is_abstract=True)
umlclassdiagram_BooleanExpCS = Class(name="umlclassdiagram::BooleanExpCS")
BooleanLiteralExpCS = Class(name="BooleanLiteralExpCS")
umlclassdiagram_ExistsExpCS = Class(name="umlclassdiagram::ExistsExpCS")
umlclassdiagram_NavigationNameExpCS = Class(name="umlclassdiagram::NavigationNameExpCS")
umlclassdiagram_NavigationPathNameCS = Class(name="umlclassdiagram::NavigationPathNameCS")
umlclassdiagram_Modifier = Class(name="umlclassdiagram::Modifier", is_abstract=True)
umlclassdiagram_NavigationPathVariableCS = Class(name="umlclassdiagram::NavigationPathVariableCS")
NavigationPathCS = Class(name="NavigationPathCS")
umlclassdiagram_NavigationPathElementCS = Class(name="umlclassdiagram::NavigationPathElementCS")
umlclassdiagram_ForAllExpCS = Class(name="umlclassdiagram::ForAllExpCS")
umlclassdiagram_ClassDiagram = Class(name="umlclassdiagram::ClassDiagram")
umlclassdiagram_Classifier = Class(name="umlclassdiagram::Classifier", is_abstract=True)
umlclassdiagram_Relation = Class(name="umlclassdiagram::Relation", is_abstract=True)
umlclassdiagram_PrimitiveElement = Class(name="umlclassdiagram::PrimitiveElement")
umlclassdiagram_Constraint = Class(name="umlclassdiagram::Constraint")
umlclassdiagram_NamedElement = Class(name="umlclassdiagram::NamedElement", is_abstract=True)
NamedElement = Class(name="NamedElement")
umlclassdiagram_Parameter = Class(name="umlclassdiagram::Parameter")
umlclassdiagram_Operation = Class(name="umlclassdiagram::Operation")
umlclassdiagram_Operator = Class(name="umlclassdiagram::Operator")
Modifier = Class(name="Modifier")
umlclassdiagram_Class = Class(name="umlclassdiagram::Class")
Classifier = Class(name="Classifier")
umlclassdiagram_Attribute = Class(name="umlclassdiagram::Attribute")
Feature = Class(name="Feature")
umlclassdiagram_Dependency = Class(name="umlclassdiagram::Dependency")
Relation = Class(name="Relation")
umlclassdiagram_Association = Class(name="umlclassdiagram::Association")
umlclassdiagram_Aggregation = Class(name="umlclassdiagram::Aggregation")
umlclassdiagram_Composition = Class(name="umlclassdiagram::Composition")
umlclassdiagram_AssociationClass = Class(name="umlclassdiagram::AssociationClass")

# umlclassdiagram_PathNameCS class attributes and methods

# umlclassdiagram_PropertyCS class attributes and methods
umlclassdiagram_PropertyCS_name: Property = Property(name="name", type=StringType)
umlclassdiagram_PropertyCS.attributes={umlclassdiagram_PropertyCS_name}

# umlclassdiagram_RootCS class attributes and methods

# umlclassdiagram_PackageCS class attributes and methods
umlclassdiagram_PackageCS_name: Property = Property(name="name", type=StringType)
umlclassdiagram_PackageCS.attributes={umlclassdiagram_PackageCS_name}

# umlclassdiagram_ConstraintCS class attributes and methods

# umlclassdiagram_ClassCS class attributes and methods
umlclassdiagram_ClassCS_name: Property = Property(name="name", type=StringType)
umlclassdiagram_ClassCS.attributes={umlclassdiagram_ClassCS_name}

# umlclassdiagram_CallExpCS class attributes and methods

# LogicExpCS class attributes and methods

# umlclassdiagram_OperationCS class attributes and methods
umlclassdiagram_OperationCS_name: Property = Property(name="name", type=StringType)
umlclassdiagram_OperationCS.attributes={umlclassdiagram_OperationCS_name}

# umlclassdiagram_ParameterCS class attributes and methods
umlclassdiagram_ParameterCS_name: Property = Property(name="name", type=StringType)
umlclassdiagram_ParameterCS.attributes={umlclassdiagram_ParameterCS_name}

# umlclassdiagram_ExpCS class attributes and methods

# umlclassdiagram_InvariantCS class attributes and methods

# umlclassdiagram_LogicExpCS class attributes and methods
umlclassdiagram_LogicExpCS_op: Property = Property(name="op", type=StringType)
umlclassdiagram_LogicExpCS.attributes={umlclassdiagram_LogicExpCS_op}

# ExpCS class attributes and methods

# umlclassdiagram_NavigationExpCS class attributes and methods

# umlclassdiagram_PrimaryExpCS class attributes and methods

# CallExpCS class attributes and methods

# PrimaryExpCS class attributes and methods

# umlclassdiagram_NameExpCS class attributes and methods

# NavigationExpCS class attributes and methods

# umlclassdiagram_RoundedBracketClauseCS class attributes and methods

# umlclassdiagram_LoopExpCS class attributes and methods
umlclassdiagram_LoopExpCS_logicOp: Property = Property(name="logicOp", type=StringType)
umlclassdiagram_LoopExpCS.attributes={umlclassdiagram_LoopExpCS_logicOp}

# umlclassdiagram_IteratorVarCS class attributes and methods
umlclassdiagram_IteratorVarCS_itName: Property = Property(name="itName", type=StringType)
umlclassdiagram_IteratorVarCS.attributes={umlclassdiagram_IteratorVarCS_itName}

# umlclassdiagram_CollectExpCS class attributes and methods

# LoopExpCS class attributes and methods

# umlclassdiagram_IterateExpCS class attributes and methods

# umlclassdiagram_AccVarCS class attributes and methods
umlclassdiagram_AccVarCS_accVarName: Property = Property(name="accVarName", type=StringType)
umlclassdiagram_AccVarCS.attributes={umlclassdiagram_AccVarCS_accVarName}

# umlclassdiagram_NavigationPathCS class attributes and methods

# umlclassdiagram_LiteralExpCS class attributes and methods

# umlclassdiagram_IntLiteralExpCS class attributes and methods
umlclassdiagram_IntLiteralExpCS_intSymbol: Property = Property(name="intSymbol", type=IntegerType)
umlclassdiagram_IntLiteralExpCS.attributes={umlclassdiagram_IntLiteralExpCS_intSymbol}

# LiteralExpCS class attributes and methods

# umlclassdiagram_StringLiteralExpCS class attributes and methods
umlclassdiagram_StringLiteralExpCS_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
umlclassdiagram_StringLiteralExpCS.attributes={umlclassdiagram_StringLiteralExpCS_stringSymbol}

# umlclassdiagram_BooleanLiteralExpCS class attributes and methods

# umlclassdiagram_PathCS class attributes and methods

# umlclassdiagram_PathVariableCS class attributes and methods
umlclassdiagram_PathVariableCS_varName: Property = Property(name="varName", type=StringType)
umlclassdiagram_PathVariableCS.attributes={umlclassdiagram_PathVariableCS_varName}

# PathCS class attributes and methods

# umlclassdiagram_PathElementCS class attributes and methods

# umlclassdiagram_Feature class attributes and methods
umlclassdiagram_Feature_name: Property = Property(name="name", type=StringType)
umlclassdiagram_Feature_visibility: Property = Property(name="visibility", type=StringType)
umlclassdiagram_Feature_scope: Property = Property(name="scope", type=StringType)
umlclassdiagram_Feature.attributes={umlclassdiagram_Feature_name, umlclassdiagram_Feature_scope, umlclassdiagram_Feature_visibility}

# umlclassdiagram_BooleanExpCS class attributes and methods
umlclassdiagram_BooleanExpCS_boolSymbol: Property = Property(name="boolSymbol", type=BooleanType)
umlclassdiagram_BooleanExpCS.attributes={umlclassdiagram_BooleanExpCS_boolSymbol}

# BooleanLiteralExpCS class attributes and methods

# umlclassdiagram_ExistsExpCS class attributes and methods

# umlclassdiagram_NavigationNameExpCS class attributes and methods

# umlclassdiagram_NavigationPathNameCS class attributes and methods

# umlclassdiagram_Modifier class attributes and methods
umlclassdiagram_Modifier_visibility: Property = Property(name="visibility", type=StringType)
umlclassdiagram_Modifier_scope: Property = Property(name="scope", type=StringType)
umlclassdiagram_Modifier.attributes={umlclassdiagram_Modifier_scope, umlclassdiagram_Modifier_visibility}

# umlclassdiagram_NavigationPathVariableCS class attributes and methods
umlclassdiagram_NavigationPathVariableCS_varName: Property = Property(name="varName", type=StringType)
umlclassdiagram_NavigationPathVariableCS.attributes={umlclassdiagram_NavigationPathVariableCS_varName}

# NavigationPathCS class attributes and methods

# umlclassdiagram_NavigationPathElementCS class attributes and methods

# umlclassdiagram_ForAllExpCS class attributes and methods

# umlclassdiagram_ClassDiagram class attributes and methods

# umlclassdiagram_Classifier class attributes and methods
umlclassdiagram_Classifier_abstract: Property = Property(name="abstract", type=BooleanType)
umlclassdiagram_Classifier_derived: Property = Property(name="derived", type=BooleanType)
umlclassdiagram_Classifier.attributes={umlclassdiagram_Classifier_abstract, umlclassdiagram_Classifier_derived}

# umlclassdiagram_Relation class attributes and methods
umlclassdiagram_Relation_nsrc: Property = Property(name="nsrc", type=StringType)
umlclassdiagram_Relation_ntar: Property = Property(name="ntar", type=StringType)
umlclassdiagram_Relation_derived: Property = Property(name="derived", type=BooleanType)
umlclassdiagram_Relation.attributes={umlclassdiagram_Relation_ntar, umlclassdiagram_Relation_derived, umlclassdiagram_Relation_nsrc}

# umlclassdiagram_PrimitiveElement class attributes and methods
umlclassdiagram_PrimitiveElement_type: Property = Property(name="type", type=StringType)
umlclassdiagram_PrimitiveElement.attributes={umlclassdiagram_PrimitiveElement_type}

# umlclassdiagram_Constraint class attributes and methods
umlclassdiagram_Constraint_id: Property = Property(name="id", type=StringType)
umlclassdiagram_Constraint.attributes={umlclassdiagram_Constraint_id}

# umlclassdiagram_NamedElement class attributes and methods
umlclassdiagram_NamedElement_name: Property = Property(name="name", type=StringType)
umlclassdiagram_NamedElement.attributes={umlclassdiagram_NamedElement_name}

# NamedElement class attributes and methods

# umlclassdiagram_Parameter class attributes and methods

# umlclassdiagram_Operation class attributes and methods

# umlclassdiagram_Operator class attributes and methods
umlclassdiagram_Operator_operator: Property = Property(name="operator", type=StringType)
umlclassdiagram_Operator.attributes={umlclassdiagram_Operator_operator}

# Modifier class attributes and methods

# umlclassdiagram_Class class attributes and methods

# Classifier class attributes and methods

# umlclassdiagram_Attribute class attributes and methods
umlclassdiagram_Attribute_derived: Property = Property(name="derived", type=BooleanType)
umlclassdiagram_Attribute.attributes={umlclassdiagram_Attribute_derived}

# Feature class attributes and methods

# umlclassdiagram_Dependency class attributes and methods

# Relation class attributes and methods

# umlclassdiagram_Association class attributes and methods

# umlclassdiagram_Aggregation class attributes and methods

# umlclassdiagram_Composition class attributes and methods

# umlclassdiagram_AssociationClass class attributes and methods

# Relationships
extends8: BinaryAssociation = BinaryAssociation(
    name="extends8",
    ends={
        Property(name="umlclassdiagram_PathNameCS", type=umlclassdiagram_ClassCS, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_ClassCS9", type=umlclassdiagram_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties10: BinaryAssociation = BinaryAssociation(
    name="properties10",
    ends={
        Property(name="umlclassdiagram_PropertyCS", type=umlclassdiagram_ClassCS, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_ClassCS11", type=umlclassdiagram_PropertyCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packages0: BinaryAssociation = BinaryAssociation(
    name="packages0",
    ends={
        Property(name="umlclassdiagram_PackageCS", type=umlclassdiagram_RootCS, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_RootCS", type=umlclassdiagram_PackageCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints1: BinaryAssociation = BinaryAssociation(
    name="constraints1",
    ends={
        Property(name="umlclassdiagram_ConstraintCS", type=umlclassdiagram_RootCS, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_RootCS2", type=umlclassdiagram_ConstraintCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packages4: BinaryAssociation = BinaryAssociation(
    name="packages4",
    ends={
        Property(name="umlclassdiagram_PackageCS5", type=umlclassdiagram_PackageCS, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_PackageCS3", type=umlclassdiagram_PackageCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classes6: BinaryAssociation = BinaryAssociation(
    name="classes6",
    ends={
        Property(name="umlclassdiagram_ClassCS", type=umlclassdiagram_PackageCS, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_PackageCS7", type=umlclassdiagram_ClassCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
right37: BinaryAssociation = BinaryAssociation(
    name="right37",
    ends={
        Property(name="umlclassdiagram_CallExpCS", type=umlclassdiagram_LogicExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_LogicExpCS38", type=umlclassdiagram_CallExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source40: BinaryAssociation = BinaryAssociation(
    name="source40",
    ends={
        Property(name="umlclassdiagram_CallExpCS41", type=umlclassdiagram_CallExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_CallExpCS39", type=umlclassdiagram_CallExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operations12: BinaryAssociation = BinaryAssociation(
    name="operations12",
    ends={
        Property(name="umlclassdiagram_OperationCS", type=umlclassdiagram_ClassCS, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_ClassCS13", type=umlclassdiagram_OperationCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeRef14: BinaryAssociation = BinaryAssociation(
    name="typeRef14",
    ends={
        Property(name="umlclassdiagram_PathNameCS16", type=umlclassdiagram_PropertyCS, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_PropertyCS15", type=umlclassdiagram_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
params17: BinaryAssociation = BinaryAssociation(
    name="params17",
    ends={
        Property(name="umlclassdiagram_ParameterCS", type=umlclassdiagram_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_OperationCS18", type=umlclassdiagram_ParameterCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resultRef19: BinaryAssociation = BinaryAssociation(
    name="resultRef19",
    ends={
        Property(name="umlclassdiagram_PathNameCS21", type=umlclassdiagram_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_OperationCS20", type=umlclassdiagram_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body22: BinaryAssociation = BinaryAssociation(
    name="body22",
    ends={
        Property(name="umlclassdiagram_ExpCS", type=umlclassdiagram_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_OperationCS23", type=umlclassdiagram_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeRef24: BinaryAssociation = BinaryAssociation(
    name="typeRef24",
    ends={
        Property(name="umlclassdiagram_PathNameCS26", type=umlclassdiagram_ParameterCS, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_ParameterCS25", type=umlclassdiagram_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeRef27: BinaryAssociation = BinaryAssociation(
    name="typeRef27",
    ends={
        Property(name="umlclassdiagram_PathNameCS29", type=umlclassdiagram_ConstraintCS, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_ConstraintCS28", type=umlclassdiagram_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
invariants30: BinaryAssociation = BinaryAssociation(
    name="invariants30",
    ends={
        Property(name="umlclassdiagram_InvariantCS", type=umlclassdiagram_ConstraintCS, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_ConstraintCS31", type=umlclassdiagram_InvariantCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp32: BinaryAssociation = BinaryAssociation(
    name="exp32",
    ends={
        Property(name="umlclassdiagram_ExpCS34", type=umlclassdiagram_InvariantCS, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_InvariantCS33", type=umlclassdiagram_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left36: BinaryAssociation = BinaryAssociation(
    name="left36",
    ends={
        Property(name="umlclassdiagram_LogicExpCS", type=umlclassdiagram_LogicExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_LogicExpCS35", type=umlclassdiagram_LogicExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accType59: BinaryAssociation = BinaryAssociation(
    name="accType59",
    ends={
        Property(name="umlclassdiagram_PathNameCS61", type=umlclassdiagram_AccVarCS, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_AccVarCS60", type=umlclassdiagram_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accInitExp62: BinaryAssociation = BinaryAssociation(
    name="accInitExp62",
    ends={
        Property(name="umlclassdiagram_ExpCS64", type=umlclassdiagram_AccVarCS, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_AccVarCS63", type=umlclassdiagram_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
navExp42: BinaryAssociation = BinaryAssociation(
    name="navExp42",
    ends={
        Property(name="umlclassdiagram_NavigationExpCS", type=umlclassdiagram_CallExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_CallExpCS43", type=umlclassdiagram_NavigationExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expName44: BinaryAssociation = BinaryAssociation(
    name="expName44",
    ends={
        Property(name="umlclassdiagram_PathNameCS45", type=umlclassdiagram_NameExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_NameExpCS", type=umlclassdiagram_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
roundedBrackets46: BinaryAssociation = BinaryAssociation(
    name="roundedBrackets46",
    ends={
        Property(name="umlclassdiagram_RoundedBracketClauseCS", type=umlclassdiagram_NameExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_NameExpCS47", type=umlclassdiagram_RoundedBracketClauseCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
callExp48: BinaryAssociation = BinaryAssociation(
    name="callExp48",
    ends={
        Property(name="umlclassdiagram_CallExpCS50", type=umlclassdiagram_NameExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_NameExpCS49", type=umlclassdiagram_CallExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
itVar51: BinaryAssociation = BinaryAssociation(
    name="itVar51",
    ends={
        Property(name="umlclassdiagram_IteratorVarCS", type=umlclassdiagram_LoopExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_LoopExpCS", type=umlclassdiagram_IteratorVarCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp52: BinaryAssociation = BinaryAssociation(
    name="exp52",
    ends={
        Property(name="umlclassdiagram_ExpCS54", type=umlclassdiagram_LoopExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_LoopExpCS53", type=umlclassdiagram_ExpCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
itType55: BinaryAssociation = BinaryAssociation(
    name="itType55",
    ends={
        Property(name="umlclassdiagram_PathNameCS57", type=umlclassdiagram_IteratorVarCS, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_IteratorVarCS56", type=umlclassdiagram_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accVar58: BinaryAssociation = BinaryAssociation(
    name="accVar58",
    ends={
        Property(name="umlclassdiagram_AccVarCS", type=umlclassdiagram_IterateExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_IterateExpCS", type=umlclassdiagram_AccVarCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expName73: BinaryAssociation = BinaryAssociation(
    name="expName73",
    ends={
        Property(name="umlclassdiagram_NavigationNameExpCS", type=umlclassdiagram_NavigationPathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="umlclassdiagram_NavigationPathNameCS", type=umlclassdiagram_NavigationNameExpCS, multiplicity=Multiplicity(1, 1))
    }
)
roundedBrackets74: BinaryAssociation = BinaryAssociation(
    name="roundedBrackets74",
    ends={
        Property(name="umlclassdiagram_RoundedBracketClauseCS76", type=umlclassdiagram_NavigationNameExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_NavigationNameExpCS75", type=umlclassdiagram_RoundedBracketClauseCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
callExp77: BinaryAssociation = BinaryAssociation(
    name="callExp77",
    ends={
        Property(name="umlclassdiagram_CallExpCS79", type=umlclassdiagram_NavigationNameExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_NavigationNameExpCS78", type=umlclassdiagram_CallExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args65: BinaryAssociation = BinaryAssociation(
    name="args65",
    ends={
        Property(name="umlclassdiagram_ExpCS67", type=umlclassdiagram_RoundedBracketClauseCS, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_RoundedBracketClauseCS66", type=umlclassdiagram_ExpCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
path68: BinaryAssociation = BinaryAssociation(
    name="path68",
    ends={
        Property(name="umlclassdiagram_PathCS", type=umlclassdiagram_PathNameCS, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_PathNameCS69", type=umlclassdiagram_PathCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pathName70: BinaryAssociation = BinaryAssociation(
    name="pathName70",
    ends={
        Property(name="umlclassdiagram_Feature", type=umlclassdiagram_PathElementCS, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_PathElementCS", type=umlclassdiagram_Feature, multiplicity=Multiplicity(0, 1))
    }
)
accVars71: BinaryAssociation = BinaryAssociation(
    name="accVars71",
    ends={
        Property(name="umlclassdiagram_AccVarCS72", type=umlclassdiagram_ExistsExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_ExistsExpCS", type=umlclassdiagram_AccVarCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type94: BinaryAssociation = BinaryAssociation(
    name="type94",
    ends={
        Property(name="umlclassdiagram_NamedElement96", type=umlclassdiagram_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_Feature95", type=umlclassdiagram_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
path80: BinaryAssociation = BinaryAssociation(
    name="path80",
    ends={
        Property(name="umlclassdiagram_NavigationPathCS", type=umlclassdiagram_NavigationPathNameCS, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_NavigationPathNameCS81", type=umlclassdiagram_NavigationPathCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pathName82: BinaryAssociation = BinaryAssociation(
    name="pathName82",
    ends={
        Property(name="umlclassdiagram_Feature83", type=umlclassdiagram_NavigationPathElementCS, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_NavigationPathElementCS", type=umlclassdiagram_Feature, multiplicity=Multiplicity(0, 1))
    }
)
accVars84: BinaryAssociation = BinaryAssociation(
    name="accVars84",
    ends={
        Property(name="umlclassdiagram_AccVarCS85", type=umlclassdiagram_ForAllExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_ForAllExpCS", type=umlclassdiagram_AccVarCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classes86: BinaryAssociation = BinaryAssociation(
    name="classes86",
    ends={
        Property(name="umlclassdiagram_Classifier", type=umlclassdiagram_ClassDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_ClassDiagram", type=umlclassdiagram_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations87: BinaryAssociation = BinaryAssociation(
    name="relations87",
    ends={
        Property(name="umlclassdiagram_Relation", type=umlclassdiagram_ClassDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_ClassDiagram88", type=umlclassdiagram_Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types89: BinaryAssociation = BinaryAssociation(
    name="types89",
    ends={
        Property(name="umlclassdiagram_PrimitiveElement", type=umlclassdiagram_ClassDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_ClassDiagram90", type=umlclassdiagram_PrimitiveElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints91: BinaryAssociation = BinaryAssociation(
    name="constraints91",
    ends={
        Property(name="umlclassdiagram_Constraint", type=umlclassdiagram_ClassDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_ClassDiagram92", type=umlclassdiagram_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type93: BinaryAssociation = BinaryAssociation(
    name="type93",
    ends={
        Property(name="umlclassdiagram_NamedElement", type=umlclassdiagram_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_Parameter", type=umlclassdiagram_NamedElement, multiplicity=Multiplicity(1, 1))
    }
)
params111: BinaryAssociation = BinaryAssociation(
    name="params111",
    ends={
        Property(name="umlclassdiagram_Parameter112", type=umlclassdiagram_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_Operation", type=umlclassdiagram_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operators113: BinaryAssociation = BinaryAssociation(
    name="operators113",
    ends={
        Property(name="umlclassdiagram_Operator", type=umlclassdiagram_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_Operation114", type=umlclassdiagram_Operator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
src115: BinaryAssociation = BinaryAssociation(
    name="src115",
    ends={
        Property(name="umlclassdiagram_Classifier117", type=umlclassdiagram_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_Relation116", type=umlclassdiagram_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
features97: BinaryAssociation = BinaryAssociation(
    name="features97",
    ends={
        Property(name="umlclassdiagram_Feature99", type=umlclassdiagram_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_Classifier98", type=umlclassdiagram_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
super100: BinaryAssociation = BinaryAssociation(
    name="super100",
    ends={
        Property(name="umlclassdiagram_Class", type=umlclassdiagram_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_Classifier101", type=umlclassdiagram_Class, multiplicity=Multiplicity(0, 9999))
    }
)
supplier102: BinaryAssociation = BinaryAssociation(
    name="supplier102",
    ends={
        Property(name="umlclassdiagram_Class104", type=umlclassdiagram_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_Classifier103", type=umlclassdiagram_Class, multiplicity=Multiplicity(0, 9999))
    }
)
type105: BinaryAssociation = BinaryAssociation(
    name="type105",
    ends={
        Property(name="umlclassdiagram_Class107", type=umlclassdiagram_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_Constraint106", type=umlclassdiagram_Class, multiplicity=Multiplicity(1, 1))
    }
)
expressions108: BinaryAssociation = BinaryAssociation(
    name="expressions108",
    ends={
        Property(name="umlclassdiagram_RootCS110", type=umlclassdiagram_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_Constraint109", type=umlclassdiagram_RootCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tar118: BinaryAssociation = BinaryAssociation(
    name="tar118",
    ends={
        Property(name="umlclassdiagram_Classifier120", type=umlclassdiagram_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_Relation119", type=umlclassdiagram_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
association121: BinaryAssociation = BinaryAssociation(
    name="association121",
    ends={
        Property(name="umlclassdiagram_Association", type=umlclassdiagram_AssociationClass, multiplicity=Multiplicity(1, 1)),
        Property(name="umlclassdiagram_AssociationClass", type=umlclassdiagram_Association, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_umlclassdiagram_CallExpCS_LogicExpCS = Generalization(general=LogicExpCS, specific=umlclassdiagram_CallExpCS)
gen_umlclassdiagram_LogicExpCS_ExpCS = Generalization(general=ExpCS, specific=umlclassdiagram_LogicExpCS)
gen_umlclassdiagram_PrimaryExpCS_CallExpCS = Generalization(general=CallExpCS, specific=umlclassdiagram_PrimaryExpCS)
gen_umlclassdiagram_NavigationExpCS_PrimaryExpCS = Generalization(general=PrimaryExpCS, specific=umlclassdiagram_NavigationExpCS)
gen_umlclassdiagram_NameExpCS_NavigationExpCS = Generalization(general=NavigationExpCS, specific=umlclassdiagram_NameExpCS)
gen_umlclassdiagram_LoopExpCS_NavigationExpCS = Generalization(general=NavigationExpCS, specific=umlclassdiagram_LoopExpCS)
gen_umlclassdiagram_CollectExpCS_LoopExpCS = Generalization(general=LoopExpCS, specific=umlclassdiagram_CollectExpCS)
gen_umlclassdiagram_IterateExpCS_LoopExpCS = Generalization(general=LoopExpCS, specific=umlclassdiagram_IterateExpCS)
gen_umlclassdiagram_LiteralExpCS_PrimaryExpCS = Generalization(general=PrimaryExpCS, specific=umlclassdiagram_LiteralExpCS)
gen_umlclassdiagram_IntLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=umlclassdiagram_IntLiteralExpCS)
gen_umlclassdiagram_StringLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=umlclassdiagram_StringLiteralExpCS)
gen_umlclassdiagram_BooleanLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=umlclassdiagram_BooleanLiteralExpCS)
gen_umlclassdiagram_PathVariableCS_PathCS = Generalization(general=PathCS, specific=umlclassdiagram_PathVariableCS)
gen_umlclassdiagram_PathElementCS_PathCS = Generalization(general=PathCS, specific=umlclassdiagram_PathElementCS)
gen_umlclassdiagram_BooleanExpCS_BooleanLiteralExpCS = Generalization(general=BooleanLiteralExpCS, specific=umlclassdiagram_BooleanExpCS)
gen_umlclassdiagram_ExistsExpCS_LoopExpCS = Generalization(general=LoopExpCS, specific=umlclassdiagram_ExistsExpCS)
gen_umlclassdiagram_NavigationNameExpCS_NavigationExpCS = Generalization(general=NavigationExpCS, specific=umlclassdiagram_NavigationNameExpCS)
gen_umlclassdiagram_Modifier_NamedElement = Generalization(general=NamedElement, specific=umlclassdiagram_Modifier)
gen_umlclassdiagram_NavigationPathVariableCS_NavigationPathCS = Generalization(general=NavigationPathCS, specific=umlclassdiagram_NavigationPathVariableCS)
gen_umlclassdiagram_NavigationPathElementCS_NavigationPathCS = Generalization(general=NavigationPathCS, specific=umlclassdiagram_NavigationPathElementCS)
gen_umlclassdiagram_ForAllExpCS_LoopExpCS = Generalization(general=LoopExpCS, specific=umlclassdiagram_ForAllExpCS)
gen_umlclassdiagram_PrimitiveElement_NamedElement = Generalization(general=NamedElement, specific=umlclassdiagram_PrimitiveElement)
gen_umlclassdiagram_Parameter_NamedElement = Generalization(general=NamedElement, specific=umlclassdiagram_Parameter)
gen_umlclassdiagram_Operation_Feature = Generalization(general=Feature, specific=umlclassdiagram_Operation)
gen_umlclassdiagram_Relation_Modifier = Generalization(general=Modifier, specific=umlclassdiagram_Relation)
gen_umlclassdiagram_Classifier_Modifier = Generalization(general=Modifier, specific=umlclassdiagram_Classifier)
gen_umlclassdiagram_Class_Classifier = Generalization(general=Classifier, specific=umlclassdiagram_Class)
gen_umlclassdiagram_Attribute_Feature = Generalization(general=Feature, specific=umlclassdiagram_Attribute)
gen_umlclassdiagram_Dependency_Relation = Generalization(general=Relation, specific=umlclassdiagram_Dependency)
gen_umlclassdiagram_Association_Relation = Generalization(general=Relation, specific=umlclassdiagram_Association)
gen_umlclassdiagram_Aggregation_Relation = Generalization(general=Relation, specific=umlclassdiagram_Aggregation)
gen_umlclassdiagram_Composition_Relation = Generalization(general=Relation, specific=umlclassdiagram_Composition)
gen_umlclassdiagram_AssociationClass_Classifier = Generalization(general=Classifier, specific=umlclassdiagram_AssociationClass)

# Domain Model
domain_model = DomainModel(
    name="umlclassdiagram",
    types={umlclassdiagram_PathNameCS, umlclassdiagram_PropertyCS, umlclassdiagram_RootCS, umlclassdiagram_PackageCS, umlclassdiagram_ConstraintCS, umlclassdiagram_ClassCS, umlclassdiagram_CallExpCS, LogicExpCS, umlclassdiagram_OperationCS, umlclassdiagram_ParameterCS, umlclassdiagram_ExpCS, umlclassdiagram_InvariantCS, umlclassdiagram_LogicExpCS, ExpCS, umlclassdiagram_NavigationExpCS, umlclassdiagram_PrimaryExpCS, CallExpCS, PrimaryExpCS, umlclassdiagram_NameExpCS, NavigationExpCS, umlclassdiagram_RoundedBracketClauseCS, umlclassdiagram_LoopExpCS, umlclassdiagram_IteratorVarCS, umlclassdiagram_CollectExpCS, LoopExpCS, umlclassdiagram_IterateExpCS, umlclassdiagram_AccVarCS, umlclassdiagram_NavigationPathCS, umlclassdiagram_LiteralExpCS, umlclassdiagram_IntLiteralExpCS, LiteralExpCS, umlclassdiagram_StringLiteralExpCS, umlclassdiagram_BooleanLiteralExpCS, umlclassdiagram_PathCS, umlclassdiagram_PathVariableCS, PathCS, umlclassdiagram_PathElementCS, umlclassdiagram_Feature, umlclassdiagram_BooleanExpCS, BooleanLiteralExpCS, umlclassdiagram_ExistsExpCS, umlclassdiagram_NavigationNameExpCS, umlclassdiagram_NavigationPathNameCS, umlclassdiagram_Modifier, umlclassdiagram_NavigationPathVariableCS, NavigationPathCS, umlclassdiagram_NavigationPathElementCS, umlclassdiagram_ForAllExpCS, umlclassdiagram_ClassDiagram, umlclassdiagram_Classifier, umlclassdiagram_Relation, umlclassdiagram_PrimitiveElement, umlclassdiagram_Constraint, umlclassdiagram_NamedElement, NamedElement, umlclassdiagram_Parameter, umlclassdiagram_Operation, umlclassdiagram_Operator, Modifier, umlclassdiagram_Class, Classifier, umlclassdiagram_Attribute, Feature, umlclassdiagram_Dependency, Relation, umlclassdiagram_Association, umlclassdiagram_Aggregation, umlclassdiagram_Composition, umlclassdiagram_AssociationClass, PrimitiveDataType, VisbilityType, ScopeType, OperatorType},
    associations={extends8, properties10, packages0, constraints1, packages4, classes6, right37, source40, operations12, typeRef14, params17, resultRef19, body22, typeRef24, typeRef27, invariants30, exp32, left36, accType59, accInitExp62, navExp42, expName44, roundedBrackets46, callExp48, itVar51, exp52, itType55, accVar58, expName73, roundedBrackets74, callExp77, args65, path68, pathName70, accVars71, type94, path80, pathName82, accVars84, classes86, relations87, types89, constraints91, type93, params111, operators113, src115, features97, super100, supplier102, type105, expressions108, tar118, association121},
    generalizations={gen_umlclassdiagram_CallExpCS_LogicExpCS, gen_umlclassdiagram_LogicExpCS_ExpCS, gen_umlclassdiagram_PrimaryExpCS_CallExpCS, gen_umlclassdiagram_NavigationExpCS_PrimaryExpCS, gen_umlclassdiagram_NameExpCS_NavigationExpCS, gen_umlclassdiagram_LoopExpCS_NavigationExpCS, gen_umlclassdiagram_CollectExpCS_LoopExpCS, gen_umlclassdiagram_IterateExpCS_LoopExpCS, gen_umlclassdiagram_LiteralExpCS_PrimaryExpCS, gen_umlclassdiagram_IntLiteralExpCS_LiteralExpCS, gen_umlclassdiagram_StringLiteralExpCS_LiteralExpCS, gen_umlclassdiagram_BooleanLiteralExpCS_LiteralExpCS, gen_umlclassdiagram_PathVariableCS_PathCS, gen_umlclassdiagram_PathElementCS_PathCS, gen_umlclassdiagram_BooleanExpCS_BooleanLiteralExpCS, gen_umlclassdiagram_ExistsExpCS_LoopExpCS, gen_umlclassdiagram_NavigationNameExpCS_NavigationExpCS, gen_umlclassdiagram_Modifier_NamedElement, gen_umlclassdiagram_NavigationPathVariableCS_NavigationPathCS, gen_umlclassdiagram_NavigationPathElementCS_NavigationPathCS, gen_umlclassdiagram_ForAllExpCS_LoopExpCS, gen_umlclassdiagram_PrimitiveElement_NamedElement, gen_umlclassdiagram_Parameter_NamedElement, gen_umlclassdiagram_Operation_Feature, gen_umlclassdiagram_Relation_Modifier, gen_umlclassdiagram_Classifier_Modifier, gen_umlclassdiagram_Class_Classifier, gen_umlclassdiagram_Attribute_Feature, gen_umlclassdiagram_Dependency_Relation, gen_umlclassdiagram_Association_Relation, gen_umlclassdiagram_Aggregation_Relation, gen_umlclassdiagram_Composition_Relation, gen_umlclassdiagram_AssociationClass_Classifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)