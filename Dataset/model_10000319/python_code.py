from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class post_status(Enum):
    pass
class UserState(Enum):
    pass

############################################
# Definition of Classes
############################################










class post:

    def __init__(self, ID: int, description: str, lineItems10: set["LineItem"] = None):
        self.ID = ID
        self.description = description
        self.lineItems10 = lineItems10 if lineItems10 is not None else set()
        
        pass
    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def lineItems10(self):
        return self.__lineItems10
    @lineItems10.setter
    def lineItems10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_post__lineItems10", None)
        self.__lineItems10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Post11"):
                    opp_val = getattr(item, "Post11", None)
                    
                    if opp_val == self:
                        setattr(item, "Post11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Post11"):
                    opp_val = getattr(item, "Post11", None)
                    
                    setattr(item, "Post11", self)
                    



class LineItem:

    def __init__(self, category: int, tags: float, order13: "Post" = None, sc9: "AddPost" = None, Post11: "post" = None):
        self.category = category
        self.tags = tags
        self.order13 = order13
        self.sc9 = sc9
        self.Post11 = Post11
        
        pass
    @property
    def category(self):
        return self.__category
    @category.setter
    def category(self, category: int):
        self.__category = category

    @property
    def tags(self):
        return self.__tags
    @tags.setter
    def tags(self, tags: float):
        self.__tags = tags

    @property
    def order13(self):
        return self.__order13
    @order13.setter
    def order13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LineItem__order13", None)
        self.__order13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "additionals12"):
                opp_val = getattr(old_value, "additionals12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "additionals12"):
                opp_val = getattr(value, "additionals12", None)
                if opp_val is None:
                    setattr(value, "additionals12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sc9(self):
        return self.__sc9
    @sc9.setter
    def sc9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LineItem__sc9", None)
        self.__sc9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "items8"):
                opp_val = getattr(old_value, "items8", None)
                if opp_val == self:
                    setattr(old_value, "items8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "items8"):
                opp_val = getattr(value, "items8", None)
                setattr(value, "items8", self)

    @property
    def Post11(self):
        return self.__Post11
    @Post11.setter
    def Post11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LineItem__Post11", None)
        self.__Post11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lineItems10"):
                opp_val = getattr(old_value, "lineItems10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lineItems10"):
                opp_val = getattr(value, "lineItems10", None)
                if opp_val is None:
                    setattr(value, "lineItems10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Post:

    def __init__(self, ID: int, Created: date, User: str, Category: str, tags: float, status: post_status, additionals12: set["LineItem"] = None, account15: "Account" = None):
        self.ID = ID
        self.Created = Created
        self.User = User
        self.Category = Category
        self.tags = tags
        self.status = status
        self.additionals12 = additionals12 if additionals12 is not None else set()
        self.account15 = account15
        
        pass
    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def User(self):
        return self.__User
    @User.setter
    def User(self, User: str):
        self.__User = User

    @property
    def tags(self):
        return self.__tags
    @tags.setter
    def tags(self, tags: float):
        self.__tags = tags

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: post_status):
        self.__status = status

    @property
    def Category(self):
        return self.__Category
    @Category.setter
    def Category(self, Category: str):
        self.__Category = Category

    @property
    def Created(self):
        return self.__Created
    @Created.setter
    def Created(self, Created: date):
        self.__Created = Created

    @property
    def account15(self):
        return self.__account15
    @account15.setter
    def account15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Post__account15", None)
        self.__account15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order14"):
                opp_val = getattr(old_value, "order14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order14"):
                opp_val = getattr(value, "order14", None)
                if opp_val is None:
                    setattr(value, "order14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def additionals12(self):
        return self.__additionals12
    @additionals12.setter
    def additionals12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Post__additionals12", None)
        self.__additionals12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "order13"):
                    opp_val = getattr(item, "order13", None)
                    
                    if opp_val == self:
                        setattr(item, "order13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "order13"):
                    opp_val = getattr(item, "order13", None)
                    
                    setattr(item, "order13", self)
                    



class WebUser:

    def __init__(self, login: str, password: str, state: UserState, shoppingCart0: "AddPost" = None, customer2: "User" = None):
        self.login = login
        self.password = password
        self.state = state
        self.shoppingCart0 = shoppingCart0
        self.customer2 = customer2
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def login(self):
        return self.__login
    @login.setter
    def login(self, login: str):
        self.__login = login

    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, state: UserState):
        self.__state = state

    @property
    def shoppingCart0(self):
        return self.__shoppingCart0
    @shoppingCart0.setter
    def shoppingCart0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WebUser__shoppingCart0", None)
        self.__shoppingCart0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webUser1"):
                opp_val = getattr(old_value, "webUser1", None)
                if opp_val == self:
                    setattr(old_value, "webUser1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webUser1"):
                opp_val = getattr(value, "webUser1", None)
                setattr(value, "webUser1", self)

    @property
    def customer2(self):
        return self.__customer2
    @customer2.setter
    def customer2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WebUser__customer2", None)
        self.__customer2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webUser3"):
                opp_val = getattr(old_value, "webUser3", None)
                if opp_val == self:
                    setattr(old_value, "webUser3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webUser3"):
                opp_val = getattr(value, "webUser3", None)
                setattr(value, "webUser3", self)



class Account:

    def __init__(self, Name: str, created: date, closed: date, isClosed: bool, customer5: "User" = None, cart6: "AddPost" = None, order14: set["Post"] = None):
        self.Name = Name
        self.created = created
        self.closed = closed
        self.isClosed = isClosed
        self.customer5 = customer5
        self.cart6 = cart6
        self.order14 = order14 if order14 is not None else set()
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def created(self):
        return self.__created
    @created.setter
    def created(self, created: date):
        self.__created = created

    @property
    def isClosed(self):
        return self.__isClosed
    @isClosed.setter
    def isClosed(self, isClosed: bool):
        self.__isClosed = isClosed

    @property
    def closed(self):
        return self.__closed
    @closed.setter
    def closed(self, closed: date):
        self.__closed = closed

    @property
    def cart6(self):
        return self.__cart6
    @cart6.setter
    def cart6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__cart6", None)
        self.__cart6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account7"):
                opp_val = getattr(old_value, "account7", None)
                if opp_val == self:
                    setattr(old_value, "account7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account7"):
                opp_val = getattr(value, "account7", None)
                setattr(value, "account7", self)

    @property
    def customer5(self):
        return self.__customer5
    @customer5.setter
    def customer5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__customer5", None)
        self.__customer5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account4"):
                opp_val = getattr(old_value, "account4", None)
                if opp_val == self:
                    setattr(old_value, "account4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account4"):
                opp_val = getattr(value, "account4", None)
                setattr(value, "account4", self)

    @property
    def order14(self):
        return self.__order14
    @order14.setter
    def order14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__order14", None)
        self.__order14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "account15"):
                    opp_val = getattr(item, "account15", None)
                    
                    if opp_val == self:
                        setattr(item, "account15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "account15"):
                    opp_val = getattr(item, "account15", None)
                    
                    setattr(item, "account15", self)
                    



class AddPost:

    def __init__(self, creationDate: date, webUser1: "WebUser" = None, account7: "Account" = None, items8: "LineItem" = None):
        self.creationDate = creationDate
        self.webUser1 = webUser1
        self.account7 = account7
        self.items8 = items8
        
        pass
    @property
    def creationDate(self):
        return self.__creationDate
    @creationDate.setter
    def creationDate(self, creationDate: date):
        self.__creationDate = creationDate

    @property
    def webUser1(self):
        return self.__webUser1
    @webUser1.setter
    def webUser1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AddPost__webUser1", None)
        self.__webUser1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shoppingCart0"):
                opp_val = getattr(old_value, "shoppingCart0", None)
                if opp_val == self:
                    setattr(old_value, "shoppingCart0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shoppingCart0"):
                opp_val = getattr(value, "shoppingCart0", None)
                setattr(value, "shoppingCart0", self)

    @property
    def items8(self):
        return self.__items8
    @items8.setter
    def items8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AddPost__items8", None)
        self.__items8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sc9"):
                opp_val = getattr(old_value, "sc9", None)
                if opp_val == self:
                    setattr(old_value, "sc9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sc9"):
                opp_val = getattr(value, "sc9", None)
                setattr(value, "sc9", self)

    @property
    def account7(self):
        return self.__account7
    @account7.setter
    def account7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AddPost__account7", None)
        self.__account7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cart6"):
                opp_val = getattr(old_value, "cart6", None)
                if opp_val == self:
                    setattr(old_value, "cart6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cart6"):
                opp_val = getattr(value, "cart6", None)
                setattr(value, "cart6", self)



class User:

    def __init__(self, Id: int, Name: str, email: str, webUser3: "WebUser" = None, account4: "Account" = None):
        self.Id = Id
        self.Name = Name
        self.email = email
        self.webUser3 = webUser3
        self.account4 = account4
        
        pass
    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: int):
        self.__Id = Id

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def account4(self):
        return self.__account4
    @account4.setter
    def account4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__account4", None)
        self.__account4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer5"):
                opp_val = getattr(old_value, "customer5", None)
                if opp_val == self:
                    setattr(old_value, "customer5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer5"):
                opp_val = getattr(value, "customer5", None)
                setattr(value, "customer5", self)

    @property
    def webUser3(self):
        return self.__webUser3
    @webUser3.setter
    def webUser3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__webUser3", None)
        self.__webUser3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer2"):
                opp_val = getattr(old_value, "customer2", None)
                if opp_val == self:
                    setattr(old_value, "customer2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer2"):
                opp_val = getattr(value, "customer2", None)
                setattr(value, "customer2", self)

