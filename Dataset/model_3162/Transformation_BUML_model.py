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
transformation_Transformation = Class(name="transformation::Transformation")
transformation_MetamodelDeclaration = Class(name="transformation::MetamodelDeclaration", is_abstract=True)
transformation_AbstractMapping = Class(name="transformation::AbstractMapping", is_abstract=True)
transformation_EPackage = Class(name="transformation::EPackage")
transformation_ExplicitMetamodel = Class(name="transformation::ExplicitMetamodel")
MetamodelDeclaration = Class(name="MetamodelDeclaration")
transformation_SourceMetamodel = Class(name="transformation::SourceMetamodel")
ExplicitMetamodel = Class(name="ExplicitMetamodel")
transformation_TargetMetamodel = Class(name="transformation::TargetMetamodel")
transformation_ExtentMetamodel = Class(name="transformation::ExtentMetamodel")
transformation_DataTypeMapping = Class(name="transformation::DataTypeMapping")
AbstractMapping = Class(name="AbstractMapping")
transformation_EDataType = Class(name="transformation::EDataType")
transformation_ContentMapping = Class(name="transformation::ContentMapping", is_abstract=True)
transformation_ClassMapping = Class(name="transformation::ClassMapping")
transformation_EClass = Class(name="transformation::EClass")
transformation_CompositeMapping = Class(name="transformation::CompositeMapping")
ContentMapping = Class(name="ContentMapping")
transformation_ConditionalMapping = Class(name="transformation::ConditionalMapping")
transformation_WhenClause = Class(name="transformation::WhenClause")
transformation_OtherwiseClause = Class(name="transformation::OtherwiseClause")
CompositeMapping = Class(name="CompositeMapping")
transformation_Expression = Class(name="transformation::Expression", is_abstract=True)
transformation_ResultMapping = Class(name="transformation::ResultMapping")
transformation_FeatureMapping = Class(name="transformation::FeatureMapping")
transformation_EStructuralFeature = Class(name="transformation::EStructuralFeature")
transformation_VariableDefinition = Class(name="transformation::VariableDefinition")
transformation_VariableInitialization = Class(name="transformation::VariableInitialization")
transformation_If = Class(name="transformation::If")
Expression = Class(name="Expression")
transformation_Let = Class(name="transformation::Let")
transformation_ConditionalExpression = Class(name="transformation::ConditionalExpression")
transformation_BinaryExpression = Class(name="transformation::BinaryExpression", is_abstract=True)
transformation_CoalescingExpression = Class(name="transformation::CoalescingExpression")
BinaryExpression = Class(name="BinaryExpression")
transformation_LogicalExpression = Class(name="transformation::LogicalExpression", is_abstract=True)
transformation_Or = Class(name="transformation::Or")
LogicalExpression = Class(name="LogicalExpression")
transformation_And = Class(name="transformation::And")
transformation_EqualityExpression = Class(name="transformation::EqualityExpression", is_abstract=True)
transformation_Equal = Class(name="transformation::Equal")
EqualityExpression = Class(name="EqualityExpression")
transformation_Different = Class(name="transformation::Different")
transformation_RelationalExpression = Class(name="transformation::RelationalExpression", is_abstract=True)
transformation_Less = Class(name="transformation::Less")
RelationalExpression = Class(name="RelationalExpression")
transformation_Greater = Class(name="transformation::Greater")
transformation_LessOrEqual = Class(name="transformation::LessOrEqual")
transformation_GreaterOrEqual = Class(name="transformation::GreaterOrEqual")
transformation_ArithmeticExpression = Class(name="transformation::ArithmeticExpression", is_abstract=True)
transformation_Addition = Class(name="transformation::Addition")
ArithmeticExpression = Class(name="ArithmeticExpression")
transformation_Subtraction = Class(name="transformation::Subtraction")
transformation_Multiplication = Class(name="transformation::Multiplication")
transformation_Division = Class(name="transformation::Division")
transformation_UnaryExpression = Class(name="transformation::UnaryExpression", is_abstract=True)
transformation_Negation = Class(name="transformation::Negation")
UnaryExpression = Class(name="UnaryExpression")
transformation_Minus = Class(name="transformation::Minus")
transformation_ETypedElement = Class(name="transformation::ETypedElement")
transformation_ExtentExpression = Class(name="transformation::ExtentExpression")
transformation_TypeOfExpression = Class(name="transformation::TypeOfExpression")
transformation_Invocation = Class(name="transformation::Invocation")
transformation_Lambda = Class(name="transformation::Lambda")
transformation_Map = Class(name="transformation::Map")
transformation_EClassifier = Class(name="transformation::EClassifier")
transformation_Source = Class(name="transformation::Source")
transformation_VariableUse = Class(name="transformation::VariableUse")
transformation_ClassLiteral = Class(name="transformation::ClassLiteral")
transformation_EnumLiteral = Class(name="transformation::EnumLiteral")
transformation_FeatureAccess = Class(name="transformation::FeatureAccess")
transformation_BooleanLiteral = Class(name="transformation::BooleanLiteral")
transformation_IntegerLiteral = Class(name="transformation::IntegerLiteral")
transformation_RealLiteral = Class(name="transformation::RealLiteral")
transformation_StringLiteral = Class(name="transformation::StringLiteral")
transformation_EEnumLiteral = Class(name="transformation::EEnumLiteral")

# transformation_Transformation class attributes and methods
transformation_Transformation_name: Property = Property(name="name", type=StringType)
transformation_Transformation.attributes={transformation_Transformation_name}

# transformation_MetamodelDeclaration class attributes and methods

# transformation_AbstractMapping class attributes and methods

# transformation_EPackage class attributes and methods

# transformation_ExplicitMetamodel class attributes and methods
transformation_ExplicitMetamodel_alias: Property = Property(name="alias", type=StringType)
transformation_ExplicitMetamodel.attributes={transformation_ExplicitMetamodel_alias}

# MetamodelDeclaration class attributes and methods

# transformation_SourceMetamodel class attributes and methods

# ExplicitMetamodel class attributes and methods

# transformation_TargetMetamodel class attributes and methods

# transformation_ExtentMetamodel class attributes and methods
transformation_ExtentMetamodel_generated: Property = Property(name="generated", type=BooleanType)
transformation_ExtentMetamodel.attributes={transformation_ExtentMetamodel_generated}

# transformation_DataTypeMapping class attributes and methods

# AbstractMapping class attributes and methods

# transformation_EDataType class attributes and methods

# transformation_ContentMapping class attributes and methods

# transformation_ClassMapping class attributes and methods
transformation_ClassMapping_default: Property = Property(name="default", type=BooleanType)
transformation_ClassMapping.attributes={transformation_ClassMapping_default}

# transformation_EClass class attributes and methods

# transformation_CompositeMapping class attributes and methods

# ContentMapping class attributes and methods

# transformation_ConditionalMapping class attributes and methods

# transformation_WhenClause class attributes and methods

# transformation_OtherwiseClause class attributes and methods

# CompositeMapping class attributes and methods

# transformation_Expression class attributes and methods

# transformation_ResultMapping class attributes and methods

# transformation_FeatureMapping class attributes and methods

# transformation_EStructuralFeature class attributes and methods

# transformation_VariableDefinition class attributes and methods
transformation_VariableDefinition_name: Property = Property(name="name", type=StringType)
transformation_VariableDefinition.attributes={transformation_VariableDefinition_name}

# transformation_VariableInitialization class attributes and methods

# transformation_If class attributes and methods

# Expression class attributes and methods

# transformation_Let class attributes and methods

# transformation_ConditionalExpression class attributes and methods

# transformation_BinaryExpression class attributes and methods

# transformation_CoalescingExpression class attributes and methods

# BinaryExpression class attributes and methods

# transformation_LogicalExpression class attributes and methods

# transformation_Or class attributes and methods

# LogicalExpression class attributes and methods

# transformation_And class attributes and methods

# transformation_EqualityExpression class attributes and methods

# transformation_Equal class attributes and methods

# EqualityExpression class attributes and methods

# transformation_Different class attributes and methods

# transformation_RelationalExpression class attributes and methods

# transformation_Less class attributes and methods

# RelationalExpression class attributes and methods

# transformation_Greater class attributes and methods

# transformation_LessOrEqual class attributes and methods

# transformation_GreaterOrEqual class attributes and methods

# transformation_ArithmeticExpression class attributes and methods

# transformation_Addition class attributes and methods

# ArithmeticExpression class attributes and methods

# transformation_Subtraction class attributes and methods

# transformation_Multiplication class attributes and methods

# transformation_Division class attributes and methods

# transformation_UnaryExpression class attributes and methods

# transformation_Negation class attributes and methods

# UnaryExpression class attributes and methods

# transformation_Minus class attributes and methods

# transformation_ETypedElement class attributes and methods

# transformation_ExtentExpression class attributes and methods

# transformation_TypeOfExpression class attributes and methods

# transformation_Invocation class attributes and methods

# transformation_Lambda class attributes and methods

# transformation_Map class attributes and methods

# transformation_EClassifier class attributes and methods

# transformation_Source class attributes and methods

# transformation_VariableUse class attributes and methods

# transformation_ClassLiteral class attributes and methods

# transformation_EnumLiteral class attributes and methods

# transformation_FeatureAccess class attributes and methods
transformation_FeatureAccess_nullable: Property = Property(name="nullable", type=BooleanType)
transformation_FeatureAccess_spreading: Property = Property(name="spreading", type=BooleanType)
transformation_FeatureAccess.attributes={transformation_FeatureAccess_nullable, transformation_FeatureAccess_spreading}

# transformation_BooleanLiteral class attributes and methods
transformation_BooleanLiteral_value: Property = Property(name="value", type=BooleanType)
transformation_BooleanLiteral.attributes={transformation_BooleanLiteral_value}

# transformation_IntegerLiteral class attributes and methods
transformation_IntegerLiteral_value: Property = Property(name="value", type=IntegerType)
transformation_IntegerLiteral.attributes={transformation_IntegerLiteral_value}

# transformation_RealLiteral class attributes and methods
transformation_RealLiteral_value: Property = Property(name="value", type=FloatType)
transformation_RealLiteral.attributes={transformation_RealLiteral_value}

# transformation_StringLiteral class attributes and methods
transformation_StringLiteral_value: Property = Property(name="value", type=StringType)
transformation_StringLiteral.attributes={transformation_StringLiteral_value}

# transformation_EEnumLiteral class attributes and methods

# Relationships
metamodelDeclarations0: BinaryAssociation = BinaryAssociation(
    name="metamodelDeclarations0",
    ends={
        Property(name="transformation_MetamodelDeclaration", type=transformation_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_Transformation", type=transformation_MetamodelDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mappings1: BinaryAssociation = BinaryAssociation(
    name="mappings1",
    ends={
        Property(name="transformation_AbstractMapping", type=transformation_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_Transformation2", type=transformation_AbstractMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package3: BinaryAssociation = BinaryAssociation(
    name="package3",
    ends={
        Property(name="transformation_EPackage", type=transformation_MetamodelDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_MetamodelDeclaration4", type=transformation_EPackage, multiplicity=Multiplicity(1, 1))
    }
)
sourceMetamodel5: BinaryAssociation = BinaryAssociation(
    name="sourceMetamodel5",
    ends={
        Property(name="transformation_SourceMetamodel", type=transformation_ExtentMetamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_ExtentMetamodel", type=transformation_SourceMetamodel, multiplicity=Multiplicity(1, 1))
    }
)
source6: BinaryAssociation = BinaryAssociation(
    name="source6",
    ends={
        Property(name="transformation_EDataType", type=transformation_DataTypeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_DataTypeMapping", type=transformation_EDataType, multiplicity=Multiplicity(1, 1))
    }
)
target7: BinaryAssociation = BinaryAssociation(
    name="target7",
    ends={
        Property(name="transformation_EDataType9", type=transformation_DataTypeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_DataTypeMapping8", type=transformation_EDataType, multiplicity=Multiplicity(1, 1))
    }
)
content10: BinaryAssociation = BinaryAssociation(
    name="content10",
    ends={
        Property(name="transformation_ContentMapping", type=transformation_DataTypeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_DataTypeMapping11", type=transformation_ContentMapping, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source12: BinaryAssociation = BinaryAssociation(
    name="source12",
    ends={
        Property(name="transformation_EClass", type=transformation_ClassMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_ClassMapping", type=transformation_EClass, multiplicity=Multiplicity(1, 1))
    }
)
target13: BinaryAssociation = BinaryAssociation(
    name="target13",
    ends={
        Property(name="transformation_EClass15", type=transformation_ClassMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_ClassMapping14", type=transformation_EClass, multiplicity=Multiplicity(1, 1))
    }
)
content16: BinaryAssociation = BinaryAssociation(
    name="content16",
    ends={
        Property(name="transformation_ContentMapping18", type=transformation_ClassMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_ClassMapping17", type=transformation_ContentMapping, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
children19: BinaryAssociation = BinaryAssociation(
    name="children19",
    ends={
        Property(name="transformation_ContentMapping20", type=transformation_CompositeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_CompositeMapping", type=transformation_ContentMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
whenClauses21: BinaryAssociation = BinaryAssociation(
    name="whenClauses21",
    ends={
        Property(name="transformation_WhenClause", type=transformation_ConditionalMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_ConditionalMapping", type=transformation_WhenClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
otherwiseClause22: BinaryAssociation = BinaryAssociation(
    name="otherwiseClause22",
    ends={
        Property(name="transformation_OtherwiseClause", type=transformation_ConditionalMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_ConditionalMapping23", type=transformation_OtherwiseClause, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition24: BinaryAssociation = BinaryAssociation(
    name="condition24",
    ends={
        Property(name="transformation_Expression", type=transformation_WhenClause, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_WhenClause25", type=transformation_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value26: BinaryAssociation = BinaryAssociation(
    name="value26",
    ends={
        Property(name="transformation_Expression27", type=transformation_ResultMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_ResultMapping", type=transformation_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target28: BinaryAssociation = BinaryAssociation(
    name="target28",
    ends={
        Property(name="transformation_EStructuralFeature", type=transformation_FeatureMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_FeatureMapping", type=transformation_EStructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
value29: BinaryAssociation = BinaryAssociation(
    name="value29",
    ends={
        Property(name="transformation_Expression31", type=transformation_FeatureMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_FeatureMapping30", type=transformation_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable32: BinaryAssociation = BinaryAssociation(
    name="variable32",
    ends={
        Property(name="transformation_VariableDefinition", type=transformation_VariableInitialization, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_VariableInitialization", type=transformation_VariableDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value33: BinaryAssociation = BinaryAssociation(
    name="value33",
    ends={
        Property(name="transformation_Expression35", type=transformation_VariableInitialization, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_VariableInitialization34", type=transformation_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition36: BinaryAssociation = BinaryAssociation(
    name="condition36",
    ends={
        Property(name="transformation_Expression37", type=transformation_If, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_If", type=transformation_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenExpression38: BinaryAssociation = BinaryAssociation(
    name="thenExpression38",
    ends={
        Property(name="transformation_Expression40", type=transformation_If, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_If39", type=transformation_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseExpression41: BinaryAssociation = BinaryAssociation(
    name="elseExpression41",
    ends={
        Property(name="transformation_Expression43", type=transformation_If, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_If42", type=transformation_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables44: BinaryAssociation = BinaryAssociation(
    name="variables44",
    ends={
        Property(name="transformation_VariableInitialization45", type=transformation_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_Let", type=transformation_VariableInitialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
result46: BinaryAssociation = BinaryAssociation(
    name="result46",
    ends={
        Property(name="transformation_Expression48", type=transformation_Let, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_Let47", type=transformation_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition49: BinaryAssociation = BinaryAssociation(
    name="condition49",
    ends={
        Property(name="transformation_ConditionalExpression", type=transformation_Expression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="transformation_Expression50", type=transformation_ConditionalExpression, multiplicity=Multiplicity(1, 1))
    }
)
trueExpression51: BinaryAssociation = BinaryAssociation(
    name="trueExpression51",
    ends={
        Property(name="transformation_Expression53", type=transformation_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_ConditionalExpression52", type=transformation_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
falseExpression54: BinaryAssociation = BinaryAssociation(
    name="falseExpression54",
    ends={
        Property(name="transformation_Expression56", type=transformation_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_ConditionalExpression55", type=transformation_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left57: BinaryAssociation = BinaryAssociation(
    name="left57",
    ends={
        Property(name="transformation_Expression58", type=transformation_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_BinaryExpression", type=transformation_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right59: BinaryAssociation = BinaryAssociation(
    name="right59",
    ends={
        Property(name="transformation_Expression61", type=transformation_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_BinaryExpression60", type=transformation_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand62: BinaryAssociation = BinaryAssociation(
    name="operand62",
    ends={
        Property(name="transformation_Expression63", type=transformation_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_UnaryExpression", type=transformation_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object64: BinaryAssociation = BinaryAssociation(
    name="object64",
    ends={
        Property(name="transformation_FeatureAccess", type=transformation_Expression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="transformation_Expression65", type=transformation_FeatureAccess, multiplicity=Multiplicity(1, 1))
    }
)
feature66: BinaryAssociation = BinaryAssociation(
    name="feature66",
    ends={
        Property(name="transformation_ETypedElement", type=transformation_FeatureAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_FeatureAccess67", type=transformation_ETypedElement, multiplicity=Multiplicity(0, 1))
    }
)
source68: BinaryAssociation = BinaryAssociation(
    name="source68",
    ends={
        Property(name="transformation_Expression69", type=transformation_ExtentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_ExtentExpression", type=transformation_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object70: BinaryAssociation = BinaryAssociation(
    name="object70",
    ends={
        Property(name="transformation_Expression71", type=transformation_TypeOfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_TypeOfExpression", type=transformation_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
function72: BinaryAssociation = BinaryAssociation(
    name="function72",
    ends={
        Property(name="transformation_Expression73", type=transformation_Invocation, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_Invocation", type=transformation_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters74: BinaryAssociation = BinaryAssociation(
    name="parameters74",
    ends={
        Property(name="transformation_Expression76", type=transformation_Invocation, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_Invocation75", type=transformation_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters77: BinaryAssociation = BinaryAssociation(
    name="parameters77",
    ends={
        Property(name="transformation_VariableDefinition78", type=transformation_Lambda, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_Lambda", type=transformation_VariableDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
result79: BinaryAssociation = BinaryAssociation(
    name="result79",
    ends={
        Property(name="transformation_Expression81", type=transformation_Lambda, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_Lambda80", type=transformation_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value82: BinaryAssociation = BinaryAssociation(
    name="value82",
    ends={
        Property(name="transformation_Expression83", type=transformation_Map, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_Map", type=transformation_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target84: BinaryAssociation = BinaryAssociation(
    name="target84",
    ends={
        Property(name="transformation_EClassifier", type=transformation_Map, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_Map85", type=transformation_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
variable86: BinaryAssociation = BinaryAssociation(
    name="variable86",
    ends={
        Property(name="transformation_VariableDefinition87", type=transformation_VariableUse, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_VariableUse", type=transformation_VariableDefinition, multiplicity=Multiplicity(0, 1))
    }
)
objectType88: BinaryAssociation = BinaryAssociation(
    name="objectType88",
    ends={
        Property(name="transformation_EClassifier89", type=transformation_ClassLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_ClassLiteral", type=transformation_EClassifier, multiplicity=Multiplicity(1, 1))
    }
)
enumConstant90: BinaryAssociation = BinaryAssociation(
    name="enumConstant90",
    ends={
        Property(name="transformation_EEnumLiteral", type=transformation_EnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation_EnumLiteral", type=transformation_EEnumLiteral, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_transformation_ExplicitMetamodel_MetamodelDeclaration = Generalization(general=MetamodelDeclaration, specific=transformation_ExplicitMetamodel)
gen_transformation_SourceMetamodel_ExplicitMetamodel = Generalization(general=ExplicitMetamodel, specific=transformation_SourceMetamodel)
gen_transformation_TargetMetamodel_ExplicitMetamodel = Generalization(general=ExplicitMetamodel, specific=transformation_TargetMetamodel)
gen_transformation_ExtentMetamodel_MetamodelDeclaration = Generalization(general=MetamodelDeclaration, specific=transformation_ExtentMetamodel)
gen_transformation_DataTypeMapping_AbstractMapping = Generalization(general=AbstractMapping, specific=transformation_DataTypeMapping)
gen_transformation_ClassMapping_AbstractMapping = Generalization(general=AbstractMapping, specific=transformation_ClassMapping)
gen_transformation_CompositeMapping_ContentMapping = Generalization(general=ContentMapping, specific=transformation_CompositeMapping)
gen_transformation_ConditionalMapping_ContentMapping = Generalization(general=ContentMapping, specific=transformation_ConditionalMapping)
gen_transformation_WhenClause_CompositeMapping = Generalization(general=CompositeMapping, specific=transformation_WhenClause)
gen_transformation_OtherwiseClause_CompositeMapping = Generalization(general=CompositeMapping, specific=transformation_OtherwiseClause)
gen_transformation_ResultMapping_ContentMapping = Generalization(general=ContentMapping, specific=transformation_ResultMapping)
gen_transformation_FeatureMapping_ContentMapping = Generalization(general=ContentMapping, specific=transformation_FeatureMapping)
gen_transformation_If_Expression = Generalization(general=Expression, specific=transformation_If)
gen_transformation_Let_Expression = Generalization(general=Expression, specific=transformation_Let)
gen_transformation_BinaryExpression_Expression = Generalization(general=Expression, specific=transformation_BinaryExpression)
gen_transformation_CoalescingExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=transformation_CoalescingExpression)
gen_transformation_LogicalExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=transformation_LogicalExpression)
gen_transformation_Or_LogicalExpression = Generalization(general=LogicalExpression, specific=transformation_Or)
gen_transformation_And_LogicalExpression = Generalization(general=LogicalExpression, specific=transformation_And)
gen_transformation_EqualityExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=transformation_EqualityExpression)
gen_transformation_Equal_EqualityExpression = Generalization(general=EqualityExpression, specific=transformation_Equal)
gen_transformation_Different_EqualityExpression = Generalization(general=EqualityExpression, specific=transformation_Different)
gen_transformation_RelationalExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=transformation_RelationalExpression)
gen_transformation_Less_RelationalExpression = Generalization(general=RelationalExpression, specific=transformation_Less)
gen_transformation_Greater_RelationalExpression = Generalization(general=RelationalExpression, specific=transformation_Greater)
gen_transformation_LessOrEqual_RelationalExpression = Generalization(general=RelationalExpression, specific=transformation_LessOrEqual)
gen_transformation_GreaterOrEqual_RelationalExpression = Generalization(general=RelationalExpression, specific=transformation_GreaterOrEqual)
gen_transformation_ArithmeticExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=transformation_ArithmeticExpression)
gen_transformation_Addition_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=transformation_Addition)
gen_transformation_Subtraction_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=transformation_Subtraction)
gen_transformation_Multiplication_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=transformation_Multiplication)
gen_transformation_Division_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=transformation_Division)
gen_transformation_UnaryExpression_Expression = Generalization(general=Expression, specific=transformation_UnaryExpression)
gen_transformation_Negation_UnaryExpression = Generalization(general=UnaryExpression, specific=transformation_Negation)
gen_transformation_Minus_UnaryExpression = Generalization(general=UnaryExpression, specific=transformation_Minus)
gen_transformation_ConditionalExpression_Expression = Generalization(general=Expression, specific=transformation_ConditionalExpression)
gen_transformation_ExtentExpression_Expression = Generalization(general=Expression, specific=transformation_ExtentExpression)
gen_transformation_TypeOfExpression_Expression = Generalization(general=Expression, specific=transformation_TypeOfExpression)
gen_transformation_Invocation_Expression = Generalization(general=Expression, specific=transformation_Invocation)
gen_transformation_Lambda_Expression = Generalization(general=Expression, specific=transformation_Lambda)
gen_transformation_Map_Expression = Generalization(general=Expression, specific=transformation_Map)
gen_transformation_Source_Expression = Generalization(general=Expression, specific=transformation_Source)
gen_transformation_VariableUse_Expression = Generalization(general=Expression, specific=transformation_VariableUse)
gen_transformation_ClassLiteral_Expression = Generalization(general=Expression, specific=transformation_ClassLiteral)
gen_transformation_EnumLiteral_Expression = Generalization(general=Expression, specific=transformation_EnumLiteral)
gen_transformation_FeatureAccess_Expression = Generalization(general=Expression, specific=transformation_FeatureAccess)
gen_transformation_BooleanLiteral_Expression = Generalization(general=Expression, specific=transformation_BooleanLiteral)
gen_transformation_IntegerLiteral_Expression = Generalization(general=Expression, specific=transformation_IntegerLiteral)
gen_transformation_RealLiteral_Expression = Generalization(general=Expression, specific=transformation_RealLiteral)
gen_transformation_StringLiteral_Expression = Generalization(general=Expression, specific=transformation_StringLiteral)

# Domain Model
domain_model = DomainModel(
    name="transformation",
    types={transformation_Transformation, transformation_MetamodelDeclaration, transformation_AbstractMapping, transformation_EPackage, transformation_ExplicitMetamodel, MetamodelDeclaration, transformation_SourceMetamodel, ExplicitMetamodel, transformation_TargetMetamodel, transformation_ExtentMetamodel, transformation_DataTypeMapping, AbstractMapping, transformation_EDataType, transformation_ContentMapping, transformation_ClassMapping, transformation_EClass, transformation_CompositeMapping, ContentMapping, transformation_ConditionalMapping, transformation_WhenClause, transformation_OtherwiseClause, CompositeMapping, transformation_Expression, transformation_ResultMapping, transformation_FeatureMapping, transformation_EStructuralFeature, transformation_VariableDefinition, transformation_VariableInitialization, transformation_If, Expression, transformation_Let, transformation_ConditionalExpression, transformation_BinaryExpression, transformation_CoalescingExpression, BinaryExpression, transformation_LogicalExpression, transformation_Or, LogicalExpression, transformation_And, transformation_EqualityExpression, transformation_Equal, EqualityExpression, transformation_Different, transformation_RelationalExpression, transformation_Less, RelationalExpression, transformation_Greater, transformation_LessOrEqual, transformation_GreaterOrEqual, transformation_ArithmeticExpression, transformation_Addition, ArithmeticExpression, transformation_Subtraction, transformation_Multiplication, transformation_Division, transformation_UnaryExpression, transformation_Negation, UnaryExpression, transformation_Minus, transformation_ETypedElement, transformation_ExtentExpression, transformation_TypeOfExpression, transformation_Invocation, transformation_Lambda, transformation_Map, transformation_EClassifier, transformation_Source, transformation_VariableUse, transformation_ClassLiteral, transformation_EnumLiteral, transformation_FeatureAccess, transformation_BooleanLiteral, transformation_IntegerLiteral, transformation_RealLiteral, transformation_StringLiteral, transformation_EEnumLiteral},
    associations={metamodelDeclarations0, mappings1, package3, sourceMetamodel5, source6, target7, content10, source12, target13, content16, children19, whenClauses21, otherwiseClause22, condition24, value26, target28, value29, variable32, value33, condition36, thenExpression38, elseExpression41, variables44, result46, condition49, trueExpression51, falseExpression54, left57, right59, operand62, object64, feature66, source68, object70, function72, parameters74, parameters77, result79, value82, target84, variable86, objectType88, enumConstant90},
    generalizations={gen_transformation_ExplicitMetamodel_MetamodelDeclaration, gen_transformation_SourceMetamodel_ExplicitMetamodel, gen_transformation_TargetMetamodel_ExplicitMetamodel, gen_transformation_ExtentMetamodel_MetamodelDeclaration, gen_transformation_DataTypeMapping_AbstractMapping, gen_transformation_ClassMapping_AbstractMapping, gen_transformation_CompositeMapping_ContentMapping, gen_transformation_ConditionalMapping_ContentMapping, gen_transformation_WhenClause_CompositeMapping, gen_transformation_OtherwiseClause_CompositeMapping, gen_transformation_ResultMapping_ContentMapping, gen_transformation_FeatureMapping_ContentMapping, gen_transformation_If_Expression, gen_transformation_Let_Expression, gen_transformation_BinaryExpression_Expression, gen_transformation_CoalescingExpression_BinaryExpression, gen_transformation_LogicalExpression_BinaryExpression, gen_transformation_Or_LogicalExpression, gen_transformation_And_LogicalExpression, gen_transformation_EqualityExpression_BinaryExpression, gen_transformation_Equal_EqualityExpression, gen_transformation_Different_EqualityExpression, gen_transformation_RelationalExpression_BinaryExpression, gen_transformation_Less_RelationalExpression, gen_transformation_Greater_RelationalExpression, gen_transformation_LessOrEqual_RelationalExpression, gen_transformation_GreaterOrEqual_RelationalExpression, gen_transformation_ArithmeticExpression_BinaryExpression, gen_transformation_Addition_ArithmeticExpression, gen_transformation_Subtraction_ArithmeticExpression, gen_transformation_Multiplication_ArithmeticExpression, gen_transformation_Division_ArithmeticExpression, gen_transformation_UnaryExpression_Expression, gen_transformation_Negation_UnaryExpression, gen_transformation_Minus_UnaryExpression, gen_transformation_ConditionalExpression_Expression, gen_transformation_ExtentExpression_Expression, gen_transformation_TypeOfExpression_Expression, gen_transformation_Invocation_Expression, gen_transformation_Lambda_Expression, gen_transformation_Map_Expression, gen_transformation_Source_Expression, gen_transformation_VariableUse_Expression, gen_transformation_ClassLiteral_Expression, gen_transformation_EnumLiteral_Expression, gen_transformation_FeatureAccess_Expression, gen_transformation_BooleanLiteral_Expression, gen_transformation_IntegerLiteral_Expression, gen_transformation_RealLiteral_Expression, gen_transformation_StringLiteral_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)