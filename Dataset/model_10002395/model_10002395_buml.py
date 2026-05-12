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
Places = Class(name="Places")
Reviews = Class(name="Reviews")
Users = Class(name="Users")

# Places class attributes and methods
Places_ID: Property = Property(name="ID", type=IntegerType)
Places_address: Property = Property(name="address", type=StringType)
Places_opening_times: Property = Property(name="opening_times", type=DateType)
Places_review_count: Property = Property(name="review_count", type=IntegerType)
Places_place_id: Property = Property(name="place_id", type=StringType)
Places_wifi: Property = Property(name="wifi", type=StringType)
Places_plugs: Property = Property(name="plugs", type=StringType)
Places_music: Property = Property(name="music", type=StringType)
Places.attributes={Places_plugs, Places_review_count, Places_wifi, Places_place_id, Places_opening_times, Places_music, Places_ID, Places_address}

# Reviews class attributes and methods
Reviews_ID: Property = Property(name="ID", type=IntegerType)
Reviews_business_id: Property = Property(name="business_id", type=IntegerType)
Reviews_user_id: Property = Property(name="user_id", type=IntegerType)
Reviews_date: Property = Property(name="date", type=DateType)
Reviews_text: Property = Property(name="text", type=StringType)
Reviews_rating: Property = Property(name="rating", type=IntegerType)
Reviews.attributes={Reviews_ID, Reviews_date, Reviews_business_id, Reviews_user_id, Reviews_rating, Reviews_text}

# Users class attributes and methods
Users_ID: Property = Property(name="ID", type=IntegerType)
Users_name: Property = Property(name="name", type=StringType)
Users_average_star: Property = Property(name="average_star", type=IntegerType)
Users_review_count: Property = Property(name="review_count", type=IntegerType)
Users_date_joined: Property = Property(name="date_joined", type=DateType)
Users.attributes={Users_average_star, Users_date_joined, Users_review_count, Users_name, Users_ID}

# Domain Model
domain_model = DomainModel(
    name="ae9efbbf_70d1_4a97_9679_eef8f69c6152",
    types={Places, Reviews, Users},
    associations={},
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