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
guest_user2_Actor = Class(name="guest_user2_Actor")
admin2_Actor = Class(name="admin2_Actor")
view_item2_UseCase = Class(name="view_item2_UseCase")
login2_UseCase = Class(name="login2_UseCase")
logout2_UseCase = Class(name="logout2_UseCase")
submit_information2_UseCase = Class(name="submit_information2_UseCase")
remove_user2_UseCase = Class(name="remove_user2_UseCase")
cancle2_UseCase = Class(name="cancle2_UseCase")
book_a_ticket2_UseCase = Class(name="book_a_ticket2_UseCase")
captcha2_UseCase = Class(name="captcha2_UseCase")
enter_user_name2_UseCase = Class(name="enter_user_name2_UseCase")
browse_item2_UseCase = Class(name="browse_item2_UseCase")
search_item_2_UseCase = Class(name="search_item_2_UseCase")
view_seat2_UseCase = Class(name="view_seat2_UseCase")
exciting_package2_UseCase = Class(name="exciting_package2_UseCase")
enter_password2_UseCase = Class(name="enter_password2_UseCase")
cancle_with_driver2_UseCase = Class(name="cancle_with_driver2_UseCase")
driver_planing2_UseCase = Class(name="driver_planing2_UseCase")
changing_seats_by_admin2_UseCase = Class(name="changing_seats_by_admin2_UseCase")
payment2_UseCase = Class(name="payment2_UseCase")
return_the_money_to_the_customer2_UseCase = Class(name="return_the_money_to_the_customer2_UseCase")
ticket_printing2_UseCase = Class(name="ticket_printing2_UseCase")
send_message_to_number_registered2_UseCase = Class(name="send_message_to_number_registered2_UseCase")
user_Actor1 = Class(name="user_Actor1")
guest_user_Actor1 = Class(name="guest_user_Actor1")
admin_Actor1 = Class(name="admin_Actor1")
online_booking_of_bus_tickets_login_UseCase1 = Class(name="online_booking_of_bus_tickets_login_UseCase1")
online_booking_of_bus_tickets_remove_user_UseCase1 = Class(name="online_booking_of_bus_tickets_remove_user_UseCase1")
online_booking_of_bus_tickets_view_item_UseCase1 = Class(name="online_booking_of_bus_tickets_view_item_UseCase1")
online_booking_of_bus_tickets_submit_information_UseCase1 = Class(name="online_booking_of_bus_tickets_submit_information_UseCase1")
online_booking_of_bus_tickets_cancel_UseCase = Class(name="online_booking_of_bus_tickets_cancel_UseCase")
online_booking_of_bus_tickets_logout_UseCase1 = Class(name="online_booking_of_bus_tickets_logout_UseCase1")
online_booking_of_bus_tickets_driver_planing_UseCase1 = Class(name="online_booking_of_bus_tickets_driver_planing_UseCase1")
online_booking_of_bus_tickets_captcha_UseCase1 = Class(name="online_booking_of_bus_tickets_captcha_UseCase1")
online_booking_of_bus_tickets_enter_user_name_UseCase1 = Class(name="online_booking_of_bus_tickets_enter_user_name_UseCase1")
online_booking_of_bus_tickets_search_item__UseCase1 = Class(name="online_booking_of_bus_tickets_search_item__UseCase1")
online_booking_of_bus_tickets_view_seat_UseCase1 = Class(name="online_booking_of_bus_tickets_view_seat_UseCase1")
online_booking_of_bus_tickets_enter_password_UseCase1 = Class(name="online_booking_of_bus_tickets_enter_password_UseCase1")
online_booking_of_bus_tickets_browse_item_UseCase1 = Class(name="online_booking_of_bus_tickets_browse_item_UseCase1")
online_booking_of_bus_tickets_exciting_package_UseCase1 = Class(name="online_booking_of_bus_tickets_exciting_package_UseCase1")
online_booking_of_bus_tickets_book_a_ticket_UseCase1 = Class(name="online_booking_of_bus_tickets_book_a_ticket_UseCase1")
online_booking_of_bus_tickets_send_message_to_number_registered_UseCase1 = Class(name="online_booking_of_bus_tickets_send_message_to_number_registered_UseCase1")
online_booking_of_bus_tickets_changing_seats_by_admin_UseCase1 = Class(name="online_booking_of_bus_tickets_changing_seats_by_admin_UseCase1")
online_booking_of_bus_tickets_ticket_printing_UseCase1 = Class(name="online_booking_of_bus_tickets_ticket_printing_UseCase1")
online_booking_of_bus_tickets_payment_UseCase1 = Class(name="online_booking_of_bus_tickets_payment_UseCase1")
online_booking_of_bus_tickets_cancel_with_driver_UseCase = Class(name="online_booking_of_bus_tickets_cancel_with_driver_UseCase")
online_booking_of_bus_tickets_return_the_money_to_the_customer_UseCase1 = Class(name="online_booking_of_bus_tickets_return_the_money_to_the_customer_UseCase1")
user_Actor2 = Class(name="user_Actor2")
driver_Actor1 = Class(name="driver_Actor1")
guest_user_Actor2 = Class(name="guest_user_Actor2")
admin_Actor2 = Class(name="admin_Actor2")
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
Userguest = Class(name="Userguest")
Submit_information = Class(name="Submit_information")
Cancle = Class(name="Cancle")
online_booking_of_bus_tickets_view_item_UseCase = Class(name="online_booking_of_bus_tickets_view_item_UseCase")
online_booking_of_bus_tickets_login_UseCase = Class(name="online_booking_of_bus_tickets_login_UseCase")
online_booking_of_bus_tickets_logout_UseCase = Class(name="online_booking_of_bus_tickets_logout_UseCase")
online_booking_of_bus_tickets_submit_information_UseCase = Class(name="online_booking_of_bus_tickets_submit_information_UseCase")
online_booking_of_bus_tickets_remove_user_UseCase = Class(name="online_booking_of_bus_tickets_remove_user_UseCase")
online_booking_of_bus_tickets_cancle_UseCase = Class(name="online_booking_of_bus_tickets_cancle_UseCase")
online_booking_of_bus_tickets_book_a_ticket_UseCase = Class(name="online_booking_of_bus_tickets_book_a_ticket_UseCase")
online_booking_of_bus_tickets_captcha_UseCase = Class(name="online_booking_of_bus_tickets_captcha_UseCase")
online_booking_of_bus_tickets_enter_user_name_UseCase = Class(name="online_booking_of_bus_tickets_enter_user_name_UseCase")
online_booking_of_bus_tickets_browse_item_UseCase = Class(name="online_booking_of_bus_tickets_browse_item_UseCase")
online_booking_of_bus_tickets_search_item__UseCase = Class(name="online_booking_of_bus_tickets_search_item__UseCase")
online_booking_of_bus_tickets_view_seat_UseCase = Class(name="online_booking_of_bus_tickets_view_seat_UseCase")
online_booking_of_bus_tickets_exciting_package_UseCase = Class(name="online_booking_of_bus_tickets_exciting_package_UseCase")
online_booking_of_bus_tickets_enter_password_UseCase = Class(name="online_booking_of_bus_tickets_enter_password_UseCase")
online_booking_of_bus_tickets_cancle_with_driver_UseCase = Class(name="online_booking_of_bus_tickets_cancle_with_driver_UseCase")
online_booking_of_bus_tickets_driver_planing_UseCase = Class(name="online_booking_of_bus_tickets_driver_planing_UseCase")
online_booking_of_bus_tickets_changing_seats_by_admin_UseCase = Class(name="online_booking_of_bus_tickets_changing_seats_by_admin_UseCase")
online_booking_of_bus_tickets_payment_UseCase = Class(name="online_booking_of_bus_tickets_payment_UseCase")
online_booking_of_bus_tickets_return_the_money_to_the_customer_UseCase = Class(name="online_booking_of_bus_tickets_return_the_money_to_the_customer_UseCase")
online_booking_of_bus_tickets_ticket_printing_UseCase = Class(name="online_booking_of_bus_tickets_ticket_printing_UseCase")
online_booking_of_bus_tickets_send_message_to_number_registered_UseCase = Class(name="online_booking_of_bus_tickets_send_message_to_number_registered_UseCase")
user2_Actor = Class(name="user2_Actor")

# guest_user2_Actor class attributes and methods

# admin2_Actor class attributes and methods

# view_item2_UseCase class attributes and methods

# login2_UseCase class attributes and methods

# logout2_UseCase class attributes and methods

# submit_information2_UseCase class attributes and methods

# remove_user2_UseCase class attributes and methods

# cancle2_UseCase class attributes and methods

# book_a_ticket2_UseCase class attributes and methods

# captcha2_UseCase class attributes and methods

# enter_user_name2_UseCase class attributes and methods

# browse_item2_UseCase class attributes and methods

# search_item_2_UseCase class attributes and methods

# view_seat2_UseCase class attributes and methods

# exciting_package2_UseCase class attributes and methods

# enter_password2_UseCase class attributes and methods

# cancle_with_driver2_UseCase class attributes and methods

# driver_planing2_UseCase class attributes and methods

# changing_seats_by_admin2_UseCase class attributes and methods

# payment2_UseCase class attributes and methods

# return_the_money_to_the_customer2_UseCase class attributes and methods

# ticket_printing2_UseCase class attributes and methods

# send_message_to_number_registered2_UseCase class attributes and methods

# user_Actor1 class attributes and methods

# guest_user_Actor1 class attributes and methods

# admin_Actor1 class attributes and methods

# online_booking_of_bus_tickets_login_UseCase1 class attributes and methods

# online_booking_of_bus_tickets_remove_user_UseCase1 class attributes and methods

# online_booking_of_bus_tickets_view_item_UseCase1 class attributes and methods

# online_booking_of_bus_tickets_submit_information_UseCase1 class attributes and methods

# online_booking_of_bus_tickets_cancel_UseCase class attributes and methods

# online_booking_of_bus_tickets_logout_UseCase1 class attributes and methods

# online_booking_of_bus_tickets_driver_planing_UseCase1 class attributes and methods

# online_booking_of_bus_tickets_captcha_UseCase1 class attributes and methods

# online_booking_of_bus_tickets_enter_user_name_UseCase1 class attributes and methods

# online_booking_of_bus_tickets_search_item__UseCase1 class attributes and methods

# online_booking_of_bus_tickets_view_seat_UseCase1 class attributes and methods

# online_booking_of_bus_tickets_enter_password_UseCase1 class attributes and methods

# online_booking_of_bus_tickets_browse_item_UseCase1 class attributes and methods

# online_booking_of_bus_tickets_exciting_package_UseCase1 class attributes and methods

# online_booking_of_bus_tickets_book_a_ticket_UseCase1 class attributes and methods

# online_booking_of_bus_tickets_send_message_to_number_registered_UseCase1 class attributes and methods

# online_booking_of_bus_tickets_changing_seats_by_admin_UseCase1 class attributes and methods

# online_booking_of_bus_tickets_ticket_printing_UseCase1 class attributes and methods

# online_booking_of_bus_tickets_payment_UseCase1 class attributes and methods

# online_booking_of_bus_tickets_cancel_with_driver_UseCase class attributes and methods

# online_booking_of_bus_tickets_return_the_money_to_the_customer_UseCase1 class attributes and methods

# user_Actor2 class attributes and methods

# driver_Actor1 class attributes and methods

# guest_user_Actor2 class attributes and methods

# admin_Actor2 class attributes and methods

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
Person.attributes={Person_phone_, Person_password_, Person_name_, Person_id_}

# Driver class attributes and methods

# Admin class attributes and methods

# User class attributes and methods

# Login class attributes and methods
Login_password_: Property = Property(name="password_", type=StringType)
Login_username_: Property = Property(name="username_", type=StringType)
Login.attributes={Login_password_, Login_username_}

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
Book_a_ticek.attributes={Book_a_ticek_starting_city_, Book_a_ticek_destination_city, Book_a_ticek_date_, Book_a_ticek_time_, Book_a_ticek_ticket_id_}

# Userguest class attributes and methods

# Submit_information class attributes and methods
Submit_information_name_: Property = Property(name="name_", type=StringType)
Submit_information_phone_: Property = Property(name="phone_", type=StringType)
Submit_information_password_: Property = Property(name="password_", type=StringType)
Submit_information_username: Property = Property(name="username", type=StringType)
Submit_information.attributes={Submit_information_username, Submit_information_name_, Submit_information_password_, Submit_information_phone_}

# Cancle class attributes and methods
Cancle_ticket_id_: Property = Property(name="ticket_id_", type=StringType)
Cancle_user_id_: Property = Property(name="user_id_", type=StringType)
Cancle.attributes={Cancle_ticket_id_, Cancle_user_id_}

# online_booking_of_bus_tickets_view_item_UseCase class attributes and methods

# online_booking_of_bus_tickets_login_UseCase class attributes and methods

# online_booking_of_bus_tickets_logout_UseCase class attributes and methods

# online_booking_of_bus_tickets_submit_information_UseCase class attributes and methods

# online_booking_of_bus_tickets_remove_user_UseCase class attributes and methods

# online_booking_of_bus_tickets_cancle_UseCase class attributes and methods

# online_booking_of_bus_tickets_book_a_ticket_UseCase class attributes and methods

# online_booking_of_bus_tickets_captcha_UseCase class attributes and methods

# online_booking_of_bus_tickets_enter_user_name_UseCase class attributes and methods

# online_booking_of_bus_tickets_browse_item_UseCase class attributes and methods

# online_booking_of_bus_tickets_search_item__UseCase class attributes and methods

# online_booking_of_bus_tickets_view_seat_UseCase class attributes and methods

# online_booking_of_bus_tickets_exciting_package_UseCase class attributes and methods

# online_booking_of_bus_tickets_enter_password_UseCase class attributes and methods

# online_booking_of_bus_tickets_cancle_with_driver_UseCase class attributes and methods

# online_booking_of_bus_tickets_driver_planing_UseCase class attributes and methods

# online_booking_of_bus_tickets_changing_seats_by_admin_UseCase class attributes and methods

# online_booking_of_bus_tickets_payment_UseCase class attributes and methods

# online_booking_of_bus_tickets_return_the_money_to_the_customer_UseCase class attributes and methods

# online_booking_of_bus_tickets_ticket_printing_UseCase class attributes and methods

# online_booking_of_bus_tickets_send_message_to_number_registered_UseCase class attributes and methods

# user2_Actor class attributes and methods

# Relationships
driver_logout: BinaryAssociation = BinaryAssociation(
    name="driver_logout",
    ends={
        Property(name="logout26", type=logout_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="driver27", type=driver_Actor, multiplicity=Multiplicity(0, 1))
    }
)
user_logout2: BinaryAssociation = BinaryAssociation(
    name="user_logout2",
    ends={
        Property(name="logout28", type=logout2_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user29", type=user2_Actor, multiplicity=Multiplicity(0, 1))
    }
)
user_login2: BinaryAssociation = BinaryAssociation(
    name="user_login2",
    ends={
        Property(name="login30", type=login2_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user31", type=user2_Actor, multiplicity=Multiplicity(0, 1))
    }
)
guest_user_view_item2: BinaryAssociation = BinaryAssociation(
    name="guest_user_view_item2",
    ends={
        Property(name="view_item32", type=view_item2_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="guest_user33", type=guest_user2_Actor, multiplicity=Multiplicity(0, 1))
    }
)
guest_user_submit_information2: BinaryAssociation = BinaryAssociation(
    name="guest_user_submit_information2",
    ends={
        Property(name="submit_information34", type=submit_information2_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="guest_user35", type=guest_user2_Actor, multiplicity=Multiplicity(0, 1))
    }
)
admin_login2: BinaryAssociation = BinaryAssociation(
    name="admin_login2",
    ends={
        Property(name="login36", type=login2_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin37", type=admin2_Actor, multiplicity=Multiplicity(0, 1))
    }
)
user_logout1: BinaryAssociation = BinaryAssociation(
    name="user_logout1",
    ends={
        Property(name="logout38", type=online_booking_of_bus_tickets_logout_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user39", type=user_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
user_login1: BinaryAssociation = BinaryAssociation(
    name="user_login1",
    ends={
        Property(name="login40", type=online_booking_of_bus_tickets_login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user41", type=user_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
guest_user_view_item1: BinaryAssociation = BinaryAssociation(
    name="guest_user_view_item1",
    ends={
        Property(name="view_item42", type=online_booking_of_bus_tickets_view_item_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="guest_user43", type=guest_user_Actor1, multiplicity=Multiplicity(0, 1))
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
user_logout: BinaryAssociation = BinaryAssociation(
    name="user_logout",
    ends={
        Property(name="logout24", type=logout_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user25", type=user_Actor, multiplicity=Multiplicity(0, 1))
    }
)
guest_user_submit_information1: BinaryAssociation = BinaryAssociation(
    name="guest_user_submit_information1",
    ends={
        Property(name="submit_information44", type=online_booking_of_bus_tickets_submit_information_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="guest_user45", type=guest_user_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
admin_login1: BinaryAssociation = BinaryAssociation(
    name="admin_login1",
    ends={
        Property(name="login46", type=online_booking_of_bus_tickets_login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin47", type=admin_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
user_login3: BinaryAssociation = BinaryAssociation(
    name="user_login3",
    ends={
        Property(name="login48", type=online_booking_of_bus_tickets_login_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="user49", type=user_Actor2, multiplicity=Multiplicity(0, 1))
    }
)
driver_login2: BinaryAssociation = BinaryAssociation(
    name="driver_login2",
    ends={
        Property(name="login50", type=online_booking_of_bus_tickets_login_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="driver51", type=driver_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
admin_login3: BinaryAssociation = BinaryAssociation(
    name="admin_login3",
    ends={
        Property(name="login52", type=online_booking_of_bus_tickets_login_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="admin53", type=admin_Actor2, multiplicity=Multiplicity(0, 1))
    }
)
user_logout3: BinaryAssociation = BinaryAssociation(
    name="user_logout3",
    ends={
        Property(name="logout54", type=online_booking_of_bus_tickets_logout_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="user55", type=user_Actor2, multiplicity=Multiplicity(0, 1))
    }
)
driver_logout2: BinaryAssociation = BinaryAssociation(
    name="driver_logout2",
    ends={
        Property(name="logout56", type=online_booking_of_bus_tickets_logout_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="driver57", type=driver_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
guest_user_view_item3: BinaryAssociation = BinaryAssociation(
    name="guest_user_view_item3",
    ends={
        Property(name="view_item58", type=online_booking_of_bus_tickets_view_item_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="guest_user59", type=guest_user_Actor2, multiplicity=Multiplicity(0, 1))
    }
)
guest_user_submit_information3: BinaryAssociation = BinaryAssociation(
    name="guest_user_submit_information3",
    ends={
        Property(name="submit_information60", type=online_booking_of_bus_tickets_submit_information_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="guest_user61", type=guest_user_Actor2, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_21dc1a19_77da_4bec_a72a_c5e20fbef990",
    types={guest_user2_Actor, admin2_Actor, view_item2_UseCase, login2_UseCase, logout2_UseCase, submit_information2_UseCase, remove_user2_UseCase, cancle2_UseCase, book_a_ticket2_UseCase, captcha2_UseCase, enter_user_name2_UseCase, browse_item2_UseCase, search_item_2_UseCase, view_seat2_UseCase, exciting_package2_UseCase, enter_password2_UseCase, cancle_with_driver2_UseCase, driver_planing2_UseCase, changing_seats_by_admin2_UseCase, payment2_UseCase, return_the_money_to_the_customer2_UseCase, ticket_printing2_UseCase, send_message_to_number_registered2_UseCase, user_Actor1, guest_user_Actor1, admin_Actor1, online_booking_of_bus_tickets_login_UseCase1, online_booking_of_bus_tickets_remove_user_UseCase1, online_booking_of_bus_tickets_view_item_UseCase1, online_booking_of_bus_tickets_submit_information_UseCase1, online_booking_of_bus_tickets_cancel_UseCase, online_booking_of_bus_tickets_logout_UseCase1, online_booking_of_bus_tickets_driver_planing_UseCase1, online_booking_of_bus_tickets_captcha_UseCase1, online_booking_of_bus_tickets_enter_user_name_UseCase1, online_booking_of_bus_tickets_search_item__UseCase1, online_booking_of_bus_tickets_view_seat_UseCase1, online_booking_of_bus_tickets_enter_password_UseCase1, online_booking_of_bus_tickets_browse_item_UseCase1, online_booking_of_bus_tickets_exciting_package_UseCase1, online_booking_of_bus_tickets_book_a_ticket_UseCase1, online_booking_of_bus_tickets_send_message_to_number_registered_UseCase1, online_booking_of_bus_tickets_changing_seats_by_admin_UseCase1, online_booking_of_bus_tickets_ticket_printing_UseCase1, online_booking_of_bus_tickets_payment_UseCase1, online_booking_of_bus_tickets_cancel_with_driver_UseCase, online_booking_of_bus_tickets_return_the_money_to_the_customer_UseCase1, user_Actor2, driver_Actor1, guest_user_Actor2, admin_Actor2, user_Actor, guest_user_Actor, driver_Actor, admin_Actor, login_UseCase, enter_user_name_UseCase, view_item_UseCase, captcha_UseCase, browse_item_UseCase, search_item__UseCase, ticket_printing_UseCase, view_seat_UseCase, send_message_to_number_registered_UseCase, exciting_package_UseCase, book_a_ticket_UseCase, changing_seats_by_admin_UseCase, payment_UseCase, submit_information_UseCase, cancle_UseCase, cancle_with_driver_UseCase, return_the_money_to_the_customer_UseCase, logout_UseCase, remove_user_UseCase, driver_planing_UseCase, enter_password_UseCase, Person, Driver, Admin, User, Login, view_item, Pay, Book_a_ticek, Userguest, Submit_information, Cancle, online_booking_of_bus_tickets_view_item_UseCase, online_booking_of_bus_tickets_login_UseCase, online_booking_of_bus_tickets_logout_UseCase, online_booking_of_bus_tickets_submit_information_UseCase, online_booking_of_bus_tickets_remove_user_UseCase, online_booking_of_bus_tickets_cancle_UseCase, online_booking_of_bus_tickets_book_a_ticket_UseCase, online_booking_of_bus_tickets_captcha_UseCase, online_booking_of_bus_tickets_enter_user_name_UseCase, online_booking_of_bus_tickets_browse_item_UseCase, online_booking_of_bus_tickets_search_item__UseCase, online_booking_of_bus_tickets_view_seat_UseCase, online_booking_of_bus_tickets_exciting_package_UseCase, online_booking_of_bus_tickets_enter_password_UseCase, online_booking_of_bus_tickets_cancle_with_driver_UseCase, online_booking_of_bus_tickets_driver_planing_UseCase, online_booking_of_bus_tickets_changing_seats_by_admin_UseCase, online_booking_of_bus_tickets_payment_UseCase, online_booking_of_bus_tickets_return_the_money_to_the_customer_UseCase, online_booking_of_bus_tickets_ticket_printing_UseCase, online_booking_of_bus_tickets_send_message_to_number_registered_UseCase, user2_Actor},
    associations={driver_logout, user_logout2, user_login2, guest_user_view_item2, guest_user_submit_information2, admin_login2, user_logout1, user_login1, guest_user_view_item1, user_login, guest_user_view_item, guest_user_submit_information, admin_login, driver_login, Person_Login, Book_a_ticek_Pay, Book_a_ticek_Cancle, Submit_information_Userguest, Userguest_view_item, Login_view_item, Driver_User, user_logout, guest_user_submit_information1, admin_login1, user_login3, driver_login2, admin_login3, user_logout3, driver_logout2, guest_user_view_item3, guest_user_submit_information3},
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