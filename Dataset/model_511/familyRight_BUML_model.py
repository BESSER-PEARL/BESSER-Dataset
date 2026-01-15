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
familyright_Family = Class(name="familyright::Family")
familyright_Mother = Class(name="familyright::Mother")
familyright_Son = Class(name="familyright::Son")
familyright_Daughter = Class(name="familyright::Daughter")
familyright_Father = Class(name="familyright::Father")

# familyright_Family class attributes and methods

# familyright_Mother class attributes and methods
familyright_Mother_name: Property = Property(name="name", type=StringType)
familyright_Mother_age: Property = Property(name="age", type=IntegerType)
familyright_Mother_address: Property = Property(name="address", type=StringType)
familyright_Mother.attributes={familyright_Mother_name, familyright_Mother_address, familyright_Mother_age}

# familyright_Son class attributes and methods
familyright_Son_name: Property = Property(name="name", type=StringType)
familyright_Son_age: Property = Property(name="age", type=IntegerType)
familyright_Son.attributes={familyright_Son_age, familyright_Son_name}

# familyright_Daughter class attributes and methods
familyright_Daughter_name: Property = Property(name="name", type=StringType)
familyright_Daughter_age: Property = Property(name="age", type=IntegerType)
familyright_Daughter.attributes={familyright_Daughter_age, familyright_Daughter_name}

# familyright_Father class attributes and methods
familyright_Father_name: Property = Property(name="name", type=StringType)
familyright_Father_age: Property = Property(name="age", type=IntegerType)
familyright_Father_address: Property = Property(name="address", type=StringType)
familyright_Father.attributes={familyright_Father_name, familyright_Father_age, familyright_Father_address}

# Relationships
family0: BinaryAssociation = BinaryAssociation(
    name="family0",
    ends={
        Property(name="Family", type=familyright_Father, multiplicity=Multiplicity(1, 1)),
        Property(name="father", type=familyright_Family, multiplicity=Multiplicity(0, 1))
    }
)
family1: BinaryAssociation = BinaryAssociation(
    name="family1",
    ends={
        Property(name="Family2", type=familyright_Mother, multiplicity=Multiplicity(1, 1)),
        Property(name="mother", type=familyright_Family, multiplicity=Multiplicity(0, 1))
    }
)
family3: BinaryAssociation = BinaryAssociation(
    name="family3",
    ends={
        Property(name="Family4", type=familyright_Son, multiplicity=Multiplicity(1, 1)),
        Property(name="sons", type=familyright_Family, multiplicity=Multiplicity(0, 1))
    }
)
family5: BinaryAssociation = BinaryAssociation(
    name="family5",
    ends={
        Property(name="Family6", type=familyright_Daughter, multiplicity=Multiplicity(1, 1)),
        Property(name="daughters", type=familyright_Family, multiplicity=Multiplicity(0, 1))
    }
)
father7: BinaryAssociation = BinaryAssociation(
    name="father7",
    ends={
        Property(name="Father", type=familyright_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family", type=familyright_Father, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mother8: BinaryAssociation = BinaryAssociation(
    name="mother8",
    ends={
        Property(name="Mother", type=familyright_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family9", type=familyright_Mother, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sons10: BinaryAssociation = BinaryAssociation(
    name="sons10",
    ends={
        Property(name="Son", type=familyright_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family11", type=familyright_Son, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
daughters12: BinaryAssociation = BinaryAssociation(
    name="daughters12",
    ends={
        Property(name="Daughter", type=familyright_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family13", type=familyright_Daughter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="familyright",
    types={familyright_Family, familyright_Mother, familyright_Son, familyright_Daughter, familyright_Father},
    associations={family0, family1, family3, family5, father7, mother8, sons10, daughters12},
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