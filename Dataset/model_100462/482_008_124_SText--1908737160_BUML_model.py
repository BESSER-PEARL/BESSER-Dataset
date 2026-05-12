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
Direction: Enumeration = Enumeration(
    name="Direction",
    literals={
            EnumerationLiteral(name="LOCAL"),
			EnumerationLiteral(name="IN"),
			EnumerationLiteral(name="OUT")
    }
)

TimeEventType: Enumeration = Enumeration(
    name="TimeEventType",
    literals={
            EnumerationLiteral(name="after"),
			EnumerationLiteral(name="every")
    }
)

AssignmentOperator: Enumeration = Enumeration(
    name="AssignmentOperator",
    literals={
            EnumerationLiteral(name="assign"),
			EnumerationLiteral(name="multAssign"),
			EnumerationLiteral(name="divAssign"),
			EnumerationLiteral(name="modAssign"),
			EnumerationLiteral(name="addAssign"),
			EnumerationLiteral(name="subAssign"),
			EnumerationLiteral(name="leftShiftAssign"),
			EnumerationLiteral(name="rightShiftAssign"),
			EnumerationLiteral(name="andAssign"),
			EnumerationLiteral(name="xorAssign"),
			EnumerationLiteral(name="orAssign")
    }
)

ShiftOperator: Enumeration = Enumeration(
    name="ShiftOperator",
    literals={
            EnumerationLiteral(name="left"),
			EnumerationLiteral(name="right")
    }
)

AdditiveOperator: Enumeration = Enumeration(
    name="AdditiveOperator",
    literals={
            EnumerationLiteral(name="plus"),
			EnumerationLiteral(name="minus")
    }
)

MultiplicativeOperator: Enumeration = Enumeration(
    name="MultiplicativeOperator",
    literals={
            EnumerationLiteral(name="mul"),
			EnumerationLiteral(name="div"),
			EnumerationLiteral(name="mod")
    }
)

UnaryOperator: Enumeration = Enumeration(
    name="UnaryOperator",
    literals={
            EnumerationLiteral(name="positive"),
			EnumerationLiteral(name="negative"),
			EnumerationLiteral(name="complement")
    }
)

RelationalOperator: Enumeration = Enumeration(
    name="RelationalOperator",
    literals={
            EnumerationLiteral(name="smaller"),
			EnumerationLiteral(name="smallerEqual"),
			EnumerationLiteral(name="greater"),
			EnumerationLiteral(name="greaterEqual"),
			EnumerationLiteral(name="equals"),
			EnumerationLiteral(name="notEquals")
    }
)

TimeUnit: Enumeration = Enumeration(
    name="TimeUnit",
    literals={
            EnumerationLiteral(name="second"),
			EnumerationLiteral(name="millisecond"),
			EnumerationLiteral(name="microsecond"),
			EnumerationLiteral(name="nanosecond")
    }
)

# Classes
ScopedElement = Class(name="ScopedElement")
stext_Root = Class(name="stext_Root")
stext_DefRoot = Class(name="stext_DefRoot")
stext_StatechartRoot = Class(name="stext_StatechartRoot")
DefRoot = Class(name="DefRoot")
stext_StatechartSpecification = Class(name="stext_StatechartSpecification")
stext_StateRoot = Class(name="stext_StateRoot")
stext_StateSpecification = Class(name="stext_StateSpecification")
stext_TransitionRoot = Class(name="stext_TransitionRoot")
stext_TransitionSpecification = Class(name="stext_TransitionSpecification")
stext_Entrypoint = Class(name="stext_Entrypoint")
stext_Scope = Class(name="stext_Scope")
stext_TransitionReaction = Class(name="stext_TransitionReaction")
stext_StatechartScope = Class(name="stext_StatechartScope")
Scope = Class(name="Scope")
stext_InterfaceScope = Class(name="stext_InterfaceScope")
StatechartScope = Class(name="StatechartScope")
NamedElement = Class(name="NamedElement")
stext_InternalScope = Class(name="stext_InternalScope")
stext_EventDefinition = Class(name="stext_EventDefinition")
Event = Class(name="Event")
stext_VariableDefinition = Class(name="stext_VariableDefinition")
Variable = Class(name="Variable")
Property_ = Class(name="Property")
stext_Expression = Class(name="stext_Expression")
stext_OperationDefinition = Class(name="stext_OperationDefinition")
Declaration = Class(name="Declaration")
Operation = Class(name="Operation")
stext_LocalReaction = Class(name="stext_LocalReaction")
Reaction = Class(name="Reaction")
stext_ReactionProperties = Class(name="stext_ReactionProperties")
stext_ReactionProperty = Class(name="stext_ReactionProperty")
stext_EntryPointSpec = Class(name="stext_EntryPointSpec")
ReactionProperty = Class(name="ReactionProperty")
stext_ExitPointSpec = Class(name="stext_ExitPointSpec")
stext_Exitpoint = Class(name="stext_Exitpoint")
stext_EventSpec = Class(name="stext_EventSpec")
stext_RegularEventSpec = Class(name="stext_RegularEventSpec")
EventSpec = Class(name="EventSpec")
stext_TimeEventSpec = Class(name="stext_TimeEventSpec")
stext_BuiltinEventSpec = Class(name="stext_BuiltinEventSpec")
stext_EntryEvent = Class(name="stext_EntryEvent")
BuiltinEventSpec = Class(name="BuiltinEventSpec")
stext_ExitEvent = Class(name="stext_ExitEvent")
stext_OnCycleEvent = Class(name="stext_OnCycleEvent")
stext_AlwaysEvent = Class(name="stext_AlwaysEvent")
stext_DefaultEvent = Class(name="stext_DefaultEvent")
Statement = Class(name="Statement")
stext_Literal = Class(name="stext_Literal")
stext_BoolLiteral = Class(name="stext_BoolLiteral")
Literal = Class(name="Literal")
stext_IntLiteral = Class(name="stext_IntLiteral")
stext_RealLiteral = Class(name="stext_RealLiteral")
stext_HexLiteral = Class(name="stext_HexLiteral")
stext_StringLiteral = Class(name="stext_StringLiteral")
stext_SimpleScope = Class(name="stext_SimpleScope")
stext_ReactionTrigger = Class(name="stext_ReactionTrigger")
Trigger = Class(name="Trigger")
stext_LogicalNotExpression = Class(name="stext_LogicalNotExpression")
stext_ReactionEffect = Class(name="stext_ReactionEffect")
Effect = Class(name="Effect")
stext_EventRaisingExpression = Class(name="stext_EventRaisingExpression")
Expression = Class(name="Expression")
stext_AssignmentExpression = Class(name="stext_AssignmentExpression")
stext_ConditionalExpression = Class(name="stext_ConditionalExpression")
stext_LogicalOrExpression = Class(name="stext_LogicalOrExpression")
stext_LogicalAndExpression = Class(name="stext_LogicalAndExpression")
stext_NumericalAddSubtractExpression = Class(name="stext_NumericalAddSubtractExpression")
stext_BitwiseXorExpression = Class(name="stext_BitwiseXorExpression")
stext_BitwiseOrExpression = Class(name="stext_BitwiseOrExpression")
stext_BitwiseAndExpression = Class(name="stext_BitwiseAndExpression")
stext_LogicalRelationExpression = Class(name="stext_LogicalRelationExpression")
stext_ShiftExpression = Class(name="stext_ShiftExpression")
stext_NumericalMultiplyDivideExpression = Class(name="stext_NumericalMultiplyDivideExpression")
stext_NumericalUnaryExpression = Class(name="stext_NumericalUnaryExpression")
stext_PrimitiveValueExpression = Class(name="stext_PrimitiveValueExpression")
stext_FeatureCall = Class(name="stext_FeatureCall")
stext_EObject = Class(name="stext_EObject")
stext_ElementReferenceExpression = Class(name="stext_ElementReferenceExpression")
stext_EventValueReferenceExpression = Class(name="stext_EventValueReferenceExpression")
stext_ActiveStateReferenceExpression = Class(name="stext_ActiveStateReferenceExpression")
stext_State = Class(name="stext_State")

# ScopedElement class attributes and methods

# stext_Root class attributes and methods

# stext_DefRoot class attributes and methods

# stext_StatechartRoot class attributes and methods

# DefRoot class attributes and methods

# stext_StatechartSpecification class attributes and methods

# stext_StateRoot class attributes and methods

# stext_StateSpecification class attributes and methods

# stext_TransitionRoot class attributes and methods

# stext_TransitionSpecification class attributes and methods

# stext_Entrypoint class attributes and methods

# stext_Scope class attributes and methods

# stext_TransitionReaction class attributes and methods

# stext_StatechartScope class attributes and methods

# Scope class attributes and methods

# stext_InterfaceScope class attributes and methods

# StatechartScope class attributes and methods

# NamedElement class attributes and methods

# stext_InternalScope class attributes and methods

# stext_EventDefinition class attributes and methods
stext_EventDefinition_direction: Property = Property(name="direction", type=StringType)
stext_EventDefinition.attributes={stext_EventDefinition_direction}

# Event class attributes and methods

# stext_VariableDefinition class attributes and methods
stext_VariableDefinition_readonly: Property = Property(name="readonly", type=BooleanType)
stext_VariableDefinition_external: Property = Property(name="external", type=BooleanType)
stext_VariableDefinition.attributes={stext_VariableDefinition_external, stext_VariableDefinition_readonly}

# Variable class attributes and methods

# Property class attributes and methods

# stext_Expression class attributes and methods

# stext_OperationDefinition class attributes and methods

# Declaration class attributes and methods

# Operation class attributes and methods

# stext_LocalReaction class attributes and methods

# Reaction class attributes and methods

# stext_ReactionProperties class attributes and methods

# stext_ReactionProperty class attributes and methods

# stext_EntryPointSpec class attributes and methods

# ReactionProperty class attributes and methods

# stext_ExitPointSpec class attributes and methods

# stext_Exitpoint class attributes and methods

# stext_EventSpec class attributes and methods

# stext_RegularEventSpec class attributes and methods

# EventSpec class attributes and methods

# stext_TimeEventSpec class attributes and methods
stext_TimeEventSpec_type: Property = Property(name="type", type=StringType)
stext_TimeEventSpec_value: Property = Property(name="value", type=IntegerType)
stext_TimeEventSpec_unit: Property = Property(name="unit", type=StringType)
stext_TimeEventSpec.attributes={stext_TimeEventSpec_value, stext_TimeEventSpec_unit, stext_TimeEventSpec_type}

# stext_BuiltinEventSpec class attributes and methods

# stext_EntryEvent class attributes and methods

# BuiltinEventSpec class attributes and methods

# stext_ExitEvent class attributes and methods

# stext_OnCycleEvent class attributes and methods

# stext_AlwaysEvent class attributes and methods

# stext_DefaultEvent class attributes and methods

# Statement class attributes and methods

# stext_Literal class attributes and methods

# stext_BoolLiteral class attributes and methods
stext_BoolLiteral_value: Property = Property(name="value", type=BooleanType)
stext_BoolLiteral.attributes={stext_BoolLiteral_value}

# Literal class attributes and methods

# stext_IntLiteral class attributes and methods
stext_IntLiteral_value: Property = Property(name="value", type=IntegerType)
stext_IntLiteral.attributes={stext_IntLiteral_value}

# stext_RealLiteral class attributes and methods
stext_RealLiteral_value: Property = Property(name="value", type=FloatType)
stext_RealLiteral.attributes={stext_RealLiteral_value}

# stext_HexLiteral class attributes and methods
stext_HexLiteral_value: Property = Property(name="value", type=IntegerType)
stext_HexLiteral.attributes={stext_HexLiteral_value}

# stext_StringLiteral class attributes and methods
stext_StringLiteral_value: Property = Property(name="value", type=StringType)
stext_StringLiteral.attributes={stext_StringLiteral_value}

# stext_SimpleScope class attributes and methods

# stext_ReactionTrigger class attributes and methods

# Trigger class attributes and methods

# stext_LogicalNotExpression class attributes and methods

# stext_ReactionEffect class attributes and methods

# Effect class attributes and methods

# stext_EventRaisingExpression class attributes and methods

# Expression class attributes and methods

# stext_AssignmentExpression class attributes and methods
stext_AssignmentExpression_operator: Property = Property(name="operator", type=StringType)
stext_AssignmentExpression.attributes={stext_AssignmentExpression_operator}

# stext_ConditionalExpression class attributes and methods

# stext_LogicalOrExpression class attributes and methods

# stext_LogicalAndExpression class attributes and methods

# stext_NumericalAddSubtractExpression class attributes and methods
stext_NumericalAddSubtractExpression_operator: Property = Property(name="operator", type=StringType)
stext_NumericalAddSubtractExpression.attributes={stext_NumericalAddSubtractExpression_operator}

# stext_BitwiseXorExpression class attributes and methods

# stext_BitwiseOrExpression class attributes and methods

# stext_BitwiseAndExpression class attributes and methods

# stext_LogicalRelationExpression class attributes and methods
stext_LogicalRelationExpression_operator: Property = Property(name="operator", type=StringType)
stext_LogicalRelationExpression.attributes={stext_LogicalRelationExpression_operator}

# stext_ShiftExpression class attributes and methods
stext_ShiftExpression_operator: Property = Property(name="operator", type=StringType)
stext_ShiftExpression.attributes={stext_ShiftExpression_operator}

# stext_NumericalMultiplyDivideExpression class attributes and methods
stext_NumericalMultiplyDivideExpression_operator: Property = Property(name="operator", type=StringType)
stext_NumericalMultiplyDivideExpression.attributes={stext_NumericalMultiplyDivideExpression_operator}

# stext_NumericalUnaryExpression class attributes and methods
stext_NumericalUnaryExpression_operator: Property = Property(name="operator", type=StringType)
stext_NumericalUnaryExpression.attributes={stext_NumericalUnaryExpression_operator}

# stext_PrimitiveValueExpression class attributes and methods

# stext_FeatureCall class attributes and methods
stext_FeatureCall_operationCall: Property = Property(name="operationCall", type=BooleanType)
stext_FeatureCall.attributes={stext_FeatureCall_operationCall}

# stext_EObject class attributes and methods

# stext_ElementReferenceExpression class attributes and methods
stext_ElementReferenceExpression_operationCall: Property = Property(name="operationCall", type=BooleanType)
stext_ElementReferenceExpression.attributes={stext_ElementReferenceExpression_operationCall}

# stext_EventValueReferenceExpression class attributes and methods

# stext_ActiveStateReferenceExpression class attributes and methods

# stext_State class attributes and methods

# Relationships
roots0: BinaryAssociation = BinaryAssociation(
    name="roots0",
    ends={
        Property(name="stext_DefRoot", type=stext_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_Root", type=stext_DefRoot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
def_1: BinaryAssociation = BinaryAssociation(
    name="def_1",
    ends={
        Property(name="stext_StatechartSpecification", type=stext_StatechartRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_StatechartRoot", type=stext_StatechartSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
def_2: BinaryAssociation = BinaryAssociation(
    name="def_2",
    ends={
        Property(name="stext_StateSpecification", type=stext_StateRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_StateRoot", type=stext_StateSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
def_3: BinaryAssociation = BinaryAssociation(
    name="def_3",
    ends={
        Property(name="stext_TransitionSpecification", type=stext_TransitionRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_TransitionRoot", type=stext_TransitionSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entrypoint13: BinaryAssociation = BinaryAssociation(
    name="entrypoint13",
    ends={
        Property(name="stext_Entrypoint", type=stext_EntryPointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_EntryPointSpec", type=stext_Entrypoint, multiplicity=Multiplicity(0, 1))
    }
)
scope4: BinaryAssociation = BinaryAssociation(
    name="scope4",
    ends={
        Property(name="stext_Scope", type=stext_StateSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_StateSpecification5", type=stext_Scope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reaction6: BinaryAssociation = BinaryAssociation(
    name="reaction6",
    ends={
        Property(name="stext_TransitionReaction", type=stext_TransitionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_TransitionSpecification7", type=stext_TransitionReaction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initialValue8: BinaryAssociation = BinaryAssociation(
    name="initialValue8",
    ends={
        Property(name="stext_Expression", type=stext_VariableDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_VariableDefinition", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties9: BinaryAssociation = BinaryAssociation(
    name="properties9",
    ends={
        Property(name="stext_ReactionProperties", type=stext_TransitionReaction, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_TransitionReaction10", type=stext_ReactionProperties, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties11: BinaryAssociation = BinaryAssociation(
    name="properties11",
    ends={
        Property(name="stext_ReactionProperty", type=stext_ReactionProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_ReactionProperties12", type=stext_ReactionProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exitpoint14: BinaryAssociation = BinaryAssociation(
    name="exitpoint14",
    ends={
        Property(name="stext_Exitpoint", type=stext_ExitPointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_ExitPointSpec", type=stext_Exitpoint, multiplicity=Multiplicity(0, 1))
    }
)
event15: BinaryAssociation = BinaryAssociation(
    name="event15",
    ends={
        Property(name="stext_Expression16", type=stext_RegularEventSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_RegularEventSpec", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
triggers17: BinaryAssociation = BinaryAssociation(
    name="triggers17",
    ends={
        Property(name="stext_EventSpec", type=stext_ReactionTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_ReactionTrigger", type=stext_EventSpec, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guardExpression18: BinaryAssociation = BinaryAssociation(
    name="guardExpression18",
    ends={
        Property(name="stext_Expression20", type=stext_ReactionTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_ReactionTrigger19", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actions21: BinaryAssociation = BinaryAssociation(
    name="actions21",
    ends={
        Property(name="stext_Expression22", type=stext_ReactionEffect, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_ReactionEffect", type=stext_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event23: BinaryAssociation = BinaryAssociation(
    name="event23",
    ends={
        Property(name="stext_Expression24", type=stext_EventRaisingExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_EventRaisingExpression", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value25: BinaryAssociation = BinaryAssociation(
    name="value25",
    ends={
        Property(name="stext_Expression27", type=stext_EventRaisingExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_EventRaisingExpression26", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
varRef28: BinaryAssociation = BinaryAssociation(
    name="varRef28",
    ends={
        Property(name="stext_Expression29", type=stext_AssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_AssignmentExpression", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression30: BinaryAssociation = BinaryAssociation(
    name="expression30",
    ends={
        Property(name="stext_Expression32", type=stext_AssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_AssignmentExpression31", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition33: BinaryAssociation = BinaryAssociation(
    name="condition33",
    ends={
        Property(name="stext_Expression34", type=stext_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_ConditionalExpression", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trueCase35: BinaryAssociation = BinaryAssociation(
    name="trueCase35",
    ends={
        Property(name="stext_Expression37", type=stext_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_ConditionalExpression36", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
falseCase38: BinaryAssociation = BinaryAssociation(
    name="falseCase38",
    ends={
        Property(name="stext_Expression40", type=stext_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_ConditionalExpression39", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand41: BinaryAssociation = BinaryAssociation(
    name="leftOperand41",
    ends={
        Property(name="stext_Expression42", type=stext_LogicalOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_LogicalOrExpression", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand43: BinaryAssociation = BinaryAssociation(
    name="rightOperand43",
    ends={
        Property(name="stext_Expression45", type=stext_LogicalOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_LogicalOrExpression44", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand46: BinaryAssociation = BinaryAssociation(
    name="leftOperand46",
    ends={
        Property(name="stext_Expression47", type=stext_LogicalAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_LogicalAndExpression", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand48: BinaryAssociation = BinaryAssociation(
    name="rightOperand48",
    ends={
        Property(name="stext_Expression50", type=stext_LogicalAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_LogicalAndExpression49", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand51: BinaryAssociation = BinaryAssociation(
    name="operand51",
    ends={
        Property(name="stext_Expression52", type=stext_LogicalNotExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_LogicalNotExpression", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand53: BinaryAssociation = BinaryAssociation(
    name="leftOperand53",
    ends={
        Property(name="stext_Expression54", type=stext_BitwiseXorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_BitwiseXorExpression", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand55: BinaryAssociation = BinaryAssociation(
    name="rightOperand55",
    ends={
        Property(name="stext_Expression57", type=stext_BitwiseXorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_BitwiseXorExpression56", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand58: BinaryAssociation = BinaryAssociation(
    name="leftOperand58",
    ends={
        Property(name="stext_Expression59", type=stext_BitwiseOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_BitwiseOrExpression", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand60: BinaryAssociation = BinaryAssociation(
    name="rightOperand60",
    ends={
        Property(name="stext_Expression62", type=stext_BitwiseOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_BitwiseOrExpression61", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand63: BinaryAssociation = BinaryAssociation(
    name="leftOperand63",
    ends={
        Property(name="stext_Expression64", type=stext_BitwiseAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_BitwiseAndExpression", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand65: BinaryAssociation = BinaryAssociation(
    name="rightOperand65",
    ends={
        Property(name="stext_Expression67", type=stext_BitwiseAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_BitwiseAndExpression66", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand68: BinaryAssociation = BinaryAssociation(
    name="leftOperand68",
    ends={
        Property(name="stext_Expression69", type=stext_LogicalRelationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_LogicalRelationExpression", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand70: BinaryAssociation = BinaryAssociation(
    name="rightOperand70",
    ends={
        Property(name="stext_Expression72", type=stext_LogicalRelationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_LogicalRelationExpression71", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand73: BinaryAssociation = BinaryAssociation(
    name="leftOperand73",
    ends={
        Property(name="stext_Expression74", type=stext_ShiftExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_ShiftExpression", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand75: BinaryAssociation = BinaryAssociation(
    name="rightOperand75",
    ends={
        Property(name="stext_Expression77", type=stext_ShiftExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_ShiftExpression76", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand78: BinaryAssociation = BinaryAssociation(
    name="leftOperand78",
    ends={
        Property(name="stext_Expression79", type=stext_NumericalAddSubtractExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_NumericalAddSubtractExpression", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand80: BinaryAssociation = BinaryAssociation(
    name="rightOperand80",
    ends={
        Property(name="stext_Expression82", type=stext_NumericalAddSubtractExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_NumericalAddSubtractExpression81", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand83: BinaryAssociation = BinaryAssociation(
    name="leftOperand83",
    ends={
        Property(name="stext_Expression84", type=stext_NumericalMultiplyDivideExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_NumericalMultiplyDivideExpression", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand85: BinaryAssociation = BinaryAssociation(
    name="rightOperand85",
    ends={
        Property(name="stext_Expression87", type=stext_NumericalMultiplyDivideExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_NumericalMultiplyDivideExpression86", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand88: BinaryAssociation = BinaryAssociation(
    name="operand88",
    ends={
        Property(name="stext_Expression89", type=stext_NumericalUnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_NumericalUnaryExpression", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value90: BinaryAssociation = BinaryAssociation(
    name="value90",
    ends={
        Property(name="stext_Literal", type=stext_PrimitiveValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_PrimitiveValueExpression", type=stext_Literal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owner91: BinaryAssociation = BinaryAssociation(
    name="owner91",
    ends={
        Property(name="stext_Expression92", type=stext_FeatureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_FeatureCall", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
feature93: BinaryAssociation = BinaryAssociation(
    name="feature93",
    ends={
        Property(name="stext_EObject", type=stext_FeatureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_FeatureCall94", type=stext_EObject, multiplicity=Multiplicity(0, 1))
    }
)
args95: BinaryAssociation = BinaryAssociation(
    name="args95",
    ends={
        Property(name="stext_Expression97", type=stext_FeatureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_FeatureCall96", type=stext_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reference98: BinaryAssociation = BinaryAssociation(
    name="reference98",
    ends={
        Property(name="stext_EObject99", type=stext_ElementReferenceExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_ElementReferenceExpression", type=stext_EObject, multiplicity=Multiplicity(0, 1))
    }
)
args100: BinaryAssociation = BinaryAssociation(
    name="args100",
    ends={
        Property(name="stext_Expression102", type=stext_ElementReferenceExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_ElementReferenceExpression101", type=stext_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value103: BinaryAssociation = BinaryAssociation(
    name="value103",
    ends={
        Property(name="stext_Expression104", type=stext_EventValueReferenceExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_EventValueReferenceExpression", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value105: BinaryAssociation = BinaryAssociation(
    name="value105",
    ends={
        Property(name="stext_State", type=stext_ActiveStateReferenceExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_ActiveStateReferenceExpression", type=stext_State, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_stext_StatechartSpecification_ScopedElement = Generalization(general=ScopedElement, specific=stext_StatechartSpecification)
gen_stext_StatechartRoot_DefRoot = Generalization(general=DefRoot, specific=stext_StatechartRoot)
gen_stext_StateRoot_DefRoot = Generalization(general=DefRoot, specific=stext_StateRoot)
gen_stext_TransitionRoot_DefRoot = Generalization(general=DefRoot, specific=stext_TransitionRoot)
gen_stext_StatechartScope_Scope = Generalization(general=Scope, specific=stext_StatechartScope)
gen_stext_InterfaceScope_StatechartScope = Generalization(general=StatechartScope, specific=stext_InterfaceScope)
gen_stext_InterfaceScope_NamedElement = Generalization(general=NamedElement, specific=stext_InterfaceScope)
gen_stext_InternalScope_StatechartScope = Generalization(general=StatechartScope, specific=stext_InternalScope)
gen_stext_EventDefinition_Event = Generalization(general=Event, specific=stext_EventDefinition)
gen_stext_EventDefinition_Event = Generalization(general=Event, specific=stext_EventDefinition)
gen_stext_VariableDefinition_Variable = Generalization(general=Variable, specific=stext_VariableDefinition)
gen_stext_VariableDefinition_Property = Generalization(general=Property_, specific=stext_VariableDefinition)
gen_stext_OperationDefinition_Declaration = Generalization(general=Declaration, specific=stext_OperationDefinition)
gen_stext_OperationDefinition_Operation = Generalization(general=Operation, specific=stext_OperationDefinition)
gen_stext_LocalReaction_Declaration = Generalization(general=Declaration, specific=stext_LocalReaction)
gen_stext_LocalReaction_Reaction = Generalization(general=Reaction, specific=stext_LocalReaction)
gen_stext_TransitionReaction_Reaction = Generalization(general=Reaction, specific=stext_TransitionReaction)
gen_stext_EntryPointSpec_ReactionProperty = Generalization(general=ReactionProperty, specific=stext_EntryPointSpec)
gen_stext_ExitPointSpec_ReactionProperty = Generalization(general=ReactionProperty, specific=stext_ExitPointSpec)
gen_stext_RegularEventSpec_EventSpec = Generalization(general=EventSpec, specific=stext_RegularEventSpec)
gen_stext_TimeEventSpec_EventSpec = Generalization(general=EventSpec, specific=stext_TimeEventSpec)
gen_stext_BuiltinEventSpec_EventSpec = Generalization(general=EventSpec, specific=stext_BuiltinEventSpec)
gen_stext_EntryEvent_BuiltinEventSpec = Generalization(general=BuiltinEventSpec, specific=stext_EntryEvent)
gen_stext_ExitEvent_BuiltinEventSpec = Generalization(general=BuiltinEventSpec, specific=stext_ExitEvent)
gen_stext_OnCycleEvent_BuiltinEventSpec = Generalization(general=BuiltinEventSpec, specific=stext_OnCycleEvent)
gen_stext_AlwaysEvent_BuiltinEventSpec = Generalization(general=BuiltinEventSpec, specific=stext_AlwaysEvent)
gen_stext_DefaultEvent_BuiltinEventSpec = Generalization(general=BuiltinEventSpec, specific=stext_DefaultEvent)
gen_stext_Expression_Statement = Generalization(general=Statement, specific=stext_Expression)
gen_stext_BoolLiteral_Literal = Generalization(general=Literal, specific=stext_BoolLiteral)
gen_stext_IntLiteral_Literal = Generalization(general=Literal, specific=stext_IntLiteral)
gen_stext_RealLiteral_Literal = Generalization(general=Literal, specific=stext_RealLiteral)
gen_stext_HexLiteral_Literal = Generalization(general=Literal, specific=stext_HexLiteral)
gen_stext_StringLiteral_Literal = Generalization(general=Literal, specific=stext_StringLiteral)
gen_stext_SimpleScope_Scope = Generalization(general=Scope, specific=stext_SimpleScope)
gen_stext_Entrypoint_Declaration = Generalization(general=Declaration, specific=stext_Entrypoint)
gen_stext_Exitpoint_Declaration = Generalization(general=Declaration, specific=stext_Exitpoint)
gen_stext_ReactionTrigger_Trigger = Generalization(general=Trigger, specific=stext_ReactionTrigger)
gen_stext_ReactionEffect_Effect = Generalization(general=Effect, specific=stext_ReactionEffect)
gen_stext_EventRaisingExpression_Expression = Generalization(general=Expression, specific=stext_EventRaisingExpression)
gen_stext_AssignmentExpression_Expression = Generalization(general=Expression, specific=stext_AssignmentExpression)
gen_stext_ConditionalExpression_Expression = Generalization(general=Expression, specific=stext_ConditionalExpression)
gen_stext_LogicalOrExpression_Expression = Generalization(general=Expression, specific=stext_LogicalOrExpression)
gen_stext_LogicalAndExpression_Expression = Generalization(general=Expression, specific=stext_LogicalAndExpression)
gen_stext_LogicalNotExpression_Expression = Generalization(general=Expression, specific=stext_LogicalNotExpression)
gen_stext_BitwiseXorExpression_Expression = Generalization(general=Expression, specific=stext_BitwiseXorExpression)
gen_stext_BitwiseOrExpression_Expression = Generalization(general=Expression, specific=stext_BitwiseOrExpression)
gen_stext_BitwiseAndExpression_Expression = Generalization(general=Expression, specific=stext_BitwiseAndExpression)
gen_stext_LogicalRelationExpression_Expression = Generalization(general=Expression, specific=stext_LogicalRelationExpression)
gen_stext_ShiftExpression_Expression = Generalization(general=Expression, specific=stext_ShiftExpression)
gen_stext_NumericalAddSubtractExpression_Expression = Generalization(general=Expression, specific=stext_NumericalAddSubtractExpression)
gen_stext_NumericalMultiplyDivideExpression_Expression = Generalization(general=Expression, specific=stext_NumericalMultiplyDivideExpression)
gen_stext_NumericalUnaryExpression_Expression = Generalization(general=Expression, specific=stext_NumericalUnaryExpression)
gen_stext_PrimitiveValueExpression_Expression = Generalization(general=Expression, specific=stext_PrimitiveValueExpression)
gen_stext_FeatureCall_Expression = Generalization(general=Expression, specific=stext_FeatureCall)
gen_stext_ElementReferenceExpression_Expression = Generalization(general=Expression, specific=stext_ElementReferenceExpression)
gen_stext_EventValueReferenceExpression_Expression = Generalization(general=Expression, specific=stext_EventValueReferenceExpression)
gen_stext_ActiveStateReferenceExpression_Expression = Generalization(general=Expression, specific=stext_ActiveStateReferenceExpression)

# Domain Model
domain_model = DomainModel(
    name="stext",
    types={ScopedElement, stext_Root, stext_DefRoot, stext_StatechartRoot, DefRoot, stext_StatechartSpecification, stext_StateRoot, stext_StateSpecification, stext_TransitionRoot, stext_TransitionSpecification, stext_Entrypoint, stext_Scope, stext_TransitionReaction, stext_StatechartScope, Scope, stext_InterfaceScope, StatechartScope, NamedElement, stext_InternalScope, stext_EventDefinition, Event, stext_VariableDefinition, Variable, Property_, stext_Expression, stext_OperationDefinition, Declaration, Operation, stext_LocalReaction, Reaction, stext_ReactionProperties, stext_ReactionProperty, stext_EntryPointSpec, ReactionProperty, stext_ExitPointSpec, stext_Exitpoint, stext_EventSpec, stext_RegularEventSpec, EventSpec, stext_TimeEventSpec, stext_BuiltinEventSpec, stext_EntryEvent, BuiltinEventSpec, stext_ExitEvent, stext_OnCycleEvent, stext_AlwaysEvent, stext_DefaultEvent, Statement, stext_Literal, stext_BoolLiteral, Literal, stext_IntLiteral, stext_RealLiteral, stext_HexLiteral, stext_StringLiteral, stext_SimpleScope, stext_ReactionTrigger, Trigger, stext_LogicalNotExpression, stext_ReactionEffect, Effect, stext_EventRaisingExpression, Expression, stext_AssignmentExpression, stext_ConditionalExpression, stext_LogicalOrExpression, stext_LogicalAndExpression, stext_NumericalAddSubtractExpression, stext_BitwiseXorExpression, stext_BitwiseOrExpression, stext_BitwiseAndExpression, stext_LogicalRelationExpression, stext_ShiftExpression, stext_NumericalMultiplyDivideExpression, stext_NumericalUnaryExpression, stext_PrimitiveValueExpression, stext_FeatureCall, stext_EObject, stext_ElementReferenceExpression, stext_EventValueReferenceExpression, stext_ActiveStateReferenceExpression, stext_State, Direction, TimeEventType, AssignmentOperator, ShiftOperator, AdditiveOperator, MultiplicativeOperator, UnaryOperator, RelationalOperator, TimeUnit},
    associations={roots0, def_1, def_2, def_3, entrypoint13, scope4, reaction6, initialValue8, properties9, properties11, exitpoint14, event15, triggers17, guardExpression18, actions21, event23, value25, varRef28, expression30, condition33, trueCase35, falseCase38, leftOperand41, rightOperand43, leftOperand46, rightOperand48, operand51, leftOperand53, rightOperand55, leftOperand58, rightOperand60, leftOperand63, rightOperand65, leftOperand68, rightOperand70, leftOperand73, rightOperand75, leftOperand78, rightOperand80, leftOperand83, rightOperand85, operand88, value90, owner91, feature93, args95, reference98, args100, value103, value105},
    generalizations={gen_stext_StatechartSpecification_ScopedElement, gen_stext_StatechartRoot_DefRoot, gen_stext_StateRoot_DefRoot, gen_stext_TransitionRoot_DefRoot, gen_stext_StatechartScope_Scope, gen_stext_InterfaceScope_StatechartScope, gen_stext_InterfaceScope_NamedElement, gen_stext_InternalScope_StatechartScope, gen_stext_EventDefinition_Event, gen_stext_EventDefinition_Event, gen_stext_VariableDefinition_Variable, gen_stext_VariableDefinition_Property, gen_stext_OperationDefinition_Declaration, gen_stext_OperationDefinition_Operation, gen_stext_LocalReaction_Declaration, gen_stext_LocalReaction_Reaction, gen_stext_TransitionReaction_Reaction, gen_stext_EntryPointSpec_ReactionProperty, gen_stext_ExitPointSpec_ReactionProperty, gen_stext_RegularEventSpec_EventSpec, gen_stext_TimeEventSpec_EventSpec, gen_stext_BuiltinEventSpec_EventSpec, gen_stext_EntryEvent_BuiltinEventSpec, gen_stext_ExitEvent_BuiltinEventSpec, gen_stext_OnCycleEvent_BuiltinEventSpec, gen_stext_AlwaysEvent_BuiltinEventSpec, gen_stext_DefaultEvent_BuiltinEventSpec, gen_stext_Expression_Statement, gen_stext_BoolLiteral_Literal, gen_stext_IntLiteral_Literal, gen_stext_RealLiteral_Literal, gen_stext_HexLiteral_Literal, gen_stext_StringLiteral_Literal, gen_stext_SimpleScope_Scope, gen_stext_Entrypoint_Declaration, gen_stext_Exitpoint_Declaration, gen_stext_ReactionTrigger_Trigger, gen_stext_ReactionEffect_Effect, gen_stext_EventRaisingExpression_Expression, gen_stext_AssignmentExpression_Expression, gen_stext_ConditionalExpression_Expression, gen_stext_LogicalOrExpression_Expression, gen_stext_LogicalAndExpression_Expression, gen_stext_LogicalNotExpression_Expression, gen_stext_BitwiseXorExpression_Expression, gen_stext_BitwiseOrExpression_Expression, gen_stext_BitwiseAndExpression_Expression, gen_stext_LogicalRelationExpression_Expression, gen_stext_ShiftExpression_Expression, gen_stext_NumericalAddSubtractExpression_Expression, gen_stext_NumericalMultiplyDivideExpression_Expression, gen_stext_NumericalUnaryExpression_Expression, gen_stext_PrimitiveValueExpression_Expression, gen_stext_FeatureCall_Expression, gen_stext_ElementReferenceExpression_Expression, gen_stext_EventValueReferenceExpression_Expression, gen_stext_ActiveStateReferenceExpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)