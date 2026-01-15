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
Families_Country = Class(name="Families::Country")
NamedElement = Class(name="NamedElement")
Families_Family = Class(name="Families::Family")
Families_City = Class(name="Families::City")
Families_Company = Class(name="Families::Company")
Families_Parent = Class(name="Families::Parent")
Families_Child = Class(name="Families::Child")
Families_Neighborhood = Class(name="Families::Neighborhood")
Member = Class(name="Member")
Families_School = Class(name="Families::School")
Families_Service = Class(name="Families::Service")
Families_Member = Class(name="Families::Member", is_abstract=True)
Families_NamedElement = Class(name="Families::NamedElement", is_abstract=True)

# Families_Country class attributes and methods

# NamedElement class attributes and methods

# Families_Family class attributes and methods
Families_Family_lastName: Property = Property(name="lastName", type=StringType)
Families_Family.attributes={Families_Family_lastName}

# Families_City class attributes and methods

# Families_Company class attributes and methods

# Families_Parent class attributes and methods

# Families_Child class attributes and methods

# Families_Neighborhood class attributes and methods

# Member class attributes and methods

# Families_School class attributes and methods

# Families_Service class attributes and methods

# Families_Member class attributes and methods
Families_Member_firstName: Property = Property(name="firstName", type=StringType)
Families_Member.attributes={Families_Member_firstName}

# Families_NamedElement class attributes and methods
Families_NamedElement_name: Property = Property(name="name", type=StringType)
Families_NamedElement.attributes={Families_NamedElement_name}

# Relationships
families0: BinaryAssociation = BinaryAssociation(
    name="families0",
    ends={
        Property(name="Families_Family", type=Families_Country, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_Country", type=Families_Family, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
cities1: BinaryAssociation = BinaryAssociation(
    name="cities1",
    ends={
        Property(name="Families_City", type=Families_Country, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_Country2", type=Families_City, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
companies3: BinaryAssociation = BinaryAssociation(
    name="companies3",
    ends={
        Property(name="Families_Company", type=Families_Country, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_Country4", type=Families_Company, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fathers5: BinaryAssociation = BinaryAssociation(
    name="fathers5",
    ends={
        Property(name="Families_Parent", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_Family6", type=Families_Parent, multiplicity=Multiplicity(0, 2), is_composite=True)
    }
)
mothers7: BinaryAssociation = BinaryAssociation(
    name="mothers7",
    ends={
        Property(name="Families_Parent9", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_Family8", type=Families_Parent, multiplicity=Multiplicity(0, 2), is_composite=True)
    }
)
daughters10: BinaryAssociation = BinaryAssociation(
    name="daughters10",
    ends={
        Property(name="Families_Child", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_Family11", type=Families_Child, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sons12: BinaryAssociation = BinaryAssociation(
    name="sons12",
    ends={
        Property(name="Families_Child14", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_Family13", type=Families_Child, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
registeredIn15: BinaryAssociation = BinaryAssociation(
    name="registeredIn15",
    ends={
        Property(name="Neighborhood", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="contains", type=Families_Neighborhood, multiplicity=Multiplicity(1, 1))
    }
)
goesTo17: BinaryAssociation = BinaryAssociation(
    name="goesTo17",
    ends={
        Property(name="School", type=Families_Child, multiplicity=Multiplicity(1, 1)),
        Property(name="students", type=Families_School, multiplicity=Multiplicity(1, 1))
    }
)
contains18: BinaryAssociation = BinaryAssociation(
    name="contains18",
    ends={
        Property(name="Family", type=Families_Neighborhood, multiplicity=Multiplicity(1, 1)),
        Property(name="registeredIn", type=Families_Family, multiplicity=Multiplicity(1, 9999))
    }
)
schools19: BinaryAssociation = BinaryAssociation(
    name="schools19",
    ends={
        Property(name="Families_School", type=Families_Neighborhood, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_Neighborhood", type=Families_School, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
companies20: BinaryAssociation = BinaryAssociation(
    name="companies20",
    ends={
        Property(name="Company21", type=Families_City, multiplicity=Multiplicity(1, 1)),
        Property(name="isIn", type=Families_Company, multiplicity=Multiplicity(0, 9999))
    }
)
neighborhoods22: BinaryAssociation = BinaryAssociation(
    name="neighborhoods22",
    ends={
        Property(name="Families_Neighborhood24", type=Families_City, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_City23", type=Families_Neighborhood, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ordinary25: BinaryAssociation = BinaryAssociation(
    name="ordinary25",
    ends={
        Property(name="Families_Service", type=Families_School, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_School26", type=Families_Service, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
special27: BinaryAssociation = BinaryAssociation(
    name="special27",
    ends={
        Property(name="Families_Service29", type=Families_School, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_School28", type=Families_Service, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
students30: BinaryAssociation = BinaryAssociation(
    name="students30",
    ends={
        Property(name="Child", type=Families_School, multiplicity=Multiplicity(1, 1)),
        Property(name="goesTo", type=Families_Child, multiplicity=Multiplicity(0, 9999))
    }
)
employees31: BinaryAssociation = BinaryAssociation(
    name="employees31",
    ends={
        Property(name="Parent", type=Families_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="worksIn", type=Families_Parent, multiplicity=Multiplicity(0, 9999))
    }
)
isIn32: BinaryAssociation = BinaryAssociation(
    name="isIn32",
    ends={
        Property(name="City", type=Families_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="companies", type=Families_City, multiplicity=Multiplicity(1, 9999))
    }
)
worksIn16: BinaryAssociation = BinaryAssociation(
    name="worksIn16",
    ends={
        Property(name="Company", type=Families_Parent, multiplicity=Multiplicity(1, 1)),
        Property(name="employees", type=Families_Company, multiplicity=Multiplicity(0, 1))
    }
)
family33: BinaryAssociation = BinaryAssociation(
    name="family33",
    ends={
        Property(name="Families_Family34", type=Families_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_Member", type=Families_Family, multiplicity=Multiplicity(1, 1))
    }
)
livesIn35: BinaryAssociation = BinaryAssociation(
    name="livesIn35",
    ends={
        Property(name="Families_City37", type=Families_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_Member36", type=Families_City, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_Families_Country_NamedElement = Generalization(general=NamedElement, specific=Families_Country)
gen_Families_Parent_Member = Generalization(general=Member, specific=Families_Parent)
gen_Families_Child_Member = Generalization(general=Member, specific=Families_Child)
gen_Families_Neighborhood_NamedElement = Generalization(general=NamedElement, specific=Families_Neighborhood)
gen_Families_City_NamedElement = Generalization(general=NamedElement, specific=Families_City)
gen_Families_School_NamedElement = Generalization(general=NamedElement, specific=Families_School)
gen_Families_Company_NamedElement = Generalization(general=NamedElement, specific=Families_Company)

# Domain Model
domain_model = DomainModel(
    name="Families",
    types={Families_Country, NamedElement, Families_Family, Families_City, Families_Company, Families_Parent, Families_Child, Families_Neighborhood, Member, Families_School, Families_Service, Families_Member, Families_NamedElement},
    associations={families0, cities1, companies3, fathers5, mothers7, daughters10, sons12, registeredIn15, goesTo17, contains18, schools19, companies20, neighborhoods22, ordinary25, special27, students30, employees31, isIn32, worksIn16, family33, livesIn35},
    generalizations={gen_Families_Country_NamedElement, gen_Families_Parent_Member, gen_Families_Child_Member, gen_Families_Neighborhood_NamedElement, gen_Families_City_NamedElement, gen_Families_School_NamedElement, gen_Families_Company_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)