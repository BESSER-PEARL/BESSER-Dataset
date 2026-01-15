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
demo1_Model = Class(name="demo1::Model")
demo1_Category = Class(name="demo1::Category")
demo1_Rule = Class(name="demo1::Rule")
demo1_RuleExpression = Class(name="demo1::RuleExpression")
demo1_EObject = Class(name="demo1::EObject")
demo1_TestExpression = Class(name="demo1::TestExpression")
demo1_RatioExpression = Class(name="demo1::RatioExpression")

# demo1_Model class attributes and methods

# demo1_Category class attributes and methods
demo1_Category_name: Property = Property(name="name", type=StringType)
demo1_Category.attributes={demo1_Category_name}

# demo1_Rule class attributes and methods

# demo1_RuleExpression class attributes and methods

# demo1_EObject class attributes and methods

# demo1_TestExpression class attributes and methods

# demo1_RatioExpression class attributes and methods
demo1_RatioExpression_ratio: Property = Property(name="ratio", type=IntegerType)
demo1_RatioExpression.attributes={demo1_RatioExpression_ratio}

# Relationships
categories0: BinaryAssociation = BinaryAssociation(
    name="categories0",
    ends={
        Property(name="demo1_Category", type=demo1_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="demo1_Model", type=demo1_Category, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rule1: BinaryAssociation = BinaryAssociation(
    name="rule1",
    ends={
        Property(name="demo1_Rule", type=demo1_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="demo1_Model2", type=demo1_Rule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
first3: BinaryAssociation = BinaryAssociation(
    name="first3",
    ends={
        Property(name="demo1_RuleExpression", type=demo1_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="demo1_Rule4", type=demo1_RuleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
next5: BinaryAssociation = BinaryAssociation(
    name="next5",
    ends={
        Property(name="demo1_EObject", type=demo1_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="demo1_Rule6", type=demo1_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
test7: BinaryAssociation = BinaryAssociation(
    name="test7",
    ends={
        Property(name="demo1_TestExpression", type=demo1_RuleExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="demo1_RuleExpression8", type=demo1_TestExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ratio9: BinaryAssociation = BinaryAssociation(
    name="ratio9",
    ends={
        Property(name="demo1_RatioExpression", type=demo1_RuleExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="demo1_RuleExpression10", type=demo1_RatioExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
category11: BinaryAssociation = BinaryAssociation(
    name="category11",
    ends={
        Property(name="demo1_Category13", type=demo1_TestExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="demo1_TestExpression12", type=demo1_Category, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="demo1",
    types={demo1_Model, demo1_Category, demo1_Rule, demo1_RuleExpression, demo1_EObject, demo1_TestExpression, demo1_RatioExpression},
    associations={categories0, rule1, first3, next5, test7, ratio9, category11},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)