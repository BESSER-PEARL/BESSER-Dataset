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
CATEGORY = Class(name="CATEGORY", is_abstract=True)
POST = Class(name="POST", is_abstract=True)
USER_TYPE = Class(name="USER_TYPE")
Admin = Class(name="Admin")
User = Class(name="User")

# CATEGORY class attributes and methods

# POST class attributes and methods
POST_name: Property = Property(name="name", type=StringType)
POST.attributes={POST_name}

# USER_TYPE class attributes and methods

# Admin class attributes and methods

# User class attributes and methods

# Relationships
USER_TYPE_Admin: BinaryAssociation = BinaryAssociation(
    name="USER_TYPE_Admin",
    ends={
        Property(name="admin0", type=Admin, multiplicity=Multiplicity(0, 1)),
        Property(name="admin1", type=USER_TYPE, multiplicity=Multiplicity(1, 1))
    }
)
USER_TYPE_User: BinaryAssociation = BinaryAssociation(
    name="USER_TYPE_User",
    ends={
        Property(name="user2", type=User, multiplicity=Multiplicity(1, 9999)),
        Property(name="User3", type=USER_TYPE, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="c5db6e5f_d590_4193_a727_3681467bd795",
    types={CATEGORY, POST, USER_TYPE, Admin, User},
    associations={USER_TYPE_Admin, USER_TYPE_User},
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