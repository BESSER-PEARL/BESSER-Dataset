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
simple_lang_SimpleLang = Class(name="simple::lang::SimpleLang")
simple_lang_Statement = Class(name="simple::lang::Statement", is_abstract=True)
simple_lang_Expression = Class(name="simple::lang::Expression", is_abstract=True)
simple_lang_Type = Class(name="simple::lang::Type")
simple_lang_BinaryExpression = Class(name="simple::lang::BinaryExpression", is_abstract=True)
Expression = Class(name="Expression")
simple_lang_LogicalExpression = Class(name="simple::lang::LogicalExpression")
BinaryExpression = Class(name="BinaryExpression")
simple_lang_ArithmeticExpression = Class(name="simple::lang::ArithmeticExpression")
simple_lang_ComparisonExpression = Class(name="simple::lang::ComparisonExpression")
simple_lang_FeatureCallExpression = Class(name="simple::lang::FeatureCallExpression", is_abstract=True)
simple_lang_MethodCallExpression = Class(name="simple::lang::MethodCallExpression")
FeatureCallExpression = Class(name="FeatureCallExpression")
simple_lang_ExpressionStatement = Class(name="simple::lang::ExpressionStatement")
Statement = Class(name="Statement")
simple_lang_IfStatement = Class(name="simple::lang::IfStatement")
simple_lang_WhileStatement = Class(name="simple::lang::WhileStatement")
simple_lang_AssignmentStatement = Class(name="simple::lang::AssignmentStatement")
simple_lang_PropertyCallExpression = Class(name="simple::lang::PropertyCallExpression")

# simple_lang_SimpleLang class attributes and methods

# simple_lang_Statement class attributes and methods

# simple_lang_Expression class attributes and methods

# simple_lang_Type class attributes and methods

# simple_lang_BinaryExpression class attributes and methods
simple_lang_BinaryExpression_operator: Property = Property(name="operator", type=StringType)
simple_lang_BinaryExpression.attributes={simple_lang_BinaryExpression_operator}

# Expression class attributes and methods

# simple_lang_LogicalExpression class attributes and methods

# BinaryExpression class attributes and methods

# simple_lang_ArithmeticExpression class attributes and methods

# simple_lang_ComparisonExpression class attributes and methods

# simple_lang_FeatureCallExpression class attributes and methods
simple_lang_FeatureCallExpression_name: Property = Property(name="name", type=StringType)
simple_lang_FeatureCallExpression.attributes={simple_lang_FeatureCallExpression_name}

# simple_lang_MethodCallExpression class attributes and methods

# FeatureCallExpression class attributes and methods

# simple_lang_ExpressionStatement class attributes and methods

# Statement class attributes and methods

# simple_lang_IfStatement class attributes and methods

# simple_lang_WhileStatement class attributes and methods

# simple_lang_AssignmentStatement class attributes and methods

# simple_lang_PropertyCallExpression class attributes and methods

# Relationships
statements0: BinaryAssociation = BinaryAssociation(
    name="statements0",
    ends={
        Property(name="simple_lang_Statement", type=simple_lang_SimpleLang, multiplicity=Multiplicity(1, 1)),
        Property(name="simple_lang_SimpleLang", type=simple_lang_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type1: BinaryAssociation = BinaryAssociation(
    name="type1",
    ends={
        Property(name="simple_lang_Type", type=simple_lang_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="simple_lang_Expression", type=simple_lang_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs2: BinaryAssociation = BinaryAssociation(
    name="lhs2",
    ends={
        Property(name="simple_lang_Expression3", type=simple_lang_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simple_lang_BinaryExpression", type=simple_lang_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs4: BinaryAssociation = BinaryAssociation(
    name="rhs4",
    ends={
        Property(name="simple_lang_Expression6", type=simple_lang_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simple_lang_BinaryExpression5", type=simple_lang_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target7: BinaryAssociation = BinaryAssociation(
    name="target7",
    ends={
        Property(name="simple_lang_Expression8", type=simple_lang_FeatureCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simple_lang_FeatureCallExpression", type=simple_lang_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments9: BinaryAssociation = BinaryAssociation(
    name="arguments9",
    ends={
        Property(name="simple_lang_Expression10", type=simple_lang_MethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simple_lang_MethodCallExpression", type=simple_lang_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression11: BinaryAssociation = BinaryAssociation(
    name="expression11",
    ends={
        Property(name="simple_lang_Expression12", type=simple_lang_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="simple_lang_ExpressionStatement", type=simple_lang_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition13: BinaryAssociation = BinaryAssociation(
    name="condition13",
    ends={
        Property(name="simple_lang_Expression14", type=simple_lang_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="simple_lang_IfStatement", type=simple_lang_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ifBody15: BinaryAssociation = BinaryAssociation(
    name="ifBody15",
    ends={
        Property(name="simple_lang_Statement17", type=simple_lang_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="simple_lang_IfStatement16", type=simple_lang_Statement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elseBody18: BinaryAssociation = BinaryAssociation(
    name="elseBody18",
    ends={
        Property(name="simple_lang_Statement20", type=simple_lang_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="simple_lang_IfStatement19", type=simple_lang_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition21: BinaryAssociation = BinaryAssociation(
    name="condition21",
    ends={
        Property(name="simple_lang_Expression22", type=simple_lang_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="simple_lang_WhileStatement", type=simple_lang_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement23: BinaryAssociation = BinaryAssociation(
    name="statement23",
    ends={
        Property(name="simple_lang_Statement25", type=simple_lang_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="simple_lang_WhileStatement24", type=simple_lang_Statement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
lhs26: BinaryAssociation = BinaryAssociation(
    name="lhs26",
    ends={
        Property(name="simple_lang_Expression27", type=simple_lang_AssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="simple_lang_AssignmentStatement", type=simple_lang_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs28: BinaryAssociation = BinaryAssociation(
    name="rhs28",
    ends={
        Property(name="simple_lang_Expression30", type=simple_lang_AssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="simple_lang_AssignmentStatement29", type=simple_lang_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_simple_lang_BinaryExpression_Expression = Generalization(general=Expression, specific=simple_lang_BinaryExpression)
gen_simple_lang_LogicalExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=simple_lang_LogicalExpression)
gen_simple_lang_ArithmeticExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=simple_lang_ArithmeticExpression)
gen_simple_lang_ComparisonExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=simple_lang_ComparisonExpression)
gen_simple_lang_FeatureCallExpression_Expression = Generalization(general=Expression, specific=simple_lang_FeatureCallExpression)
gen_simple_lang_MethodCallExpression_FeatureCallExpression = Generalization(general=FeatureCallExpression, specific=simple_lang_MethodCallExpression)
gen_simple_lang_ExpressionStatement_Statement = Generalization(general=Statement, specific=simple_lang_ExpressionStatement)
gen_simple_lang_IfStatement_Statement = Generalization(general=Statement, specific=simple_lang_IfStatement)
gen_simple_lang_WhileStatement_Statement = Generalization(general=Statement, specific=simple_lang_WhileStatement)
gen_simple_lang_AssignmentStatement_Statement = Generalization(general=Statement, specific=simple_lang_AssignmentStatement)
gen_simple_lang_PropertyCallExpression_FeatureCallExpression = Generalization(general=FeatureCallExpression, specific=simple_lang_PropertyCallExpression)

# Domain Model
domain_model = DomainModel(
    name="simple_lang",
    types={simple_lang_SimpleLang, simple_lang_Statement, simple_lang_Expression, simple_lang_Type, simple_lang_BinaryExpression, Expression, simple_lang_LogicalExpression, BinaryExpression, simple_lang_ArithmeticExpression, simple_lang_ComparisonExpression, simple_lang_FeatureCallExpression, simple_lang_MethodCallExpression, FeatureCallExpression, simple_lang_ExpressionStatement, Statement, simple_lang_IfStatement, simple_lang_WhileStatement, simple_lang_AssignmentStatement, simple_lang_PropertyCallExpression},
    associations={statements0, type1, lhs2, rhs4, target7, arguments9, expression11, condition13, ifBody15, elseBody18, condition21, statement23, lhs26, rhs28},
    generalizations={gen_simple_lang_BinaryExpression_Expression, gen_simple_lang_LogicalExpression_BinaryExpression, gen_simple_lang_ArithmeticExpression_BinaryExpression, gen_simple_lang_ComparisonExpression_BinaryExpression, gen_simple_lang_FeatureCallExpression_Expression, gen_simple_lang_MethodCallExpression_FeatureCallExpression, gen_simple_lang_ExpressionStatement_Statement, gen_simple_lang_IfStatement_Statement, gen_simple_lang_WhileStatement_Statement, gen_simple_lang_AssignmentStatement_Statement, gen_simple_lang_PropertyCallExpression_FeatureCallExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)