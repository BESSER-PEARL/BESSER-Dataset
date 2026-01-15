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
xpand3_File = Class(name="xpand3::File")
SyntaxElement = Class(name="SyntaxElement")
xpand3_SyntaxElement = Class(name="xpand3::SyntaxElement", is_abstract=True)
xpand3_expression_AbstractExpression = Class(name="xpand3::expression::AbstractExpression", is_abstract=True)
xpand3_expression_BooleanOperation = Class(name="xpand3::expression::BooleanOperation")
BinaryOperation = Class(name="BinaryOperation")
xpand3_expression_Cast = Class(name="xpand3::expression::Cast")
AbstractExpression = Class(name="AbstractExpression")
xpand3_ImportStatement = Class(name="xpand3::ImportStatement")
AbstractDeclaration = Class(name="AbstractDeclaration")
xpand3_Identifier = Class(name="xpand3::Identifier")
xpand3_DeclaredParameter = Class(name="xpand3::DeclaredParameter")
xpand3_expression_CollectionExpression = Class(name="xpand3::expression::CollectionExpression")
FeatureCall = Class(name="FeatureCall")
expression_xpand3_Identifier = Class(name="expression::xpand3::Identifier")
xpand3_expression_ChainExpression = Class(name="xpand3::expression::ChainExpression")
xpand3_expression_ConstructorCallExpression = Class(name="xpand3::expression::ConstructorCallExpression")
xpand3_expression_FeatureCall = Class(name="xpand3::expression::FeatureCall")
xpand3_expression_LetExpression = Class(name="xpand3::expression::LetExpression")
xpand3_expression_OperationCall = Class(name="xpand3::expression::OperationCall")
xpand3_expression_TypeSelectExpression = Class(name="xpand3::expression::TypeSelectExpression")
xpand3_expression_GlobalVarExpression = Class(name="xpand3::expression::GlobalVarExpression")
xpand3_expression_IfExpression = Class(name="xpand3::expression::IfExpression")
xpand3_expression_IntegerLiteral = Class(name="xpand3::expression::IntegerLiteral")
xpand3_expression_NullLiteral = Class(name="xpand3::expression::NullLiteral")
xpand3_expression_RealLiteral = Class(name="xpand3::expression::RealLiteral")
xpand3_expression_ListLiteral = Class(name="xpand3::expression::ListLiteral")
xpand3_expression_Literal = Class(name="xpand3::expression::Literal", is_abstract=True)
xpand3_expression_BooleanLiteral = Class(name="xpand3::expression::BooleanLiteral")
Literal = Class(name="Literal")
xpand3_expression_BinaryOperation = Class(name="xpand3::expression::BinaryOperation")
xpand3_expression_StringLiteral = Class(name="xpand3::expression::StringLiteral")
xpand3_expression_SwitchExpression = Class(name="xpand3::expression::SwitchExpression")
Case = Class(name="Case")
xpand3_expression_Case = Class(name="xpand3::expression::Case")
xpand3_expression_UnaryOperation = Class(name="xpand3::expression::UnaryOperation")
xpand3_statement_AbstractStatement = Class(name="xpand3::statement::AbstractStatement", is_abstract=True)
xpand3_statement_ExpandStatement = Class(name="xpand3::statement::ExpandStatement")
AbstractStatement = Class(name="AbstractStatement")
xpand3_statement_AbstractStatementWithBody = Class(name="xpand3::statement::AbstractStatementWithBody", is_abstract=True)
xpand3_statement_FileStatement = Class(name="xpand3::statement::FileStatement")
AbstractStatementWithBody = Class(name="AbstractStatementWithBody")
statement_xpand3_Identifier = Class(name="statement::xpand3::Identifier")
xpand3_statement_ExpressionStatement = Class(name="xpand3::statement::ExpressionStatement")
xpand3_statement_ErrorStatement = Class(name="xpand3::statement::ErrorStatement")
xpand3_statement_IfStatement = Class(name="xpand3::statement::IfStatement")
IfStatement = Class(name="IfStatement")
xpand3_statement_ForEachStatement = Class(name="xpand3::statement::ForEachStatement")
xpand3_statement_TextStatement = Class(name="xpand3::statement::TextStatement")
xpand3_statement_LetStatement = Class(name="xpand3::statement::LetStatement")
xpand3_statement_ProtectStatement = Class(name="xpand3::statement::ProtectStatement")
xpand3_declaration_Extension = Class(name="xpand3::declaration::Extension")
xpand3_declaration_AbstractDeclaration = Class(name="xpand3::declaration::AbstractDeclaration", is_abstract=True)
declaration_xpand3_File = Class(name="declaration::xpand3::File")
declaration_xpand3_DeclaredParameter = Class(name="declaration::xpand3::DeclaredParameter")
xpand3_declaration_AbstractNamedDeclaration = Class(name="xpand3::declaration::AbstractNamedDeclaration", is_abstract=True)
declaration_xpand3_Identifier = Class(name="declaration::xpand3::Identifier")
xpand3_declaration_Definition = Class(name="xpand3::declaration::Definition")
AbstractNamedDeclaration = Class(name="AbstractNamedDeclaration")
xpand3_declaration_AbstractAspect = Class(name="xpand3::declaration::AbstractAspect", is_abstract=True)
xpand3_declaration_ExtensionAspect = Class(name="xpand3::declaration::ExtensionAspect")
AbstractAspect = Class(name="AbstractAspect")
xpand3_declaration_DefinitionAspect = Class(name="xpand3::declaration::DefinitionAspect")
xpand3_declaration_Check = Class(name="xpand3::declaration::Check")
xpand3_declaration_CreateExtension = Class(name="xpand3::declaration::CreateExtension")
Extension = Class(name="Extension")
xpand3_declaration_JavaExtension = Class(name="xpand3::declaration::JavaExtension")

# xpand3_File class attributes and methods

# SyntaxElement class attributes and methods

# xpand3_SyntaxElement class attributes and methods
xpand3_SyntaxElement_start: Property = Property(name="start", type=IntegerType)
xpand3_SyntaxElement_end: Property = Property(name="end", type=IntegerType)
xpand3_SyntaxElement_fileName: Property = Property(name="fileName", type=StringType)
xpand3_SyntaxElement_line: Property = Property(name="line", type=IntegerType)
xpand3_SyntaxElement.attributes={xpand3_SyntaxElement_line, xpand3_SyntaxElement_start, xpand3_SyntaxElement_end, xpand3_SyntaxElement_fileName}

# xpand3_expression_AbstractExpression class attributes and methods

# xpand3_expression_BooleanOperation class attributes and methods

# BinaryOperation class attributes and methods

# xpand3_expression_Cast class attributes and methods

# AbstractExpression class attributes and methods

# xpand3_ImportStatement class attributes and methods
xpand3_ImportStatement_exported: Property = Property(name="exported", type=BooleanType)
xpand3_ImportStatement.attributes={xpand3_ImportStatement_exported}

# AbstractDeclaration class attributes and methods

# xpand3_Identifier class attributes and methods
xpand3_Identifier_value: Property = Property(name="value", type=StringType)
xpand3_Identifier.attributes={xpand3_Identifier_value}

# xpand3_DeclaredParameter class attributes and methods

# xpand3_expression_CollectionExpression class attributes and methods

# FeatureCall class attributes and methods

# expression_xpand3_Identifier class attributes and methods

# xpand3_expression_ChainExpression class attributes and methods

# xpand3_expression_ConstructorCallExpression class attributes and methods

# xpand3_expression_FeatureCall class attributes and methods

# xpand3_expression_LetExpression class attributes and methods

# xpand3_expression_OperationCall class attributes and methods

# xpand3_expression_TypeSelectExpression class attributes and methods

# xpand3_expression_GlobalVarExpression class attributes and methods

# xpand3_expression_IfExpression class attributes and methods

# xpand3_expression_IntegerLiteral class attributes and methods

# xpand3_expression_NullLiteral class attributes and methods

# xpand3_expression_RealLiteral class attributes and methods

# xpand3_expression_ListLiteral class attributes and methods

# xpand3_expression_Literal class attributes and methods

# xpand3_expression_BooleanLiteral class attributes and methods

# Literal class attributes and methods

# xpand3_expression_BinaryOperation class attributes and methods

# xpand3_expression_StringLiteral class attributes and methods

# xpand3_expression_SwitchExpression class attributes and methods

# Case class attributes and methods

# xpand3_expression_Case class attributes and methods

# xpand3_expression_UnaryOperation class attributes and methods

# xpand3_statement_AbstractStatement class attributes and methods

# xpand3_statement_ExpandStatement class attributes and methods
xpand3_statement_ExpandStatement_foreach: Property = Property(name="foreach", type=BooleanType)
xpand3_statement_ExpandStatement.attributes={xpand3_statement_ExpandStatement_foreach}

# AbstractStatement class attributes and methods

# xpand3_statement_AbstractStatementWithBody class attributes and methods

# xpand3_statement_FileStatement class attributes and methods
xpand3_statement_FileStatement_once: Property = Property(name="once", type=BooleanType)
xpand3_statement_FileStatement.attributes={xpand3_statement_FileStatement_once}

# AbstractStatementWithBody class attributes and methods

# statement_xpand3_Identifier class attributes and methods

# xpand3_statement_ExpressionStatement class attributes and methods

# xpand3_statement_ErrorStatement class attributes and methods

# xpand3_statement_IfStatement class attributes and methods

# IfStatement class attributes and methods

# xpand3_statement_ForEachStatement class attributes and methods

# xpand3_statement_TextStatement class attributes and methods
xpand3_statement_TextStatement_value: Property = Property(name="value", type=StringType)
xpand3_statement_TextStatement_deleteLine: Property = Property(name="deleteLine", type=BooleanType)
xpand3_statement_TextStatement.attributes={xpand3_statement_TextStatement_value, xpand3_statement_TextStatement_deleteLine}

# xpand3_statement_LetStatement class attributes and methods

# xpand3_statement_ProtectStatement class attributes and methods
xpand3_statement_ProtectStatement_disable: Property = Property(name="disable", type=BooleanType)
xpand3_statement_ProtectStatement.attributes={xpand3_statement_ProtectStatement_disable}

# xpand3_declaration_Extension class attributes and methods
xpand3_declaration_Extension_cached: Property = Property(name="cached", type=BooleanType)
xpand3_declaration_Extension.attributes={xpand3_declaration_Extension_cached}

# xpand3_declaration_AbstractDeclaration class attributes and methods
xpand3_declaration_AbstractDeclaration_isPrivate: Property = Property(name="isPrivate", type=BooleanType)
xpand3_declaration_AbstractDeclaration.attributes={xpand3_declaration_AbstractDeclaration_isPrivate}

# declaration_xpand3_File class attributes and methods

# declaration_xpand3_DeclaredParameter class attributes and methods

# xpand3_declaration_AbstractNamedDeclaration class attributes and methods

# declaration_xpand3_Identifier class attributes and methods

# xpand3_declaration_Definition class attributes and methods

# AbstractNamedDeclaration class attributes and methods

# xpand3_declaration_AbstractAspect class attributes and methods
xpand3_declaration_AbstractAspect_wildparams: Property = Property(name="wildparams", type=BooleanType)
xpand3_declaration_AbstractAspect.attributes={xpand3_declaration_AbstractAspect_wildparams}

# xpand3_declaration_ExtensionAspect class attributes and methods

# AbstractAspect class attributes and methods

# xpand3_declaration_DefinitionAspect class attributes and methods

# xpand3_declaration_Check class attributes and methods
xpand3_declaration_Check_errorSeverity: Property = Property(name="errorSeverity", type=BooleanType)
xpand3_declaration_Check_feature: Property = Property(name="feature", type=StringType)
xpand3_declaration_Check.attributes={xpand3_declaration_Check_feature, xpand3_declaration_Check_errorSeverity}

# xpand3_declaration_CreateExtension class attributes and methods

# Extension class attributes and methods

# xpand3_declaration_JavaExtension class attributes and methods

# Relationships
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="xpand3_ImportStatement", type=xpand3_File, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_File", type=xpand3_ImportStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declarations1: BinaryAssociation = BinaryAssociation(
    name="declarations1",
    ends={
        Property(name="AbstractDeclaration", type=xpand3_File, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_File2", type=AbstractDeclaration, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
importedId3: BinaryAssociation = BinaryAssociation(
    name="importedId3",
    ends={
        Property(name="xpand3_Identifier", type=xpand3_ImportStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_ImportStatement4", type=xpand3_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name5: BinaryAssociation = BinaryAssociation(
    name="name5",
    ends={
        Property(name="xpand3_Identifier6", type=xpand3_DeclaredParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_DeclaredParameter", type=xpand3_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type7: BinaryAssociation = BinaryAssociation(
    name="type7",
    ends={
        Property(name="xpand3_Identifier9", type=xpand3_DeclaredParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_DeclaredParameter8", type=xpand3_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
closure25: BinaryAssociation = BinaryAssociation(
    name="closure25",
    ends={
        Property(name="AbstractExpression26", type=xpand3_expression_CollectionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_expression_CollectionExpression", type=AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type10: BinaryAssociation = BinaryAssociation(
    name="type10",
    ends={
        Property(name="expression_xpand3_Identifier", type=xpand3_expression_Cast, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_expression_Cast", type=expression_xpand3_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target11: BinaryAssociation = BinaryAssociation(
    name="target11",
    ends={
        Property(name="AbstractExpression", type=xpand3_expression_Cast, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_expression_Cast12", type=AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
first13: BinaryAssociation = BinaryAssociation(
    name="first13",
    ends={
        Property(name="AbstractExpression14", type=xpand3_expression_ChainExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_expression_ChainExpression", type=AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
next15: BinaryAssociation = BinaryAssociation(
    name="next15",
    ends={
        Property(name="AbstractExpression17", type=xpand3_expression_ChainExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_expression_ChainExpression16", type=AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type18: BinaryAssociation = BinaryAssociation(
    name="type18",
    ends={
        Property(name="expression_xpand3_Identifier19", type=xpand3_expression_ConstructorCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_expression_ConstructorCallExpression", type=expression_xpand3_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target20: BinaryAssociation = BinaryAssociation(
    name="target20",
    ends={
        Property(name="AbstractExpression21", type=xpand3_expression_FeatureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_expression_FeatureCall", type=AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name22: BinaryAssociation = BinaryAssociation(
    name="name22",
    ends={
        Property(name="expression_xpand3_Identifier24", type=xpand3_expression_FeatureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_expression_FeatureCall23", type=expression_xpand3_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elsePart41: BinaryAssociation = BinaryAssociation(
    name="elsePart41",
    ends={
        Property(name="AbstractExpression43", type=xpand3_expression_IfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_expression_IfExpression42", type=AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eleName27: BinaryAssociation = BinaryAssociation(
    name="eleName27",
    ends={
        Property(name="expression_xpand3_Identifier29", type=xpand3_expression_CollectionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_expression_CollectionExpression28", type=expression_xpand3_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
params30: BinaryAssociation = BinaryAssociation(
    name="params30",
    ends={
        Property(name="AbstractExpression31", type=xpand3_expression_OperationCall, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_expression_OperationCall", type=AbstractExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeLiteral32: BinaryAssociation = BinaryAssociation(
    name="typeLiteral32",
    ends={
        Property(name="expression_xpand3_Identifier33", type=xpand3_expression_TypeSelectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_expression_TypeSelectExpression", type=expression_xpand3_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
globalVarName34: BinaryAssociation = BinaryAssociation(
    name="globalVarName34",
    ends={
        Property(name="expression_xpand3_Identifier35", type=xpand3_expression_GlobalVarExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_expression_GlobalVarExpression", type=expression_xpand3_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition36: BinaryAssociation = BinaryAssociation(
    name="condition36",
    ends={
        Property(name="AbstractExpression37", type=xpand3_expression_IfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_expression_IfExpression", type=AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenPart38: BinaryAssociation = BinaryAssociation(
    name="thenPart38",
    ends={
        Property(name="AbstractExpression40", type=xpand3_expression_IfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_expression_IfExpression39", type=AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
varExpression44: BinaryAssociation = BinaryAssociation(
    name="varExpression44",
    ends={
        Property(name="AbstractExpression45", type=xpand3_expression_LetExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_expression_LetExpression", type=AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetExpression46: BinaryAssociation = BinaryAssociation(
    name="targetExpression46",
    ends={
        Property(name="AbstractExpression48", type=xpand3_expression_LetExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_expression_LetExpression47", type=AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
varName49: BinaryAssociation = BinaryAssociation(
    name="varName49",
    ends={
        Property(name="expression_xpand3_Identifier51", type=xpand3_expression_LetExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_expression_LetExpression50", type=expression_xpand3_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements52: BinaryAssociation = BinaryAssociation(
    name="elements52",
    ends={
        Property(name="AbstractExpression53", type=xpand3_expression_ListLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_expression_ListLiteral", type=AbstractExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
literalValue54: BinaryAssociation = BinaryAssociation(
    name="literalValue54",
    ends={
        Property(name="expression_xpand3_Identifier55", type=xpand3_expression_Literal, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_expression_Literal", type=expression_xpand3_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left68: BinaryAssociation = BinaryAssociation(
    name="left68",
    ends={
        Property(name="AbstractExpression69", type=xpand3_expression_BinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_expression_BinaryOperation", type=AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
switchExpr56: BinaryAssociation = BinaryAssociation(
    name="switchExpr56",
    ends={
        Property(name="AbstractExpression57", type=xpand3_expression_SwitchExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_expression_SwitchExpression", type=AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultExpr58: BinaryAssociation = BinaryAssociation(
    name="defaultExpr58",
    ends={
        Property(name="AbstractExpression60", type=xpand3_expression_SwitchExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_expression_SwitchExpression59", type=AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cases61: BinaryAssociation = BinaryAssociation(
    name="cases61",
    ends={
        Property(name="Case", type=xpand3_expression_SwitchExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_expression_SwitchExpression62", type=Case, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition63: BinaryAssociation = BinaryAssociation(
    name="condition63",
    ends={
        Property(name="AbstractExpression64", type=xpand3_expression_Case, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_expression_Case", type=AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenPart65: BinaryAssociation = BinaryAssociation(
    name="thenPart65",
    ends={
        Property(name="AbstractExpression67", type=xpand3_expression_Case, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_expression_Case66", type=AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters81: BinaryAssociation = BinaryAssociation(
    name="parameters81",
    ends={
        Property(name="AbstractExpression82", type=xpand3_statement_ExpandStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_statement_ExpandStatement", type=AbstractExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
separator83: BinaryAssociation = BinaryAssociation(
    name="separator83",
    ends={
        Property(name="AbstractExpression85", type=xpand3_statement_ExpandStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_statement_ExpandStatement84", type=AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right70: BinaryAssociation = BinaryAssociation(
    name="right70",
    ends={
        Property(name="AbstractExpression72", type=xpand3_expression_BinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_expression_BinaryOperation71", type=AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operator73: BinaryAssociation = BinaryAssociation(
    name="operator73",
    ends={
        Property(name="expression_xpand3_Identifier75", type=xpand3_expression_BinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_expression_BinaryOperation74", type=expression_xpand3_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operator76: BinaryAssociation = BinaryAssociation(
    name="operator76",
    ends={
        Property(name="expression_xpand3_Identifier77", type=xpand3_expression_UnaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_expression_UnaryOperation", type=expression_xpand3_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand78: BinaryAssociation = BinaryAssociation(
    name="operand78",
    ends={
        Property(name="AbstractExpression80", type=xpand3_expression_UnaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_expression_UnaryOperation79", type=AbstractExpression, multiplicity=Multiplicity(0, 1))
    }
)
body95: BinaryAssociation = BinaryAssociation(
    name="body95",
    ends={
        Property(name="AbstractStatement", type=xpand3_statement_AbstractStatementWithBody, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_statement_AbstractStatementWithBody", type=AbstractStatement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
fileNameExpression96: BinaryAssociation = BinaryAssociation(
    name="fileNameExpression96",
    ends={
        Property(name="AbstractExpression97", type=xpand3_statement_FileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_statement_FileStatement", type=AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target86: BinaryAssociation = BinaryAssociation(
    name="target86",
    ends={
        Property(name="AbstractExpression88", type=xpand3_statement_ExpandStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_statement_ExpandStatement87", type=AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definition89: BinaryAssociation = BinaryAssociation(
    name="definition89",
    ends={
        Property(name="statement_xpand3_Identifier", type=xpand3_statement_ExpandStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_statement_ExpandStatement90", type=statement_xpand3_Identifier, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression91: BinaryAssociation = BinaryAssociation(
    name="expression91",
    ends={
        Property(name="AbstractExpression92", type=xpand3_statement_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_statement_ExpressionStatement", type=AbstractExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
message93: BinaryAssociation = BinaryAssociation(
    name="message93",
    ends={
        Property(name="AbstractExpression94", type=xpand3_statement_ErrorStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_statement_ErrorStatement", type=AbstractExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition112: BinaryAssociation = BinaryAssociation(
    name="condition112",
    ends={
        Property(name="AbstractExpression113", type=xpand3_statement_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_statement_IfStatement", type=AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseIf114: BinaryAssociation = BinaryAssociation(
    name="elseIf114",
    ends={
        Property(name="IfStatement", type=xpand3_statement_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_statement_IfStatement115", type=IfStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outletNameIdentifier98: BinaryAssociation = BinaryAssociation(
    name="outletNameIdentifier98",
    ends={
        Property(name="statement_xpand3_Identifier100", type=xpand3_statement_FileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_statement_FileStatement99", type=statement_xpand3_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target101: BinaryAssociation = BinaryAssociation(
    name="target101",
    ends={
        Property(name="AbstractExpression102", type=xpand3_statement_ForEachStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_statement_ForEachStatement", type=AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
separator103: BinaryAssociation = BinaryAssociation(
    name="separator103",
    ends={
        Property(name="AbstractExpression105", type=xpand3_statement_ForEachStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_statement_ForEachStatement104", type=AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable106: BinaryAssociation = BinaryAssociation(
    name="variable106",
    ends={
        Property(name="statement_xpand3_Identifier108", type=xpand3_statement_ForEachStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_statement_ForEachStatement107", type=statement_xpand3_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
iteratorName109: BinaryAssociation = BinaryAssociation(
    name="iteratorName109",
    ends={
        Property(name="statement_xpand3_Identifier111", type=xpand3_statement_ForEachStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_statement_ForEachStatement110", type=statement_xpand3_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
varName116: BinaryAssociation = BinaryAssociation(
    name="varName116",
    ends={
        Property(name="statement_xpand3_Identifier117", type=xpand3_statement_LetStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_statement_LetStatement", type=statement_xpand3_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
varValue118: BinaryAssociation = BinaryAssociation(
    name="varValue118",
    ends={
        Property(name="AbstractExpression120", type=xpand3_statement_LetStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_statement_LetStatement119", type=AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commentStart121: BinaryAssociation = BinaryAssociation(
    name="commentStart121",
    ends={
        Property(name="AbstractExpression122", type=xpand3_statement_ProtectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_statement_ProtectStatement", type=AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commentEnd123: BinaryAssociation = BinaryAssociation(
    name="commentEnd123",
    ends={
        Property(name="AbstractExpression125", type=xpand3_statement_ProtectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_statement_ProtectStatement124", type=AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id126: BinaryAssociation = BinaryAssociation(
    name="id126",
    ends={
        Property(name="AbstractExpression128", type=xpand3_statement_ProtectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_statement_ProtectStatement127", type=AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body136: BinaryAssociation = BinaryAssociation(
    name="body136",
    ends={
        Property(name="AbstractStatement137", type=xpand3_declaration_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_declaration_Definition", type=AbstractStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body138: BinaryAssociation = BinaryAssociation(
    name="body138",
    ends={
        Property(name="AbstractExpression139", type=xpand3_declaration_Extension, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_declaration_Extension", type=AbstractExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
owner129: BinaryAssociation = BinaryAssociation(
    name="owner129",
    ends={
        Property(name="declaration_xpand3_File", type=xpand3_declaration_AbstractDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_declaration_AbstractDeclaration", type=declaration_xpand3_File, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
params130: BinaryAssociation = BinaryAssociation(
    name="params130",
    ends={
        Property(name="declaration_xpand3_DeclaredParameter", type=xpand3_declaration_AbstractDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_declaration_AbstractDeclaration131", type=declaration_xpand3_DeclaredParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard132: BinaryAssociation = BinaryAssociation(
    name="guard132",
    ends={
        Property(name="AbstractExpression134", type=xpand3_declaration_AbstractDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_declaration_AbstractDeclaration133", type=AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name135: BinaryAssociation = BinaryAssociation(
    name="name135",
    ends={
        Property(name="declaration_xpand3_Identifier", type=xpand3_declaration_AbstractNamedDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_declaration_AbstractNamedDeclaration", type=declaration_xpand3_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
msg149: BinaryAssociation = BinaryAssociation(
    name="msg149",
    ends={
        Property(name="AbstractExpression150", type=xpand3_declaration_Check, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_declaration_Check", type=AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constraint151: BinaryAssociation = BinaryAssociation(
    name="constraint151",
    ends={
        Property(name="AbstractExpression153", type=xpand3_declaration_Check, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_declaration_Check152", type=AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnType140: BinaryAssociation = BinaryAssociation(
    name="returnType140",
    ends={
        Property(name="declaration_xpand3_Identifier142", type=xpand3_declaration_Extension, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_declaration_Extension141", type=declaration_xpand3_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pointcut143: BinaryAssociation = BinaryAssociation(
    name="pointcut143",
    ends={
        Property(name="declaration_xpand3_Identifier144", type=xpand3_declaration_AbstractAspect, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_declaration_AbstractAspect", type=declaration_xpand3_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression145: BinaryAssociation = BinaryAssociation(
    name="expression145",
    ends={
        Property(name="AbstractExpression146", type=xpand3_declaration_ExtensionAspect, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_declaration_ExtensionAspect", type=AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body147: BinaryAssociation = BinaryAssociation(
    name="body147",
    ends={
        Property(name="AbstractStatement148", type=xpand3_declaration_DefinitionAspect, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_declaration_DefinitionAspect", type=AbstractStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
toBeCreated154: BinaryAssociation = BinaryAssociation(
    name="toBeCreated154",
    ends={
        Property(name="declaration_xpand3_DeclaredParameter155", type=xpand3_declaration_CreateExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_declaration_CreateExtension", type=declaration_xpand3_DeclaredParameter, multiplicity=Multiplicity(0, 1))
    }
)
javaType156: BinaryAssociation = BinaryAssociation(
    name="javaType156",
    ends={
        Property(name="declaration_xpand3_Identifier157", type=xpand3_declaration_JavaExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_declaration_JavaExtension", type=declaration_xpand3_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
javaMethod158: BinaryAssociation = BinaryAssociation(
    name="javaMethod158",
    ends={
        Property(name="declaration_xpand3_Identifier160", type=xpand3_declaration_JavaExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_declaration_JavaExtension159", type=declaration_xpand3_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
javaParamTypes161: BinaryAssociation = BinaryAssociation(
    name="javaParamTypes161",
    ends={
        Property(name="declaration_xpand3_Identifier163", type=xpand3_declaration_JavaExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="xpand3_declaration_JavaExtension162", type=declaration_xpand3_Identifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_xpand3_File_SyntaxElement = Generalization(general=SyntaxElement, specific=xpand3_File)
gen_xpand3_expression_AbstractExpression_SyntaxElement = Generalization(general=SyntaxElement, specific=xpand3_expression_AbstractExpression)
gen_xpand3_expression_BooleanOperation_BinaryOperation = Generalization(general=BinaryOperation, specific=xpand3_expression_BooleanOperation)
gen_xpand3_expression_Cast_AbstractExpression = Generalization(general=AbstractExpression, specific=xpand3_expression_Cast)
gen_xpand3_ImportStatement_SyntaxElement = Generalization(general=SyntaxElement, specific=xpand3_ImportStatement)
gen_xpand3_Identifier_SyntaxElement = Generalization(general=SyntaxElement, specific=xpand3_Identifier)
gen_xpand3_DeclaredParameter_SyntaxElement = Generalization(general=SyntaxElement, specific=xpand3_DeclaredParameter)
gen_xpand3_expression_CollectionExpression_FeatureCall = Generalization(general=FeatureCall, specific=xpand3_expression_CollectionExpression)
gen_xpand3_expression_ChainExpression_AbstractExpression = Generalization(general=AbstractExpression, specific=xpand3_expression_ChainExpression)
gen_xpand3_expression_ConstructorCallExpression_AbstractExpression = Generalization(general=AbstractExpression, specific=xpand3_expression_ConstructorCallExpression)
gen_xpand3_expression_FeatureCall_AbstractExpression = Generalization(general=AbstractExpression, specific=xpand3_expression_FeatureCall)
gen_xpand3_expression_OperationCall_FeatureCall = Generalization(general=FeatureCall, specific=xpand3_expression_OperationCall)
gen_xpand3_expression_TypeSelectExpression_FeatureCall = Generalization(general=FeatureCall, specific=xpand3_expression_TypeSelectExpression)
gen_xpand3_expression_GlobalVarExpression_AbstractExpression = Generalization(general=AbstractExpression, specific=xpand3_expression_GlobalVarExpression)
gen_xpand3_expression_IfExpression_AbstractExpression = Generalization(general=AbstractExpression, specific=xpand3_expression_IfExpression)
gen_xpand3_expression_IntegerLiteral_Literal = Generalization(general=Literal, specific=xpand3_expression_IntegerLiteral)
gen_xpand3_expression_NullLiteral_Literal = Generalization(general=Literal, specific=xpand3_expression_NullLiteral)
gen_xpand3_expression_RealLiteral_Literal = Generalization(general=Literal, specific=xpand3_expression_RealLiteral)
gen_xpand3_expression_LetExpression_AbstractExpression = Generalization(general=AbstractExpression, specific=xpand3_expression_LetExpression)
gen_xpand3_expression_ListLiteral_AbstractExpression = Generalization(general=AbstractExpression, specific=xpand3_expression_ListLiteral)
gen_xpand3_expression_Literal_AbstractExpression = Generalization(general=AbstractExpression, specific=xpand3_expression_Literal)
gen_xpand3_expression_BooleanLiteral_Literal = Generalization(general=Literal, specific=xpand3_expression_BooleanLiteral)
gen_xpand3_expression_BinaryOperation_AbstractExpression = Generalization(general=AbstractExpression, specific=xpand3_expression_BinaryOperation)
gen_xpand3_expression_StringLiteral_Literal = Generalization(general=Literal, specific=xpand3_expression_StringLiteral)
gen_xpand3_expression_SwitchExpression_AbstractExpression = Generalization(general=AbstractExpression, specific=xpand3_expression_SwitchExpression)
gen_xpand3_expression_Case_SyntaxElement = Generalization(general=SyntaxElement, specific=xpand3_expression_Case)
gen_xpand3_expression_UnaryOperation_AbstractExpression = Generalization(general=AbstractExpression, specific=xpand3_expression_UnaryOperation)
gen_xpand3_statement_AbstractStatement_SyntaxElement = Generalization(general=SyntaxElement, specific=xpand3_statement_AbstractStatement)
gen_xpand3_statement_ExpandStatement_AbstractStatement = Generalization(general=AbstractStatement, specific=xpand3_statement_ExpandStatement)
gen_xpand3_statement_AbstractStatementWithBody_AbstractStatement = Generalization(general=AbstractStatement, specific=xpand3_statement_AbstractStatementWithBody)
gen_xpand3_statement_FileStatement_AbstractStatementWithBody = Generalization(general=AbstractStatementWithBody, specific=xpand3_statement_FileStatement)
gen_xpand3_statement_ExpressionStatement_AbstractStatement = Generalization(general=AbstractStatement, specific=xpand3_statement_ExpressionStatement)
gen_xpand3_statement_ErrorStatement_AbstractStatement = Generalization(general=AbstractStatement, specific=xpand3_statement_ErrorStatement)
gen_xpand3_statement_IfStatement_AbstractStatementWithBody = Generalization(general=AbstractStatementWithBody, specific=xpand3_statement_IfStatement)
gen_xpand3_statement_ForEachStatement_AbstractStatementWithBody = Generalization(general=AbstractStatementWithBody, specific=xpand3_statement_ForEachStatement)
gen_xpand3_statement_TextStatement_AbstractStatement = Generalization(general=AbstractStatement, specific=xpand3_statement_TextStatement)
gen_xpand3_statement_LetStatement_AbstractStatementWithBody = Generalization(general=AbstractStatementWithBody, specific=xpand3_statement_LetStatement)
gen_xpand3_statement_ProtectStatement_AbstractStatementWithBody = Generalization(general=AbstractStatementWithBody, specific=xpand3_statement_ProtectStatement)
gen_xpand3_declaration_Extension_AbstractNamedDeclaration = Generalization(general=AbstractNamedDeclaration, specific=xpand3_declaration_Extension)
gen_xpand3_declaration_AbstractDeclaration_SyntaxElement = Generalization(general=SyntaxElement, specific=xpand3_declaration_AbstractDeclaration)
gen_xpand3_declaration_AbstractNamedDeclaration_AbstractDeclaration = Generalization(general=AbstractDeclaration, specific=xpand3_declaration_AbstractNamedDeclaration)
gen_xpand3_declaration_Definition_AbstractNamedDeclaration = Generalization(general=AbstractNamedDeclaration, specific=xpand3_declaration_Definition)
gen_xpand3_declaration_Check_AbstractDeclaration = Generalization(general=AbstractDeclaration, specific=xpand3_declaration_Check)
gen_xpand3_declaration_AbstractAspect_AbstractDeclaration = Generalization(general=AbstractDeclaration, specific=xpand3_declaration_AbstractAspect)
gen_xpand3_declaration_ExtensionAspect_AbstractAspect = Generalization(general=AbstractAspect, specific=xpand3_declaration_ExtensionAspect)
gen_xpand3_declaration_DefinitionAspect_AbstractAspect = Generalization(general=AbstractAspect, specific=xpand3_declaration_DefinitionAspect)
gen_xpand3_declaration_CreateExtension_Extension = Generalization(general=Extension, specific=xpand3_declaration_CreateExtension)
gen_xpand3_declaration_JavaExtension_AbstractNamedDeclaration = Generalization(general=AbstractNamedDeclaration, specific=xpand3_declaration_JavaExtension)

# Domain Model
domain_model = DomainModel(
    name="xpand3",
    types={xpand3_File, SyntaxElement, xpand3_SyntaxElement, xpand3_expression_AbstractExpression, xpand3_expression_BooleanOperation, BinaryOperation, xpand3_expression_Cast, AbstractExpression, xpand3_ImportStatement, AbstractDeclaration, xpand3_Identifier, xpand3_DeclaredParameter, xpand3_expression_CollectionExpression, FeatureCall, expression_xpand3_Identifier, xpand3_expression_ChainExpression, xpand3_expression_ConstructorCallExpression, xpand3_expression_FeatureCall, xpand3_expression_LetExpression, xpand3_expression_OperationCall, xpand3_expression_TypeSelectExpression, xpand3_expression_GlobalVarExpression, xpand3_expression_IfExpression, xpand3_expression_IntegerLiteral, xpand3_expression_NullLiteral, xpand3_expression_RealLiteral, xpand3_expression_ListLiteral, xpand3_expression_Literal, xpand3_expression_BooleanLiteral, Literal, xpand3_expression_BinaryOperation, xpand3_expression_StringLiteral, xpand3_expression_SwitchExpression, Case, xpand3_expression_Case, xpand3_expression_UnaryOperation, xpand3_statement_AbstractStatement, xpand3_statement_ExpandStatement, AbstractStatement, xpand3_statement_AbstractStatementWithBody, xpand3_statement_FileStatement, AbstractStatementWithBody, statement_xpand3_Identifier, xpand3_statement_ExpressionStatement, xpand3_statement_ErrorStatement, xpand3_statement_IfStatement, IfStatement, xpand3_statement_ForEachStatement, xpand3_statement_TextStatement, xpand3_statement_LetStatement, xpand3_statement_ProtectStatement, xpand3_declaration_Extension, xpand3_declaration_AbstractDeclaration, declaration_xpand3_File, declaration_xpand3_DeclaredParameter, xpand3_declaration_AbstractNamedDeclaration, declaration_xpand3_Identifier, xpand3_declaration_Definition, AbstractNamedDeclaration, xpand3_declaration_AbstractAspect, xpand3_declaration_ExtensionAspect, AbstractAspect, xpand3_declaration_DefinitionAspect, xpand3_declaration_Check, xpand3_declaration_CreateExtension, Extension, xpand3_declaration_JavaExtension},
    associations={imports0, declarations1, importedId3, name5, type7, closure25, type10, target11, first13, next15, type18, target20, name22, elsePart41, eleName27, params30, typeLiteral32, globalVarName34, condition36, thenPart38, varExpression44, targetExpression46, varName49, elements52, literalValue54, left68, switchExpr56, defaultExpr58, cases61, condition63, thenPart65, parameters81, separator83, right70, operator73, operator76, operand78, body95, fileNameExpression96, target86, definition89, expression91, message93, condition112, elseIf114, outletNameIdentifier98, target101, separator103, variable106, iteratorName109, varName116, varValue118, commentStart121, commentEnd123, id126, body136, body138, owner129, params130, guard132, name135, msg149, constraint151, returnType140, pointcut143, expression145, body147, toBeCreated154, javaType156, javaMethod158, javaParamTypes161},
    generalizations={gen_xpand3_File_SyntaxElement, gen_xpand3_expression_AbstractExpression_SyntaxElement, gen_xpand3_expression_BooleanOperation_BinaryOperation, gen_xpand3_expression_Cast_AbstractExpression, gen_xpand3_ImportStatement_SyntaxElement, gen_xpand3_Identifier_SyntaxElement, gen_xpand3_DeclaredParameter_SyntaxElement, gen_xpand3_expression_CollectionExpression_FeatureCall, gen_xpand3_expression_ChainExpression_AbstractExpression, gen_xpand3_expression_ConstructorCallExpression_AbstractExpression, gen_xpand3_expression_FeatureCall_AbstractExpression, gen_xpand3_expression_OperationCall_FeatureCall, gen_xpand3_expression_TypeSelectExpression_FeatureCall, gen_xpand3_expression_GlobalVarExpression_AbstractExpression, gen_xpand3_expression_IfExpression_AbstractExpression, gen_xpand3_expression_IntegerLiteral_Literal, gen_xpand3_expression_NullLiteral_Literal, gen_xpand3_expression_RealLiteral_Literal, gen_xpand3_expression_LetExpression_AbstractExpression, gen_xpand3_expression_ListLiteral_AbstractExpression, gen_xpand3_expression_Literal_AbstractExpression, gen_xpand3_expression_BooleanLiteral_Literal, gen_xpand3_expression_BinaryOperation_AbstractExpression, gen_xpand3_expression_StringLiteral_Literal, gen_xpand3_expression_SwitchExpression_AbstractExpression, gen_xpand3_expression_Case_SyntaxElement, gen_xpand3_expression_UnaryOperation_AbstractExpression, gen_xpand3_statement_AbstractStatement_SyntaxElement, gen_xpand3_statement_ExpandStatement_AbstractStatement, gen_xpand3_statement_AbstractStatementWithBody_AbstractStatement, gen_xpand3_statement_FileStatement_AbstractStatementWithBody, gen_xpand3_statement_ExpressionStatement_AbstractStatement, gen_xpand3_statement_ErrorStatement_AbstractStatement, gen_xpand3_statement_IfStatement_AbstractStatementWithBody, gen_xpand3_statement_ForEachStatement_AbstractStatementWithBody, gen_xpand3_statement_TextStatement_AbstractStatement, gen_xpand3_statement_LetStatement_AbstractStatementWithBody, gen_xpand3_statement_ProtectStatement_AbstractStatementWithBody, gen_xpand3_declaration_Extension_AbstractNamedDeclaration, gen_xpand3_declaration_AbstractDeclaration_SyntaxElement, gen_xpand3_declaration_AbstractNamedDeclaration_AbstractDeclaration, gen_xpand3_declaration_Definition_AbstractNamedDeclaration, gen_xpand3_declaration_Check_AbstractDeclaration, gen_xpand3_declaration_AbstractAspect_AbstractDeclaration, gen_xpand3_declaration_ExtensionAspect_AbstractAspect, gen_xpand3_declaration_DefinitionAspect_AbstractAspect, gen_xpand3_declaration_CreateExtension_Extension, gen_xpand3_declaration_JavaExtension_AbstractNamedDeclaration},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)