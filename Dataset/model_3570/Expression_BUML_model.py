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
expression_Expression = Class(name="expression::Expression")
SyntaxElement = Class(name="SyntaxElement")
expression_SyntaxElement = Class(name="expression::SyntaxElement")
expression_IfExpression = Class(name="expression::IfExpression")
expression_SwitchExpression = Class(name="expression::SwitchExpression")
expression_LetExpression = Class(name="expression::LetExpression")
Expression = Class(name="Expression")
expression_CastedExpression = Class(name="expression::CastedExpression")
expression_Identifier = Class(name="expression::Identifier")
expression_OperationCall = Class(name="expression::OperationCall")
FeatureCall = Class(name="FeatureCall")
expression_Literal = Class(name="expression::Literal")
expression_BooleanLiteral = Class(name="expression::BooleanLiteral")
Literal = Class(name="Literal")
expression_Case = Class(name="expression::Case")
expression_FeatureCall = Class(name="expression::FeatureCall")
expression_ListLiteral = Class(name="expression::ListLiteral")
expression_IntegerLiteral = Class(name="expression::IntegerLiteral")
expression_NullLiteral = Class(name="expression::NullLiteral")
expression_RealLiteral = Class(name="expression::RealLiteral")
expression_StringLiteral = Class(name="expression::StringLiteral")
expression_GlobalVarExpression = Class(name="expression::GlobalVarExpression")
expression_ChainExpression = Class(name="expression::ChainExpression")
expression_BooleanOperation = Class(name="expression::BooleanOperation")
expression_ConstructorCallExpression = Class(name="expression::ConstructorCallExpression")
expression_TypeSelectExpression = Class(name="expression::TypeSelectExpression")
expression_CollectionExpression = Class(name="expression::CollectionExpression")

# expression_Expression class attributes and methods

# SyntaxElement class attributes and methods

# expression_SyntaxElement class attributes and methods

# expression_IfExpression class attributes and methods

# expression_SwitchExpression class attributes and methods

# expression_LetExpression class attributes and methods
expression_LetExpression_identifier: Property = Property(name="identifier", type=StringType)
expression_LetExpression.attributes={expression_LetExpression_identifier}

# Expression class attributes and methods

# expression_CastedExpression class attributes and methods

# expression_Identifier class attributes and methods
expression_Identifier_cl: Property = Property(name="cl", type=StringType)
expression_Identifier_id: Property = Property(name="id", type=StringType)
expression_Identifier.attributes={expression_Identifier_id, expression_Identifier_cl}

# expression_OperationCall class attributes and methods

# FeatureCall class attributes and methods

# expression_Literal class attributes and methods

# expression_BooleanLiteral class attributes and methods
expression_BooleanLiteral_val: Property = Property(name="val", type=StringType)
expression_BooleanLiteral.attributes={expression_BooleanLiteral_val}

# Literal class attributes and methods

# expression_Case class attributes and methods

# expression_FeatureCall class attributes and methods
expression_FeatureCall_name: Property = Property(name="name", type=StringType)
expression_FeatureCall.attributes={expression_FeatureCall_name}

# expression_ListLiteral class attributes and methods

# expression_IntegerLiteral class attributes and methods
expression_IntegerLiteral_val: Property = Property(name="val", type=IntegerType)
expression_IntegerLiteral.attributes={expression_IntegerLiteral_val}

# expression_NullLiteral class attributes and methods
expression_NullLiteral_val: Property = Property(name="val", type=StringType)
expression_NullLiteral.attributes={expression_NullLiteral_val}

# expression_RealLiteral class attributes and methods
expression_RealLiteral_val: Property = Property(name="val", type=StringType)
expression_RealLiteral.attributes={expression_RealLiteral_val}

# expression_StringLiteral class attributes and methods
expression_StringLiteral_val: Property = Property(name="val", type=StringType)
expression_StringLiteral.attributes={expression_StringLiteral_val}

# expression_GlobalVarExpression class attributes and methods
expression_GlobalVarExpression_name: Property = Property(name="name", type=StringType)
expression_GlobalVarExpression.attributes={expression_GlobalVarExpression_name}

# expression_ChainExpression class attributes and methods

# expression_BooleanOperation class attributes and methods
expression_BooleanOperation_operator: Property = Property(name="operator", type=StringType)
expression_BooleanOperation.attributes={expression_BooleanOperation_operator}

# expression_ConstructorCallExpression class attributes and methods

# expression_TypeSelectExpression class attributes and methods

# expression_CollectionExpression class attributes and methods
expression_CollectionExpression_var: Property = Property(name="var", type=StringType)
expression_CollectionExpression.attributes={expression_CollectionExpression_var}

# Relationships
target5: BinaryAssociation = BinaryAssociation(
    name="target5",
    ends={
        Property(name="expression_Expression7", type=expression_CastedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_CastedExpression6", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition8: BinaryAssociation = BinaryAssociation(
    name="condition8",
    ends={
        Property(name="expression_Expression9", type=expression_IfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_IfExpression", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenPart10: BinaryAssociation = BinaryAssociation(
    name="thenPart10",
    ends={
        Property(name="expression_Expression12", type=expression_IfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_IfExpression11", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elsePart13: BinaryAssociation = BinaryAssociation(
    name="elsePart13",
    ends={
        Property(name="expression_Expression15", type=expression_IfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_IfExpression14", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
varExpr0: BinaryAssociation = BinaryAssociation(
    name="varExpr0",
    ends={
        Property(name="expression_Expression", type=expression_LetExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_LetExpression", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target1: BinaryAssociation = BinaryAssociation(
    name="target1",
    ends={
        Property(name="expression_Expression3", type=expression_LetExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_LetExpression2", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type4: BinaryAssociation = BinaryAssociation(
    name="type4",
    ends={
        Property(name="expression_Identifier", type=expression_CastedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_CastedExpression", type=expression_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenPar26: BinaryAssociation = BinaryAssociation(
    name="thenPar26",
    ends={
        Property(name="expression_Expression28", type=expression_Case, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_Case27", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
params29: BinaryAssociation = BinaryAssociation(
    name="params29",
    ends={
        Property(name="expression_Expression30", type=expression_OperationCall, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_OperationCall", type=expression_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
switchExpr16: BinaryAssociation = BinaryAssociation(
    name="switchExpr16",
    ends={
        Property(name="expression_Expression17", type=expression_SwitchExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_SwitchExpression", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
case18: BinaryAssociation = BinaryAssociation(
    name="case18",
    ends={
        Property(name="expression_Case", type=expression_SwitchExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_SwitchExpression19", type=expression_Case, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultExpr20: BinaryAssociation = BinaryAssociation(
    name="defaultExpr20",
    ends={
        Property(name="expression_Expression22", type=expression_SwitchExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_SwitchExpression21", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition23: BinaryAssociation = BinaryAssociation(
    name="condition23",
    ends={
        Property(name="expression_Expression25", type=expression_Case, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_Case24", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target31: BinaryAssociation = BinaryAssociation(
    name="target31",
    ends={
        Property(name="expression_Expression32", type=expression_FeatureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_FeatureCall", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type33: BinaryAssociation = BinaryAssociation(
    name="type33",
    ends={
        Property(name="expression_Identifier35", type=expression_FeatureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_FeatureCall34", type=expression_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements36: BinaryAssociation = BinaryAssociation(
    name="elements36",
    ends={
        Property(name="expression_Expression37", type=expression_ListLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_ListLiteral", type=expression_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
id143: BinaryAssociation = BinaryAssociation(
    name="id143",
    ends={
        Property(name="expression_Identifier44", type=expression_Identifier, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_Identifier42", type=expression_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
first45: BinaryAssociation = BinaryAssociation(
    name="first45",
    ends={
        Property(name="expression_Expression46", type=expression_ChainExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_ChainExpression", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
next47: BinaryAssociation = BinaryAssociation(
    name="next47",
    ends={
        Property(name="expression_Expression49", type=expression_ChainExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_ChainExpression48", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type38: BinaryAssociation = BinaryAssociation(
    name="type38",
    ends={
        Property(name="expression_Identifier39", type=expression_ConstructorCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_ConstructorCallExpression", type=expression_Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp40: BinaryAssociation = BinaryAssociation(
    name="exp40",
    ends={
        Property(name="expression_Expression41", type=expression_CollectionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_CollectionExpression", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left50: BinaryAssociation = BinaryAssociation(
    name="left50",
    ends={
        Property(name="expression_Expression51", type=expression_BooleanOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_BooleanOperation", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right52: BinaryAssociation = BinaryAssociation(
    name="right52",
    ends={
        Property(name="expression_Expression54", type=expression_BooleanOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_BooleanOperation53", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_expression_Expression_SyntaxElement = Generalization(general=SyntaxElement, specific=expression_Expression)
gen_expression_IfExpression_Expression = Generalization(general=Expression, specific=expression_IfExpression)
gen_expression_SwitchExpression_Expression = Generalization(general=Expression, specific=expression_SwitchExpression)
gen_expression_LetExpression_Expression = Generalization(general=Expression, specific=expression_LetExpression)
gen_expression_CastedExpression_Expression = Generalization(general=Expression, specific=expression_CastedExpression)
gen_expression_OperationCall_Expression = Generalization(general=Expression, specific=expression_OperationCall)
gen_expression_OperationCall_FeatureCall = Generalization(general=FeatureCall, specific=expression_OperationCall)
gen_expression_Literal_Expression = Generalization(general=Expression, specific=expression_Literal)
gen_expression_BooleanLiteral_Literal = Generalization(general=Literal, specific=expression_BooleanLiteral)
gen_expression_Case_SyntaxElement = Generalization(general=SyntaxElement, specific=expression_Case)
gen_expression_FeatureCall_Expression = Generalization(general=Expression, specific=expression_FeatureCall)
gen_expression_ListLiteral_Expression = Generalization(general=Expression, specific=expression_ListLiteral)
gen_expression_IntegerLiteral_Literal = Generalization(general=Literal, specific=expression_IntegerLiteral)
gen_expression_NullLiteral_Literal = Generalization(general=Literal, specific=expression_NullLiteral)
gen_expression_RealLiteral_Literal = Generalization(general=Literal, specific=expression_RealLiteral)
gen_expression_StringLiteral_Literal = Generalization(general=Literal, specific=expression_StringLiteral)
gen_expression_GlobalVarExpression_Expression = Generalization(general=Expression, specific=expression_GlobalVarExpression)
gen_expression_ChainExpression_Expression = Generalization(general=Expression, specific=expression_ChainExpression)
gen_expression_ConstructorCallExpression_Expression = Generalization(general=Expression, specific=expression_ConstructorCallExpression)
gen_expression_TypeSelectExpression_Expression = Generalization(general=Expression, specific=expression_TypeSelectExpression)
gen_expression_TypeSelectExpression_FeatureCall = Generalization(general=FeatureCall, specific=expression_TypeSelectExpression)
gen_expression_CollectionExpression_Expression = Generalization(general=Expression, specific=expression_CollectionExpression)
gen_expression_CollectionExpression_FeatureCall = Generalization(general=FeatureCall, specific=expression_CollectionExpression)
gen_expression_Identifier_SyntaxElement = Generalization(general=SyntaxElement, specific=expression_Identifier)
gen_expression_BooleanOperation_Expression = Generalization(general=Expression, specific=expression_BooleanOperation)

# Domain Model
domain_model = DomainModel(
    name="expression",
    types={expression_Expression, SyntaxElement, expression_SyntaxElement, expression_IfExpression, expression_SwitchExpression, expression_LetExpression, Expression, expression_CastedExpression, expression_Identifier, expression_OperationCall, FeatureCall, expression_Literal, expression_BooleanLiteral, Literal, expression_Case, expression_FeatureCall, expression_ListLiteral, expression_IntegerLiteral, expression_NullLiteral, expression_RealLiteral, expression_StringLiteral, expression_GlobalVarExpression, expression_ChainExpression, expression_BooleanOperation, expression_ConstructorCallExpression, expression_TypeSelectExpression, expression_CollectionExpression},
    associations={target5, condition8, thenPart10, elsePart13, varExpr0, target1, type4, thenPar26, params29, switchExpr16, case18, defaultExpr20, condition23, target31, type33, elements36, id143, first45, next47, type38, exp40, left50, right52},
    generalizations={gen_expression_Expression_SyntaxElement, gen_expression_IfExpression_Expression, gen_expression_SwitchExpression_Expression, gen_expression_LetExpression_Expression, gen_expression_CastedExpression_Expression, gen_expression_OperationCall_Expression, gen_expression_OperationCall_FeatureCall, gen_expression_Literal_Expression, gen_expression_BooleanLiteral_Literal, gen_expression_Case_SyntaxElement, gen_expression_FeatureCall_Expression, gen_expression_ListLiteral_Expression, gen_expression_IntegerLiteral_Literal, gen_expression_NullLiteral_Literal, gen_expression_RealLiteral_Literal, gen_expression_StringLiteral_Literal, gen_expression_GlobalVarExpression_Expression, gen_expression_ChainExpression_Expression, gen_expression_ConstructorCallExpression_Expression, gen_expression_TypeSelectExpression_Expression, gen_expression_TypeSelectExpression_FeatureCall, gen_expression_CollectionExpression_Expression, gen_expression_CollectionExpression_FeatureCall, gen_expression_Identifier_SyntaxElement, gen_expression_BooleanOperation_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)