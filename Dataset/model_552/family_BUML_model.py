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
family_Members = Class(name="family::Members")
NamedElement = Class(name="NamedElement")
family_Person = Class(name="family::Person")
family_NamedElement = Class(name="family::NamedElement", is_abstract=True)
family_Family = Class(name="family::Family")

# family_Members class attributes and methods
family_Members_hasChild: Property = Property(name="hasChild", type=BooleanType)
family_Members.attributes={family_Members_hasChild}

# NamedElement class attributes and methods

# family_Person class attributes and methods
family_Person_surname: Property = Property(name="surname", type=StringType)
family_Person_age: Property = Property(name="age", type=IntegerType)
family_Person_gender: Property = Property(name="gender", type=StringType)
family_Person.attributes={family_Person_age, family_Person_surname, family_Person_gender}

# family_NamedElement class attributes and methods
family_NamedElement_name: Property = Property(name="name", type=StringType)
family_NamedElement.attributes={family_NamedElement_name}

# family_Family class attributes and methods
family_Family_numberOfComponents: Property = Property(name="numberOfComponents", type=IntegerType)
family_Family_familyIncome: Property = Property(name="familyIncome", type=FloatType)
family_Family.attributes={family_Family_familyIncome, family_Family_numberOfComponents}

# Relationships
person0: BinaryAssociation = BinaryAssociation(
    name="person0",
    ends={
        Property(name="family_Person", type=family_Members, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Members", type=family_Person, multiplicity=Multiplicity(1, 1))
    }
)
member1: BinaryAssociation = BinaryAssociation(
    name="member1",
    ends={
        Property(name="family_Members2", type=family_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Family", type=family_Members, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_family_Members_NamedElement = Generalization(general=NamedElement, specific=family_Members)
gen_family_Person_NamedElement = Generalization(general=NamedElement, specific=family_Person)
gen_family_Family_NamedElement = Generalization(general=NamedElement, specific=family_Family)

# Domain Model
domain_model = DomainModel(
    name="family",
    types={family_Members, NamedElement, family_Person, family_NamedElement, family_Family},
    associations={person0, member1},
    generalizations={gen_family_Members_NamedElement, gen_family_Person_NamedElement, gen_family_Family_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)