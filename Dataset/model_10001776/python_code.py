from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class View_price_of_served_orders_UseCase:

    pass


class Cashier_Actor:

    pass


class Mark_order_as_prepared_UseCase:

    pass


class View_current_orders_UseCase:

    pass


class Chef_Actor:

    pass


class Place_order_UseCase:

    pass


class Consult_menu_UseCase:

    pass


class Mark_order_as_served_UseCase:

    pass


class View_prepared_orders_UseCase:

    pass


class Register_order_UseCase:

    pass


class Client_Actor:

    pass


class Waiter_Actor:

    pass





class Tag:

    pass


class User:

    pass


class QuestonOrAnswer:

    def __init__(self, body: str, user17: "User" = None):
        self.body = body
        self.user17 = user17
        
        pass
    @property
    def body(self):
        return self.__body
    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def user17(self):
        return self.__user17
    @user17.setter
    def user17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QuestonOrAnswer__user17", None)
        self.__user17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "questonOrAnswer16"):
                opp_val = getattr(old_value, "questonOrAnswer16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "questonOrAnswer16"):
                opp_val = getattr(value, "questonOrAnswer16", None)
                if opp_val is None:
                    setattr(value, "questonOrAnswer16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Answer:

    pass


class Question:

    def __init__(self, title: str, tags19: set["Tag"] = None, question20: "Question" = None, similar21: set["Question"] = None):
        self.title = title
        self.tags19 = tags19 if tags19 is not None else set()
        self.question20 = question20
        self.similar21 = similar21 if similar21 is not None else set()
        
        pass
    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def question20(self):
        return self.__question20
    @question20.setter
    def question20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Question__question20", None)
        self.__question20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "similar21"):
                opp_val = getattr(old_value, "similar21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "similar21"):
                opp_val = getattr(value, "similar21", None)
                if opp_val is None:
                    setattr(value, "similar21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tags19(self):
        return self.__tags19
    @tags19.setter
    def tags19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Question__tags19", None)
        self.__tags19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "questions18"):
                    opp_val = getattr(item, "questions18", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "questions18"):
                    opp_val = getattr(item, "questions18", None)
                    
                    if opp_val is None:
                        setattr(item, "questions18", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def similar21(self):
        return self.__similar21
    @similar21.setter
    def similar21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Question__similar21", None)
        self.__similar21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "question20"):
                    opp_val = getattr(item, "question20", None)
                    
                    if opp_val == self:
                        setattr(item, "question20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "question20"):
                    opp_val = getattr(item, "question20", None)
                    
                    setattr(item, "question20", self)
                    

