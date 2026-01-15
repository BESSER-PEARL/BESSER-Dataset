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
Expression_Expression = Class(name="Expression::Expression")
Expression_Operation = Class(name="Expression::Operation")
Expression = Class(name="Expression")

# Expression_Expression class attributes and methods
Expression_Expression_value: Property = Property(name="value", type=FloatType)
Expression_Expression.attributes={Expression_Expression_value}

# Expression_Operation class attributes and methods
Expression_Operation_op: Property = Property(name="op", type=StringType)
Expression_Operation.attributes={Expression_Operation_op}

# Expression class attributes and methods

# Relationships
operation0: BinaryAssociation = BinaryAssociation(
    name="operation0",
    ends={
        Property(name="Operation", type=Expression_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="left", type=Expression_Operation, multiplicity=Multiplicity(0, 1))
    }
)
left1: BinaryAssociation = BinaryAssociation(
    name="left1",
    ends={
        Property(name="Expression", type=Expression_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation", type=Expression_Expression, multiplicity=Multiplicity(1, 1))
    }
)
right2: BinaryAssociation = BinaryAssociation(
    name="right2",
    ends={
        Property(name="Expression_Expression", type=Expression_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="Expression_Operation", type=Expression_Expression, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_Expression_Operation_Expression = Generalization(general=Expression, specific=Expression_Operation)

# Domain Model
domain_model = DomainModel(
    name="Expression",
    types={Expression_Expression, Expression_Operation, Expression},
    associations={operation0, left1, right2},
    generalizations={gen_Expression_Operation_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)