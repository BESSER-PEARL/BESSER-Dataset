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
DogBreed: Enumeration = Enumeration(
    name="DogBreed",
    literals={
            EnumerationLiteral(name="poodle"),
			EnumerationLiteral(name="labrador")
    }
)

# Classes
families_Family = Class(name="families::Family")
NamedElement = Class(name="NamedElement")
families_NamedElement = Class(name="families::NamedElement", is_abstract=True)
families_Account = Class(name="families::Account")
families_Pet = Class(name="families::Pet")
families_Person = Class(name="families::Person")
families_Dog = Class(name="families::Dog")
families_District = Class(name="families::District")
Pet = Class(name="Pet")
families_Suburb = Class(name="families::Suburb")
District = Class(name="District")
families_Model = Class(name="families::Model")
families_Bike = Class(name="families::Bike")
families_Band = Class(name="families::Band")

# families_Family class attributes and methods
families_Family_address: Property = Property(name="address", type=StringType)
families_Family_numberOfChildren: Property = Property(name="numberOfChildren", type=IntegerType)
families_Family_id: Property = Property(name="id", type=StringType)
families_Family_nuclear: Property = Property(name="nuclear", type=BooleanType)
families_Family_averageAge: Property = Property(name="averageAge", type=FloatType)
families_Family_lotteryNumbers: Property = Property(name="lotteryNumbers", type=IntegerType)
families_Family_averageAgePrecise: Property = Property(name="averageAgePrecise", type=FloatType)
families_Family.attributes={families_Family_averageAge, families_Family_numberOfChildren, families_Family_lotteryNumbers, families_Family_id, families_Family_address, families_Family_nuclear, families_Family_averageAgePrecise}

# NamedElement class attributes and methods

# families_NamedElement class attributes and methods
families_NamedElement_name: Property = Property(name="name", type=StringType)
families_NamedElement.attributes={families_NamedElement_name}

# families_Account class attributes and methods

# families_Pet class attributes and methods
families_Pet_male: Property = Property(name="male", type=BooleanType)
families_Pet.attributes={families_Pet_male}

# families_Person class attributes and methods

# families_Dog class attributes and methods
families_Dog_loud: Property = Property(name="loud", type=BooleanType)
families_Dog_breed: Property = Property(name="breed", type=StringType)
families_Dog.attributes={families_Dog_loud, families_Dog_breed}

# families_District class attributes and methods

# Pet class attributes and methods

# families_Suburb class attributes and methods

# District class attributes and methods

# families_Model class attributes and methods

# families_Bike class attributes and methods

# families_Band class attributes and methods

# Relationships
sharedAccounts6: BinaryAssociation = BinaryAssociation(
    name="sharedAccounts6",
    ends={
        Property(name="families_Account", type=families_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="families_Person7", type=families_Account, multiplicity=Multiplicity(0, 9999))
    }
)
pets0: BinaryAssociation = BinaryAssociation(
    name="pets0",
    ends={
        Property(name="families_Pet", type=families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="families_Family", type=families_Pet, multiplicity=Multiplicity(0, 9999))
    }
)
members1: BinaryAssociation = BinaryAssociation(
    name="members1",
    ends={
        Property(name="families_Person", type=families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="families_Family2", type=families_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dogs3: BinaryAssociation = BinaryAssociation(
    name="dogs3",
    ends={
        Property(name="families_Dog", type=families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="families_Family4", type=families_Dog, multiplicity=Multiplicity(1, 9999))
    }
)
district5: BinaryAssociation = BinaryAssociation(
    name="district5",
    ends={
        Property(name="District", type=families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="families", type=families_District, multiplicity=Multiplicity(0, 1))
    }
)
dogs23: BinaryAssociation = BinaryAssociation(
    name="dogs23",
    ends={
        Property(name="Dog", type=families_District, multiplicity=Multiplicity(1, 1)),
        Property(name="district24", type=families_Dog, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
accounts8: BinaryAssociation = BinaryAssociation(
    name="accounts8",
    ends={
        Property(name="families_Account10", type=families_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="families_Person9", type=families_Account, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
friends12: BinaryAssociation = BinaryAssociation(
    name="friends12",
    ends={
        Property(name="families_Person13", type=families_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="families_Person11", type=families_Person, multiplicity=Multiplicity(0, 9999))
    }
)
parents15: BinaryAssociation = BinaryAssociation(
    name="parents15",
    ends={
        Property(name="families_Person16", type=families_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="families_Person14", type=families_Person, multiplicity=Multiplicity(0, 2))
    }
)
allParents18: BinaryAssociation = BinaryAssociation(
    name="allParents18",
    ends={
        Property(name="families_Person19", type=families_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="families_Person17", type=families_Person, multiplicity=Multiplicity(0, 4))
    }
)
district20: BinaryAssociation = BinaryAssociation(
    name="district20",
    ends={
        Property(name="District21", type=families_Dog, multiplicity=Multiplicity(1, 1)),
        Property(name="dogs", type=families_District, multiplicity=Multiplicity(0, 1))
    }
)
families22: BinaryAssociation = BinaryAssociation(
    name="families22",
    ends={
        Property(name="Family", type=families_District, multiplicity=Multiplicity(1, 1)),
        Property(name="district", type=families_Family, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
contents25: BinaryAssociation = BinaryAssociation(
    name="contents25",
    ends={
        Property(name="families_NamedElement", type=families_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="families_Model", type=families_NamedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contents226: BinaryAssociation = BinaryAssociation(
    name="contents226",
    ends={
        Property(name="families_NamedElement28", type=families_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="families_Model27", type=families_NamedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rider29: BinaryAssociation = BinaryAssociation(
    name="rider29",
    ends={
        Property(name="families_Person30", type=families_Bike, multiplicity=Multiplicity(1, 1)),
        Property(name="families_Bike", type=families_Person, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owner31: BinaryAssociation = BinaryAssociation(
    name="owner31",
    ends={
        Property(name="families_Family33", type=families_Bike, multiplicity=Multiplicity(1, 1)),
        Property(name="families_Bike32", type=families_Family, multiplicity=Multiplicity(0, 1))
    }
)
members34: BinaryAssociation = BinaryAssociation(
    name="members34",
    ends={
        Property(name="families_Person35", type=families_Band, multiplicity=Multiplicity(1, 1)),
        Property(name="families_Band", type=families_Person, multiplicity=Multiplicity(3, 9999))
    }
)

# Generalizations
gen_families_Family_NamedElement = Generalization(general=NamedElement, specific=families_Family)
gen_families_Pet_NamedElement = Generalization(general=NamedElement, specific=families_Pet)
gen_families_Person_NamedElement = Generalization(general=NamedElement, specific=families_Person)
gen_families_Dog_Pet = Generalization(general=Pet, specific=families_Dog)
gen_families_Suburb_District = Generalization(general=District, specific=families_Suburb)
gen_families_Model_NamedElement = Generalization(general=NamedElement, specific=families_Model)

# Domain Model
domain_model = DomainModel(
    name="families",
    types={families_Family, NamedElement, families_NamedElement, families_Account, families_Pet, families_Person, families_Dog, families_District, Pet, families_Suburb, District, families_Model, families_Bike, families_Band, DogBreed},
    associations={sharedAccounts6, pets0, members1, dogs3, district5, dogs23, accounts8, friends12, parents15, allParents18, district20, families22, contents25, contents226, rider29, owner31, members34},
    generalizations={gen_families_Family_NamedElement, gen_families_Pet_NamedElement, gen_families_Person_NamedElement, gen_families_Dog_Pet, gen_families_Suburb_District, gen_families_Model_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)