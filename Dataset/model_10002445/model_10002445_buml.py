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
WELCOME_PAGE = Class(name="WELCOME_PAGE")
LoginPage = Class(name="LoginPage")
T = Class(name="T")
DATABASE_SYSTEM = Class(name="DATABASE_SYSTEM")
ACADEMIC_PAGE = Class(name="ACADEMIC_PAGE")
PLACEMENTS_PAGE = Class(name="PLACEMENTS_PAGE")
PERSONAL_PAGE = Class(name="PERSONAL_PAGE")

# WELCOME_PAGE class attributes and methods
WELCOME_PAGE_personal: Property = Property(name="personal", type=StringType)
WELCOME_PAGE_academic: Property = Property(name="academic", type=StringType)
WELCOME_PAGE_placements: Property = Property(name="placements", type=StringType)
WELCOME_PAGE.attributes={WELCOME_PAGE_placements, WELCOME_PAGE_academic, WELCOME_PAGE_personal}

# LoginPage class attributes and methods
LoginPage_User_name: Property = Property(name="User_name", type=StringType)
LoginPage.attributes={LoginPage_User_name}

# T class attributes and methods

# DATABASE_SYSTEM class attributes and methods
DATABASE_SYSTEM_Content: Property = Property(name="Content", type=BooleanType)
DATABASE_SYSTEM.attributes={DATABASE_SYSTEM_Content}

# ACADEMIC_PAGE class attributes and methods
ACADEMIC_PAGE_BRANCH: Property = Property(name="BRANCH", type=StringType)
ACADEMIC_PAGE_STUDIES: Property = Property(name="STUDIES", type=StringType)
ACADEMIC_PAGE.attributes={ACADEMIC_PAGE_STUDIES, ACADEMIC_PAGE_BRANCH}

# PLACEMENTS_PAGE class attributes and methods
PLACEMENTS_PAGE_SALARY: Property = Property(name="SALARY", type=IntegerType)
PLACEMENTS_PAGE_BRANCH: Property = Property(name="BRANCH", type=StringType)
PLACEMENTS_PAGE_INTREST: Property = Property(name="INTREST", type=StringType)
PLACEMENTS_PAGE.attributes={PLACEMENTS_PAGE_SALARY, PLACEMENTS_PAGE_BRANCH, PLACEMENTS_PAGE_INTREST}

# PERSONAL_PAGE class attributes and methods
PERSONAL_PAGE_BRANCH: Property = Property(name="BRANCH", type=StringType)
PERSONAL_PAGE_YEAR: Property = Property(name="YEAR", type=IntegerType)
PERSONAL_PAGE.attributes={PERSONAL_PAGE_YEAR, PERSONAL_PAGE_BRANCH}

# Relationships
User_Myprofile: BinaryAssociation = BinaryAssociation(
    name="User_Myprofile",
    ends={
        Property(name="user1", type=WELCOME_PAGE, multiplicity=Multiplicity(1, 1)),
        Property(name="myprofile0", type=LoginPage, multiplicity=Multiplicity(1, 1))
    }
)
User_Post: BinaryAssociation = BinaryAssociation(
    name="User_Post",
    ends={
        Property(name="post2", type=DATABASE_SYSTEM, multiplicity=Multiplicity(0, 9999)),
        Property(name="user3", type=WELCOME_PAGE, multiplicity=Multiplicity(1, 1))
    }
)
User_Group: BinaryAssociation = BinaryAssociation(
    name="User_Group",
    ends={
        Property(name="group4", type=ACADEMIC_PAGE, multiplicity=Multiplicity(0, 9999)),
        Property(name="user5", type=WELCOME_PAGE, multiplicity=Multiplicity(1, 1))
    }
)
PERSONAL_PAGE_WELCOME_PAGE: BinaryAssociation = BinaryAssociation(
    name="PERSONAL_PAGE_WELCOME_PAGE",
    ends={
        Property(name="wELCOME_PAGE6", type=WELCOME_PAGE, multiplicity=Multiplicity(0, 1)),
        Property(name="pERSONAL_PAGE7", type=PERSONAL_PAGE, multiplicity=Multiplicity(0, 1))
    }
)
WELCOME_PAGE_PLACEMENTS_PAGE: BinaryAssociation = BinaryAssociation(
    name="WELCOME_PAGE_PLACEMENTS_PAGE",
    ends={
        Property(name="pLACEMENTS_PAGE8", type=PLACEMENTS_PAGE, multiplicity=Multiplicity(0, 1)),
        Property(name="wELCOME_PAGE9", type=WELCOME_PAGE, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="b44afb2e_de19_4594_af36_1c51a26f4fcc",
    types={WELCOME_PAGE, LoginPage, T, DATABASE_SYSTEM, ACADEMIC_PAGE, PLACEMENTS_PAGE, PERSONAL_PAGE},
    associations={User_Myprofile, User_Post, User_Group, PERSONAL_PAGE_WELCOME_PAGE, WELCOME_PAGE_PLACEMENTS_PAGE},
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