from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Dessert:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name



class Main_Course:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name



class Login:

    def __init__(self, username: str, password: str, user5: "User" = None):
        self.username = username
        self.password = password
        self.user5 = user5
        
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

    @property
    def user5(self):
        return self.__user5
    @user5.setter
    def user5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Login__user5", None)
        self.__user5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "login4"):
                opp_val = getattr(old_value, "login4", None)
                if opp_val == self:
                    setattr(old_value, "login4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "login4"):
                opp_val = getattr(value, "login4", None)
                setattr(value, "login4", self)



class Bio_Info:

    def __init__(self, name: str, age: str, favourite_cuisine: str, average_ratings: int, user13: "User" = None):
        self.name = name
        self.age = age
        self.favourite_cuisine = favourite_cuisine
        self.average_ratings = average_ratings
        self.user13 = user13
        
        pass
    @property
    def favourite_cuisine(self):
        return self.__favourite_cuisine
    @favourite_cuisine.setter
    def favourite_cuisine(self, favourite_cuisine: str):
        self.__favourite_cuisine = favourite_cuisine

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age: str):
        self.__age = age

    @property
    def average_ratings(self):
        return self.__average_ratings
    @average_ratings.setter
    def average_ratings(self, average_ratings: int):
        self.__average_ratings = average_ratings

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def user13(self):
        return self.__user13
    @user13.setter
    def user13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bio_Info__user13", None)
        self.__user13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pages12"):
                opp_val = getattr(old_value, "pages12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pages12"):
                opp_val = getattr(value, "pages12", None)
                if opp_val is None:
                    setattr(value, "pages12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Social_Media:

    def __init__(self, name: str, user11: "User" = None):
        self.name = name
        self.user11 = user11
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def user11(self):
        return self.__user11
    @user11.setter
    def user11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Social_Media__user11", None)
        self.__user11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hashtag10"):
                opp_val = getattr(old_value, "hashtag10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hashtag10"):
                opp_val = getattr(value, "hashtag10", None)
                if opp_val is None:
                    setattr(value, "hashtag10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Visitor_Comment:

    pass


class Drinks:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name



class Vegetarian:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name



class Browse_Recipes:

    def __init__(self, name: str, description: str, user7: "User" = None):
        self.name = name
        self.description = description
        self.user7 = user7
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def user7(self):
        return self.__user7
    @user7.setter
    def user7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Browse_Recipes__user7", None)
        self.__user7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "group6"):
                opp_val = getattr(old_value, "group6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "group6"):
                opp_val = getattr(value, "group6", None)
                if opp_val is None:
                    setattr(value, "group6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Return:

    pass


class Profile_Page:

    def __init__(self, username: str, password: str, user1: "User" = None):
        self.username = username
        self.password = password
        self.user1 = user1
        
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

    @property
    def user1(self):
        return self.__user1
    @user1.setter
    def user1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Profile_Page__user1", None)
        self.__user1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myprofile0"):
                opp_val = getattr(old_value, "myprofile0", None)
                if opp_val == self:
                    setattr(old_value, "myprofile0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myprofile0"):
                opp_val = getattr(value, "myprofile0", None)
                setattr(value, "myprofile0", self)



class User:

    def __init__(self, name: str, myprofile0: "Profile_Page" = None, post2: set["Return"] = None, login4: "Login" = None, group6: set["Browse_Recipes"] = None, friends8: set["Visitor_Comment"] = None, hashtag10: set["Social_Media"] = None, pages12: set["Bio_Info"] = None):
        self.name = name
        self.myprofile0 = myprofile0
        self.post2 = post2 if post2 is not None else set()
        self.login4 = login4
        self.group6 = group6 if group6 is not None else set()
        self.friends8 = friends8 if friends8 is not None else set()
        self.hashtag10 = hashtag10 if hashtag10 is not None else set()
        self.pages12 = pages12 if pages12 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pages12(self):
        return self.__pages12
    @pages12.setter
    def pages12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__pages12", None)
        self.__pages12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user13"):
                    opp_val = getattr(item, "user13", None)
                    
                    if opp_val == self:
                        setattr(item, "user13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user13"):
                    opp_val = getattr(item, "user13", None)
                    
                    setattr(item, "user13", self)
                    

    @property
    def myprofile0(self):
        return self.__myprofile0
    @myprofile0.setter
    def myprofile0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__myprofile0", None)
        self.__myprofile0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user1"):
                opp_val = getattr(old_value, "user1", None)
                if opp_val == self:
                    setattr(old_value, "user1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user1"):
                opp_val = getattr(value, "user1", None)
                setattr(value, "user1", self)

    @property
    def hashtag10(self):
        return self.__hashtag10
    @hashtag10.setter
    def hashtag10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__hashtag10", None)
        self.__hashtag10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user11"):
                    opp_val = getattr(item, "user11", None)
                    
                    if opp_val == self:
                        setattr(item, "user11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user11"):
                    opp_val = getattr(item, "user11", None)
                    
                    setattr(item, "user11", self)
                    

    @property
    def login4(self):
        return self.__login4
    @login4.setter
    def login4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__login4", None)
        self.__login4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user5"):
                opp_val = getattr(old_value, "user5", None)
                if opp_val == self:
                    setattr(old_value, "user5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user5"):
                opp_val = getattr(value, "user5", None)
                setattr(value, "user5", self)

    @property
    def post2(self):
        return self.__post2
    @post2.setter
    def post2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__post2", None)
        self.__post2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user3"):
                    opp_val = getattr(item, "user3", None)
                    
                    if opp_val == self:
                        setattr(item, "user3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user3"):
                    opp_val = getattr(item, "user3", None)
                    
                    setattr(item, "user3", self)
                    

    @property
    def group6(self):
        return self.__group6
    @group6.setter
    def group6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__group6", None)
        self.__group6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user7"):
                    opp_val = getattr(item, "user7", None)
                    
                    if opp_val == self:
                        setattr(item, "user7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user7"):
                    opp_val = getattr(item, "user7", None)
                    
                    setattr(item, "user7", self)
                    

    @property
    def friends8(self):
        return self.__friends8
    @friends8.setter
    def friends8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__friends8", None)
        self.__friends8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user9"):
                    opp_val = getattr(item, "user9", None)
                    
                    if opp_val == self:
                        setattr(item, "user9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user9"):
                    opp_val = getattr(item, "user9", None)
                    
                    setattr(item, "user9", self)
                    

