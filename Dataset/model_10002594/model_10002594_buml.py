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
Enumeration_: Enumeration = Enumeration(
    name="Enumeration",
    literals={
            
    }
)

# Classes
LibraryController = Class(name="LibraryController")
LibraryGui = Class(name="LibraryGui")
Library = Class(name="Library")
Book = Class(name="Book")
User_Actor = Class(name="User_Actor")
Login_UseCase = Class(name="Login_UseCase")
Sign_up_UseCase = Class(name="Sign_up_UseCase")
Home_Page_UseCase = Class(name="Home_Page_UseCase")
Categorize_apps_as_productive___Social_UseCase = Class(name="Categorize_apps_as_productive___Social_UseCase")
View_points_scored_UseCase = Class(name="View_points_scored_UseCase")
View_time_spent_on_each_app_UseCase = Class(name="View_time_spent_on_each_app_UseCase")
view_the_count_each_app_has_been_opened_UseCase = Class(name="view_the_count_each_app_has_been_opened_UseCase")
Settings_UseCase = Class(name="Settings_UseCase")
Manage_Tracking_UseCase = Class(name="Manage_Tracking_UseCase")
Manage_Notifications_UseCase = Class(name="Manage_Notifications_UseCase")
Change_Password_UseCase = Class(name="Change_Password_UseCase")
Login = Class(name="Login")

# LibraryController class attributes and methods
LibraryController_libraryDataAcces: Property = Property(name="libraryDataAcces", type=StringType)
LibraryController.attributes={LibraryController_libraryDataAcces}

# LibraryGui class attributes and methods
LibraryGui_library: Property = Property(name="library", type=Library)
LibraryGui_libraryController: Property = Property(name="libraryController", type=LibraryController)
LibraryGui.attributes={LibraryGui_libraryController, LibraryGui_library}

# Library class attributes and methods
Library_count: Property = Property(name="count", type=IntegerType)
Library_file: Property = Property(name="file", type=StringType)
Library_changeSinceLastSave: Property = Property(name="changeSinceLastSave", type=BooleanType)
Library_collection: Property = Property(name="collection", type=StringType)
Library.attributes={Library_file, Library_count, Library_changeSinceLastSave, Library_collection}

# Book class attributes and methods
Book_Author: Property = Property(name="Author", type=StringType)
Book_title: Property = Property(name="title", type=StringType)
Book_publisherCity: Property = Property(name="publisherCity", type=StringType)
Book_yearPublished: Property = Property(name="yearPublished", type=IntegerType)
Book_publisher: Property = Property(name="publisher", type=StringType)
Book.attributes={Book_publisherCity, Book_Author, Book_title, Book_yearPublished, Book_publisher}

# User_Actor class attributes and methods

# Login_UseCase class attributes and methods

# Sign_up_UseCase class attributes and methods

# Home_Page_UseCase class attributes and methods

# Categorize_apps_as_productive___Social_UseCase class attributes and methods

# View_points_scored_UseCase class attributes and methods

# View_time_spent_on_each_app_UseCase class attributes and methods

# view_the_count_each_app_has_been_opened_UseCase class attributes and methods

# Settings_UseCase class attributes and methods

# Manage_Tracking_UseCase class attributes and methods

# Manage_Notifications_UseCase class attributes and methods

# Change_Password_UseCase class attributes and methods

# Login class attributes and methods
Login_username: Property = Property(name="username", type=StringType)
Login__attr: Property = Property(name="_attr", type=StringType)
Login.attributes={Login_username, Login__attr}

# Relationships
LibraryGui_LibraryController: BinaryAssociation = BinaryAssociation(
    name="LibraryGui_LibraryController",
    ends={
        Property(name="LibraryGui_LibraryController_00", type=LibraryController, multiplicity=Multiplicity(1, 1)),
        Property(name="LibraryGui_LibraryController_11", type=LibraryGui, multiplicity=Multiplicity(1, 1))
    }
)
Library_LibraryGui: BinaryAssociation = BinaryAssociation(
    name="Library_LibraryGui",
    ends={
        Property(name="libraryGui2", type=LibraryGui, multiplicity=Multiplicity(1, 1)),
        Property(name="library3", type=Library, multiplicity=Multiplicity(1, 1))
    }
)
Book_Library: BinaryAssociation = BinaryAssociation(
    name="Book_Library",
    ends={
        Property(name="Book_Library_04", type=Library, multiplicity=Multiplicity(1, 1)),
        Property(name="Book_Library_15", type=Book, multiplicity=Multiplicity(0, 9999))
    }
)
User_Login: BinaryAssociation = BinaryAssociation(
    name="User_Login",
    ends={
        Property(name="login6", type=Login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user7", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Sign_up: BinaryAssociation = BinaryAssociation(
    name="User_Sign_up",
    ends={
        Property(name="sign_up8", type=Sign_up_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user9", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Home_Page: BinaryAssociation = BinaryAssociation(
    name="User_Home_Page",
    ends={
        Property(name="home_Page10", type=Home_Page_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user11", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Home_Page_Categorize_apps_as_productive___Social: BinaryAssociation = BinaryAssociation(
    name="Home_Page_Categorize_apps_as_productive___Social",
    ends={
        Property(name="categorize_apps_as_productive___Social12", type=Categorize_apps_as_productive___Social_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="home_Page13", type=Home_Page_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Home_Page_View_points_scored: BinaryAssociation = BinaryAssociation(
    name="Home_Page_View_points_scored",
    ends={
        Property(name="view_points_scored14", type=View_points_scored_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="home_Page15", type=Home_Page_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Home_Page_View_time_spent_on_each_app: BinaryAssociation = BinaryAssociation(
    name="Home_Page_View_time_spent_on_each_app",
    ends={
        Property(name="view_time_spent_on_each_app16", type=View_time_spent_on_each_app_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="home_Page17", type=Home_Page_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Home_Page_view_the_count_each_app_has_been_opened: BinaryAssociation = BinaryAssociation(
    name="Home_Page_view_the_count_each_app_has_been_opened",
    ends={
        Property(name="view_the_count_each_app_has_been_opened18", type=view_the_count_each_app_has_been_opened_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="home_Page19", type=Home_Page_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Home_Page_Settings: BinaryAssociation = BinaryAssociation(
    name="Home_Page_Settings",
    ends={
        Property(name="settings20", type=Settings_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="home_Page21", type=Home_Page_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Settings_Manage_Tracking: BinaryAssociation = BinaryAssociation(
    name="Settings_Manage_Tracking",
    ends={
        Property(name="manage_Tracking22", type=Manage_Tracking_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="settings23", type=Settings_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Settings_Manage_Notifications: BinaryAssociation = BinaryAssociation(
    name="Settings_Manage_Notifications",
    ends={
        Property(name="manage_Notifications24", type=Manage_Notifications_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="settings25", type=Settings_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Settings_Change_Password: BinaryAssociation = BinaryAssociation(
    name="Settings_Change_Password",
    ends={
        Property(name="change_Password26", type=Change_Password_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="settings27", type=Settings_UseCase, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="c4e873fa_475e_45b5_bb9a_5df4c1c60578",
    types={LibraryController, LibraryGui, Library, Book, User_Actor, Login_UseCase, Sign_up_UseCase, Home_Page_UseCase, Categorize_apps_as_productive___Social_UseCase, View_points_scored_UseCase, View_time_spent_on_each_app_UseCase, view_the_count_each_app_has_been_opened_UseCase, Settings_UseCase, Manage_Tracking_UseCase, Manage_Notifications_UseCase, Change_Password_UseCase, Login, Enumeration_},
    associations={LibraryGui_LibraryController, Library_LibraryGui, Book_Library, User_Login, User_Sign_up, User_Home_Page, Home_Page_Categorize_apps_as_productive___Social, Home_Page_View_points_scored, Home_Page_View_time_spent_on_each_app, Home_Page_view_the_count_each_app_has_been_opened, Home_Page_Settings, Settings_Manage_Tracking, Settings_Manage_Notifications, Settings_Change_Password},
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