from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class client_Actor:

    pass


class login_UseCase:

    pass


class logout_technician_UseCase:

    pass


class send_to_admin_UseCase:

    pass


class find_out_fault_UseCase:

    pass


class new_complaint_details_UseCase:

    pass


class login_technical_UseCase:

    pass


class technical_team_Actor:

    pass


class search_user_UseCase:

    pass


class create_user_UseCase:

    pass


class administrator_Actor:

    pass


class logout_UseCase:

    pass


class view_status_UseCase:

    pass


class register_complaint_UseCase:

    pass





class Login:

    pass


class DbDetails:

    pass


class CheckStatus:

    pass


class Logout:

    pass


class UpdateStatus:

    pass


class Administrator:

    def __init__(self, password: str):
        self.password = password
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password



class RegisterComplaint:

    pass


class MonitorComplaint:

    pass


class Customer:

    pass


class login:

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        
        pass
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password



class D_B_details:

    def __init__(self, logged_in: str, session_out: str):
        self.logged_in = logged_in
        self.session_out = session_out
        
        pass
    @property
    def logged_in(self):
        return self.__logged_in
    @logged_in.setter
    def logged_in(self, logged_in: str):
        self.__logged_in = logged_in

    @property
    def session_out(self):
        return self.__session_out
    @session_out.setter
    def session_out(self, session_out: str):
        self.__session_out = session_out



class logout:

    def __init__(self, session_out: str):
        self.session_out = session_out
        
        pass
    @property
    def session_out(self):
        return self.__session_out
    @session_out.setter
    def session_out(self, session_out: str):
        self.__session_out = session_out



class check_status:

    def __init__(self, complaint: str):
        self.complaint = complaint
        
        pass
    @property
    def complaint(self):
        return self.__complaint
    @complaint.setter
    def complaint(self, complaint: str):
        self.__complaint = complaint



class register_complaint:

    def __init__(self, complaint_type: str, description: str):
        self.complaint_type = complaint_type
        self.description = description
        
        pass
    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def complaint_type(self):
        return self.__complaint_type
    @complaint_type.setter
    def complaint_type(self, complaint_type: str):
        self.__complaint_type = complaint_type



class update_status:

    def __init__(self, supdate: str):
        self.supdate = supdate
        
        pass
    @property
    def supdate(self):
        return self.__supdate
    @supdate.setter
    def supdate(self, supdate: str):
        self.__supdate = supdate



class administrator:

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username



class monitor_complaint:

    def __init__(self, complaintid: int, complaint_type: str, date: str):
        self.complaintid = complaintid
        self.complaint_type = complaint_type
        self.date = date
        
        pass
    @property
    def complaint_type(self):
        return self.__complaint_type
    @complaint_type.setter
    def complaint_type(self, complaint_type: str):
        self.__complaint_type = complaint_type

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def complaintid(self):
        return self.__complaintid
    @complaintid.setter
    def complaintid(self, complaintid: int):
        self.__complaintid = complaintid



class customer:

    def __init__(self, product_id: str, email_id: int, name: str, address: str):
        self.product_id = product_id
        self.email_id = email_id
        self.name = name
        self.address = address
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def product_id(self):
        return self.__product_id
    @product_id.setter
    def product_id(self, product_id: str):
        self.__product_id = product_id

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def email_id(self):
        return self.__email_id
    @email_id.setter
    def email_id(self, email_id: int):
        self.__email_id = email_id

