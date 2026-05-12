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
ScenarioKind: Enumeration = Enumeration(
    name="ScenarioKind",
    literals={
            EnumerationLiteral(name="assumption"),
			EnumerationLiteral(name="specification"),
			EnumerationLiteral(name="requirement"),
			EnumerationLiteral(name="existential")
    }
)

CollectionOperation: Enumeration = Enumeration(
    name="CollectionOperation",
    literals={
            EnumerationLiteral(name="any"),
			EnumerationLiteral(name="contains"),
			EnumerationLiteral(name="containsAll"),
			EnumerationLiteral(name="first"),
			EnumerationLiteral(name="get"),
			EnumerationLiteral(name="isEmpty"),
			EnumerationLiteral(name="last"),
			EnumerationLiteral(name="size")
    }
)

# Classes
sml_Specification = Class(name="sml_Specification")
sml_Import = Class(name="sml_Import")
sml_SmlEPackage = Class(name="sml_SmlEPackage")
sml_SmlEClass = Class(name="sml_SmlEClass")
sml_SmlETypedElement = Class(name="sml_SmlETypedElement")
sml_EventParameterRanges = Class(name="sml_EventParameterRanges")
sml_Collaboration = Class(name="sml_Collaboration")
sml_SmlEEnum = Class(name="sml_SmlEEnum")
sml_SmlEEnumLiteral = Class(name="sml_SmlEEnumLiteral")
sml_Role = Class(name="sml_Role")
sml_Scenario = Class(name="sml_Scenario")
sml_RangesForParameter = Class(name="sml_RangesForParameter")
sml_AbstractRanges = Class(name="sml_AbstractRanges")
sml_IntegerRanges = Class(name="sml_IntegerRanges")
AbstractRanges = Class(name="AbstractRanges")
sml_StringRanges = Class(name="sml_StringRanges")
sml_SmlEClassifier = Class(name="sml_SmlEClassifier")
sml_SmlEStructuralFeature = Class(name="sml_SmlEStructuralFeature")
sml_RoleBindingConstraint = Class(name="sml_RoleBindingConstraint")
sml_Interaction = Class(name="sml_Interaction")
sml_BindingExpression = Class(name="sml_BindingExpression")
sml_EnumRanges = Class(name="sml_EnumRanges")
sml_FeatureAccessBindingExpression = Class(name="sml_FeatureAccessBindingExpression")
BindingExpression = Class(name="BindingExpression")
sml_FeatureAccess = Class(name="sml_FeatureAccess")
sml_InteractionFragment = Class(name="sml_InteractionFragment")
sml_VariableFragment = Class(name="sml_VariableFragment")
InteractionFragment = Class(name="InteractionFragment")
sml_VariableExpression = Class(name="sml_VariableExpression")
sml_ConstraintBlock = Class(name="sml_ConstraintBlock")
sml_ModalMessage = Class(name="sml_ModalMessage")
sml_ParameterBinding = Class(name="sml_ParameterBinding")
sml_ParameterExpression = Class(name="sml_ParameterExpression")
sml_RandomParameter = Class(name="sml_RandomParameter")
ParameterExpression = Class(name="ParameterExpression")
sml_ExpressionParameter = Class(name="sml_ExpressionParameter")
sml_Expression = Class(name="sml_Expression")
sml_VariableBindingParameter = Class(name="sml_VariableBindingParameter")
sml_VariableValue = Class(name="sml_VariableValue")
sml_Alternative = Class(name="sml_Alternative")
sml_Case = Class(name="sml_Case")
sml_CaseCondition = Class(name="sml_CaseCondition")
sml_Loop = Class(name="sml_Loop")
sml_LoopCondition = Class(name="sml_LoopCondition")
sml_Condition = Class(name="sml_Condition")
sml_ConditionExpression = Class(name="sml_ConditionExpression")
sml_WaitCondition = Class(name="sml_WaitCondition")
Condition = Class(name="Condition")
sml_InterruptCondition = Class(name="sml_InterruptCondition")
sml_ViolationCondition = Class(name="sml_ViolationCondition")
sml_Message = Class(name="sml_Message")
sml_Parallel = Class(name="sml_Parallel")
sml_ExpressionRegion = Class(name="sml_ExpressionRegion")
ExpressionOrRegion = Class(name="ExpressionOrRegion")
sml_ExpressionOrRegion = Class(name="sml_ExpressionOrRegion")
sml_ExpressionAndVariables = Class(name="sml_ExpressionAndVariables")
ExpressionAndVariables = Class(name="ExpressionAndVariables")
sml_VariableDeclaration = Class(name="sml_VariableDeclaration")
sml_TypedVariableDeclaration = Class(name="sml_TypedVariableDeclaration")
VariableExpression = Class(name="VariableExpression")
sml_VariableAssignment = Class(name="sml_VariableAssignment")
sml_Value = Class(name="sml_Value")
Expression = Class(name="Expression")
sml_IntegerValue = Class(name="sml_IntegerValue")
Value = Class(name="Value")
sml_BooleanValue = Class(name="sml_BooleanValue")
sml_Document = Class(name="sml_Document")
sml_NullValue = Class(name="sml_NullValue")
sml_Variable = Class(name="sml_Variable")
sml_CollectionAccess = Class(name="sml_CollectionAccess")
sml_StructuralFeatureValue = Class(name="sml_StructuralFeatureValue")
sml_BinaryOperationExpression = Class(name="sml_BinaryOperationExpression")
sml_StringValue = Class(name="sml_StringValue")
sml_EnumValue = Class(name="sml_EnumValue")
sml_UnaryOperationExpression = Class(name="sml_UnaryOperationExpression")

# sml_Specification class attributes and methods
sml_Specification_name: Property = Property(name="name", type=StringType)
sml_Specification.attributes={sml_Specification_name}

# sml_Import class attributes and methods
sml_Import_importURI: Property = Property(name="importURI", type=StringType)
sml_Import.attributes={sml_Import_importURI}

# sml_SmlEPackage class attributes and methods
sml_SmlEPackage_name: Property = Property(name="name", type=StringType)
sml_SmlEPackage.attributes={sml_SmlEPackage_name}

# sml_SmlEClass class attributes and methods
sml_SmlEClass_name: Property = Property(name="name", type=StringType)
sml_SmlEClass.attributes={sml_SmlEClass_name}

# sml_SmlETypedElement class attributes and methods
sml_SmlETypedElement_name: Property = Property(name="name", type=StringType)
sml_SmlETypedElement.attributes={sml_SmlETypedElement_name}

# sml_EventParameterRanges class attributes and methods

# sml_Collaboration class attributes and methods
sml_Collaboration_name: Property = Property(name="name", type=StringType)
sml_Collaboration.attributes={sml_Collaboration_name}

# sml_SmlEEnum class attributes and methods
sml_SmlEEnum_name: Property = Property(name="name", type=StringType)
sml_SmlEEnum.attributes={sml_SmlEEnum_name}

# sml_SmlEEnumLiteral class attributes and methods
sml_SmlEEnumLiteral_name: Property = Property(name="name", type=StringType)
sml_SmlEEnumLiteral.attributes={sml_SmlEEnumLiteral_name}

# sml_Role class attributes and methods
sml_Role_static: Property = Property(name="static", type=BooleanType)
sml_Role_name: Property = Property(name="name", type=StringType)
sml_Role.attributes={sml_Role_name, sml_Role_static}

# sml_Scenario class attributes and methods
sml_Scenario_singular: Property = Property(name="singular", type=BooleanType)
sml_Scenario_kind: Property = Property(name="kind", type=StringType)
sml_Scenario_name: Property = Property(name="name", type=StringType)
sml_Scenario.attributes={sml_Scenario_kind, sml_Scenario_name, sml_Scenario_singular}

# sml_RangesForParameter class attributes and methods

# sml_AbstractRanges class attributes and methods

# sml_IntegerRanges class attributes and methods
sml_IntegerRanges_min: Property = Property(name="min", type=IntegerType)
sml_IntegerRanges_max: Property = Property(name="max", type=IntegerType)
sml_IntegerRanges_values: Property = Property(name="values", type=IntegerType)
sml_IntegerRanges.attributes={sml_IntegerRanges_values, sml_IntegerRanges_min, sml_IntegerRanges_max}

# AbstractRanges class attributes and methods

# sml_StringRanges class attributes and methods
sml_StringRanges_values: Property = Property(name="values", type=StringType)
sml_StringRanges.attributes={sml_StringRanges_values}

# sml_SmlEClassifier class attributes and methods
sml_SmlEClassifier_name: Property = Property(name="name", type=StringType)
sml_SmlEClassifier.attributes={sml_SmlEClassifier_name}

# sml_SmlEStructuralFeature class attributes and methods
sml_SmlEStructuralFeature_name: Property = Property(name="name", type=StringType)
sml_SmlEStructuralFeature.attributes={sml_SmlEStructuralFeature_name}

# sml_RoleBindingConstraint class attributes and methods

# sml_Interaction class attributes and methods

# sml_BindingExpression class attributes and methods

# sml_EnumRanges class attributes and methods

# sml_FeatureAccessBindingExpression class attributes and methods

# BindingExpression class attributes and methods

# sml_FeatureAccess class attributes and methods

# sml_InteractionFragment class attributes and methods

# sml_VariableFragment class attributes and methods

# InteractionFragment class attributes and methods

# sml_VariableExpression class attributes and methods

# sml_ConstraintBlock class attributes and methods

# sml_ModalMessage class attributes and methods
sml_ModalMessage_strict: Property = Property(name="strict", type=BooleanType)
sml_ModalMessage_requested: Property = Property(name="requested", type=BooleanType)
sml_ModalMessage.attributes={sml_ModalMessage_strict, sml_ModalMessage_requested}

# sml_ParameterBinding class attributes and methods

# sml_ParameterExpression class attributes and methods

# sml_RandomParameter class attributes and methods

# ParameterExpression class attributes and methods

# sml_ExpressionParameter class attributes and methods

# sml_Expression class attributes and methods

# sml_VariableBindingParameter class attributes and methods

# sml_VariableValue class attributes and methods

# sml_Alternative class attributes and methods

# sml_Case class attributes and methods

# sml_CaseCondition class attributes and methods

# sml_Loop class attributes and methods

# sml_LoopCondition class attributes and methods

# sml_Condition class attributes and methods

# sml_ConditionExpression class attributes and methods

# sml_WaitCondition class attributes and methods
sml_WaitCondition_strict: Property = Property(name="strict", type=BooleanType)
sml_WaitCondition_requested: Property = Property(name="requested", type=BooleanType)
sml_WaitCondition.attributes={sml_WaitCondition_strict, sml_WaitCondition_requested}

# Condition class attributes and methods

# sml_InterruptCondition class attributes and methods

# sml_ViolationCondition class attributes and methods

# sml_Message class attributes and methods

# sml_Parallel class attributes and methods

# sml_ExpressionRegion class attributes and methods

# ExpressionOrRegion class attributes and methods

# sml_ExpressionOrRegion class attributes and methods

# sml_ExpressionAndVariables class attributes and methods

# ExpressionAndVariables class attributes and methods

# sml_VariableDeclaration class attributes and methods
sml_VariableDeclaration_name: Property = Property(name="name", type=StringType)
sml_VariableDeclaration.attributes={sml_VariableDeclaration_name}

# sml_TypedVariableDeclaration class attributes and methods
sml_TypedVariableDeclaration_name: Property = Property(name="name", type=StringType)
sml_TypedVariableDeclaration.attributes={sml_TypedVariableDeclaration_name}

# VariableExpression class attributes and methods

# sml_VariableAssignment class attributes and methods

# sml_Value class attributes and methods

# Expression class attributes and methods

# sml_IntegerValue class attributes and methods
sml_IntegerValue_value: Property = Property(name="value", type=IntegerType)
sml_IntegerValue.attributes={sml_IntegerValue_value}

# Value class attributes and methods

# sml_BooleanValue class attributes and methods
sml_BooleanValue_value: Property = Property(name="value", type=BooleanType)
sml_BooleanValue.attributes={sml_BooleanValue_value}

# sml_Document class attributes and methods

# sml_NullValue class attributes and methods

# sml_Variable class attributes and methods
sml_Variable_name: Property = Property(name="name", type=StringType)
sml_Variable.attributes={sml_Variable_name}

# sml_CollectionAccess class attributes and methods
sml_CollectionAccess_collectionOperation: Property = Property(name="collectionOperation", type=StringType)
sml_CollectionAccess.attributes={sml_CollectionAccess_collectionOperation}

# sml_StructuralFeatureValue class attributes and methods

# sml_BinaryOperationExpression class attributes and methods
sml_BinaryOperationExpression_operator: Property = Property(name="operator", type=StringType)
sml_BinaryOperationExpression.attributes={sml_BinaryOperationExpression_operator}

# sml_StringValue class attributes and methods
sml_StringValue_value: Property = Property(name="value", type=StringType)
sml_StringValue.attributes={sml_StringValue_value}

# sml_EnumValue class attributes and methods

# sml_UnaryOperationExpression class attributes and methods
sml_UnaryOperationExpression_operator: Property = Property(name="operator", type=StringType)
sml_UnaryOperationExpression.attributes={sml_UnaryOperationExpression_operator}

# Relationships
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="sml_Import", type=sml_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_Specification", type=sml_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
domains1: BinaryAssociation = BinaryAssociation(
    name="domains1",
    ends={
        Property(name="sml_SmlEPackage", type=sml_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_Specification2", type=sml_SmlEPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controllableEClasses3: BinaryAssociation = BinaryAssociation(
    name="controllableEClasses3",
    ends={
        Property(name="sml_SmlEClass", type=sml_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_Specification4", type=sml_SmlEClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uncontrollableEClasses5: BinaryAssociation = BinaryAssociation(
    name="uncontrollableEClasses5",
    ends={
        Property(name="sml_SmlEClass7", type=sml_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_Specification6", type=sml_SmlEClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nonSpontaneousOperations8: BinaryAssociation = BinaryAssociation(
    name="nonSpontaneousOperations8",
    ends={
        Property(name="sml_SmlETypedElement", type=sml_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_Specification9", type=sml_SmlETypedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventParameterRanges10: BinaryAssociation = BinaryAssociation(
    name="eventParameterRanges10",
    ends={
        Property(name="sml_EventParameterRanges", type=sml_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_Specification11", type=sml_EventParameterRanges, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containedCollaborations12: BinaryAssociation = BinaryAssociation(
    name="containedCollaborations12",
    ends={
        Property(name="sml_Collaboration", type=sml_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_Specification13", type=sml_Collaboration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
includedCollaborations14: BinaryAssociation = BinaryAssociation(
    name="includedCollaborations14",
    ends={
        Property(name="sml_Collaboration16", type=sml_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_Specification15", type=sml_Collaboration, multiplicity=Multiplicity(0, 9999))
    }
)
roles17: BinaryAssociation = BinaryAssociation(
    name="roles17",
    ends={
        Property(name="sml_Role", type=sml_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_Collaboration18", type=sml_Role, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scenarios19: BinaryAssociation = BinaryAssociation(
    name="scenarios19",
    ends={
        Property(name="sml_Scenario", type=sml_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_Collaboration20", type=sml_Scenario, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports21: BinaryAssociation = BinaryAssociation(
    name="imports21",
    ends={
        Property(name="sml_Import23", type=sml_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_Collaboration22", type=sml_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
domains24: BinaryAssociation = BinaryAssociation(
    name="domains24",
    ends={
        Property(name="sml_SmlEPackage26", type=sml_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_Collaboration25", type=sml_SmlEPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event27: BinaryAssociation = BinaryAssociation(
    name="event27",
    ends={
        Property(name="sml_SmlETypedElement29", type=sml_EventParameterRanges, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_EventParameterRanges28", type=sml_SmlETypedElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rangesForParameter30: BinaryAssociation = BinaryAssociation(
    name="rangesForParameter30",
    ends={
        Property(name="sml_RangesForParameter", type=sml_EventParameterRanges, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_EventParameterRanges31", type=sml_RangesForParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter32: BinaryAssociation = BinaryAssociation(
    name="parameter32",
    ends={
        Property(name="sml_SmlETypedElement34", type=sml_RangesForParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_RangesForParameter33", type=sml_SmlETypedElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ranges35: BinaryAssociation = BinaryAssociation(
    name="ranges35",
    ends={
        Property(name="sml_AbstractRanges", type=sml_RangesForParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_RangesForParameter36", type=sml_AbstractRanges, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
roleBindings41: BinaryAssociation = BinaryAssociation(
    name="roleBindings41",
    ends={
        Property(name="sml_RoleBindingConstraint", type=sml_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_Scenario42", type=sml_RoleBindingConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedInteraction43: BinaryAssociation = BinaryAssociation(
    name="ownedInteraction43",
    ends={
        Property(name="sml_Interaction", type=sml_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_Scenario44", type=sml_Interaction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
role45: BinaryAssociation = BinaryAssociation(
    name="role45",
    ends={
        Property(name="sml_Role47", type=sml_RoleBindingConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_RoleBindingConstraint46", type=sml_Role, multiplicity=Multiplicity(0, 1))
    }
)
bindingExpression48: BinaryAssociation = BinaryAssociation(
    name="bindingExpression48",
    ends={
        Property(name="sml_BindingExpression", type=sml_RoleBindingConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_RoleBindingConstraint49", type=sml_BindingExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
values37: BinaryAssociation = BinaryAssociation(
    name="values37",
    ends={
        Property(name="sml_SmlEEnumLiteral", type=sml_EnumRanges, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_EnumRanges", type=sml_SmlEEnumLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type38: BinaryAssociation = BinaryAssociation(
    name="type38",
    ends={
        Property(name="sml_SmlEClass40", type=sml_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_Role39", type=sml_SmlEClass, multiplicity=Multiplicity(0, 1))
    }
)
featureaccess50: BinaryAssociation = BinaryAssociation(
    name="featureaccess50",
    ends={
        Property(name="sml_FeatureAccess", type=sml_FeatureAccessBindingExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_FeatureAccessBindingExpression", type=sml_FeatureAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression51: BinaryAssociation = BinaryAssociation(
    name="expression51",
    ends={
        Property(name="sml_VariableExpression", type=sml_VariableFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_VariableFragment", type=sml_VariableExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fragments52: BinaryAssociation = BinaryAssociation(
    name="fragments52",
    ends={
        Property(name="sml_InteractionFragment", type=sml_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_Interaction53", type=sml_InteractionFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints54: BinaryAssociation = BinaryAssociation(
    name="constraints54",
    ends={
        Property(name="sml_ConstraintBlock", type=sml_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_Interaction55", type=sml_ConstraintBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modelElement61: BinaryAssociation = BinaryAssociation(
    name="modelElement61",
    ends={
        Property(name="sml_SmlETypedElement63", type=sml_ModalMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_ModalMessage62", type=sml_SmlETypedElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters64: BinaryAssociation = BinaryAssociation(
    name="parameters64",
    ends={
        Property(name="sml_ParameterBinding", type=sml_ModalMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_ModalMessage65", type=sml_ParameterBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindingExpression66: BinaryAssociation = BinaryAssociation(
    name="bindingExpression66",
    ends={
        Property(name="sml_ParameterExpression", type=sml_ParameterBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_ParameterBinding67", type=sml_ParameterExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value68: BinaryAssociation = BinaryAssociation(
    name="value68",
    ends={
        Property(name="sml_Expression", type=sml_ExpressionParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_ExpressionParameter", type=sml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable69: BinaryAssociation = BinaryAssociation(
    name="variable69",
    ends={
        Property(name="sml_VariableValue", type=sml_VariableBindingParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_VariableBindingParameter", type=sml_VariableValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cases70: BinaryAssociation = BinaryAssociation(
    name="cases70",
    ends={
        Property(name="sml_Case", type=sml_Alternative, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_Alternative", type=sml_Case, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
caseCondition71: BinaryAssociation = BinaryAssociation(
    name="caseCondition71",
    ends={
        Property(name="sml_CaseCondition", type=sml_Case, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_Case72", type=sml_CaseCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
caseInteraction73: BinaryAssociation = BinaryAssociation(
    name="caseInteraction73",
    ends={
        Property(name="sml_Interaction75", type=sml_Case, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_Case74", type=sml_Interaction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sender56: BinaryAssociation = BinaryAssociation(
    name="sender56",
    ends={
        Property(name="sml_Role57", type=sml_ModalMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_ModalMessage", type=sml_Role, multiplicity=Multiplicity(0, 1))
    }
)
receiver58: BinaryAssociation = BinaryAssociation(
    name="receiver58",
    ends={
        Property(name="sml_Role60", type=sml_ModalMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_ModalMessage59", type=sml_Role, multiplicity=Multiplicity(0, 1))
    }
)
conditionExpression82: BinaryAssociation = BinaryAssociation(
    name="conditionExpression82",
    ends={
        Property(name="sml_ConditionExpression", type=sml_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_Condition", type=sml_ConditionExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditionExpression83: BinaryAssociation = BinaryAssociation(
    name="conditionExpression83",
    ends={
        Property(name="sml_ConditionExpression85", type=sml_LoopCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_LoopCondition84", type=sml_ConditionExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditionExpression86: BinaryAssociation = BinaryAssociation(
    name="conditionExpression86",
    ends={
        Property(name="sml_ConditionExpression88", type=sml_CaseCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_CaseCondition87", type=sml_ConditionExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression89: BinaryAssociation = BinaryAssociation(
    name="expression89",
    ends={
        Property(name="sml_Expression91", type=sml_ConditionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_ConditionExpression90", type=sml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
consider92: BinaryAssociation = BinaryAssociation(
    name="consider92",
    ends={
        Property(name="sml_Message", type=sml_ConstraintBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_ConstraintBlock93", type=sml_Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ignore94: BinaryAssociation = BinaryAssociation(
    name="ignore94",
    ends={
        Property(name="sml_Message96", type=sml_ConstraintBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_ConstraintBlock95", type=sml_Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
forbidden97: BinaryAssociation = BinaryAssociation(
    name="forbidden97",
    ends={
        Property(name="sml_Message99", type=sml_ConstraintBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_ConstraintBlock98", type=sml_Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interrupt100: BinaryAssociation = BinaryAssociation(
    name="interrupt100",
    ends={
        Property(name="sml_Message102", type=sml_ConstraintBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_ConstraintBlock101", type=sml_Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sender103: BinaryAssociation = BinaryAssociation(
    name="sender103",
    ends={
        Property(name="sml_Role105", type=sml_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_Message104", type=sml_Role, multiplicity=Multiplicity(0, 1))
    }
)
receiver106: BinaryAssociation = BinaryAssociation(
    name="receiver106",
    ends={
        Property(name="sml_Role108", type=sml_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_Message107", type=sml_Role, multiplicity=Multiplicity(0, 1))
    }
)
loopCondition76: BinaryAssociation = BinaryAssociation(
    name="loopCondition76",
    ends={
        Property(name="sml_LoopCondition", type=sml_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_Loop", type=sml_LoopCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bodyInteraction77: BinaryAssociation = BinaryAssociation(
    name="bodyInteraction77",
    ends={
        Property(name="sml_Interaction79", type=sml_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_Loop78", type=sml_Interaction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parallelInteraction80: BinaryAssociation = BinaryAssociation(
    name="parallelInteraction80",
    ends={
        Property(name="sml_Interaction81", type=sml_Parallel, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_Parallel", type=sml_Interaction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
domains117: BinaryAssociation = BinaryAssociation(
    name="domains117",
    ends={
        Property(name="sml_SmlEPackage119", type=sml_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_Document118", type=sml_SmlEPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressions120: BinaryAssociation = BinaryAssociation(
    name="expressions120",
    ends={
        Property(name="sml_ExpressionRegion", type=sml_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_Document121", type=sml_ExpressionRegion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressions122: BinaryAssociation = BinaryAssociation(
    name="expressions122",
    ends={
        Property(name="sml_ExpressionOrRegion", type=sml_ExpressionRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_ExpressionRegion123", type=sml_ExpressionOrRegion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression124: BinaryAssociation = BinaryAssociation(
    name="expression124",
    ends={
        Property(name="sml_Expression126", type=sml_VariableExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_VariableExpression125", type=sml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression127: BinaryAssociation = BinaryAssociation(
    name="expression127",
    ends={
        Property(name="sml_Expression128", type=sml_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_VariableDeclaration", type=sml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type129: BinaryAssociation = BinaryAssociation(
    name="type129",
    ends={
        Property(name="sml_SmlEClassifier", type=sml_TypedVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_TypedVariableDeclaration", type=sml_SmlEClassifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable130: BinaryAssociation = BinaryAssociation(
    name="variable130",
    ends={
        Property(name="sml_VariableDeclaration131", type=sml_VariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_VariableAssignment", type=sml_VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
modelElement109: BinaryAssociation = BinaryAssociation(
    name="modelElement109",
    ends={
        Property(name="sml_SmlETypedElement111", type=sml_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_Message110", type=sml_SmlETypedElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters112: BinaryAssociation = BinaryAssociation(
    name="parameters112",
    ends={
        Property(name="sml_ParameterBinding114", type=sml_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_Message113", type=sml_ParameterBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports115: BinaryAssociation = BinaryAssociation(
    name="imports115",
    ends={
        Property(name="sml_Import116", type=sml_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_Document", type=sml_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value133: BinaryAssociation = BinaryAssociation(
    name="value133",
    ends={
        Property(name="sml_SmlEEnumLiteral135", type=sml_EnumValue, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_EnumValue134", type=sml_SmlEEnumLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value136: BinaryAssociation = BinaryAssociation(
    name="value136",
    ends={
        Property(name="sml_Variable", type=sml_VariableValue, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_VariableValue137", type=sml_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter138: BinaryAssociation = BinaryAssociation(
    name="parameter138",
    ends={
        Property(name="sml_Expression139", type=sml_CollectionAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_CollectionAccess", type=sml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable140: BinaryAssociation = BinaryAssociation(
    name="variable140",
    ends={
        Property(name="sml_Variable142", type=sml_FeatureAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_FeatureAccess141", type=sml_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value143: BinaryAssociation = BinaryAssociation(
    name="value143",
    ends={
        Property(name="sml_StructuralFeatureValue", type=sml_FeatureAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_FeatureAccess144", type=sml_StructuralFeatureValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
collectionAccess145: BinaryAssociation = BinaryAssociation(
    name="collectionAccess145",
    ends={
        Property(name="sml_CollectionAccess147", type=sml_FeatureAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_FeatureAccess146", type=sml_CollectionAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value148: BinaryAssociation = BinaryAssociation(
    name="value148",
    ends={
        Property(name="sml_SmlEStructuralFeature", type=sml_StructuralFeatureValue, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_StructuralFeatureValue149", type=sml_SmlEStructuralFeature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left150: BinaryAssociation = BinaryAssociation(
    name="left150",
    ends={
        Property(name="sml_Expression151", type=sml_BinaryOperationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_BinaryOperationExpression", type=sml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type132: BinaryAssociation = BinaryAssociation(
    name="type132",
    ends={
        Property(name="sml_SmlEEnum", type=sml_EnumValue, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_EnumValue", type=sml_SmlEEnum, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand155: BinaryAssociation = BinaryAssociation(
    name="operand155",
    ends={
        Property(name="sml_Expression156", type=sml_UnaryOperationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_UnaryOperationExpression", type=sml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right152: BinaryAssociation = BinaryAssociation(
    name="right152",
    ends={
        Property(name="sml_Expression154", type=sml_BinaryOperationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sml_BinaryOperationExpression153", type=sml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_sml_IntegerRanges_AbstractRanges = Generalization(general=AbstractRanges, specific=sml_IntegerRanges)
gen_sml_StringRanges_AbstractRanges = Generalization(general=AbstractRanges, specific=sml_StringRanges)
gen_sml_EnumRanges_AbstractRanges = Generalization(general=AbstractRanges, specific=sml_EnumRanges)
gen_sml_FeatureAccessBindingExpression_BindingExpression = Generalization(general=BindingExpression, specific=sml_FeatureAccessBindingExpression)
gen_sml_VariableFragment_InteractionFragment = Generalization(general=InteractionFragment, specific=sml_VariableFragment)
gen_sml_Interaction_InteractionFragment = Generalization(general=InteractionFragment, specific=sml_Interaction)
gen_sml_ModalMessage_InteractionFragment = Generalization(general=InteractionFragment, specific=sml_ModalMessage)
gen_sml_RandomParameter_ParameterExpression = Generalization(general=ParameterExpression, specific=sml_RandomParameter)
gen_sml_ExpressionParameter_ParameterExpression = Generalization(general=ParameterExpression, specific=sml_ExpressionParameter)
gen_sml_VariableBindingParameter_ParameterExpression = Generalization(general=ParameterExpression, specific=sml_VariableBindingParameter)
gen_sml_Alternative_InteractionFragment = Generalization(general=InteractionFragment, specific=sml_Alternative)
gen_sml_Loop_InteractionFragment = Generalization(general=InteractionFragment, specific=sml_Loop)
gen_sml_Condition_InteractionFragment = Generalization(general=InteractionFragment, specific=sml_Condition)
gen_sml_WaitCondition_Condition = Generalization(general=Condition, specific=sml_WaitCondition)
gen_sml_InterruptCondition_Condition = Generalization(general=Condition, specific=sml_InterruptCondition)
gen_sml_ViolationCondition_Condition = Generalization(general=Condition, specific=sml_ViolationCondition)
gen_sml_Parallel_InteractionFragment = Generalization(general=InteractionFragment, specific=sml_Parallel)
gen_sml_ExpressionRegion_ExpressionOrRegion = Generalization(general=ExpressionOrRegion, specific=sml_ExpressionRegion)
gen_sml_ExpressionAndVariables_ExpressionOrRegion = Generalization(general=ExpressionOrRegion, specific=sml_ExpressionAndVariables)
gen_sml_VariableExpression_ExpressionAndVariables = Generalization(general=ExpressionAndVariables, specific=sml_VariableExpression)
gen_sml_TypedVariableDeclaration_VariableExpression = Generalization(general=VariableExpression, specific=sml_TypedVariableDeclaration)
gen_sml_VariableAssignment_VariableExpression = Generalization(general=VariableExpression, specific=sml_VariableAssignment)
gen_sml_Expression_ExpressionAndVariables = Generalization(general=ExpressionAndVariables, specific=sml_Expression)
gen_sml_Value_Expression = Generalization(general=Expression, specific=sml_Value)
gen_sml_IntegerValue_Value = Generalization(general=Value, specific=sml_IntegerValue)
gen_sml_BooleanValue_Value = Generalization(general=Value, specific=sml_BooleanValue)
gen_sml_NullValue_Value = Generalization(general=Value, specific=sml_NullValue)
gen_sml_VariableValue_Value = Generalization(general=Value, specific=sml_VariableValue)
gen_sml_FeatureAccess_Value = Generalization(general=Value, specific=sml_FeatureAccess)
gen_sml_BinaryOperationExpression_Expression = Generalization(general=Expression, specific=sml_BinaryOperationExpression)
gen_sml_StringValue_Value = Generalization(general=Value, specific=sml_StringValue)
gen_sml_EnumValue_Value = Generalization(general=Value, specific=sml_EnumValue)
gen_sml_UnaryOperationExpression_Expression = Generalization(general=Expression, specific=sml_UnaryOperationExpression)

# Domain Model
domain_model = DomainModel(
    name="sml",
    types={sml_Specification, sml_Import, sml_SmlEPackage, sml_SmlEClass, sml_SmlETypedElement, sml_EventParameterRanges, sml_Collaboration, sml_SmlEEnum, sml_SmlEEnumLiteral, sml_Role, sml_Scenario, sml_RangesForParameter, sml_AbstractRanges, sml_IntegerRanges, AbstractRanges, sml_StringRanges, sml_SmlEClassifier, sml_SmlEStructuralFeature, sml_RoleBindingConstraint, sml_Interaction, sml_BindingExpression, sml_EnumRanges, sml_FeatureAccessBindingExpression, BindingExpression, sml_FeatureAccess, sml_InteractionFragment, sml_VariableFragment, InteractionFragment, sml_VariableExpression, sml_ConstraintBlock, sml_ModalMessage, sml_ParameterBinding, sml_ParameterExpression, sml_RandomParameter, ParameterExpression, sml_ExpressionParameter, sml_Expression, sml_VariableBindingParameter, sml_VariableValue, sml_Alternative, sml_Case, sml_CaseCondition, sml_Loop, sml_LoopCondition, sml_Condition, sml_ConditionExpression, sml_WaitCondition, Condition, sml_InterruptCondition, sml_ViolationCondition, sml_Message, sml_Parallel, sml_ExpressionRegion, ExpressionOrRegion, sml_ExpressionOrRegion, sml_ExpressionAndVariables, ExpressionAndVariables, sml_VariableDeclaration, sml_TypedVariableDeclaration, VariableExpression, sml_VariableAssignment, sml_Value, Expression, sml_IntegerValue, Value, sml_BooleanValue, sml_Document, sml_NullValue, sml_Variable, sml_CollectionAccess, sml_StructuralFeatureValue, sml_BinaryOperationExpression, sml_StringValue, sml_EnumValue, sml_UnaryOperationExpression, ScenarioKind, CollectionOperation},
    associations={imports0, domains1, controllableEClasses3, uncontrollableEClasses5, nonSpontaneousOperations8, eventParameterRanges10, containedCollaborations12, includedCollaborations14, roles17, scenarios19, imports21, domains24, event27, rangesForParameter30, parameter32, ranges35, roleBindings41, ownedInteraction43, role45, bindingExpression48, values37, type38, featureaccess50, expression51, fragments52, constraints54, modelElement61, parameters64, bindingExpression66, value68, variable69, cases70, caseCondition71, caseInteraction73, sender56, receiver58, conditionExpression82, conditionExpression83, conditionExpression86, expression89, consider92, ignore94, forbidden97, interrupt100, sender103, receiver106, loopCondition76, bodyInteraction77, parallelInteraction80, domains117, expressions120, expressions122, expression124, expression127, type129, variable130, modelElement109, parameters112, imports115, value133, value136, parameter138, variable140, value143, collectionAccess145, value148, left150, type132, operand155, right152},
    generalizations={gen_sml_IntegerRanges_AbstractRanges, gen_sml_StringRanges_AbstractRanges, gen_sml_EnumRanges_AbstractRanges, gen_sml_FeatureAccessBindingExpression_BindingExpression, gen_sml_VariableFragment_InteractionFragment, gen_sml_Interaction_InteractionFragment, gen_sml_ModalMessage_InteractionFragment, gen_sml_RandomParameter_ParameterExpression, gen_sml_ExpressionParameter_ParameterExpression, gen_sml_VariableBindingParameter_ParameterExpression, gen_sml_Alternative_InteractionFragment, gen_sml_Loop_InteractionFragment, gen_sml_Condition_InteractionFragment, gen_sml_WaitCondition_Condition, gen_sml_InterruptCondition_Condition, gen_sml_ViolationCondition_Condition, gen_sml_Parallel_InteractionFragment, gen_sml_ExpressionRegion_ExpressionOrRegion, gen_sml_ExpressionAndVariables_ExpressionOrRegion, gen_sml_VariableExpression_ExpressionAndVariables, gen_sml_TypedVariableDeclaration_VariableExpression, gen_sml_VariableAssignment_VariableExpression, gen_sml_Expression_ExpressionAndVariables, gen_sml_Value_Expression, gen_sml_IntegerValue_Value, gen_sml_BooleanValue_Value, gen_sml_NullValue_Value, gen_sml_VariableValue_Value, gen_sml_FeatureAccess_Value, gen_sml_BinaryOperationExpression_Expression, gen_sml_StringValue_Value, gen_sml_EnumValue_Value, gen_sml_UnaryOperationExpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)