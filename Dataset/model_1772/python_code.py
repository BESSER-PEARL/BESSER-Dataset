from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class bookOrder_Book:

    def __init__(self, title: str, bookOrder_Book: "bookOrder_BookOrder" = None):
        self.title = title
        self.bookOrder_Book = bookOrder_Book
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def bookOrder_Book(self):
        return self.__bookOrder_Book

    @bookOrder_Book.setter
    def bookOrder_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookOrder_Book__bookOrder_Book", None)
        self.__bookOrder_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookOrder_BookOrder2"):
                opp_val = getattr(old_value, "bookOrder_BookOrder2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookOrder_BookOrder2"):
                opp_val = getattr(value, "bookOrder_BookOrder2", None)
                if opp_val is None:
                    setattr(value, "bookOrder_BookOrder2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bookOrder_BookOrder:

    def __init__(self, info: str, bookOrder_BookOrder: "bookOrder_Universe" = None, bookOrder_BookOrder2: set["bookOrder_Book"] = None):
        self.info = info
        self.bookOrder_BookOrder = bookOrder_BookOrder
        self.bookOrder_BookOrder2 = bookOrder_BookOrder2 if bookOrder_BookOrder2 is not None else set()
        
    @property
    def info(self) -> str:
        return self.__info

    @info.setter
    def info(self, info: str):
        self.__info = info

    @property
    def bookOrder_BookOrder(self):
        return self.__bookOrder_BookOrder

    @bookOrder_BookOrder.setter
    def bookOrder_BookOrder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookOrder_BookOrder__bookOrder_BookOrder", None)
        self.__bookOrder_BookOrder = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookOrder_Universe"):
                opp_val = getattr(old_value, "bookOrder_Universe", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookOrder_Universe"):
                opp_val = getattr(value, "bookOrder_Universe", None)
                if opp_val is None:
                    setattr(value, "bookOrder_Universe", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bookOrder_BookOrder2(self):
        return self.__bookOrder_BookOrder2

    @bookOrder_BookOrder2.setter
    def bookOrder_BookOrder2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookOrder_BookOrder__bookOrder_BookOrder2", None)
        self.__bookOrder_BookOrder2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bookOrder_Book"):
                    opp_val = getattr(item, "bookOrder_Book", None)
                    
                    if opp_val == self:
                        setattr(item, "bookOrder_Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bookOrder_Book"):
                    opp_val = getattr(item, "bookOrder_Book", None)
                    
                    setattr(item, "bookOrder_Book", self)
                    

class bookOrder_Universe:

    pass