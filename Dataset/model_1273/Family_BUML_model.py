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
family_ecore_Person = Class(name="family::ecore::Person")
family_ecore_Family = Class(name="family::ecore::Family")

# family_ecore_Person class attributes and methods
family_ecore_Person_name: Property = Property(name="name", type=StringType)
family_ecore_Person_age: Property = Property(name="age", type=IntegerType)
family_ecore_Person_height: Property = Property(name="height", type=FloatType)
family_ecore_Person.attributes={family_ecore_Person_name, family_ecore_Person_height, family_ecore_Person_age}

# family_ecore_Family class attributes and methods

# Relationships
hasFather1: BinaryAssociation = BinaryAssociation(
    name="hasFather1",
    ends={
        Property(name="family_ecore_Person", type=family_ecore_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="family_ecore_Person0", type=family_ecore_Person, multiplicity=Multiplicity(1, 1))
    }
)
hasSister3: BinaryAssociation = BinaryAssociation(
    name="hasSister3",
    ends={
        Property(name="family_ecore_Person4", type=family_ecore_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="family_ecore_Person2", type=family_ecore_Person, multiplicity=Multiplicity(0, 9999))
    }
)
hasUncle6: BinaryAssociation = BinaryAssociation(
    name="hasUncle6",
    ends={
        Property(name="family_ecore_Person7", type=family_ecore_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="family_ecore_Person5", type=family_ecore_Person, multiplicity=Multiplicity(0, 9999))
    }
)
hasBrother9: BinaryAssociation = BinaryAssociation(
    name="hasBrother9",
    ends={
        Property(name="family_ecore_Person10", type=family_ecore_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="family_ecore_Person8", type=family_ecore_Person, multiplicity=Multiplicity(0, 9999))
    }
)
member11: BinaryAssociation = BinaryAssociation(
    name="member11",
    ends={
        Property(name="family_ecore_Person12", type=family_ecore_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family_ecore_Family", type=family_ecore_Person, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="family_ecore",
    types={family_ecore_Person, family_ecore_Family},
    associations={hasFather1, hasSister3, hasUncle6, hasBrother9, member11},
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