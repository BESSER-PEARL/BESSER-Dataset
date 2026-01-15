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
family_Family = Class(name="family::Family")
family_Person = Class(name="family::Person")

# family_Family class attributes and methods
family_Family_name: Property = Property(name="name", type=StringType)
family_Family.attributes={family_Family_name}

# family_Person class attributes and methods
family_Person_name: Property = Property(name="name", type=StringType)
family_Person_male: Property = Property(name="male", type=BooleanType)
family_Person.attributes={family_Person_name, family_Person_male}

# Relationships
members0: BinaryAssociation = BinaryAssociation(
    name="members0",
    ends={
        Property(name="family_Person", type=family_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Family", type=family_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="family",
    types={family_Family, family_Person},
    associations={members0},
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