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
family_Father = Class(name="family_Father")
family_Son = Class(name="family_Son")
family_Daughter = Class(name="family_Daughter")
family_FatherInLove = Class(name="family_FatherInLove")
family_Family = Class(name="family_Family")
family_Mother = Class(name="family_Mother")

# family_Father class attributes and methods
family_Father_Name: Property = Property(name="Name", type=StringType)
family_Father_Age: Property = Property(name="Age", type=IntegerType)
family_Father.attributes={family_Father_Age, family_Father_Name}

# family_Son class attributes and methods
family_Son_Name: Property = Property(name="Name", type=StringType)
family_Son_Age: Property = Property(name="Age", type=IntegerType)
family_Son.attributes={family_Son_Name, family_Son_Age}

# family_Daughter class attributes and methods
family_Daughter_Name: Property = Property(name="Name", type=StringType)
family_Daughter_Age: Property = Property(name="Age", type=IntegerType)
family_Daughter.attributes={family_Daughter_Name, family_Daughter_Age}

# family_FatherInLove class attributes and methods
family_FatherInLove_Name: Property = Property(name="Name", type=StringType)
family_FatherInLove_Age: Property = Property(name="Age", type=IntegerType)
family_FatherInLove.attributes={family_FatherInLove_Name, family_FatherInLove_Age}

# family_Family class attributes and methods

# family_Mother class attributes and methods
family_Mother_Name: Property = Property(name="Name", type=StringType)
family_Mother_Age: Property = Property(name="Age", type=IntegerType)
family_Mother.attributes={family_Mother_Age, family_Mother_Name}

# Relationships
son1: BinaryAssociation = BinaryAssociation(
    name="son1",
    ends={
        Property(name="family_Son", type=family_Father, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Father2", type=family_Son, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
daughter3: BinaryAssociation = BinaryAssociation(
    name="daughter3",
    ends={
        Property(name="family_Daughter", type=family_Father, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Father4", type=family_Daughter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fatherinlove5: BinaryAssociation = BinaryAssociation(
    name="fatherinlove5",
    ends={
        Property(name="family_FatherInLove", type=family_Mother, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Mother6", type=family_FatherInLove, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
father7: BinaryAssociation = BinaryAssociation(
    name="father7",
    ends={
        Property(name="family_Father8", type=family_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Family", type=family_Father, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
wife0: BinaryAssociation = BinaryAssociation(
    name="wife0",
    ends={
        Property(name="family_Mother", type=family_Father, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Father", type=family_Mother, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="family",
    types={family_Father, family_Son, family_Daughter, family_FatherInLove, family_Family, family_Mother},
    associations={son1, daughter3, fatherinlove5, father7, wife0},
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