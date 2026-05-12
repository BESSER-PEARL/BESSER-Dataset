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
Database_system = Class(name="Database_system")
WebUser = Class(name="WebUser")
PLACEMENTS_PAGE = Class(name="PLACEMENTS_PAGE")
PERSONAL_PAGE = Class(name="PERSONAL_PAGE")
ACADEMIC_PAGE = Class(name="ACADEMIC_PAGE")
Welcome = Class(name="Welcome")

# Database_system class attributes and methods
Database_system_Content: Property = Property(name="Content", type=BooleanType)
Database_system.attributes={Database_system_Content}

# WebUser class attributes and methods
WebUser_login: Property = Property(name="login", type=StringType)
WebUser_password: Property = Property(name="password", type=StringType)
WebUser_state: Property = Property(name="state", type=StringType)
WebUser.attributes={WebUser_state, WebUser_password, WebUser_login}

# PLACEMENTS_PAGE class attributes and methods
PLACEMENTS_PAGE_SALARY: Property = Property(name="SALARY", type=IntegerType)
PLACEMENTS_PAGE_BRANCH: Property = Property(name="BRANCH", type=StringType)
PLACEMENTS_PAGE_INTREST: Property = Property(name="INTREST", type=StringType)
PLACEMENTS_PAGE.attributes={PLACEMENTS_PAGE_INTREST, PLACEMENTS_PAGE_SALARY, PLACEMENTS_PAGE_BRANCH}

# PERSONAL_PAGE class attributes and methods
PERSONAL_PAGE_YEAR: Property = Property(name="YEAR", type=IntegerType)
PERSONAL_PAGE_BRANCH: Property = Property(name="BRANCH", type=StringType)
PERSONAL_PAGE.attributes={PERSONAL_PAGE_YEAR, PERSONAL_PAGE_BRANCH}

# ACADEMIC_PAGE class attributes and methods
ACADEMIC_PAGE_BRANCH: Property = Property(name="BRANCH", type=StringType)
ACADEMIC_PAGE_STUDIES: Property = Property(name="STUDIES", type=StringType)
ACADEMIC_PAGE.attributes={ACADEMIC_PAGE_BRANCH, ACADEMIC_PAGE_STUDIES}

# Welcome class attributes and methods
Welcome_personal: Property = Property(name="personal", type=StringType)
Welcome_academic: Property = Property(name="academic", type=StringType)
Welcome_placements: Property = Property(name="placements", type=StringType)
Welcome.attributes={Welcome_personal, Welcome_placements, Welcome_academic}

# Relationships
Product_LineItem: BinaryAssociation = BinaryAssociation(
    name="Product_LineItem",
    ends={
        Property(name="lineItems0", type=PERSONAL_PAGE, multiplicity=Multiplicity(0, 9999)),
        Property(name="product1", type=ACADEMIC_PAGE, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="b821d03f_f61a_4df7_8701_2cccf8babbf5",
    types={Database_system, WebUser, PLACEMENTS_PAGE, PERSONAL_PAGE, ACADEMIC_PAGE, Welcome},
    associations={Product_LineItem},
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