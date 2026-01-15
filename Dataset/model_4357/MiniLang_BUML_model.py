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
mini_lang_MiniLang = Class(name="mini::lang::MiniLang")
mini_lang_Block = Class(name="mini::lang::Block")
mini_lang_Statement = Class(name="mini::lang::Statement", is_abstract=True)
mini_lang_IfStatement = Class(name="mini::lang::IfStatement")
Statement = Class(name="Statement")
mini_lang_ComparisonExpression = Class(name="mini::lang::ComparisonExpression", is_abstract=True)
Expression = Class(name="Expression")
mini_lang_NotEqualsExpression = Class(name="mini::lang::NotEqualsExpression")
ComparisonExpression = Class(name="ComparisonExpression")
mini_lang_EqualsExpression = Class(name="mini::lang::EqualsExpression")
mini_lang_FOLCallExpression = Class(name="mini::lang::FOLCallExpression")
mini_lang_Expression = Class(name="mini::lang::Expression", is_abstract=True)
mini_lang_AssignmentStatement = Class(name="mini::lang::AssignmentStatement")
mini_lang_ExpressionStatement = Class(name="mini::lang::ExpressionStatement")
mini_lang_ReturnStatement = Class(name="mini::lang::ReturnStatement")
mini_lang_NameExpression = Class(name="mini::lang::NameExpression")

# mini_lang_MiniLang class attributes and methods

# mini_lang_Block class attributes and methods

# mini_lang_Statement class attributes and methods

# mini_lang_IfStatement class attributes and methods

# Statement class attributes and methods

# mini_lang_ComparisonExpression class attributes and methods

# Expression class attributes and methods

# mini_lang_NotEqualsExpression class attributes and methods

# ComparisonExpression class attributes and methods

# mini_lang_EqualsExpression class attributes and methods

# mini_lang_FOLCallExpression class attributes and methods
mini_lang_FOLCallExpression_iterator: Property = Property(name="iterator", type=StringType)
mini_lang_FOLCallExpression_method: Property = Property(name="method", type=StringType)
mini_lang_FOLCallExpression.attributes={mini_lang_FOLCallExpression_iterator, mini_lang_FOLCallExpression_method}

# mini_lang_Expression class attributes and methods

# mini_lang_AssignmentStatement class attributes and methods

# mini_lang_ExpressionStatement class attributes and methods

# mini_lang_ReturnStatement class attributes and methods

# mini_lang_NameExpression class attributes and methods
mini_lang_NameExpression_name: Property = Property(name="name", type=StringType)
mini_lang_NameExpression.attributes={mini_lang_NameExpression_name}

# Relationships
block0: BinaryAssociation = BinaryAssociation(
    name="block0",
    ends={
        Property(name="mini_lang_Block", type=mini_lang_MiniLang, multiplicity=Multiplicity(1, 1)),
        Property(name="mini_lang_MiniLang", type=mini_lang_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements1: BinaryAssociation = BinaryAssociation(
    name="statements1",
    ends={
        Property(name="mini_lang_Statement", type=mini_lang_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="mini_lang_Block2", type=mini_lang_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr14: BinaryAssociation = BinaryAssociation(
    name="expr14",
    ends={
        Property(name="mini_lang_Expression15", type=mini_lang_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mini_lang_ReturnStatement", type=mini_lang_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs16: BinaryAssociation = BinaryAssociation(
    name="lhs16",
    ends={
        Property(name="mini_lang_Expression17", type=mini_lang_ComparisonExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mini_lang_ComparisonExpression", type=mini_lang_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs18: BinaryAssociation = BinaryAssociation(
    name="rhs18",
    ends={
        Property(name="mini_lang_Expression20", type=mini_lang_ComparisonExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mini_lang_ComparisonExpression19", type=mini_lang_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition21: BinaryAssociation = BinaryAssociation(
    name="condition21",
    ends={
        Property(name="mini_lang_Expression22", type=mini_lang_FOLCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mini_lang_FOLCallExpression", type=mini_lang_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition3: BinaryAssociation = BinaryAssociation(
    name="condition3",
    ends={
        Property(name="mini_lang_Expression", type=mini_lang_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mini_lang_IfStatement", type=mini_lang_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ifBody4: BinaryAssociation = BinaryAssociation(
    name="ifBody4",
    ends={
        Property(name="mini_lang_Block6", type=mini_lang_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mini_lang_IfStatement5", type=mini_lang_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs7: BinaryAssociation = BinaryAssociation(
    name="lhs7",
    ends={
        Property(name="mini_lang_Expression8", type=mini_lang_AssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mini_lang_AssignmentStatement", type=mini_lang_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs9: BinaryAssociation = BinaryAssociation(
    name="rhs9",
    ends={
        Property(name="mini_lang_Expression11", type=mini_lang_AssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mini_lang_AssignmentStatement10", type=mini_lang_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr12: BinaryAssociation = BinaryAssociation(
    name="expr12",
    ends={
        Property(name="mini_lang_Expression13", type=mini_lang_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mini_lang_ExpressionStatement", type=mini_lang_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target23: BinaryAssociation = BinaryAssociation(
    name="target23",
    ends={
        Property(name="mini_lang_Expression25", type=mini_lang_FOLCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mini_lang_FOLCallExpression24", type=mini_lang_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_mini_lang_IfStatement_Statement = Generalization(general=Statement, specific=mini_lang_IfStatement)
gen_mini_lang_ComparisonExpression_Expression = Generalization(general=Expression, specific=mini_lang_ComparisonExpression)
gen_mini_lang_NotEqualsExpression_ComparisonExpression = Generalization(general=ComparisonExpression, specific=mini_lang_NotEqualsExpression)
gen_mini_lang_EqualsExpression_ComparisonExpression = Generalization(general=ComparisonExpression, specific=mini_lang_EqualsExpression)
gen_mini_lang_FOLCallExpression_Expression = Generalization(general=Expression, specific=mini_lang_FOLCallExpression)
gen_mini_lang_AssignmentStatement_Statement = Generalization(general=Statement, specific=mini_lang_AssignmentStatement)
gen_mini_lang_ExpressionStatement_Statement = Generalization(general=Statement, specific=mini_lang_ExpressionStatement)
gen_mini_lang_ReturnStatement_Statement = Generalization(general=Statement, specific=mini_lang_ReturnStatement)
gen_mini_lang_NameExpression_Expression = Generalization(general=Expression, specific=mini_lang_NameExpression)

# Domain Model
domain_model = DomainModel(
    name="mini_lang",
    types={mini_lang_MiniLang, mini_lang_Block, mini_lang_Statement, mini_lang_IfStatement, Statement, mini_lang_ComparisonExpression, Expression, mini_lang_NotEqualsExpression, ComparisonExpression, mini_lang_EqualsExpression, mini_lang_FOLCallExpression, mini_lang_Expression, mini_lang_AssignmentStatement, mini_lang_ExpressionStatement, mini_lang_ReturnStatement, mini_lang_NameExpression},
    associations={block0, statements1, expr14, lhs16, rhs18, condition21, condition3, ifBody4, lhs7, rhs9, expr12, target23},
    generalizations={gen_mini_lang_IfStatement_Statement, gen_mini_lang_ComparisonExpression_Expression, gen_mini_lang_NotEqualsExpression_ComparisonExpression, gen_mini_lang_EqualsExpression_ComparisonExpression, gen_mini_lang_FOLCallExpression_Expression, gen_mini_lang_AssignmentStatement_Statement, gen_mini_lang_ExpressionStatement_Statement, gen_mini_lang_ReturnStatement_Statement, gen_mini_lang_NameExpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)