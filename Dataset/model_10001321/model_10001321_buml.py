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
person = Class(name="person")
login = Class(name="login")
view_item = Class(name="view_item")
book_a_ticket = Class(name="book_a_ticket")
cancle = Class(name="cancle")
pay = Class(name="pay")
user = Class(name="user")
driver = Class(name="driver")
admin = Class(name="admin")
user_register = Class(name="user_register")
submit_information = Class(name="submit_information")

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

# person class attributes and methods
person_username: Property = Property(name="username", type=StringType)
person_name: Property = Property(name="name", type=StringType)
person_phone: Property = Property(name="phone", type=StringType)
person_password: Property = Property(name="password", type=StringType)
person.attributes={person_username, person_phone, person_name, person_password}

# login class attributes and methods
login_password: Property = Property(name="password", type=StringType)
login_username: Property = Property(name="username", type=StringType)
login.attributes={login_username, login_password}

# view_item class attributes and methods

# book_a_ticket class attributes and methods

# cancle class attributes and methods

# pay class attributes and methods
pay_id: Property = Property(name="id", type=StringType)
pay.attributes={pay_id}

# user class attributes and methods

# driver class attributes and methods

# admin class attributes and methods

# user_register class attributes and methods

# submit_information class attributes and methods

# Relationships
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

# Domain Model
domain_model = DomainModel(
    name="__jn3gIyGEemq7_yOQcm9ow",
    types={user_Actor, guest_user_Actor, driver_Actor, admin_Actor, login_UseCase, enter_user_name_UseCase, view_item_UseCase, captcha_UseCase, browse_item_UseCase, search_item__UseCase, ticket_printing_UseCase, view_seat_UseCase, send_message_to_number_registered_UseCase, exciting_package_UseCase, book_a_ticket_UseCase, changing_seats_by_admin_UseCase, payment_UseCase, submit_information_UseCase, cancle_UseCase, cancle_with_driver_UseCase, return_the_money_to_the_customer_UseCase, logout_UseCase, remove_user_UseCase, driver_planing_UseCase, enter_password_UseCase, person, login, view_item, book_a_ticket, cancle, pay, user, driver, admin, user_register, submit_information},
    associations={user_login, guest_user_view_item, guest_user_submit_information, admin_login, driver_login},
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