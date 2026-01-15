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
FunctionKind: Enumeration = Enumeration(
    name="FunctionKind",
    literals={
            EnumerationLiteral(name="Stateless"),
			EnumerationLiteral(name="Stateful"),
			EnumerationLiteral(name="Continuous")
    }
)

AssertionStatusKind: Enumeration = Enumeration(
    name="AssertionStatusKind",
    literals={
            EnumerationLiteral(name="Info"),
			EnumerationLiteral(name="Warning"),
			EnumerationLiteral(name="Error"),
			EnumerationLiteral(name="Fatal")
    }
)

EqualityOperator: Enumeration = Enumeration(
    name="EqualityOperator",
    literals={
            EnumerationLiteral(name="EqualTo"),
			EnumerationLiteral(name="NotEqualTo")
    }
)

RelationalOperator: Enumeration = Enumeration(
    name="RelationalOperator",
    literals={
            EnumerationLiteral(name="LessThan"),
			EnumerationLiteral(name="LessThanOrEqualTo"),
			EnumerationLiteral(name="GreaterThan"),
			EnumerationLiteral(name="GreaterThanOrEqualTo")
    }
)

AdditiveOperator: Enumeration = Enumeration(
    name="AdditiveOperator",
    literals={
            EnumerationLiteral(name="Add"),
			EnumerationLiteral(name="Subtract")
    }
)

UnaryOperator: Enumeration = Enumeration(
    name="UnaryOperator",
    literals={
            EnumerationLiteral(name="Negate"),
			EnumerationLiteral(name="LogicalNot")
    }
)

PostfixOperator: Enumeration = Enumeration(
    name="PostfixOperator",
    literals={
            EnumerationLiteral(name="Transpose")
    }
)

MultiplicativeOperator: Enumeration = Enumeration(
    name="MultiplicativeOperator",
    literals={
            EnumerationLiteral(name="Multiply"),
			EnumerationLiteral(name="Divide"),
			EnumerationLiteral(name="ElementWiseMultiply"),
			EnumerationLiteral(name="ElementWiseDivide")
    }
)

PowerOperator: Enumeration = Enumeration(
    name="PowerOperator",
    literals={
            EnumerationLiteral(name="ElementWisePower"),
			EnumerationLiteral(name="Power")
    }
)

# Classes
ast_Module = Class(name="ast::Module")
ast_Definition = Class(name="ast::Definition", is_abstract=True)
ast_EnumerationDefinition = Class(name="ast::EnumerationDefinition")
DataTypeDefinition = Class(name="DataTypeDefinition")
ast_EnumerationLiteralDeclaration = Class(name="ast::EnumerationLiteralDeclaration")
ast_TypeAliasDefinition = Class(name="ast::TypeAliasDefinition")
ast_PrimitiveType = Class(name="ast::PrimitiveType")
ast_RecordDefinition = Class(name="ast::RecordDefinition")
ast_RecordFieldDeclaration = Class(name="ast::RecordFieldDeclaration")
ast_DataTypeSpecifier = Class(name="ast::DataTypeSpecifier")
ast_FunctionDefinition = Class(name="ast::FunctionDefinition")
CallableElement = Class(name="CallableElement")
ast_DataTypeDefinition = Class(name="ast::DataTypeDefinition", is_abstract=True)
Definition = Class(name="Definition")
ast_OutputParameterDeclaration = Class(name="ast::OutputParameterDeclaration")
ast_Check = Class(name="ast::Check")
ast_Assertion = Class(name="ast::Assertion")
ast_FunctionObjectDeclaration = Class(name="ast::FunctionObjectDeclaration")
ast_StateVariableDeclaration = Class(name="ast::StateVariableDeclaration")
ast_Equation = Class(name="ast::Equation")
ast_TemplateParameterDeclaration = Class(name="ast::TemplateParameterDeclaration")
ast_InputParameterDeclaration = Class(name="ast::InputParameterDeclaration")
ast_CallableElement = Class(name="ast::CallableElement", is_abstract=True)
ast_ParameterDeclaration = Class(name="ast::ParameterDeclaration", is_abstract=True)
ParameterDeclaration = Class(name="ParameterDeclaration")
ast_Expression = Class(name="ast::Expression")
ast_DataType = Class(name="ast::DataType")
ast_LetExpressionVariableDeclarationPart = Class(name="ast::LetExpressionVariableDeclarationPart")
ast_IfExpression = Class(name="ast::IfExpression")
ast_LetExpression = Class(name="ast::LetExpression")
Expression = Class(name="Expression")
ast_LetExpressionVariableDeclaration = Class(name="ast::LetExpressionVariableDeclaration")
ast_SwitchCase = Class(name="ast::SwitchCase")
ast_SwitchExpression = Class(name="ast::SwitchExpression")
ast_ArrayElementAccess = Class(name="ast::ArrayElementAccess")
ast_ArraySubscript = Class(name="ast::ArraySubscript")
ast_IterationCall = Class(name="ast::IterationCall")
ast_DerivativeOperator = Class(name="ast::DerivativeOperator")
ast_ArrayConstructionOperator = Class(name="ast::ArrayConstructionOperator")
ast_IterationVariable = Class(name="ast::IterationVariable")
ast_IterationAccumulator = Class(name="ast::IterationAccumulator")
ast_ArrayConcatenationOperator = Class(name="ast::ArrayConcatenationOperator")
ast_ExpressionList = Class(name="ast::ExpressionList")
ast_UnitConstructionOperator = Class(name="ast::UnitConstructionOperator")
ast_Unit = Class(name="ast::Unit")
ast_ParenthesizedExpression = Class(name="ast::ParenthesizedExpression")
ast_EndExpression = Class(name="ast::EndExpression")
ast_ArrayConstructionIterationClause = Class(name="ast::ArrayConstructionIterationClause")
ast_LogicalOrExpression = Class(name="ast::LogicalOrExpression")
ast_LogicalAndExpression = Class(name="ast::LogicalAndExpression")
ast_EqualityExpression = Class(name="ast::EqualityExpression")
ast_RangeExpression = Class(name="ast::RangeExpression")
ast_ImpliesExpression = Class(name="ast::ImpliesExpression")
ast_RelationalExpression = Class(name="ast::RelationalExpression")
ast_TypeTestExpression = Class(name="ast::TypeTestExpression")
ast_AdditiveExpression = Class(name="ast::AdditiveExpression")
ast_MultiplicativeExpression = Class(name="ast::MultiplicativeExpression")
ast_PowerExpression = Class(name="ast::PowerExpression")
ast_UnaryExpression = Class(name="ast::UnaryExpression")
ast_FeatureCall = Class(name="ast::FeatureCall", is_abstract=True)
ast_VariableAccess = Class(name="ast::VariableAccess")
FeatureCall = Class(name="FeatureCall")
ast_StepExpression = Class(name="ast::StepExpression", is_abstract=True)
ast_RangeStepExpression = Class(name="ast::RangeStepExpression")
StepExpression = Class(name="StepExpression")
ast_AdditiveStepExpression = Class(name="ast::AdditiveStepExpression")
ast_PostfixExpression = Class(name="ast::PostfixExpression")
ast_NegateStepExpression = Class(name="ast::NegateStepExpression")
ast_PrimitiveStepExpression = Class(name="ast::PrimitiveStepExpression", is_abstract=True)
ast_StepLiteral = Class(name="ast::StepLiteral")
PrimitiveStepExpression = Class(name="PrimitiveStepExpression")
ast_StepN = Class(name="ast::StepN")
ast_FunctionCall = Class(name="ast::FunctionCall")
ast_MemberVariableAccess = Class(name="ast::MemberVariableAccess")
Statement = Class(name="Statement")
ast_Statement = Class(name="ast::Statement", is_abstract=True)
ast_Assignment = Class(name="ast::Assignment")
ast_VariableDeclaration = Class(name="ast::VariableDeclaration")
ast_IfStatement = Class(name="ast::IfStatement")
ast_AlgorithmExpression = Class(name="ast::AlgorithmExpression")
ast_Compound = Class(name="ast::Compound")
ast_WhileStatement = Class(name="ast::WhileStatement")
ast_DoWhileStatement = Class(name="ast::DoWhileStatement")
ast_ForStatement = Class(name="ast::ForStatement")
ast_BreakStatement = Class(name="ast::BreakStatement")
ast_ReturnStatement = Class(name="ast::ReturnStatement")
ast_BuiltinDefinition = Class(name="ast::BuiltinDefinition")
ast_BuiltinFunction = Class(name="ast::BuiltinFunction")
BuiltinDefinition = Class(name="BuiltinDefinition")
ast_BuiltinVariable = Class(name="ast::BuiltinVariable")
ast_ContinueStatement = Class(name="ast::ContinueStatement")

# ast_Module class attributes and methods

# ast_Definition class attributes and methods
ast_Definition_name: Property = Property(name="name", type=StringType)
ast_Definition.attributes={ast_Definition_name}

# ast_EnumerationDefinition class attributes and methods

# DataTypeDefinition class attributes and methods

# ast_EnumerationLiteralDeclaration class attributes and methods
ast_EnumerationLiteralDeclaration_name: Property = Property(name="name", type=StringType)
ast_EnumerationLiteralDeclaration.attributes={ast_EnumerationLiteralDeclaration_name}

# ast_TypeAliasDefinition class attributes and methods

# ast_PrimitiveType class attributes and methods

# ast_RecordDefinition class attributes and methods

# ast_RecordFieldDeclaration class attributes and methods
ast_RecordFieldDeclaration_name: Property = Property(name="name", type=StringType)
ast_RecordFieldDeclaration.attributes={ast_RecordFieldDeclaration_name}

# ast_DataTypeSpecifier class attributes and methods

# ast_FunctionDefinition class attributes and methods
ast_FunctionDefinition_kind: Property = Property(name="kind", type=StringType)
ast_FunctionDefinition.attributes={ast_FunctionDefinition_kind}

# CallableElement class attributes and methods

# ast_DataTypeDefinition class attributes and methods

# Definition class attributes and methods

# ast_OutputParameterDeclaration class attributes and methods

# ast_Check class attributes and methods

# ast_Assertion class attributes and methods
ast_Assertion_static: Property = Property(name="static", type=BooleanType)
ast_Assertion_statusKind: Property = Property(name="statusKind", type=StringType)
ast_Assertion.attributes={ast_Assertion_static, ast_Assertion_statusKind}

# ast_FunctionObjectDeclaration class attributes and methods
ast_FunctionObjectDeclaration_name: Property = Property(name="name", type=StringType)
ast_FunctionObjectDeclaration.attributes={ast_FunctionObjectDeclaration_name}

# ast_StateVariableDeclaration class attributes and methods
ast_StateVariableDeclaration_name: Property = Property(name="name", type=StringType)
ast_StateVariableDeclaration.attributes={ast_StateVariableDeclaration_name}

# ast_Equation class attributes and methods
ast_Equation_initial: Property = Property(name="initial", type=BooleanType)
ast_Equation.attributes={ast_Equation_initial}

# ast_TemplateParameterDeclaration class attributes and methods

# ast_InputParameterDeclaration class attributes and methods

# ast_CallableElement class attributes and methods
ast_CallableElement_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
ast_CallableElement_m_getQualifiedName: Method = Method(name="getQualifiedName", parameters={}, type=StringType)
ast_CallableElement.methods={ast_CallableElement_m_getQualifiedName, ast_CallableElement_m_getName}

# ast_ParameterDeclaration class attributes and methods
ast_ParameterDeclaration_name: Property = Property(name="name", type=StringType)
ast_ParameterDeclaration.attributes={ast_ParameterDeclaration_name}

# ParameterDeclaration class attributes and methods

# ast_Expression class attributes and methods

# ast_DataType class attributes and methods

# ast_LetExpressionVariableDeclarationPart class attributes and methods
ast_LetExpressionVariableDeclarationPart_name: Property = Property(name="name", type=StringType)
ast_LetExpressionVariableDeclarationPart.attributes={ast_LetExpressionVariableDeclarationPart_name}

# ast_IfExpression class attributes and methods
ast_IfExpression_static: Property = Property(name="static", type=BooleanType)
ast_IfExpression.attributes={ast_IfExpression_static}

# ast_LetExpression class attributes and methods

# Expression class attributes and methods

# ast_LetExpressionVariableDeclaration class attributes and methods

# ast_SwitchCase class attributes and methods

# ast_SwitchExpression class attributes and methods
ast_SwitchExpression_static: Property = Property(name="static", type=BooleanType)
ast_SwitchExpression.attributes={ast_SwitchExpression_static}

# ast_ArrayElementAccess class attributes and methods

# ast_ArraySubscript class attributes and methods
ast_ArraySubscript_slice: Property = Property(name="slice", type=BooleanType)
ast_ArraySubscript.attributes={ast_ArraySubscript_slice}

# ast_IterationCall class attributes and methods
ast_IterationCall_identifier: Property = Property(name="identifier", type=StringType)
ast_IterationCall.attributes={ast_IterationCall_identifier}

# ast_DerivativeOperator class attributes and methods

# ast_ArrayConstructionOperator class attributes and methods

# ast_IterationVariable class attributes and methods
ast_IterationVariable_name: Property = Property(name="name", type=StringType)
ast_IterationVariable.attributes={ast_IterationVariable_name}

# ast_IterationAccumulator class attributes and methods
ast_IterationAccumulator_name: Property = Property(name="name", type=StringType)
ast_IterationAccumulator.attributes={ast_IterationAccumulator_name}

# ast_ArrayConcatenationOperator class attributes and methods

# ast_ExpressionList class attributes and methods

# ast_UnitConstructionOperator class attributes and methods

# ast_Unit class attributes and methods

# ast_ParenthesizedExpression class attributes and methods

# ast_EndExpression class attributes and methods

# ast_ArrayConstructionIterationClause class attributes and methods
ast_ArrayConstructionIterationClause_variableName: Property = Property(name="variableName", type=StringType)
ast_ArrayConstructionIterationClause.attributes={ast_ArrayConstructionIterationClause_variableName}

# ast_LogicalOrExpression class attributes and methods

# ast_LogicalAndExpression class attributes and methods

# ast_EqualityExpression class attributes and methods
ast_EqualityExpression_operator: Property = Property(name="operator", type=StringType)
ast_EqualityExpression.attributes={ast_EqualityExpression_operator}

# ast_RangeExpression class attributes and methods

# ast_ImpliesExpression class attributes and methods

# ast_RelationalExpression class attributes and methods
ast_RelationalExpression_operator: Property = Property(name="operator", type=StringType)
ast_RelationalExpression.attributes={ast_RelationalExpression_operator}

# ast_TypeTestExpression class attributes and methods

# ast_AdditiveExpression class attributes and methods
ast_AdditiveExpression_operator: Property = Property(name="operator", type=StringType)
ast_AdditiveExpression.attributes={ast_AdditiveExpression_operator}

# ast_MultiplicativeExpression class attributes and methods
ast_MultiplicativeExpression_operator: Property = Property(name="operator", type=StringType)
ast_MultiplicativeExpression.attributes={ast_MultiplicativeExpression_operator}

# ast_PowerExpression class attributes and methods
ast_PowerExpression_operator: Property = Property(name="operator", type=StringType)
ast_PowerExpression.attributes={ast_PowerExpression_operator}

# ast_UnaryExpression class attributes and methods
ast_UnaryExpression_operator: Property = Property(name="operator", type=StringType)
ast_UnaryExpression.attributes={ast_UnaryExpression_operator}

# ast_FeatureCall class attributes and methods

# ast_VariableAccess class attributes and methods
ast_VariableAccess_m_isInitial: Method = Method(name="isInitial", parameters={}, type=BooleanType)
ast_VariableAccess.methods={ast_VariableAccess_m_isInitial}

# FeatureCall class attributes and methods

# ast_StepExpression class attributes and methods

# ast_RangeStepExpression class attributes and methods

# StepExpression class attributes and methods

# ast_AdditiveStepExpression class attributes and methods
ast_AdditiveStepExpression_operator: Property = Property(name="operator", type=StringType)
ast_AdditiveStepExpression.attributes={ast_AdditiveStepExpression_operator}

# ast_PostfixExpression class attributes and methods
ast_PostfixExpression_operator: Property = Property(name="operator", type=StringType)
ast_PostfixExpression.attributes={ast_PostfixExpression_operator}

# ast_NegateStepExpression class attributes and methods

# ast_PrimitiveStepExpression class attributes and methods

# ast_StepLiteral class attributes and methods
ast_StepLiteral_value: Property = Property(name="value", type=IntegerType)
ast_StepLiteral.attributes={ast_StepLiteral_value}

# PrimitiveStepExpression class attributes and methods

# ast_StepN class attributes and methods

# ast_FunctionCall class attributes and methods

# ast_MemberVariableAccess class attributes and methods

# Statement class attributes and methods

# ast_Statement class attributes and methods

# ast_Assignment class attributes and methods

# ast_VariableDeclaration class attributes and methods
ast_VariableDeclaration_name: Property = Property(name="name", type=StringType)
ast_VariableDeclaration.attributes={ast_VariableDeclaration_name}

# ast_IfStatement class attributes and methods

# ast_AlgorithmExpression class attributes and methods

# ast_Compound class attributes and methods

# ast_WhileStatement class attributes and methods

# ast_DoWhileStatement class attributes and methods

# ast_ForStatement class attributes and methods

# ast_BreakStatement class attributes and methods

# ast_ReturnStatement class attributes and methods

# ast_BuiltinDefinition class attributes and methods

# ast_BuiltinFunction class attributes and methods

# BuiltinDefinition class attributes and methods

# ast_BuiltinVariable class attributes and methods

# ast_ContinueStatement class attributes and methods

# Relationships
literalDeclarations1: BinaryAssociation = BinaryAssociation(
    name="literalDeclarations1",
    ends={
        Property(name="ast_EnumerationLiteralDeclaration", type=ast_EnumerationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_EnumerationDefinition", type=ast_EnumerationLiteralDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type2: BinaryAssociation = BinaryAssociation(
    name="type2",
    ends={
        Property(name="ast_PrimitiveType", type=ast_TypeAliasDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_TypeAliasDefinition", type=ast_PrimitiveType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fieldDeclarations3: BinaryAssociation = BinaryAssociation(
    name="fieldDeclarations3",
    ends={
        Property(name="ast_RecordFieldDeclaration", type=ast_RecordDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_RecordDefinition", type=ast_RecordFieldDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type4: BinaryAssociation = BinaryAssociation(
    name="type4",
    ends={
        Property(name="ast_DataTypeSpecifier", type=ast_RecordFieldDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_RecordFieldDeclaration5", type=ast_DataTypeSpecifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definitions0: BinaryAssociation = BinaryAssociation(
    name="definitions0",
    ends={
        Property(name="ast_Definition", type=ast_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_Module", type=ast_Definition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputParameterDeclarations9: BinaryAssociation = BinaryAssociation(
    name="outputParameterDeclarations9",
    ends={
        Property(name="ast_OutputParameterDeclaration", type=ast_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_FunctionDefinition10", type=ast_OutputParameterDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
checks11: BinaryAssociation = BinaryAssociation(
    name="checks11",
    ends={
        Property(name="Check", type=ast_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="function", type=ast_Check, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assertions12: BinaryAssociation = BinaryAssociation(
    name="assertions12",
    ends={
        Property(name="ast_Assertion", type=ast_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_FunctionDefinition13", type=ast_Assertion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionObjectDeclarations14: BinaryAssociation = BinaryAssociation(
    name="functionObjectDeclarations14",
    ends={
        Property(name="ast_FunctionObjectDeclaration", type=ast_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_FunctionDefinition15", type=ast_FunctionObjectDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateVariableDeclarations16: BinaryAssociation = BinaryAssociation(
    name="stateVariableDeclarations16",
    ends={
        Property(name="ast_StateVariableDeclaration", type=ast_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_FunctionDefinition17", type=ast_StateVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
equations18: BinaryAssociation = BinaryAssociation(
    name="equations18",
    ends={
        Property(name="ast_Equation", type=ast_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_FunctionDefinition19", type=ast_Equation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
templateParameterDeclarations6: BinaryAssociation = BinaryAssociation(
    name="templateParameterDeclarations6",
    ends={
        Property(name="ast_TemplateParameterDeclaration", type=ast_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_FunctionDefinition", type=ast_TemplateParameterDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputParameterDeclarations7: BinaryAssociation = BinaryAssociation(
    name="inputParameterDeclarations7",
    ends={
        Property(name="ast_InputParameterDeclaration", type=ast_FunctionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_FunctionDefinition8", type=ast_InputParameterDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputParameterTypes22: BinaryAssociation = BinaryAssociation(
    name="inputParameterTypes22",
    ends={
        Property(name="ast_DataTypeSpecifier24", type=ast_Check, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_Check23", type=ast_DataTypeSpecifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputParameterTypes25: BinaryAssociation = BinaryAssociation(
    name="outputParameterTypes25",
    ends={
        Property(name="ast_DataTypeSpecifier27", type=ast_Check, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_Check26", type=ast_DataTypeSpecifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
function20: BinaryAssociation = BinaryAssociation(
    name="function20",
    ends={
        Property(name="FunctionDefinition", type=ast_Check, multiplicity=Multiplicity(1, 1)),
        Property(name="checks", type=ast_FunctionDefinition, multiplicity=Multiplicity(1, 1))
    }
)
templateArguments21: BinaryAssociation = BinaryAssociation(
    name="templateArguments21",
    ends={
        Property(name="ast_Expression", type=ast_Check, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_Check", type=ast_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionName34: BinaryAssociation = BinaryAssociation(
    name="functionName34",
    ends={
        Property(name="ast_FunctionDefinition36", type=ast_FunctionObjectDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_FunctionObjectDeclaration35", type=ast_FunctionDefinition, multiplicity=Multiplicity(0, 1))
    }
)
templateArguments37: BinaryAssociation = BinaryAssociation(
    name="templateArguments37",
    ends={
        Property(name="ast_Expression39", type=ast_FunctionObjectDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_FunctionObjectDeclaration38", type=ast_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leftHandSide40: BinaryAssociation = BinaryAssociation(
    name="leftHandSide40",
    ends={
        Property(name="ast_Expression42", type=ast_Equation, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_Equation41", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightHandSide43: BinaryAssociation = BinaryAssociation(
    name="rightHandSide43",
    ends={
        Property(name="ast_Expression45", type=ast_Equation, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_Equation44", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition28: BinaryAssociation = BinaryAssociation(
    name="condition28",
    ends={
        Property(name="ast_Expression30", type=ast_Assertion, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_Assertion29", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableDeclarations51: BinaryAssociation = BinaryAssociation(
    name="variableDeclarations51",
    ends={
        Property(name="ast_LetExpressionVariableDeclaration", type=ast_LetExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_LetExpression", type=ast_LetExpressionVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
message31: BinaryAssociation = BinaryAssociation(
    name="message31",
    ends={
        Property(name="ast_Expression33", type=ast_Assertion, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_Assertion32", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetExpression52: BinaryAssociation = BinaryAssociation(
    name="targetExpression52",
    ends={
        Property(name="ast_Expression54", type=ast_LetExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_LetExpression53", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parts55: BinaryAssociation = BinaryAssociation(
    name="parts55",
    ends={
        Property(name="ast_LetExpressionVariableDeclarationPart", type=ast_LetExpressionVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_LetExpressionVariableDeclaration56", type=ast_LetExpressionVariableDeclarationPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assignedExpression57: BinaryAssociation = BinaryAssociation(
    name="assignedExpression57",
    ends={
        Property(name="ast_Expression59", type=ast_LetExpressionVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_LetExpressionVariableDeclaration58", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition60: BinaryAssociation = BinaryAssociation(
    name="condition60",
    ends={
        Property(name="ast_Expression61", type=ast_IfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_IfExpression", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenExpression62: BinaryAssociation = BinaryAssociation(
    name="thenExpression62",
    ends={
        Property(name="ast_Expression64", type=ast_IfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_IfExpression63", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type46: BinaryAssociation = BinaryAssociation(
    name="type46",
    ends={
        Property(name="ast_DataType", type=ast_DataTypeSpecifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_DataTypeSpecifier47", type=ast_DataType, multiplicity=Multiplicity(0, 1))
    }
)
definedType48: BinaryAssociation = BinaryAssociation(
    name="definedType48",
    ends={
        Property(name="ast_DataType50", type=ast_DataTypeSpecifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_DataTypeSpecifier49", type=ast_DataType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cases70: BinaryAssociation = BinaryAssociation(
    name="cases70",
    ends={
        Property(name="ast_SwitchCase", type=ast_SwitchExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_SwitchExpression71", type=ast_SwitchCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultExpression72: BinaryAssociation = BinaryAssociation(
    name="defaultExpression72",
    ends={
        Property(name="ast_Expression74", type=ast_SwitchExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_SwitchExpression73", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
caseExpression75: BinaryAssociation = BinaryAssociation(
    name="caseExpression75",
    ends={
        Property(name="ast_Expression77", type=ast_SwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_SwitchCase76", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resultExpression78: BinaryAssociation = BinaryAssociation(
    name="resultExpression78",
    ends={
        Property(name="ast_Expression80", type=ast_SwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_SwitchCase79", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseExpression65: BinaryAssociation = BinaryAssociation(
    name="elseExpression65",
    ends={
        Property(name="ast_Expression67", type=ast_IfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_IfExpression66", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
controlExpression68: BinaryAssociation = BinaryAssociation(
    name="controlExpression68",
    ends={
        Property(name="ast_Expression69", type=ast_SwitchExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_SwitchExpression", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
array81: BinaryAssociation = BinaryAssociation(
    name="array81",
    ends={
        Property(name="ast_Expression82", type=ast_ArrayElementAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ArrayElementAccess", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subscripts83: BinaryAssociation = BinaryAssociation(
    name="subscripts83",
    ends={
        Property(name="ast_ArraySubscript", type=ast_ArrayElementAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ArrayElementAccess84", type=ast_ArraySubscript, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression85: BinaryAssociation = BinaryAssociation(
    name="expression85",
    ends={
        Property(name="ast_Expression87", type=ast_ArraySubscript, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ArraySubscript86", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target88: BinaryAssociation = BinaryAssociation(
    name="target88",
    ends={
        Property(name="ast_Expression89", type=ast_IterationCall, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_IterationCall", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
breakCondition94: BinaryAssociation = BinaryAssociation(
    name="breakCondition94",
    ends={
        Property(name="ast_Expression96", type=ast_IterationCall, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_IterationCall95", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression97: BinaryAssociation = BinaryAssociation(
    name="expression97",
    ends={
        Property(name="ast_Expression99", type=ast_IterationCall, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_IterationCall98", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initializer100: BinaryAssociation = BinaryAssociation(
    name="initializer100",
    ends={
        Property(name="ast_Expression102", type=ast_IterationAccumulator, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_IterationAccumulator101", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable103: BinaryAssociation = BinaryAssociation(
    name="variable103",
    ends={
        Property(name="ast_CallableElement", type=ast_DerivativeOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_DerivativeOperator", type=ast_CallableElement, multiplicity=Multiplicity(0, 1))
    }
)
variables90: BinaryAssociation = BinaryAssociation(
    name="variables90",
    ends={
        Property(name="ast_IterationVariable", type=ast_IterationCall, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_IterationCall91", type=ast_IterationVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
accumulator92: BinaryAssociation = BinaryAssociation(
    name="accumulator92",
    ends={
        Property(name="ast_IterationAccumulator", type=ast_IterationCall, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_IterationCall93", type=ast_IterationAccumulator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
collectionExpression108: BinaryAssociation = BinaryAssociation(
    name="collectionExpression108",
    ends={
        Property(name="ast_Expression110", type=ast_ArrayConstructionIterationClause, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ArrayConstructionIterationClause109", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rows111: BinaryAssociation = BinaryAssociation(
    name="rows111",
    ends={
        Property(name="ast_ExpressionList", type=ast_ArrayConcatenationOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ArrayConcatenationOperator", type=ast_ExpressionList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressions112: BinaryAssociation = BinaryAssociation(
    name="expressions112",
    ends={
        Property(name="ast_Expression114", type=ast_ExpressionList, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ExpressionList113", type=ast_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unit115: BinaryAssociation = BinaryAssociation(
    name="unit115",
    ends={
        Property(name="ast_Unit", type=ast_UnitConstructionOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_UnitConstructionOperator", type=ast_Unit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions116: BinaryAssociation = BinaryAssociation(
    name="expressions116",
    ends={
        Property(name="ast_Expression117", type=ast_ParenthesizedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ParenthesizedExpression", type=ast_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressions104: BinaryAssociation = BinaryAssociation(
    name="expressions104",
    ends={
        Property(name="ast_Expression105", type=ast_ArrayConstructionOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ArrayConstructionOperator", type=ast_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
iterationClauses106: BinaryAssociation = BinaryAssociation(
    name="iterationClauses106",
    ends={
        Property(name="ast_ArrayConstructionIterationClause", type=ast_ArrayConstructionOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ArrayConstructionOperator107", type=ast_ArrayConstructionIterationClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leftOperand120: BinaryAssociation = BinaryAssociation(
    name="leftOperand120",
    ends={
        Property(name="ast_ImpliesExpression", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="ast_Expression121", type=ast_ImpliesExpression, multiplicity=Multiplicity(1, 1))
    }
)
rightOperand122: BinaryAssociation = BinaryAssociation(
    name="rightOperand122",
    ends={
        Property(name="ast_Expression124", type=ast_ImpliesExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ImpliesExpression123", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand125: BinaryAssociation = BinaryAssociation(
    name="leftOperand125",
    ends={
        Property(name="ast_Expression126", type=ast_LogicalOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_LogicalOrExpression", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand127: BinaryAssociation = BinaryAssociation(
    name="rightOperand127",
    ends={
        Property(name="ast_Expression129", type=ast_LogicalOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_LogicalOrExpression128", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand130: BinaryAssociation = BinaryAssociation(
    name="leftOperand130",
    ends={
        Property(name="ast_Expression131", type=ast_LogicalAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_LogicalAndExpression", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand132: BinaryAssociation = BinaryAssociation(
    name="rightOperand132",
    ends={
        Property(name="ast_Expression134", type=ast_LogicalAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_LogicalAndExpression133", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operands118: BinaryAssociation = BinaryAssociation(
    name="operands118",
    ends={
        Property(name="ast_Expression119", type=ast_RangeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_RangeExpression", type=ast_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leftOperand140: BinaryAssociation = BinaryAssociation(
    name="leftOperand140",
    ends={
        Property(name="ast_Expression141", type=ast_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_RelationalExpression", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand142: BinaryAssociation = BinaryAssociation(
    name="rightOperand142",
    ends={
        Property(name="ast_Expression144", type=ast_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_RelationalExpression143", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression145: BinaryAssociation = BinaryAssociation(
    name="expression145",
    ends={
        Property(name="ast_Expression146", type=ast_TypeTestExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_TypeTestExpression", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type147: BinaryAssociation = BinaryAssociation(
    name="type147",
    ends={
        Property(name="ast_DataTypeSpecifier149", type=ast_TypeTestExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_TypeTestExpression148", type=ast_DataTypeSpecifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand150: BinaryAssociation = BinaryAssociation(
    name="leftOperand150",
    ends={
        Property(name="ast_Expression151", type=ast_AdditiveExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_AdditiveExpression", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand135: BinaryAssociation = BinaryAssociation(
    name="leftOperand135",
    ends={
        Property(name="ast_Expression136", type=ast_EqualityExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_EqualityExpression", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand137: BinaryAssociation = BinaryAssociation(
    name="rightOperand137",
    ends={
        Property(name="ast_Expression139", type=ast_EqualityExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_EqualityExpression138", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand155: BinaryAssociation = BinaryAssociation(
    name="leftOperand155",
    ends={
        Property(name="ast_Expression156", type=ast_MultiplicativeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MultiplicativeExpression", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand157: BinaryAssociation = BinaryAssociation(
    name="rightOperand157",
    ends={
        Property(name="ast_Expression159", type=ast_MultiplicativeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MultiplicativeExpression158", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand160: BinaryAssociation = BinaryAssociation(
    name="operand160",
    ends={
        Property(name="ast_Expression161", type=ast_PowerExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_PowerExpression", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exponent162: BinaryAssociation = BinaryAssociation(
    name="exponent162",
    ends={
        Property(name="ast_Expression164", type=ast_PowerExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_PowerExpression163", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand152: BinaryAssociation = BinaryAssociation(
    name="rightOperand152",
    ends={
        Property(name="ast_Expression154", type=ast_AdditiveExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_AdditiveExpression153", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand167: BinaryAssociation = BinaryAssociation(
    name="operand167",
    ends={
        Property(name="ast_Expression168", type=ast_PostfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_PostfixExpression", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
feature169: BinaryAssociation = BinaryAssociation(
    name="feature169",
    ends={
        Property(name="ast_CallableElement170", type=ast_FeatureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_FeatureCall", type=ast_CallableElement, multiplicity=Multiplicity(0, 1))
    }
)
stepExpression171: BinaryAssociation = BinaryAssociation(
    name="stepExpression171",
    ends={
        Property(name="ast_StepExpression", type=ast_VariableAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_VariableAccess", type=ast_StepExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
start172: BinaryAssociation = BinaryAssociation(
    name="start172",
    ends={
        Property(name="ast_StepExpression173", type=ast_RangeStepExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_RangeStepExpression", type=ast_StepExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
end174: BinaryAssociation = BinaryAssociation(
    name="end174",
    ends={
        Property(name="ast_StepExpression176", type=ast_RangeStepExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_RangeStepExpression175", type=ast_StepExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand165: BinaryAssociation = BinaryAssociation(
    name="operand165",
    ends={
        Property(name="ast_Expression166", type=ast_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_UnaryExpression", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand182: BinaryAssociation = BinaryAssociation(
    name="operand182",
    ends={
        Property(name="ast_StepExpression183", type=ast_NegateStepExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_NegateStepExpression", type=ast_StepExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments184: BinaryAssociation = BinaryAssociation(
    name="arguments184",
    ends={
        Property(name="ast_Expression185", type=ast_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_FunctionCall", type=ast_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target186: BinaryAssociation = BinaryAssociation(
    name="target186",
    ends={
        Property(name="ast_Expression187", type=ast_MemberVariableAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MemberVariableAccess", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand177: BinaryAssociation = BinaryAssociation(
    name="leftOperand177",
    ends={
        Property(name="ast_StepExpression178", type=ast_AdditiveStepExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_AdditiveStepExpression", type=ast_StepExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand179: BinaryAssociation = BinaryAssociation(
    name="rightOperand179",
    ends={
        Property(name="ast_StepExpression181", type=ast_AdditiveStepExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_AdditiveStepExpression180", type=ast_StepExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements192: BinaryAssociation = BinaryAssociation(
    name="statements192",
    ends={
        Property(name="ast_Statement", type=ast_Compound, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_Compound193", type=ast_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target194: BinaryAssociation = BinaryAssociation(
    name="target194",
    ends={
        Property(name="ast_Expression195", type=ast_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_Assignment", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression196: BinaryAssociation = BinaryAssociation(
    name="expression196",
    ends={
        Property(name="ast_Expression198", type=ast_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_Assignment197", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initializer199: BinaryAssociation = BinaryAssociation(
    name="initializer199",
    ends={
        Property(name="ast_Expression200", type=ast_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_VariableDeclaration", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
memberVariable188: BinaryAssociation = BinaryAssociation(
    name="memberVariable188",
    ends={
        Property(name="ast_CallableElement190", type=ast_MemberVariableAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_MemberVariableAccess189", type=ast_CallableElement, multiplicity=Multiplicity(0, 1))
    }
)
body191: BinaryAssociation = BinaryAssociation(
    name="body191",
    ends={
        Property(name="ast_Compound", type=ast_AlgorithmExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_AlgorithmExpression", type=ast_Compound, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseStatement206: BinaryAssociation = BinaryAssociation(
    name="elseStatement206",
    ends={
        Property(name="ast_Statement208", type=ast_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_IfStatement207", type=ast_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition209: BinaryAssociation = BinaryAssociation(
    name="condition209",
    ends={
        Property(name="ast_Expression210", type=ast_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_WhileStatement", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body211: BinaryAssociation = BinaryAssociation(
    name="body211",
    ends={
        Property(name="ast_Statement213", type=ast_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_WhileStatement212", type=ast_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition214: BinaryAssociation = BinaryAssociation(
    name="condition214",
    ends={
        Property(name="ast_Expression215", type=ast_DoWhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_DoWhileStatement", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body216: BinaryAssociation = BinaryAssociation(
    name="body216",
    ends={
        Property(name="ast_Statement218", type=ast_DoWhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_DoWhileStatement217", type=ast_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
iterationVariable219: BinaryAssociation = BinaryAssociation(
    name="iterationVariable219",
    ends={
        Property(name="ast_IterationVariable220", type=ast_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ForStatement", type=ast_IterationVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition201: BinaryAssociation = BinaryAssociation(
    name="condition201",
    ends={
        Property(name="ast_Expression202", type=ast_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_IfStatement", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenStatement203: BinaryAssociation = BinaryAssociation(
    name="thenStatement203",
    ends={
        Property(name="ast_Statement205", type=ast_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_IfStatement204", type=ast_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression227: BinaryAssociation = BinaryAssociation(
    name="expression227",
    ends={
        Property(name="ast_Expression228", type=ast_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ReturnStatement", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
collectionExpression221: BinaryAssociation = BinaryAssociation(
    name="collectionExpression221",
    ends={
        Property(name="ast_Expression223", type=ast_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ForStatement222", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body224: BinaryAssociation = BinaryAssociation(
    name="body224",
    ends={
        Property(name="ast_Statement226", type=ast_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ast_ForStatement225", type=ast_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_ast_EnumerationDefinition_DataTypeDefinition = Generalization(general=DataTypeDefinition, specific=ast_EnumerationDefinition)
gen_ast_TypeAliasDefinition_DataTypeDefinition = Generalization(general=DataTypeDefinition, specific=ast_TypeAliasDefinition)
gen_ast_RecordDefinition_DataTypeDefinition = Generalization(general=DataTypeDefinition, specific=ast_RecordDefinition)
gen_ast_FunctionDefinition_Definition = Generalization(general=Definition, specific=ast_FunctionDefinition)
gen_ast_FunctionDefinition_CallableElement = Generalization(general=CallableElement, specific=ast_FunctionDefinition)
gen_ast_DataTypeDefinition_Definition = Generalization(general=Definition, specific=ast_DataTypeDefinition)
gen_ast_ParameterDeclaration_CallableElement = Generalization(general=CallableElement, specific=ast_ParameterDeclaration)
gen_ast_TemplateParameterDeclaration_ParameterDeclaration = Generalization(general=ParameterDeclaration, specific=ast_TemplateParameterDeclaration)
gen_ast_InputParameterDeclaration_ParameterDeclaration = Generalization(general=ParameterDeclaration, specific=ast_InputParameterDeclaration)
gen_ast_OutputParameterDeclaration_ParameterDeclaration = Generalization(general=ParameterDeclaration, specific=ast_OutputParameterDeclaration)
gen_ast_StateVariableDeclaration_CallableElement = Generalization(general=CallableElement, specific=ast_StateVariableDeclaration)
gen_ast_FunctionObjectDeclaration_CallableElement = Generalization(general=CallableElement, specific=ast_FunctionObjectDeclaration)
gen_ast_LetExpressionVariableDeclarationPart_CallableElement = Generalization(general=CallableElement, specific=ast_LetExpressionVariableDeclarationPart)
gen_ast_IfExpression_Expression = Generalization(general=Expression, specific=ast_IfExpression)
gen_ast_LetExpression_Expression = Generalization(general=Expression, specific=ast_LetExpression)
gen_ast_SwitchExpression_Expression = Generalization(general=Expression, specific=ast_SwitchExpression)
gen_ast_ArrayElementAccess_Expression = Generalization(general=Expression, specific=ast_ArrayElementAccess)
gen_ast_IterationCall_Expression = Generalization(general=Expression, specific=ast_IterationCall)
gen_ast_IterationVariable_CallableElement = Generalization(general=CallableElement, specific=ast_IterationVariable)
gen_ast_IterationAccumulator_CallableElement = Generalization(general=CallableElement, specific=ast_IterationAccumulator)
gen_ast_DerivativeOperator_Expression = Generalization(general=Expression, specific=ast_DerivativeOperator)
gen_ast_ArrayConstructionOperator_Expression = Generalization(general=Expression, specific=ast_ArrayConstructionOperator)
gen_ast_ArrayConcatenationOperator_Expression = Generalization(general=Expression, specific=ast_ArrayConcatenationOperator)
gen_ast_UnitConstructionOperator_Expression = Generalization(general=Expression, specific=ast_UnitConstructionOperator)
gen_ast_ParenthesizedExpression_Expression = Generalization(general=Expression, specific=ast_ParenthesizedExpression)
gen_ast_EndExpression_Expression = Generalization(general=Expression, specific=ast_EndExpression)
gen_ast_LogicalOrExpression_Expression = Generalization(general=Expression, specific=ast_LogicalOrExpression)
gen_ast_LogicalAndExpression_Expression = Generalization(general=Expression, specific=ast_LogicalAndExpression)
gen_ast_EqualityExpression_Expression = Generalization(general=Expression, specific=ast_EqualityExpression)
gen_ast_RangeExpression_Expression = Generalization(general=Expression, specific=ast_RangeExpression)
gen_ast_ImpliesExpression_Expression = Generalization(general=Expression, specific=ast_ImpliesExpression)
gen_ast_RelationalExpression_Expression = Generalization(general=Expression, specific=ast_RelationalExpression)
gen_ast_TypeTestExpression_Expression = Generalization(general=Expression, specific=ast_TypeTestExpression)
gen_ast_AdditiveExpression_Expression = Generalization(general=Expression, specific=ast_AdditiveExpression)
gen_ast_MultiplicativeExpression_Expression = Generalization(general=Expression, specific=ast_MultiplicativeExpression)
gen_ast_PowerExpression_Expression = Generalization(general=Expression, specific=ast_PowerExpression)
gen_ast_UnaryExpression_Expression = Generalization(general=Expression, specific=ast_UnaryExpression)
gen_ast_FeatureCall_Expression = Generalization(general=Expression, specific=ast_FeatureCall)
gen_ast_VariableAccess_FeatureCall = Generalization(general=FeatureCall, specific=ast_VariableAccess)
gen_ast_RangeStepExpression_StepExpression = Generalization(general=StepExpression, specific=ast_RangeStepExpression)
gen_ast_AdditiveStepExpression_StepExpression = Generalization(general=StepExpression, specific=ast_AdditiveStepExpression)
gen_ast_PostfixExpression_Expression = Generalization(general=Expression, specific=ast_PostfixExpression)
gen_ast_NegateStepExpression_StepExpression = Generalization(general=StepExpression, specific=ast_NegateStepExpression)
gen_ast_PrimitiveStepExpression_StepExpression = Generalization(general=StepExpression, specific=ast_PrimitiveStepExpression)
gen_ast_StepLiteral_PrimitiveStepExpression = Generalization(general=PrimitiveStepExpression, specific=ast_StepLiteral)
gen_ast_StepN_PrimitiveStepExpression = Generalization(general=PrimitiveStepExpression, specific=ast_StepN)
gen_ast_FunctionCall_FeatureCall = Generalization(general=FeatureCall, specific=ast_FunctionCall)
gen_ast_MemberVariableAccess_Expression = Generalization(general=Expression, specific=ast_MemberVariableAccess)
gen_ast_Compound_Statement = Generalization(general=Statement, specific=ast_Compound)
gen_ast_Assignment_Statement = Generalization(general=Statement, specific=ast_Assignment)
gen_ast_VariableDeclaration_Statement = Generalization(general=Statement, specific=ast_VariableDeclaration)
gen_ast_IfStatement_Statement = Generalization(general=Statement, specific=ast_IfStatement)
gen_ast_AlgorithmExpression_Expression = Generalization(general=Expression, specific=ast_AlgorithmExpression)
gen_ast_WhileStatement_Statement = Generalization(general=Statement, specific=ast_WhileStatement)
gen_ast_DoWhileStatement_Statement = Generalization(general=Statement, specific=ast_DoWhileStatement)
gen_ast_ForStatement_Statement = Generalization(general=Statement, specific=ast_ForStatement)
gen_ast_BreakStatement_Statement = Generalization(general=Statement, specific=ast_BreakStatement)
gen_ast_ReturnStatement_Statement = Generalization(general=Statement, specific=ast_ReturnStatement)
gen_ast_BuiltinDefinition_Definition = Generalization(general=Definition, specific=ast_BuiltinDefinition)
gen_ast_BuiltinDefinition_CallableElement = Generalization(general=CallableElement, specific=ast_BuiltinDefinition)
gen_ast_BuiltinFunction_BuiltinDefinition = Generalization(general=BuiltinDefinition, specific=ast_BuiltinFunction)
gen_ast_BuiltinVariable_BuiltinDefinition = Generalization(general=BuiltinDefinition, specific=ast_BuiltinVariable)
gen_ast_ContinueStatement_Statement = Generalization(general=Statement, specific=ast_ContinueStatement)

# Domain Model
domain_model = DomainModel(
    name="ast",
    types={ast_Module, ast_Definition, ast_EnumerationDefinition, DataTypeDefinition, ast_EnumerationLiteralDeclaration, ast_TypeAliasDefinition, ast_PrimitiveType, ast_RecordDefinition, ast_RecordFieldDeclaration, ast_DataTypeSpecifier, ast_FunctionDefinition, CallableElement, ast_DataTypeDefinition, Definition, ast_OutputParameterDeclaration, ast_Check, ast_Assertion, ast_FunctionObjectDeclaration, ast_StateVariableDeclaration, ast_Equation, ast_TemplateParameterDeclaration, ast_InputParameterDeclaration, ast_CallableElement, ast_ParameterDeclaration, ParameterDeclaration, ast_Expression, ast_DataType, ast_LetExpressionVariableDeclarationPart, ast_IfExpression, ast_LetExpression, Expression, ast_LetExpressionVariableDeclaration, ast_SwitchCase, ast_SwitchExpression, ast_ArrayElementAccess, ast_ArraySubscript, ast_IterationCall, ast_DerivativeOperator, ast_ArrayConstructionOperator, ast_IterationVariable, ast_IterationAccumulator, ast_ArrayConcatenationOperator, ast_ExpressionList, ast_UnitConstructionOperator, ast_Unit, ast_ParenthesizedExpression, ast_EndExpression, ast_ArrayConstructionIterationClause, ast_LogicalOrExpression, ast_LogicalAndExpression, ast_EqualityExpression, ast_RangeExpression, ast_ImpliesExpression, ast_RelationalExpression, ast_TypeTestExpression, ast_AdditiveExpression, ast_MultiplicativeExpression, ast_PowerExpression, ast_UnaryExpression, ast_FeatureCall, ast_VariableAccess, FeatureCall, ast_StepExpression, ast_RangeStepExpression, StepExpression, ast_AdditiveStepExpression, ast_PostfixExpression, ast_NegateStepExpression, ast_PrimitiveStepExpression, ast_StepLiteral, PrimitiveStepExpression, ast_StepN, ast_FunctionCall, ast_MemberVariableAccess, Statement, ast_Statement, ast_Assignment, ast_VariableDeclaration, ast_IfStatement, ast_AlgorithmExpression, ast_Compound, ast_WhileStatement, ast_DoWhileStatement, ast_ForStatement, ast_BreakStatement, ast_ReturnStatement, ast_BuiltinDefinition, ast_BuiltinFunction, BuiltinDefinition, ast_BuiltinVariable, ast_ContinueStatement, FunctionKind, AssertionStatusKind, EqualityOperator, RelationalOperator, AdditiveOperator, UnaryOperator, PostfixOperator, MultiplicativeOperator, PowerOperator},
    associations={literalDeclarations1, type2, fieldDeclarations3, type4, definitions0, outputParameterDeclarations9, checks11, assertions12, functionObjectDeclarations14, stateVariableDeclarations16, equations18, templateParameterDeclarations6, inputParameterDeclarations7, inputParameterTypes22, outputParameterTypes25, function20, templateArguments21, functionName34, templateArguments37, leftHandSide40, rightHandSide43, condition28, variableDeclarations51, message31, targetExpression52, parts55, assignedExpression57, condition60, thenExpression62, type46, definedType48, cases70, defaultExpression72, caseExpression75, resultExpression78, elseExpression65, controlExpression68, array81, subscripts83, expression85, target88, breakCondition94, expression97, initializer100, variable103, variables90, accumulator92, collectionExpression108, rows111, expressions112, unit115, expressions116, expressions104, iterationClauses106, leftOperand120, rightOperand122, leftOperand125, rightOperand127, leftOperand130, rightOperand132, operands118, leftOperand140, rightOperand142, expression145, type147, leftOperand150, leftOperand135, rightOperand137, leftOperand155, rightOperand157, operand160, exponent162, rightOperand152, operand167, feature169, stepExpression171, start172, end174, operand165, operand182, arguments184, target186, leftOperand177, rightOperand179, statements192, target194, expression196, initializer199, memberVariable188, body191, elseStatement206, condition209, body211, condition214, body216, iterationVariable219, condition201, thenStatement203, expression227, collectionExpression221, body224},
    generalizations={gen_ast_EnumerationDefinition_DataTypeDefinition, gen_ast_TypeAliasDefinition_DataTypeDefinition, gen_ast_RecordDefinition_DataTypeDefinition, gen_ast_FunctionDefinition_Definition, gen_ast_FunctionDefinition_CallableElement, gen_ast_DataTypeDefinition_Definition, gen_ast_ParameterDeclaration_CallableElement, gen_ast_TemplateParameterDeclaration_ParameterDeclaration, gen_ast_InputParameterDeclaration_ParameterDeclaration, gen_ast_OutputParameterDeclaration_ParameterDeclaration, gen_ast_StateVariableDeclaration_CallableElement, gen_ast_FunctionObjectDeclaration_CallableElement, gen_ast_LetExpressionVariableDeclarationPart_CallableElement, gen_ast_IfExpression_Expression, gen_ast_LetExpression_Expression, gen_ast_SwitchExpression_Expression, gen_ast_ArrayElementAccess_Expression, gen_ast_IterationCall_Expression, gen_ast_IterationVariable_CallableElement, gen_ast_IterationAccumulator_CallableElement, gen_ast_DerivativeOperator_Expression, gen_ast_ArrayConstructionOperator_Expression, gen_ast_ArrayConcatenationOperator_Expression, gen_ast_UnitConstructionOperator_Expression, gen_ast_ParenthesizedExpression_Expression, gen_ast_EndExpression_Expression, gen_ast_LogicalOrExpression_Expression, gen_ast_LogicalAndExpression_Expression, gen_ast_EqualityExpression_Expression, gen_ast_RangeExpression_Expression, gen_ast_ImpliesExpression_Expression, gen_ast_RelationalExpression_Expression, gen_ast_TypeTestExpression_Expression, gen_ast_AdditiveExpression_Expression, gen_ast_MultiplicativeExpression_Expression, gen_ast_PowerExpression_Expression, gen_ast_UnaryExpression_Expression, gen_ast_FeatureCall_Expression, gen_ast_VariableAccess_FeatureCall, gen_ast_RangeStepExpression_StepExpression, gen_ast_AdditiveStepExpression_StepExpression, gen_ast_PostfixExpression_Expression, gen_ast_NegateStepExpression_StepExpression, gen_ast_PrimitiveStepExpression_StepExpression, gen_ast_StepLiteral_PrimitiveStepExpression, gen_ast_StepN_PrimitiveStepExpression, gen_ast_FunctionCall_FeatureCall, gen_ast_MemberVariableAccess_Expression, gen_ast_Compound_Statement, gen_ast_Assignment_Statement, gen_ast_VariableDeclaration_Statement, gen_ast_IfStatement_Statement, gen_ast_AlgorithmExpression_Expression, gen_ast_WhileStatement_Statement, gen_ast_DoWhileStatement_Statement, gen_ast_ForStatement_Statement, gen_ast_BreakStatement_Statement, gen_ast_ReturnStatement_Statement, gen_ast_BuiltinDefinition_Definition, gen_ast_BuiltinDefinition_CallableElement, gen_ast_BuiltinFunction_BuiltinDefinition, gen_ast_BuiltinVariable_BuiltinDefinition, gen_ast_ContinueStatement_Statement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)