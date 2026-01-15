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
familyleft2_Family = Class(name="familyleft2::Family")
familyleft2_Mother = Class(name="familyleft2::Mother")
familyleft2_Son = Class(name="familyleft2::Son")
familyleft2_Daughter = Class(name="familyleft2::Daughter")
familyleft2_Person = Class(name="familyleft2::Person", is_abstract=True)
familyleft2_Father = Class(name="familyleft2::Father")
Person = Class(name="Person")

# familyleft2_Family class attributes and methods

# familyleft2_Mother class attributes and methods
familyleft2_Mother_address: Property = Property(name="address", type=StringType)
familyleft2_Mother.attributes={familyleft2_Mother_address}

# familyleft2_Son class attributes and methods

# familyleft2_Daughter class attributes and methods

# familyleft2_Person class attributes and methods
familyleft2_Person_name: Property = Property(name="name", type=StringType)
familyleft2_Person_age: Property = Property(name="age", type=IntegerType)
familyleft2_Person_isMale: Property = Property(name="isMale", type=BooleanType)
familyleft2_Person.attributes={familyleft2_Person_name, familyleft2_Person_age, familyleft2_Person_isMale}

# familyleft2_Father class attributes and methods
familyleft2_Father_address: Property = Property(name="address", type=StringType)
familyleft2_Father.attributes={familyleft2_Father_address}

# Person class attributes and methods

# Relationships
family0: BinaryAssociation = BinaryAssociation(
    name="family0",
    ends={
        Property(name="Family", type=familyleft2_Father, multiplicity=Multiplicity(1, 1)),
        Property(name="father", type=familyleft2_Family, multiplicity=Multiplicity(0, 1))
    }
)
family1: BinaryAssociation = BinaryAssociation(
    name="family1",
    ends={
        Property(name="Family2", type=familyleft2_Mother, multiplicity=Multiplicity(1, 1)),
        Property(name="mother", type=familyleft2_Family, multiplicity=Multiplicity(0, 1))
    }
)
family3: BinaryAssociation = BinaryAssociation(
    name="family3",
    ends={
        Property(name="Family4", type=familyleft2_Son, multiplicity=Multiplicity(1, 1)),
        Property(name="sons", type=familyleft2_Family, multiplicity=Multiplicity(0, 1))
    }
)
family5: BinaryAssociation = BinaryAssociation(
    name="family5",
    ends={
        Property(name="Family6", type=familyleft2_Daughter, multiplicity=Multiplicity(1, 1)),
        Property(name="daughters", type=familyleft2_Family, multiplicity=Multiplicity(0, 1))
    }
)
father7: BinaryAssociation = BinaryAssociation(
    name="father7",
    ends={
        Property(name="Father", type=familyleft2_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family", type=familyleft2_Father, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mother8: BinaryAssociation = BinaryAssociation(
    name="mother8",
    ends={
        Property(name="Mother", type=familyleft2_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family9", type=familyleft2_Mother, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sons10: BinaryAssociation = BinaryAssociation(
    name="sons10",
    ends={
        Property(name="Son", type=familyleft2_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family11", type=familyleft2_Son, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
daughters12: BinaryAssociation = BinaryAssociation(
    name="daughters12",
    ends={
        Property(name="Daughter", type=familyleft2_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family13", type=familyleft2_Daughter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_familyleft2_Father_Person = Generalization(general=Person, specific=familyleft2_Father)
gen_familyleft2_Mother_Person = Generalization(general=Person, specific=familyleft2_Mother)
gen_familyleft2_Son_Person = Generalization(general=Person, specific=familyleft2_Son)
gen_familyleft2_Daughter_Person = Generalization(general=Person, specific=familyleft2_Daughter)

# Domain Model
domain_model = DomainModel(
    name="familyleft2",
    types={familyleft2_Family, familyleft2_Mother, familyleft2_Son, familyleft2_Daughter, familyleft2_Person, familyleft2_Father, Person},
    associations={family0, family1, family3, family5, father7, mother8, sons10, daughters12},
    generalizations={gen_familyleft2_Father_Person, gen_familyleft2_Mother_Person, gen_familyleft2_Son_Person, gen_familyleft2_Daughter_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)