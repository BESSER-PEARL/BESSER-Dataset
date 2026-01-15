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
UnaryOperator: Enumeration = Enumeration(
    name="UnaryOperator",
    literals={
            EnumerationLiteral(name="postfixInc"),
			EnumerationLiteral(name="postfixDec"),
			EnumerationLiteral(name="delete"),
			EnumerationLiteral(name="void"),
			EnumerationLiteral(name="typeof"),
			EnumerationLiteral(name="prefixInc"),
			EnumerationLiteral(name="prefixDec"),
			EnumerationLiteral(name="unaryPlus"),
			EnumerationLiteral(name="numNeg"),
			EnumerationLiteral(name="bwNot"),
			EnumerationLiteral(name="not"),
			EnumerationLiteral(name="yield")
    }
)

BinaryOperator: Enumeration = Enumeration(
    name="BinaryOperator",
    literals={
            EnumerationLiteral(name="mul"),
			EnumerationLiteral(name="div"),
			EnumerationLiteral(name="mod"),
			EnumerationLiteral(name="add"),
			EnumerationLiteral(name="sub"),
			EnumerationLiteral(name="lsh"),
			EnumerationLiteral(name="rsh"),
			EnumerationLiteral(name="ursh"),
			EnumerationLiteral(name="less"),
			EnumerationLiteral(name="greater"),
			EnumerationLiteral(name="leq"),
			EnumerationLiteral(name="geq"),
			EnumerationLiteral(name="instanceof"),
			EnumerationLiteral(name="in"),
			EnumerationLiteral(name="eq"),
			EnumerationLiteral(name="neq"),
			EnumerationLiteral(name="same"),
			EnumerationLiteral(name="nsame"),
			EnumerationLiteral(name="bwAnd"),
			EnumerationLiteral(name="bwXor"),
			EnumerationLiteral(name="mulAssign"),
			EnumerationLiteral(name="divAssign"),
			EnumerationLiteral(name="modAssign"),
			EnumerationLiteral(name="addAssign"),
			EnumerationLiteral(name="subAssign"),
			EnumerationLiteral(name="lshAssign"),
			EnumerationLiteral(name="rshAssign"),
			EnumerationLiteral(name="urshAssign"),
			EnumerationLiteral(name="andAssign"),
			EnumerationLiteral(name="xorAssign"),
			EnumerationLiteral(name="orAssign"),
			EnumerationLiteral(name="comma"),
			EnumerationLiteral(name="bwOr"),
			EnumerationLiteral(name="logAnd"),
			EnumerationLiteral(name="logOr"),
			EnumerationLiteral(name="assign")
    }
)

# Classes
dom_Node = Class(name="dom::Node", is_abstract=True)
dom_Comment = Class(name="dom::Comment")
Node = Class(name="Node")
dom_Identifier = Class(name="dom::Identifier")
IPropertyName = Class(name="IPropertyName")
IPropertySelector = Class(name="IPropertySelector")
IProperty = Class(name="IProperty")
dom_VariableReference = Class(name="dom::VariableReference")
Expression = Class(name="Expression")
dom_Label = Class(name="dom::Label")
dom_Expression = Class(name="dom::Expression", is_abstract=True)
IArrayElement = Class(name="IArrayElement")
IForInitializer = Class(name="IForInitializer")
dom_NullLiteral = Class(name="dom::NullLiteral")
dom_BooleanLiteral = Class(name="dom::BooleanLiteral")
dom_NumericLiteral = Class(name="dom::NumericLiteral")
dom_StringLiteral = Class(name="dom::StringLiteral")
dom_RegularExpressionLiteral = Class(name="dom::RegularExpressionLiteral")
dom_ThisExpression = Class(name="dom::ThisExpression")
dom_ArrayLiteral = Class(name="dom::ArrayLiteral")
dom_Elision = Class(name="dom::Elision")
dom_ObjectLiteral = Class(name="dom::ObjectLiteral")
dom_PropertyAssignment = Class(name="dom::PropertyAssignment", is_abstract=True)
dom_IPropertyName = Class(name="dom::IPropertyName", is_abstract=True)
dom_SimplePropertyAssignment = Class(name="dom::SimplePropertyAssignment")
PropertyAssignment = Class(name="PropertyAssignment")
dom_AccessorAssignment = Class(name="dom::AccessorAssignment", is_abstract=True)
dom_BlockStatement = Class(name="dom::BlockStatement")
dom_GetterAssignment = Class(name="dom::GetterAssignment")
AccessorAssignment = Class(name="AccessorAssignment")
dom_ParenthesizedExpression = Class(name="dom::ParenthesizedExpression")
dom_IArrayElement = Class(name="dom::IArrayElement", is_abstract=True)
dom_ArrayAccessExpression = Class(name="dom::ArrayAccessExpression")
dom_PropertyAccessExpression = Class(name="dom::PropertyAccessExpression")
dom_IProperty = Class(name="dom::IProperty", is_abstract=True)
dom_NewExpression = Class(name="dom::NewExpression")
dom_SetterAssignment = Class(name="dom::SetterAssignment")
dom_UnaryExpression = Class(name="dom::UnaryExpression")
dom_BinaryExpression = Class(name="dom::BinaryExpression")
dom_CallExpression = Class(name="dom::CallExpression")
dom_ConditionalExpression = Class(name="dom::ConditionalExpression")
dom_Statement = Class(name="dom::Statement", is_abstract=True)
Statement = Class(name="Statement")
dom_VariableStatement = Class(name="dom::VariableStatement")
dom_VariableDeclaration = Class(name="dom::VariableDeclaration")
dom_EmptyStatement = Class(name="dom::EmptyStatement")
dom_ExpressionStatement = Class(name="dom::ExpressionStatement")
dom_IfStatement = Class(name="dom::IfStatement")
dom_IterationStatement = Class(name="dom::IterationStatement", is_abstract=True)
dom_DoStatement = Class(name="dom::DoStatement")
IterationStatement = Class(name="IterationStatement")
dom_WhileStatement = Class(name="dom::WhileStatement")
dom_ForStatement = Class(name="dom::ForStatement")
dom_IForInitializer = Class(name="dom::IForInitializer", is_abstract=True)
dom_ForInStatement = Class(name="dom::ForInStatement")
dom_ContinueStatement = Class(name="dom::ContinueStatement")
dom_BreakStatement = Class(name="dom::BreakStatement")
dom_ReturnStatement = Class(name="dom::ReturnStatement")
dom_WithStatement = Class(name="dom::WithStatement")
dom_SwitchStatement = Class(name="dom::SwitchStatement")
dom_SwitchElement = Class(name="dom::SwitchElement", is_abstract=True)
dom_CaseClause = Class(name="dom::CaseClause")
SwitchElement = Class(name="SwitchElement")
dom_DefaultClause = Class(name="dom::DefaultClause")
dom_LabeledStatement = Class(name="dom::LabeledStatement")
dom_TryStatement = Class(name="dom::TryStatement")
dom_CatchClause = Class(name="dom::CatchClause")
dom_FinallyClause = Class(name="dom::FinallyClause")
dom_ThrowStatement = Class(name="dom::ThrowStatement")
dom_Parameter = Class(name="dom::Parameter")
dom_Source = Class(name="dom::Source")
dom_ConstStatement = Class(name="dom::ConstStatement")
dom_PropertyIdentifier = Class(name="dom::PropertyIdentifier", is_abstract=True)
dom_FunctionExpression = Class(name="dom::FunctionExpression")
dom_XmlInitializer = Class(name="dom::XmlInitializer")
dom_XmlFragment = Class(name="dom::XmlFragment", is_abstract=True)
dom_AttributeIdentifier = Class(name="dom::AttributeIdentifier")
PropertyIdentifier = Class(name="PropertyIdentifier")
dom_ISelector = Class(name="dom::ISelector", is_abstract=True)
dom_QualifiedIdentifier = Class(name="dom::QualifiedIdentifier")
ISelector = Class(name="ISelector")
dom_IPropertySelector = Class(name="dom::IPropertySelector", is_abstract=True)
dom_IUnqualifiedSelector = Class(name="dom::IUnqualifiedSelector", is_abstract=True)
dom_WildcardIdentifier = Class(name="dom::WildcardIdentifier")
dom_ExpressionSelector = Class(name="dom::ExpressionSelector")
dom_XmlTextFragment = Class(name="dom::XmlTextFragment")
XmlFragment = Class(name="XmlFragment")
dom_XmlExpressionFragment = Class(name="dom::XmlExpressionFragment")
dom_DescendantAccessExpression = Class(name="dom::DescendantAccessExpression")
IUnqualifiedSelector = Class(name="IUnqualifiedSelector")
dom_DefaultXmlNamespaceStatement = Class(name="dom::DefaultXmlNamespaceStatement")
dom_ForEachInStatement = Class(name="dom::ForEachInStatement")
dom_FilterExpression = Class(name="dom::FilterExpression")

# dom_Node class attributes and methods
dom_Node_begin: Property = Property(name="begin", type=IntegerType)
dom_Node_end: Property = Property(name="end", type=IntegerType)
dom_Node.attributes={dom_Node_begin, dom_Node_end}

# dom_Comment class attributes and methods
dom_Comment_text: Property = Property(name="text", type=StringType)
dom_Comment.attributes={dom_Comment_text}

# Node class attributes and methods

# dom_Identifier class attributes and methods
dom_Identifier_name: Property = Property(name="name", type=StringType)
dom_Identifier.attributes={dom_Identifier_name}

# IPropertyName class attributes and methods

# IPropertySelector class attributes and methods

# IProperty class attributes and methods

# dom_VariableReference class attributes and methods

# Expression class attributes and methods

# dom_Label class attributes and methods
dom_Label_name: Property = Property(name="name", type=StringType)
dom_Label.attributes={dom_Label_name}

# dom_Expression class attributes and methods

# IArrayElement class attributes and methods

# IForInitializer class attributes and methods

# dom_NullLiteral class attributes and methods

# dom_BooleanLiteral class attributes and methods
dom_BooleanLiteral_text: Property = Property(name="text", type=StringType)
dom_BooleanLiteral.attributes={dom_BooleanLiteral_text}

# dom_NumericLiteral class attributes and methods
dom_NumericLiteral_text: Property = Property(name="text", type=StringType)
dom_NumericLiteral.attributes={dom_NumericLiteral_text}

# dom_StringLiteral class attributes and methods
dom_StringLiteral_text: Property = Property(name="text", type=StringType)
dom_StringLiteral.attributes={dom_StringLiteral_text}

# dom_RegularExpressionLiteral class attributes and methods
dom_RegularExpressionLiteral_text: Property = Property(name="text", type=StringType)
dom_RegularExpressionLiteral.attributes={dom_RegularExpressionLiteral_text}

# dom_ThisExpression class attributes and methods

# dom_ArrayLiteral class attributes and methods

# dom_Elision class attributes and methods

# dom_ObjectLiteral class attributes and methods

# dom_PropertyAssignment class attributes and methods

# dom_IPropertyName class attributes and methods

# dom_SimplePropertyAssignment class attributes and methods

# PropertyAssignment class attributes and methods

# dom_AccessorAssignment class attributes and methods

# dom_BlockStatement class attributes and methods

# dom_GetterAssignment class attributes and methods

# AccessorAssignment class attributes and methods

# dom_ParenthesizedExpression class attributes and methods

# dom_IArrayElement class attributes and methods

# dom_ArrayAccessExpression class attributes and methods

# dom_PropertyAccessExpression class attributes and methods

# dom_IProperty class attributes and methods

# dom_NewExpression class attributes and methods

# dom_SetterAssignment class attributes and methods

# dom_UnaryExpression class attributes and methods
dom_UnaryExpression_operation: Property = Property(name="operation", type=StringType)
dom_UnaryExpression.attributes={dom_UnaryExpression_operation}

# dom_BinaryExpression class attributes and methods
dom_BinaryExpression_operation: Property = Property(name="operation", type=StringType)
dom_BinaryExpression_operatorPosition: Property = Property(name="operatorPosition", type=IntegerType)
dom_BinaryExpression.attributes={dom_BinaryExpression_operation, dom_BinaryExpression_operatorPosition}

# dom_CallExpression class attributes and methods

# dom_ConditionalExpression class attributes and methods

# dom_Statement class attributes and methods

# Statement class attributes and methods

# dom_VariableStatement class attributes and methods

# dom_VariableDeclaration class attributes and methods

# dom_EmptyStatement class attributes and methods

# dom_ExpressionStatement class attributes and methods

# dom_IfStatement class attributes and methods

# dom_IterationStatement class attributes and methods

# dom_DoStatement class attributes and methods

# IterationStatement class attributes and methods

# dom_WhileStatement class attributes and methods

# dom_ForStatement class attributes and methods

# dom_IForInitializer class attributes and methods

# dom_ForInStatement class attributes and methods

# dom_ContinueStatement class attributes and methods

# dom_BreakStatement class attributes and methods

# dom_ReturnStatement class attributes and methods

# dom_WithStatement class attributes and methods

# dom_SwitchStatement class attributes and methods

# dom_SwitchElement class attributes and methods

# dom_CaseClause class attributes and methods

# SwitchElement class attributes and methods

# dom_DefaultClause class attributes and methods

# dom_LabeledStatement class attributes and methods

# dom_TryStatement class attributes and methods

# dom_CatchClause class attributes and methods

# dom_FinallyClause class attributes and methods

# dom_ThrowStatement class attributes and methods

# dom_Parameter class attributes and methods

# dom_Source class attributes and methods

# dom_ConstStatement class attributes and methods

# dom_PropertyIdentifier class attributes and methods

# dom_FunctionExpression class attributes and methods
dom_FunctionExpression_parametersPosition: Property = Property(name="parametersPosition", type=IntegerType)
dom_FunctionExpression.attributes={dom_FunctionExpression_parametersPosition}

# dom_XmlInitializer class attributes and methods

# dom_XmlFragment class attributes and methods

# dom_AttributeIdentifier class attributes and methods

# PropertyIdentifier class attributes and methods

# dom_ISelector class attributes and methods

# dom_QualifiedIdentifier class attributes and methods

# ISelector class attributes and methods

# dom_IPropertySelector class attributes and methods

# dom_IUnqualifiedSelector class attributes and methods

# dom_WildcardIdentifier class attributes and methods

# dom_ExpressionSelector class attributes and methods

# dom_XmlTextFragment class attributes and methods
dom_XmlTextFragment_text: Property = Property(name="text", type=StringType)
dom_XmlTextFragment.attributes={dom_XmlTextFragment_text}

# XmlFragment class attributes and methods

# dom_XmlExpressionFragment class attributes and methods

# dom_DescendantAccessExpression class attributes and methods

# IUnqualifiedSelector class attributes and methods

# dom_DefaultXmlNamespaceStatement class attributes and methods

# dom_ForEachInStatement class attributes and methods

# dom_FilterExpression class attributes and methods

# Relationships
variable0: BinaryAssociation = BinaryAssociation(
    name="variable0",
    ends={
        Property(name="dom_Identifier", type=dom_VariableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_VariableReference", type=dom_Identifier, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="dom_IArrayElement", type=dom_ArrayLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ArrayLiteral", type=dom_IArrayElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties2: BinaryAssociation = BinaryAssociation(
    name="properties2",
    ends={
        Property(name="dom_PropertyAssignment", type=dom_ObjectLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ObjectLiteral", type=dom_PropertyAssignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name3: BinaryAssociation = BinaryAssociation(
    name="name3",
    ends={
        Property(name="dom_IPropertyName", type=dom_PropertyAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_PropertyAssignment4", type=dom_IPropertyName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initializer5: BinaryAssociation = BinaryAssociation(
    name="initializer5",
    ends={
        Property(name="dom_Expression", type=dom_SimplePropertyAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_SimplePropertyAssignment", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body6: BinaryAssociation = BinaryAssociation(
    name="body6",
    ends={
        Property(name="dom_BlockStatement", type=dom_AccessorAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_AccessorAssignment", type=dom_BlockStatement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
enclosed9: BinaryAssociation = BinaryAssociation(
    name="enclosed9",
    ends={
        Property(name="dom_Expression10", type=dom_ParenthesizedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ParenthesizedExpression", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
array11: BinaryAssociation = BinaryAssociation(
    name="array11",
    ends={
        Property(name="dom_Expression12", type=dom_ArrayAccessExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ArrayAccessExpression", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
index13: BinaryAssociation = BinaryAssociation(
    name="index13",
    ends={
        Property(name="dom_Expression15", type=dom_ArrayAccessExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ArrayAccessExpression14", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object16: BinaryAssociation = BinaryAssociation(
    name="object16",
    ends={
        Property(name="dom_Expression17", type=dom_PropertyAccessExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_PropertyAccessExpression", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
property18: BinaryAssociation = BinaryAssociation(
    name="property18",
    ends={
        Property(name="dom_IProperty", type=dom_PropertyAccessExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_PropertyAccessExpression19", type=dom_IProperty, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
constructor20: BinaryAssociation = BinaryAssociation(
    name="constructor20",
    ends={
        Property(name="dom_Expression21", type=dom_NewExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_NewExpression", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments22: BinaryAssociation = BinaryAssociation(
    name="arguments22",
    ends={
        Property(name="dom_Expression24", type=dom_NewExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_NewExpression23", type=dom_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter7: BinaryAssociation = BinaryAssociation(
    name="parameter7",
    ends={
        Property(name="dom_Identifier8", type=dom_SetterAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_SetterAssignment", type=dom_Identifier, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
applicant25: BinaryAssociation = BinaryAssociation(
    name="applicant25",
    ends={
        Property(name="dom_CallExpression", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="dom_Expression26", type=dom_CallExpression, multiplicity=Multiplicity(1, 1))
    }
)
arguments27: BinaryAssociation = BinaryAssociation(
    name="arguments27",
    ends={
        Property(name="dom_Expression29", type=dom_CallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_CallExpression28", type=dom_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument30: BinaryAssociation = BinaryAssociation(
    name="argument30",
    ends={
        Property(name="dom_Expression31", type=dom_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_UnaryExpression", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right34: BinaryAssociation = BinaryAssociation(
    name="right34",
    ends={
        Property(name="dom_Expression36", type=dom_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_BinaryExpression35", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left32: BinaryAssociation = BinaryAssociation(
    name="left32",
    ends={
        Property(name="dom_Expression33", type=dom_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_BinaryExpression", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
predicate37: BinaryAssociation = BinaryAssociation(
    name="predicate37",
    ends={
        Property(name="dom_Expression38", type=dom_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ConditionalExpression", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
consequent39: BinaryAssociation = BinaryAssociation(
    name="consequent39",
    ends={
        Property(name="dom_Expression41", type=dom_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ConditionalExpression40", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
alternative42: BinaryAssociation = BinaryAssociation(
    name="alternative42",
    ends={
        Property(name="dom_Expression44", type=dom_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ConditionalExpression43", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
declarations47: BinaryAssociation = BinaryAssociation(
    name="declarations47",
    ends={
        Property(name="dom_VariableDeclaration", type=dom_VariableStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_VariableStatement", type=dom_VariableDeclaration, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
identifier48: BinaryAssociation = BinaryAssociation(
    name="identifier48",
    ends={
        Property(name="dom_Identifier50", type=dom_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_VariableDeclaration49", type=dom_Identifier, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initializer51: BinaryAssociation = BinaryAssociation(
    name="initializer51",
    ends={
        Property(name="dom_Expression53", type=dom_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_VariableDeclaration52", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression54: BinaryAssociation = BinaryAssociation(
    name="expression54",
    ends={
        Property(name="dom_Expression55", type=dom_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ExpressionStatement", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
predicate56: BinaryAssociation = BinaryAssociation(
    name="predicate56",
    ends={
        Property(name="dom_Expression57", type=dom_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_IfStatement", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
consequent58: BinaryAssociation = BinaryAssociation(
    name="consequent58",
    ends={
        Property(name="dom_Statement60", type=dom_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_IfStatement59", type=dom_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements45: BinaryAssociation = BinaryAssociation(
    name="statements45",
    ends={
        Property(name="dom_Statement", type=dom_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_BlockStatement46", type=dom_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body64: BinaryAssociation = BinaryAssociation(
    name="body64",
    ends={
        Property(name="dom_Statement65", type=dom_IterationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_IterationStatement", type=dom_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition66: BinaryAssociation = BinaryAssociation(
    name="condition66",
    ends={
        Property(name="dom_Expression67", type=dom_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_DoStatement", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition68: BinaryAssociation = BinaryAssociation(
    name="condition68",
    ends={
        Property(name="dom_Expression69", type=dom_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_WhileStatement", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialization70: BinaryAssociation = BinaryAssociation(
    name="initialization70",
    ends={
        Property(name="dom_IForInitializer", type=dom_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ForStatement", type=dom_IForInitializer, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition71: BinaryAssociation = BinaryAssociation(
    name="condition71",
    ends={
        Property(name="dom_Expression73", type=dom_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ForStatement72", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
increment74: BinaryAssociation = BinaryAssociation(
    name="increment74",
    ends={
        Property(name="dom_Expression76", type=dom_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ForStatement75", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
alternative61: BinaryAssociation = BinaryAssociation(
    name="alternative61",
    ends={
        Property(name="dom_Statement63", type=dom_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_IfStatement62", type=dom_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
item77: BinaryAssociation = BinaryAssociation(
    name="item77",
    ends={
        Property(name="dom_IForInitializer78", type=dom_ForInStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ForInStatement", type=dom_IForInitializer, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collection79: BinaryAssociation = BinaryAssociation(
    name="collection79",
    ends={
        Property(name="dom_Expression81", type=dom_ForInStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ForInStatement80", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
label82: BinaryAssociation = BinaryAssociation(
    name="label82",
    ends={
        Property(name="dom_Label", type=dom_ContinueStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ContinueStatement", type=dom_Label, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
label83: BinaryAssociation = BinaryAssociation(
    name="label83",
    ends={
        Property(name="dom_Label84", type=dom_BreakStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_BreakStatement", type=dom_Label, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression85: BinaryAssociation = BinaryAssociation(
    name="expression85",
    ends={
        Property(name="dom_Expression86", type=dom_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ReturnStatement", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression87: BinaryAssociation = BinaryAssociation(
    name="expression87",
    ends={
        Property(name="dom_Expression88", type=dom_WithStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_WithStatement", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement89: BinaryAssociation = BinaryAssociation(
    name="statement89",
    ends={
        Property(name="dom_Statement91", type=dom_WithStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_WithStatement90", type=dom_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
selector92: BinaryAssociation = BinaryAssociation(
    name="selector92",
    ends={
        Property(name="dom_Expression93", type=dom_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_SwitchStatement", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elements94: BinaryAssociation = BinaryAssociation(
    name="elements94",
    ends={
        Property(name="dom_SwitchElement", type=dom_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_SwitchStatement95", type=dom_SwitchElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements96: BinaryAssociation = BinaryAssociation(
    name="statements96",
    ends={
        Property(name="dom_Statement98", type=dom_SwitchElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_SwitchElement97", type=dom_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression99: BinaryAssociation = BinaryAssociation(
    name="expression99",
    ends={
        Property(name="dom_Expression100", type=dom_CaseClause, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_CaseClause", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
label101: BinaryAssociation = BinaryAssociation(
    name="label101",
    ends={
        Property(name="dom_Label102", type=dom_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_LabeledStatement", type=dom_Label, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exception106: BinaryAssociation = BinaryAssociation(
    name="exception106",
    ends={
        Property(name="dom_Expression107", type=dom_ThrowStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ThrowStatement", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body108: BinaryAssociation = BinaryAssociation(
    name="body108",
    ends={
        Property(name="dom_BlockStatement109", type=dom_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_TryStatement", type=dom_BlockStatement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
catches110: BinaryAssociation = BinaryAssociation(
    name="catches110",
    ends={
        Property(name="dom_CatchClause", type=dom_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_TryStatement111", type=dom_CatchClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
finallyClause112: BinaryAssociation = BinaryAssociation(
    name="finallyClause112",
    ends={
        Property(name="dom_FinallyClause", type=dom_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_TryStatement113", type=dom_FinallyClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exception114: BinaryAssociation = BinaryAssociation(
    name="exception114",
    ends={
        Property(name="dom_Identifier116", type=dom_CatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_CatchClause115", type=dom_Identifier, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
filter117: BinaryAssociation = BinaryAssociation(
    name="filter117",
    ends={
        Property(name="dom_Expression119", type=dom_CatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_CatchClause118", type=dom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body120: BinaryAssociation = BinaryAssociation(
    name="body120",
    ends={
        Property(name="dom_BlockStatement122", type=dom_CatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_CatchClause121", type=dom_BlockStatement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement103: BinaryAssociation = BinaryAssociation(
    name="statement103",
    ends={
        Property(name="dom_Statement105", type=dom_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_LabeledStatement104", type=dom_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
documentation126: BinaryAssociation = BinaryAssociation(
    name="documentation126",
    ends={
        Property(name="dom_Comment", type=dom_FunctionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_FunctionExpression", type=dom_Comment, multiplicity=Multiplicity(0, 1))
    }
)
identifier127: BinaryAssociation = BinaryAssociation(
    name="identifier127",
    ends={
        Property(name="dom_Identifier129", type=dom_FunctionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_FunctionExpression128", type=dom_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters130: BinaryAssociation = BinaryAssociation(
    name="parameters130",
    ends={
        Property(name="dom_Parameter", type=dom_FunctionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_FunctionExpression131", type=dom_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body132: BinaryAssociation = BinaryAssociation(
    name="body132",
    ends={
        Property(name="dom_BlockStatement134", type=dom_FunctionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_FunctionExpression133", type=dom_BlockStatement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name135: BinaryAssociation = BinaryAssociation(
    name="name135",
    ends={
        Property(name="dom_Identifier137", type=dom_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Parameter136", type=dom_Identifier, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements138: BinaryAssociation = BinaryAssociation(
    name="statements138",
    ends={
        Property(name="dom_Statement139", type=dom_Source, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_Source", type=dom_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declarations140: BinaryAssociation = BinaryAssociation(
    name="declarations140",
    ends={
        Property(name="dom_VariableDeclaration141", type=dom_ConstStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ConstStatement", type=dom_VariableDeclaration, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
body123: BinaryAssociation = BinaryAssociation(
    name="body123",
    ends={
        Property(name="dom_BlockStatement125", type=dom_FinallyClause, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_FinallyClause124", type=dom_BlockStatement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fragments142: BinaryAssociation = BinaryAssociation(
    name="fragments142",
    ends={
        Property(name="dom_XmlFragment", type=dom_XmlInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_XmlInitializer", type=dom_XmlFragment, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
selector143: BinaryAssociation = BinaryAssociation(
    name="selector143",
    ends={
        Property(name="dom_ISelector", type=dom_AttributeIdentifier, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_AttributeIdentifier", type=dom_ISelector, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
namespace144: BinaryAssociation = BinaryAssociation(
    name="namespace144",
    ends={
        Property(name="dom_IPropertySelector", type=dom_QualifiedIdentifier, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_QualifiedIdentifier", type=dom_IPropertySelector, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
member145: BinaryAssociation = BinaryAssociation(
    name="member145",
    ends={
        Property(name="dom_IUnqualifiedSelector", type=dom_QualifiedIdentifier, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_QualifiedIdentifier146", type=dom_IUnqualifiedSelector, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
index147: BinaryAssociation = BinaryAssociation(
    name="index147",
    ends={
        Property(name="dom_Expression148", type=dom_ExpressionSelector, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ExpressionSelector", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression149: BinaryAssociation = BinaryAssociation(
    name="expression149",
    ends={
        Property(name="dom_Expression150", type=dom_XmlExpressionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_XmlExpressionFragment", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object151: BinaryAssociation = BinaryAssociation(
    name="object151",
    ends={
        Property(name="dom_Expression152", type=dom_DescendantAccessExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_DescendantAccessExpression", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object156: BinaryAssociation = BinaryAssociation(
    name="object156",
    ends={
        Property(name="dom_Expression157", type=dom_FilterExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_FilterExpression", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
filter158: BinaryAssociation = BinaryAssociation(
    name="filter158",
    ends={
        Property(name="dom_Expression160", type=dom_FilterExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_FilterExpression159", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression161: BinaryAssociation = BinaryAssociation(
    name="expression161",
    ends={
        Property(name="dom_Expression162", type=dom_DefaultXmlNamespaceStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_DefaultXmlNamespaceStatement", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
item163: BinaryAssociation = BinaryAssociation(
    name="item163",
    ends={
        Property(name="dom_IForInitializer164", type=dom_ForEachInStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ForEachInStatement", type=dom_IForInitializer, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collection165: BinaryAssociation = BinaryAssociation(
    name="collection165",
    ends={
        Property(name="dom_Expression167", type=dom_ForEachInStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_ForEachInStatement166", type=dom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
property153: BinaryAssociation = BinaryAssociation(
    name="property153",
    ends={
        Property(name="dom_IProperty155", type=dom_DescendantAccessExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dom_DescendantAccessExpression154", type=dom_IProperty, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_dom_Comment_Node = Generalization(general=Node, specific=dom_Comment)
gen_dom_Identifier_Node = Generalization(general=Node, specific=dom_Identifier)
gen_dom_Identifier_IPropertyName = Generalization(general=IPropertyName, specific=dom_Identifier)
gen_dom_Identifier_IPropertySelector = Generalization(general=IPropertySelector, specific=dom_Identifier)
gen_dom_Identifier_IProperty = Generalization(general=IProperty, specific=dom_Identifier)
gen_dom_Label_Node = Generalization(general=Node, specific=dom_Label)
gen_dom_Expression_Node = Generalization(general=Node, specific=dom_Expression)
gen_dom_Expression_IArrayElement = Generalization(general=IArrayElement, specific=dom_Expression)
gen_dom_Expression_IForInitializer = Generalization(general=IForInitializer, specific=dom_Expression)
gen_dom_NullLiteral_Expression = Generalization(general=Expression, specific=dom_NullLiteral)
gen_dom_BooleanLiteral_Expression = Generalization(general=Expression, specific=dom_BooleanLiteral)
gen_dom_NumericLiteral_Expression = Generalization(general=Expression, specific=dom_NumericLiteral)
gen_dom_NumericLiteral_IPropertyName = Generalization(general=IPropertyName, specific=dom_NumericLiteral)
gen_dom_StringLiteral_Expression = Generalization(general=Expression, specific=dom_StringLiteral)
gen_dom_StringLiteral_IPropertyName = Generalization(general=IPropertyName, specific=dom_StringLiteral)
gen_dom_RegularExpressionLiteral_Expression = Generalization(general=Expression, specific=dom_RegularExpressionLiteral)
gen_dom_ThisExpression_Expression = Generalization(general=Expression, specific=dom_ThisExpression)
gen_dom_ArrayLiteral_Expression = Generalization(general=Expression, specific=dom_ArrayLiteral)
gen_dom_VariableReference_Expression = Generalization(general=Expression, specific=dom_VariableReference)
gen_dom_IArrayElement_Node = Generalization(general=Node, specific=dom_IArrayElement)
gen_dom_Elision_IArrayElement = Generalization(general=IArrayElement, specific=dom_Elision)
gen_dom_ObjectLiteral_Expression = Generalization(general=Expression, specific=dom_ObjectLiteral)
gen_dom_PropertyAssignment_Node = Generalization(general=Node, specific=dom_PropertyAssignment)
gen_dom_IPropertyName_Node = Generalization(general=Node, specific=dom_IPropertyName)
gen_dom_SimplePropertyAssignment_PropertyAssignment = Generalization(general=PropertyAssignment, specific=dom_SimplePropertyAssignment)
gen_dom_AccessorAssignment_PropertyAssignment = Generalization(general=PropertyAssignment, specific=dom_AccessorAssignment)
gen_dom_GetterAssignment_AccessorAssignment = Generalization(general=AccessorAssignment, specific=dom_GetterAssignment)
gen_dom_ParenthesizedExpression_Expression = Generalization(general=Expression, specific=dom_ParenthesizedExpression)
gen_dom_ArrayAccessExpression_Expression = Generalization(general=Expression, specific=dom_ArrayAccessExpression)
gen_dom_PropertyAccessExpression_Expression = Generalization(general=Expression, specific=dom_PropertyAccessExpression)
gen_dom_NewExpression_Expression = Generalization(general=Expression, specific=dom_NewExpression)
gen_dom_SetterAssignment_AccessorAssignment = Generalization(general=AccessorAssignment, specific=dom_SetterAssignment)
gen_dom_UnaryExpression_Expression = Generalization(general=Expression, specific=dom_UnaryExpression)
gen_dom_BinaryExpression_Expression = Generalization(general=Expression, specific=dom_BinaryExpression)
gen_dom_CallExpression_Expression = Generalization(general=Expression, specific=dom_CallExpression)
gen_dom_ConditionalExpression_Expression = Generalization(general=Expression, specific=dom_ConditionalExpression)
gen_dom_Statement_Node = Generalization(general=Node, specific=dom_Statement)
gen_dom_BlockStatement_Statement = Generalization(general=Statement, specific=dom_BlockStatement)
gen_dom_VariableStatement_Statement = Generalization(general=Statement, specific=dom_VariableStatement)
gen_dom_VariableStatement_IForInitializer = Generalization(general=IForInitializer, specific=dom_VariableStatement)
gen_dom_VariableDeclaration_Node = Generalization(general=Node, specific=dom_VariableDeclaration)
gen_dom_EmptyStatement_Statement = Generalization(general=Statement, specific=dom_EmptyStatement)
gen_dom_ExpressionStatement_Statement = Generalization(general=Statement, specific=dom_ExpressionStatement)
gen_dom_IfStatement_Statement = Generalization(general=Statement, specific=dom_IfStatement)
gen_dom_IterationStatement_Statement = Generalization(general=Statement, specific=dom_IterationStatement)
gen_dom_DoStatement_IterationStatement = Generalization(general=IterationStatement, specific=dom_DoStatement)
gen_dom_WhileStatement_IterationStatement = Generalization(general=IterationStatement, specific=dom_WhileStatement)
gen_dom_ForStatement_IterationStatement = Generalization(general=IterationStatement, specific=dom_ForStatement)
gen_dom_IForInitializer_Node = Generalization(general=Node, specific=dom_IForInitializer)
gen_dom_ForInStatement_IterationStatement = Generalization(general=IterationStatement, specific=dom_ForInStatement)
gen_dom_ContinueStatement_Statement = Generalization(general=Statement, specific=dom_ContinueStatement)
gen_dom_BreakStatement_Statement = Generalization(general=Statement, specific=dom_BreakStatement)
gen_dom_ReturnStatement_Statement = Generalization(general=Statement, specific=dom_ReturnStatement)
gen_dom_WithStatement_Statement = Generalization(general=Statement, specific=dom_WithStatement)
gen_dom_SwitchStatement_Statement = Generalization(general=Statement, specific=dom_SwitchStatement)
gen_dom_SwitchElement_Node = Generalization(general=Node, specific=dom_SwitchElement)
gen_dom_CaseClause_SwitchElement = Generalization(general=SwitchElement, specific=dom_CaseClause)
gen_dom_DefaultClause_SwitchElement = Generalization(general=SwitchElement, specific=dom_DefaultClause)
gen_dom_LabeledStatement_Statement = Generalization(general=Statement, specific=dom_LabeledStatement)
gen_dom_TryStatement_Statement = Generalization(general=Statement, specific=dom_TryStatement)
gen_dom_CatchClause_Node = Generalization(general=Node, specific=dom_CatchClause)
gen_dom_FinallyClause_Node = Generalization(general=Node, specific=dom_FinallyClause)
gen_dom_ThrowStatement_Statement = Generalization(general=Statement, specific=dom_ThrowStatement)
gen_dom_Parameter_Node = Generalization(general=Node, specific=dom_Parameter)
gen_dom_Source_Node = Generalization(general=Node, specific=dom_Source)
gen_dom_ConstStatement_Statement = Generalization(general=Statement, specific=dom_ConstStatement)
gen_dom_FunctionExpression_Expression = Generalization(general=Expression, specific=dom_FunctionExpression)
gen_dom_IProperty_Node = Generalization(general=Node, specific=dom_IProperty)
gen_dom_XmlInitializer_Expression = Generalization(general=Expression, specific=dom_XmlInitializer)
gen_dom_AttributeIdentifier_PropertyIdentifier = Generalization(general=PropertyIdentifier, specific=dom_AttributeIdentifier)
gen_dom_ISelector_Node = Generalization(general=Node, specific=dom_ISelector)
gen_dom_QualifiedIdentifier_PropertyIdentifier = Generalization(general=PropertyIdentifier, specific=dom_QualifiedIdentifier)
gen_dom_QualifiedIdentifier_ISelector = Generalization(general=ISelector, specific=dom_QualifiedIdentifier)
gen_dom_IUnqualifiedSelector_ISelector = Generalization(general=ISelector, specific=dom_IUnqualifiedSelector)
gen_dom_WildcardIdentifier_PropertyIdentifier = Generalization(general=PropertyIdentifier, specific=dom_WildcardIdentifier)
gen_dom_WildcardIdentifier_IPropertySelector = Generalization(general=IPropertySelector, specific=dom_WildcardIdentifier)
gen_dom_ExpressionSelector_IUnqualifiedSelector = Generalization(general=IUnqualifiedSelector, specific=dom_ExpressionSelector)
gen_dom_PropertyIdentifier_Expression = Generalization(general=Expression, specific=dom_PropertyIdentifier)
gen_dom_PropertyIdentifier_IProperty = Generalization(general=IProperty, specific=dom_PropertyIdentifier)
gen_dom_XmlFragment_Node = Generalization(general=Node, specific=dom_XmlFragment)
gen_dom_XmlTextFragment_XmlFragment = Generalization(general=XmlFragment, specific=dom_XmlTextFragment)
gen_dom_XmlExpressionFragment_XmlFragment = Generalization(general=XmlFragment, specific=dom_XmlExpressionFragment)
gen_dom_DescendantAccessExpression_Expression = Generalization(general=Expression, specific=dom_DescendantAccessExpression)
gen_dom_IPropertySelector_IUnqualifiedSelector = Generalization(general=IUnqualifiedSelector, specific=dom_IPropertySelector)
gen_dom_DefaultXmlNamespaceStatement_Statement = Generalization(general=Statement, specific=dom_DefaultXmlNamespaceStatement)
gen_dom_ForEachInStatement_IterationStatement = Generalization(general=IterationStatement, specific=dom_ForEachInStatement)
gen_dom_FilterExpression_Expression = Generalization(general=Expression, specific=dom_FilterExpression)

# Domain Model
domain_model = DomainModel(
    name="dom",
    types={dom_Node, dom_Comment, Node, dom_Identifier, IPropertyName, IPropertySelector, IProperty, dom_VariableReference, Expression, dom_Label, dom_Expression, IArrayElement, IForInitializer, dom_NullLiteral, dom_BooleanLiteral, dom_NumericLiteral, dom_StringLiteral, dom_RegularExpressionLiteral, dom_ThisExpression, dom_ArrayLiteral, dom_Elision, dom_ObjectLiteral, dom_PropertyAssignment, dom_IPropertyName, dom_SimplePropertyAssignment, PropertyAssignment, dom_AccessorAssignment, dom_BlockStatement, dom_GetterAssignment, AccessorAssignment, dom_ParenthesizedExpression, dom_IArrayElement, dom_ArrayAccessExpression, dom_PropertyAccessExpression, dom_IProperty, dom_NewExpression, dom_SetterAssignment, dom_UnaryExpression, dom_BinaryExpression, dom_CallExpression, dom_ConditionalExpression, dom_Statement, Statement, dom_VariableStatement, dom_VariableDeclaration, dom_EmptyStatement, dom_ExpressionStatement, dom_IfStatement, dom_IterationStatement, dom_DoStatement, IterationStatement, dom_WhileStatement, dom_ForStatement, dom_IForInitializer, dom_ForInStatement, dom_ContinueStatement, dom_BreakStatement, dom_ReturnStatement, dom_WithStatement, dom_SwitchStatement, dom_SwitchElement, dom_CaseClause, SwitchElement, dom_DefaultClause, dom_LabeledStatement, dom_TryStatement, dom_CatchClause, dom_FinallyClause, dom_ThrowStatement, dom_Parameter, dom_Source, dom_ConstStatement, dom_PropertyIdentifier, dom_FunctionExpression, dom_XmlInitializer, dom_XmlFragment, dom_AttributeIdentifier, PropertyIdentifier, dom_ISelector, dom_QualifiedIdentifier, ISelector, dom_IPropertySelector, dom_IUnqualifiedSelector, dom_WildcardIdentifier, dom_ExpressionSelector, dom_XmlTextFragment, XmlFragment, dom_XmlExpressionFragment, dom_DescendantAccessExpression, IUnqualifiedSelector, dom_DefaultXmlNamespaceStatement, dom_ForEachInStatement, dom_FilterExpression, UnaryOperator, BinaryOperator},
    associations={variable0, elements1, properties2, name3, initializer5, body6, enclosed9, array11, index13, object16, property18, constructor20, arguments22, parameter7, applicant25, arguments27, argument30, right34, left32, predicate37, consequent39, alternative42, declarations47, identifier48, initializer51, expression54, predicate56, consequent58, statements45, body64, condition66, condition68, initialization70, condition71, increment74, alternative61, item77, collection79, label82, label83, expression85, expression87, statement89, selector92, elements94, statements96, expression99, label101, exception106, body108, catches110, finallyClause112, exception114, filter117, body120, statement103, documentation126, identifier127, parameters130, body132, name135, statements138, declarations140, body123, fragments142, selector143, namespace144, member145, index147, expression149, object151, object156, filter158, expression161, item163, collection165, property153},
    generalizations={gen_dom_Comment_Node, gen_dom_Identifier_Node, gen_dom_Identifier_IPropertyName, gen_dom_Identifier_IPropertySelector, gen_dom_Identifier_IProperty, gen_dom_Label_Node, gen_dom_Expression_Node, gen_dom_Expression_IArrayElement, gen_dom_Expression_IForInitializer, gen_dom_NullLiteral_Expression, gen_dom_BooleanLiteral_Expression, gen_dom_NumericLiteral_Expression, gen_dom_NumericLiteral_IPropertyName, gen_dom_StringLiteral_Expression, gen_dom_StringLiteral_IPropertyName, gen_dom_RegularExpressionLiteral_Expression, gen_dom_ThisExpression_Expression, gen_dom_ArrayLiteral_Expression, gen_dom_VariableReference_Expression, gen_dom_IArrayElement_Node, gen_dom_Elision_IArrayElement, gen_dom_ObjectLiteral_Expression, gen_dom_PropertyAssignment_Node, gen_dom_IPropertyName_Node, gen_dom_SimplePropertyAssignment_PropertyAssignment, gen_dom_AccessorAssignment_PropertyAssignment, gen_dom_GetterAssignment_AccessorAssignment, gen_dom_ParenthesizedExpression_Expression, gen_dom_ArrayAccessExpression_Expression, gen_dom_PropertyAccessExpression_Expression, gen_dom_NewExpression_Expression, gen_dom_SetterAssignment_AccessorAssignment, gen_dom_UnaryExpression_Expression, gen_dom_BinaryExpression_Expression, gen_dom_CallExpression_Expression, gen_dom_ConditionalExpression_Expression, gen_dom_Statement_Node, gen_dom_BlockStatement_Statement, gen_dom_VariableStatement_Statement, gen_dom_VariableStatement_IForInitializer, gen_dom_VariableDeclaration_Node, gen_dom_EmptyStatement_Statement, gen_dom_ExpressionStatement_Statement, gen_dom_IfStatement_Statement, gen_dom_IterationStatement_Statement, gen_dom_DoStatement_IterationStatement, gen_dom_WhileStatement_IterationStatement, gen_dom_ForStatement_IterationStatement, gen_dom_IForInitializer_Node, gen_dom_ForInStatement_IterationStatement, gen_dom_ContinueStatement_Statement, gen_dom_BreakStatement_Statement, gen_dom_ReturnStatement_Statement, gen_dom_WithStatement_Statement, gen_dom_SwitchStatement_Statement, gen_dom_SwitchElement_Node, gen_dom_CaseClause_SwitchElement, gen_dom_DefaultClause_SwitchElement, gen_dom_LabeledStatement_Statement, gen_dom_TryStatement_Statement, gen_dom_CatchClause_Node, gen_dom_FinallyClause_Node, gen_dom_ThrowStatement_Statement, gen_dom_Parameter_Node, gen_dom_Source_Node, gen_dom_ConstStatement_Statement, gen_dom_FunctionExpression_Expression, gen_dom_IProperty_Node, gen_dom_XmlInitializer_Expression, gen_dom_AttributeIdentifier_PropertyIdentifier, gen_dom_ISelector_Node, gen_dom_QualifiedIdentifier_PropertyIdentifier, gen_dom_QualifiedIdentifier_ISelector, gen_dom_IUnqualifiedSelector_ISelector, gen_dom_WildcardIdentifier_PropertyIdentifier, gen_dom_WildcardIdentifier_IPropertySelector, gen_dom_ExpressionSelector_IUnqualifiedSelector, gen_dom_PropertyIdentifier_Expression, gen_dom_PropertyIdentifier_IProperty, gen_dom_XmlFragment_Node, gen_dom_XmlTextFragment_XmlFragment, gen_dom_XmlExpressionFragment_XmlFragment, gen_dom_DescendantAccessExpression_Expression, gen_dom_IPropertySelector_IUnqualifiedSelector, gen_dom_DefaultXmlNamespaceStatement_Statement, gen_dom_ForEachInStatement_IterationStatement, gen_dom_FilterExpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)