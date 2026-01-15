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
familyleft1_Family = Class(name="familyleft1::Family")
familyleft1_Mother = Class(name="familyleft1::Mother")
familyleft1_Father = Class(name="familyleft1::Father")
familyleft1_Son = Class(name="familyleft1::Son")

# familyleft1_Family class attributes and methods
familyleft1_Family_surname: Property = Property(name="surname", type=StringType)
familyleft1_Family_location: Property = Property(name="location", type=StringType)
familyleft1_Family.attributes={familyleft1_Family_surname, familyleft1_Family_location}

# familyleft1_Mother class attributes and methods
familyleft1_Mother_name: Property = Property(name="name", type=StringType)
familyleft1_Mother_age: Property = Property(name="age", type=IntegerType)
familyleft1_Mother.attributes={familyleft1_Mother_age, familyleft1_Mother_name}

# familyleft1_Father class attributes and methods
familyleft1_Father_age: Property = Property(name="age", type=IntegerType)
familyleft1_Father_name: Property = Property(name="name", type=StringType)
familyleft1_Father.attributes={familyleft1_Father_age, familyleft1_Father_name}

# familyleft1_Son class attributes and methods
familyleft1_Son_name: Property = Property(name="name", type=StringType)
familyleft1_Son_age: Property = Property(name="age", type=IntegerType)
familyleft1_Son_sex: Property = Property(name="sex", type=StringType)
familyleft1_Son.attributes={familyleft1_Son_age, familyleft1_Son_name, familyleft1_Son_sex}

# Relationships
family0: BinaryAssociation = BinaryAssociation(
    name="family0",
    ends={
        Property(name="Family", type=familyleft1_Father, multiplicity=Multiplicity(1, 1)),
        Property(name="father", type=familyleft1_Family, multiplicity=Multiplicity(0, 1))
    }
)
mother6: BinaryAssociation = BinaryAssociation(
    name="mother6",
    ends={
        Property(name="Mother", type=familyleft1_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family7", type=familyleft1_Mother, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sons8: BinaryAssociation = BinaryAssociation(
    name="sons8",
    ends={
        Property(name="Son", type=familyleft1_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family9", type=familyleft1_Son, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
family1: BinaryAssociation = BinaryAssociation(
    name="family1",
    ends={
        Property(name="Family2", type=familyleft1_Mother, multiplicity=Multiplicity(1, 1)),
        Property(name="mother", type=familyleft1_Family, multiplicity=Multiplicity(0, 1))
    }
)
family3: BinaryAssociation = BinaryAssociation(
    name="family3",
    ends={
        Property(name="Family4", type=familyleft1_Son, multiplicity=Multiplicity(1, 1)),
        Property(name="sons", type=familyleft1_Family, multiplicity=Multiplicity(0, 1))
    }
)
father5: BinaryAssociation = BinaryAssociation(
    name="father5",
    ends={
        Property(name="Father", type=familyleft1_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family", type=familyleft1_Father, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="familyleft1",
    types={familyleft1_Family, familyleft1_Mother, familyleft1_Father, familyleft1_Son},
    associations={family0, mother6, sons8, family1, family3, father5},
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