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
properties_Person = Class(name="properties::Person")
properties_Address = Class(name="properties::Address")
properties_Employee = Class(name="properties::Employee")
Person = Class(name="Person")

# properties_Person class attributes and methods

# properties_Address class attributes and methods

# properties_Employee class attributes and methods
properties_Employee_hasSalary: Property = Property(name="hasSalary", type=IntegerType)
properties_Employee_hasAge: Property = Property(name="hasAge", type=IntegerType)
properties_Employee.attributes={properties_Employee_hasAge, properties_Employee_hasSalary}

# Person class attributes and methods

# Relationships
hasAddress0: BinaryAssociation = BinaryAssociation(
    name="hasAddress0",
    ends={
        Property(name="properties_Address", type=properties_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="properties_Person", type=properties_Address, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_properties_Employee_Person = Generalization(general=Person, specific=properties_Employee)

# Domain Model
domain_model = DomainModel(
    name="properties",
    types={properties_Person, properties_Address, properties_Employee, Person},
    associations={hasAddress0},
    generalizations={gen_properties_Employee_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)