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
            EnumerationLiteral(name="IN"),
			EnumerationLiteral(name="OUT")
    }
)

AssignmentOperator: Enumeration = Enumeration(
    name="AssignmentOperator",
    literals={
            EnumerationLiteral(name="assign"),
			EnumerationLiteral(name="multAssign"),
			EnumerationLiteral(name="andAssign"),
			EnumerationLiteral(name="xorAssign"),
			EnumerationLiteral(name="orAssign"),
			EnumerationLiteral(name="divAssign"),
			EnumerationLiteral(name="modAssign"),
			EnumerationLiteral(name="addAssign"),
			EnumerationLiteral(name="subAssign"),
			EnumerationLiteral(name="leftShiftAssign"),
			EnumerationLiteral(name="rightShiftAssign")
    }
)

TimeEventType: Enumeration = Enumeration(
    name="TimeEventType",
    literals={
            EnumerationLiteral(name="after"),
			EnumerationLiteral(name="every")
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
			EnumerationLiteral(name="nanosecond")
    }
)

Type: Enumeration = Enumeration(
    name="Type",
    literals={
            EnumerationLiteral(name="void"),
			EnumerationLiteral(name="integer"),
			EnumerationLiteral(name="real"),
			EnumerationLiteral(name="boolean"),
			EnumerationLiteral(name="string")
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

# Classes
stext_Root = Class(name="stext_Root")
stext_DefRoot = Class(name="stext_DefRoot")
stext_StatechartDefinition = Class(name="stext_StatechartDefinition")
stext_StateRoot = Class(name="stext_StateRoot")
stext_StateDeclaration = Class(name="stext_StateDeclaration")
stext_TransitionRoot = Class(name="stext_TransitionRoot")
stext_TransitionStatement = Class(name="stext_TransitionStatement")
stext_Scope = Class(name="stext_Scope")
stext_StatechartRoot = Class(name="stext_StatechartRoot")
DefRoot = Class(name="DefRoot")
stext_EventDerivation = Class(name="stext_EventDerivation")
stext_Expression = Class(name="stext_Expression")
stext_LocalReaction = Class(name="stext_LocalReaction")
Declaration = Class(name="Declaration")
Reaction = Class(name="Reaction")
stext_ReactionProperties = Class(name="stext_ReactionProperties")
stext_TransitionReaction = Class(name="stext_TransitionReaction")
TransitionStatement = Class(name="TransitionStatement")
stext_ReactionPriority = Class(name="stext_ReactionPriority")
ReactionProperty = Class(name="ReactionProperty")
stext_EntryPointSpec = Class(name="stext_EntryPointSpec")
stext_Entrypoint = Class(name="stext_Entrypoint")
stext_ExitPointSpec = Class(name="stext_ExitPointSpec")
stext_Exitpoint = Class(name="stext_Exitpoint")
stext_EventSpec = Class(name="stext_EventSpec")
stext_RegularEventSpec = Class(name="stext_RegularEventSpec")
EventSpec = Class(name="EventSpec")
stext_Event = Class(name="stext_Event")
stext_TimeEventSpec = Class(name="stext_TimeEventSpec")
stext_ReactionProperty = Class(name="stext_ReactionProperty")
stext_BuiltinEventSpec = Class(name="stext_BuiltinEventSpec")
stext_EntryEvent = Class(name="stext_EntryEvent")
BuiltinEventSpec = Class(name="BuiltinEventSpec")
stext_ExitEvent = Class(name="stext_ExitEvent")
stext_OnCycleEvent = Class(name="stext_OnCycleEvent")
stext_AlwaysEvent = Class(name="stext_AlwaysEvent")
stext_Assignment = Class(name="stext_Assignment")
Statement = Class(name="Statement")
stext_Variable = Class(name="stext_Variable")
stext_EventRaising = Class(name="stext_EventRaising")
stext_SimpleScope = Class(name="stext_SimpleScope")
Scope = Class(name="Scope")
stext_InterfaceScope = Class(name="stext_InterfaceScope")
stext_InternalScope = Class(name="stext_InternalScope")
stext_EventDefinition = Class(name="stext_EventDefinition")
Event = Class(name="Event")
stext_VariableDefinition = Class(name="stext_VariableDefinition")
Variable = Class(name="Variable")
stext_Clock = Class(name="stext_Clock")
stext_ReactionTrigger = Class(name="stext_ReactionTrigger")
Trigger = Class(name="Trigger")
stext_Operation = Class(name="stext_Operation")
Expression = Class(name="Expression")
stext_LogicalOrExpression = Class(name="stext_LogicalOrExpression")
stext_LogicalAndExpression = Class(name="stext_LogicalAndExpression")
stext_ReactionEffect = Class(name="stext_ReactionEffect")
Effect = Class(name="Effect")
stext_Statement = Class(name="stext_Statement")
stext_ConditionalExpression = Class(name="stext_ConditionalExpression")
stext_LogicalNotExpression = Class(name="stext_LogicalNotExpression")
stext_BitwiseXorExpression = Class(name="stext_BitwiseXorExpression")
stext_BitwiseOrExpression = Class(name="stext_BitwiseOrExpression")
stext_LogicalRelationExpression = Class(name="stext_LogicalRelationExpression")
stext_ShiftExpression = Class(name="stext_ShiftExpression")
stext_BitwiseAndExpression = Class(name="stext_BitwiseAndExpression")
stext_NumericalAddSubtractExpression = Class(name="stext_NumericalAddSubtractExpression")
stext_NumericalMultiplyDivideExpression = Class(name="stext_NumericalMultiplyDivideExpression")
stext_PrimitiveValueExpression = Class(name="stext_PrimitiveValueExpression")
stext_ElementReferenceExpression = Class(name="stext_ElementReferenceExpression")
stext_Declaration = Class(name="stext_Declaration")
stext_OperationCall = Class(name="stext_OperationCall")
stext_NumericalUnaryExpression = Class(name="stext_NumericalUnaryExpression")

# stext_Root class attributes and methods

# stext_DefRoot class attributes and methods

# stext_StatechartDefinition class attributes and methods

# stext_StateRoot class attributes and methods

# stext_StateDeclaration class attributes and methods

# stext_TransitionRoot class attributes and methods

# stext_TransitionStatement class attributes and methods

# stext_Scope class attributes and methods

# stext_StatechartRoot class attributes and methods

# DefRoot class attributes and methods

# stext_EventDerivation class attributes and methods

# stext_Expression class attributes and methods

# stext_LocalReaction class attributes and methods

# Declaration class attributes and methods

# Reaction class attributes and methods

# stext_ReactionProperties class attributes and methods

# stext_TransitionReaction class attributes and methods

# TransitionStatement class attributes and methods

# stext_ReactionPriority class attributes and methods
stext_ReactionPriority_priority: Property = Property(name="priority", type=IntegerType)
stext_ReactionPriority.attributes={stext_ReactionPriority_priority}

# ReactionProperty class attributes and methods

# stext_EntryPointSpec class attributes and methods

# stext_Entrypoint class attributes and methods

# stext_ExitPointSpec class attributes and methods

# stext_Exitpoint class attributes and methods

# stext_EventSpec class attributes and methods

# stext_RegularEventSpec class attributes and methods

# EventSpec class attributes and methods

# stext_Event class attributes and methods

# stext_TimeEventSpec class attributes and methods
stext_TimeEventSpec_type: Property = Property(name="type", type=StringType)
stext_TimeEventSpec_value: Property = Property(name="value", type=IntegerType)
stext_TimeEventSpec_unit: Property = Property(name="unit", type=StringType)
stext_TimeEventSpec.attributes={stext_TimeEventSpec_value, stext_TimeEventSpec_type, stext_TimeEventSpec_unit}

# stext_ReactionProperty class attributes and methods

# stext_BuiltinEventSpec class attributes and methods

# stext_EntryEvent class attributes and methods

# BuiltinEventSpec class attributes and methods

# stext_ExitEvent class attributes and methods

# stext_OnCycleEvent class attributes and methods

# stext_AlwaysEvent class attributes and methods

# stext_Assignment class attributes and methods
stext_Assignment_operator: Property = Property(name="operator", type=StringType)
stext_Assignment.attributes={stext_Assignment_operator}

# Statement class attributes and methods

# stext_Variable class attributes and methods

# stext_EventRaising class attributes and methods

# stext_SimpleScope class attributes and methods

# Scope class attributes and methods

# stext_InterfaceScope class attributes and methods
stext_InterfaceScope_name: Property = Property(name="name", type=StringType)
stext_InterfaceScope.attributes={stext_InterfaceScope_name}

# stext_InternalScope class attributes and methods

# stext_EventDefinition class attributes and methods
stext_EventDefinition_direction: Property = Property(name="direction", type=StringType)
stext_EventDefinition_type: Property = Property(name="type", type=StringType)
stext_EventDefinition.attributes={stext_EventDefinition_direction, stext_EventDefinition_type}

# Event class attributes and methods

# stext_VariableDefinition class attributes and methods
stext_VariableDefinition_readonly: Property = Property(name="readonly", type=BooleanType)
stext_VariableDefinition_external: Property = Property(name="external", type=BooleanType)
stext_VariableDefinition_type: Property = Property(name="type", type=StringType)
stext_VariableDefinition_initialValue: Property = Property(name="initialValue", type=StringType)
stext_VariableDefinition.attributes={stext_VariableDefinition_external, stext_VariableDefinition_initialValue, stext_VariableDefinition_readonly, stext_VariableDefinition_type}

# Variable class attributes and methods

# stext_Clock class attributes and methods

# stext_ReactionTrigger class attributes and methods

# Trigger class attributes and methods

# stext_Operation class attributes and methods
stext_Operation_paramTypes: Property = Property(name="paramTypes", type=StringType)
stext_Operation_type: Property = Property(name="type", type=StringType)
stext_Operation.attributes={stext_Operation_paramTypes, stext_Operation_type}

# Expression class attributes and methods

# stext_LogicalOrExpression class attributes and methods

# stext_LogicalAndExpression class attributes and methods

# stext_ReactionEffect class attributes and methods

# Effect class attributes and methods

# stext_Statement class attributes and methods

# stext_ConditionalExpression class attributes and methods

# stext_LogicalNotExpression class attributes and methods

# stext_BitwiseXorExpression class attributes and methods

# stext_BitwiseOrExpression class attributes and methods

# stext_LogicalRelationExpression class attributes and methods
stext_LogicalRelationExpression_operator: Property = Property(name="operator", type=StringType)
stext_LogicalRelationExpression.attributes={stext_LogicalRelationExpression_operator}

# stext_ShiftExpression class attributes and methods
stext_ShiftExpression_operator: Property = Property(name="operator", type=StringType)
stext_ShiftExpression.attributes={stext_ShiftExpression_operator}

# stext_BitwiseAndExpression class attributes and methods

# stext_NumericalAddSubtractExpression class attributes and methods
stext_NumericalAddSubtractExpression_operator: Property = Property(name="operator", type=StringType)
stext_NumericalAddSubtractExpression.attributes={stext_NumericalAddSubtractExpression_operator}

# stext_NumericalMultiplyDivideExpression class attributes and methods
stext_NumericalMultiplyDivideExpression_operator: Property = Property(name="operator", type=StringType)
stext_NumericalMultiplyDivideExpression.attributes={stext_NumericalMultiplyDivideExpression_operator}

# stext_PrimitiveValueExpression class attributes and methods
stext_PrimitiveValueExpression_value: Property = Property(name="value", type=StringType)
stext_PrimitiveValueExpression.attributes={stext_PrimitiveValueExpression_value}

# stext_ElementReferenceExpression class attributes and methods

# stext_Declaration class attributes and methods

# stext_OperationCall class attributes and methods

# stext_NumericalUnaryExpression class attributes and methods
stext_NumericalUnaryExpression_operator: Property = Property(name="operator", type=StringType)
stext_NumericalUnaryExpression.attributes={stext_NumericalUnaryExpression_operator}

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
        Property(name="stext_StatechartDefinition", type=stext_StatechartRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_StatechartRoot", type=stext_StatechartDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
def_2: BinaryAssociation = BinaryAssociation(
    name="def_2",
    ends={
        Property(name="stext_StateDeclaration", type=stext_StateRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_StateRoot", type=stext_StateDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
def_3: BinaryAssociation = BinaryAssociation(
    name="def_3",
    ends={
        Property(name="stext_TransitionStatement", type=stext_TransitionRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_TransitionRoot", type=stext_TransitionStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definitionScopes4: BinaryAssociation = BinaryAssociation(
    name="definitionScopes4",
    ends={
        Property(name="stext_Scope", type=stext_StatechartDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_StatechartDefinition5", type=stext_Scope, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition9: BinaryAssociation = BinaryAssociation(
    name="condition9",
    ends={
        Property(name="stext_Expression", type=stext_EventDerivation, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_EventDerivation", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value10: BinaryAssociation = BinaryAssociation(
    name="value10",
    ends={
        Property(name="stext_Expression12", type=stext_EventDerivation, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_EventDerivation11", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties13: BinaryAssociation = BinaryAssociation(
    name="properties13",
    ends={
        Property(name="stext_ReactionProperties", type=stext_LocalReaction, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_LocalReaction", type=stext_ReactionProperties, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties14: BinaryAssociation = BinaryAssociation(
    name="properties14",
    ends={
        Property(name="stext_ReactionProperties15", type=stext_TransitionReaction, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_TransitionReaction", type=stext_ReactionProperties, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scope6: BinaryAssociation = BinaryAssociation(
    name="scope6",
    ends={
        Property(name="stext_Scope8", type=stext_StateDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_StateDeclaration7", type=stext_Scope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entrypoint18: BinaryAssociation = BinaryAssociation(
    name="entrypoint18",
    ends={
        Property(name="stext_Entrypoint", type=stext_EntryPointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_EntryPointSpec", type=stext_Entrypoint, multiplicity=Multiplicity(0, 1))
    }
)
exitpoint19: BinaryAssociation = BinaryAssociation(
    name="exitpoint19",
    ends={
        Property(name="stext_Exitpoint", type=stext_ExitPointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_ExitPointSpec", type=stext_Exitpoint, multiplicity=Multiplicity(0, 1))
    }
)
event20: BinaryAssociation = BinaryAssociation(
    name="event20",
    ends={
        Property(name="stext_Event", type=stext_RegularEventSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_RegularEventSpec", type=stext_Event, multiplicity=Multiplicity(0, 1))
    }
)
properties16: BinaryAssociation = BinaryAssociation(
    name="properties16",
    ends={
        Property(name="stext_ReactionProperty", type=stext_ReactionProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_ReactionProperties17", type=stext_ReactionProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
varRef21: BinaryAssociation = BinaryAssociation(
    name="varRef21",
    ends={
        Property(name="stext_Variable", type=stext_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_Assignment", type=stext_Variable, multiplicity=Multiplicity(0, 1))
    }
)
expression22: BinaryAssociation = BinaryAssociation(
    name="expression22",
    ends={
        Property(name="stext_Expression24", type=stext_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_Assignment23", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
event25: BinaryAssociation = BinaryAssociation(
    name="event25",
    ends={
        Property(name="stext_Event26", type=stext_EventRaising, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_EventRaising", type=stext_Event, multiplicity=Multiplicity(0, 1))
    }
)
value27: BinaryAssociation = BinaryAssociation(
    name="value27",
    ends={
        Property(name="stext_Expression29", type=stext_EventRaising, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_EventRaising28", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
derivation30: BinaryAssociation = BinaryAssociation(
    name="derivation30",
    ends={
        Property(name="stext_EventDerivation31", type=stext_EventDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_EventDefinition", type=stext_EventDerivation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
triggers32: BinaryAssociation = BinaryAssociation(
    name="triggers32",
    ends={
        Property(name="stext_EventSpec", type=stext_ReactionTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_ReactionTrigger", type=stext_EventSpec, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guardExpression33: BinaryAssociation = BinaryAssociation(
    name="guardExpression33",
    ends={
        Property(name="stext_Expression35", type=stext_ReactionTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_ReactionTrigger34", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition37: BinaryAssociation = BinaryAssociation(
    name="condition37",
    ends={
        Property(name="stext_Expression38", type=stext_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_ConditionalExpression", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trueCase39: BinaryAssociation = BinaryAssociation(
    name="trueCase39",
    ends={
        Property(name="stext_Expression41", type=stext_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_ConditionalExpression40", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
falseCase42: BinaryAssociation = BinaryAssociation(
    name="falseCase42",
    ends={
        Property(name="stext_Expression44", type=stext_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_ConditionalExpression43", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand45: BinaryAssociation = BinaryAssociation(
    name="leftOperand45",
    ends={
        Property(name="stext_Expression46", type=stext_LogicalOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_LogicalOrExpression", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand47: BinaryAssociation = BinaryAssociation(
    name="rightOperand47",
    ends={
        Property(name="stext_Expression49", type=stext_LogicalOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_LogicalOrExpression48", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actions36: BinaryAssociation = BinaryAssociation(
    name="actions36",
    ends={
        Property(name="stext_Statement", type=stext_ReactionEffect, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_ReactionEffect", type=stext_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operand55: BinaryAssociation = BinaryAssociation(
    name="operand55",
    ends={
        Property(name="stext_Expression56", type=stext_LogicalNotExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_LogicalNotExpression", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand57: BinaryAssociation = BinaryAssociation(
    name="leftOperand57",
    ends={
        Property(name="stext_Expression58", type=stext_BitwiseXorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_BitwiseXorExpression", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand59: BinaryAssociation = BinaryAssociation(
    name="rightOperand59",
    ends={
        Property(name="stext_Expression61", type=stext_BitwiseXorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_BitwiseXorExpression60", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand62: BinaryAssociation = BinaryAssociation(
    name="leftOperand62",
    ends={
        Property(name="stext_Expression63", type=stext_BitwiseOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_BitwiseOrExpression", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand64: BinaryAssociation = BinaryAssociation(
    name="rightOperand64",
    ends={
        Property(name="stext_Expression66", type=stext_BitwiseOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_BitwiseOrExpression65", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand50: BinaryAssociation = BinaryAssociation(
    name="leftOperand50",
    ends={
        Property(name="stext_Expression51", type=stext_LogicalAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_LogicalAndExpression", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand52: BinaryAssociation = BinaryAssociation(
    name="rightOperand52",
    ends={
        Property(name="stext_Expression54", type=stext_LogicalAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_LogicalAndExpression53", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand69: BinaryAssociation = BinaryAssociation(
    name="rightOperand69",
    ends={
        Property(name="stext_Expression71", type=stext_BitwiseAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_BitwiseAndExpression70", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand72: BinaryAssociation = BinaryAssociation(
    name="leftOperand72",
    ends={
        Property(name="stext_Expression73", type=stext_LogicalRelationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_LogicalRelationExpression", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand74: BinaryAssociation = BinaryAssociation(
    name="rightOperand74",
    ends={
        Property(name="stext_Expression76", type=stext_LogicalRelationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_LogicalRelationExpression75", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand77: BinaryAssociation = BinaryAssociation(
    name="leftOperand77",
    ends={
        Property(name="stext_Expression78", type=stext_ShiftExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_ShiftExpression", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand67: BinaryAssociation = BinaryAssociation(
    name="leftOperand67",
    ends={
        Property(name="stext_Expression68", type=stext_BitwiseAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_BitwiseAndExpression", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand82: BinaryAssociation = BinaryAssociation(
    name="leftOperand82",
    ends={
        Property(name="stext_Expression83", type=stext_NumericalAddSubtractExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_NumericalAddSubtractExpression", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand84: BinaryAssociation = BinaryAssociation(
    name="rightOperand84",
    ends={
        Property(name="stext_Expression86", type=stext_NumericalAddSubtractExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_NumericalAddSubtractExpression85", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand87: BinaryAssociation = BinaryAssociation(
    name="leftOperand87",
    ends={
        Property(name="stext_Expression88", type=stext_NumericalMultiplyDivideExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_NumericalMultiplyDivideExpression", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand89: BinaryAssociation = BinaryAssociation(
    name="rightOperand89",
    ends={
        Property(name="stext_Expression91", type=stext_NumericalMultiplyDivideExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_NumericalMultiplyDivideExpression90", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand79: BinaryAssociation = BinaryAssociation(
    name="rightOperand79",
    ends={
        Property(name="stext_Expression81", type=stext_ShiftExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_ShiftExpression80", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand92: BinaryAssociation = BinaryAssociation(
    name="operand92",
    ends={
        Property(name="stext_Expression93", type=stext_NumericalUnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_NumericalUnaryExpression", type=stext_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value94: BinaryAssociation = BinaryAssociation(
    name="value94",
    ends={
        Property(name="stext_Declaration", type=stext_ElementReferenceExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_ElementReferenceExpression", type=stext_Declaration, multiplicity=Multiplicity(0, 1))
    }
)
operation95: BinaryAssociation = BinaryAssociation(
    name="operation95",
    ends={
        Property(name="stext_Operation", type=stext_OperationCall, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_OperationCall", type=stext_Operation, multiplicity=Multiplicity(0, 1))
    }
)
args96: BinaryAssociation = BinaryAssociation(
    name="args96",
    ends={
        Property(name="stext_Expression98", type=stext_OperationCall, multiplicity=Multiplicity(1, 1)),
        Property(name="stext_OperationCall97", type=stext_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_stext_StateRoot_DefRoot = Generalization(general=DefRoot, specific=stext_StateRoot)
gen_stext_TransitionRoot_DefRoot = Generalization(general=DefRoot, specific=stext_TransitionRoot)
gen_stext_StatechartRoot_DefRoot = Generalization(general=DefRoot, specific=stext_StatechartRoot)
gen_stext_LocalReaction_Declaration = Generalization(general=Declaration, specific=stext_LocalReaction)
gen_stext_LocalReaction_Reaction = Generalization(general=Reaction, specific=stext_LocalReaction)
gen_stext_TransitionReaction_TransitionStatement = Generalization(general=TransitionStatement, specific=stext_TransitionReaction)
gen_stext_TransitionReaction_Reaction = Generalization(general=Reaction, specific=stext_TransitionReaction)
gen_stext_ReactionPriority_ReactionProperty = Generalization(general=ReactionProperty, specific=stext_ReactionPriority)
gen_stext_EntryPointSpec_ReactionProperty = Generalization(general=ReactionProperty, specific=stext_EntryPointSpec)
gen_stext_ExitPointSpec_ReactionProperty = Generalization(general=ReactionProperty, specific=stext_ExitPointSpec)
gen_stext_RegularEventSpec_EventSpec = Generalization(general=EventSpec, specific=stext_RegularEventSpec)
gen_stext_TimeEventSpec_EventSpec = Generalization(general=EventSpec, specific=stext_TimeEventSpec)
gen_stext_BuiltinEventSpec_EventSpec = Generalization(general=EventSpec, specific=stext_BuiltinEventSpec)
gen_stext_EntryEvent_BuiltinEventSpec = Generalization(general=BuiltinEventSpec, specific=stext_EntryEvent)
gen_stext_ExitEvent_BuiltinEventSpec = Generalization(general=BuiltinEventSpec, specific=stext_ExitEvent)
gen_stext_OnCycleEvent_BuiltinEventSpec = Generalization(general=BuiltinEventSpec, specific=stext_OnCycleEvent)
gen_stext_AlwaysEvent_BuiltinEventSpec = Generalization(general=BuiltinEventSpec, specific=stext_AlwaysEvent)
gen_stext_Assignment_Statement = Generalization(general=Statement, specific=stext_Assignment)
gen_stext_EventRaising_Statement = Generalization(general=Statement, specific=stext_EventRaising)
gen_stext_Expression_Statement = Generalization(general=Statement, specific=stext_Expression)
gen_stext_SimpleScope_Scope = Generalization(general=Scope, specific=stext_SimpleScope)
gen_stext_InterfaceScope_Scope = Generalization(general=Scope, specific=stext_InterfaceScope)
gen_stext_InternalScope_Scope = Generalization(general=Scope, specific=stext_InternalScope)
gen_stext_EventDefinition_Event = Generalization(general=Event, specific=stext_EventDefinition)
gen_stext_VariableDefinition_Variable = Generalization(general=Variable, specific=stext_VariableDefinition)
gen_stext_Entrypoint_Declaration = Generalization(general=Declaration, specific=stext_Entrypoint)
gen_stext_Exitpoint_Declaration = Generalization(general=Declaration, specific=stext_Exitpoint)
gen_stext_ReactionTrigger_Trigger = Generalization(general=Trigger, specific=stext_ReactionTrigger)
gen_stext_Clock_Declaration = Generalization(general=Declaration, specific=stext_Clock)
gen_stext_Operation_Declaration = Generalization(general=Declaration, specific=stext_Operation)
gen_stext_ConditionalExpression_Expression = Generalization(general=Expression, specific=stext_ConditionalExpression)
gen_stext_LogicalOrExpression_Expression = Generalization(general=Expression, specific=stext_LogicalOrExpression)
gen_stext_LogicalAndExpression_Expression = Generalization(general=Expression, specific=stext_LogicalAndExpression)
gen_stext_ReactionEffect_Effect = Generalization(general=Effect, specific=stext_ReactionEffect)
gen_stext_LogicalNotExpression_Expression = Generalization(general=Expression, specific=stext_LogicalNotExpression)
gen_stext_BitwiseXorExpression_Expression = Generalization(general=Expression, specific=stext_BitwiseXorExpression)
gen_stext_BitwiseOrExpression_Expression = Generalization(general=Expression, specific=stext_BitwiseOrExpression)
gen_stext_LogicalRelationExpression_Expression = Generalization(general=Expression, specific=stext_LogicalRelationExpression)
gen_stext_ShiftExpression_Expression = Generalization(general=Expression, specific=stext_ShiftExpression)
gen_stext_BitwiseAndExpression_Expression = Generalization(general=Expression, specific=stext_BitwiseAndExpression)
gen_stext_NumericalAddSubtractExpression_Expression = Generalization(general=Expression, specific=stext_NumericalAddSubtractExpression)
gen_stext_NumericalMultiplyDivideExpression_Expression = Generalization(general=Expression, specific=stext_NumericalMultiplyDivideExpression)
gen_stext_PrimitiveValueExpression_Expression = Generalization(general=Expression, specific=stext_PrimitiveValueExpression)
gen_stext_ElementReferenceExpression_Expression = Generalization(general=Expression, specific=stext_ElementReferenceExpression)
gen_stext_OperationCall_Expression = Generalization(general=Expression, specific=stext_OperationCall)
gen_stext_NumericalUnaryExpression_Expression = Generalization(general=Expression, specific=stext_NumericalUnaryExpression)

# Domain Model
domain_model = DomainModel(
    name="stext",
    types={stext_Root, stext_DefRoot, stext_StatechartDefinition, stext_StateRoot, stext_StateDeclaration, stext_TransitionRoot, stext_TransitionStatement, stext_Scope, stext_StatechartRoot, DefRoot, stext_EventDerivation, stext_Expression, stext_LocalReaction, Declaration, Reaction, stext_ReactionProperties, stext_TransitionReaction, TransitionStatement, stext_ReactionPriority, ReactionProperty, stext_EntryPointSpec, stext_Entrypoint, stext_ExitPointSpec, stext_Exitpoint, stext_EventSpec, stext_RegularEventSpec, EventSpec, stext_Event, stext_TimeEventSpec, stext_ReactionProperty, stext_BuiltinEventSpec, stext_EntryEvent, BuiltinEventSpec, stext_ExitEvent, stext_OnCycleEvent, stext_AlwaysEvent, stext_Assignment, Statement, stext_Variable, stext_EventRaising, stext_SimpleScope, Scope, stext_InterfaceScope, stext_InternalScope, stext_EventDefinition, Event, stext_VariableDefinition, Variable, stext_Clock, stext_ReactionTrigger, Trigger, stext_Operation, Expression, stext_LogicalOrExpression, stext_LogicalAndExpression, stext_ReactionEffect, Effect, stext_Statement, stext_ConditionalExpression, stext_LogicalNotExpression, stext_BitwiseXorExpression, stext_BitwiseOrExpression, stext_LogicalRelationExpression, stext_ShiftExpression, stext_BitwiseAndExpression, stext_NumericalAddSubtractExpression, stext_NumericalMultiplyDivideExpression, stext_PrimitiveValueExpression, stext_ElementReferenceExpression, stext_Declaration, stext_OperationCall, stext_NumericalUnaryExpression, Direction, AssignmentOperator, TimeEventType, ShiftOperator, AdditiveOperator, MultiplicativeOperator, RelationalOperator, TimeUnit, Type, UnaryOperator},
    associations={roots0, def_1, def_2, def_3, definitionScopes4, condition9, value10, properties13, properties14, scope6, entrypoint18, exitpoint19, event20, properties16, varRef21, expression22, event25, value27, derivation30, triggers32, guardExpression33, condition37, trueCase39, falseCase42, leftOperand45, rightOperand47, actions36, operand55, leftOperand57, rightOperand59, leftOperand62, rightOperand64, leftOperand50, rightOperand52, rightOperand69, leftOperand72, rightOperand74, leftOperand77, leftOperand67, leftOperand82, rightOperand84, leftOperand87, rightOperand89, rightOperand79, operand92, value94, operation95, args96},
    generalizations={gen_stext_StateRoot_DefRoot, gen_stext_TransitionRoot_DefRoot, gen_stext_StatechartRoot_DefRoot, gen_stext_LocalReaction_Declaration, gen_stext_LocalReaction_Reaction, gen_stext_TransitionReaction_TransitionStatement, gen_stext_TransitionReaction_Reaction, gen_stext_ReactionPriority_ReactionProperty, gen_stext_EntryPointSpec_ReactionProperty, gen_stext_ExitPointSpec_ReactionProperty, gen_stext_RegularEventSpec_EventSpec, gen_stext_TimeEventSpec_EventSpec, gen_stext_BuiltinEventSpec_EventSpec, gen_stext_EntryEvent_BuiltinEventSpec, gen_stext_ExitEvent_BuiltinEventSpec, gen_stext_OnCycleEvent_BuiltinEventSpec, gen_stext_AlwaysEvent_BuiltinEventSpec, gen_stext_Assignment_Statement, gen_stext_EventRaising_Statement, gen_stext_Expression_Statement, gen_stext_SimpleScope_Scope, gen_stext_InterfaceScope_Scope, gen_stext_InternalScope_Scope, gen_stext_EventDefinition_Event, gen_stext_VariableDefinition_Variable, gen_stext_Entrypoint_Declaration, gen_stext_Exitpoint_Declaration, gen_stext_ReactionTrigger_Trigger, gen_stext_Clock_Declaration, gen_stext_Operation_Declaration, gen_stext_ConditionalExpression_Expression, gen_stext_LogicalOrExpression_Expression, gen_stext_LogicalAndExpression_Expression, gen_stext_ReactionEffect_Effect, gen_stext_LogicalNotExpression_Expression, gen_stext_BitwiseXorExpression_Expression, gen_stext_BitwiseOrExpression_Expression, gen_stext_LogicalRelationExpression_Expression, gen_stext_ShiftExpression_Expression, gen_stext_BitwiseAndExpression_Expression, gen_stext_NumericalAddSubtractExpression_Expression, gen_stext_NumericalMultiplyDivideExpression_Expression, gen_stext_PrimitiveValueExpression_Expression, gen_stext_ElementReferenceExpression_Expression, gen_stext_OperationCall_Expression, gen_stext_NumericalUnaryExpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)