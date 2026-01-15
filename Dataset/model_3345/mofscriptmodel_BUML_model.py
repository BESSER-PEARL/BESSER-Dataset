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
ImportType: Enumeration = Enumeration(
    name="ImportType",
    literals={
            EnumerationLiteral(name="LIBRARY"),
			EnumerationLiteral(name="TRANSFORMATION")
    }
)

ImportSemantics: Enumeration = Enumeration(
    name="ImportSemantics",
    literals={
            EnumerationLiteral(name="ACCESS"),
			EnumerationLiteral(name="IMPORT")
    }
)

AssignmentOperator: Enumeration = Enumeration(
    name="AssignmentOperator",
    literals={
            EnumerationLiteral(name="EQ"),
			EnumerationLiteral(name="PLUS_EQ")
    }
)

ParameterDirection: Enumeration = Enumeration(
    name="ParameterDirection",
    literals={
            EnumerationLiteral(name="IN"),
			EnumerationLiteral(name="OUT"),
			EnumerationLiteral(name="INOUT")
    }
)

AccessLevel: Enumeration = Enumeration(
    name="AccessLevel",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="PUBLIC"),
			EnumerationLiteral(name="PROTECTED"),
			EnumerationLiteral(name="PRIVATE")
    }
)

LogicalOperator: Enumeration = Enumeration(
    name="LogicalOperator",
    literals={
            EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="NOT"),
			EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="AND")
    }
)

LiteralType: Enumeration = Enumeration(
    name="LiteralType",
    literals={
            EnumerationLiteral(name="STRING"),
			EnumerationLiteral(name="INTEGER"),
			EnumerationLiteral(name="BOOLEAN"),
			EnumerationLiteral(name="REAL"),
			EnumerationLiteral(name="NULL")
    }
)

ArithmeticOperator: Enumeration = Enumeration(
    name="ArithmeticOperator",
    literals={
            EnumerationLiteral(name="PLUS"),
			EnumerationLiteral(name="MINUS"),
			EnumerationLiteral(name="MULT"),
			EnumerationLiteral(name="DIV")
    }
)

ComparisonOperator: Enumeration = Enumeration(
    name="ComparisonOperator",
    literals={
            EnumerationLiteral(name="EQ"),
			EnumerationLiteral(name="LT"),
			EnumerationLiteral(name="GT"),
			EnumerationLiteral(name="LE"),
			EnumerationLiteral(name="GE"),
			EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="NE")
    }
)

AdviceOperator: Enumeration = Enumeration(
    name="AdviceOperator",
    literals={
            EnumerationLiteral(name="BEFORE"),
			EnumerationLiteral(name="AFTER"),
			EnumerationLiteral(name="AROUND")
    }
)

PointCutOperator: Enumeration = Enumeration(
    name="PointCutOperator",
    literals={
            EnumerationLiteral(name="EXECUTE"),
			EnumerationLiteral(name="TARGET"),
			EnumerationLiteral(name="CALL")
    }
)

PointCutCombinationOperator: Enumeration = Enumeration(
    name="PointCutCombinationOperator",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="XOR"),
			EnumerationLiteral(name="NONE")
    }
)

# Classes
MOFScriptModel_TransformationRule = Class(name="MOFScriptModel::TransformationRule")
MOFScriptStatementOwner = Class(name="MOFScriptStatementOwner")
MOFScriptModel_StatementBlock = Class(name="MOFScriptModel::StatementBlock")
MOFScriptModel_MOFScriptObject = Class(name="MOFScriptModel::MOFScriptObject", is_abstract=True)
MOFScriptModel_MOFScriptComment = Class(name="MOFScriptModel::MOFScriptComment")
MOFScriptModel_MOFScriptTransformation = Class(name="MOFScriptModel::MOFScriptTransformation")
MOFScriptModel_MOFScriptParameter = Class(name="MOFScriptModel::MOFScriptParameter")
MOFScriptModel_MOFScriptStatementOwner = Class(name="MOFScriptModel::MOFScriptStatementOwner", is_abstract=True)
MOFScriptObject = Class(name="MOFScriptObject")
MOFScriptModel_MOFScriptStatement = Class(name="MOFScriptModel::MOFScriptStatement", is_abstract=True)
MOFScriptModel_VariableDeclaration = Class(name="MOFScriptModel::VariableDeclaration")
MOFScriptModel_Expression = Class(name="MOFScriptModel::Expression", is_abstract=True)
MOFScriptModel_ValueExpression = Class(name="MOFScriptModel::ValueExpression")
Expression = Class(name="Expression")
MOFScriptModel_IteratorStatement = Class(name="MOFScriptModel::IteratorStatement")
MOFScriptStatement = Class(name="MOFScriptStatement")
MOFScriptModel_MOFScriptImport = Class(name="MOFScriptModel::MOFScriptImport")
ValueExpression = Class(name="ValueExpression")
MOFScriptModel_FunctionCall = Class(name="MOFScriptModel::FunctionCall")
SimpleExpression = Class(name="SimpleExpression")
MOFScriptModel_SimpleExpression = Class(name="MOFScriptModel::SimpleExpression")
MOFScriptModel_LogicalExpression = Class(name="MOFScriptModel::LogicalExpression")
MOFScriptModel_GeneralAssignment = Class(name="MOFScriptModel::GeneralAssignment")
MOFScriptModel_CreateStatement = Class(name="MOFScriptModel::CreateStatement")
MOFScriptModel_ResultAssignment = Class(name="MOFScriptModel::ResultAssignment")
MOFScriptModel_ArithmeticExpression = Class(name="MOFScriptModel::ArithmeticExpression")
MOFScriptModel_Literal = Class(name="MOFScriptModel::Literal")
MOFScriptModel_Reference = Class(name="MOFScriptModel::Reference")
MOFScriptModel_FunctionCallStatement = Class(name="MOFScriptModel::FunctionCallStatement")
MOFScriptModel_PrintStatement = Class(name="MOFScriptModel::PrintStatement")
MOFScriptModel_IfStatement = Class(name="MOFScriptModel::IfStatement")
MOFScriptModel_FileStatement = Class(name="MOFScriptModel::FileStatement")
MOFScriptModel_ComparisonExpression = Class(name="MOFScriptModel::ComparisonExpression")
MOFScriptModel_Advice = Class(name="MOFScriptModel::Advice")
MOFScriptModel_PointCut = Class(name="MOFScriptModel::PointCut")
MOFScriptModel_MOFScriptSpecification = Class(name="MOFScriptModel::MOFScriptSpecification")
MOFScriptModel_BreakStatement = Class(name="MOFScriptModel::BreakStatement")
MOFScriptModel_WhileStatement = Class(name="MOFScriptModel::WhileStatement")
MOFScriptModel_MOFScriptAspect = Class(name="MOFScriptModel::MOFScriptAspect")
MOFScriptTransformation = Class(name="MOFScriptTransformation")
MOFScriptModel_PointCutExpression = Class(name="MOFScriptModel::PointCutExpression")
MOFScriptModel_SelectExpression = Class(name="MOFScriptModel::SelectExpression")
MOFScriptModel_ReturnStatement = Class(name="MOFScriptModel::ReturnStatement")
MOFScriptModel_VariableDeclarationStatement = Class(name="MOFScriptModel::VariableDeclarationStatement")
MOFScriptModel_CreateExpression = Class(name="MOFScriptModel::CreateExpression")
MOFScriptModel_CreateExpressionParameter = Class(name="MOFScriptModel::CreateExpressionParameter")
MOFScriptModel_DebugStatement = Class(name="MOFScriptModel::DebugStatement")
MOFScriptModel_Trace = Class(name="MOFScriptModel::Trace", is_abstract=True)
MOFScriptModel_M2MTrace = Class(name="MOFScriptModel::M2MTrace")
Trace = Class(name="Trace")

# MOFScriptModel_TransformationRule class attributes and methods
MOFScriptModel_TransformationRule_isEntryPoint: Property = Property(name="isEntryPoint", type=BooleanType)
MOFScriptModel_TransformationRule_name: Property = Property(name="name", type=StringType)
MOFScriptModel_TransformationRule_return: Property = Property(name="return", type=StringType)
MOFScriptModel_TransformationRule_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
MOFScriptModel_TransformationRule_accessLevel: Property = Property(name="accessLevel", type=StringType)
MOFScriptModel_TransformationRule.attributes={MOFScriptModel_TransformationRule_name, MOFScriptModel_TransformationRule_isEntryPoint, MOFScriptModel_TransformationRule_accessLevel, MOFScriptModel_TransformationRule_return, MOFScriptModel_TransformationRule_isAbstract}

# MOFScriptStatementOwner class attributes and methods

# MOFScriptModel_StatementBlock class attributes and methods
MOFScriptModel_StatementBlock_id: Property = Property(name="id", type=StringType)
MOFScriptModel_StatementBlock_reference: Property = Property(name="reference", type=StringType)
MOFScriptModel_StatementBlock_protected: Property = Property(name="protected", type=BooleanType)
MOFScriptModel_StatementBlock.attributes={MOFScriptModel_StatementBlock_id, MOFScriptModel_StatementBlock_protected, MOFScriptModel_StatementBlock_reference}

# MOFScriptModel_MOFScriptObject class attributes and methods
MOFScriptModel_MOFScriptObject_line: Property = Property(name="line", type=IntegerType)
MOFScriptModel_MOFScriptObject_column: Property = Property(name="column", type=IntegerType)
MOFScriptModel_MOFScriptObject.attributes={MOFScriptModel_MOFScriptObject_line, MOFScriptModel_MOFScriptObject_column}

# MOFScriptModel_MOFScriptComment class attributes and methods
MOFScriptModel_MOFScriptComment_commentText: Property = Property(name="commentText", type=StringType)
MOFScriptModel_MOFScriptComment_singleLine: Property = Property(name="singleLine", type=BooleanType)
MOFScriptModel_MOFScriptComment_docStyle: Property = Property(name="docStyle", type=BooleanType)
MOFScriptModel_MOFScriptComment.attributes={MOFScriptModel_MOFScriptComment_commentText, MOFScriptModel_MOFScriptComment_docStyle, MOFScriptModel_MOFScriptComment_singleLine}

# MOFScriptModel_MOFScriptTransformation class attributes and methods
MOFScriptModel_MOFScriptTransformation_name: Property = Property(name="name", type=StringType)
MOFScriptModel_MOFScriptTransformation_extendsName: Property = Property(name="extendsName", type=StringType)
MOFScriptModel_MOFScriptTransformation.attributes={MOFScriptModel_MOFScriptTransformation_name, MOFScriptModel_MOFScriptTransformation_extendsName}

# MOFScriptModel_MOFScriptParameter class attributes and methods
MOFScriptModel_MOFScriptParameter_name: Property = Property(name="name", type=StringType)
MOFScriptModel_MOFScriptParameter_type: Property = Property(name="type", type=StringType)
MOFScriptModel_MOFScriptParameter_direction: Property = Property(name="direction", type=StringType)
MOFScriptModel_MOFScriptParameter_typePrefix: Property = Property(name="typePrefix", type=StringType)
MOFScriptModel_MOFScriptParameter.attributes={MOFScriptModel_MOFScriptParameter_type, MOFScriptModel_MOFScriptParameter_direction, MOFScriptModel_MOFScriptParameter_name, MOFScriptModel_MOFScriptParameter_typePrefix}

# MOFScriptModel_MOFScriptStatementOwner class attributes and methods

# MOFScriptObject class attributes and methods

# MOFScriptModel_MOFScriptStatement class attributes and methods

# MOFScriptModel_VariableDeclaration class attributes and methods
MOFScriptModel_VariableDeclaration_name: Property = Property(name="name", type=StringType)
MOFScriptModel_VariableDeclaration_type: Property = Property(name="type", type=StringType)
MOFScriptModel_VariableDeclaration_constant: Property = Property(name="constant", type=BooleanType)
MOFScriptModel_VariableDeclaration.attributes={MOFScriptModel_VariableDeclaration_name, MOFScriptModel_VariableDeclaration_type, MOFScriptModel_VariableDeclaration_constant}

# MOFScriptModel_Expression class attributes and methods

# MOFScriptModel_ValueExpression class attributes and methods
MOFScriptModel_ValueExpression_specification: Property = Property(name="specification", type=StringType)
MOFScriptModel_ValueExpression.attributes={MOFScriptModel_ValueExpression_specification}

# Expression class attributes and methods

# MOFScriptModel_IteratorStatement class attributes and methods
MOFScriptModel_IteratorStatement_type: Property = Property(name="type", type=StringType)
MOFScriptModel_IteratorStatement_variable: Property = Property(name="variable", type=StringType)
MOFScriptModel_IteratorStatement.attributes={MOFScriptModel_IteratorStatement_type, MOFScriptModel_IteratorStatement_variable}

# MOFScriptStatement class attributes and methods

# MOFScriptModel_MOFScriptImport class attributes and methods
MOFScriptModel_MOFScriptImport_type: Property = Property(name="type", type=StringType)
MOFScriptModel_MOFScriptImport_uri: Property = Property(name="uri", type=StringType)
MOFScriptModel_MOFScriptImport_importSemantics: Property = Property(name="importSemantics", type=StringType)
MOFScriptModel_MOFScriptImport_name: Property = Property(name="name", type=StringType)
MOFScriptModel_MOFScriptImport.attributes={MOFScriptModel_MOFScriptImport_uri, MOFScriptModel_MOFScriptImport_importSemantics, MOFScriptModel_MOFScriptImport_name, MOFScriptModel_MOFScriptImport_type}

# ValueExpression class attributes and methods

# MOFScriptModel_FunctionCall class attributes and methods
MOFScriptModel_FunctionCall_name: Property = Property(name="name", type=StringType)
MOFScriptModel_FunctionCall_isSuperCall: Property = Property(name="isSuperCall", type=BooleanType)
MOFScriptModel_FunctionCall_transformationContext: Property = Property(name="transformationContext", type=StringType)
MOFScriptModel_FunctionCall.attributes={MOFScriptModel_FunctionCall_isSuperCall, MOFScriptModel_FunctionCall_transformationContext, MOFScriptModel_FunctionCall_name}

# SimpleExpression class attributes and methods

# MOFScriptModel_SimpleExpression class attributes and methods

# MOFScriptModel_LogicalExpression class attributes and methods
MOFScriptModel_LogicalExpression_operator: Property = Property(name="operator", type=StringType)
MOFScriptModel_LogicalExpression.attributes={MOFScriptModel_LogicalExpression_operator}

# MOFScriptModel_GeneralAssignment class attributes and methods
MOFScriptModel_GeneralAssignment_name: Property = Property(name="name", type=StringType)
MOFScriptModel_GeneralAssignment_operator: Property = Property(name="operator", type=StringType)
MOFScriptModel_GeneralAssignment.attributes={MOFScriptModel_GeneralAssignment_operator, MOFScriptModel_GeneralAssignment_name}

# MOFScriptModel_CreateStatement class attributes and methods
MOFScriptModel_CreateStatement_type: Property = Property(name="type", type=StringType)
MOFScriptModel_CreateStatement_name: Property = Property(name="name", type=StringType)
MOFScriptModel_CreateStatement.attributes={MOFScriptModel_CreateStatement_type, MOFScriptModel_CreateStatement_name}

# MOFScriptModel_ResultAssignment class attributes and methods
MOFScriptModel_ResultAssignment_resultPart: Property = Property(name="resultPart", type=StringType)
MOFScriptModel_ResultAssignment_operator: Property = Property(name="operator", type=StringType)
MOFScriptModel_ResultAssignment.attributes={MOFScriptModel_ResultAssignment_resultPart, MOFScriptModel_ResultAssignment_operator}

# MOFScriptModel_ArithmeticExpression class attributes and methods
MOFScriptModel_ArithmeticExpression_operator: Property = Property(name="operator", type=StringType)
MOFScriptModel_ArithmeticExpression.attributes={MOFScriptModel_ArithmeticExpression_operator}

# MOFScriptModel_Literal class attributes and methods
MOFScriptModel_Literal_type: Property = Property(name="type", type=StringType)
MOFScriptModel_Literal_value: Property = Property(name="value", type=StringType)
MOFScriptModel_Literal.attributes={MOFScriptModel_Literal_type, MOFScriptModel_Literal_value}

# MOFScriptModel_Reference class attributes and methods
MOFScriptModel_Reference_name: Property = Property(name="name", type=StringType)
MOFScriptModel_Reference.attributes={MOFScriptModel_Reference_name}

# MOFScriptModel_FunctionCallStatement class attributes and methods

# MOFScriptModel_PrintStatement class attributes and methods
MOFScriptModel_PrintStatement_context: Property = Property(name="context", type=StringType)
MOFScriptModel_PrintStatement_printCommand: Property = Property(name="printCommand", type=StringType)
MOFScriptModel_PrintStatement.attributes={MOFScriptModel_PrintStatement_context, MOFScriptModel_PrintStatement_printCommand}

# MOFScriptModel_IfStatement class attributes and methods

# MOFScriptModel_FileStatement class attributes and methods
MOFScriptModel_FileStatement_fileReference: Property = Property(name="fileReference", type=StringType)
MOFScriptModel_FileStatement_use: Property = Property(name="use", type=BooleanType)
MOFScriptModel_FileStatement_append: Property = Property(name="append", type=BooleanType)
MOFScriptModel_FileStatement.attributes={MOFScriptModel_FileStatement_fileReference, MOFScriptModel_FileStatement_use, MOFScriptModel_FileStatement_append}

# MOFScriptModel_ComparisonExpression class attributes and methods
MOFScriptModel_ComparisonExpression_operator: Property = Property(name="operator", type=StringType)
MOFScriptModel_ComparisonExpression.attributes={MOFScriptModel_ComparisonExpression_operator}

# MOFScriptModel_Advice class attributes and methods
MOFScriptModel_Advice_name: Property = Property(name="name", type=StringType)
MOFScriptModel_Advice_code: Property = Property(name="code", type=StringType)
MOFScriptModel_Advice_operator: Property = Property(name="operator", type=StringType)
MOFScriptModel_Advice_pointCutRef: Property = Property(name="pointCutRef", type=StringType)
MOFScriptModel_Advice.attributes={MOFScriptModel_Advice_pointCutRef, MOFScriptModel_Advice_code, MOFScriptModel_Advice_name, MOFScriptModel_Advice_operator}

# MOFScriptModel_PointCut class attributes and methods
MOFScriptModel_PointCut_typeMatch: Property = Property(name="typeMatch", type=StringType)
MOFScriptModel_PointCut_name: Property = Property(name="name", type=StringType)
MOFScriptModel_PointCut.attributes={MOFScriptModel_PointCut_typeMatch, MOFScriptModel_PointCut_name}

# MOFScriptModel_MOFScriptSpecification class attributes and methods

# MOFScriptModel_BreakStatement class attributes and methods

# MOFScriptModel_WhileStatement class attributes and methods

# MOFScriptModel_MOFScriptAspect class attributes and methods

# MOFScriptTransformation class attributes and methods

# MOFScriptModel_PointCutExpression class attributes and methods
MOFScriptModel_PointCutExpression_expressionString: Property = Property(name="expressionString", type=StringType)
MOFScriptModel_PointCutExpression_operator: Property = Property(name="operator", type=StringType)
MOFScriptModel_PointCutExpression_combinationOperator: Property = Property(name="combinationOperator", type=StringType)
MOFScriptModel_PointCutExpression.attributes={MOFScriptModel_PointCutExpression_operator, MOFScriptModel_PointCutExpression_expressionString, MOFScriptModel_PointCutExpression_combinationOperator}

# MOFScriptModel_SelectExpression class attributes and methods
MOFScriptModel_SelectExpression_variable: Property = Property(name="variable", type=StringType)
MOFScriptModel_SelectExpression_type: Property = Property(name="type", type=StringType)
MOFScriptModel_SelectExpression.attributes={MOFScriptModel_SelectExpression_variable, MOFScriptModel_SelectExpression_type}

# MOFScriptModel_ReturnStatement class attributes and methods

# MOFScriptModel_VariableDeclarationStatement class attributes and methods

# MOFScriptModel_CreateExpression class attributes and methods
MOFScriptModel_CreateExpression_type: Property = Property(name="type", type=StringType)
MOFScriptModel_CreateExpression.attributes={MOFScriptModel_CreateExpression_type}

# MOFScriptModel_CreateExpressionParameter class attributes and methods
MOFScriptModel_CreateExpressionParameter_name: Property = Property(name="name", type=StringType)
MOFScriptModel_CreateExpressionParameter.attributes={MOFScriptModel_CreateExpressionParameter_name}

# MOFScriptModel_DebugStatement class attributes and methods
MOFScriptModel_DebugStatement_specification: Property = Property(name="specification", type=StringType)
MOFScriptModel_DebugStatement_vars: Property = Property(name="vars", type=StringType)
MOFScriptModel_DebugStatement.attributes={MOFScriptModel_DebugStatement_specification, MOFScriptModel_DebugStatement_vars}

# MOFScriptModel_Trace class attributes and methods

# MOFScriptModel_M2MTrace class attributes and methods
MOFScriptModel_M2MTrace_name: Property = Property(name="name", type=StringType)
MOFScriptModel_M2MTrace_id: Property = Property(name="id", type=StringType)
MOFScriptModel_M2MTrace.attributes={MOFScriptModel_M2MTrace_id, MOFScriptModel_M2MTrace_name}

# Trace class attributes and methods

# Relationships
variables9: BinaryAssociation = BinaryAssociation(
    name="variables9",
    ends={
        Property(name="MOFScriptModel_VariableDeclaration", type=MOFScriptModel_MOFScriptStatementOwner, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_MOFScriptStatementOwner", type=MOFScriptModel_VariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blocks10: BinaryAssociation = BinaryAssociation(
    name="blocks10",
    ends={
        Property(name="MOFScriptModel_StatementBlock", type=MOFScriptModel_MOFScriptStatementOwner, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_MOFScriptStatementOwner11", type=MOFScriptModel_StatementBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
comment12: BinaryAssociation = BinaryAssociation(
    name="comment12",
    ends={
        Property(name="MOFScriptModel_MOFScriptComment", type=MOFScriptModel_MOFScriptObject, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_MOFScriptObject", type=MOFScriptModel_MOFScriptComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner0: BinaryAssociation = BinaryAssociation(
    name="owner0",
    ends={
        Property(name="MOFScriptTransformation", type=MOFScriptModel_TransformationRule, multiplicity=Multiplicity(1, 1)),
        Property(name="transformationrules", type=MOFScriptModel_MOFScriptTransformation, multiplicity=Multiplicity(0, 1))
    }
)
extends2: BinaryAssociation = BinaryAssociation(
    name="extends2",
    ends={
        Property(name="MOFScriptModel_TransformationRule", type=MOFScriptModel_TransformationRule, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_TransformationRule1", type=MOFScriptModel_TransformationRule, multiplicity=Multiplicity(0, 1))
    }
)
parameters3: BinaryAssociation = BinaryAssociation(
    name="parameters3",
    ends={
        Property(name="MOFScriptModel_MOFScriptParameter", type=MOFScriptModel_TransformationRule, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_TransformationRule4", type=MOFScriptModel_MOFScriptParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
context5: BinaryAssociation = BinaryAssociation(
    name="context5",
    ends={
        Property(name="MOFScriptModel_MOFScriptParameter7", type=MOFScriptModel_TransformationRule, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_TransformationRule6", type=MOFScriptModel_MOFScriptParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements8: BinaryAssociation = BinaryAssociation(
    name="statements8",
    ends={
        Property(name="MOFScriptStatement", type=MOFScriptModel_MOFScriptStatementOwner, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=MOFScriptModel_MOFScriptStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables18: BinaryAssociation = BinaryAssociation(
    name="variables18",
    ends={
        Property(name="MOFScriptModel_VariableDeclaration19", type=MOFScriptModel_MOFScriptTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_MOFScriptTransformation", type=MOFScriptModel_VariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constants20: BinaryAssociation = BinaryAssociation(
    name="constants20",
    ends={
        Property(name="MOFScriptModel_VariableDeclaration22", type=MOFScriptModel_MOFScriptTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_MOFScriptTransformation21", type=MOFScriptModel_VariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters23: BinaryAssociation = BinaryAssociation(
    name="parameters23",
    ends={
        Property(name="MOFScriptModel_MOFScriptParameter25", type=MOFScriptModel_MOFScriptTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_MOFScriptTransformation24", type=MOFScriptModel_MOFScriptParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner13: BinaryAssociation = BinaryAssociation(
    name="owner13",
    ends={
        Property(name="MOFScriptStatementOwner", type=MOFScriptModel_MOFScriptStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="statements", type=MOFScriptModel_MOFScriptStatementOwner, multiplicity=Multiplicity(0, 1))
    }
)
value14: BinaryAssociation = BinaryAssociation(
    name="value14",
    ends={
        Property(name="MOFScriptModel_Expression", type=MOFScriptModel_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_VariableDeclaration15", type=MOFScriptModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements16: BinaryAssociation = BinaryAssociation(
    name="statements16",
    ends={
        Property(name="MOFScriptModel_MOFScriptStatement", type=MOFScriptModel_StatementBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_StatementBlock17", type=MOFScriptModel_MOFScriptStatement, multiplicity=Multiplicity(0, 9999))
    }
)
extends27: BinaryAssociation = BinaryAssociation(
    name="extends27",
    ends={
        Property(name="MOFScriptModel_MOFScriptTransformation28", type=MOFScriptModel_MOFScriptTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_MOFScriptTransformation26", type=MOFScriptModel_MOFScriptTransformation, multiplicity=Multiplicity(0, 1))
    }
)
transformationrules29: BinaryAssociation = BinaryAssociation(
    name="transformationrules29",
    ends={
        Property(name="TransformationRule", type=MOFScriptModel_MOFScriptTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="owner30", type=MOFScriptModel_TransformationRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
additionalExpressionPart49: BinaryAssociation = BinaryAssociation(
    name="additionalExpressionPart49",
    ends={
        Property(name="MOFScriptModel_SimpleExpression50", type=MOFScriptModel_SimpleExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_SimpleExpression48", type=MOFScriptModel_SimpleExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters51: BinaryAssociation = BinaryAssociation(
    name="parameters51",
    ends={
        Property(name="MOFScriptModel_ValueExpression52", type=MOFScriptModel_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_FunctionCall", type=MOFScriptModel_ValueExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
filterExpression31: BinaryAssociation = BinaryAssociation(
    name="filterExpression31",
    ends={
        Property(name="MOFScriptModel_Expression32", type=MOFScriptModel_IteratorStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_IteratorStatement", type=MOFScriptModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source33: BinaryAssociation = BinaryAssociation(
    name="source33",
    ends={
        Property(name="MOFScriptModel_SimpleExpression", type=MOFScriptModel_IteratorStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_IteratorStatement34", type=MOFScriptModel_SimpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
before35: BinaryAssociation = BinaryAssociation(
    name="before35",
    ends={
        Property(name="MOFScriptModel_ValueExpression", type=MOFScriptModel_IteratorStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_IteratorStatement36", type=MOFScriptModel_ValueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
between37: BinaryAssociation = BinaryAssociation(
    name="between37",
    ends={
        Property(name="MOFScriptModel_ValueExpression39", type=MOFScriptModel_IteratorStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_IteratorStatement38", type=MOFScriptModel_ValueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
after40: BinaryAssociation = BinaryAssociation(
    name="after40",
    ends={
        Property(name="MOFScriptModel_ValueExpression42", type=MOFScriptModel_IteratorStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_IteratorStatement41", type=MOFScriptModel_ValueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
part143: BinaryAssociation = BinaryAssociation(
    name="part143",
    ends={
        Property(name="MOFScriptModel_Expression44", type=MOFScriptModel_LogicalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_LogicalExpression", type=MOFScriptModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
part245: BinaryAssociation = BinaryAssociation(
    name="part245",
    ends={
        Property(name="MOFScriptModel_Expression47", type=MOFScriptModel_LogicalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_LogicalExpression46", type=MOFScriptModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression56: BinaryAssociation = BinaryAssociation(
    name="expression56",
    ends={
        Property(name="MOFScriptModel_Expression57", type=MOFScriptModel_ResultAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_ResultAssignment", type=MOFScriptModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression58: BinaryAssociation = BinaryAssociation(
    name="expression58",
    ends={
        Property(name="MOFScriptModel_Expression59", type=MOFScriptModel_GeneralAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_GeneralAssignment", type=MOFScriptModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transformationRule53: BinaryAssociation = BinaryAssociation(
    name="transformationRule53",
    ends={
        Property(name="MOFScriptModel_TransformationRule55", type=MOFScriptModel_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_FunctionCall54", type=MOFScriptModel_TransformationRule, multiplicity=Multiplicity(0, 1))
    }
)
part164: BinaryAssociation = BinaryAssociation(
    name="part164",
    ends={
        Property(name="MOFScriptModel_ValueExpression65", type=MOFScriptModel_ArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_ArithmeticExpression", type=MOFScriptModel_ValueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function60: BinaryAssociation = BinaryAssociation(
    name="function60",
    ends={
        Property(name="MOFScriptModel_FunctionCall61", type=MOFScriptModel_FunctionCallStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_FunctionCallStatement", type=MOFScriptModel_FunctionCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
printBody62: BinaryAssociation = BinaryAssociation(
    name="printBody62",
    ends={
        Property(name="MOFScriptModel_ValueExpression63", type=MOFScriptModel_PrintStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_PrintStatement", type=MOFScriptModel_ValueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
part271: BinaryAssociation = BinaryAssociation(
    name="part271",
    ends={
        Property(name="MOFScriptModel_ValueExpression72", type=MOFScriptModel_ComparisonExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_ComparisonExpression", type=MOFScriptModel_ValueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
part173: BinaryAssociation = BinaryAssociation(
    name="part173",
    ends={
        Property(name="MOFScriptModel_ValueExpression75", type=MOFScriptModel_ComparisonExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_ComparisonExpression74", type=MOFScriptModel_ValueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
part266: BinaryAssociation = BinaryAssociation(
    name="part266",
    ends={
        Property(name="MOFScriptModel_ValueExpression68", type=MOFScriptModel_ArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_ArithmeticExpression67", type=MOFScriptModel_ValueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fileURI69: BinaryAssociation = BinaryAssociation(
    name="fileURI69",
    ends={
        Property(name="MOFScriptModel_ValueExpression70", type=MOFScriptModel_FileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_FileStatement", type=MOFScriptModel_ValueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
advice87: BinaryAssociation = BinaryAssociation(
    name="advice87",
    ends={
        Property(name="MOFScriptModel_Advice", type=MOFScriptModel_MOFScriptAspect, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_MOFScriptAspect", type=MOFScriptModel_Advice, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pointcut88: BinaryAssociation = BinaryAssociation(
    name="pointcut88",
    ends={
        Property(name="MOFScriptModel_PointCut", type=MOFScriptModel_MOFScriptAspect, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_MOFScriptAspect89", type=MOFScriptModel_PointCut, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ifExpression76: BinaryAssociation = BinaryAssociation(
    name="ifExpression76",
    ends={
        Property(name="MOFScriptModel_Expression77", type=MOFScriptModel_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_IfStatement", type=MOFScriptModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseBranch79: BinaryAssociation = BinaryAssociation(
    name="elseBranch79",
    ends={
        Property(name="MOFScriptModel_IfStatement80", type=MOFScriptModel_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_IfStatement78", type=MOFScriptModel_IfStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transformation81: BinaryAssociation = BinaryAssociation(
    name="transformation81",
    ends={
        Property(name="MOFScriptModel_MOFScriptTransformation82", type=MOFScriptModel_MOFScriptSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_MOFScriptSpecification", type=MOFScriptModel_MOFScriptTransformation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports83: BinaryAssociation = BinaryAssociation(
    name="imports83",
    ends={
        Property(name="MOFScriptModel_MOFScriptImport", type=MOFScriptModel_MOFScriptSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_MOFScriptSpecification84", type=MOFScriptModel_MOFScriptImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition85: BinaryAssociation = BinaryAssociation(
    name="condition85",
    ends={
        Property(name="MOFScriptModel_Expression86", type=MOFScriptModel_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_WhileStatement", type=MOFScriptModel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
pointcutexpression93: BinaryAssociation = BinaryAssociation(
    name="pointcutexpression93",
    ends={
        Property(name="MOFScriptModel_PointCutExpression", type=MOFScriptModel_PointCut, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_PointCut94", type=MOFScriptModel_PointCutExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
pointcut90: BinaryAssociation = BinaryAssociation(
    name="pointcut90",
    ends={
        Property(name="MOFScriptModel_PointCut92", type=MOFScriptModel_Advice, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_Advice91", type=MOFScriptModel_PointCut, multiplicity=Multiplicity(0, 1))
    }
)
filterExpression98: BinaryAssociation = BinaryAssociation(
    name="filterExpression98",
    ends={
        Property(name="MOFScriptModel_Expression99", type=MOFScriptModel_SelectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_SelectExpression", type=MOFScriptModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sourceReference100: BinaryAssociation = BinaryAssociation(
    name="sourceReference100",
    ends={
        Property(name="MOFScriptModel_SimpleExpression102", type=MOFScriptModel_SelectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_SelectExpression101", type=MOFScriptModel_SimpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
combinedExpression96: BinaryAssociation = BinaryAssociation(
    name="combinedExpression96",
    ends={
        Property(name="MOFScriptModel_PointCutExpression97", type=MOFScriptModel_PointCutExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_PointCutExpression95", type=MOFScriptModel_PointCutExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression110: BinaryAssociation = BinaryAssociation(
    name="expression110",
    ends={
        Property(name="MOFScriptModel_Expression111", type=MOFScriptModel_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_ReturnStatement", type=MOFScriptModel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
appliedFunction103: BinaryAssociation = BinaryAssociation(
    name="appliedFunction103",
    ends={
        Property(name="MOFScriptModel_FunctionCall105", type=MOFScriptModel_SelectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_SelectExpression104", type=MOFScriptModel_FunctionCall, multiplicity=Multiplicity(0, 1))
    }
)
parameters106: BinaryAssociation = BinaryAssociation(
    name="parameters106",
    ends={
        Property(name="MOFScriptModel_CreateExpressionParameter", type=MOFScriptModel_CreateExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_CreateExpression", type=MOFScriptModel_CreateExpressionParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value107: BinaryAssociation = BinaryAssociation(
    name="value107",
    ends={
        Property(name="MOFScriptModel_ValueExpression109", type=MOFScriptModel_CreateExpressionParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_CreateExpressionParameter108", type=MOFScriptModel_ValueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable112: BinaryAssociation = BinaryAssociation(
    name="variable112",
    ends={
        Property(name="MOFScriptModel_VariableDeclaration113", type=MOFScriptModel_VariableDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_VariableDeclarationStatement", type=MOFScriptModel_VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
source114: BinaryAssociation = BinaryAssociation(
    name="source114",
    ends={
        Property(name="MOFScriptModel_Reference", type=MOFScriptModel_M2MTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_M2MTrace", type=MOFScriptModel_Reference, multiplicity=Multiplicity(0, 1))
    }
)
target115: BinaryAssociation = BinaryAssociation(
    name="target115",
    ends={
        Property(name="MOFScriptModel_Reference117", type=MOFScriptModel_M2MTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="MOFScriptModel_M2MTrace116", type=MOFScriptModel_Reference, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_MOFScriptModel_TransformationRule_MOFScriptStatementOwner = Generalization(general=MOFScriptStatementOwner, specific=MOFScriptModel_TransformationRule)
gen_MOFScriptModel_MOFScriptComment_MOFScriptObject = Generalization(general=MOFScriptObject, specific=MOFScriptModel_MOFScriptComment)
gen_MOFScriptModel_MOFScriptStatementOwner_MOFScriptObject = Generalization(general=MOFScriptObject, specific=MOFScriptModel_MOFScriptStatementOwner)
gen_MOFScriptModel_MOFScriptTransformation_MOFScriptObject = Generalization(general=MOFScriptObject, specific=MOFScriptModel_MOFScriptTransformation)
gen_MOFScriptModel_MOFScriptStatement_MOFScriptStatementOwner = Generalization(general=MOFScriptStatementOwner, specific=MOFScriptModel_MOFScriptStatement)
gen_MOFScriptModel_VariableDeclaration_MOFScriptObject = Generalization(general=MOFScriptObject, specific=MOFScriptModel_VariableDeclaration)
gen_MOFScriptModel_ValueExpression_Expression = Generalization(general=Expression, specific=MOFScriptModel_ValueExpression)
gen_MOFScriptModel_Expression_MOFScriptObject = Generalization(general=MOFScriptObject, specific=MOFScriptModel_Expression)
gen_MOFScriptModel_IteratorStatement_MOFScriptStatement = Generalization(general=MOFScriptStatement, specific=MOFScriptModel_IteratorStatement)
gen_MOFScriptModel_MOFScriptParameter_MOFScriptObject = Generalization(general=MOFScriptObject, specific=MOFScriptModel_MOFScriptParameter)
gen_MOFScriptModel_MOFScriptImport_MOFScriptObject = Generalization(general=MOFScriptObject, specific=MOFScriptModel_MOFScriptImport)
gen_MOFScriptModel_SimpleExpression_ValueExpression = Generalization(general=ValueExpression, specific=MOFScriptModel_SimpleExpression)
gen_MOFScriptModel_FunctionCall_SimpleExpression = Generalization(general=SimpleExpression, specific=MOFScriptModel_FunctionCall)
gen_MOFScriptModel_LogicalExpression_Expression = Generalization(general=Expression, specific=MOFScriptModel_LogicalExpression)
gen_MOFScriptModel_GeneralAssignment_MOFScriptStatement = Generalization(general=MOFScriptStatement, specific=MOFScriptModel_GeneralAssignment)
gen_MOFScriptModel_CreateStatement_MOFScriptStatement = Generalization(general=MOFScriptStatement, specific=MOFScriptModel_CreateStatement)
gen_MOFScriptModel_ResultAssignment_MOFScriptStatement = Generalization(general=MOFScriptStatement, specific=MOFScriptModel_ResultAssignment)
gen_MOFScriptModel_ArithmeticExpression_ValueExpression = Generalization(general=ValueExpression, specific=MOFScriptModel_ArithmeticExpression)
gen_MOFScriptModel_Literal_SimpleExpression = Generalization(general=SimpleExpression, specific=MOFScriptModel_Literal)
gen_MOFScriptModel_Reference_SimpleExpression = Generalization(general=SimpleExpression, specific=MOFScriptModel_Reference)
gen_MOFScriptModel_FunctionCallStatement_MOFScriptStatement = Generalization(general=MOFScriptStatement, specific=MOFScriptModel_FunctionCallStatement)
gen_MOFScriptModel_PrintStatement_MOFScriptStatement = Generalization(general=MOFScriptStatement, specific=MOFScriptModel_PrintStatement)
gen_MOFScriptModel_IfStatement_MOFScriptStatement = Generalization(general=MOFScriptStatement, specific=MOFScriptModel_IfStatement)
gen_MOFScriptModel_FileStatement_MOFScriptStatement = Generalization(general=MOFScriptStatement, specific=MOFScriptModel_FileStatement)
gen_MOFScriptModel_ComparisonExpression_Expression = Generalization(general=Expression, specific=MOFScriptModel_ComparisonExpression)
gen_MOFScriptModel_Advice_MOFScriptStatementOwner = Generalization(general=MOFScriptStatementOwner, specific=MOFScriptModel_Advice)
gen_MOFScriptModel_MOFScriptSpecification_MOFScriptObject = Generalization(general=MOFScriptObject, specific=MOFScriptModel_MOFScriptSpecification)
gen_MOFScriptModel_BreakStatement_MOFScriptStatement = Generalization(general=MOFScriptStatement, specific=MOFScriptModel_BreakStatement)
gen_MOFScriptModel_WhileStatement_MOFScriptStatement = Generalization(general=MOFScriptStatement, specific=MOFScriptModel_WhileStatement)
gen_MOFScriptModel_MOFScriptAspect_MOFScriptTransformation = Generalization(general=MOFScriptTransformation, specific=MOFScriptModel_MOFScriptAspect)
gen_MOFScriptModel_SelectExpression_ValueExpression = Generalization(general=ValueExpression, specific=MOFScriptModel_SelectExpression)
gen_MOFScriptModel_ReturnStatement_MOFScriptStatement = Generalization(general=MOFScriptStatement, specific=MOFScriptModel_ReturnStatement)
gen_MOFScriptModel_VariableDeclarationStatement_MOFScriptStatement = Generalization(general=MOFScriptStatement, specific=MOFScriptModel_VariableDeclarationStatement)
gen_MOFScriptModel_CreateExpression_Expression = Generalization(general=Expression, specific=MOFScriptModel_CreateExpression)
gen_MOFScriptModel_CreateExpressionParameter_MOFScriptObject = Generalization(general=MOFScriptObject, specific=MOFScriptModel_CreateExpressionParameter)
gen_MOFScriptModel_DebugStatement_MOFScriptStatement = Generalization(general=MOFScriptStatement, specific=MOFScriptModel_DebugStatement)
gen_MOFScriptModel_Trace_MOFScriptStatement = Generalization(general=MOFScriptStatement, specific=MOFScriptModel_Trace)
gen_MOFScriptModel_M2MTrace_Trace = Generalization(general=Trace, specific=MOFScriptModel_M2MTrace)

# Domain Model
domain_model = DomainModel(
    name="MOFScriptModel",
    types={MOFScriptModel_TransformationRule, MOFScriptStatementOwner, MOFScriptModel_StatementBlock, MOFScriptModel_MOFScriptObject, MOFScriptModel_MOFScriptComment, MOFScriptModel_MOFScriptTransformation, MOFScriptModel_MOFScriptParameter, MOFScriptModel_MOFScriptStatementOwner, MOFScriptObject, MOFScriptModel_MOFScriptStatement, MOFScriptModel_VariableDeclaration, MOFScriptModel_Expression, MOFScriptModel_ValueExpression, Expression, MOFScriptModel_IteratorStatement, MOFScriptStatement, MOFScriptModel_MOFScriptImport, ValueExpression, MOFScriptModel_FunctionCall, SimpleExpression, MOFScriptModel_SimpleExpression, MOFScriptModel_LogicalExpression, MOFScriptModel_GeneralAssignment, MOFScriptModel_CreateStatement, MOFScriptModel_ResultAssignment, MOFScriptModel_ArithmeticExpression, MOFScriptModel_Literal, MOFScriptModel_Reference, MOFScriptModel_FunctionCallStatement, MOFScriptModel_PrintStatement, MOFScriptModel_IfStatement, MOFScriptModel_FileStatement, MOFScriptModel_ComparisonExpression, MOFScriptModel_Advice, MOFScriptModel_PointCut, MOFScriptModel_MOFScriptSpecification, MOFScriptModel_BreakStatement, MOFScriptModel_WhileStatement, MOFScriptModel_MOFScriptAspect, MOFScriptTransformation, MOFScriptModel_PointCutExpression, MOFScriptModel_SelectExpression, MOFScriptModel_ReturnStatement, MOFScriptModel_VariableDeclarationStatement, MOFScriptModel_CreateExpression, MOFScriptModel_CreateExpressionParameter, MOFScriptModel_DebugStatement, MOFScriptModel_Trace, MOFScriptModel_M2MTrace, Trace, ImportType, ImportSemantics, AssignmentOperator, ParameterDirection, AccessLevel, LogicalOperator, LiteralType, ArithmeticOperator, ComparisonOperator, AdviceOperator, PointCutOperator, PointCutCombinationOperator},
    associations={variables9, blocks10, comment12, owner0, extends2, parameters3, context5, statements8, variables18, constants20, parameters23, owner13, value14, statements16, extends27, transformationrules29, additionalExpressionPart49, parameters51, filterExpression31, source33, before35, between37, after40, part143, part245, expression56, expression58, transformationRule53, part164, function60, printBody62, part271, part173, part266, fileURI69, advice87, pointcut88, ifExpression76, elseBranch79, transformation81, imports83, condition85, pointcutexpression93, pointcut90, filterExpression98, sourceReference100, combinedExpression96, expression110, appliedFunction103, parameters106, value107, variable112, source114, target115},
    generalizations={gen_MOFScriptModel_TransformationRule_MOFScriptStatementOwner, gen_MOFScriptModel_MOFScriptComment_MOFScriptObject, gen_MOFScriptModel_MOFScriptStatementOwner_MOFScriptObject, gen_MOFScriptModel_MOFScriptTransformation_MOFScriptObject, gen_MOFScriptModel_MOFScriptStatement_MOFScriptStatementOwner, gen_MOFScriptModel_VariableDeclaration_MOFScriptObject, gen_MOFScriptModel_ValueExpression_Expression, gen_MOFScriptModel_Expression_MOFScriptObject, gen_MOFScriptModel_IteratorStatement_MOFScriptStatement, gen_MOFScriptModel_MOFScriptParameter_MOFScriptObject, gen_MOFScriptModel_MOFScriptImport_MOFScriptObject, gen_MOFScriptModel_SimpleExpression_ValueExpression, gen_MOFScriptModel_FunctionCall_SimpleExpression, gen_MOFScriptModel_LogicalExpression_Expression, gen_MOFScriptModel_GeneralAssignment_MOFScriptStatement, gen_MOFScriptModel_CreateStatement_MOFScriptStatement, gen_MOFScriptModel_ResultAssignment_MOFScriptStatement, gen_MOFScriptModel_ArithmeticExpression_ValueExpression, gen_MOFScriptModel_Literal_SimpleExpression, gen_MOFScriptModel_Reference_SimpleExpression, gen_MOFScriptModel_FunctionCallStatement_MOFScriptStatement, gen_MOFScriptModel_PrintStatement_MOFScriptStatement, gen_MOFScriptModel_IfStatement_MOFScriptStatement, gen_MOFScriptModel_FileStatement_MOFScriptStatement, gen_MOFScriptModel_ComparisonExpression_Expression, gen_MOFScriptModel_Advice_MOFScriptStatementOwner, gen_MOFScriptModel_MOFScriptSpecification_MOFScriptObject, gen_MOFScriptModel_BreakStatement_MOFScriptStatement, gen_MOFScriptModel_WhileStatement_MOFScriptStatement, gen_MOFScriptModel_MOFScriptAspect_MOFScriptTransformation, gen_MOFScriptModel_SelectExpression_ValueExpression, gen_MOFScriptModel_ReturnStatement_MOFScriptStatement, gen_MOFScriptModel_VariableDeclarationStatement_MOFScriptStatement, gen_MOFScriptModel_CreateExpression_Expression, gen_MOFScriptModel_CreateExpressionParameter_MOFScriptObject, gen_MOFScriptModel_DebugStatement_MOFScriptStatement, gen_MOFScriptModel_Trace_MOFScriptStatement, gen_MOFScriptModel_M2MTrace_Trace},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)