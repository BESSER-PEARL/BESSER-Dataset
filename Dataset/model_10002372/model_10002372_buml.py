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
User = Class(name="User")
Profile_Page = Class(name="Profile_Page")
Return = Class(name="Return")
Browse_Recipes = Class(name="Browse_Recipes")
Vegetarian = Class(name="Vegetarian")
Drinks = Class(name="Drinks")
Visitor_Comment = Class(name="Visitor_Comment")
Social_Media = Class(name="Social_Media")
Bio_Info = Class(name="Bio_Info")
Login = Class(name="Login")
Main_Course = Class(name="Main_Course")
Dessert = Class(name="Dessert")

# User class attributes and methods
User_name: Property = Property(name="name", type=StringType)
User.attributes={User_name}

# Profile_Page class attributes and methods
Profile_Page_username: Property = Property(name="username", type=StringType)
Profile_Page_password: Property = Property(name="password", type=StringType)
Profile_Page.attributes={Profile_Page_password, Profile_Page_username}

# Return class attributes and methods

# Browse_Recipes class attributes and methods
Browse_Recipes_name: Property = Property(name="name", type=StringType)
Browse_Recipes_description: Property = Property(name="description", type=StringType)
Browse_Recipes.attributes={Browse_Recipes_name, Browse_Recipes_description}

# Vegetarian class attributes and methods
Vegetarian_name: Property = Property(name="name", type=StringType)
Vegetarian.attributes={Vegetarian_name}

# Drinks class attributes and methods
Drinks_name: Property = Property(name="name", type=StringType)
Drinks.attributes={Drinks_name}

# Visitor_Comment class attributes and methods

# Social_Media class attributes and methods
Social_Media_name: Property = Property(name="name", type=StringType)
Social_Media.attributes={Social_Media_name}

# Bio_Info class attributes and methods
Bio_Info_name: Property = Property(name="name", type=StringType)
Bio_Info_age: Property = Property(name="age", type=StringType)
Bio_Info_favourite_cuisine: Property = Property(name="favourite_cuisine", type=StringType)
Bio_Info_average_ratings: Property = Property(name="average_ratings", type=IntegerType)
Bio_Info.attributes={Bio_Info_name, Bio_Info_average_ratings, Bio_Info_favourite_cuisine, Bio_Info_age}

# Login class attributes and methods
Login_username: Property = Property(name="username", type=StringType)
Login_password: Property = Property(name="password", type=StringType)
Login.attributes={Login_username, Login_password}

# Main_Course class attributes and methods
Main_Course_name: Property = Property(name="name", type=StringType)
Main_Course.attributes={Main_Course_name}

# Dessert class attributes and methods
Dessert_name: Property = Property(name="name", type=StringType)
Dessert.attributes={Dessert_name}

# Relationships
User_Myprofile: BinaryAssociation = BinaryAssociation(
    name="User_Myprofile",
    ends={
        Property(name="myprofile0", type=Profile_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="user1", type=User, multiplicity=Multiplicity(1, 1))
    }
)
User_Post: BinaryAssociation = BinaryAssociation(
    name="User_Post",
    ends={
        Property(name="post2", type=Return, multiplicity=Multiplicity(0, 9999)),
        Property(name="user3", type=User, multiplicity=Multiplicity(1, 1))
    }
)
User_Login: BinaryAssociation = BinaryAssociation(
    name="User_Login",
    ends={
        Property(name="login4", type=Login, multiplicity=Multiplicity(1, 1)),
        Property(name="user5", type=User, multiplicity=Multiplicity(1, 1))
    }
)
User_Group: BinaryAssociation = BinaryAssociation(
    name="User_Group",
    ends={
        Property(name="group6", type=Browse_Recipes, multiplicity=Multiplicity(0, 9999)),
        Property(name="user7", type=User, multiplicity=Multiplicity(1, 1))
    }
)
User_Friends: BinaryAssociation = BinaryAssociation(
    name="User_Friends",
    ends={
        Property(name="friends8", type=Visitor_Comment, multiplicity=Multiplicity(0, 9999)),
        Property(name="user9", type=User, multiplicity=Multiplicity(1, 1))
    }
)
User_Hashtag: BinaryAssociation = BinaryAssociation(
    name="User_Hashtag",
    ends={
        Property(name="hashtag10", type=Social_Media, multiplicity=Multiplicity(0, 9999)),
        Property(name="user11", type=User, multiplicity=Multiplicity(1, 1))
    }
)
User_Pages: BinaryAssociation = BinaryAssociation(
    name="User_Pages",
    ends={
        Property(name="pages12", type=Bio_Info, multiplicity=Multiplicity(0, 9999)),
        Property(name="user13", type=User, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="ac784093_ac9e_4c2a_a171_741f33328805",
    types={User, Profile_Page, Return, Browse_Recipes, Vegetarian, Drinks, Visitor_Comment, Social_Media, Bio_Info, Login, Main_Course, Dessert},
    associations={User_Myprofile, User_Post, User_Login, User_Group, User_Friends, User_Hashtag, User_Pages},
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