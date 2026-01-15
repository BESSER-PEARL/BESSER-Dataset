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
families_City = Class(name="families::City")
families_Company = Class(name="families::Company")
families_Parent = Class(name="families::Parent")
families_Child = Class(name="families::Child")
families_Country = Class(name="families::Country")
NamedElement = Class(name="NamedElement")
families_Family = Class(name="families::Family")
families_Service = Class(name="families::Service")
families_Neighborhood = Class(name="families::Neighborhood")
Member = Class(name="Member")
families_School = Class(name="families::School")
families_Member = Class(name="families::Member", is_abstract=True)
families_NamedElement = Class(name="families::NamedElement", is_abstract=True)

# families_City class attributes and methods

# families_Company class attributes and methods

# families_Parent class attributes and methods

# families_Child class attributes and methods

# families_Country class attributes and methods

# NamedElement class attributes and methods

# families_Family class attributes and methods
families_Family_lastName: Property = Property(name="lastName", type=StringType)
families_Family.attributes={families_Family_lastName}

# families_Service class attributes and methods

# families_Neighborhood class attributes and methods

# Member class attributes and methods

# families_School class attributes and methods

# families_Member class attributes and methods
families_Member_firstName: Property = Property(name="firstName", type=StringType)
families_Member.attributes={families_Member_firstName}

# families_NamedElement class attributes and methods
families_NamedElement_name: Property = Property(name="name", type=StringType)
families_NamedElement.attributes={families_NamedElement_name}

# Relationships
cities1: BinaryAssociation = BinaryAssociation(
    name="cities1",
    ends={
        Property(name="families_City", type=families_Country, multiplicity=Multiplicity(1, 1)),
        Property(name="families_Country2", type=families_City, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
companies3: BinaryAssociation = BinaryAssociation(
    name="companies3",
    ends={
        Property(name="families_Company", type=families_Country, multiplicity=Multiplicity(1, 1)),
        Property(name="families_Country4", type=families_Company, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fathers5: BinaryAssociation = BinaryAssociation(
    name="fathers5",
    ends={
        Property(name="families_Parent", type=families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="families_Family6", type=families_Parent, multiplicity=Multiplicity(0, 2), is_composite=True)
    }
)
mothers7: BinaryAssociation = BinaryAssociation(
    name="mothers7",
    ends={
        Property(name="families_Parent9", type=families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="families_Family8", type=families_Parent, multiplicity=Multiplicity(0, 2), is_composite=True)
    }
)
daughters10: BinaryAssociation = BinaryAssociation(
    name="daughters10",
    ends={
        Property(name="families_Child", type=families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="families_Family11", type=families_Child, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
families0: BinaryAssociation = BinaryAssociation(
    name="families0",
    ends={
        Property(name="families_Family", type=families_Country, multiplicity=Multiplicity(1, 1)),
        Property(name="families_Country", type=families_Family, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
companies20: BinaryAssociation = BinaryAssociation(
    name="companies20",
    ends={
        Property(name="Company21", type=families_City, multiplicity=Multiplicity(1, 1)),
        Property(name="isIn", type=families_Company, multiplicity=Multiplicity(0, 9999))
    }
)
neighborhoods22: BinaryAssociation = BinaryAssociation(
    name="neighborhoods22",
    ends={
        Property(name="families_Neighborhood24", type=families_City, multiplicity=Multiplicity(1, 1)),
        Property(name="families_City23", type=families_Neighborhood, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ordinary25: BinaryAssociation = BinaryAssociation(
    name="ordinary25",
    ends={
        Property(name="families_Service", type=families_School, multiplicity=Multiplicity(1, 1)),
        Property(name="families_School26", type=families_Service, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
special27: BinaryAssociation = BinaryAssociation(
    name="special27",
    ends={
        Property(name="families_Service29", type=families_School, multiplicity=Multiplicity(1, 1)),
        Property(name="families_School28", type=families_Service, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
students30: BinaryAssociation = BinaryAssociation(
    name="students30",
    ends={
        Property(name="Child", type=families_School, multiplicity=Multiplicity(1, 1)),
        Property(name="goesTo", type=families_Child, multiplicity=Multiplicity(0, 9999))
    }
)
sons12: BinaryAssociation = BinaryAssociation(
    name="sons12",
    ends={
        Property(name="families_Child14", type=families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="families_Family13", type=families_Child, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
registeredIn15: BinaryAssociation = BinaryAssociation(
    name="registeredIn15",
    ends={
        Property(name="Neighborhood", type=families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="contains", type=families_Neighborhood, multiplicity=Multiplicity(1, 1))
    }
)
worksIn16: BinaryAssociation = BinaryAssociation(
    name="worksIn16",
    ends={
        Property(name="Company", type=families_Parent, multiplicity=Multiplicity(1, 1)),
        Property(name="employees", type=families_Company, multiplicity=Multiplicity(0, 1))
    }
)
goesTo17: BinaryAssociation = BinaryAssociation(
    name="goesTo17",
    ends={
        Property(name="School", type=families_Child, multiplicity=Multiplicity(1, 1)),
        Property(name="students", type=families_School, multiplicity=Multiplicity(1, 1))
    }
)
contains18: BinaryAssociation = BinaryAssociation(
    name="contains18",
    ends={
        Property(name="Family", type=families_Neighborhood, multiplicity=Multiplicity(1, 1)),
        Property(name="registeredIn", type=families_Family, multiplicity=Multiplicity(1, 9999))
    }
)
schools19: BinaryAssociation = BinaryAssociation(
    name="schools19",
    ends={
        Property(name="families_School", type=families_Neighborhood, multiplicity=Multiplicity(1, 1)),
        Property(name="families_Neighborhood", type=families_School, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
employees31: BinaryAssociation = BinaryAssociation(
    name="employees31",
    ends={
        Property(name="Parent", type=families_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="worksIn", type=families_Parent, multiplicity=Multiplicity(0, 9999))
    }
)
isIn32: BinaryAssociation = BinaryAssociation(
    name="isIn32",
    ends={
        Property(name="City", type=families_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="companies", type=families_City, multiplicity=Multiplicity(1, 9999))
    }
)
family33: BinaryAssociation = BinaryAssociation(
    name="family33",
    ends={
        Property(name="families_Family34", type=families_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="families_Member", type=families_Family, multiplicity=Multiplicity(1, 1))
    }
)
livesIn35: BinaryAssociation = BinaryAssociation(
    name="livesIn35",
    ends={
        Property(name="families_City37", type=families_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="families_Member36", type=families_City, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_families_Country_NamedElement = Generalization(general=NamedElement, specific=families_Country)
gen_families_School_NamedElement = Generalization(general=NamedElement, specific=families_School)
gen_families_Parent_Member = Generalization(general=Member, specific=families_Parent)
gen_families_Child_Member = Generalization(general=Member, specific=families_Child)
gen_families_Neighborhood_NamedElement = Generalization(general=NamedElement, specific=families_Neighborhood)
gen_families_City_NamedElement = Generalization(general=NamedElement, specific=families_City)
gen_families_Company_NamedElement = Generalization(general=NamedElement, specific=families_Company)

# Domain Model
domain_model = DomainModel(
    name="families",
    types={families_City, families_Company, families_Parent, families_Child, families_Country, NamedElement, families_Family, families_Service, families_Neighborhood, Member, families_School, families_Member, families_NamedElement},
    associations={cities1, companies3, fathers5, mothers7, daughters10, families0, companies20, neighborhoods22, ordinary25, special27, students30, sons12, registeredIn15, worksIn16, goesTo17, contains18, schools19, employees31, isIn32, family33, livesIn35},
    generalizations={gen_families_Country_NamedElement, gen_families_School_NamedElement, gen_families_Parent_Member, gen_families_Child_Member, gen_families_Neighborhood_NamedElement, gen_families_City_NamedElement, gen_families_Company_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)