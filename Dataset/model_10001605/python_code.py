from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Create_New_Member_UseCase:

    pass


class Head_Librarian_Actor:

    pass


class Inform_Memeber_when_Item_Available_UseCase:

    pass


class Make_Reservation_UseCase:

    pass


class Return_Item_UseCase:

    pass


class Issue_Book_UseCase:

    pass


class Checkout_Librarian_Actor:

    pass


class Carry_Out_Stock_Check_UseCase:

    pass


class Withdraw_Books_UseCase:

    pass


class Purchase_Books_UseCase:

    pass


class Collect_Fine_UseCase:

    pass


class Charge_fine_for_Late_Book_UseCase:

    pass


class Chief_Librarian_Actor:

    pass


class Amend_Membership_details_UseCase:

    pass


class Suspend_Membership_UseCase:

    pass


class Cancel_Membership_UseCase:

    pass





class Reservations:

    pass


class Library_Members:

    def __init__(self, Name: str):
        self.Name = Name
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name



class Books:

    def __init__(self, Title: str):
        self.Title = Title
        
        pass
    @property
    def Title(self):
        return self.__Title
    @Title.setter
    def Title(self, Title: str):
        self.__Title = Title

