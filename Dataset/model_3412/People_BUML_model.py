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
Gender: Enumeration = Enumeration(
    name="Gender",
    literals={
            EnumerationLiteral(name="MALE"),
			EnumerationLiteral(name="FEMALE")
    }
)

# Classes
people_Person = Class(name="people::Person")
people_Universe = Class(name="people::Universe")

# people_Person class attributes and methods
people_Person_gender: Property = Property(name="gender", type=StringType)
people_Person_name: Property = Property(name="name", type=StringType)
people_Person_m_child: Method = Method(name="child", parameters={Parameter(name='childName')}, type=StringType)
people_Person.attributes={people_Person_gender, people_Person_name}
people_Person.methods={people_Person_m_child}

# people_Universe class attributes and methods

# Relationships
children1: BinaryAssociation = BinaryAssociation(
    name="children1",
    ends={
        Property(name="people_Person", type=people_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="people_Person0", type=people_Person, multiplicity=Multiplicity(0, 9999))
    }
)
parents3: BinaryAssociation = BinaryAssociation(
    name="parents3",
    ends={
        Property(name="people_Person4", type=people_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="people_Person2", type=people_Person, multiplicity=Multiplicity(0, 2))
    }
)
father6: BinaryAssociation = BinaryAssociation(
    name="father6",
    ends={
        Property(name="people_Person7", type=people_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="people_Person5", type=people_Person, multiplicity=Multiplicity(1, 1))
    }
)
mother9: BinaryAssociation = BinaryAssociation(
    name="mother9",
    ends={
        Property(name="people_Person10", type=people_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="people_Person8", type=people_Person, multiplicity=Multiplicity(1, 1))
    }
)
people11: BinaryAssociation = BinaryAssociation(
    name="people11",
    ends={
        Property(name="people_Person12", type=people_Universe, multiplicity=Multiplicity(1, 1)),
        Property(name="people_Universe", type=people_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="people",
    types={people_Person, people_Universe, Gender},
    associations={children1, parents3, father6, mother9, people11},
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