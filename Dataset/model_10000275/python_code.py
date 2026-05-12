from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class guest_user2_Actor:

    pass


class user2_Actor:

    pass


class online_booking_of_bus_tickets_send_message_to_number_registered_UseCase:

    pass


class online_booking_of_bus_tickets_ticket_printing_UseCase:

    pass


class online_booking_of_bus_tickets_return_the_money_to_the_customer_UseCase:

    pass


class online_booking_of_bus_tickets_payment_UseCase:

    pass


class online_booking_of_bus_tickets_changing_seats_by_admin_UseCase:

    pass


class online_booking_of_bus_tickets_driver_planing_UseCase:

    pass


class online_booking_of_bus_tickets_cancle_with_driver_UseCase:

    pass


class online_booking_of_bus_tickets_enter_password_UseCase:

    pass


class online_booking_of_bus_tickets_exciting_package_UseCase:

    pass


class online_booking_of_bus_tickets_view_seat_UseCase:

    pass


class online_booking_of_bus_tickets_search_item__UseCase:

    pass


class online_booking_of_bus_tickets_browse_item_UseCase:

    pass


class online_booking_of_bus_tickets_enter_user_name_UseCase:

    pass


class online_booking_of_bus_tickets_captcha_UseCase:

    pass


class online_booking_of_bus_tickets_book_a_ticket_UseCase:

    pass


class online_booking_of_bus_tickets_cancle_UseCase:

    pass


class online_booking_of_bus_tickets_remove_user_UseCase:

    pass


class online_booking_of_bus_tickets_submit_information_UseCase:

    pass


class online_booking_of_bus_tickets_logout_UseCase:

    pass


class online_booking_of_bus_tickets_login_UseCase:

    pass


class online_booking_of_bus_tickets_view_item_UseCase:

    pass


class enter_password_UseCase:

    pass


class driver_planing_UseCase:

    pass


class remove_user_UseCase:

    pass


class logout_UseCase:

    pass


class return_the_money_to_the_customer_UseCase:

    pass


class cancle_with_driver_UseCase:

    pass


class cancle_UseCase:

    pass


class submit_information_UseCase:

    pass


class payment_UseCase:

    pass


class changing_seats_by_admin_UseCase:

    pass


class book_a_ticket_UseCase:

    pass


class exciting_package_UseCase:

    pass


class send_message_to_number_registered_UseCase:

    pass


class view_seat_UseCase:

    pass


class ticket_printing_UseCase:

    pass


class search_item__UseCase:

    pass


class browse_item_UseCase:

    pass


class captcha_UseCase:

    pass


class view_item_UseCase:

    pass


class enter_user_name_UseCase:

    pass


class login_UseCase:

    pass


class admin_Actor:

    pass


class driver_Actor:

    pass


class guest_user_Actor:

    pass


class user_Actor:

    pass


class online_booking_of_bus_tickets_cancel_with_driver_UseCase:

    pass


class online_booking_of_bus_tickets_cancel_UseCase:

    pass


class send_message_to_number_registered2_UseCase:

    pass


class ticket_printing2_UseCase:

    pass


class return_the_money_to_the_customer2_UseCase:

    pass


class payment2_UseCase:

    pass


class changing_seats_by_admin2_UseCase:

    pass


class driver_planing2_UseCase:

    pass


class cancle_with_driver2_UseCase:

    pass


class enter_password2_UseCase:

    pass


class exciting_package2_UseCase:

    pass


class view_seat2_UseCase:

    pass


class search_item_2_UseCase:

    pass


class browse_item2_UseCase:

    pass


class enter_user_name2_UseCase:

    pass


class captcha2_UseCase:

    pass


class book_a_ticket2_UseCase:

    pass


class cancle2_UseCase:

    pass


class remove_user2_UseCase:

    pass


class submit_information2_UseCase:

    pass


class logout2_UseCase:

    pass


class login2_UseCase:

    pass


class view_item2_UseCase:

    pass


class admin2_Actor:

    pass





class Cancle:

    def __init__(self, ticket_id_: str, user_id_: str, book_a_ticek15: "Book_a_ticek" = None):
        self.ticket_id_ = ticket_id_
        self.user_id_ = user_id_
        self.book_a_ticek15 = book_a_ticek15
        
        pass
    @property
    def ticket_id_(self):
        return self.__ticket_id_
    @ticket_id_.setter
    def ticket_id_(self, ticket_id_: str):
        self.__ticket_id_ = ticket_id_

    @property
    def user_id_(self):
        return self.__user_id_
    @user_id_.setter
    def user_id_(self, user_id_: str):
        self.__user_id_ = user_id_

    @property
    def book_a_ticek15(self):
        return self.__book_a_ticek15
    @book_a_ticek15.setter
    def book_a_ticek15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cancle__book_a_ticek15", None)
        self.__book_a_ticek15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cancle14"):
                opp_val = getattr(old_value, "cancle14", None)
                if opp_val == self:
                    setattr(old_value, "cancle14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cancle14"):
                opp_val = getattr(value, "cancle14", None)
                setattr(value, "cancle14", self)



class Submit_information:

    def __init__(self, name_: str, phone_: str, password_: str, username: str, userguest16: "Userguest" = None):
        self.name_ = name_
        self.phone_ = phone_
        self.password_ = password_
        self.username = username
        self.userguest16 = userguest16
        
        pass
    @property
    def name_(self):
        return self.__name_
    @name_.setter
    def name_(self, name_: str):
        self.__name_ = name_

    @property
    def phone_(self):
        return self.__phone_
    @phone_.setter
    def phone_(self, phone_: str):
        self.__phone_ = phone_

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def password_(self):
        return self.__password_
    @password_.setter
    def password_(self, password_: str):
        self.__password_ = password_

    @property
    def userguest16(self):
        return self.__userguest16
    @userguest16.setter
    def userguest16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Submit_information__userguest16", None)
        self.__userguest16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "submit_information17"):
                opp_val = getattr(old_value, "submit_information17", None)
                if opp_val == self:
                    setattr(old_value, "submit_information17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "submit_information17"):
                opp_val = getattr(value, "submit_information17", None)
                setattr(value, "submit_information17", self)



class Userguest:

    pass


class Book_a_ticek:

    def __init__(self, date_: str, starting_city_: str, destination_city: str, time_: str, ticket_id_: str, pay12: "Pay" = None, cancle14: "Cancle" = None):
        self.date_ = date_
        self.starting_city_ = starting_city_
        self.destination_city = destination_city
        self.time_ = time_
        self.ticket_id_ = ticket_id_
        self.pay12 = pay12
        self.cancle14 = cancle14
        
        pass
    @property
    def ticket_id_(self):
        return self.__ticket_id_
    @ticket_id_.setter
    def ticket_id_(self, ticket_id_: str):
        self.__ticket_id_ = ticket_id_

    @property
    def time_(self):
        return self.__time_
    @time_.setter
    def time_(self, time_: str):
        self.__time_ = time_

    @property
    def date_(self):
        return self.__date_
    @date_.setter
    def date_(self, date_: str):
        self.__date_ = date_

    @property
    def destination_city(self):
        return self.__destination_city
    @destination_city.setter
    def destination_city(self, destination_city: str):
        self.__destination_city = destination_city

    @property
    def starting_city_(self):
        return self.__starting_city_
    @starting_city_.setter
    def starting_city_(self, starting_city_: str):
        self.__starting_city_ = starting_city_

    @property
    def cancle14(self):
        return self.__cancle14
    @cancle14.setter
    def cancle14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book_a_ticek__cancle14", None)
        self.__cancle14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book_a_ticek15"):
                opp_val = getattr(old_value, "book_a_ticek15", None)
                if opp_val == self:
                    setattr(old_value, "book_a_ticek15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book_a_ticek15"):
                opp_val = getattr(value, "book_a_ticek15", None)
                setattr(value, "book_a_ticek15", self)

    @property
    def pay12(self):
        return self.__pay12
    @pay12.setter
    def pay12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book_a_ticek__pay12", None)
        self.__pay12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book_a_ticek13"):
                opp_val = getattr(old_value, "book_a_ticek13", None)
                if opp_val == self:
                    setattr(old_value, "book_a_ticek13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book_a_ticek13"):
                opp_val = getattr(value, "book_a_ticek13", None)
                setattr(value, "book_a_ticek13", self)



class Pay:

    def __init__(self, id_: str, book_a_ticek13: "Book_a_ticek" = None):
        self.id_ = id_
        self.book_a_ticek13 = book_a_ticek13
        
        pass
    @property
    def id_(self):
        return self.__id_
    @id_.setter
    def id_(self, id_: str):
        self.__id_ = id_

    @property
    def book_a_ticek13(self):
        return self.__book_a_ticek13
    @book_a_ticek13.setter
    def book_a_ticek13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pay__book_a_ticek13", None)
        self.__book_a_ticek13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pay12"):
                opp_val = getattr(old_value, "pay12", None)
                if opp_val == self:
                    setattr(old_value, "pay12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pay12"):
                opp_val = getattr(value, "pay12", None)
                setattr(value, "pay12", self)



class view_item:

    def __init__(self, ticket_id_: str, userguest19: "Userguest" = None, login21: "Login" = None):
        self.ticket_id_ = ticket_id_
        self.userguest19 = userguest19
        self.login21 = login21
        
        pass
    @property
    def ticket_id_(self):
        return self.__ticket_id_
    @ticket_id_.setter
    def ticket_id_(self, ticket_id_: str):
        self.__ticket_id_ = ticket_id_

    @property
    def userguest19(self):
        return self.__userguest19
    @userguest19.setter
    def userguest19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_view_item__userguest19", None)
        self.__userguest19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "view_item18"):
                opp_val = getattr(old_value, "view_item18", None)
                if opp_val == self:
                    setattr(old_value, "view_item18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "view_item18"):
                opp_val = getattr(value, "view_item18", None)
                setattr(value, "view_item18", self)

    @property
    def login21(self):
        return self.__login21
    @login21.setter
    def login21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_view_item__login21", None)
        self.__login21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "view_item220"):
                opp_val = getattr(old_value, "view_item220", None)
                if opp_val == self:
                    setattr(old_value, "view_item220", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "view_item220"):
                opp_val = getattr(value, "view_item220", None)
                setattr(value, "view_item220", self)



class Login:

    def __init__(self, password_: str, username_: str, person11: "Person" = None, view_item220: "view_item" = None):
        self.password_ = password_
        self.username_ = username_
        self.person11 = person11
        self.view_item220 = view_item220
        
        pass
    @property
    def username_(self):
        return self.__username_
    @username_.setter
    def username_(self, username_: str):
        self.__username_ = username_

    @property
    def password_(self):
        return self.__password_
    @password_.setter
    def password_(self, password_: str):
        self.__password_ = password_

    @property
    def person11(self):
        return self.__person11
    @person11.setter
    def person11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Login__person11", None)
        self.__person11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "login10"):
                opp_val = getattr(old_value, "login10", None)
                if opp_val == self:
                    setattr(old_value, "login10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "login10"):
                opp_val = getattr(value, "login10", None)
                setattr(value, "login10", self)

    @property
    def view_item220(self):
        return self.__view_item220
    @view_item220.setter
    def view_item220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Login__view_item220", None)
        self.__view_item220 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "login21"):
                opp_val = getattr(old_value, "login21", None)
                if opp_val == self:
                    setattr(old_value, "login21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "login21"):
                opp_val = getattr(value, "login21", None)
                setattr(value, "login21", self)



class User:

    pass


class Admin:

    pass


class Driver:

    pass


class Person:

    def __init__(self, id_: str, name_: str, phone_: str, password_: str, login10: "Login" = None):
        self.id_ = id_
        self.name_ = name_
        self.phone_ = phone_
        self.password_ = password_
        self.login10 = login10
        
        pass
    @property
    def phone_(self):
        return self.__phone_
    @phone_.setter
    def phone_(self, phone_: str):
        self.__phone_ = phone_

    @property
    def password_(self):
        return self.__password_
    @password_.setter
    def password_(self, password_: str):
        self.__password_ = password_

    @property
    def name_(self):
        return self.__name_
    @name_.setter
    def name_(self, name_: str):
        self.__name_ = name_

    @property
    def id_(self):
        return self.__id_
    @id_.setter
    def id_(self, id_: str):
        self.__id_ = id_

    @property
    def login10(self):
        return self.__login10
    @login10.setter
    def login10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Person__login10", None)
        self.__login10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "person11"):
                opp_val = getattr(old_value, "person11", None)
                if opp_val == self:
                    setattr(old_value, "person11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "person11"):
                opp_val = getattr(value, "person11", None)
                setattr(value, "person11", self)



class admin_Actor2:

    pass


class guest_user_Actor2:

    pass


class driver_Actor1:

    pass


class user_Actor2:

    pass


class online_booking_of_bus_tickets_return_the_money_to_the_customer_UseCase1:

    pass


class online_booking_of_bus_tickets_payment_UseCase1:

    pass


class online_booking_of_bus_tickets_ticket_printing_UseCase1:

    pass


class online_booking_of_bus_tickets_changing_seats_by_admin_UseCase1:

    pass


class online_booking_of_bus_tickets_send_message_to_number_registered_UseCase1:

    pass


class online_booking_of_bus_tickets_book_a_ticket_UseCase1:

    pass


class online_booking_of_bus_tickets_exciting_package_UseCase1:

    pass


class online_booking_of_bus_tickets_browse_item_UseCase1:

    pass


class online_booking_of_bus_tickets_enter_password_UseCase1:

    pass


class online_booking_of_bus_tickets_view_seat_UseCase1:

    pass


class online_booking_of_bus_tickets_search_item__UseCase1:

    pass


class online_booking_of_bus_tickets_enter_user_name_UseCase1:

    pass


class online_booking_of_bus_tickets_captcha_UseCase1:

    pass


class online_booking_of_bus_tickets_driver_planing_UseCase1:

    pass


class online_booking_of_bus_tickets_logout_UseCase1:

    pass


class online_booking_of_bus_tickets_submit_information_UseCase1:

    pass


class online_booking_of_bus_tickets_view_item_UseCase1:

    pass


class online_booking_of_bus_tickets_remove_user_UseCase1:

    pass


class online_booking_of_bus_tickets_login_UseCase1:

    pass


class admin_Actor1:

    pass


class guest_user_Actor1:

    pass


class user_Actor1:

    pass
