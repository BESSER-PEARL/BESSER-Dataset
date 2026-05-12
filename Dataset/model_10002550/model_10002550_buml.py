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
Userguest = Class(name="Userguest")
Submit_information = Class(name="Submit_information")
Cancle = Class(name="Cancle")
user_Actor = Class(name="user_Actor")
guest_user_Actor = Class(name="guest_user_Actor")
driver_Actor = Class(name="driver_Actor")
admin_Actor = Class(name="admin_Actor")
login_UseCase = Class(name="login_UseCase")
enter_user_name_UseCase = Class(name="enter_user_name_UseCase")
view_item_UseCase = Class(name="view_item_UseCase")
captcha_UseCase = Class(name="captcha_UseCase")
browse_item_UseCase = Class(name="browse_item_UseCase")
search_item__UseCase = Class(name="search_item__UseCase")
ticket_printing_UseCase = Class(name="ticket_printing_UseCase")
view_seat_UseCase = Class(name="view_seat_UseCase")
send_message_to_number_registered_UseCase = Class(name="send_message_to_number_registered_UseCase")
exciting_package_UseCase = Class(name="exciting_package_UseCase")
book_a_ticket_UseCase = Class(name="book_a_ticket_UseCase")
changing_seats_by_admin_UseCase = Class(name="changing_seats_by_admin_UseCase")
payment_UseCase = Class(name="payment_UseCase")
submit_information_UseCase = Class(name="submit_information_UseCase")
cancle_UseCase = Class(name="cancle_UseCase")
cancle_with_driver_UseCase = Class(name="cancle_with_driver_UseCase")
return_the_money_to_the_customer_UseCase = Class(name="return_the_money_to_the_customer_UseCase")
logout_UseCase = Class(name="logout_UseCase")
remove_user_UseCase = Class(name="remove_user_UseCase")
driver_planing_UseCase = Class(name="driver_planing_UseCase")
enter_password_UseCase = Class(name="enter_password_UseCase")
Person = Class(name="Person")
Driver = Class(name="Driver")
Admin = Class(name="Admin")
User = Class(name="User")
Login = Class(name="Login")
view_item = Class(name="view_item")
Pay = Class(name="Pay")
Book_a_ticek = Class(name="Book_a_ticek")

# Userguest class attributes and methods

# Submit_information class attributes and methods
Submit_information_name_: Property = Property(name="name_", type=StringType)
Submit_information_phone_: Property = Property(name="phone_", type=StringType)
Submit_information_password_: Property = Property(name="password_", type=StringType)
Submit_information_username: Property = Property(name="username", type=StringType)
Submit_information.attributes={Submit_information_password_, Submit_information_username, Submit_information_name_, Submit_information_phone_}

# Cancle class attributes and methods
Cancle_ticket_id_: Property = Property(name="ticket_id_", type=StringType)
Cancle_user_id_: Property = Property(name="user_id_", type=StringType)
Cancle.attributes={Cancle_user_id_, Cancle_ticket_id_}

# user_Actor class attributes and methods

# guest_user_Actor class attributes and methods

# driver_Actor class attributes and methods

# admin_Actor class attributes and methods

# login_UseCase class attributes and methods

# enter_user_name_UseCase class attributes and methods

# view_item_UseCase class attributes and methods

# captcha_UseCase class attributes and methods

# browse_item_UseCase class attributes and methods

# search_item__UseCase class attributes and methods

# ticket_printing_UseCase class attributes and methods

# view_seat_UseCase class attributes and methods

# send_message_to_number_registered_UseCase class attributes and methods

# exciting_package_UseCase class attributes and methods

# book_a_ticket_UseCase class attributes and methods

# changing_seats_by_admin_UseCase class attributes and methods

# payment_UseCase class attributes and methods

# submit_information_UseCase class attributes and methods

# cancle_UseCase class attributes and methods

# cancle_with_driver_UseCase class attributes and methods

# return_the_money_to_the_customer_UseCase class attributes and methods

# logout_UseCase class attributes and methods

# remove_user_UseCase class attributes and methods

# driver_planing_UseCase class attributes and methods

# enter_password_UseCase class attributes and methods

# Person class attributes and methods
Person_id_: Property = Property(name="id_", type=StringType)
Person_name_: Property = Property(name="name_", type=StringType)
Person_phone_: Property = Property(name="phone_", type=StringType)
Person_password_: Property = Property(name="password_", type=StringType)
Person.attributes={Person_name_, Person_id_, Person_phone_, Person_password_}

# Driver class attributes and methods

# Admin class attributes and methods

# User class attributes and methods

# Login class attributes and methods
Login_password_: Property = Property(name="password_", type=StringType)
Login_username_: Property = Property(name="username_", type=StringType)
Login.attributes={Login_username_, Login_password_}

# view_item class attributes and methods
view_item_ticket_id_: Property = Property(name="ticket_id_", type=StringType)
view_item.attributes={view_item_ticket_id_}

# Pay class attributes and methods
Pay_id_: Property = Property(name="id_", type=StringType)
Pay.attributes={Pay_id_}

# Book_a_ticek class attributes and methods
Book_a_ticek_date_: Property = Property(name="date_", type=StringType)
Book_a_ticek_starting_city_: Property = Property(name="starting_city_", type=StringType)
Book_a_ticek_destination_city: Property = Property(name="destination_city", type=StringType)
Book_a_ticek_time_: Property = Property(name="time_", type=StringType)
Book_a_ticek_ticket_id_: Property = Property(name="ticket_id_", type=StringType)
Book_a_ticek.attributes={Book_a_ticek_starting_city_, Book_a_ticek_date_, Book_a_ticek_time_, Book_a_ticek_ticket_id_, Book_a_ticek_destination_city}

# Relationships
Login_view_item: BinaryAssociation = BinaryAssociation(
    name="Login_view_item",
    ends={
        Property(name="view_item220", type=view_item, multiplicity=Multiplicity(0, 1)),
        Property(name="login21", type=Login, multiplicity=Multiplicity(0, 1))
    }
)
Driver_User: BinaryAssociation = BinaryAssociation(
    name="Driver_User",
    ends={
        Property(name="user22", type=User, multiplicity=Multiplicity(0, 1)),
        Property(name="driver23", type=Driver, multiplicity=Multiplicity(0, 1))
    }
)
user_login: BinaryAssociation = BinaryAssociation(
    name="user_login",
    ends={
        Property(name="login0", type=login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user1", type=user_Actor, multiplicity=Multiplicity(0, 1))
    }
)
guest_user_view_item: BinaryAssociation = BinaryAssociation(
    name="guest_user_view_item",
    ends={
        Property(name="view_item2", type=view_item_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="guest_user3", type=guest_user_Actor, multiplicity=Multiplicity(0, 1))
    }
)
guest_user_submit_information: BinaryAssociation = BinaryAssociation(
    name="guest_user_submit_information",
    ends={
        Property(name="submit_information4", type=submit_information_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="guest_user5", type=guest_user_Actor, multiplicity=Multiplicity(0, 1))
    }
)
admin_login: BinaryAssociation = BinaryAssociation(
    name="admin_login",
    ends={
        Property(name="login6", type=login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin7", type=admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
driver_login: BinaryAssociation = BinaryAssociation(
    name="driver_login",
    ends={
        Property(name="login8", type=login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="driver9", type=driver_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Person_Login: BinaryAssociation = BinaryAssociation(
    name="Person_Login",
    ends={
        Property(name="login10", type=Login, multiplicity=Multiplicity(0, 1)),
        Property(name="person11", type=Person, multiplicity=Multiplicity(0, 1))
    }
)
Book_a_ticek_Pay: BinaryAssociation = BinaryAssociation(
    name="Book_a_ticek_Pay",
    ends={
        Property(name="pay12", type=Pay, multiplicity=Multiplicity(0, 1)),
        Property(name="book_a_ticek13", type=Book_a_ticek, multiplicity=Multiplicity(0, 1))
    }
)
Book_a_ticek_Cancle: BinaryAssociation = BinaryAssociation(
    name="Book_a_ticek_Cancle",
    ends={
        Property(name="cancle14", type=Cancle, multiplicity=Multiplicity(0, 1)),
        Property(name="book_a_ticek15", type=Book_a_ticek, multiplicity=Multiplicity(0, 1))
    }
)
Submit_information_Userguest: BinaryAssociation = BinaryAssociation(
    name="Submit_information_Userguest",
    ends={
        Property(name="userguest16", type=Userguest, multiplicity=Multiplicity(0, 1)),
        Property(name="submit_information17", type=Submit_information, multiplicity=Multiplicity(0, 1))
    }
)
Userguest_view_item: BinaryAssociation = BinaryAssociation(
    name="Userguest_view_item",
    ends={
        Property(name="view_item18", type=view_item, multiplicity=Multiplicity(0, 1)),
        Property(name="userguest19", type=Userguest, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="c048477c_aa54_473d_9b08_2884b6cfc772",
    types={Userguest, Submit_information, Cancle, user_Actor, guest_user_Actor, driver_Actor, admin_Actor, login_UseCase, enter_user_name_UseCase, view_item_UseCase, captcha_UseCase, browse_item_UseCase, search_item__UseCase, ticket_printing_UseCase, view_seat_UseCase, send_message_to_number_registered_UseCase, exciting_package_UseCase, book_a_ticket_UseCase, changing_seats_by_admin_UseCase, payment_UseCase, submit_information_UseCase, cancle_UseCase, cancle_with_driver_UseCase, return_the_money_to_the_customer_UseCase, logout_UseCase, remove_user_UseCase, driver_planing_UseCase, enter_password_UseCase, Person, Driver, Admin, User, Login, view_item, Pay, Book_a_ticek},
    associations={Login_view_item, Driver_User, user_login, guest_user_view_item, guest_user_submit_information, admin_login, driver_login, Person_Login, Book_a_ticek_Pay, Book_a_ticek_Cancle, Submit_information_Userguest, Userguest_view_item},
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