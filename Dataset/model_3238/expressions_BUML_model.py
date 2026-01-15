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
TernaryOperation: Enumeration = Enumeration(
    name="TernaryOperation",
    literals={
            EnumerationLiteral(name="QUESTION")
    }
)

UnaryOperation: Enumeration = Enumeration(
    name="UnaryOperation",
    literals={
            EnumerationLiteral(name="NOT"),
			EnumerationLiteral(name="PLUS"),
			EnumerationLiteral(name="MINUS")
    }
)

ResolvedType: Enumeration = Enumeration(
    name="ResolvedType",
    literals={
            EnumerationLiteral(name="integer"),
			EnumerationLiteral(name="boolean"),
			EnumerationLiteral(name="natural"),
			EnumerationLiteral(name="clock"),
			EnumerationLiteral(name="float"),
			EnumerationLiteral(name="resource"),
			EnumerationLiteral(name="unknown")
    }
)

BinaryOperation: Enumeration = Enumeration(
    name="BinaryOperation",
    literals={
            EnumerationLiteral(name="ASSIGN_SUB"),
			EnumerationLiteral(name="ASSIGN_MUL"),
			EnumerationLiteral(name="ASSIGN_DIV"),
			EnumerationLiteral(name="ASSIGN_MOD"),
			EnumerationLiteral(name="DIFF"),
			EnumerationLiteral(name="ADD"),
			EnumerationLiteral(name="SUB"),
			EnumerationLiteral(name="MUL"),
			EnumerationLiteral(name="DIV"),
			EnumerationLiteral(name="MOD"),
			EnumerationLiteral(name="LT"),
			EnumerationLiteral(name="LE"),
			EnumerationLiteral(name="EQ"),
			EnumerationLiteral(name="GE"),
			EnumerationLiteral(name="GT"),
			EnumerationLiteral(name="NE"),
			EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="ASSIGN"),
			EnumerationLiteral(name="ASSIGN_ADD")
    }
)

# Classes
expressions_ast_AbstractRoot = Class(name="expressions::ast::AbstractRoot", is_abstract=True)
expressions_ast_LogicalRoot = Class(name="expressions::ast::LogicalRoot")
expressions_ast_ResourceRoot = Class(name="expressions::ast::ResourceRoot")
expressions_ast_Expression = Class(name="expressions::ast::Expression", is_abstract=True)
expressions_ast_TernaryExpression = Class(name="expressions::ast::TernaryExpression")
VariableReference = Class(name="VariableReference")
expressions_ast_ActionRoot = Class(name="expressions::ast::ActionRoot")
AbstractRoot = Class(name="AbstractRoot")
Expression = Class(name="Expression")
expressions_ast_UnaryExpression = Class(name="expressions::ast::UnaryExpression")
expressions_ast_BinaryExpression = Class(name="expressions::ast::BinaryExpression")
ast_expressions_EObject = Class(name="ast::expressions::EObject")
expressions_ast_Constant = Class(name="expressions::ast::Constant")
expressions_ast_Literal = Class(name="expressions::ast::Literal")
expressions_ast_VariableReference = Class(name="expressions::ast::VariableReference")
expressions_ast_AstVisitor = Class(name="expressions::ast::AstVisitor", is_abstract=True)
expressions_type_BaseType = Class(name="expressions::type::BaseType", is_abstract=True)
Type = Class(name="Type")
expressions_type_IntegerType = Class(name="expressions::type::IntegerType")
BaseType = Class(name="BaseType")
expressions_type_BooleanType = Class(name="expressions::type::BooleanType")
expressions_type_NaturalType = Class(name="expressions::type::NaturalType")
expressions_type_ClockType = Class(name="expressions::type::ClockType")
expressions_type_FloatType = Class(name="expressions::type::FloatType")
expressions_type_ResourceType = Class(name="expressions::type::ResourceType")
expressions_type_AnyType = Class(name="expressions::type::AnyType")
expressions_type_Type = Class(name="expressions::type::Type", is_abstract=True)

# expressions_ast_AbstractRoot class attributes and methods
expressions_ast_AbstractRoot_type: Property = Property(name="type", type=StringType)
expressions_ast_AbstractRoot.attributes={expressions_ast_AbstractRoot_type}

# expressions_ast_LogicalRoot class attributes and methods

# expressions_ast_ResourceRoot class attributes and methods

# expressions_ast_Expression class attributes and methods
expressions_ast_Expression_type: Property = Property(name="type", type=StringType)
expressions_ast_Expression_text: Property = Property(name="text", type=StringType)
expressions_ast_Expression_m_visit: Method = Method(name="visit", parameters={Parameter(name='visitor')})
expressions_ast_Expression.attributes={expressions_ast_Expression_type, expressions_ast_Expression_text}
expressions_ast_Expression.methods={expressions_ast_Expression_m_visit}

# expressions_ast_TernaryExpression class attributes and methods
expressions_ast_TernaryExpression_operation: Property = Property(name="operation", type=StringType)
expressions_ast_TernaryExpression.attributes={expressions_ast_TernaryExpression_operation}

# VariableReference class attributes and methods

# expressions_ast_ActionRoot class attributes and methods

# AbstractRoot class attributes and methods

# Expression class attributes and methods

# expressions_ast_UnaryExpression class attributes and methods
expressions_ast_UnaryExpression_operation: Property = Property(name="operation", type=StringType)
expressions_ast_UnaryExpression.attributes={expressions_ast_UnaryExpression_operation}

# expressions_ast_BinaryExpression class attributes and methods
expressions_ast_BinaryExpression_operation: Property = Property(name="operation", type=StringType)
expressions_ast_BinaryExpression.attributes={expressions_ast_BinaryExpression_operation}

# ast_expressions_EObject class attributes and methods

# expressions_ast_Constant class attributes and methods
expressions_ast_Constant_value: Property = Property(name="value", type=StringType)
expressions_ast_Constant.attributes={expressions_ast_Constant_value}

# expressions_ast_Literal class attributes and methods
expressions_ast_Literal_value: Property = Property(name="value", type=StringType)
expressions_ast_Literal.attributes={expressions_ast_Literal_value}

# expressions_ast_VariableReference class attributes and methods
expressions_ast_VariableReference_name: Property = Property(name="name", type=StringType)
expressions_ast_VariableReference.attributes={expressions_ast_VariableReference_name}

# expressions_ast_AstVisitor class attributes and methods
expressions_ast_AstVisitor_m_visitTernaryExpression: Method = Method(name="visitTernaryExpression", parameters={Parameter(name='node')})
expressions_ast_AstVisitor_m_visitBinaryExpression: Method = Method(name="visitBinaryExpression", parameters={Parameter(name='node')})
expressions_ast_AstVisitor_m_visitUnaryExpression: Method = Method(name="visitUnaryExpression", parameters={Parameter(name='node')})
expressions_ast_AstVisitor_m_visitVariableReference: Method = Method(name="visitVariableReference", parameters={Parameter(name='node')})
expressions_ast_AstVisitor_m_visitConstant: Method = Method(name="visitConstant", parameters={Parameter(name='node')})
expressions_ast_AstVisitor_m_visitLiteral: Method = Method(name="visitLiteral", parameters={Parameter(name='node')})
expressions_ast_AstVisitor.methods={expressions_ast_AstVisitor_m_visitUnaryExpression, expressions_ast_AstVisitor_m_visitConstant, expressions_ast_AstVisitor_m_visitTernaryExpression, expressions_ast_AstVisitor_m_visitLiteral, expressions_ast_AstVisitor_m_visitBinaryExpression, expressions_ast_AstVisitor_m_visitVariableReference}

# expressions_type_BaseType class attributes and methods

# Type class attributes and methods

# expressions_type_IntegerType class attributes and methods

# BaseType class attributes and methods

# expressions_type_BooleanType class attributes and methods

# expressions_type_NaturalType class attributes and methods

# expressions_type_ClockType class attributes and methods

# expressions_type_FloatType class attributes and methods

# expressions_type_ResourceType class attributes and methods

# expressions_type_AnyType class attributes and methods

# expressions_type_Type class attributes and methods
expressions_type_Type_m_add: Method = Method(name="add", parameters={Parameter(name='rightArgument')}, type=StringType)
expressions_type_Type_m_getPrimitiveTypeIndex: Method = Method(name="getPrimitiveTypeIndex", parameters={}, type=IntegerType)
expressions_type_Type.methods={expressions_type_Type_m_getPrimitiveTypeIndex, expressions_type_Type_m_add}

# Relationships
expression2: BinaryAssociation = BinaryAssociation(
    name="expression2",
    ends={
        Property(name="Expression3", type=expressions_ast_LogicalRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_ast_LogicalRoot", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression4: BinaryAssociation = BinaryAssociation(
    name="expression4",
    ends={
        Property(name="Expression5", type=expressions_ast_ResourceRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_ast_ResourceRoot", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referencedVariables0: BinaryAssociation = BinaryAssociation(
    name="referencedVariables0",
    ends={
        Property(name="VariableReference", type=expressions_ast_AbstractRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_ast_AbstractRoot", type=VariableReference, multiplicity=Multiplicity(0, 9999))
    }
)
expressions1: BinaryAssociation = BinaryAssociation(
    name="expressions1",
    ends={
        Property(name="Expression", type=expressions_ast_ActionRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_ast_ActionRoot", type=Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
param114: BinaryAssociation = BinaryAssociation(
    name="param114",
    ends={
        Property(name="Expression15", type=expressions_ast_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_ast_BinaryExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
param216: BinaryAssociation = BinaryAssociation(
    name="param216",
    ends={
        Property(name="Expression18", type=expressions_ast_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_ast_BinaryExpression17", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
param119: BinaryAssociation = BinaryAssociation(
    name="param119",
    ends={
        Property(name="Expression20", type=expressions_ast_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_ast_UnaryExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
param16: BinaryAssociation = BinaryAssociation(
    name="param16",
    ends={
        Property(name="Expression7", type=expressions_ast_TernaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_ast_TernaryExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
param28: BinaryAssociation = BinaryAssociation(
    name="param28",
    ends={
        Property(name="Expression10", type=expressions_ast_TernaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_ast_TernaryExpression9", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
param311: BinaryAssociation = BinaryAssociation(
    name="param311",
    ends={
        Property(name="Expression13", type=expressions_ast_TernaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_ast_TernaryExpression12", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
resolved23: BinaryAssociation = BinaryAssociation(
    name="resolved23",
    ends={
        Property(name="ast_expressions_EObject", type=expressions_ast_VariableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_ast_VariableReference24", type=ast_expressions_EObject, multiplicity=Multiplicity(1, 1))
    }
)
arrayIndex21: BinaryAssociation = BinaryAssociation(
    name="arrayIndex21",
    ends={
        Property(name="Expression22", type=expressions_ast_VariableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_ast_VariableReference", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_expressions_ast_LogicalRoot_AbstractRoot = Generalization(general=AbstractRoot, specific=expressions_ast_LogicalRoot)
gen_expressions_ast_ResourceRoot_AbstractRoot = Generalization(general=AbstractRoot, specific=expressions_ast_ResourceRoot)
gen_expressions_ast_TernaryExpression_Expression = Generalization(general=Expression, specific=expressions_ast_TernaryExpression)
gen_expressions_ast_ActionRoot_AbstractRoot = Generalization(general=AbstractRoot, specific=expressions_ast_ActionRoot)
gen_expressions_ast_UnaryExpression_Expression = Generalization(general=Expression, specific=expressions_ast_UnaryExpression)
gen_expressions_ast_BinaryExpression_Expression = Generalization(general=Expression, specific=expressions_ast_BinaryExpression)
gen_expressions_ast_Constant_Expression = Generalization(general=Expression, specific=expressions_ast_Constant)
gen_expressions_ast_Literal_Expression = Generalization(general=Expression, specific=expressions_ast_Literal)
gen_expressions_ast_VariableReference_Expression = Generalization(general=Expression, specific=expressions_ast_VariableReference)
gen_expressions_type_BaseType_Type = Generalization(general=Type, specific=expressions_type_BaseType)
gen_expressions_type_IntegerType_BaseType = Generalization(general=BaseType, specific=expressions_type_IntegerType)
gen_expressions_type_BooleanType_BaseType = Generalization(general=BaseType, specific=expressions_type_BooleanType)
gen_expressions_type_NaturalType_BaseType = Generalization(general=BaseType, specific=expressions_type_NaturalType)
gen_expressions_type_ClockType_BaseType = Generalization(general=BaseType, specific=expressions_type_ClockType)
gen_expressions_type_FloatType_BaseType = Generalization(general=BaseType, specific=expressions_type_FloatType)
gen_expressions_type_ResourceType_BaseType = Generalization(general=BaseType, specific=expressions_type_ResourceType)
gen_expressions_type_AnyType_BaseType = Generalization(general=BaseType, specific=expressions_type_AnyType)

# Domain Model
domain_model = DomainModel(
    name="expressions",
    types={expressions_ast_AbstractRoot, expressions_ast_LogicalRoot, expressions_ast_ResourceRoot, expressions_ast_Expression, expressions_ast_TernaryExpression, VariableReference, expressions_ast_ActionRoot, AbstractRoot, Expression, expressions_ast_UnaryExpression, expressions_ast_BinaryExpression, ast_expressions_EObject, expressions_ast_Constant, expressions_ast_Literal, expressions_ast_VariableReference, expressions_ast_AstVisitor, expressions_type_BaseType, Type, expressions_type_IntegerType, BaseType, expressions_type_BooleanType, expressions_type_NaturalType, expressions_type_ClockType, expressions_type_FloatType, expressions_type_ResourceType, expressions_type_AnyType, expressions_type_Type, TernaryOperation, UnaryOperation, ResolvedType, BinaryOperation},
    associations={expression2, expression4, referencedVariables0, expressions1, param114, param216, param119, param16, param28, param311, resolved23, arrayIndex21},
    generalizations={gen_expressions_ast_LogicalRoot_AbstractRoot, gen_expressions_ast_ResourceRoot_AbstractRoot, gen_expressions_ast_TernaryExpression_Expression, gen_expressions_ast_ActionRoot_AbstractRoot, gen_expressions_ast_UnaryExpression_Expression, gen_expressions_ast_BinaryExpression_Expression, gen_expressions_ast_Constant_Expression, gen_expressions_ast_Literal_Expression, gen_expressions_ast_VariableReference_Expression, gen_expressions_type_BaseType_Type, gen_expressions_type_IntegerType_BaseType, gen_expressions_type_BooleanType_BaseType, gen_expressions_type_NaturalType_BaseType, gen_expressions_type_ClockType_BaseType, gen_expressions_type_FloatType_BaseType, gen_expressions_type_ResourceType_BaseType, gen_expressions_type_AnyType_BaseType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)