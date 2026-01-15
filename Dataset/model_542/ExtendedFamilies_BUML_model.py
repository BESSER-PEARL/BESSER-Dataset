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
ExtendedFamilies_Family = Class(name="ExtendedFamilies::Family")
ExtendedFamilies_Person = Class(name="ExtendedFamilies::Person", is_abstract=True)
ExtendedFamilies_Male = Class(name="ExtendedFamilies::Male")
Person = Class(name="Person")
ExtendedFamilies_Female = Class(name="ExtendedFamilies::Female")

# ExtendedFamilies_Family class attributes and methods
ExtendedFamilies_Family_lastName: Property = Property(name="lastName", type=StringType)
ExtendedFamilies_Family.attributes={ExtendedFamilies_Family_lastName}

# ExtendedFamilies_Person class attributes and methods
ExtendedFamilies_Person_firstName: Property = Property(name="firstName", type=StringType)
ExtendedFamilies_Person.attributes={ExtendedFamilies_Person_firstName}

# ExtendedFamilies_Male class attributes and methods

# Person class attributes and methods

# ExtendedFamilies_Female class attributes and methods

# Relationships
members0: BinaryAssociation = BinaryAssociation(
    name="members0",
    ends={
        Property(name="Person", type=ExtendedFamilies_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family", type=ExtendedFamilies_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
family1: BinaryAssociation = BinaryAssociation(
    name="family1",
    ends={
        Property(name="Family", type=ExtendedFamilies_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="members", type=ExtendedFamilies_Family, multiplicity=Multiplicity(0, 1))
    }
)
children3: BinaryAssociation = BinaryAssociation(
    name="children3",
    ends={
        Property(name="Person4", type=ExtendedFamilies_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="parents", type=ExtendedFamilies_Person, multiplicity=Multiplicity(0, 9999))
    }
)
parents6: BinaryAssociation = BinaryAssociation(
    name="parents6",
    ends={
        Property(name="Person7", type=ExtendedFamilies_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=ExtendedFamilies_Person, multiplicity=Multiplicity(0, 2))
    }
)

# Generalizations
gen_ExtendedFamilies_Male_Person = Generalization(general=Person, specific=ExtendedFamilies_Male)
gen_ExtendedFamilies_Female_Person = Generalization(general=Person, specific=ExtendedFamilies_Female)

# Domain Model
domain_model = DomainModel(
    name="ExtendedFamilies",
    types={ExtendedFamilies_Family, ExtendedFamilies_Person, ExtendedFamilies_Male, Person, ExtendedFamilies_Female},
    associations={members0, family1, children3, parents6},
    generalizations={gen_ExtendedFamilies_Male_Person, gen_ExtendedFamilies_Female_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)