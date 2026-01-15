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
            EnumerationLiteral(name="SMALLER"),
			EnumerationLiteral(name="SMALLER_EQUALS"),
			EnumerationLiteral(name="EQUALS"),
			EnumerationLiteral(name="GREATER_EQUALS"),
			EnumerationLiteral(name="GREATER")
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

# Classes
iot2_System = Class(name="iot2::System")
iot2_HWComponent = Class(name="iot2::HWComponent", is_abstract=True)
iot2_Board = Class(name="iot2::Board")
iot2_Sketch = Class(name="iot2::Sketch")
iot2_ExceptionDef = Class(name="iot2::ExceptionDef")
iot2_Block = Class(name="iot2::Block")
iot2_Contained = Class(name="iot2::Contained", is_abstract=True)
iot2_Activity = Class(name="iot2::Activity")
iot2_OperationDef = Class(name="iot2::OperationDef")
iot2_Sensor = Class(name="iot2::Sensor")
HWComponent = Class(name="HWComponent")
iot2_Actuator = Class(name="iot2::Actuator")
NamedElement = Class(name="NamedElement")
iot2_ActivityNode = Class(name="iot2::ActivityNode")
iot2_ActivityEdge = Class(name="iot2::ActivityEdge", is_abstract=True)
iot2_Variable = Class(name="iot2::Variable")
Contained = Class(name="Contained")
Typed = Class(name="Typed")
iot2_ParameterDef = Class(name="iot2::ParameterDef")
iot2_Expression = Class(name="iot2::Expression")
iot2_PrimitiveDef = Class(name="iot2::PrimitiveDef")
iot2_Container = Class(name="iot2::Container", is_abstract=True)
iot2_NamedElement = Class(name="iot2::NamedElement", is_abstract=True)
iot2_Typed = Class(name="iot2::Typed", is_abstract=True)
iot2_IDLType = Class(name="iot2::IDLType", is_abstract=True)
iot2_TypedefDef = Class(name="iot2::TypedefDef", is_abstract=True)
IDLType = Class(name="IDLType")
iot2_Field = Class(name="iot2::Field")
iot2_Statement_If_Then_Else = Class(name="iot2::Statement::If::Then::Else")
iot2_Statement_If_Then_Else_ElseIfPart = Class(name="iot2::Statement::If::Then::Else::ElseIfPart")
iot2_Chunk = Class(name="iot2::Chunk")
Chunk = Class(name="Chunk")
iot2_Statement = Class(name="iot2::Statement")
iot2_LastStatement = Class(name="iot2::LastStatement")
iot2_LastStatement_Return = Class(name="iot2::LastStatement::Return")
LastStatement = Class(name="LastStatement")
iot2_LastStatement_Break = Class(name="iot2::LastStatement::Break")
iot2_Statement_Block = Class(name="iot2::Statement::Block")
Statement = Class(name="Statement")
iot2_Statement_While = Class(name="iot2::Statement::While")
iot2_Statement_Repeat = Class(name="iot2::Statement::Repeat")
iot2_Function = Class(name="iot2::Function")
iot2_Statement_LocalFunction_Declaration = Class(name="iot2::Statement::LocalFunction::Declaration")
iot2_Statement_For_Numeric = Class(name="iot2::Statement::For::Numeric")
iot2_Statement_For_Generic = Class(name="iot2::Statement::For::Generic")
iot2_Statement_GlobalFunction_Declaration = Class(name="iot2::Statement::GlobalFunction::Declaration")
iot2_Statement_Local_Variable_Declaration = Class(name="iot2::Statement::Local::Variable::Declaration")
iot2_Statement_FunctioncallOrAssignment = Class(name="iot2::Statement::FunctioncallOrAssignment")
Statement_FunctioncallOrAssignment = Class(name="Statement::FunctioncallOrAssignment")
iot2_Expression_Nil = Class(name="iot2::Expression::Nil")
Expression = Class(name="Expression")
iot2_Expression_True = Class(name="iot2::Expression::True")
iot2_Expression_False = Class(name="iot2::Expression::False")
iot2_Expression_Number = Class(name="iot2::Expression::Number")
iot2_Statement_Assignment = Class(name="iot2::Statement::Assignment")
iot2_Expression_VarArgs = Class(name="iot2::Expression::VarArgs")
iot2_Expression_String = Class(name="iot2::Expression::String")
iot2_Expression_Function = Class(name="iot2::Expression::Function")
iot2_Expression_TableConstructor = Class(name="iot2::Expression::TableConstructor")
iot2_Functioncall_Arguments = Class(name="iot2::Functioncall::Arguments")
iot2_Field_AddEntryToTable_Brackets = Class(name="iot2::Field::AddEntryToTable::Brackets")
Field = Class(name="Field")
iot2_Field_AddEntryToTable = Class(name="iot2::Field::AddEntryToTable")
iot2_Field_AppendEntryToTable = Class(name="iot2::Field::AppendEntryToTable")
iot2_LastStatement_ReturnWithValue = Class(name="iot2::LastStatement::ReturnWithValue")
LastStatement_Return = Class(name="LastStatement::Return")
iot2_Expression_Or = Class(name="iot2::Expression::Or")
iot2_Statement_CallMemberFunction = Class(name="iot2::Statement::CallMemberFunction")
iot2_Statement_CallFunction = Class(name="iot2::Statement::CallFunction")
iot2_Expression_Larger = Class(name="iot2::Expression::Larger")
iot2_Expression_And = Class(name="iot2::Expression::And")
iot2_Expression_Smaller_Equal = Class(name="iot2::Expression::Smaller::Equal")
iot2_Expression_Larger_Equal = Class(name="iot2::Expression::Larger::Equal")
iot2_Expression_Smaller = Class(name="iot2::Expression::Smaller")
iot2_Expression_Equal = Class(name="iot2::Expression::Equal")
iot2_Expression_Not_Equal = Class(name="iot2::Expression::Not::Equal")
iot2_Expression_Minus = Class(name="iot2::Expression::Minus")
iot2_Expression_Concatenation = Class(name="iot2::Expression::Concatenation")
iot2_Expression_Plus = Class(name="iot2::Expression::Plus")
iot2_Expression_Division = Class(name="iot2::Expression::Division")
iot2_Expression_Multiplication = Class(name="iot2::Expression::Multiplication")
iot2_Expression_Length = Class(name="iot2::Expression::Length")
iot2_Expression_Modulo = Class(name="iot2::Expression::Modulo")
iot2_Expression_Negate = Class(name="iot2::Expression::Negate")
iot2_Expression_CallMemberFunction = Class(name="iot2::Expression::CallMemberFunction")
iot2_Expression_Invert = Class(name="iot2::Expression::Invert")
iot2_Expression_Exponentiation = Class(name="iot2::Expression::Exponentiation")
iot2_Expression_AccessMember = Class(name="iot2::Expression::AccessMember")
iot2_Expression_CallFunction = Class(name="iot2::Expression::CallFunction")
iot2_Expression_AccessArray = Class(name="iot2::Expression::AccessArray")
iot2_ControlFlow = Class(name="iot2::ControlFlow")
ActivityEdge = Class(name="ActivityEdge")
iot2_BooleanVariable = Class(name="iot2::BooleanVariable")
iot2_ControlNode = Class(name="iot2::ControlNode", is_abstract=True)
iot2_Expression_VariableName = Class(name="iot2::Expression::VariableName")
iot2_JoinNode = Class(name="iot2::JoinNode")
iot2_MergeNode = Class(name="iot2::MergeNode")
iot2_DecisionNode = Class(name="iot2::DecisionNode")
iot2_Value = Class(name="iot2::Value")
ActivityNode = Class(name="ActivityNode")
iot2_ExecutableNode = Class(name="iot2::ExecutableNode", is_abstract=True)
iot2_Action = Class(name="iot2::Action", is_abstract=True)
ExecutableNode = Class(name="ExecutableNode")
iot2_OpaqueAction = Class(name="iot2::OpaqueAction")
Action = Class(name="Action")
iot2_InitialNode = Class(name="iot2::InitialNode")
ControlNode = Class(name="ControlNode")
iot2_FinalNode = Class(name="iot2::FinalNode", is_abstract=True)
iot2_ActivityFinalNode = Class(name="iot2::ActivityFinalNode")
FinalNode = Class(name="FinalNode")
iot2_ForkNode = Class(name="iot2::ForkNode")
iot2_BooleanExpression = Class(name="iot2::BooleanExpression", is_abstract=True)
iot2_IntegerCalculationExpression = Class(name="iot2::IntegerCalculationExpression")
IntegerExpression = Class(name="IntegerExpression")
iot2_IntegerVariable = Class(name="iot2::IntegerVariable")
Variable = Class(name="Variable")
iot2_BooleanValue = Class(name="iot2::BooleanValue")
Value = Class(name="Value")
iot2_IntegerValue = Class(name="iot2::IntegerValue")
iot2_IntegerExpression = Class(name="iot2::IntegerExpression", is_abstract=True)
iot2_BooleanBinaryExpression = Class(name="iot2::BooleanBinaryExpression")
iot2_IntegerComparisonExpression = Class(name="iot2::IntegerComparisonExpression")
iot2_BooleanUnaryExpression = Class(name="iot2::BooleanUnaryExpression")
BooleanExpression = Class(name="BooleanExpression")
iot2_Trace = Class(name="iot2::Trace")
iot2_InputValue = Class(name="iot2::InputValue")
iot2_Input = Class(name="iot2::Input")
iot2_Token = Class(name="iot2::Token")

# iot2_System class attributes and methods
iot2_System_name: Property = Property(name="name", type=StringType)
iot2_System.attributes={iot2_System_name}

# iot2_HWComponent class attributes and methods
iot2_HWComponent_name: Property = Property(name="name", type=StringType)
iot2_HWComponent.attributes={iot2_HWComponent_name}

# iot2_Board class attributes and methods
iot2_Board_name: Property = Property(name="name", type=StringType)
iot2_Board_type: Property = Property(name="type", type=StringType)
iot2_Board.attributes={iot2_Board_type, iot2_Board_name}

# iot2_Sketch class attributes and methods

# iot2_ExceptionDef class attributes and methods
iot2_ExceptionDef_typeCode: Property = Property(name="typeCode", type=StringType)
iot2_ExceptionDef.attributes={iot2_ExceptionDef_typeCode}

# iot2_Block class attributes and methods

# iot2_Contained class attributes and methods
iot2_Contained_repositoryId: Property = Property(name="repositoryId", type=StringType)
iot2_Contained_version: Property = Property(name="version", type=StringType)
iot2_Contained_absoluteName: Property = Property(name="absoluteName", type=StringType)
iot2_Contained.attributes={iot2_Contained_version, iot2_Contained_absoluteName, iot2_Contained_repositoryId}

# iot2_Activity class attributes and methods

# iot2_OperationDef class attributes and methods
iot2_OperationDef_isOneway: Property = Property(name="isOneway", type=BooleanType)
iot2_OperationDef_contexts: Property = Property(name="contexts", type=StringType)
iot2_OperationDef.attributes={iot2_OperationDef_contexts, iot2_OperationDef_isOneway}

# iot2_Sensor class attributes and methods

# HWComponent class attributes and methods

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
iot2_ParameterDef.attributes={iot2_ParameterDef_identifier, iot2_ParameterDef_direction}

# iot2_Expression class attributes and methods

# iot2_PrimitiveDef class attributes and methods
iot2_PrimitiveDef_kind: Property = Property(name="kind", type=StringType)
iot2_PrimitiveDef.attributes={iot2_PrimitiveDef_kind}

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

# IDLType class attributes and methods

# iot2_Field class attributes and methods
iot2_Field_identifier: Property = Property(name="identifier", type=StringType)
iot2_Field.attributes={iot2_Field_identifier}

# iot2_Statement_If_Then_Else class attributes and methods

# iot2_Statement_If_Then_Else_ElseIfPart class attributes and methods

# iot2_Chunk class attributes and methods

# Chunk class attributes and methods

# iot2_Statement class attributes and methods

# iot2_LastStatement class attributes and methods

# iot2_LastStatement_Return class attributes and methods

# LastStatement class attributes and methods

# iot2_LastStatement_Break class attributes and methods

# iot2_Statement_Block class attributes and methods

# Statement class attributes and methods

# iot2_Statement_While class attributes and methods

# iot2_Statement_Repeat class attributes and methods

# iot2_Function class attributes and methods
iot2_Function_parameters: Property = Property(name="parameters", type=StringType)
iot2_Function_varArgs: Property = Property(name="varArgs", type=BooleanType)
iot2_Function.attributes={iot2_Function_parameters, iot2_Function_varArgs}

# iot2_Statement_LocalFunction_Declaration class attributes and methods
iot2_Statement_LocalFunction_Declaration_functionName: Property = Property(name="functionName", type=StringType)
iot2_Statement_LocalFunction_Declaration.attributes={iot2_Statement_LocalFunction_Declaration_functionName}

# iot2_Statement_For_Numeric class attributes and methods
iot2_Statement_For_Numeric_iteratorName: Property = Property(name="iteratorName", type=StringType)
iot2_Statement_For_Numeric.attributes={iot2_Statement_For_Numeric_iteratorName}

# iot2_Statement_For_Generic class attributes and methods
iot2_Statement_For_Generic_names: Property = Property(name="names", type=StringType)
iot2_Statement_For_Generic.attributes={iot2_Statement_For_Generic_names}

# iot2_Statement_GlobalFunction_Declaration class attributes and methods
iot2_Statement_GlobalFunction_Declaration_prefix: Property = Property(name="prefix", type=StringType)
iot2_Statement_GlobalFunction_Declaration_functionName: Property = Property(name="functionName", type=StringType)
iot2_Statement_GlobalFunction_Declaration.attributes={iot2_Statement_GlobalFunction_Declaration_prefix, iot2_Statement_GlobalFunction_Declaration_functionName}

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

# iot2_Statement_Assignment class attributes and methods

# iot2_Expression_VarArgs class attributes and methods

# iot2_Expression_String class attributes and methods
iot2_Expression_String_value: Property = Property(name="value", type=StringType)
iot2_Expression_String.attributes={iot2_Expression_String_value}

# iot2_Expression_Function class attributes and methods

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

# iot2_Expression_Or class attributes and methods

# iot2_Statement_CallMemberFunction class attributes and methods
iot2_Statement_CallMemberFunction_memberFunctionName: Property = Property(name="memberFunctionName", type=StringType)
iot2_Statement_CallMemberFunction.attributes={iot2_Statement_CallMemberFunction_memberFunctionName}

# iot2_Statement_CallFunction class attributes and methods

# iot2_Expression_Larger class attributes and methods

# iot2_Expression_And class attributes and methods

# iot2_Expression_Smaller_Equal class attributes and methods

# iot2_Expression_Larger_Equal class attributes and methods

# iot2_Expression_Smaller class attributes and methods

# iot2_Expression_Equal class attributes and methods

# iot2_Expression_Not_Equal class attributes and methods

# iot2_Expression_Minus class attributes and methods

# iot2_Expression_Concatenation class attributes and methods

# iot2_Expression_Plus class attributes and methods

# iot2_Expression_Division class attributes and methods

# iot2_Expression_Multiplication class attributes and methods

# iot2_Expression_Length class attributes and methods

# iot2_Expression_Modulo class attributes and methods

# iot2_Expression_Negate class attributes and methods

# iot2_Expression_CallMemberFunction class attributes and methods
iot2_Expression_CallMemberFunction_memberFunctionName: Property = Property(name="memberFunctionName", type=StringType)
iot2_Expression_CallMemberFunction.attributes={iot2_Expression_CallMemberFunction_memberFunctionName}

# iot2_Expression_Invert class attributes and methods

# iot2_Expression_Exponentiation class attributes and methods

# iot2_Expression_AccessMember class attributes and methods
iot2_Expression_AccessMember_memberName: Property = Property(name="memberName", type=StringType)
iot2_Expression_AccessMember.attributes={iot2_Expression_AccessMember_memberName}

# iot2_Expression_CallFunction class attributes and methods

# iot2_Expression_AccessArray class attributes and methods

# iot2_ControlFlow class attributes and methods

# ActivityEdge class attributes and methods

# iot2_BooleanVariable class attributes and methods

# iot2_ControlNode class attributes and methods

# iot2_Expression_VariableName class attributes and methods
iot2_Expression_VariableName_variable: Property = Property(name="variable", type=StringType)
iot2_Expression_VariableName.attributes={iot2_Expression_VariableName_variable}

# iot2_JoinNode class attributes and methods

# iot2_MergeNode class attributes and methods

# iot2_DecisionNode class attributes and methods

# iot2_Value class attributes and methods

# ActivityNode class attributes and methods

# iot2_ExecutableNode class attributes and methods

# iot2_Action class attributes and methods

# ExecutableNode class attributes and methods

# iot2_OpaqueAction class attributes and methods

# Action class attributes and methods

# iot2_InitialNode class attributes and methods

# ControlNode class attributes and methods

# iot2_FinalNode class attributes and methods

# iot2_ActivityFinalNode class attributes and methods

# FinalNode class attributes and methods

# iot2_ForkNode class attributes and methods

# iot2_BooleanExpression class attributes and methods

# iot2_IntegerCalculationExpression class attributes and methods
iot2_IntegerCalculationExpression_operator: Property = Property(name="operator", type=StringType)
iot2_IntegerCalculationExpression.attributes={iot2_IntegerCalculationExpression_operator}

# IntegerExpression class attributes and methods

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

# iot2_BooleanBinaryExpression class attributes and methods
iot2_BooleanBinaryExpression_operator: Property = Property(name="operator", type=StringType)
iot2_BooleanBinaryExpression.attributes={iot2_BooleanBinaryExpression_operator}

# iot2_IntegerComparisonExpression class attributes and methods
iot2_IntegerComparisonExpression_operator: Property = Property(name="operator", type=StringType)
iot2_IntegerComparisonExpression.attributes={iot2_IntegerComparisonExpression_operator}

# iot2_BooleanUnaryExpression class attributes and methods
iot2_BooleanUnaryExpression_operator: Property = Property(name="operator", type=StringType)
iot2_BooleanUnaryExpression.attributes={iot2_BooleanUnaryExpression_operator}

# BooleanExpression class attributes and methods

# iot2_Trace class attributes and methods

# iot2_InputValue class attributes and methods

# iot2_Input class attributes and methods

# iot2_Token class attributes and methods

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
canRaise23: BinaryAssociation = BinaryAssociation(
    name="canRaise23",
    ends={
        Property(name="iot2_ExceptionDef", type=iot2_OperationDef, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_OperationDef24", type=iot2_ExceptionDef, multiplicity=Multiplicity(0, 9999))
    }
)
lua25: BinaryAssociation = BinaryAssociation(
    name="lua25",
    ends={
        Property(name="iot2_Block", type=iot2_OperationDef, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_OperationDef26", type=iot2_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
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
nodes12: BinaryAssociation = BinaryAssociation(
    name="nodes12",
    ends={
        Property(name="13", type=iot2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=iot2_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges14: BinaryAssociation = BinaryAssociation(
    name="edges14",
    ends={
        Property(name="iot2_ActivityEdge", type=iot2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Activity15", type=iot2_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locals16: BinaryAssociation = BinaryAssociation(
    name="locals16",
    ends={
        Property(name="iot2_Variable", type=iot2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Activity17", type=iot2_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputs18: BinaryAssociation = BinaryAssociation(
    name="inputs18",
    ends={
        Property(name="iot2_Variable20", type=iot2_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Activity19", type=iot2_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters21: BinaryAssociation = BinaryAssociation(
    name="parameters21",
    ends={
        Property(name="iot2_ParameterDef", type=iot2_OperationDef, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_OperationDef22", type=iot2_ParameterDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value38: BinaryAssociation = BinaryAssociation(
    name="value38",
    ends={
        Property(name="iot2_Expression", type=iot2_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Field39", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definedIn27: BinaryAssociation = BinaryAssociation(
    name="definedIn27",
    ends={
        Property(name="29", type=iot2_Contained, multiplicity=Multiplicity(1, 1)),
        Property(name="28", type=iot2_Container, multiplicity=Multiplicity(0, 1))
    }
)
contains30: BinaryAssociation = BinaryAssociation(
    name="contains30",
    ends={
        Property(name="32", type=iot2_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="31", type=iot2_Contained, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containedType33: BinaryAssociation = BinaryAssociation(
    name="containedType33",
    ends={
        Property(name="iot2_IDLType", type=iot2_Typed, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Typed", type=iot2_IDLType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sharedType34: BinaryAssociation = BinaryAssociation(
    name="sharedType34",
    ends={
        Property(name="iot2_TypedefDef", type=iot2_Typed, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Typed35", type=iot2_TypedefDef, multiplicity=Multiplicity(0, 1))
    }
)
expression53: BinaryAssociation = BinaryAssociation(
    name="expression53",
    ends={
        Property(name="iot2_Expression55", type=iot2_Statement_Repeat, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_Repeat54", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
members36: BinaryAssociation = BinaryAssociation(
    name="members36",
    ends={
        Property(name="iot2_Field", type=iot2_ExceptionDef, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_ExceptionDef37", type=iot2_Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ifExpression56: BinaryAssociation = BinaryAssociation(
    name="ifExpression56",
    ends={
        Property(name="iot2_Expression57", type=iot2_Statement_If_Then_Else, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_If_Then_Else", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifBlock58: BinaryAssociation = BinaryAssociation(
    name="ifBlock58",
    ends={
        Property(name="iot2_Block60", type=iot2_Statement_If_Then_Else, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_If_Then_Else59", type=iot2_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseIf61: BinaryAssociation = BinaryAssociation(
    name="elseIf61",
    ends={
        Property(name="iot2_Statement_If_Then_Else_ElseIfPart", type=iot2_Statement_If_Then_Else, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_If_Then_Else62", type=iot2_Statement_If_Then_Else_ElseIfPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseBlock63: BinaryAssociation = BinaryAssociation(
    name="elseBlock63",
    ends={
        Property(name="iot2_Block65", type=iot2_Statement_If_Then_Else, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_If_Then_Else64", type=iot2_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseifExpression66: BinaryAssociation = BinaryAssociation(
    name="elseifExpression66",
    ends={
        Property(name="iot2_Expression68", type=iot2_Statement_If_Then_Else_ElseIfPart, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_If_Then_Else_ElseIfPart67", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements40: BinaryAssociation = BinaryAssociation(
    name="statements40",
    ends={
        Property(name="iot2_Statement", type=iot2_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Block41", type=iot2_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnValue42: BinaryAssociation = BinaryAssociation(
    name="returnValue42",
    ends={
        Property(name="iot2_LastStatement", type=iot2_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Block43", type=iot2_LastStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block44: BinaryAssociation = BinaryAssociation(
    name="block44",
    ends={
        Property(name="iot2_Block45", type=iot2_Statement_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_Block", type=iot2_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression46: BinaryAssociation = BinaryAssociation(
    name="expression46",
    ends={
        Property(name="iot2_Expression47", type=iot2_Statement_While, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_While", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block48: BinaryAssociation = BinaryAssociation(
    name="block48",
    ends={
        Property(name="iot2_Block50", type=iot2_Statement_While, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_While49", type=iot2_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block51: BinaryAssociation = BinaryAssociation(
    name="block51",
    ends={
        Property(name="iot2_Block52", type=iot2_Statement_Repeat, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_Repeat", type=iot2_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function88: BinaryAssociation = BinaryAssociation(
    name="function88",
    ends={
        Property(name="iot2_Function", type=iot2_Statement_GlobalFunction_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_GlobalFunction_Declaration", type=iot2_Function, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseifBlock69: BinaryAssociation = BinaryAssociation(
    name="elseifBlock69",
    ends={
        Property(name="iot2_Block71", type=iot2_Statement_If_Then_Else_ElseIfPart, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_If_Then_Else_ElseIfPart70", type=iot2_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
startExpr72: BinaryAssociation = BinaryAssociation(
    name="startExpr72",
    ends={
        Property(name="iot2_Expression73", type=iot2_Statement_For_Numeric, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_For_Numeric", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
untilExpr74: BinaryAssociation = BinaryAssociation(
    name="untilExpr74",
    ends={
        Property(name="iot2_Expression76", type=iot2_Statement_For_Numeric, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_For_Numeric75", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stepExpr77: BinaryAssociation = BinaryAssociation(
    name="stepExpr77",
    ends={
        Property(name="iot2_Expression79", type=iot2_Statement_For_Numeric, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_For_Numeric78", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block80: BinaryAssociation = BinaryAssociation(
    name="block80",
    ends={
        Property(name="iot2_Block82", type=iot2_Statement_For_Numeric, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_For_Numeric81", type=iot2_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions83: BinaryAssociation = BinaryAssociation(
    name="expressions83",
    ends={
        Property(name="iot2_Expression84", type=iot2_Statement_For_Generic, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_For_Generic", type=iot2_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block85: BinaryAssociation = BinaryAssociation(
    name="block85",
    ends={
        Property(name="iot2_Block87", type=iot2_Statement_For_Generic, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_For_Generic86", type=iot2_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function89: BinaryAssociation = BinaryAssociation(
    name="function89",
    ends={
        Property(name="iot2_Function90", type=iot2_Statement_LocalFunction_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_LocalFunction_Declaration", type=iot2_Function, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initialValue91: BinaryAssociation = BinaryAssociation(
    name="initialValue91",
    ends={
        Property(name="iot2_Expression92", type=iot2_Statement_Local_Variable_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_Local_Variable_Declaration", type=iot2_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnValues104: BinaryAssociation = BinaryAssociation(
    name="returnValues104",
    ends={
        Property(name="iot2_Expression105", type=iot2_LastStatement_ReturnWithValue, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_LastStatement_ReturnWithValue", type=iot2_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable106: BinaryAssociation = BinaryAssociation(
    name="variable106",
    ends={
        Property(name="iot2_Expression107", type=iot2_Statement_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_Assignment", type=iot2_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values108: BinaryAssociation = BinaryAssociation(
    name="values108",
    ends={
        Property(name="iot2_Expression110", type=iot2_Statement_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_Assignment109", type=iot2_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
function93: BinaryAssociation = BinaryAssociation(
    name="function93",
    ends={
        Property(name="iot2_Function94", type=iot2_Expression_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Function", type=iot2_Function, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fields95: BinaryAssociation = BinaryAssociation(
    name="fields95",
    ends={
        Property(name="iot2_Field96", type=iot2_Expression_TableConstructor, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_TableConstructor", type=iot2_Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body97: BinaryAssociation = BinaryAssociation(
    name="body97",
    ends={
        Property(name="iot2_Block99", type=iot2_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Function98", type=iot2_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments100: BinaryAssociation = BinaryAssociation(
    name="arguments100",
    ends={
        Property(name="iot2_Expression101", type=iot2_Functioncall_Arguments, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Functioncall_Arguments", type=iot2_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
indexExpression102: BinaryAssociation = BinaryAssociation(
    name="indexExpression102",
    ends={
        Property(name="iot2_Expression103", type=iot2_Field_AddEntryToTable_Brackets, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Field_AddEntryToTable_Brackets", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object116: BinaryAssociation = BinaryAssociation(
    name="object116",
    ends={
        Property(name="iot2_Expression117", type=iot2_Statement_CallFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_CallFunction", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments118: BinaryAssociation = BinaryAssociation(
    name="arguments118",
    ends={
        Property(name="iot2_Functioncall_Arguments120", type=iot2_Statement_CallFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_CallFunction119", type=iot2_Functioncall_Arguments, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object111: BinaryAssociation = BinaryAssociation(
    name="object111",
    ends={
        Property(name="iot2_Expression112", type=iot2_Statement_CallMemberFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_CallMemberFunction", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments113: BinaryAssociation = BinaryAssociation(
    name="arguments113",
    ends={
        Property(name="iot2_Functioncall_Arguments115", type=iot2_Statement_CallMemberFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Statement_CallMemberFunction114", type=iot2_Functioncall_Arguments, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left131: BinaryAssociation = BinaryAssociation(
    name="left131",
    ends={
        Property(name="iot2_Expression132", type=iot2_Expression_Larger, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Larger", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left121: BinaryAssociation = BinaryAssociation(
    name="left121",
    ends={
        Property(name="iot2_Expression122", type=iot2_Expression_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Or", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right123: BinaryAssociation = BinaryAssociation(
    name="right123",
    ends={
        Property(name="iot2_Expression125", type=iot2_Expression_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Or124", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left126: BinaryAssociation = BinaryAssociation(
    name="left126",
    ends={
        Property(name="iot2_Expression127", type=iot2_Expression_And, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_And", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right128: BinaryAssociation = BinaryAssociation(
    name="right128",
    ends={
        Property(name="iot2_Expression130", type=iot2_Expression_And, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_And129", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right143: BinaryAssociation = BinaryAssociation(
    name="right143",
    ends={
        Property(name="iot2_Expression145", type=iot2_Expression_Smaller, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Smaller144", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right133: BinaryAssociation = BinaryAssociation(
    name="right133",
    ends={
        Property(name="iot2_Expression135", type=iot2_Expression_Larger, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Larger134", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left136: BinaryAssociation = BinaryAssociation(
    name="left136",
    ends={
        Property(name="iot2_Expression137", type=iot2_Expression_Larger_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Larger_Equal", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right138: BinaryAssociation = BinaryAssociation(
    name="right138",
    ends={
        Property(name="iot2_Expression140", type=iot2_Expression_Larger_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Larger_Equal139", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left141: BinaryAssociation = BinaryAssociation(
    name="left141",
    ends={
        Property(name="iot2_Expression142", type=iot2_Expression_Smaller, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Smaller", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left156: BinaryAssociation = BinaryAssociation(
    name="left156",
    ends={
        Property(name="iot2_Expression157", type=iot2_Expression_Not_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Not_Equal", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right158: BinaryAssociation = BinaryAssociation(
    name="right158",
    ends={
        Property(name="iot2_Expression160", type=iot2_Expression_Not_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Not_Equal159", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left146: BinaryAssociation = BinaryAssociation(
    name="left146",
    ends={
        Property(name="iot2_Expression147", type=iot2_Expression_Smaller_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Smaller_Equal", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right148: BinaryAssociation = BinaryAssociation(
    name="right148",
    ends={
        Property(name="iot2_Expression150", type=iot2_Expression_Smaller_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Smaller_Equal149", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left151: BinaryAssociation = BinaryAssociation(
    name="left151",
    ends={
        Property(name="iot2_Expression152", type=iot2_Expression_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Equal", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right153: BinaryAssociation = BinaryAssociation(
    name="right153",
    ends={
        Property(name="iot2_Expression155", type=iot2_Expression_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Equal154", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right168: BinaryAssociation = BinaryAssociation(
    name="right168",
    ends={
        Property(name="iot2_Expression170", type=iot2_Expression_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Plus169", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left161: BinaryAssociation = BinaryAssociation(
    name="left161",
    ends={
        Property(name="iot2_Expression162", type=iot2_Expression_Concatenation, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Concatenation", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right163: BinaryAssociation = BinaryAssociation(
    name="right163",
    ends={
        Property(name="iot2_Expression165", type=iot2_Expression_Concatenation, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Concatenation164", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left166: BinaryAssociation = BinaryAssociation(
    name="left166",
    ends={
        Property(name="iot2_Expression167", type=iot2_Expression_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Plus", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left181: BinaryAssociation = BinaryAssociation(
    name="left181",
    ends={
        Property(name="iot2_Expression182", type=iot2_Expression_Division, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Division", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left171: BinaryAssociation = BinaryAssociation(
    name="left171",
    ends={
        Property(name="iot2_Expression172", type=iot2_Expression_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Minus", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right173: BinaryAssociation = BinaryAssociation(
    name="right173",
    ends={
        Property(name="iot2_Expression175", type=iot2_Expression_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Minus174", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left176: BinaryAssociation = BinaryAssociation(
    name="left176",
    ends={
        Property(name="iot2_Expression177", type=iot2_Expression_Multiplication, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Multiplication", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right178: BinaryAssociation = BinaryAssociation(
    name="right178",
    ends={
        Property(name="iot2_Expression180", type=iot2_Expression_Multiplication, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Multiplication179", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp191: BinaryAssociation = BinaryAssociation(
    name="exp191",
    ends={
        Property(name="iot2_Expression_Negate", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="iot2_Expression192", type=iot2_Expression_Negate, multiplicity=Multiplicity(1, 1))
    }
)
exp193: BinaryAssociation = BinaryAssociation(
    name="exp193",
    ends={
        Property(name="iot2_Expression194", type=iot2_Expression_Length, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Length", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right183: BinaryAssociation = BinaryAssociation(
    name="right183",
    ends={
        Property(name="iot2_Expression185", type=iot2_Expression_Division, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Division184", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left186: BinaryAssociation = BinaryAssociation(
    name="left186",
    ends={
        Property(name="iot2_Expression187", type=iot2_Expression_Modulo, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Modulo", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right188: BinaryAssociation = BinaryAssociation(
    name="right188",
    ends={
        Property(name="iot2_Expression190", type=iot2_Expression_Modulo, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Modulo189", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object202: BinaryAssociation = BinaryAssociation(
    name="object202",
    ends={
        Property(name="iot2_Expression203", type=iot2_Expression_CallMemberFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_CallMemberFunction", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp195: BinaryAssociation = BinaryAssociation(
    name="exp195",
    ends={
        Property(name="iot2_Expression196", type=iot2_Expression_Invert, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Invert", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left197: BinaryAssociation = BinaryAssociation(
    name="left197",
    ends={
        Property(name="iot2_Expression198", type=iot2_Expression_Exponentiation, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Exponentiation", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right199: BinaryAssociation = BinaryAssociation(
    name="right199",
    ends={
        Property(name="iot2_Expression201", type=iot2_Expression_Exponentiation, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_Exponentiation200", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object217: BinaryAssociation = BinaryAssociation(
    name="object217",
    ends={
        Property(name="iot2_Expression218", type=iot2_Expression_AccessMember, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_AccessMember", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments204: BinaryAssociation = BinaryAssociation(
    name="arguments204",
    ends={
        Property(name="iot2_Functioncall_Arguments206", type=iot2_Expression_CallMemberFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_CallMemberFunction205", type=iot2_Functioncall_Arguments, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object207: BinaryAssociation = BinaryAssociation(
    name="object207",
    ends={
        Property(name="iot2_Expression208", type=iot2_Expression_CallFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_CallFunction", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments209: BinaryAssociation = BinaryAssociation(
    name="arguments209",
    ends={
        Property(name="iot2_Functioncall_Arguments211", type=iot2_Expression_CallFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_CallFunction210", type=iot2_Functioncall_Arguments, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
array212: BinaryAssociation = BinaryAssociation(
    name="array212",
    ends={
        Property(name="iot2_Expression213", type=iot2_Expression_AccessArray, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_AccessArray", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
index214: BinaryAssociation = BinaryAssociation(
    name="index214",
    ends={
        Property(name="iot2_Expression216", type=iot2_Expression_AccessArray, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Expression_AccessArray215", type=iot2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target231: BinaryAssociation = BinaryAssociation(
    name="target231",
    ends={
        Property(name="233", type=iot2_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="232", type=iot2_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
guard234: BinaryAssociation = BinaryAssociation(
    name="guard234",
    ends={
        Property(name="iot2_BooleanVariable", type=iot2_ControlFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_ControlFlow", type=iot2_BooleanVariable, multiplicity=Multiplicity(0, 1))
    }
)
outgoing219: BinaryAssociation = BinaryAssociation(
    name="outgoing219",
    ends={
        Property(name="221", type=iot2_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="220", type=iot2_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
incoming222: BinaryAssociation = BinaryAssociation(
    name="incoming222",
    ends={
        Property(name="224", type=iot2_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="223", type=iot2_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
activity225: BinaryAssociation = BinaryAssociation(
    name="activity225",
    ends={
        Property(name="227", type=iot2_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="226", type=iot2_Activity, multiplicity=Multiplicity(1, 1))
    }
)
source228: BinaryAssociation = BinaryAssociation(
    name="source228",
    ends={
        Property(name="230", type=iot2_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="229", type=iot2_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
initialValue240: BinaryAssociation = BinaryAssociation(
    name="initialValue240",
    ends={
        Property(name="iot2_Value", type=iot2_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Variable241", type=iot2_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions235: BinaryAssociation = BinaryAssociation(
    name="expressions235",
    ends={
        Property(name="iot2_Expression236", type=iot2_OpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_OpaqueAction", type=iot2_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
service237: BinaryAssociation = BinaryAssociation(
    name="service237",
    ends={
        Property(name="iot2_OperationDef239", type=iot2_OpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_OpaqueAction238", type=iot2_OperationDef, multiplicity=Multiplicity(0, 1))
    }
)
operand1246: BinaryAssociation = BinaryAssociation(
    name="operand1246",
    ends={
        Property(name="iot2_IntegerVariable248", type=iot2_IntegerExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_IntegerExpression247", type=iot2_IntegerVariable, multiplicity=Multiplicity(0, 1))
    }
)
assignee249: BinaryAssociation = BinaryAssociation(
    name="assignee249",
    ends={
        Property(name="iot2_BooleanVariable250", type=iot2_BooleanExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_BooleanExpression", type=iot2_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
currentValue242: BinaryAssociation = BinaryAssociation(
    name="currentValue242",
    ends={
        Property(name="iot2_Value244", type=iot2_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Variable243", type=iot2_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand2245: BinaryAssociation = BinaryAssociation(
    name="operand2245",
    ends={
        Property(name="iot2_IntegerVariable", type=iot2_IntegerExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_IntegerExpression", type=iot2_IntegerVariable, multiplicity=Multiplicity(0, 1))
    }
)
operand255: BinaryAssociation = BinaryAssociation(
    name="operand255",
    ends={
        Property(name="iot2_BooleanVariable256", type=iot2_BooleanUnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_BooleanUnaryExpression", type=iot2_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
operand1257: BinaryAssociation = BinaryAssociation(
    name="operand1257",
    ends={
        Property(name="iot2_BooleanVariable258", type=iot2_BooleanBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_BooleanBinaryExpression", type=iot2_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
assignee251: BinaryAssociation = BinaryAssociation(
    name="assignee251",
    ends={
        Property(name="iot2_IntegerVariable252", type=iot2_IntegerCalculationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_IntegerCalculationExpression", type=iot2_IntegerVariable, multiplicity=Multiplicity(1, 1))
    }
)
assignee253: BinaryAssociation = BinaryAssociation(
    name="assignee253",
    ends={
        Property(name="iot2_BooleanVariable254", type=iot2_IntegerComparisonExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_IntegerComparisonExpression", type=iot2_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
executedNodes270: BinaryAssociation = BinaryAssociation(
    name="executedNodes270",
    ends={
        Property(name="iot2_ActivityNode271", type=iot2_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Trace", type=iot2_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
operand2259: BinaryAssociation = BinaryAssociation(
    name="operand2259",
    ends={
        Property(name="iot2_BooleanVariable261", type=iot2_BooleanBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_BooleanBinaryExpression260", type=iot2_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
value262: BinaryAssociation = BinaryAssociation(
    name="value262",
    ends={
        Property(name="iot2_Value263", type=iot2_InputValue, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_InputValue", type=iot2_Value, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable264: BinaryAssociation = BinaryAssociation(
    name="variable264",
    ends={
        Property(name="iot2_Variable266", type=iot2_InputValue, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_InputValue265", type=iot2_Variable, multiplicity=Multiplicity(1, 1))
    }
)
inputValues267: BinaryAssociation = BinaryAssociation(
    name="inputValues267",
    ends={
        Property(name="iot2_InputValue268", type=iot2_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Input", type=iot2_InputValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
holder269: BinaryAssociation = BinaryAssociation(
    name="holder269",
    ends={
        Property(name="iot2_ActivityNode", type=iot2_Token, multiplicity=Multiplicity(1, 1)),
        Property(name="iot2_Token", type=iot2_ActivityNode, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_iot2_Contained_NamedElement = Generalization(general=NamedElement, specific=iot2_Contained)
gen_iot2_Sensor_HWComponent = Generalization(general=HWComponent, specific=iot2_Sensor)
gen_iot2_Actuator_HWComponent = Generalization(general=HWComponent, specific=iot2_Actuator)
gen_iot2_Activity_NamedElement = Generalization(general=NamedElement, specific=iot2_Activity)
gen_iot2_OperationDef_Contained = Generalization(general=Contained, specific=iot2_OperationDef)
gen_iot2_OperationDef_Typed = Generalization(general=Typed, specific=iot2_OperationDef)
gen_iot2_Field_Typed = Generalization(general=Typed, specific=iot2_Field)
gen_iot2_PrimitiveDef_IDLType = Generalization(general=IDLType, specific=iot2_PrimitiveDef)
gen_iot2_Container_Contained = Generalization(general=Contained, specific=iot2_Container)
gen_iot2_TypedefDef_IDLType = Generalization(general=IDLType, specific=iot2_TypedefDef)
gen_iot2_TypedefDef_Contained = Generalization(general=Contained, specific=iot2_TypedefDef)
gen_iot2_ParameterDef_Typed = Generalization(general=Typed, specific=iot2_ParameterDef)
gen_iot2_ExceptionDef_Contained = Generalization(general=Contained, specific=iot2_ExceptionDef)
gen_iot2_Statement_If_Then_Else_Statement = Generalization(general=Statement, specific=iot2_Statement_If_Then_Else)
gen_iot2_Block_Chunk = Generalization(general=Chunk, specific=iot2_Block)
gen_iot2_LastStatement_Return_LastStatement = Generalization(general=LastStatement, specific=iot2_LastStatement_Return)
gen_iot2_LastStatement_Break_LastStatement = Generalization(general=LastStatement, specific=iot2_LastStatement_Break)
gen_iot2_Statement_Block_Statement = Generalization(general=Statement, specific=iot2_Statement_Block)
gen_iot2_Statement_While_Statement = Generalization(general=Statement, specific=iot2_Statement_While)
gen_iot2_Statement_Repeat_Statement = Generalization(general=Statement, specific=iot2_Statement_Repeat)
gen_iot2_Statement_LocalFunction_Declaration_Statement = Generalization(general=Statement, specific=iot2_Statement_LocalFunction_Declaration)
gen_iot2_Statement_For_Numeric_Statement = Generalization(general=Statement, specific=iot2_Statement_For_Numeric)
gen_iot2_Statement_For_Generic_Statement = Generalization(general=Statement, specific=iot2_Statement_For_Generic)
gen_iot2_Statement_GlobalFunction_Declaration_Statement = Generalization(general=Statement, specific=iot2_Statement_GlobalFunction_Declaration)
gen_iot2_Statement_Local_Variable_Declaration_Statement = Generalization(general=Statement, specific=iot2_Statement_Local_Variable_Declaration)
gen_iot2_Statement_FunctioncallOrAssignment_Statement = Generalization(general=Statement, specific=iot2_Statement_FunctioncallOrAssignment)
gen_iot2_Expression_Statement_FunctioncallOrAssignment = Generalization(general=Statement_FunctioncallOrAssignment, specific=iot2_Expression)
gen_iot2_Expression_Nil_Expression = Generalization(general=Expression, specific=iot2_Expression_Nil)
gen_iot2_Expression_True_Expression = Generalization(general=Expression, specific=iot2_Expression_True)
gen_iot2_Expression_False_Expression = Generalization(general=Expression, specific=iot2_Expression_False)
gen_iot2_Statement_Assignment_Statement_FunctioncallOrAssignment = Generalization(general=Statement_FunctioncallOrAssignment, specific=iot2_Statement_Assignment)
gen_iot2_Expression_Number_Expression = Generalization(general=Expression, specific=iot2_Expression_Number)
gen_iot2_Expression_VarArgs_Expression = Generalization(general=Expression, specific=iot2_Expression_VarArgs)
gen_iot2_Expression_String_Expression = Generalization(general=Expression, specific=iot2_Expression_String)
gen_iot2_Expression_Function_Expression = Generalization(general=Expression, specific=iot2_Expression_Function)
gen_iot2_Expression_TableConstructor_Expression = Generalization(general=Expression, specific=iot2_Expression_TableConstructor)
gen_iot2_Field_AddEntryToTable_Brackets_Field = Generalization(general=Field, specific=iot2_Field_AddEntryToTable_Brackets)
gen_iot2_Field_AddEntryToTable_Field = Generalization(general=Field, specific=iot2_Field_AddEntryToTable)
gen_iot2_Field_AppendEntryToTable_Field = Generalization(general=Field, specific=iot2_Field_AppendEntryToTable)
gen_iot2_LastStatement_ReturnWithValue_LastStatement_Return = Generalization(general=LastStatement_Return, specific=iot2_LastStatement_ReturnWithValue)
gen_iot2_Statement_CallMemberFunction_Statement_FunctioncallOrAssignment = Generalization(general=Statement_FunctioncallOrAssignment, specific=iot2_Statement_CallMemberFunction)
gen_iot2_Statement_CallFunction_Statement_FunctioncallOrAssignment = Generalization(general=Statement_FunctioncallOrAssignment, specific=iot2_Statement_CallFunction)
gen_iot2_Expression_Larger_Expression = Generalization(general=Expression, specific=iot2_Expression_Larger)
gen_iot2_Expression_Or_Expression = Generalization(general=Expression, specific=iot2_Expression_Or)
gen_iot2_Expression_And_Expression = Generalization(general=Expression, specific=iot2_Expression_And)
gen_iot2_Expression_Smaller_Equal_Expression = Generalization(general=Expression, specific=iot2_Expression_Smaller_Equal)
gen_iot2_Expression_Larger_Equal_Expression = Generalization(general=Expression, specific=iot2_Expression_Larger_Equal)
gen_iot2_Expression_Smaller_Expression = Generalization(general=Expression, specific=iot2_Expression_Smaller)
gen_iot2_Expression_Equal_Expression = Generalization(general=Expression, specific=iot2_Expression_Equal)
gen_iot2_Expression_Not_Equal_Expression = Generalization(general=Expression, specific=iot2_Expression_Not_Equal)
gen_iot2_Expression_Minus_Expression = Generalization(general=Expression, specific=iot2_Expression_Minus)
gen_iot2_Expression_Concatenation_Expression = Generalization(general=Expression, specific=iot2_Expression_Concatenation)
gen_iot2_Expression_Plus_Expression = Generalization(general=Expression, specific=iot2_Expression_Plus)
gen_iot2_Expression_Division_Expression = Generalization(general=Expression, specific=iot2_Expression_Division)
gen_iot2_Expression_Multiplication_Expression = Generalization(general=Expression, specific=iot2_Expression_Multiplication)
gen_iot2_Expression_Length_Expression = Generalization(general=Expression, specific=iot2_Expression_Length)
gen_iot2_Expression_Modulo_Expression = Generalization(general=Expression, specific=iot2_Expression_Modulo)
gen_iot2_Expression_Negate_Expression = Generalization(general=Expression, specific=iot2_Expression_Negate)
gen_iot2_Expression_CallMemberFunction_Expression = Generalization(general=Expression, specific=iot2_Expression_CallMemberFunction)
gen_iot2_Expression_Invert_Expression = Generalization(general=Expression, specific=iot2_Expression_Invert)
gen_iot2_Expression_Exponentiation_Expression = Generalization(general=Expression, specific=iot2_Expression_Exponentiation)
gen_iot2_Expression_AccessMember_Expression = Generalization(general=Expression, specific=iot2_Expression_AccessMember)
gen_iot2_Expression_CallFunction_Expression = Generalization(general=Expression, specific=iot2_Expression_CallFunction)
gen_iot2_Expression_AccessArray_Expression = Generalization(general=Expression, specific=iot2_Expression_AccessArray)
gen_iot2_ControlFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=iot2_ControlFlow)
gen_iot2_Expression_VariableName_Expression = Generalization(general=Expression, specific=iot2_Expression_VariableName)
gen_iot2_ActivityNode_NamedElement = Generalization(general=NamedElement, specific=iot2_ActivityNode)
gen_iot2_ActivityEdge_NamedElement = Generalization(general=NamedElement, specific=iot2_ActivityEdge)
gen_iot2_JoinNode_ControlNode = Generalization(general=ControlNode, specific=iot2_JoinNode)
gen_iot2_MergeNode_ControlNode = Generalization(general=ControlNode, specific=iot2_MergeNode)
gen_iot2_DecisionNode_ControlNode = Generalization(general=ControlNode, specific=iot2_DecisionNode)
gen_iot2_ControlNode_ActivityNode = Generalization(general=ActivityNode, specific=iot2_ControlNode)
gen_iot2_ExecutableNode_ActivityNode = Generalization(general=ActivityNode, specific=iot2_ExecutableNode)
gen_iot2_Action_ExecutableNode = Generalization(general=ExecutableNode, specific=iot2_Action)
gen_iot2_OpaqueAction_Action = Generalization(general=Action, specific=iot2_OpaqueAction)
gen_iot2_InitialNode_ControlNode = Generalization(general=ControlNode, specific=iot2_InitialNode)
gen_iot2_FinalNode_ControlNode = Generalization(general=ControlNode, specific=iot2_FinalNode)
gen_iot2_ActivityFinalNode_FinalNode = Generalization(general=FinalNode, specific=iot2_ActivityFinalNode)
gen_iot2_ForkNode_ControlNode = Generalization(general=ControlNode, specific=iot2_ForkNode)
gen_iot2_BooleanExpression_Expression = Generalization(general=Expression, specific=iot2_BooleanExpression)
gen_iot2_IntegerVariable_Variable = Generalization(general=Variable, specific=iot2_IntegerVariable)
gen_iot2_BooleanVariable_Variable = Generalization(general=Variable, specific=iot2_BooleanVariable)
gen_iot2_BooleanValue_Value = Generalization(general=Value, specific=iot2_BooleanValue)
gen_iot2_IntegerValue_Value = Generalization(general=Value, specific=iot2_IntegerValue)
gen_iot2_IntegerExpression_Expression = Generalization(general=Expression, specific=iot2_IntegerExpression)
gen_iot2_BooleanBinaryExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=iot2_BooleanBinaryExpression)
gen_iot2_IntegerCalculationExpression_IntegerExpression = Generalization(general=IntegerExpression, specific=iot2_IntegerCalculationExpression)
gen_iot2_IntegerComparisonExpression_IntegerExpression = Generalization(general=IntegerExpression, specific=iot2_IntegerComparisonExpression)
gen_iot2_BooleanUnaryExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=iot2_BooleanUnaryExpression)

# Domain Model
domain_model = DomainModel(
    name="iot2",
    types={iot2_System, iot2_HWComponent, iot2_Board, iot2_Sketch, iot2_ExceptionDef, iot2_Block, iot2_Contained, iot2_Activity, iot2_OperationDef, iot2_Sensor, HWComponent, iot2_Actuator, NamedElement, iot2_ActivityNode, iot2_ActivityEdge, iot2_Variable, Contained, Typed, iot2_ParameterDef, iot2_Expression, iot2_PrimitiveDef, iot2_Container, iot2_NamedElement, iot2_Typed, iot2_IDLType, iot2_TypedefDef, IDLType, iot2_Field, iot2_Statement_If_Then_Else, iot2_Statement_If_Then_Else_ElseIfPart, iot2_Chunk, Chunk, iot2_Statement, iot2_LastStatement, iot2_LastStatement_Return, LastStatement, iot2_LastStatement_Break, iot2_Statement_Block, Statement, iot2_Statement_While, iot2_Statement_Repeat, iot2_Function, iot2_Statement_LocalFunction_Declaration, iot2_Statement_For_Numeric, iot2_Statement_For_Generic, iot2_Statement_GlobalFunction_Declaration, iot2_Statement_Local_Variable_Declaration, iot2_Statement_FunctioncallOrAssignment, Statement_FunctioncallOrAssignment, iot2_Expression_Nil, Expression, iot2_Expression_True, iot2_Expression_False, iot2_Expression_Number, iot2_Statement_Assignment, iot2_Expression_VarArgs, iot2_Expression_String, iot2_Expression_Function, iot2_Expression_TableConstructor, iot2_Functioncall_Arguments, iot2_Field_AddEntryToTable_Brackets, Field, iot2_Field_AddEntryToTable, iot2_Field_AppendEntryToTable, iot2_LastStatement_ReturnWithValue, LastStatement_Return, iot2_Expression_Or, iot2_Statement_CallMemberFunction, iot2_Statement_CallFunction, iot2_Expression_Larger, iot2_Expression_And, iot2_Expression_Smaller_Equal, iot2_Expression_Larger_Equal, iot2_Expression_Smaller, iot2_Expression_Equal, iot2_Expression_Not_Equal, iot2_Expression_Minus, iot2_Expression_Concatenation, iot2_Expression_Plus, iot2_Expression_Division, iot2_Expression_Multiplication, iot2_Expression_Length, iot2_Expression_Modulo, iot2_Expression_Negate, iot2_Expression_CallMemberFunction, iot2_Expression_Invert, iot2_Expression_Exponentiation, iot2_Expression_AccessMember, iot2_Expression_CallFunction, iot2_Expression_AccessArray, iot2_ControlFlow, ActivityEdge, iot2_BooleanVariable, iot2_ControlNode, iot2_Expression_VariableName, iot2_JoinNode, iot2_MergeNode, iot2_DecisionNode, iot2_Value, ActivityNode, iot2_ExecutableNode, iot2_Action, ExecutableNode, iot2_OpaqueAction, Action, iot2_InitialNode, ControlNode, iot2_FinalNode, iot2_ActivityFinalNode, FinalNode, iot2_ForkNode, iot2_BooleanExpression, iot2_IntegerCalculationExpression, IntegerExpression, iot2_IntegerVariable, Variable, iot2_BooleanValue, Value, iot2_IntegerValue, iot2_IntegerExpression, iot2_BooleanBinaryExpression, iot2_IntegerComparisonExpression, iot2_BooleanUnaryExpression, BooleanExpression, iot2_Trace, iot2_InputValue, iot2_Input, iot2_Token, BoardType, PrimitiveKind, ParameterMode, IntegerCalculationOperator, IntegerComparisonOperator, BooleanUnaryOperator, BooleanBinaryOperator},
    associations={components0, boards1, sketch3, canRaise23, lua25, components5, activity8, services10, nodes12, edges14, locals16, inputs18, parameters21, value38, definedIn27, contains30, containedType33, sharedType34, expression53, members36, ifExpression56, ifBlock58, elseIf61, elseBlock63, elseifExpression66, statements40, returnValue42, block44, expression46, block48, block51, function88, elseifBlock69, startExpr72, untilExpr74, stepExpr77, block80, expressions83, block85, function89, initialValue91, returnValues104, variable106, values108, function93, fields95, body97, arguments100, indexExpression102, object116, arguments118, object111, arguments113, left131, left121, right123, left126, right128, right143, right133, left136, right138, left141, left156, right158, left146, right148, left151, right153, right168, left161, right163, left166, left181, left171, right173, left176, right178, exp191, exp193, right183, left186, right188, object202, exp195, left197, right199, object217, arguments204, object207, arguments209, array212, index214, target231, guard234, outgoing219, incoming222, activity225, source228, initialValue240, expressions235, service237, operand1246, assignee249, currentValue242, operand2245, operand255, operand1257, assignee251, assignee253, executedNodes270, operand2259, value262, variable264, inputValues267, holder269},
    generalizations={gen_iot2_Contained_NamedElement, gen_iot2_Sensor_HWComponent, gen_iot2_Actuator_HWComponent, gen_iot2_Activity_NamedElement, gen_iot2_OperationDef_Contained, gen_iot2_OperationDef_Typed, gen_iot2_Field_Typed, gen_iot2_PrimitiveDef_IDLType, gen_iot2_Container_Contained, gen_iot2_TypedefDef_IDLType, gen_iot2_TypedefDef_Contained, gen_iot2_ParameterDef_Typed, gen_iot2_ExceptionDef_Contained, gen_iot2_Statement_If_Then_Else_Statement, gen_iot2_Block_Chunk, gen_iot2_LastStatement_Return_LastStatement, gen_iot2_LastStatement_Break_LastStatement, gen_iot2_Statement_Block_Statement, gen_iot2_Statement_While_Statement, gen_iot2_Statement_Repeat_Statement, gen_iot2_Statement_LocalFunction_Declaration_Statement, gen_iot2_Statement_For_Numeric_Statement, gen_iot2_Statement_For_Generic_Statement, gen_iot2_Statement_GlobalFunction_Declaration_Statement, gen_iot2_Statement_Local_Variable_Declaration_Statement, gen_iot2_Statement_FunctioncallOrAssignment_Statement, gen_iot2_Expression_Statement_FunctioncallOrAssignment, gen_iot2_Expression_Nil_Expression, gen_iot2_Expression_True_Expression, gen_iot2_Expression_False_Expression, gen_iot2_Statement_Assignment_Statement_FunctioncallOrAssignment, gen_iot2_Expression_Number_Expression, gen_iot2_Expression_VarArgs_Expression, gen_iot2_Expression_String_Expression, gen_iot2_Expression_Function_Expression, gen_iot2_Expression_TableConstructor_Expression, gen_iot2_Field_AddEntryToTable_Brackets_Field, gen_iot2_Field_AddEntryToTable_Field, gen_iot2_Field_AppendEntryToTable_Field, gen_iot2_LastStatement_ReturnWithValue_LastStatement_Return, gen_iot2_Statement_CallMemberFunction_Statement_FunctioncallOrAssignment, gen_iot2_Statement_CallFunction_Statement_FunctioncallOrAssignment, gen_iot2_Expression_Larger_Expression, gen_iot2_Expression_Or_Expression, gen_iot2_Expression_And_Expression, gen_iot2_Expression_Smaller_Equal_Expression, gen_iot2_Expression_Larger_Equal_Expression, gen_iot2_Expression_Smaller_Expression, gen_iot2_Expression_Equal_Expression, gen_iot2_Expression_Not_Equal_Expression, gen_iot2_Expression_Minus_Expression, gen_iot2_Expression_Concatenation_Expression, gen_iot2_Expression_Plus_Expression, gen_iot2_Expression_Division_Expression, gen_iot2_Expression_Multiplication_Expression, gen_iot2_Expression_Length_Expression, gen_iot2_Expression_Modulo_Expression, gen_iot2_Expression_Negate_Expression, gen_iot2_Expression_CallMemberFunction_Expression, gen_iot2_Expression_Invert_Expression, gen_iot2_Expression_Exponentiation_Expression, gen_iot2_Expression_AccessMember_Expression, gen_iot2_Expression_CallFunction_Expression, gen_iot2_Expression_AccessArray_Expression, gen_iot2_ControlFlow_ActivityEdge, gen_iot2_Expression_VariableName_Expression, gen_iot2_ActivityNode_NamedElement, gen_iot2_ActivityEdge_NamedElement, gen_iot2_JoinNode_ControlNode, gen_iot2_MergeNode_ControlNode, gen_iot2_DecisionNode_ControlNode, gen_iot2_ControlNode_ActivityNode, gen_iot2_ExecutableNode_ActivityNode, gen_iot2_Action_ExecutableNode, gen_iot2_OpaqueAction_Action, gen_iot2_InitialNode_ControlNode, gen_iot2_FinalNode_ControlNode, gen_iot2_ActivityFinalNode_FinalNode, gen_iot2_ForkNode_ControlNode, gen_iot2_BooleanExpression_Expression, gen_iot2_IntegerVariable_Variable, gen_iot2_BooleanVariable_Variable, gen_iot2_BooleanValue_Value, gen_iot2_IntegerValue_Value, gen_iot2_IntegerExpression_Expression, gen_iot2_BooleanBinaryExpression_BooleanExpression, gen_iot2_IntegerCalculationExpression_IntegerExpression, gen_iot2_IntegerComparisonExpression_IntegerExpression, gen_iot2_BooleanUnaryExpression_BooleanExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)