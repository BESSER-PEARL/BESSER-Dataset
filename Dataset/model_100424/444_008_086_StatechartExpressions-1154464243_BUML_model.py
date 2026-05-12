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
TimeUnit: Enumeration = Enumeration(
    name="TimeUnit",
    literals={
            EnumerationLiteral(name="second"),
			EnumerationLiteral(name="millisecond"),
			EnumerationLiteral(name="nanosecond")
    }
)

AssignmentOperator: Enumeration = Enumeration(
    name="AssignmentOperator",
    literals={
            EnumerationLiteral(name="multAssign"),
			EnumerationLiteral(name="divAssign"),
			EnumerationLiteral(name="modAssign"),
			EnumerationLiteral(name="addAssign"),
			EnumerationLiteral(name="subAssign"),
			EnumerationLiteral(name="leftShiftAssign"),
			EnumerationLiteral(name="rightShiftAssign"),
			EnumerationLiteral(name="andAssign"),
			EnumerationLiteral(name="xorAssign"),
			EnumerationLiteral(name="orAssign"),
			EnumerationLiteral(name="assign")
    }
)

EqualityOperator: Enumeration = Enumeration(
    name="EqualityOperator",
    literals={
            EnumerationLiteral(name="equals"),
			EnumerationLiteral(name="notEquals")
    }
)

RelationalOperator: Enumeration = Enumeration(
    name="RelationalOperator",
    literals={
            EnumerationLiteral(name="smaller"),
			EnumerationLiteral(name="greater"),
			EnumerationLiteral(name="smallerEqual"),
			EnumerationLiteral(name="greaterEqual")
    }
)

AdditiveOperator: Enumeration = Enumeration(
    name="AdditiveOperator",
    literals={
            EnumerationLiteral(name="plus"),
			EnumerationLiteral(name="minus")
    }
)

ShiftOperator: Enumeration = Enumeration(
    name="ShiftOperator",
    literals={
            EnumerationLiteral(name="left"),
			EnumerationLiteral(name="right")
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
			EnumerationLiteral(name="complement"),
			EnumerationLiteral(name="not_")
    }
)

# Classes
statechartexpressions_Expression = Class(name="statechartexpressions_Expression")
statechartexpressions_TriggerExpression = Class(name="statechartexpressions_TriggerExpression")
Expression = Class(name="Expression")
statechartexpressions_Trigger = Class(name="statechartexpressions_Trigger")
statechartexpressions_GuardExpression = Class(name="statechartexpressions_GuardExpression")
statechartexpressions_BooleanOrExpression = Class(name="statechartexpressions_BooleanOrExpression")
statechartexpressions_SignalEvent = Class(name="statechartexpressions_SignalEvent")
Event = Class(name="Event")
statechartexpressions_TimeEvent = Class(name="statechartexpressions_TimeEvent")
statechartexpressions_TimeExpression = Class(name="statechartexpressions_TimeExpression")
statechartexpressions_VariableReference = Class(name="statechartexpressions_VariableReference")
statechartexpressions_ActionExpression = Class(name="statechartexpressions_ActionExpression")
statechartexpressions_Statement = Class(name="statechartexpressions_Statement")
statechartexpressions_Event = Class(name="statechartexpressions_Event")
statechartexpressions_VariableAssignment = Class(name="statechartexpressions_VariableAssignment")
Statement = Class(name="Statement")
TimeExpression = Class(name="TimeExpression")
PrimaryExpression = Class(name="PrimaryExpression")
statechartexpressions_Variable = Class(name="statechartexpressions_Variable")
statechartexpressions_TimeConstant = Class(name="statechartexpressions_TimeConstant")
statechartexpressions_EventRaising = Class(name="statechartexpressions_EventRaising")
statechartexpressions_ConditionalExpression = Class(name="statechartexpressions_ConditionalExpression")
statechartexpressions_ProcedureCall = Class(name="statechartexpressions_ProcedureCall")
statechartexpressions_Procedure = Class(name="statechartexpressions_Procedure")
statechartexpressions_BitwiseOrExpression = Class(name="statechartexpressions_BitwiseOrExpression")
statechartexpressions_BitwiseAndExpression = Class(name="statechartexpressions_BitwiseAndExpression")
statechartexpressions_BooleanAndExpression = Class(name="statechartexpressions_BooleanAndExpression")
statechartexpressions_BitwiseXorExpression = Class(name="statechartexpressions_BitwiseXorExpression")
statechartexpressions_RelationalExpression = Class(name="statechartexpressions_RelationalExpression")
statechartexpressions_ShiftExpression = Class(name="statechartexpressions_ShiftExpression")
statechartexpressions_EqualityExpression = Class(name="statechartexpressions_EqualityExpression")
statechartexpressions_AdditiveExpression = Class(name="statechartexpressions_AdditiveExpression")
statechartexpressions_UnaryExpression = Class(name="statechartexpressions_UnaryExpression")
statechartexpressions_MultiplicativeExpression = Class(name="statechartexpressions_MultiplicativeExpression")
statechartexpressions_NestedExpression = Class(name="statechartexpressions_NestedExpression")
statechartexpressions_LiteralValue = Class(name="statechartexpressions_LiteralValue")
statechartexpressions_PrimaryExpression = Class(name="statechartexpressions_PrimaryExpression")

# statechartexpressions_Expression class attributes and methods

# statechartexpressions_TriggerExpression class attributes and methods

# Expression class attributes and methods

# statechartexpressions_Trigger class attributes and methods

# statechartexpressions_GuardExpression class attributes and methods

# statechartexpressions_BooleanOrExpression class attributes and methods

# statechartexpressions_SignalEvent class attributes and methods
statechartexpressions_SignalEvent_identifier: Property = Property(name="identifier", type=StringType)
statechartexpressions_SignalEvent.attributes={statechartexpressions_SignalEvent_identifier}

# Event class attributes and methods

# statechartexpressions_TimeEvent class attributes and methods

# statechartexpressions_TimeExpression class attributes and methods

# statechartexpressions_VariableReference class attributes and methods

# statechartexpressions_ActionExpression class attributes and methods

# statechartexpressions_Statement class attributes and methods

# statechartexpressions_Event class attributes and methods

# statechartexpressions_VariableAssignment class attributes and methods
statechartexpressions_VariableAssignment_operator: Property = Property(name="operator", type=StringType)
statechartexpressions_VariableAssignment.attributes={statechartexpressions_VariableAssignment_operator}

# Statement class attributes and methods

# TimeExpression class attributes and methods

# PrimaryExpression class attributes and methods

# statechartexpressions_Variable class attributes and methods
statechartexpressions_Variable_identifier: Property = Property(name="identifier", type=StringType)
statechartexpressions_Variable.attributes={statechartexpressions_Variable_identifier}

# statechartexpressions_TimeConstant class attributes and methods
statechartexpressions_TimeConstant_value: Property = Property(name="value", type=IntegerType)
statechartexpressions_TimeConstant_unit: Property = Property(name="unit", type=StringType)
statechartexpressions_TimeConstant.attributes={statechartexpressions_TimeConstant_unit, statechartexpressions_TimeConstant_value}

# statechartexpressions_EventRaising class attributes and methods

# statechartexpressions_ConditionalExpression class attributes and methods

# statechartexpressions_ProcedureCall class attributes and methods

# statechartexpressions_Procedure class attributes and methods
statechartexpressions_Procedure_identifier: Property = Property(name="identifier", type=StringType)
statechartexpressions_Procedure.attributes={statechartexpressions_Procedure_identifier}

# statechartexpressions_BitwiseOrExpression class attributes and methods

# statechartexpressions_BitwiseAndExpression class attributes and methods

# statechartexpressions_BooleanAndExpression class attributes and methods

# statechartexpressions_BitwiseXorExpression class attributes and methods

# statechartexpressions_RelationalExpression class attributes and methods
statechartexpressions_RelationalExpression_operator: Property = Property(name="operator", type=StringType)
statechartexpressions_RelationalExpression.attributes={statechartexpressions_RelationalExpression_operator}

# statechartexpressions_ShiftExpression class attributes and methods
statechartexpressions_ShiftExpression_operator: Property = Property(name="operator", type=StringType)
statechartexpressions_ShiftExpression.attributes={statechartexpressions_ShiftExpression_operator}

# statechartexpressions_EqualityExpression class attributes and methods
statechartexpressions_EqualityExpression_operator: Property = Property(name="operator", type=StringType)
statechartexpressions_EqualityExpression.attributes={statechartexpressions_EqualityExpression_operator}

# statechartexpressions_AdditiveExpression class attributes and methods
statechartexpressions_AdditiveExpression_operator: Property = Property(name="operator", type=StringType)
statechartexpressions_AdditiveExpression.attributes={statechartexpressions_AdditiveExpression_operator}

# statechartexpressions_UnaryExpression class attributes and methods
statechartexpressions_UnaryExpression_operator: Property = Property(name="operator", type=StringType)
statechartexpressions_UnaryExpression.attributes={statechartexpressions_UnaryExpression_operator}

# statechartexpressions_MultiplicativeExpression class attributes and methods
statechartexpressions_MultiplicativeExpression_operator: Property = Property(name="operator", type=StringType)
statechartexpressions_MultiplicativeExpression.attributes={statechartexpressions_MultiplicativeExpression_operator}

# statechartexpressions_NestedExpression class attributes and methods

# statechartexpressions_LiteralValue class attributes and methods
statechartexpressions_LiteralValue_value: Property = Property(name="value", type=StringType)
statechartexpressions_LiteralValue.attributes={statechartexpressions_LiteralValue_value}

# statechartexpressions_PrimaryExpression class attributes and methods

# Relationships
triggers0: BinaryAssociation = BinaryAssociation(
    name="triggers0",
    ends={
        Property(name="statechartexpressions_Trigger", type=statechartexpressions_TriggerExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="statechartexpressions_TriggerExpression", type=statechartexpressions_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression1: BinaryAssociation = BinaryAssociation(
    name="expression1",
    ends={
        Property(name="statechartexpressions_BooleanOrExpression", type=statechartexpressions_GuardExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="statechartexpressions_GuardExpression", type=statechartexpressions_BooleanOrExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
event3: BinaryAssociation = BinaryAssociation(
    name="event3",
    ends={
        Property(name="statechartexpressions_Trigger4", type=statechartexpressions_Event, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="statechartexpressions_Event", type=statechartexpressions_Trigger, multiplicity=Multiplicity(1, 1))
    }
)
duration5: BinaryAssociation = BinaryAssociation(
    name="duration5",
    ends={
        Property(name="statechartexpressions_TimeExpression", type=statechartexpressions_TimeEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="statechartexpressions_TimeEvent", type=statechartexpressions_TimeExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement2: BinaryAssociation = BinaryAssociation(
    name="statement2",
    ends={
        Property(name="statechartexpressions_Statement", type=statechartexpressions_ActionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="statechartexpressions_ActionExpression", type=statechartexpressions_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variableReference7: BinaryAssociation = BinaryAssociation(
    name="variableReference7",
    ends={
        Property(name="statechartexpressions_VariableReference8", type=statechartexpressions_VariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="statechartexpressions_VariableAssignment", type=statechartexpressions_VariableReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable6: BinaryAssociation = BinaryAssociation(
    name="variable6",
    ends={
        Property(name="statechartexpressions_Variable", type=statechartexpressions_VariableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="statechartexpressions_VariableReference", type=statechartexpressions_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value9: BinaryAssociation = BinaryAssociation(
    name="value9",
    ends={
        Property(name="statechartexpressions_ConditionalExpression", type=statechartexpressions_VariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="statechartexpressions_VariableAssignment10", type=statechartexpressions_ConditionalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
procedure11: BinaryAssociation = BinaryAssociation(
    name="procedure11",
    ends={
        Property(name="statechartexpressions_Procedure", type=statechartexpressions_ProcedureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="statechartexpressions_ProcedureCall", type=statechartexpressions_Procedure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand220: BinaryAssociation = BinaryAssociation(
    name="operand220",
    ends={
        Property(name="statechartexpressions_BitwiseXorExpression22", type=statechartexpressions_BooleanAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="statechartexpressions_BooleanAndExpression21", type=statechartexpressions_BitwiseXorExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand123: BinaryAssociation = BinaryAssociation(
    name="operand123",
    ends={
        Property(name="statechartexpressions_BitwiseOrExpression", type=statechartexpressions_BitwiseXorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="statechartexpressions_BitwiseXorExpression24", type=statechartexpressions_BitwiseOrExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand225: BinaryAssociation = BinaryAssociation(
    name="operand225",
    ends={
        Property(name="statechartexpressions_BitwiseOrExpression27", type=statechartexpressions_BitwiseXorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="statechartexpressions_BitwiseXorExpression26", type=statechartexpressions_BitwiseOrExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand128: BinaryAssociation = BinaryAssociation(
    name="operand128",
    ends={
        Property(name="statechartexpressions_BitwiseAndExpression", type=statechartexpressions_BitwiseOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="statechartexpressions_BitwiseOrExpression29", type=statechartexpressions_BitwiseAndExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
event12: BinaryAssociation = BinaryAssociation(
    name="event12",
    ends={
        Property(name="statechartexpressions_SignalEvent", type=statechartexpressions_EventRaising, multiplicity=Multiplicity(1, 1)),
        Property(name="statechartexpressions_EventRaising", type=statechartexpressions_SignalEvent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand113: BinaryAssociation = BinaryAssociation(
    name="operand113",
    ends={
        Property(name="statechartexpressions_BooleanAndExpression", type=statechartexpressions_BooleanOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="statechartexpressions_BooleanOrExpression14", type=statechartexpressions_BooleanAndExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand215: BinaryAssociation = BinaryAssociation(
    name="operand215",
    ends={
        Property(name="statechartexpressions_BooleanAndExpression17", type=statechartexpressions_BooleanOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="statechartexpressions_BooleanOrExpression16", type=statechartexpressions_BooleanAndExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand118: BinaryAssociation = BinaryAssociation(
    name="operand118",
    ends={
        Property(name="statechartexpressions_BitwiseXorExpression", type=statechartexpressions_BooleanAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="statechartexpressions_BooleanAndExpression19", type=statechartexpressions_BitwiseXorExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand138: BinaryAssociation = BinaryAssociation(
    name="operand138",
    ends={
        Property(name="statechartexpressions_RelationalExpression", type=statechartexpressions_EqualityExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="statechartexpressions_EqualityExpression39", type=statechartexpressions_RelationalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand240: BinaryAssociation = BinaryAssociation(
    name="operand240",
    ends={
        Property(name="statechartexpressions_RelationalExpression42", type=statechartexpressions_EqualityExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="statechartexpressions_EqualityExpression41", type=statechartexpressions_RelationalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand230: BinaryAssociation = BinaryAssociation(
    name="operand230",
    ends={
        Property(name="statechartexpressions_BitwiseAndExpression32", type=statechartexpressions_BitwiseOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="statechartexpressions_BitwiseOrExpression31", type=statechartexpressions_BitwiseAndExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand133: BinaryAssociation = BinaryAssociation(
    name="operand133",
    ends={
        Property(name="statechartexpressions_EqualityExpression", type=statechartexpressions_BitwiseAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="statechartexpressions_BitwiseAndExpression34", type=statechartexpressions_EqualityExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand235: BinaryAssociation = BinaryAssociation(
    name="operand235",
    ends={
        Property(name="statechartexpressions_EqualityExpression37", type=statechartexpressions_BitwiseAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="statechartexpressions_BitwiseAndExpression36", type=statechartexpressions_EqualityExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand148: BinaryAssociation = BinaryAssociation(
    name="operand148",
    ends={
        Property(name="statechartexpressions_BooleanOrExpression50", type=statechartexpressions_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="statechartexpressions_ConditionalExpression49", type=statechartexpressions_BooleanOrExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand251: BinaryAssociation = BinaryAssociation(
    name="operand251",
    ends={
        Property(name="statechartexpressions_ShiftExpression53", type=statechartexpressions_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="statechartexpressions_ConditionalExpression52", type=statechartexpressions_ShiftExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand354: BinaryAssociation = BinaryAssociation(
    name="operand354",
    ends={
        Property(name="statechartexpressions_ShiftExpression56", type=statechartexpressions_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="statechartexpressions_ConditionalExpression55", type=statechartexpressions_ShiftExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand157: BinaryAssociation = BinaryAssociation(
    name="operand157",
    ends={
        Property(name="statechartexpressions_AdditiveExpression", type=statechartexpressions_ShiftExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="statechartexpressions_ShiftExpression58", type=statechartexpressions_AdditiveExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand143: BinaryAssociation = BinaryAssociation(
    name="operand143",
    ends={
        Property(name="statechartexpressions_ShiftExpression", type=statechartexpressions_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="statechartexpressions_RelationalExpression44", type=statechartexpressions_ShiftExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand245: BinaryAssociation = BinaryAssociation(
    name="operand245",
    ends={
        Property(name="statechartexpressions_ShiftExpression47", type=statechartexpressions_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="statechartexpressions_RelationalExpression46", type=statechartexpressions_ShiftExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand264: BinaryAssociation = BinaryAssociation(
    name="operand264",
    ends={
        Property(name="statechartexpressions_MultiplicativeExpression66", type=statechartexpressions_AdditiveExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="statechartexpressions_AdditiveExpression65", type=statechartexpressions_MultiplicativeExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand167: BinaryAssociation = BinaryAssociation(
    name="operand167",
    ends={
        Property(name="statechartexpressions_UnaryExpression", type=statechartexpressions_MultiplicativeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="statechartexpressions_MultiplicativeExpression68", type=statechartexpressions_UnaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand269: BinaryAssociation = BinaryAssociation(
    name="operand269",
    ends={
        Property(name="statechartexpressions_UnaryExpression71", type=statechartexpressions_MultiplicativeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="statechartexpressions_MultiplicativeExpression70", type=statechartexpressions_UnaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand259: BinaryAssociation = BinaryAssociation(
    name="operand259",
    ends={
        Property(name="statechartexpressions_AdditiveExpression61", type=statechartexpressions_ShiftExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="statechartexpressions_ShiftExpression60", type=statechartexpressions_AdditiveExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand162: BinaryAssociation = BinaryAssociation(
    name="operand162",
    ends={
        Property(name="statechartexpressions_MultiplicativeExpression", type=statechartexpressions_AdditiveExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="statechartexpressions_AdditiveExpression63", type=statechartexpressions_MultiplicativeExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression74: BinaryAssociation = BinaryAssociation(
    name="expression74",
    ends={
        Property(name="statechartexpressions_ConditionalExpression75", type=statechartexpressions_NestedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="statechartexpressions_NestedExpression", type=statechartexpressions_ConditionalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand72: BinaryAssociation = BinaryAssociation(
    name="operand72",
    ends={
        Property(name="statechartexpressions_PrimaryExpression", type=statechartexpressions_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="statechartexpressions_UnaryExpression73", type=statechartexpressions_PrimaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_statechartexpressions_TriggerExpression_Expression = Generalization(general=Expression, specific=statechartexpressions_TriggerExpression)
gen_statechartexpressions_GuardExpression_Expression = Generalization(general=Expression, specific=statechartexpressions_GuardExpression)
gen_statechartexpressions_SignalEvent_Event = Generalization(general=Event, specific=statechartexpressions_SignalEvent)
gen_statechartexpressions_TimeEvent_Event = Generalization(general=Event, specific=statechartexpressions_TimeEvent)
gen_statechartexpressions_ActionExpression_Expression = Generalization(general=Expression, specific=statechartexpressions_ActionExpression)
gen_statechartexpressions_VariableAssignment_Statement = Generalization(general=Statement, specific=statechartexpressions_VariableAssignment)
gen_statechartexpressions_VariableReference_TimeExpression = Generalization(general=TimeExpression, specific=statechartexpressions_VariableReference)
gen_statechartexpressions_VariableReference_PrimaryExpression = Generalization(general=PrimaryExpression, specific=statechartexpressions_VariableReference)
gen_statechartexpressions_TimeConstant_TimeExpression = Generalization(general=TimeExpression, specific=statechartexpressions_TimeConstant)
gen_statechartexpressions_EventRaising_Statement = Generalization(general=Statement, specific=statechartexpressions_EventRaising)
gen_statechartexpressions_ProcedureCall_Statement = Generalization(general=Statement, specific=statechartexpressions_ProcedureCall)
gen_statechartexpressions_NestedExpression_PrimaryExpression = Generalization(general=PrimaryExpression, specific=statechartexpressions_NestedExpression)
gen_statechartexpressions_LiteralValue_PrimaryExpression = Generalization(general=PrimaryExpression, specific=statechartexpressions_LiteralValue)

# Domain Model
domain_model = DomainModel(
    name="statechartexpressions",
    types={statechartexpressions_Expression, statechartexpressions_TriggerExpression, Expression, statechartexpressions_Trigger, statechartexpressions_GuardExpression, statechartexpressions_BooleanOrExpression, statechartexpressions_SignalEvent, Event, statechartexpressions_TimeEvent, statechartexpressions_TimeExpression, statechartexpressions_VariableReference, statechartexpressions_ActionExpression, statechartexpressions_Statement, statechartexpressions_Event, statechartexpressions_VariableAssignment, Statement, TimeExpression, PrimaryExpression, statechartexpressions_Variable, statechartexpressions_TimeConstant, statechartexpressions_EventRaising, statechartexpressions_ConditionalExpression, statechartexpressions_ProcedureCall, statechartexpressions_Procedure, statechartexpressions_BitwiseOrExpression, statechartexpressions_BitwiseAndExpression, statechartexpressions_BooleanAndExpression, statechartexpressions_BitwiseXorExpression, statechartexpressions_RelationalExpression, statechartexpressions_ShiftExpression, statechartexpressions_EqualityExpression, statechartexpressions_AdditiveExpression, statechartexpressions_UnaryExpression, statechartexpressions_MultiplicativeExpression, statechartexpressions_NestedExpression, statechartexpressions_LiteralValue, statechartexpressions_PrimaryExpression, TimeUnit, AssignmentOperator, EqualityOperator, RelationalOperator, AdditiveOperator, ShiftOperator, MultiplicativeOperator, UnaryOperator},
    associations={triggers0, expression1, event3, duration5, statement2, variableReference7, variable6, value9, procedure11, operand220, operand123, operand225, operand128, event12, operand113, operand215, operand118, operand138, operand240, operand230, operand133, operand235, operand148, operand251, operand354, operand157, operand143, operand245, operand264, operand167, operand269, operand259, operand162, expression74, operand72},
    generalizations={gen_statechartexpressions_TriggerExpression_Expression, gen_statechartexpressions_GuardExpression_Expression, gen_statechartexpressions_SignalEvent_Event, gen_statechartexpressions_TimeEvent_Event, gen_statechartexpressions_ActionExpression_Expression, gen_statechartexpressions_VariableAssignment_Statement, gen_statechartexpressions_VariableReference_TimeExpression, gen_statechartexpressions_VariableReference_PrimaryExpression, gen_statechartexpressions_TimeConstant_TimeExpression, gen_statechartexpressions_EventRaising_Statement, gen_statechartexpressions_ProcedureCall_Statement, gen_statechartexpressions_NestedExpression_PrimaryExpression, gen_statechartexpressions_LiteralValue_PrimaryExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)