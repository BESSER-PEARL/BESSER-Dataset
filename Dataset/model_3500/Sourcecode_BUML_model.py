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
sourcecode_Statement = Class(name="sourcecode::Statement", is_abstract=True)
sourcecode_While = Class(name="sourcecode::While")
sourcecode_Program = Class(name="sourcecode::Program")
sourcecode_Assignment = Class(name="sourcecode::Assignment")
Statement = Class(name="Statement")
sourcecode_Decision = Class(name="sourcecode::Decision")

# sourcecode_Statement class attributes and methods
sourcecode_Statement_id: Property = Property(name="id", type=StringType)
sourcecode_Statement.attributes={sourcecode_Statement_id}

# sourcecode_While class attributes and methods

# sourcecode_Program class attributes and methods

# sourcecode_Assignment class attributes and methods

# Statement class attributes and methods

# sourcecode_Decision class attributes and methods

# Relationships
next1: BinaryAssociation = BinaryAssociation(
    name="next1",
    ends={
        Property(name="sourcecode_Statement", type=sourcecode_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="sourcecode_Statement0", type=sourcecode_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
first7: BinaryAssociation = BinaryAssociation(
    name="first7",
    ends={
        Property(name="sourcecode_Statement8", type=sourcecode_While, multiplicity=Multiplicity(1, 1)),
        Property(name="sourcecode_While", type=sourcecode_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
last9: BinaryAssociation = BinaryAssociation(
    name="last9",
    ends={
        Property(name="sourcecode_Statement11", type=sourcecode_While, multiplicity=Multiplicity(1, 1)),
        Property(name="sourcecode_While10", type=sourcecode_Statement, multiplicity=Multiplicity(0, 1))
    }
)
first12: BinaryAssociation = BinaryAssociation(
    name="first12",
    ends={
        Property(name="sourcecode_Statement13", type=sourcecode_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="sourcecode_Program", type=sourcecode_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
positive2: BinaryAssociation = BinaryAssociation(
    name="positive2",
    ends={
        Property(name="sourcecode_Statement3", type=sourcecode_Decision, multiplicity=Multiplicity(1, 1)),
        Property(name="sourcecode_Decision", type=sourcecode_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
negative4: BinaryAssociation = BinaryAssociation(
    name="negative4",
    ends={
        Property(name="sourcecode_Statement6", type=sourcecode_Decision, multiplicity=Multiplicity(1, 1)),
        Property(name="sourcecode_Decision5", type=sourcecode_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_sourcecode_While_Statement = Generalization(general=Statement, specific=sourcecode_While)
gen_sourcecode_Assignment_Statement = Generalization(general=Statement, specific=sourcecode_Assignment)
gen_sourcecode_Decision_Statement = Generalization(general=Statement, specific=sourcecode_Decision)

# Domain Model
domain_model = DomainModel(
    name="sourcecode",
    types={sourcecode_Statement, sourcecode_While, sourcecode_Program, sourcecode_Assignment, Statement, sourcecode_Decision},
    associations={next1, first7, last9, first12, positive2, negative4},
    generalizations={gen_sourcecode_While_Statement, gen_sourcecode_Assignment_Statement, gen_sourcecode_Decision_Statement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)