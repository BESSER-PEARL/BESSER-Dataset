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
t2_Person = Class(name="t2_Person", is_abstract=True)
t2_Dad = Class(name="t2_Dad")
Person = Class(name="Person")
t2_Son = Class(name="t2_Son")

# t2_Person class attributes and methods
t2_Person_age: Property = Property(name="age", type=IntegerType)
t2_Person.attributes={t2_Person_age}

# t2_Dad class attributes and methods

# Person class attributes and methods

# t2_Son class attributes and methods

# Generalizations
gen_t2_Dad_Person = Generalization(general=Person, specific=t2_Dad)
gen_t2_Son_Person = Generalization(general=Person, specific=t2_Son)


# OCL Constraints
Unnamed: Constraint = Constraint(
    name="Unnamed",
    context=t2_Person,
    expression="context Person inv: self.age > 0 and self.age <=99",
    language="OCL"
)
Unnamed1: Constraint = Constraint(
    name="Unnamed1",
    context=t2_Dad,
    expression="context Dad inv: self.age > 30",
    language="OCL"
)
Unnamed2: Constraint = Constraint(
    name="Unnamed2",
    context=t2_Dad,
    expression="context Dad inv: Dad.allInstances()->forAll(d|Son.allInstances()->forAll(s|d.age > s.age))endpackage T2",
    language="OCL"
)

# Domain Model
domain_model = DomainModel(
    name="t2",
    types={t2_Person, t2_Dad, Person, t2_Son},
    associations={},
    constraints={Unnamed, Unnamed1, Unnamed2},
    generalizations={gen_t2_Dad_Person, gen_t2_Son_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)