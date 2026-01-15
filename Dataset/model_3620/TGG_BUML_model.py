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
tgg_TripleGraphGrammarFile = Class(name="tgg::TripleGraphGrammarFile")
tgg_Import = Class(name="tgg::Import")
tgg_Using = Class(name="tgg::Using")
tgg_Schema = Class(name="tgg::Schema")
tgg_Rule = Class(name="tgg::Rule")
tgg_ComplementRule = Class(name="tgg::ComplementRule")
tgg_Nac = Class(name="tgg::Nac")
tgg_AttrCondDefLibrary = Class(name="tgg::AttrCondDefLibrary")
NamedElements = Class(name="NamedElements")
tgg_EPackage = Class(name="tgg::EPackage")
tgg_CorrType = Class(name="tgg::CorrType")
tgg_AttrCondDef = Class(name="tgg::AttrCondDef")
tgg_EClass = Class(name="tgg::EClass")
tgg_Param = Class(name="tgg::Param")
tgg_Adornment = Class(name="tgg::Adornment")
tgg_EDataType = Class(name="tgg::EDataType")
tgg_ObjectVariablePattern = Class(name="tgg::ObjectVariablePattern")
tgg_CorrVariablePattern = Class(name="tgg::CorrVariablePattern")
tgg_AttrCond = Class(name="tgg::AttrCond")
tgg_LocalVariable = Class(name="tgg::LocalVariable")
ParamValue = Class(name="ParamValue")
NamePattern = Class(name="NamePattern")
tgg_AttributeAssignment = Class(name="tgg::AttributeAssignment")
tgg_AttributeConstraint = Class(name="tgg::AttributeConstraint")
tgg_LinkVariablePattern = Class(name="tgg::LinkVariablePattern")
tgg_ContextObjectVariablePattern = Class(name="tgg::ContextObjectVariablePattern")
tgg_ContextLinkVariablePattern = Class(name="tgg::ContextLinkVariablePattern")
tgg_EAttribute = Class(name="tgg::EAttribute")
tgg_ParamValue = Class(name="tgg::ParamValue")
tgg_EnumExpression = Class(name="tgg::EnumExpression")
Expression = Class(name="Expression")
tgg_EEnum = Class(name="tgg::EEnum")
tgg_EEnumLiteral = Class(name="tgg::EEnumLiteral")
tgg_AttributeExpression = Class(name="tgg::AttributeExpression")
tgg_EObject = Class(name="tgg::EObject")
tgg_LiteralExpression = Class(name="tgg::LiteralExpression")
OperatorPattern = Class(name="OperatorPattern")
tgg_EReference = Class(name="tgg::EReference")
tgg_Operator = Class(name="tgg::Operator")
tgg_Expression = Class(name="tgg::Expression")
tgg_OperatorPattern = Class(name="tgg::OperatorPattern")
tgg_NamedElements = Class(name="tgg::NamedElements")
tgg_NamePattern = Class(name="tgg::NamePattern")

# tgg_TripleGraphGrammarFile class attributes and methods

# tgg_Import class attributes and methods
tgg_Import_name: Property = Property(name="name", type=StringType)
tgg_Import.attributes={tgg_Import_name}

# tgg_Using class attributes and methods
tgg_Using_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
tgg_Using.attributes={tgg_Using_importedNamespace}

# tgg_Schema class attributes and methods

# tgg_Rule class attributes and methods
tgg_Rule_abstractRule: Property = Property(name="abstractRule", type=BooleanType)
tgg_Rule.attributes={tgg_Rule_abstractRule}

# tgg_ComplementRule class attributes and methods

# tgg_Nac class attributes and methods

# tgg_AttrCondDefLibrary class attributes and methods

# NamedElements class attributes and methods

# tgg_EPackage class attributes and methods

# tgg_CorrType class attributes and methods

# tgg_AttrCondDef class attributes and methods
tgg_AttrCondDef_userDefined: Property = Property(name="userDefined", type=BooleanType)
tgg_AttrCondDef.attributes={tgg_AttrCondDef_userDefined}

# tgg_EClass class attributes and methods

# tgg_Param class attributes and methods
tgg_Param_paramName: Property = Property(name="paramName", type=StringType)
tgg_Param.attributes={tgg_Param_paramName}

# tgg_Adornment class attributes and methods
tgg_Adornment_value: Property = Property(name="value", type=StringType)
tgg_Adornment.attributes={tgg_Adornment_value}

# tgg_EDataType class attributes and methods

# tgg_ObjectVariablePattern class attributes and methods

# tgg_CorrVariablePattern class attributes and methods

# tgg_AttrCond class attributes and methods

# tgg_LocalVariable class attributes and methods
tgg_LocalVariable_name: Property = Property(name="name", type=StringType)
tgg_LocalVariable.attributes={tgg_LocalVariable_name}

# ParamValue class attributes and methods

# NamePattern class attributes and methods

# tgg_AttributeAssignment class attributes and methods
tgg_AttributeAssignment_op: Property = Property(name="op", type=StringType)
tgg_AttributeAssignment.attributes={tgg_AttributeAssignment_op}

# tgg_AttributeConstraint class attributes and methods
tgg_AttributeConstraint_op: Property = Property(name="op", type=StringType)
tgg_AttributeConstraint.attributes={tgg_AttributeConstraint_op}

# tgg_LinkVariablePattern class attributes and methods

# tgg_ContextObjectVariablePattern class attributes and methods
tgg_ContextObjectVariablePattern_name: Property = Property(name="name", type=StringType)
tgg_ContextObjectVariablePattern.attributes={tgg_ContextObjectVariablePattern_name}

# tgg_ContextLinkVariablePattern class attributes and methods

# tgg_EAttribute class attributes and methods

# tgg_ParamValue class attributes and methods

# tgg_EnumExpression class attributes and methods

# Expression class attributes and methods

# tgg_EEnum class attributes and methods

# tgg_EEnumLiteral class attributes and methods

# tgg_AttributeExpression class attributes and methods

# tgg_EObject class attributes and methods

# tgg_LiteralExpression class attributes and methods
tgg_LiteralExpression_value: Property = Property(name="value", type=StringType)
tgg_LiteralExpression.attributes={tgg_LiteralExpression_value}

# OperatorPattern class attributes and methods

# tgg_EReference class attributes and methods

# tgg_Operator class attributes and methods
tgg_Operator_value: Property = Property(name="value", type=StringType)
tgg_Operator.attributes={tgg_Operator_value}

# tgg_Expression class attributes and methods

# tgg_OperatorPattern class attributes and methods

# tgg_NamedElements class attributes and methods
tgg_NamedElements_name: Property = Property(name="name", type=StringType)
tgg_NamedElements.attributes={tgg_NamedElements_name}

# tgg_NamePattern class attributes and methods

# Relationships
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="tgg_Import", type=tgg_TripleGraphGrammarFile, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_TripleGraphGrammarFile", type=tgg_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
using1: BinaryAssociation = BinaryAssociation(
    name="using1",
    ends={
        Property(name="tgg_Using", type=tgg_TripleGraphGrammarFile, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_TripleGraphGrammarFile2", type=tgg_Using, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schema3: BinaryAssociation = BinaryAssociation(
    name="schema3",
    ends={
        Property(name="tgg_Schema", type=tgg_TripleGraphGrammarFile, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_TripleGraphGrammarFile4", type=tgg_Schema, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rules5: BinaryAssociation = BinaryAssociation(
    name="rules5",
    ends={
        Property(name="tgg_Rule", type=tgg_TripleGraphGrammarFile, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_TripleGraphGrammarFile6", type=tgg_Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
complementRules7: BinaryAssociation = BinaryAssociation(
    name="complementRules7",
    ends={
        Property(name="tgg_ComplementRule", type=tgg_TripleGraphGrammarFile, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_TripleGraphGrammarFile8", type=tgg_ComplementRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nacs9: BinaryAssociation = BinaryAssociation(
    name="nacs9",
    ends={
        Property(name="tgg_Nac", type=tgg_TripleGraphGrammarFile, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_TripleGraphGrammarFile10", type=tgg_Nac, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
library11: BinaryAssociation = BinaryAssociation(
    name="library11",
    ends={
        Property(name="tgg_AttrCondDefLibrary", type=tgg_TripleGraphGrammarFile, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_TripleGraphGrammarFile12", type=tgg_AttrCondDefLibrary, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sourceTypes13: BinaryAssociation = BinaryAssociation(
    name="sourceTypes13",
    ends={
        Property(name="tgg_EPackage", type=tgg_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_Schema14", type=tgg_EPackage, multiplicity=Multiplicity(0, 9999))
    }
)
targetTypes15: BinaryAssociation = BinaryAssociation(
    name="targetTypes15",
    ends={
        Property(name="tgg_EPackage17", type=tgg_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_Schema16", type=tgg_EPackage, multiplicity=Multiplicity(0, 9999))
    }
)
correspondenceTypes18: BinaryAssociation = BinaryAssociation(
    name="correspondenceTypes18",
    ends={
        Property(name="tgg_CorrType", type=tgg_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_Schema19", type=tgg_CorrType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributeCondDefs20: BinaryAssociation = BinaryAssociation(
    name="attributeCondDefs20",
    ends={
        Property(name="tgg_AttrCondDef", type=tgg_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_Schema21", type=tgg_AttrCondDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
super23: BinaryAssociation = BinaryAssociation(
    name="super23",
    ends={
        Property(name="tgg_CorrType24", type=tgg_CorrType, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_CorrType22", type=tgg_CorrType, multiplicity=Multiplicity(0, 1))
    }
)
source25: BinaryAssociation = BinaryAssociation(
    name="source25",
    ends={
        Property(name="tgg_EClass", type=tgg_CorrType, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_CorrType26", type=tgg_EClass, multiplicity=Multiplicity(0, 1))
    }
)
target27: BinaryAssociation = BinaryAssociation(
    name="target27",
    ends={
        Property(name="tgg_EClass29", type=tgg_CorrType, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_CorrType28", type=tgg_EClass, multiplicity=Multiplicity(0, 1))
    }
)
params30: BinaryAssociation = BinaryAssociation(
    name="params30",
    ends={
        Property(name="tgg_Param", type=tgg_AttrCondDef, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_AttrCondDef31", type=tgg_Param, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allowedSyncAdornments32: BinaryAssociation = BinaryAssociation(
    name="allowedSyncAdornments32",
    ends={
        Property(name="tgg_Adornment", type=tgg_AttrCondDef, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_AttrCondDef33", type=tgg_Adornment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allowedGenAdornments34: BinaryAssociation = BinaryAssociation(
    name="allowedGenAdornments34",
    ends={
        Property(name="tgg_Adornment36", type=tgg_AttrCondDef, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_AttrCondDef35", type=tgg_Adornment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type37: BinaryAssociation = BinaryAssociation(
    name="type37",
    ends={
        Property(name="tgg_EDataType", type=tgg_Param, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_Param38", type=tgg_EDataType, multiplicity=Multiplicity(0, 1))
    }
)
supertypes40: BinaryAssociation = BinaryAssociation(
    name="supertypes40",
    ends={
        Property(name="tgg_Rule41", type=tgg_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_Rule39", type=tgg_Rule, multiplicity=Multiplicity(0, 9999))
    }
)
schema42: BinaryAssociation = BinaryAssociation(
    name="schema42",
    ends={
        Property(name="tgg_Schema44", type=tgg_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_Rule43", type=tgg_Schema, multiplicity=Multiplicity(0, 1))
    }
)
sourcePatterns45: BinaryAssociation = BinaryAssociation(
    name="sourcePatterns45",
    ends={
        Property(name="tgg_ObjectVariablePattern", type=tgg_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_Rule46", type=tgg_ObjectVariablePattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetPatterns47: BinaryAssociation = BinaryAssociation(
    name="targetPatterns47",
    ends={
        Property(name="tgg_ObjectVariablePattern49", type=tgg_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_Rule48", type=tgg_ObjectVariablePattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
correspondencePatterns50: BinaryAssociation = BinaryAssociation(
    name="correspondencePatterns50",
    ends={
        Property(name="tgg_CorrVariablePattern", type=tgg_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_Rule51", type=tgg_CorrVariablePattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attrConditions52: BinaryAssociation = BinaryAssociation(
    name="attrConditions52",
    ends={
        Property(name="tgg_AttrCond", type=tgg_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_Rule53", type=tgg_AttrCond, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name54: BinaryAssociation = BinaryAssociation(
    name="name54",
    ends={
        Property(name="tgg_AttrCondDef56", type=tgg_AttrCond, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_AttrCond55", type=tgg_AttrCondDef, multiplicity=Multiplicity(0, 1))
    }
)
attributeCondDefs59: BinaryAssociation = BinaryAssociation(
    name="attributeCondDefs59",
    ends={
        Property(name="tgg_AttrCondDef61", type=tgg_AttrCondDefLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_AttrCondDefLibrary60", type=tgg_AttrCondDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type62: BinaryAssociation = BinaryAssociation(
    name="type62",
    ends={
        Property(name="tgg_CorrType64", type=tgg_CorrVariablePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_CorrVariablePattern63", type=tgg_CorrType, multiplicity=Multiplicity(0, 1))
    }
)
source65: BinaryAssociation = BinaryAssociation(
    name="source65",
    ends={
        Property(name="tgg_ObjectVariablePattern67", type=tgg_CorrVariablePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_CorrVariablePattern66", type=tgg_ObjectVariablePattern, multiplicity=Multiplicity(0, 1))
    }
)
target68: BinaryAssociation = BinaryAssociation(
    name="target68",
    ends={
        Property(name="tgg_ObjectVariablePattern70", type=tgg_CorrVariablePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_CorrVariablePattern69", type=tgg_ObjectVariablePattern, multiplicity=Multiplicity(0, 1))
    }
)
type71: BinaryAssociation = BinaryAssociation(
    name="type71",
    ends={
        Property(name="tgg_EClass73", type=tgg_ObjectVariablePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_ObjectVariablePattern72", type=tgg_EClass, multiplicity=Multiplicity(0, 1))
    }
)
attributeAssignments74: BinaryAssociation = BinaryAssociation(
    name="attributeAssignments74",
    ends={
        Property(name="tgg_AttributeAssignment", type=tgg_ObjectVariablePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_ObjectVariablePattern75", type=tgg_AttributeAssignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributeConstraints76: BinaryAssociation = BinaryAssociation(
    name="attributeConstraints76",
    ends={
        Property(name="tgg_AttributeConstraint", type=tgg_ObjectVariablePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_ObjectVariablePattern77", type=tgg_AttributeConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
linkVariablePatterns78: BinaryAssociation = BinaryAssociation(
    name="linkVariablePatterns78",
    ends={
        Property(name="tgg_LinkVariablePattern", type=tgg_ObjectVariablePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_ObjectVariablePattern79", type=tgg_LinkVariablePattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type80: BinaryAssociation = BinaryAssociation(
    name="type80",
    ends={
        Property(name="tgg_EClass81", type=tgg_ContextObjectVariablePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_ContextObjectVariablePattern", type=tgg_EClass, multiplicity=Multiplicity(0, 1))
    }
)
attributeConstraints82: BinaryAssociation = BinaryAssociation(
    name="attributeConstraints82",
    ends={
        Property(name="tgg_AttributeConstraint84", type=tgg_ContextObjectVariablePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_ContextObjectVariablePattern83", type=tgg_AttributeConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
linkVariablePatterns85: BinaryAssociation = BinaryAssociation(
    name="linkVariablePatterns85",
    ends={
        Property(name="tgg_ContextLinkVariablePattern", type=tgg_ContextObjectVariablePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_ContextObjectVariablePattern86", type=tgg_ContextLinkVariablePattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute87: BinaryAssociation = BinaryAssociation(
    name="attribute87",
    ends={
        Property(name="tgg_EAttribute", type=tgg_AttributeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_AttributeConstraint88", type=tgg_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
values57: BinaryAssociation = BinaryAssociation(
    name="values57",
    ends={
        Property(name="tgg_ParamValue", type=tgg_AttrCond, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_AttrCond58", type=tgg_ParamValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute91: BinaryAssociation = BinaryAssociation(
    name="attribute91",
    ends={
        Property(name="tgg_EAttribute93", type=tgg_AttributeAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_AttributeAssignment92", type=tgg_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
valueExp94: BinaryAssociation = BinaryAssociation(
    name="valueExp94",
    ends={
        Property(name="tgg_Expression96", type=tgg_AttributeAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_AttributeAssignment95", type=tgg_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eenum97: BinaryAssociation = BinaryAssociation(
    name="eenum97",
    ends={
        Property(name="tgg_EEnum", type=tgg_EnumExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_EnumExpression", type=tgg_EEnum, multiplicity=Multiplicity(0, 1))
    }
)
literal98: BinaryAssociation = BinaryAssociation(
    name="literal98",
    ends={
        Property(name="tgg_EEnumLiteral", type=tgg_EnumExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_EnumExpression99", type=tgg_EEnumLiteral, multiplicity=Multiplicity(0, 1))
    }
)
objectVar100: BinaryAssociation = BinaryAssociation(
    name="objectVar100",
    ends={
        Property(name="tgg_EObject", type=tgg_AttributeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_AttributeExpression", type=tgg_EObject, multiplicity=Multiplicity(0, 1))
    }
)
attribute101: BinaryAssociation = BinaryAssociation(
    name="attribute101",
    ends={
        Property(name="tgg_EAttribute103", type=tgg_AttributeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_AttributeExpression102", type=tgg_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
type104: BinaryAssociation = BinaryAssociation(
    name="type104",
    ends={
        Property(name="tgg_EReference", type=tgg_LinkVariablePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_LinkVariablePattern105", type=tgg_EReference, multiplicity=Multiplicity(0, 1))
    }
)
target106: BinaryAssociation = BinaryAssociation(
    name="target106",
    ends={
        Property(name="tgg_ObjectVariablePattern108", type=tgg_LinkVariablePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_LinkVariablePattern107", type=tgg_ObjectVariablePattern, multiplicity=Multiplicity(0, 1))
    }
)
type109: BinaryAssociation = BinaryAssociation(
    name="type109",
    ends={
        Property(name="tgg_EReference111", type=tgg_ContextLinkVariablePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_ContextLinkVariablePattern110", type=tgg_EReference, multiplicity=Multiplicity(0, 1))
    }
)
target112: BinaryAssociation = BinaryAssociation(
    name="target112",
    ends={
        Property(name="tgg_ContextObjectVariablePattern114", type=tgg_ContextLinkVariablePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_ContextLinkVariablePattern113", type=tgg_ContextObjectVariablePattern, multiplicity=Multiplicity(0, 1))
    }
)
kernel115: BinaryAssociation = BinaryAssociation(
    name="kernel115",
    ends={
        Property(name="tgg_Rule117", type=tgg_ComplementRule, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_ComplementRule116", type=tgg_Rule, multiplicity=Multiplicity(0, 1))
    }
)
sourcePatterns118: BinaryAssociation = BinaryAssociation(
    name="sourcePatterns118",
    ends={
        Property(name="tgg_ObjectVariablePattern120", type=tgg_ComplementRule, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_ComplementRule119", type=tgg_ObjectVariablePattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
valueExp89: BinaryAssociation = BinaryAssociation(
    name="valueExp89",
    ends={
        Property(name="tgg_Expression", type=tgg_AttributeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_AttributeConstraint90", type=tgg_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
correspondencePatterns124: BinaryAssociation = BinaryAssociation(
    name="correspondencePatterns124",
    ends={
        Property(name="tgg_CorrVariablePattern126", type=tgg_ComplementRule, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_ComplementRule125", type=tgg_CorrVariablePattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attrConditions127: BinaryAssociation = BinaryAssociation(
    name="attrConditions127",
    ends={
        Property(name="tgg_AttrCond129", type=tgg_ComplementRule, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_ComplementRule128", type=tgg_AttrCond, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rule130: BinaryAssociation = BinaryAssociation(
    name="rule130",
    ends={
        Property(name="tgg_Rule132", type=tgg_Nac, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_Nac131", type=tgg_Rule, multiplicity=Multiplicity(0, 1))
    }
)
sourcePatterns133: BinaryAssociation = BinaryAssociation(
    name="sourcePatterns133",
    ends={
        Property(name="tgg_ContextObjectVariablePattern135", type=tgg_Nac, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_Nac134", type=tgg_ContextObjectVariablePattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetPatterns136: BinaryAssociation = BinaryAssociation(
    name="targetPatterns136",
    ends={
        Property(name="tgg_ContextObjectVariablePattern138", type=tgg_Nac, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_Nac137", type=tgg_ContextObjectVariablePattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attrConditions139: BinaryAssociation = BinaryAssociation(
    name="attrConditions139",
    ends={
        Property(name="tgg_AttrCond141", type=tgg_Nac, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_Nac140", type=tgg_AttrCond, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
op142: BinaryAssociation = BinaryAssociation(
    name="op142",
    ends={
        Property(name="tgg_Operator", type=tgg_OperatorPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_OperatorPattern", type=tgg_Operator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetPatterns121: BinaryAssociation = BinaryAssociation(
    name="targetPatterns121",
    ends={
        Property(name="tgg_ObjectVariablePattern123", type=tgg_ComplementRule, multiplicity=Multiplicity(1, 1)),
        Property(name="tgg_ComplementRule122", type=tgg_ObjectVariablePattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_tgg_Schema_NamedElements = Generalization(general=NamedElements, specific=tgg_Schema)
gen_tgg_CorrType_NamedElements = Generalization(general=NamedElements, specific=tgg_CorrType)
gen_tgg_AttrCondDef_NamedElements = Generalization(general=NamedElements, specific=tgg_AttrCondDef)
gen_tgg_Rule_NamedElements = Generalization(general=NamedElements, specific=tgg_Rule)
gen_tgg_AttrCondDefLibrary_NamedElements = Generalization(general=NamedElements, specific=tgg_AttrCondDefLibrary)
gen_tgg_LocalVariable_ParamValue = Generalization(general=ParamValue, specific=tgg_LocalVariable)
gen_tgg_CorrVariablePattern_NamePattern = Generalization(general=NamePattern, specific=tgg_CorrVariablePattern)
gen_tgg_ObjectVariablePattern_NamePattern = Generalization(general=NamePattern, specific=tgg_ObjectVariablePattern)
gen_tgg_Expression_ParamValue = Generalization(general=ParamValue, specific=tgg_Expression)
gen_tgg_EnumExpression_Expression = Generalization(general=Expression, specific=tgg_EnumExpression)
gen_tgg_AttributeExpression_Expression = Generalization(general=Expression, specific=tgg_AttributeExpression)
gen_tgg_LiteralExpression_Expression = Generalization(general=Expression, specific=tgg_LiteralExpression)
gen_tgg_LinkVariablePattern_OperatorPattern = Generalization(general=OperatorPattern, specific=tgg_LinkVariablePattern)
gen_tgg_ComplementRule_NamedElements = Generalization(general=NamedElements, specific=tgg_ComplementRule)
gen_tgg_Nac_NamedElements = Generalization(general=NamedElements, specific=tgg_Nac)
gen_tgg_NamePattern_OperatorPattern = Generalization(general=OperatorPattern, specific=tgg_NamePattern)
gen_tgg_NamePattern_NamedElements = Generalization(general=NamedElements, specific=tgg_NamePattern)

# Domain Model
domain_model = DomainModel(
    name="tgg",
    types={tgg_TripleGraphGrammarFile, tgg_Import, tgg_Using, tgg_Schema, tgg_Rule, tgg_ComplementRule, tgg_Nac, tgg_AttrCondDefLibrary, NamedElements, tgg_EPackage, tgg_CorrType, tgg_AttrCondDef, tgg_EClass, tgg_Param, tgg_Adornment, tgg_EDataType, tgg_ObjectVariablePattern, tgg_CorrVariablePattern, tgg_AttrCond, tgg_LocalVariable, ParamValue, NamePattern, tgg_AttributeAssignment, tgg_AttributeConstraint, tgg_LinkVariablePattern, tgg_ContextObjectVariablePattern, tgg_ContextLinkVariablePattern, tgg_EAttribute, tgg_ParamValue, tgg_EnumExpression, Expression, tgg_EEnum, tgg_EEnumLiteral, tgg_AttributeExpression, tgg_EObject, tgg_LiteralExpression, OperatorPattern, tgg_EReference, tgg_Operator, tgg_Expression, tgg_OperatorPattern, tgg_NamedElements, tgg_NamePattern},
    associations={imports0, using1, schema3, rules5, complementRules7, nacs9, library11, sourceTypes13, targetTypes15, correspondenceTypes18, attributeCondDefs20, super23, source25, target27, params30, allowedSyncAdornments32, allowedGenAdornments34, type37, supertypes40, schema42, sourcePatterns45, targetPatterns47, correspondencePatterns50, attrConditions52, name54, attributeCondDefs59, type62, source65, target68, type71, attributeAssignments74, attributeConstraints76, linkVariablePatterns78, type80, attributeConstraints82, linkVariablePatterns85, attribute87, values57, attribute91, valueExp94, eenum97, literal98, objectVar100, attribute101, type104, target106, type109, target112, kernel115, sourcePatterns118, valueExp89, correspondencePatterns124, attrConditions127, rule130, sourcePatterns133, targetPatterns136, attrConditions139, op142, targetPatterns121},
    generalizations={gen_tgg_Schema_NamedElements, gen_tgg_CorrType_NamedElements, gen_tgg_AttrCondDef_NamedElements, gen_tgg_Rule_NamedElements, gen_tgg_AttrCondDefLibrary_NamedElements, gen_tgg_LocalVariable_ParamValue, gen_tgg_CorrVariablePattern_NamePattern, gen_tgg_ObjectVariablePattern_NamePattern, gen_tgg_Expression_ParamValue, gen_tgg_EnumExpression_Expression, gen_tgg_AttributeExpression_Expression, gen_tgg_LiteralExpression_Expression, gen_tgg_LinkVariablePattern_OperatorPattern, gen_tgg_ComplementRule_NamedElements, gen_tgg_Nac_NamedElements, gen_tgg_NamePattern_OperatorPattern, gen_tgg_NamePattern_NamedElements},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)