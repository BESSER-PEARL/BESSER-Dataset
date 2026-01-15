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

LogicalOperator: Enumeration = Enumeration(
    name="LogicalOperator",
    literals={
            EnumerationLiteral(name="and"),
			EnumerationLiteral(name="or"),
			EnumerationLiteral(name="not")
    }
)

BitwiseOperator: Enumeration = Enumeration(
    name="BitwiseOperator",
    literals={
            EnumerationLiteral(name="xor"),
			EnumerationLiteral(name="and"),
			EnumerationLiteral(name="or")
    }
)

# Classes
expressions_Expression = Class(name="expressions::Expression", is_abstract=True)
expressions_BinaryExpression = Class(name="expressions::BinaryExpression", is_abstract=True)
Expression = Class(name="Expression")
expressions_UnaryExpression = Class(name="expressions::UnaryExpression", is_abstract=True)
expressions_ArgumentExpression = Class(name="expressions::ArgumentExpression", is_abstract=True)
expressions_IntLiteral = Class(name="expressions::IntLiteral")
expressions_DoubleLiteral = Class(name="expressions::DoubleLiteral")
expressions_FloatLiteral = Class(name="expressions::FloatLiteral")
expressions_HexLiteral = Class(name="expressions::HexLiteral")
expressions_StringLiteral = Class(name="expressions::StringLiteral")
expressions_NullLiteral = Class(name="expressions::NullLiteral")
expressions_Literal = Class(name="expressions::Literal", is_abstract=True)
expressions_BoolLiteral = Class(name="expressions::BoolLiteral")
Literal = Class(name="Literal")
expressions_AssignmentExpression = Class(name="expressions::AssignmentExpression")
expressions_ConditionalExpression = Class(name="expressions::ConditionalExpression")
expressions_LogicalOrExpression = Class(name="expressions::LogicalOrExpression")
BinaryExpression = Class(name="BinaryExpression")
expressions_LogicalAndExpression = Class(name="expressions::LogicalAndExpression")
expressions_LogicalNotExpression = Class(name="expressions::LogicalNotExpression")
UnaryExpression = Class(name="UnaryExpression")
expressions_BitwiseXorExpression = Class(name="expressions::BitwiseXorExpression")
expressions_BitwiseOrExpression = Class(name="expressions::BitwiseOrExpression")
expressions_BitwiseAndExpression = Class(name="expressions::BitwiseAndExpression")
expressions_LogicalRelationExpression = Class(name="expressions::LogicalRelationExpression")
expressions_ShiftExpression = Class(name="expressions::ShiftExpression")
expressions_NumericalAddSubtractExpression = Class(name="expressions::NumericalAddSubtractExpression")
expressions_NumericalMultiplyDivideExpression = Class(name="expressions::NumericalMultiplyDivideExpression")
expressions_NumericalUnaryExpression = Class(name="expressions::NumericalUnaryExpression")
expressions_PrimitiveValueExpression = Class(name="expressions::PrimitiveValueExpression")
expressions_FeatureCall = Class(name="expressions::FeatureCall")
ArgumentExpression = Class(name="ArgumentExpression")
expressions_EObject = Class(name="expressions::EObject")
expressions_ElementReferenceExpression = Class(name="expressions::ElementReferenceExpression")
expressions_ParenthesizedExpression = Class(name="expressions::ParenthesizedExpression")
expressions_TypeCastExpression = Class(name="expressions::TypeCastExpression")
expressions_Type = Class(name="expressions::Type")

# expressions_Expression class attributes and methods

# expressions_BinaryExpression class attributes and methods
expressions_BinaryExpression_m_getOperator: Method = Method(name="getOperator", parameters={}, type=StringType)
expressions_BinaryExpression.methods={expressions_BinaryExpression_m_getOperator}

# Expression class attributes and methods

# expressions_UnaryExpression class attributes and methods
expressions_UnaryExpression_m_getOperator: Method = Method(name="getOperator", parameters={}, type=StringType)
expressions_UnaryExpression.methods={expressions_UnaryExpression_m_getOperator}

# expressions_ArgumentExpression class attributes and methods

# expressions_IntLiteral class attributes and methods
expressions_IntLiteral_value: Property = Property(name="value", type=IntegerType)
expressions_IntLiteral.attributes={expressions_IntLiteral_value}

# expressions_DoubleLiteral class attributes and methods
expressions_DoubleLiteral_value: Property = Property(name="value", type=FloatType)
expressions_DoubleLiteral.attributes={expressions_DoubleLiteral_value}

# expressions_FloatLiteral class attributes and methods
expressions_FloatLiteral_value: Property = Property(name="value", type=FloatType)
expressions_FloatLiteral.attributes={expressions_FloatLiteral_value}

# expressions_HexLiteral class attributes and methods
expressions_HexLiteral_value: Property = Property(name="value", type=IntegerType)
expressions_HexLiteral.attributes={expressions_HexLiteral_value}

# expressions_StringLiteral class attributes and methods
expressions_StringLiteral_value: Property = Property(name="value", type=StringType)
expressions_StringLiteral.attributes={expressions_StringLiteral_value}

# expressions_NullLiteral class attributes and methods

# expressions_Literal class attributes and methods

# expressions_BoolLiteral class attributes and methods
expressions_BoolLiteral_value: Property = Property(name="value", type=BooleanType)
expressions_BoolLiteral.attributes={expressions_BoolLiteral_value}

# Literal class attributes and methods

# expressions_AssignmentExpression class attributes and methods
expressions_AssignmentExpression_operator: Property = Property(name="operator", type=StringType)
expressions_AssignmentExpression.attributes={expressions_AssignmentExpression_operator}

# expressions_ConditionalExpression class attributes and methods

# expressions_LogicalOrExpression class attributes and methods

# BinaryExpression class attributes and methods

# expressions_LogicalAndExpression class attributes and methods

# expressions_LogicalNotExpression class attributes and methods

# UnaryExpression class attributes and methods

# expressions_BitwiseXorExpression class attributes and methods

# expressions_BitwiseOrExpression class attributes and methods

# expressions_BitwiseAndExpression class attributes and methods

# expressions_LogicalRelationExpression class attributes and methods
expressions_LogicalRelationExpression_operator: Property = Property(name="operator", type=StringType)
expressions_LogicalRelationExpression.attributes={expressions_LogicalRelationExpression_operator}

# expressions_ShiftExpression class attributes and methods
expressions_ShiftExpression_operator: Property = Property(name="operator", type=StringType)
expressions_ShiftExpression.attributes={expressions_ShiftExpression_operator}

# expressions_NumericalAddSubtractExpression class attributes and methods
expressions_NumericalAddSubtractExpression_operator: Property = Property(name="operator", type=StringType)
expressions_NumericalAddSubtractExpression.attributes={expressions_NumericalAddSubtractExpression_operator}

# expressions_NumericalMultiplyDivideExpression class attributes and methods
expressions_NumericalMultiplyDivideExpression_operator: Property = Property(name="operator", type=StringType)
expressions_NumericalMultiplyDivideExpression.attributes={expressions_NumericalMultiplyDivideExpression_operator}

# expressions_NumericalUnaryExpression class attributes and methods
expressions_NumericalUnaryExpression_operator: Property = Property(name="operator", type=StringType)
expressions_NumericalUnaryExpression.attributes={expressions_NumericalUnaryExpression_operator}

# expressions_PrimitiveValueExpression class attributes and methods

# expressions_FeatureCall class attributes and methods
expressions_FeatureCall_operationCall: Property = Property(name="operationCall", type=BooleanType)
expressions_FeatureCall_arrayAccess: Property = Property(name="arrayAccess", type=BooleanType)
expressions_FeatureCall.attributes={expressions_FeatureCall_operationCall, expressions_FeatureCall_arrayAccess}

# ArgumentExpression class attributes and methods

# expressions_EObject class attributes and methods

# expressions_ElementReferenceExpression class attributes and methods
expressions_ElementReferenceExpression_operationCall: Property = Property(name="operationCall", type=BooleanType)
expressions_ElementReferenceExpression_arrayAccess: Property = Property(name="arrayAccess", type=BooleanType)
expressions_ElementReferenceExpression.attributes={expressions_ElementReferenceExpression_operationCall, expressions_ElementReferenceExpression_arrayAccess}

# expressions_ParenthesizedExpression class attributes and methods

# expressions_TypeCastExpression class attributes and methods

# expressions_Type class attributes and methods

# Relationships
leftOperand0: BinaryAssociation = BinaryAssociation(
    name="leftOperand0",
    ends={
        Property(name="expressions_Expression", type=expressions_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_BinaryExpression", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand1: BinaryAssociation = BinaryAssociation(
    name="rightOperand1",
    ends={
        Property(name="expressions_Expression3", type=expressions_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_BinaryExpression2", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand4: BinaryAssociation = BinaryAssociation(
    name="operand4",
    ends={
        Property(name="expressions_Expression5", type=expressions_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_UnaryExpression", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args6: BinaryAssociation = BinaryAssociation(
    name="args6",
    ends={
        Property(name="expressions_Expression7", type=expressions_ArgumentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_ArgumentExpression", type=expressions_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
varRef8: BinaryAssociation = BinaryAssociation(
    name="varRef8",
    ends={
        Property(name="expressions_Expression9", type=expressions_AssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_AssignmentExpression", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression10: BinaryAssociation = BinaryAssociation(
    name="expression10",
    ends={
        Property(name="expressions_Expression12", type=expressions_AssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_AssignmentExpression11", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition13: BinaryAssociation = BinaryAssociation(
    name="condition13",
    ends={
        Property(name="expressions_Expression14", type=expressions_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_ConditionalExpression", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trueCase15: BinaryAssociation = BinaryAssociation(
    name="trueCase15",
    ends={
        Property(name="expressions_Expression17", type=expressions_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_ConditionalExpression16", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
falseCase18: BinaryAssociation = BinaryAssociation(
    name="falseCase18",
    ends={
        Property(name="expressions_Expression20", type=expressions_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_ConditionalExpression19", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value21: BinaryAssociation = BinaryAssociation(
    name="value21",
    ends={
        Property(name="expressions_Literal", type=expressions_PrimitiveValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_PrimitiveValueExpression", type=expressions_Literal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owner22: BinaryAssociation = BinaryAssociation(
    name="owner22",
    ends={
        Property(name="expressions_Expression23", type=expressions_FeatureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_FeatureCall", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
feature24: BinaryAssociation = BinaryAssociation(
    name="feature24",
    ends={
        Property(name="expressions_EObject", type=expressions_FeatureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_FeatureCall25", type=expressions_EObject, multiplicity=Multiplicity(0, 1))
    }
)
arraySelector26: BinaryAssociation = BinaryAssociation(
    name="arraySelector26",
    ends={
        Property(name="expressions_Expression28", type=expressions_FeatureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_FeatureCall27", type=expressions_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reference29: BinaryAssociation = BinaryAssociation(
    name="reference29",
    ends={
        Property(name="expressions_EObject30", type=expressions_ElementReferenceExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_ElementReferenceExpression", type=expressions_EObject, multiplicity=Multiplicity(0, 1))
    }
)
arraySelector31: BinaryAssociation = BinaryAssociation(
    name="arraySelector31",
    ends={
        Property(name="expressions_Expression33", type=expressions_ElementReferenceExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_ElementReferenceExpression32", type=expressions_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression34: BinaryAssociation = BinaryAssociation(
    name="expression34",
    ends={
        Property(name="expressions_Expression35", type=expressions_ParenthesizedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_ParenthesizedExpression", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand36: BinaryAssociation = BinaryAssociation(
    name="operand36",
    ends={
        Property(name="expressions_Expression37", type=expressions_TypeCastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_TypeCastExpression", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type38: BinaryAssociation = BinaryAssociation(
    name="type38",
    ends={
        Property(name="expressions_TypeCastExpression39", type=expressions_Type, multiplicity=Multiplicity(0, 1)),
        Property(name="expressions_Type", type=expressions_TypeCastExpression, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_expressions_BinaryExpression_Expression = Generalization(general=Expression, specific=expressions_BinaryExpression)
gen_expressions_UnaryExpression_Expression = Generalization(general=Expression, specific=expressions_UnaryExpression)
gen_expressions_ArgumentExpression_Expression = Generalization(general=Expression, specific=expressions_ArgumentExpression)
gen_expressions_IntLiteral_Literal = Generalization(general=Literal, specific=expressions_IntLiteral)
gen_expressions_DoubleLiteral_Literal = Generalization(general=Literal, specific=expressions_DoubleLiteral)
gen_expressions_FloatLiteral_Literal = Generalization(general=Literal, specific=expressions_FloatLiteral)
gen_expressions_HexLiteral_Literal = Generalization(general=Literal, specific=expressions_HexLiteral)
gen_expressions_StringLiteral_Literal = Generalization(general=Literal, specific=expressions_StringLiteral)
gen_expressions_NullLiteral_Literal = Generalization(general=Literal, specific=expressions_NullLiteral)
gen_expressions_BoolLiteral_Literal = Generalization(general=Literal, specific=expressions_BoolLiteral)
gen_expressions_AssignmentExpression_Expression = Generalization(general=Expression, specific=expressions_AssignmentExpression)
gen_expressions_ConditionalExpression_Expression = Generalization(general=Expression, specific=expressions_ConditionalExpression)
gen_expressions_LogicalOrExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=expressions_LogicalOrExpression)
gen_expressions_LogicalAndExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=expressions_LogicalAndExpression)
gen_expressions_LogicalNotExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=expressions_LogicalNotExpression)
gen_expressions_BitwiseXorExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=expressions_BitwiseXorExpression)
gen_expressions_BitwiseOrExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=expressions_BitwiseOrExpression)
gen_expressions_BitwiseAndExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=expressions_BitwiseAndExpression)
gen_expressions_LogicalRelationExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=expressions_LogicalRelationExpression)
gen_expressions_ShiftExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=expressions_ShiftExpression)
gen_expressions_NumericalAddSubtractExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=expressions_NumericalAddSubtractExpression)
gen_expressions_NumericalMultiplyDivideExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=expressions_NumericalMultiplyDivideExpression)
gen_expressions_NumericalUnaryExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=expressions_NumericalUnaryExpression)
gen_expressions_PrimitiveValueExpression_Expression = Generalization(general=Expression, specific=expressions_PrimitiveValueExpression)
gen_expressions_FeatureCall_ArgumentExpression = Generalization(general=ArgumentExpression, specific=expressions_FeatureCall)
gen_expressions_ElementReferenceExpression_ArgumentExpression = Generalization(general=ArgumentExpression, specific=expressions_ElementReferenceExpression)
gen_expressions_ParenthesizedExpression_Expression = Generalization(general=Expression, specific=expressions_ParenthesizedExpression)
gen_expressions_TypeCastExpression_Expression = Generalization(general=Expression, specific=expressions_TypeCastExpression)

# Domain Model
domain_model = DomainModel(
    name="expressions",
    types={expressions_Expression, expressions_BinaryExpression, Expression, expressions_UnaryExpression, expressions_ArgumentExpression, expressions_IntLiteral, expressions_DoubleLiteral, expressions_FloatLiteral, expressions_HexLiteral, expressions_StringLiteral, expressions_NullLiteral, expressions_Literal, expressions_BoolLiteral, Literal, expressions_AssignmentExpression, expressions_ConditionalExpression, expressions_LogicalOrExpression, BinaryExpression, expressions_LogicalAndExpression, expressions_LogicalNotExpression, UnaryExpression, expressions_BitwiseXorExpression, expressions_BitwiseOrExpression, expressions_BitwiseAndExpression, expressions_LogicalRelationExpression, expressions_ShiftExpression, expressions_NumericalAddSubtractExpression, expressions_NumericalMultiplyDivideExpression, expressions_NumericalUnaryExpression, expressions_PrimitiveValueExpression, expressions_FeatureCall, ArgumentExpression, expressions_EObject, expressions_ElementReferenceExpression, expressions_ParenthesizedExpression, expressions_TypeCastExpression, expressions_Type, AssignmentOperator, ShiftOperator, AdditiveOperator, MultiplicativeOperator, UnaryOperator, RelationalOperator, LogicalOperator, BitwiseOperator},
    associations={leftOperand0, rightOperand1, operand4, args6, varRef8, expression10, condition13, trueCase15, falseCase18, value21, owner22, feature24, arraySelector26, reference29, arraySelector31, expression34, operand36, type38},
    generalizations={gen_expressions_BinaryExpression_Expression, gen_expressions_UnaryExpression_Expression, gen_expressions_ArgumentExpression_Expression, gen_expressions_IntLiteral_Literal, gen_expressions_DoubleLiteral_Literal, gen_expressions_FloatLiteral_Literal, gen_expressions_HexLiteral_Literal, gen_expressions_StringLiteral_Literal, gen_expressions_NullLiteral_Literal, gen_expressions_BoolLiteral_Literal, gen_expressions_AssignmentExpression_Expression, gen_expressions_ConditionalExpression_Expression, gen_expressions_LogicalOrExpression_BinaryExpression, gen_expressions_LogicalAndExpression_BinaryExpression, gen_expressions_LogicalNotExpression_UnaryExpression, gen_expressions_BitwiseXorExpression_BinaryExpression, gen_expressions_BitwiseOrExpression_BinaryExpression, gen_expressions_BitwiseAndExpression_BinaryExpression, gen_expressions_LogicalRelationExpression_BinaryExpression, gen_expressions_ShiftExpression_BinaryExpression, gen_expressions_NumericalAddSubtractExpression_BinaryExpression, gen_expressions_NumericalMultiplyDivideExpression_BinaryExpression, gen_expressions_NumericalUnaryExpression_UnaryExpression, gen_expressions_PrimitiveValueExpression_Expression, gen_expressions_FeatureCall_ArgumentExpression, gen_expressions_ElementReferenceExpression_ArgumentExpression, gen_expressions_ParenthesizedExpression_Expression, gen_expressions_TypeCastExpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)