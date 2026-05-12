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
LOGIN = Class(name="LOGIN")
void = Class(name="void")
User = Class(name="User")
Admin = Class(name="Admin")
Catering = Class(name="Catering")
Decoration = Class(name="Decoration")
Hall = Class(name="Hall")
View_and_update = Class(name="View_and_update")
Catering_book = Class(name="Catering_book")
Decoration_book = Class(name="Decoration_book")
View_and_place_order = Class(name="View_and_place_order")
Hall_book = Class(name="Hall_book")

# LOGIN class attributes and methods
LOGIN_f_Name: Property = Property(name="f_Name", type=StringType)
LOGIN_l_Name: Property = Property(name="l_Name", type=StringType)
LOGIN_user_Name: Property = Property(name="user_Name", type=StringType)
LOGIN_password: Property = Property(name="password", type=StringType)
LOGIN.attributes={LOGIN_password, LOGIN_user_Name, LOGIN_f_Name, LOGIN_l_Name}

# void class attributes and methods

# User class attributes and methods
User_userID: Property = Property(name="userID", type=IntegerType)
User_userName: Property = Property(name="userName", type=StringType)
User_password: Property = Property(name="password", type=StringType)
User.attributes={User_password, User_userName, User_userID}

# Admin class attributes and methods
Admin_userID: Property = Property(name="userID", type=IntegerType)
Admin_userName: Property = Property(name="userName", type=StringType)
Admin_password: Property = Property(name="password", type=StringType)
Admin.attributes={Admin_userID, Admin_userName, Admin_password}

# Catering class attributes and methods
Catering_get_menu: Property = Property(name="get_menu", type=StringType)
Catering_get_cost: Property = Property(name="get_cost", type=StringType)
Catering.attributes={Catering_get_cost, Catering_get_menu}

# Decoration class attributes and methods
Decoration_Decor_type: Property = Property(name="Decor_type", type=Decoration)
Decoration_cost: Property = Property(name="cost", type=StringType)
Decoration_Square_feet: Property = Property(name="Square_feet", type=StringType)
Decoration.attributes={Decoration_cost, Decoration_Square_feet, Decoration_Decor_type}

# Hall class attributes and methods
Hall_get_hall_no: Property = Property(name="get_hall_no", type=StringType)
Hall_get_room_type: Property = Property(name="get_room_type", type=StringType)
Hall_cost_per_day: Property = Property(name="cost_per_day", type=StringType)
Hall.attributes={Hall_cost_per_day, Hall_get_hall_no, Hall_get_room_type}

# View_and_update class attributes and methods
View_and_update_order_view: Property = Property(name="order_view", type=Admin)
View_and_update_update_order: Property = Property(name="update_order", type=Admin)
View_and_update.attributes={View_and_update_update_order, View_and_update_order_view}

# Catering_book class attributes and methods
Catering_book_get_menu: Property = Property(name="get_menu", type=StringType)
Catering_book_get_cost: Property = Property(name="get_cost", type=StringType)
Catering_book.attributes={Catering_book_get_menu, Catering_book_get_cost}

# Decoration_book class attributes and methods
Decoration_book_Decor_type: Property = Property(name="Decor_type", type=Decoration_book)
Decoration_book_cost: Property = Property(name="cost", type=StringType)
Decoration_book_Square_feet: Property = Property(name="Square_feet", type=StringType)
Decoration_book.attributes={Decoration_book_cost, Decoration_book_Decor_type, Decoration_book_Square_feet}

# View_and_place_order class attributes and methods
View_and_place_order_order_view: Property = Property(name="order_view", type=User)
View_and_place_order_place_order: Property = Property(name="place_order", type=User)
View_and_place_order.attributes={View_and_place_order_place_order, View_and_place_order_order_view}

# Hall_book class attributes and methods
Hall_book_get_hall_no: Property = Property(name="get_hall_no", type=StringType)
Hall_book_get_room_type: Property = Property(name="get_room_type", type=StringType)
Hall_book_cost_per_day: Property = Property(name="cost_per_day", type=StringType)
Hall_book.attributes={Hall_book_get_room_type, Hall_book_cost_per_day, Hall_book_get_hall_no}

# Domain Model
domain_model = DomainModel(
    name="e989bbf3_71af_4d1c_80a6_384fb449da92",
    types={LOGIN, void, User, Admin, Catering, Decoration, Hall, View_and_update, Catering_book, Decoration_book, View_and_place_order, Hall_book},
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