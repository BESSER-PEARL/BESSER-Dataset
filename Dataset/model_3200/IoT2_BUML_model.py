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
BoardType: Enumeration = Enumeration(
    name="BoardType",
    literals={
            EnumerationLiteral(name="RaspberryPi"),
			EnumerationLiteral(name="Arduino"),
			EnumerationLiteral(name="BeagleBoard")
    }
)

PrimitiveKind: Enumeration = Enumeration(
    name="PrimitiveKind",
    literals={
            EnumerationLiteral(name="PK_NULL"),
			EnumerationLiteral(name="PK_VOID"),
			EnumerationLiteral(name="PK_SHORT"),
			EnumerationLiteral(name="PK_LONG"),
			EnumerationLiteral(name="PK_USHORT"),
			EnumerationLiteral(name="PK_ULONG"),
			EnumerationLiteral(name="PK_FLOAT"),
			EnumerationLiteral(name="PK_DOUBLE"),
			EnumerationLiteral(name="PK_BOOLEAN"),
			EnumerationLiteral(name="PK_CHAR"),
			EnumerationLiteral(name="PK_OCTET"),
			EnumerationLiteral(name="PK_ANY"),
			EnumerationLiteral(name="PK_LONGDOUBLE"),
			EnumerationLiteral(name="PK_WSTRING"),
			EnumerationLiteral(name="PK_TYPECODE"),
			EnumerationLiteral(name="PK_WCHAR"),
			EnumerationLiteral(name="PK_PRINCIPAL"),
			EnumerationLiteral(name="PK_STRING"),
			EnumerationLiteral(name="PK_ULONGLONG"),
			EnumerationLiteral(name="PK_OBJREF"),
			EnumerationLiteral(name="PK_LONGLONG")
    }
)

ParameterMode: Enumeration = Enumeration(
    name="ParameterMode",
    literals={
            EnumerationLiteral(name="PARAM_IN"),
			EnumerationLiteral(name="PARAM_OUT"),
			EnumerationLiteral(name="PARAM_INOUT")
    }
)

BooleanUnaryOperator: Enumeration = Enumeration(
    name="BooleanUnaryOperator",
    literals={
            EnumerationLiteral(name="NOT")
    }
)

BooleanBinaryOperator: Enumeration = Enumeration(
    name="BooleanBinaryOperator",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR")
    }
)

IntegerCalculationOperator: Enumeration = Enumeration(
    name="IntegerCalculationOperator",
    literals={
            EnumerationLiteral(name="ADD"),
			EnumerationLiteral(name="SUBRACT")
    }
)

IntegerComparisonOperator: Enumeration = Enumeration(
    name="IntegerComparisonOperator",
    literals={
            EnumerationLiteral(name="SMALLER_EQUALS"),
			EnumerationLiteral(name="EQUALS"),
			EnumerationLiteral(name="GREATER_EQUALS"),
			EnumerationLiteral(name="GREATER"),
			EnumerationLiteral(name="SMALLER")
    }
)

# Classes
iot2_System = Class(name="iot2_System")
iot2_HWComponent = Class(name="iot2_HWComponent", is_abstract=True)
iot2_Board = Class(name="iot2_Board")
iot2_Sketch = Class(name="iot2_Sketch")
iot2_Activity = Class(name="iot2_Activity")
iot2_OperationDef = Class(name="iot2_OperationDef")
iot2_Sensor = Class(name="iot2_Sensor")
HWComponent = Class(name="HWComponent")
iot2_ExceptionDef = Class(name="iot2_ExceptionDef")
iot2_Block = Class(name="iot2_Block")
iot2_Contained = Class(name="iot2_Contained", is_abstract=True)
iot2_Container = Class(name="iot2_Container", is_abstract=True)
iot2_NamedElement = Class(name="iot2_NamedElement", is_abstract=True)
iot2_Typed = Class(name="iot2_Typed", is_abstract=True)
iot2_IDLType = Class(name="iot2_IDLType", is_abstract=True)
iot2_TypedefDef = Class(name="iot2_TypedefDef", is_abstract=True)
iot2_Actuator = Class(name="iot2_Actuator")
NamedElement = Class(name="NamedElement")
iot2_ActivityNode = Class(name="iot2_ActivityNode")
iot2_ActivityEdge = Class(name="iot2_ActivityEdge", is_abstract=True)
iot2_Variable = Class(name="iot2_Variable")
Contained = Class(name="Contained")
Typed = Class(name="Typed")
iot2_ParameterDef = Class(name="iot2_ParameterDef")
iot2_PrimitiveDef = Class(name="iot2_PrimitiveDef")
iot2_Chunk = Class(name="iot2_Chunk")
Chunk = Class(name="Chunk")
iot2_Statement = Class(name="iot2_Statement")
iot2_LastStatement = Class(name="iot2_LastStatement")
iot2_LastStatement_Return = Class(name="iot2_LastStatement_Return")
LastStatement = Class(name="LastStatement")
iot2_LastStatement_Break = Class(name="iot2_LastStatement_Break")
iot2_Statement_Block = Class(name="iot2_Statement_Block")
Statement = Class(name="Statement")
IDLType = Class(name="IDLType")
iot2_Field = Class(name="iot2_Field")
iot2_Expression = Class(name="iot2_Expression")
iot2_Statement_For_Numeric = Class(name="iot2_Statement_For_Numeric")
iot2_Statement_For_Generic = Class(name="iot2_Statement_For_Generic")
iot2_Statement_GlobalFunction_Declaration = Class(name="iot2_Statement_GlobalFunction_Declaration")
iot2_Function = Class(name="iot2_Function")
iot2_Statement_LocalFunction_Declaration = Class(name="iot2_Statement_LocalFunction_Declaration")
iot2_Statement_While = Class(name="iot2_Statement_While")
iot2_Statement_Repeat = Class(name="iot2_Statement_Repeat")
iot2_Statement_If_Then_Else = Class(name="iot2_Statement_If_Then_Else")
iot2_Statement_If_Then_Else_ElseIfPart = Class(name="iot2_Statement_If_Then_Else_ElseIfPart")
iot2_Expression_TableConstructor = Class(name="iot2_Expression_TableConstructor")
iot2_Functioncall_Arguments = Class(name="iot2_Functioncall_Arguments")
iot2_Field_AddEntryToTable_Brackets = Class(name="iot2_Field_AddEntryToTable_Brackets")
Field = Class(name="Field")
iot2_Field_AddEntryToTable = Class(name="iot2_Field_AddEntryToTable")
iot2_Field_AppendEntryToTable = Class(name="iot2_Field_AppendEntryToTable")
iot2_LastStatement_ReturnWithValue = Class(name="iot2_LastStatement_ReturnWithValue")
LastStatement_Return = Class(name="LastStatement_Return")
iot2_Statement_Assignment = Class(name="iot2_Statement_Assignment")
iot2_Statement_Local_Variable_Declaration = Class(name="iot2_Statement_Local_Variable_Declaration")
iot2_Statement_FunctioncallOrAssignment = Class(name="iot2_Statement_FunctioncallOrAssignment")
Statement_FunctioncallOrAssignment = Class(name="Statement_FunctioncallOrAssignment")
iot2_Expression_Nil = Class(name="iot2_Expression_Nil")
Expression = Class(name="Expression")
iot2_Expression_True = Class(name="iot2_Expression_True")
iot2_Expression_False = Class(name="iot2_Expression_False")
iot2_Expression_Number = Class(name="iot2_Expression_Number")
iot2_Expression_VarArgs = Class(name="iot2_Expression_VarArgs")
iot2_Expression_String = Class(name="iot2_Expression_String")
iot2_Expression_Function = Class(name="iot2_Expression_Function")
iot2_Expression_Or = Class(name="iot2_Expression_Or")
iot2_Expression_And = Class(name="iot2_Expression_And")
iot2_Expression_Larger = Class(name="iot2_Expression_Larger")
iot2_Expression_Larger_Equal = Class(name="iot2_Expression_Larger_Equal")
iot2_Statement_CallMemberFunction = Class(name="iot2_Statement_CallMemberFunction")
iot2_Statement_CallFunction = Class(name="iot2_Statement_CallFunction")
iot2_Expression_Concatenation = Class(name="iot2_Expression_Concatenation")
iot2_Expression_Plus = Class(name="iot2_Expression_Plus")
iot2_Expression_Minus = Class(name="iot2_Expression_Minus")
iot2_Expression_Smaller = Class(name="iot2_Expression_Smaller")
iot2_Expression_Multiplication = Class(name="iot2_Expression_Multiplication")
iot2_Expression_Smaller_Equal = Class(name="iot2_Expression_Smaller_Equal")
iot2_Expression_Equal = Class(name="iot2_Expression_Equal")
iot2_Expression_Not_Equal = Class(name="iot2_Expression_Not_Equal")
iot2_Expression_Negate = Class(name="iot2_Expression_Negate")
iot2_Expression_Length = Class(name="iot2_Expression_Length")
iot2_Expression_Invert = Class(name="iot2_Expression_Invert")
iot2_Expression_Exponentiation = Class(name="iot2_Expression_Exponentiation")
iot2_Expression_Division = Class(name="iot2_Expression_Division")
iot2_Expression_Modulo = Class(name="iot2_Expression_Modulo")
iot2_Expression_AccessMember = Class(name="iot2_Expression_AccessMember")
iot2_Expression_VariableName = Class(name="iot2_Expression_VariableName")
iot2_Expression_CallMemberFunction = Class(name="iot2_Expression_CallMemberFunction")
iot2_Expression_CallFunction = Class(name="iot2_Expression_CallFunction")
iot2_Expression_AccessArray = Class(name="iot2_Expression_AccessArray")
iot2_InitialNode = Class(name="iot2_InitialNode")
ControlNode = Class(name="ControlNode")
iot2_FinalNode = Class(name="iot2_FinalNode", is_abstract=True)
iot2_ActivityFinalNode = Class(name="iot2_ActivityFinalNode")
FinalNode = Class(name="FinalNode")
iot2_ForkNode = Class(name="iot2_ForkNode")
iot2_JoinNode = Class(name="iot2_JoinNode")
iot2_MergeNode = Class(name="iot2_MergeNode")
iot2_DecisionNode = Class(name="iot2_DecisionNode")
iot2_Value = Class(name="iot2_Value")
iot2_IntegerVariable = Class(name="iot2_IntegerVariable")
Variable = Class(name="Variable")
iot2_BooleanValue = Class(name="iot2_BooleanValue")
Value = Class(name="Value")
iot2_IntegerValue = Class(name="iot2_IntegerValue")
iot2_IntegerExpression = Class(name="iot2_IntegerExpression", is_abstract=True)
iot2_ControlFlow = Class(name="iot2_ControlFlow")
ActivityEdge = Class(name="ActivityEdge")
iot2_BooleanVariable = Class(name="iot2_BooleanVariable")
iot2_ControlNode = Class(name="iot2_ControlNode", is_abstract=True)
ActivityNode = Class(name="ActivityNode")
iot2_ExecutableNode = Class(name="iot2_ExecutableNode", is_abstract=True)
iot2_Action = Class(name="iot2_Action", is_abstract=True)
ExecutableNode = Class(name="ExecutableNode")
iot2_OpaqueAction = Class(name="iot2_OpaqueAction")
Action = Class(name="Action")
iot2_BooleanUnaryExpression = Class(name="iot2_BooleanUnaryExpression")
BooleanExpression = Class(name="BooleanExpression")
iot2_BooleanBinaryExpression = Class(name="iot2_BooleanBinaryExpression")
iot2_InputValue = Class(name="iot2_InputValue")
iot2_Input = Class(name="iot2_Input")
iot2_Token = Class(name="iot2_Token")
iot2_BooleanExpression = Class(name="iot2_BooleanExpression", is_abstract=True)
iot2_IntegerCalculationExpression = Class(name="iot2_IntegerCalculationExpression")
IntegerExpression = Class(name="IntegerExpression")
iot2_IntegerComparisonExpression = Class(name="iot2_IntegerComparisonExpression")
iot2_Trace = Class(name="iot2_Trace")

# iot2_System class attributes and methods
iot2_System_name: Property = Property(name="name", type=StringType)
iot2_System.attributes={iot2_System_name}

# iot2_HWComponent class attributes and methods
iot2_HWComponent_name: Property = Property(name="name", type=StringType)
iot2_HWComponent.attributes={iot2_HWComponent_name}

# iot2_Board class attributes and methods
iot2_Board_name: Property = Property(name="name", type=StringType)
iot2_Board_type: Property = Property(name="type", type=StringType)
iot2_Board.attributes={iot2_Board_name, iot2_Board_type}

# iot2_Sketch class attributes and methods

# iot2_Activity class attributes and methods

# iot2_OperationDef class attributes and methods
iot2_OperationDef_isOneway: Property = Property(name="isOneway", type=BooleanType)
iot2_OperationDef_contexts: Property = Property(name="contexts", type=StringType)
iot2_OperationDef.attributes={iot2_OperationDef_contexts, iot2_OperationDef_isOneway}

# iot2_Sensor class attributes and methods

# HWComponent class attributes and methods

# iot2_ExceptionDef class attributes and methods
iot2_ExceptionDef_typeCode: Property = Property(name="typeCode", type=StringType)
iot2_ExceptionDef.attributes={iot2_ExceptionDef_typeCode}

# iot2_Block class attributes and methods

# iot2_Contained class attributes and methods
iot2_Contained_repositoryId: Property = Property(name="repositoryId", type=StringType)
iot2_Contained_version: Property = Property(name="version", type=StringType)
iot2_Contained_absoluteName: Property = Property(name="absoluteName", type=StringType)
iot2_Contained.attributes={iot2_Contained_version, iot2_Contained_repositoryId, iot2_Contained_absoluteName}

# iot2_Container class attributes and methods

# iot2_NamedElement class attributes and methods
iot2_NamedElement_identifier: Property = Property(name="identifier", type=StringType)
iot2_NamedElement_name: Property = Property(name="name", type=StringType)
iot2_NamedElement.attributes={iot2_NamedElement_name, iot2_NamedElement_identifier}

# iot2_Typed class attributes and methods

# iot2_IDLType class attributes and methods
iot2_IDLType_typeCode: Property = Property(name="typeCode", type=StringType)
iot2_IDLType.attributes={iot2_IDLType_typeCode}

# iot2_TypedefDef class attributes and methods

# iot2_Actuator class attributes and methods

# NamedElement class attributes and methods

# iot2_ActivityNode class attributes and methods
iot2_ActivityNode_running: Property = Property(name="running", type=BooleanType)
iot2_ActivityNode.attributes={iot2_ActivityNode_running}

# iot2_ActivityEdge class attributes and methods

# iot2_Variable class attributes and methods
iot2_Variable_name: Property = Property(name="name", type=StringType)
iot2_Variable.attributes={iot2_Variable_name}

# Contained class attributes and methods

# Typed class attributes and methods

# iot2_ParameterDef class attributes and methods
iot2_ParameterDef_identifier: Property = Property(name="identifier", type=StringType)
iot2_ParameterDef_direction: Property = Property(name="direction", type=StringType)
iot2_ParameterDef.attributes={iot2_ParameterDef_direction, iot2_ParameterDef_identifier}

# iot2_PrimitiveDef class attributes and methods
iot2_PrimitiveDef_kind: Property = Property(name="kind", type=StringType)
iot2_PrimitiveDef.attributes={iot2_PrimitiveDef_kind}

# iot2_Chunk class attributes and methods

# Chunk class attributes and methods

# iot2_Statement class attributes and methods

# iot2_LastStatement class attributes and methods

# iot2_LastStatement_Return class attributes and methods

# LastStatement class attributes and methods

# iot2_LastStatement_Break class attributes and methods

# iot2_Statement_Block class attributes and methods

# Statement class attributes and methods

# IDLType class attributes and methods

# iot2_Field class attributes and methods
iot2_Field_identifier: Property = Property(name="identifier", type=StringType)
iot2_Field.attributes={iot2_Field_identifier}

# iot2_Expression class attributes and methods

# iot2_Statement_For_Numeric class attributes and methods
iot2_Statement_For_Numeric_iteratorName: Property = Property(name="iteratorName", type=StringType)
iot2_Statement_For_Numeric.attributes={iot2_Statement_For_Numeric_iteratorName}

# iot2_Statement_For_Generic class attributes and methods
iot2_Statement_For_Generic_names: Property = Property(name="names", type=StringType)
iot2_Statement_For_Generic.attributes={iot2_Statement_For_Generic_names}

# iot2_Statement_GlobalFunction_Declaration class attributes and methods
iot2_Statement_GlobalFunction_Declaration_prefix: Property = Property(name="prefix", type=StringType)
iot2_Statement_GlobalFunction_Declaration_functionName: Property = Property(name="functionName", type=StringType)
iot2_Statement_GlobalFunction_Declaration.attributes={iot2_Statement_GlobalFunction_Declaration_functionName, iot2_Statement_GlobalFunction_Declaration_prefix}

# iot2_Function class attributes and methods
iot2_Function_parameters: Property = Property(name="parameters", type=StringType)
iot2_Function_varArgs: Property = Property(name="varArgs", type=BooleanType)
iot2_Function.attributes={iot2_Function_varArgs, iot2_Function_parameters}

# iot2_Statement_LocalFunction_Declaration class attributes and methods
iot2_Statement_LocalFunction_Declaration_functionName: Property = Property(name="functionName", type=StringType)
iot2_Statement_LocalFunction_Declaration.attributes={iot2_Statement_LocalFunction_Declaration_functionName}

# iot2_Statement_While class attributes and methods

# iot2_Statement_Repeat class attributes and methods

# iot2_Statement_If_Then_Else class attributes and methods

# iot2_Statement_If_Then_Else_ElseIfPart class attributes and methods

# iot2_Expression_TableConstructor class attributes and methods

# iot2_Functioncall_Arguments class attributes and methods

# iot2_Field_AddEntryToTable_Brackets class attributes and methods

# Field class attributes and methods

# iot2_Field_AddEntryToTable class attributes and methods
iot2_Field_AddEntryToTable_key: Property = Property(name="key", type=StringType)
iot2_Field_AddEntryToTable.attributes={iot2_Field_AddEntryToTable_key}

# iot2_Field_AppendEntryToTable class attributes and methods

# iot2_LastStatement_ReturnWithValue class attributes and methods

# LastStatement_Return class attributes and methods

# iot2_Statement_Assignment class attributes and methods

# iot2_Statement_Local_Variable_Declaration class attributes and methods
iot2_Statement_Local_Variable_Declaration_variableNames: Property = Property(name="variableNames", type=StringType)
iot2_Statement_Local_Variable_Declaration.attributes={iot2_Statement_Local_Variable_Declaration_variableNames}

# iot2_Statement_FunctioncallOrAssignment class attributes and methods

# Statement_FunctioncallOrAssignment class attributes and methods

# iot2_Expression_Nil class attributes and methods

# Expression class attributes and methods

# iot2_Expression_True class attributes and methods

# iot2_Expression_False class attributes and methods

# iot2_Expression_Number class attributes and methods
iot2_Expression_Number_value: Property = Property(name="value", type=FloatType)
iot2_Expression_Number.attributes={iot2_Expression_Number_value}

# iot2_Expression_VarArgs class attributes and methods

# iot2_Expression_String class attributes and methods
iot2_Expression_String_value: Property = Property(name="value", type=StringType)
iot2_Expression_String.attributes={iot2_Expression_String_value}

# iot2_Expression_Function class attributes and methods

# iot2_Expression_Or class attributes and methods

# iot2_Expression_And class attributes and methods

# iot2_Expression_Larger class attributes and methods

# iot2_Expression_Larger_Equal class attributes and methods

# iot2_Statement_CallMemberFunction class attributes and methods
iot2_Statement_CallMemberFunction_memberFunctionName: Property = Property(name="memberFunctionName", type=StringType)
iot2_Statement_CallMemberFunction.attributes={iot2_Statement_CallMemberFunction_memberFunctionName}

# iot2_Statement_CallFunction class attributes and methods

# iot2_Expression_Concatenation class attributes and methods

# iot2_Expression_Plus class attributes and methods

# iot2_Expression_Minus class attributes and methods

# iot2_Expression_Smaller class attributes and methods

# iot2_Expression_Multiplication class attributes and methods

# iot2_Expression_Smaller_Equal class attributes and methods

# iot2_Expression_Equal class attributes and methods

# iot2_Expression_Not_Equal class attributes and methods

# iot2_Expression_Negate class attributes and methods

# iot2_Expression_Length class attributes and methods

# iot2_Expression_Invert class attributes and methods

# iot2_Expression_Exponentiation class attributes and methods

# iot2_Expression_Division class attributes and methods

# iot2_Expression_Modulo class attributes and methods

# iot2_Expression_AccessMember class attributes and methods
iot2_Expression_AccessMember_memberName: Property = Property(name="memberName", type=StringType)
iot2_Expression_AccessMember.attributes={iot2_Expression_AccessMember_memberName}

# iot2_Expression_VariableName class attributes and methods
iot2_Expression_VariableName_variable: Property = Property(name="variable", type=StringType)
iot2_Expression_VariableName.attributes={iot2_Expression_VariableName_variable}

# iot2_Expression_CallMemberFunction class attributes and methods
iot2_Expression_CallMemberFunction_memberFunctionName: Property = Property(name="memberFunctionName", type=StringType)
iot2_Expression_CallMemberFunction.attributes={iot2_Expression_CallMemberFunction_memberFunctionName}

# iot2_Expression_CallFunction class attributes and methods

# iot2_Expression_AccessArray class attributes and methods

# iot2_InitialNode class attributes and methods

# ControlNode class attributes and methods

# iot2_FinalNode class attributes and methods

# iot2_ActivityFinalNode class attributes and methods

# FinalNode class attributes and methods

# iot2_ForkNode class attributes and methods

# iot2_JoinNode class attributes and methods

# iot2_MergeNode class attributes and methods

# iot2_DecisionNode class attributes and methods

# iot2_Value class attributes and methods

# iot2_IntegerVariable class attributes and methods

# Variable class attributes and methods

# iot2_BooleanValue class attributes and methods
iot2_BooleanValue_value: Property = Property(name="value", type=BooleanType)
iot2_BooleanValue.attributes={iot2_BooleanValue_value}

# Value class attributes and methods

# iot2_IntegerValue class attributes and methods
iot2_IntegerValue_value: Property = Property(name="value", type=IntegerType)
iot2_IntegerValue.attributes={iot2_IntegerValue_value}

# iot2_IntegerExpression class attributes and methods

# iot2_ControlFlow class attributes and methods

# ActivityEdge class attributes and methods

# iot2_BooleanVariable class attributes and methods

# iot2_ControlNode class attributes and methods

# ActivityNode class attributes and methods

# iot2_ExecutableNode class attributes and methods

# iot2_Action class attributes and methods

# ExecutableNode class attributes and methods

# iot2_OpaqueAction class attributes and methods

# Action class attributes and methods

# iot2_BooleanUnaryExpression class attributes and methods
iot2_BooleanUnaryExpression_operator: Property = Property(name="operator", type=StringType)
iot2_BooleanUnaryExpression.attributes={iot2_BooleanUnaryExpression_operator}

# BooleanExpression class attributes and methods

# iot2_BooleanBinaryExpression class attributes and methods
iot2_BooleanBinaryExpression_operator: Property = Property(name="operator", type=StringType)
iot2_BooleanBinaryExpression.attributes={iot2_BooleanBinaryExpression_operator}

# iot2_InputValue class attributes and methods

# iot2_Input class attributes and methods

# iot2_Token class attributes and methods

# iot2_BooleanExpression class attributes and methods

# iot2_IntegerCalculationExpression class attributes and methods
iot2_IntegerCalculationExpression_operator: Property = Property(name="operator", type=StringType)
iot2_IntegerCalculationExpression.attributes={iot2_IntegerCalculationExpression_operator}

# IntegerExpression class attributes and methods

# iot2_IntegerComparisonExpression class attributes and methods
iot2_IntegerComparisonExpression_operator: Property = Property(name="operator", type=StringType)
iot2_IntegerComparisonExpression.attributes={iot2_IntegerComparisonExpression_operator}

# iot2_Trace class attributes and methods

# Relationships
components0: BinaryAssociation = BinaryAssociation(
    name="components0",
    ends={
        Property(name="iot2_HWComponent", type=iot2_System, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_System", type=iot2_HWComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
boards1: BinaryAssociation = BinaryAssociation(
    name="boards1",
    ends={
        Property(name="iot2_Board", type=iot2_System, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_System2", type=iot2_Board, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sketch3: BinaryAssociation = BinaryAssociation(
    name="sketch3",
    ends={
        Property(name="iot2_Sketch", type=iot2_System, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_System4", type=iot2_Sketch, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
components5: BinaryAssociation = BinaryAssociation(
    name="components5",
    ends={
        Property(name="iot2_HWComponent7", type=iot2_Board, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Board6", type=iot2_HWComponent, multiplicity=Multiplicity(0, 9999))
    }
)
activity8: BinaryAssociation = BinaryAssociation(
    name="activity8",
    ends={
        Property(name="iot2_Activity", type=iot2_Sketch, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Sketch9", type=iot2_Activity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
services10: BinaryAssociation = BinaryAssociation(
    name="services10",
    ends={
        Property(name="iot2_OperationDef", type=iot2_HWComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_HWComponent11", type=iot2_OperationDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
canRaise22: BinaryAssociation = BinaryAssociation(
    name="canRaise22",
    ends={
        Property(name="iot2_ExceptionDef", type=iot2_OperationDef, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_OperationDef23", type=iot2_ExceptionDef, multiplicity=Multiplicity(0, 9999))
    }
)
lua24: BinaryAssociation = BinaryAssociation(
    name="lua24",
    ends={
        Property(name="iot2_Block", type=iot2_OperationDef, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_OperationDef25", type=iot2_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definedIn26: BinaryAssociation = BinaryAssociation(
    name="definedIn26",
    ends={
        Property(name="Container", type=iot2_Contained, multiplicity=Multiplicity(1, 1)),
        Property(name="contains", type=iot2_Container, multiplicity=Multiplicity(0, 1))
    }
)
contains27: BinaryAssociation = BinaryAssociation(
    name="contains27",
    ends={
        Property(name="Contained", type=iot2_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="definedIn", type=iot2_Contained, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containedType28: BinaryAssociation = BinaryAssociation(
    name="containedType28",
    ends={
        Property(name="iot2_IDLType", type=iot2_Typed, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Typed", type=iot2_IDLType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sharedType29: BinaryAssociation = BinaryAssociation(
    name="sharedType29",
    ends={
        Property(name="iot2_TypedefDef", type=iot2_Typed, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Typed30", type=iot2_TypedefDef, multiplicity=Multiplicity(0, 1))
    }
)
nodes12: BinaryAssociation = BinaryAssociation(
    name="nodes12",
    ends={
        Property(name="ActivityNode", type=iot2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activity", type=iot2_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges13: BinaryAssociation = BinaryAssociation(
    name="edges13",
    ends={
        Property(name="iot2_ActivityEdge", type=iot2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Activity14", type=iot2_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locals15: BinaryAssociation = BinaryAssociation(
    name="locals15",
    ends={
        Property(name="iot2_Variable", type=iot2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Activity16", type=iot2_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputs17: BinaryAssociation = BinaryAssociation(
    name="inputs17",
    ends={
        Property(name="iot2_Variable19", type=iot2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Activity18", type=iot2_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters20: BinaryAssociation = BinaryAssociation(
    name="parameters20",
    ends={
        Property(name="iot2_ParameterDef", type=iot2_OperationDef, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_OperationDef21", type=iot2_ParameterDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements35: BinaryAssociation = BinaryAssociation(
    name="statements35",
    ends={
        Property(name="iot2_Statement", type=iot2_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Block36", type=iot2_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnValue37: BinaryAssociation = BinaryAssociation(
    name="returnValue37",
    ends={
        Property(name="iot2_LastStatement", type=iot2_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Block38", type=iot2_LastStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block39: BinaryAssociation = BinaryAssociation(
    name="block39",
    ends={
        Property(name="iot2_Block40", type=iot2_Statement_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_Block", type=iot2_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
members31: BinaryAssociation = BinaryAssociation(
    name="members31",
    ends={
        Property(name="iot2_Field", type=iot2_ExceptionDef, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_ExceptionDef32", type=iot2_Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value33: BinaryAssociation = BinaryAssociation(
    name="value33",
    ends={
        Property(name="iot2_Expression", type=iot2_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Field34", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseifBlock64: BinaryAssociation = BinaryAssociation(
    name="elseifBlock64",
    ends={
        Property(name="iot2_Block66", type=iot2_Statement_If_Then_Else_ElseIfPart, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_If_Then_Else_ElseIfPart65", type=iot2_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
startExpr67: BinaryAssociation = BinaryAssociation(
    name="startExpr67",
    ends={
        Property(name="iot2_Expression68", type=iot2_Statement_For_Numeric, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_For_Numeric", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
untilExpr69: BinaryAssociation = BinaryAssociation(
    name="untilExpr69",
    ends={
        Property(name="iot2_Expression71", type=iot2_Statement_For_Numeric, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_For_Numeric70", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stepExpr72: BinaryAssociation = BinaryAssociation(
    name="stepExpr72",
    ends={
        Property(name="iot2_Expression74", type=iot2_Statement_For_Numeric, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_For_Numeric73", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block75: BinaryAssociation = BinaryAssociation(
    name="block75",
    ends={
        Property(name="iot2_Block77", type=iot2_Statement_For_Numeric, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_For_Numeric76", type=iot2_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions78: BinaryAssociation = BinaryAssociation(
    name="expressions78",
    ends={
        Property(name="iot2_Expression79", type=iot2_Statement_For_Generic, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_For_Generic", type=iot2_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block80: BinaryAssociation = BinaryAssociation(
    name="block80",
    ends={
        Property(name="iot2_Block82", type=iot2_Statement_For_Generic, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_For_Generic81", type=iot2_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function83: BinaryAssociation = BinaryAssociation(
    name="function83",
    ends={
        Property(name="iot2_Function", type=iot2_Statement_GlobalFunction_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_GlobalFunction_Declaration", type=iot2_Function, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression41: BinaryAssociation = BinaryAssociation(
    name="expression41",
    ends={
        Property(name="iot2_Expression42", type=iot2_Statement_While, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_While", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block43: BinaryAssociation = BinaryAssociation(
    name="block43",
    ends={
        Property(name="iot2_Block45", type=iot2_Statement_While, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_While44", type=iot2_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block46: BinaryAssociation = BinaryAssociation(
    name="block46",
    ends={
        Property(name="iot2_Block47", type=iot2_Statement_Repeat, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_Repeat", type=iot2_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression48: BinaryAssociation = BinaryAssociation(
    name="expression48",
    ends={
        Property(name="iot2_Expression50", type=iot2_Statement_Repeat, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_Repeat49", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifExpression51: BinaryAssociation = BinaryAssociation(
    name="ifExpression51",
    ends={
        Property(name="iot2_Expression52", type=iot2_Statement_If_Then_Else, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_If_Then_Else", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifBlock53: BinaryAssociation = BinaryAssociation(
    name="ifBlock53",
    ends={
        Property(name="iot2_Block55", type=iot2_Statement_If_Then_Else, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_If_Then_Else54", type=iot2_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseIf56: BinaryAssociation = BinaryAssociation(
    name="elseIf56",
    ends={
        Property(name="iot2_Statement_If_Then_Else_ElseIfPart", type=iot2_Statement_If_Then_Else, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_If_Then_Else57", type=iot2_Statement_If_Then_Else_ElseIfPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseBlock58: BinaryAssociation = BinaryAssociation(
    name="elseBlock58",
    ends={
        Property(name="iot2_Block60", type=iot2_Statement_If_Then_Else, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_If_Then_Else59", type=iot2_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseifExpression61: BinaryAssociation = BinaryAssociation(
    name="elseifExpression61",
    ends={
        Property(name="iot2_Expression63", type=iot2_Statement_If_Then_Else_ElseIfPart, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_If_Then_Else_ElseIfPart62", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function88: BinaryAssociation = BinaryAssociation(
    name="function88",
    ends={
        Property(name="iot2_Expression_Function", type=iot2_Function, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="iot2_Function89", type=iot2_Expression_Function, multiplicity=Multiplicity(1, 1))
    }
)
fields90: BinaryAssociation = BinaryAssociation(
    name="fields90",
    ends={
        Property(name="iot2_Field91", type=iot2_Expression_TableConstructor, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_TableConstructor", type=iot2_Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body92: BinaryAssociation = BinaryAssociation(
    name="body92",
    ends={
        Property(name="iot2_Block94", type=iot2_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Function93", type=iot2_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments95: BinaryAssociation = BinaryAssociation(
    name="arguments95",
    ends={
        Property(name="iot2_Expression96", type=iot2_Functioncall_Arguments, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Functioncall_Arguments", type=iot2_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
indexExpression97: BinaryAssociation = BinaryAssociation(
    name="indexExpression97",
    ends={
        Property(name="iot2_Expression98", type=iot2_Field_AddEntryToTable_Brackets, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Field_AddEntryToTable_Brackets", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnValues99: BinaryAssociation = BinaryAssociation(
    name="returnValues99",
    ends={
        Property(name="iot2_Expression100", type=iot2_LastStatement_ReturnWithValue, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_LastStatement_ReturnWithValue", type=iot2_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable101: BinaryAssociation = BinaryAssociation(
    name="variable101",
    ends={
        Property(name="iot2_Expression102", type=iot2_Statement_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_Assignment", type=iot2_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values103: BinaryAssociation = BinaryAssociation(
    name="values103",
    ends={
        Property(name="iot2_Expression105", type=iot2_Statement_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_Assignment104", type=iot2_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
function84: BinaryAssociation = BinaryAssociation(
    name="function84",
    ends={
        Property(name="iot2_Function85", type=iot2_Statement_LocalFunction_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_LocalFunction_Declaration", type=iot2_Function, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initialValue86: BinaryAssociation = BinaryAssociation(
    name="initialValue86",
    ends={
        Property(name="iot2_Expression87", type=iot2_Statement_Local_Variable_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_Local_Variable_Declaration", type=iot2_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left116: BinaryAssociation = BinaryAssociation(
    name="left116",
    ends={
        Property(name="iot2_Expression117", type=iot2_Expression_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Or", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right118: BinaryAssociation = BinaryAssociation(
    name="right118",
    ends={
        Property(name="iot2_Expression120", type=iot2_Expression_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Or119", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left121: BinaryAssociation = BinaryAssociation(
    name="left121",
    ends={
        Property(name="iot2_Expression122", type=iot2_Expression_And, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_And", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right123: BinaryAssociation = BinaryAssociation(
    name="right123",
    ends={
        Property(name="iot2_Expression125", type=iot2_Expression_And, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_And124", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left126: BinaryAssociation = BinaryAssociation(
    name="left126",
    ends={
        Property(name="iot2_Expression127", type=iot2_Expression_Larger, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Larger", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right128: BinaryAssociation = BinaryAssociation(
    name="right128",
    ends={
        Property(name="iot2_Expression130", type=iot2_Expression_Larger, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Larger129", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left131: BinaryAssociation = BinaryAssociation(
    name="left131",
    ends={
        Property(name="iot2_Expression132", type=iot2_Expression_Larger_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Larger_Equal", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right133: BinaryAssociation = BinaryAssociation(
    name="right133",
    ends={
        Property(name="iot2_Expression135", type=iot2_Expression_Larger_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Larger_Equal134", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object106: BinaryAssociation = BinaryAssociation(
    name="object106",
    ends={
        Property(name="iot2_Expression107", type=iot2_Statement_CallMemberFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_CallMemberFunction", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments108: BinaryAssociation = BinaryAssociation(
    name="arguments108",
    ends={
        Property(name="iot2_Functioncall_Arguments110", type=iot2_Statement_CallMemberFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_CallMemberFunction109", type=iot2_Functioncall_Arguments, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object111: BinaryAssociation = BinaryAssociation(
    name="object111",
    ends={
        Property(name="iot2_Expression112", type=iot2_Statement_CallFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_CallFunction", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left151: BinaryAssociation = BinaryAssociation(
    name="left151",
    ends={
        Property(name="iot2_Expression152", type=iot2_Expression_Not_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Not_Equal", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments113: BinaryAssociation = BinaryAssociation(
    name="arguments113",
    ends={
        Property(name="iot2_Functioncall_Arguments115", type=iot2_Statement_CallFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_CallFunction114", type=iot2_Functioncall_Arguments, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right153: BinaryAssociation = BinaryAssociation(
    name="right153",
    ends={
        Property(name="iot2_Expression155", type=iot2_Expression_Not_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Not_Equal154", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left156: BinaryAssociation = BinaryAssociation(
    name="left156",
    ends={
        Property(name="iot2_Expression157", type=iot2_Expression_Concatenation, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Concatenation", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right158: BinaryAssociation = BinaryAssociation(
    name="right158",
    ends={
        Property(name="iot2_Expression160", type=iot2_Expression_Concatenation, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Concatenation159", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left161: BinaryAssociation = BinaryAssociation(
    name="left161",
    ends={
        Property(name="iot2_Expression162", type=iot2_Expression_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Plus", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right163: BinaryAssociation = BinaryAssociation(
    name="right163",
    ends={
        Property(name="iot2_Expression165", type=iot2_Expression_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Plus164", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left166: BinaryAssociation = BinaryAssociation(
    name="left166",
    ends={
        Property(name="iot2_Expression167", type=iot2_Expression_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Minus", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right168: BinaryAssociation = BinaryAssociation(
    name="right168",
    ends={
        Property(name="iot2_Expression170", type=iot2_Expression_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Minus169", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left136: BinaryAssociation = BinaryAssociation(
    name="left136",
    ends={
        Property(name="iot2_Expression137", type=iot2_Expression_Smaller, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Smaller", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right138: BinaryAssociation = BinaryAssociation(
    name="right138",
    ends={
        Property(name="iot2_Expression140", type=iot2_Expression_Smaller, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Smaller139", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left141: BinaryAssociation = BinaryAssociation(
    name="left141",
    ends={
        Property(name="iot2_Expression142", type=iot2_Expression_Smaller_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Smaller_Equal", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right143: BinaryAssociation = BinaryAssociation(
    name="right143",
    ends={
        Property(name="iot2_Expression145", type=iot2_Expression_Smaller_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Smaller_Equal144", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left146: BinaryAssociation = BinaryAssociation(
    name="left146",
    ends={
        Property(name="iot2_Expression147", type=iot2_Expression_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Equal", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right148: BinaryAssociation = BinaryAssociation(
    name="right148",
    ends={
        Property(name="iot2_Expression150", type=iot2_Expression_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Equal149", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp186: BinaryAssociation = BinaryAssociation(
    name="exp186",
    ends={
        Property(name="iot2_Expression187", type=iot2_Expression_Negate, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Negate", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp188: BinaryAssociation = BinaryAssociation(
    name="exp188",
    ends={
        Property(name="iot2_Expression189", type=iot2_Expression_Length, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Length", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp190: BinaryAssociation = BinaryAssociation(
    name="exp190",
    ends={
        Property(name="iot2_Expression191", type=iot2_Expression_Invert, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Invert", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left192: BinaryAssociation = BinaryAssociation(
    name="left192",
    ends={
        Property(name="iot2_Expression193", type=iot2_Expression_Exponentiation, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Exponentiation", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right194: BinaryAssociation = BinaryAssociation(
    name="right194",
    ends={
        Property(name="iot2_Expression196", type=iot2_Expression_Exponentiation, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Exponentiation195", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left171: BinaryAssociation = BinaryAssociation(
    name="left171",
    ends={
        Property(name="iot2_Expression172", type=iot2_Expression_Multiplication, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Multiplication", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right173: BinaryAssociation = BinaryAssociation(
    name="right173",
    ends={
        Property(name="iot2_Expression175", type=iot2_Expression_Multiplication, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Multiplication174", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left176: BinaryAssociation = BinaryAssociation(
    name="left176",
    ends={
        Property(name="iot2_Expression177", type=iot2_Expression_Division, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Division", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right178: BinaryAssociation = BinaryAssociation(
    name="right178",
    ends={
        Property(name="iot2_Expression180", type=iot2_Expression_Division, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Division179", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left181: BinaryAssociation = BinaryAssociation(
    name="left181",
    ends={
        Property(name="iot2_Expression182", type=iot2_Expression_Modulo, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Modulo", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
index209: BinaryAssociation = BinaryAssociation(
    name="index209",
    ends={
        Property(name="iot2_Expression211", type=iot2_Expression_AccessArray, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_AccessArray210", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right183: BinaryAssociation = BinaryAssociation(
    name="right183",
    ends={
        Property(name="iot2_Expression185", type=iot2_Expression_Modulo, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Modulo184", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object212: BinaryAssociation = BinaryAssociation(
    name="object212",
    ends={
        Property(name="iot2_Expression213", type=iot2_Expression_AccessMember, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_AccessMember", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outgoing214: BinaryAssociation = BinaryAssociation(
    name="outgoing214",
    ends={
        Property(name="ActivityEdge", type=iot2_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=iot2_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
incoming215: BinaryAssociation = BinaryAssociation(
    name="incoming215",
    ends={
        Property(name="ActivityEdge216", type=iot2_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=iot2_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
activity217: BinaryAssociation = BinaryAssociation(
    name="activity217",
    ends={
        Property(name="Activity", type=iot2_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=iot2_Activity, multiplicity=Multiplicity(1, 1))
    }
)
object197: BinaryAssociation = BinaryAssociation(
    name="object197",
    ends={
        Property(name="iot2_Expression198", type=iot2_Expression_CallMemberFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_CallMemberFunction", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments199: BinaryAssociation = BinaryAssociation(
    name="arguments199",
    ends={
        Property(name="iot2_Functioncall_Arguments201", type=iot2_Expression_CallMemberFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_CallMemberFunction200", type=iot2_Functioncall_Arguments, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object202: BinaryAssociation = BinaryAssociation(
    name="object202",
    ends={
        Property(name="iot2_Expression203", type=iot2_Expression_CallFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_CallFunction", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments204: BinaryAssociation = BinaryAssociation(
    name="arguments204",
    ends={
        Property(name="iot2_Functioncall_Arguments206", type=iot2_Expression_CallFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_CallFunction205", type=iot2_Functioncall_Arguments, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
array207: BinaryAssociation = BinaryAssociation(
    name="array207",
    ends={
        Property(name="iot2_Expression208", type=iot2_Expression_AccessArray, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_AccessArray", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initialValue228: BinaryAssociation = BinaryAssociation(
    name="initialValue228",
    ends={
        Property(name="iot2_Value", type=iot2_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Variable229", type=iot2_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
currentValue230: BinaryAssociation = BinaryAssociation(
    name="currentValue230",
    ends={
        Property(name="iot2_Value232", type=iot2_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Variable231", type=iot2_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand2233: BinaryAssociation = BinaryAssociation(
    name="operand2233",
    ends={
        Property(name="iot2_IntegerVariable", type=iot2_IntegerExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_IntegerExpression", type=iot2_IntegerVariable, multiplicity=Multiplicity(0, 1))
    }
)
source218: BinaryAssociation = BinaryAssociation(
    name="source218",
    ends={
        Property(name="ActivityNode219", type=iot2_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=iot2_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
target220: BinaryAssociation = BinaryAssociation(
    name="target220",
    ends={
        Property(name="ActivityNode221", type=iot2_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=iot2_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
guard222: BinaryAssociation = BinaryAssociation(
    name="guard222",
    ends={
        Property(name="iot2_BooleanVariable", type=iot2_ControlFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_ControlFlow", type=iot2_BooleanVariable, multiplicity=Multiplicity(0, 1))
    }
)
expressions223: BinaryAssociation = BinaryAssociation(
    name="expressions223",
    ends={
        Property(name="iot2_Expression224", type=iot2_OpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_OpaqueAction", type=iot2_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
service225: BinaryAssociation = BinaryAssociation(
    name="service225",
    ends={
        Property(name="iot2_OperationDef227", type=iot2_OpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_OpaqueAction226", type=iot2_OperationDef, multiplicity=Multiplicity(0, 1))
    }
)
operand243: BinaryAssociation = BinaryAssociation(
    name="operand243",
    ends={
        Property(name="iot2_BooleanVariable244", type=iot2_BooleanUnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_BooleanUnaryExpression", type=iot2_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
operand1245: BinaryAssociation = BinaryAssociation(
    name="operand1245",
    ends={
        Property(name="iot2_BooleanVariable246", type=iot2_BooleanBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_BooleanBinaryExpression", type=iot2_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
operand2247: BinaryAssociation = BinaryAssociation(
    name="operand2247",
    ends={
        Property(name="iot2_BooleanVariable249", type=iot2_BooleanBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_BooleanBinaryExpression248", type=iot2_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
value250: BinaryAssociation = BinaryAssociation(
    name="value250",
    ends={
        Property(name="iot2_Value251", type=iot2_InputValue, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_InputValue", type=iot2_Value, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable252: BinaryAssociation = BinaryAssociation(
    name="variable252",
    ends={
        Property(name="iot2_Variable254", type=iot2_InputValue, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_InputValue253", type=iot2_Variable, multiplicity=Multiplicity(1, 1))
    }
)
inputValues255: BinaryAssociation = BinaryAssociation(
    name="inputValues255",
    ends={
        Property(name="iot2_InputValue256", type=iot2_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Input", type=iot2_InputValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operand1234: BinaryAssociation = BinaryAssociation(
    name="operand1234",
    ends={
        Property(name="iot2_IntegerVariable236", type=iot2_IntegerExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_IntegerExpression235", type=iot2_IntegerVariable, multiplicity=Multiplicity(0, 1))
    }
)
assignee237: BinaryAssociation = BinaryAssociation(
    name="assignee237",
    ends={
        Property(name="iot2_BooleanVariable238", type=iot2_BooleanExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_BooleanExpression", type=iot2_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
assignee239: BinaryAssociation = BinaryAssociation(
    name="assignee239",
    ends={
        Property(name="iot2_IntegerVariable240", type=iot2_IntegerCalculationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_IntegerCalculationExpression", type=iot2_IntegerVariable, multiplicity=Multiplicity(1, 1))
    }
)
assignee241: BinaryAssociation = BinaryAssociation(
    name="assignee241",
    ends={
        Property(name="iot2_BooleanVariable242", type=iot2_IntegerComparisonExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_IntegerComparisonExpression", type=iot2_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
holder257: BinaryAssociation = BinaryAssociation(
    name="holder257",
    ends={
        Property(name="iot2_ActivityNode", type=iot2_Token, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Token", type=iot2_ActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
executedNodes258: BinaryAssociation = BinaryAssociation(
    name="executedNodes258",
    ends={
        Property(name="iot2_ActivityNode259", type=iot2_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Trace", type=iot2_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_iot2_Sensor_HWComponent = Generalization(general=HWComponent, specific=iot2_Sensor)
gen_iot2_Contained_NamedElement = Generalization(general=NamedElement, specific=iot2_Contained)
gen_iot2_Container_Contained = Generalization(general=Contained, specific=iot2_Container)
gen_iot2_Actuator_HWComponent = Generalization(general=HWComponent, specific=iot2_Actuator)
gen_iot2_Activity_NamedElement = Generalization(general=NamedElement, specific=iot2_Activity)
gen_iot2_OperationDef_Contained = Generalization(general=Contained, specific=iot2_OperationDef)
gen_iot2_OperationDef_Typed = Generalization(general=Typed, specific=iot2_OperationDef)
gen_iot2_PrimitiveDef_IDLType = Generalization(general=IDLType, specific=iot2_PrimitiveDef)
gen_iot2_Block_Chunk = Generalization(general=Chunk, specific=iot2_Block)
gen_iot2_LastStatement_Return_LastStatement = Generalization(general=LastStatement, specific=iot2_LastStatement_Return)
gen_iot2_LastStatement_Break_LastStatement = Generalization(general=LastStatement, specific=iot2_LastStatement_Break)
gen_iot2_Statement_Block_Statement = Generalization(general=Statement, specific=iot2_Statement_Block)
gen_iot2_TypedefDef_IDLType = Generalization(general=IDLType, specific=iot2_TypedefDef)
gen_iot2_TypedefDef_Contained = Generalization(general=Contained, specific=iot2_TypedefDef)
gen_iot2_ParameterDef_Typed = Generalization(general=Typed, specific=iot2_ParameterDef)
gen_iot2_ExceptionDef_Contained = Generalization(general=Contained, specific=iot2_ExceptionDef)
gen_iot2_Field_Typed = Generalization(general=Typed, specific=iot2_Field)
gen_iot2_Statement_For_Numeric_Statement = Generalization(general=Statement, specific=iot2_Statement_For_Numeric)
gen_iot2_Statement_For_Generic_Statement = Generalization(general=Statement, specific=iot2_Statement_For_Generic)
gen_iot2_Statement_GlobalFunction_Declaration_Statement = Generalization(general=Statement, specific=iot2_Statement_GlobalFunction_Declaration)
gen_iot2_Statement_LocalFunction_Declaration_Statement = Generalization(general=Statement, specific=iot2_Statement_LocalFunction_Declaration)
gen_iot2_Statement_While_Statement = Generalization(general=Statement, specific=iot2_Statement_While)
gen_iot2_Statement_Repeat_Statement = Generalization(general=Statement, specific=iot2_Statement_Repeat)
gen_iot2_Statement_If_Then_Else_Statement = Generalization(general=Statement, specific=iot2_Statement_If_Then_Else)
gen_iot2_Expression_TableConstructor_Expression = Generalization(general=Expression, specific=iot2_Expression_TableConstructor)
gen_iot2_Field_AddEntryToTable_Brackets_Field = Generalization(general=Field, specific=iot2_Field_AddEntryToTable_Brackets)
gen_iot2_Field_AddEntryToTable_Field = Generalization(general=Field, specific=iot2_Field_AddEntryToTable)
gen_iot2_Field_AppendEntryToTable_Field = Generalization(general=Field, specific=iot2_Field_AppendEntryToTable)
gen_iot2_LastStatement_ReturnWithValue_LastStatement_Return = Generalization(general=LastStatement_Return, specific=iot2_LastStatement_ReturnWithValue)
gen_iot2_Statement_Assignment_Statement_FunctioncallOrAssignment = Generalization(general=Statement_FunctioncallOrAssignment, specific=iot2_Statement_Assignment)
gen_iot2_Statement_Local_Variable_Declaration_Statement = Generalization(general=Statement, specific=iot2_Statement_Local_Variable_Declaration)
gen_iot2_Statement_FunctioncallOrAssignment_Statement = Generalization(general=Statement, specific=iot2_Statement_FunctioncallOrAssignment)
gen_iot2_Expression_Statement_FunctioncallOrAssignment = Generalization(general=Statement_FunctioncallOrAssignment, specific=iot2_Expression)
gen_iot2_Expression_Nil_Expression = Generalization(general=Expression, specific=iot2_Expression_Nil)
gen_iot2_Expression_True_Expression = Generalization(general=Expression, specific=iot2_Expression_True)
gen_iot2_Expression_False_Expression = Generalization(general=Expression, specific=iot2_Expression_False)
gen_iot2_Expression_Number_Expression = Generalization(general=Expression, specific=iot2_Expression_Number)
gen_iot2_Expression_VarArgs_Expression = Generalization(general=Expression, specific=iot2_Expression_VarArgs)
gen_iot2_Expression_String_Expression = Generalization(general=Expression, specific=iot2_Expression_String)
gen_iot2_Expression_Function_Expression = Generalization(general=Expression, specific=iot2_Expression_Function)
gen_iot2_Expression_Or_Expression = Generalization(general=Expression, specific=iot2_Expression_Or)
gen_iot2_Expression_And_Expression = Generalization(general=Expression, specific=iot2_Expression_And)
gen_iot2_Expression_Larger_Expression = Generalization(general=Expression, specific=iot2_Expression_Larger)
gen_iot2_Expression_Larger_Equal_Expression = Generalization(general=Expression, specific=iot2_Expression_Larger_Equal)
gen_iot2_Statement_CallMemberFunction_Statement_FunctioncallOrAssignment = Generalization(general=Statement_FunctioncallOrAssignment, specific=iot2_Statement_CallMemberFunction)
gen_iot2_Statement_CallFunction_Statement_FunctioncallOrAssignment = Generalization(general=Statement_FunctioncallOrAssignment, specific=iot2_Statement_CallFunction)
gen_iot2_Expression_Concatenation_Expression = Generalization(general=Expression, specific=iot2_Expression_Concatenation)
gen_iot2_Expression_Plus_Expression = Generalization(general=Expression, specific=iot2_Expression_Plus)
gen_iot2_Expression_Minus_Expression = Generalization(general=Expression, specific=iot2_Expression_Minus)
gen_iot2_Expression_Smaller_Expression = Generalization(general=Expression, specific=iot2_Expression_Smaller)
gen_iot2_Expression_Multiplication_Expression = Generalization(general=Expression, specific=iot2_Expression_Multiplication)
gen_iot2_Expression_Smaller_Equal_Expression = Generalization(general=Expression, specific=iot2_Expression_Smaller_Equal)
gen_iot2_Expression_Equal_Expression = Generalization(general=Expression, specific=iot2_Expression_Equal)
gen_iot2_Expression_Not_Equal_Expression = Generalization(general=Expression, specific=iot2_Expression_Not_Equal)
gen_iot2_Expression_Negate_Expression = Generalization(general=Expression, specific=iot2_Expression_Negate)
gen_iot2_Expression_Length_Expression = Generalization(general=Expression, specific=iot2_Expression_Length)
gen_iot2_Expression_Invert_Expression = Generalization(general=Expression, specific=iot2_Expression_Invert)
gen_iot2_Expression_Exponentiation_Expression = Generalization(general=Expression, specific=iot2_Expression_Exponentiation)
gen_iot2_Expression_Division_Expression = Generalization(general=Expression, specific=iot2_Expression_Division)
gen_iot2_Expression_Modulo_Expression = Generalization(general=Expression, specific=iot2_Expression_Modulo)
gen_iot2_Expression_AccessMember_Expression = Generalization(general=Expression, specific=iot2_Expression_AccessMember)
gen_iot2_Expression_VariableName_Expression = Generalization(general=Expression, specific=iot2_Expression_VariableName)
gen_iot2_ActivityNode_NamedElement = Generalization(general=NamedElement, specific=iot2_ActivityNode)
gen_iot2_Expression_CallMemberFunction_Expression = Generalization(general=Expression, specific=iot2_Expression_CallMemberFunction)
gen_iot2_ActivityEdge_NamedElement = Generalization(general=NamedElement, specific=iot2_ActivityEdge)
gen_iot2_Expression_CallFunction_Expression = Generalization(general=Expression, specific=iot2_Expression_CallFunction)
gen_iot2_Expression_AccessArray_Expression = Generalization(general=Expression, specific=iot2_Expression_AccessArray)
gen_iot2_InitialNode_ControlNode = Generalization(general=ControlNode, specific=iot2_InitialNode)
gen_iot2_FinalNode_ControlNode = Generalization(general=ControlNode, specific=iot2_FinalNode)
gen_iot2_ActivityFinalNode_FinalNode = Generalization(general=FinalNode, specific=iot2_ActivityFinalNode)
gen_iot2_ForkNode_ControlNode = Generalization(general=ControlNode, specific=iot2_ForkNode)
gen_iot2_JoinNode_ControlNode = Generalization(general=ControlNode, specific=iot2_JoinNode)
gen_iot2_MergeNode_ControlNode = Generalization(general=ControlNode, specific=iot2_MergeNode)
gen_iot2_DecisionNode_ControlNode = Generalization(general=ControlNode, specific=iot2_DecisionNode)
gen_iot2_IntegerVariable_Variable = Generalization(general=Variable, specific=iot2_IntegerVariable)
gen_iot2_BooleanVariable_Variable = Generalization(general=Variable, specific=iot2_BooleanVariable)
gen_iot2_BooleanValue_Value = Generalization(general=Value, specific=iot2_BooleanValue)
gen_iot2_IntegerValue_Value = Generalization(general=Value, specific=iot2_IntegerValue)
gen_iot2_IntegerExpression_Expression = Generalization(general=Expression, specific=iot2_IntegerExpression)
gen_iot2_ControlFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=iot2_ControlFlow)
gen_iot2_ControlNode_ActivityNode = Generalization(general=ActivityNode, specific=iot2_ControlNode)
gen_iot2_ExecutableNode_ActivityNode = Generalization(general=ActivityNode, specific=iot2_ExecutableNode)
gen_iot2_Action_ExecutableNode = Generalization(general=ExecutableNode, specific=iot2_Action)
gen_iot2_OpaqueAction_Action = Generalization(general=Action, specific=iot2_OpaqueAction)
gen_iot2_BooleanUnaryExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=iot2_BooleanUnaryExpression)
gen_iot2_BooleanBinaryExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=iot2_BooleanBinaryExpression)
gen_iot2_BooleanExpression_Expression = Generalization(general=Expression, specific=iot2_BooleanExpression)
gen_iot2_IntegerCalculationExpression_IntegerExpression = Generalization(general=IntegerExpression, specific=iot2_IntegerCalculationExpression)
gen_iot2_IntegerComparisonExpression_IntegerExpression = Generalization(general=IntegerExpression, specific=iot2_IntegerComparisonExpression)

# Domain Model
domain_model = DomainModel(
    name="iot2",
    types={iot2_System, iot2_HWComponent, iot2_Board, iot2_Sketch, iot2_Activity, iot2_OperationDef, iot2_Sensor, HWComponent, iot2_ExceptionDef, iot2_Block, iot2_Contained, iot2_Container, iot2_NamedElement, iot2_Typed, iot2_IDLType, iot2_TypedefDef, iot2_Actuator, NamedElement, iot2_ActivityNode, iot2_ActivityEdge, iot2_Variable, Contained, Typed, iot2_ParameterDef, iot2_PrimitiveDef, iot2_Chunk, Chunk, iot2_Statement, iot2_LastStatement, iot2_LastStatement_Return, LastStatement, iot2_LastStatement_Break, iot2_Statement_Block, Statement, IDLType, iot2_Field, iot2_Expression, iot2_Statement_For_Numeric, iot2_Statement_For_Generic, iot2_Statement_GlobalFunction_Declaration, iot2_Function, iot2_Statement_LocalFunction_Declaration, iot2_Statement_While, iot2_Statement_Repeat, iot2_Statement_If_Then_Else, iot2_Statement_If_Then_Else_ElseIfPart, iot2_Expression_TableConstructor, iot2_Functioncall_Arguments, iot2_Field_AddEntryToTable_Brackets, Field, iot2_Field_AddEntryToTable, iot2_Field_AppendEntryToTable, iot2_LastStatement_ReturnWithValue, LastStatement_Return, iot2_Statement_Assignment, iot2_Statement_Local_Variable_Declaration, iot2_Statement_FunctioncallOrAssignment, Statement_FunctioncallOrAssignment, iot2_Expression_Nil, Expression, iot2_Expression_True, iot2_Expression_False, iot2_Expression_Number, iot2_Expression_VarArgs, iot2_Expression_String, iot2_Expression_Function, iot2_Expression_Or, iot2_Expression_And, iot2_Expression_Larger, iot2_Expression_Larger_Equal, iot2_Statement_CallMemberFunction, iot2_Statement_CallFunction, iot2_Expression_Concatenation, iot2_Expression_Plus, iot2_Expression_Minus, iot2_Expression_Smaller, iot2_Expression_Multiplication, iot2_Expression_Smaller_Equal, iot2_Expression_Equal, iot2_Expression_Not_Equal, iot2_Expression_Negate, iot2_Expression_Length, iot2_Expression_Invert, iot2_Expression_Exponentiation, iot2_Expression_Division, iot2_Expression_Modulo, iot2_Expression_AccessMember, iot2_Expression_VariableName, iot2_Expression_CallMemberFunction, iot2_Expression_CallFunction, iot2_Expression_AccessArray, iot2_InitialNode, ControlNode, iot2_FinalNode, iot2_ActivityFinalNode, FinalNode, iot2_ForkNode, iot2_JoinNode, iot2_MergeNode, iot2_DecisionNode, iot2_Value, iot2_IntegerVariable, Variable, iot2_BooleanValue, Value, iot2_IntegerValue, iot2_IntegerExpression, iot2_ControlFlow, ActivityEdge, iot2_BooleanVariable, iot2_ControlNode, ActivityNode, iot2_ExecutableNode, iot2_Action, ExecutableNode, iot2_OpaqueAction, Action, iot2_BooleanUnaryExpression, BooleanExpression, iot2_BooleanBinaryExpression, iot2_InputValue, iot2_Input, iot2_Token, iot2_BooleanExpression, iot2_IntegerCalculationExpression, IntegerExpression, iot2_IntegerComparisonExpression, iot2_Trace, BoardType, PrimitiveKind, ParameterMode, BooleanUnaryOperator, BooleanBinaryOperator, IntegerCalculationOperator, IntegerComparisonOperator},
    associations={components0, boards1, sketch3, components5, activity8, services10, canRaise22, lua24, definedIn26, contains27, containedType28, sharedType29, nodes12, edges13, locals15, inputs17, parameters20, statements35, returnValue37, block39, members31, value33, elseifBlock64, startExpr67, untilExpr69, stepExpr72, block75, expressions78, block80, function83, expression41, block43, block46, expression48, ifExpression51, ifBlock53, elseIf56, elseBlock58, elseifExpression61, function88, fields90, body92, arguments95, indexExpression97, returnValues99, variable101, values103, function84, initialValue86, left116, right118, left121, right123, left126, right128, left131, right133, object106, arguments108, object111, left151, arguments113, right153, left156, right158, left161, right163, left166, right168, left136, right138, left141, right143, left146, right148, exp186, exp188, exp190, left192, right194, left171, right173, left176, right178, left181, index209, right183, object212, outgoing214, incoming215, activity217, object197, arguments199, object202, arguments204, array207, initialValue228, currentValue230, operand2233, source218, target220, guard222, expressions223, service225, operand243, operand1245, operand2247, value250, variable252, inputValues255, operand1234, assignee237, assignee239, assignee241, holder257, executedNodes258},
    generalizations={gen_iot2_Sensor_HWComponent, gen_iot2_Contained_NamedElement, gen_iot2_Container_Contained, gen_iot2_Actuator_HWComponent, gen_iot2_Activity_NamedElement, gen_iot2_OperationDef_Contained, gen_iot2_OperationDef_Typed, gen_iot2_PrimitiveDef_IDLType, gen_iot2_Block_Chunk, gen_iot2_LastStatement_Return_LastStatement, gen_iot2_LastStatement_Break_LastStatement, gen_iot2_Statement_Block_Statement, gen_iot2_TypedefDef_IDLType, gen_iot2_TypedefDef_Contained, gen_iot2_ParameterDef_Typed, gen_iot2_ExceptionDef_Contained, gen_iot2_Field_Typed, gen_iot2_Statement_For_Numeric_Statement, gen_iot2_Statement_For_Generic_Statement, gen_iot2_Statement_GlobalFunction_Declaration_Statement, gen_iot2_Statement_LocalFunction_Declaration_Statement, gen_iot2_Statement_While_Statement, gen_iot2_Statement_Repeat_Statement, gen_iot2_Statement_If_Then_Else_Statement, gen_iot2_Expression_TableConstructor_Expression, gen_iot2_Field_AddEntryToTable_Brackets_Field, gen_iot2_Field_AddEntryToTable_Field, gen_iot2_Field_AppendEntryToTable_Field, gen_iot2_LastStatement_ReturnWithValue_LastStatement_Return, gen_iot2_Statement_Assignment_Statement_FunctioncallOrAssignment, gen_iot2_Statement_Local_Variable_Declaration_Statement, gen_iot2_Statement_FunctioncallOrAssignment_Statement, gen_iot2_Expression_Statement_FunctioncallOrAssignment, gen_iot2_Expression_Nil_Expression, gen_iot2_Expression_True_Expression, gen_iot2_Expression_False_Expression, gen_iot2_Expression_Number_Expression, gen_iot2_Expression_VarArgs_Expression, gen_iot2_Expression_String_Expression, gen_iot2_Expression_Function_Expression, gen_iot2_Expression_Or_Expression, gen_iot2_Expression_And_Expression, gen_iot2_Expression_Larger_Expression, gen_iot2_Expression_Larger_Equal_Expression, gen_iot2_Statement_CallMemberFunction_Statement_FunctioncallOrAssignment, gen_iot2_Statement_CallFunction_Statement_FunctioncallOrAssignment, gen_iot2_Expression_Concatenation_Expression, gen_iot2_Expression_Plus_Expression, gen_iot2_Expression_Minus_Expression, gen_iot2_Expression_Smaller_Expression, gen_iot2_Expression_Multiplication_Expression, gen_iot2_Expression_Smaller_Equal_Expression, gen_iot2_Expression_Equal_Expression, gen_iot2_Expression_Not_Equal_Expression, gen_iot2_Expression_Negate_Expression, gen_iot2_Expression_Length_Expression, gen_iot2_Expression_Invert_Expression, gen_iot2_Expression_Exponentiation_Expression, gen_iot2_Expression_Division_Expression, gen_iot2_Expression_Modulo_Expression, gen_iot2_Expression_AccessMember_Expression, gen_iot2_Expression_VariableName_Expression, gen_iot2_ActivityNode_NamedElement, gen_iot2_Expression_CallMemberFunction_Expression, gen_iot2_ActivityEdge_NamedElement, gen_iot2_Expression_CallFunction_Expression, gen_iot2_Expression_AccessArray_Expression, gen_iot2_InitialNode_ControlNode, gen_iot2_FinalNode_ControlNode, gen_iot2_ActivityFinalNode_FinalNode, gen_iot2_ForkNode_ControlNode, gen_iot2_JoinNode_ControlNode, gen_iot2_MergeNode_ControlNode, gen_iot2_DecisionNode_ControlNode, gen_iot2_IntegerVariable_Variable, gen_iot2_BooleanVariable_Variable, gen_iot2_BooleanValue_Value, gen_iot2_IntegerValue_Value, gen_iot2_IntegerExpression_Expression, gen_iot2_ControlFlow_ActivityEdge, gen_iot2_ControlNode_ActivityNode, gen_iot2_ExecutableNode_ActivityNode, gen_iot2_Action_ExecutableNode, gen_iot2_OpaqueAction_Action, gen_iot2_BooleanUnaryExpression_BooleanExpression, gen_iot2_BooleanBinaryExpression_BooleanExpression, gen_iot2_BooleanExpression_Expression, gen_iot2_IntegerCalculationExpression_IntegerExpression, gen_iot2_IntegerComparisonExpression_IntegerExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)