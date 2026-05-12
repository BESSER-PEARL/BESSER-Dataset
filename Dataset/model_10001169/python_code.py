from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class test_UseCase:

    pass


class User_Actor:

    pass





class Admin1:

    pass


class Student1:

    def __init__(self, school: str, course: str, yearOfStudy: int):
        self.school = school
        self.course = course
        self.yearOfStudy = yearOfStudy
        
        pass
    @property
    def yearOfStudy(self):
        return self.__yearOfStudy
    @yearOfStudy.setter
    def yearOfStudy(self, yearOfStudy: int):
        self.__yearOfStudy = yearOfStudy

    @property
    def school(self):
        return self.__school
    @school.setter
    def school(self, school: str):
        self.__school = school

    @property
    def course(self):
        return self.__course
    @course.setter
    def course(self, course: str):
        self.__course = course



class Society1:

    def __init__(self, yearEstablished: int):
        self.yearEstablished = yearEstablished
        
        pass
    @property
    def yearEstablished(self):
        return self.__yearEstablished
    @yearEstablished.setter
    def yearEstablished(self, yearEstablished: int):
        self.__yearEstablished = yearEstablished



class Lecturer1:

    def __init__(self, school: str):
        self.school = school
        
        pass
    @property
    def school(self):
        return self.__school
    @school.setter
    def school(self, school: str):
        self.__school = school



class Comment1:

    def __init__(self, author: str, date: str, body: str, user20: "User1" = None, post25: "Post1" = None):
        self.author = author
        self.date = date
        self.body = body
        self.user20 = user20
        self.post25 = post25
        
        pass
    @property
    def body(self):
        return self.__body
    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def author(self):
        return self.__author
    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def user20(self):
        return self.__user20
    @user20.setter
    def user20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Comment1__user20", None)
        self.__user20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "comment21"):
                opp_val = getattr(old_value, "comment21", None)
                if opp_val == self:
                    setattr(old_value, "comment21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "comment21"):
                opp_val = getattr(value, "comment21", None)
                setattr(value, "comment21", self)

    @property
    def post25(self):
        return self.__post25
    @post25.setter
    def post25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Comment1__post25", None)
        self.__post25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "comment24"):
                opp_val = getattr(old_value, "comment24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "comment24"):
                opp_val = getattr(value, "comment24", None)
                if opp_val is None:
                    setattr(value, "comment24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Location1:

    def __init__(self, name: str, address: str, capacity: int, event28: "Event1" = None):
        self.name = name
        self.address = address
        self.capacity = capacity
        self.event28 = event28
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def capacity(self):
        return self.__capacity
    @capacity.setter
    def capacity(self, capacity: int):
        self.__capacity = capacity

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def event28(self):
        return self.__event28
    @event28.setter
    def event28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Location1__event28", None)
        self.__event28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "location229"):
                opp_val = getattr(old_value, "location229", None)
                if opp_val == self:
                    setattr(old_value, "location229", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "location229"):
                opp_val = getattr(value, "location229", None)
                setattr(value, "location229", self)



class Event1:

    def __init__(self, eventOwner: User1, size: int, isOpen: bool, invites: str, joined: str, name: str, location: Location, date: str, rating: int, user23: "User1" = None, post26: set["Post1"] = None, location229: "Location1" = None):
        self.eventOwner = eventOwner
        self.size = size
        self.isOpen = isOpen
        self.invites = invites
        self.joined = joined
        self.name = name
        self.location = location
        self.date = date
        self.rating = rating
        self.user23 = user23
        self.post26 = post26 if post26 is not None else set()
        self.location229 = location229
        
        pass
    @property
    def rating(self):
        return self.__rating
    @rating.setter
    def rating(self, rating: int):
        self.__rating = rating

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, location: Location):
        self.__location = location

    @property
    def eventOwner(self):
        return self.__eventOwner
    @eventOwner.setter
    def eventOwner(self, eventOwner: User1):
        self.__eventOwner = eventOwner

    @property
    def isOpen(self):
        return self.__isOpen
    @isOpen.setter
    def isOpen(self, isOpen: bool):
        self.__isOpen = isOpen

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def invites(self):
        return self.__invites
    @invites.setter
    def invites(self, invites: str):
        self.__invites = invites

    @property
    def joined(self):
        return self.__joined
    @joined.setter
    def joined(self, joined: str):
        self.__joined = joined

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def post26(self):
        return self.__post26
    @post26.setter
    def post26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Event1__post26", None)
        self.__post26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "event27"):
                    opp_val = getattr(item, "event27", None)
                    
                    if opp_val == self:
                        setattr(item, "event27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "event27"):
                    opp_val = getattr(item, "event27", None)
                    
                    setattr(item, "event27", self)
                    

    @property
    def user23(self):
        return self.__user23
    @user23.setter
    def user23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Event1__user23", None)
        self.__user23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "event22"):
                opp_val = getattr(old_value, "event22", None)
                if opp_val == self:
                    setattr(old_value, "event22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "event22"):
                opp_val = getattr(value, "event22", None)
                setattr(value, "event22", self)

    @property
    def location229(self):
        return self.__location229
    @location229.setter
    def location229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Event1__location229", None)
        self.__location229 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "event28"):
                opp_val = getattr(old_value, "event28", None)
                if opp_val == self:
                    setattr(old_value, "event28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "event28"):
                opp_val = getattr(value, "event28", None)
                setattr(value, "event28", self)



class Post1:

    def __init__(self, date: str, title: str, body: str, author: str, files: str, user19: "User1" = None, comment24: set["Comment1"] = None, event27: "Event1" = None):
        self.date = date
        self.title = title
        self.body = body
        self.author = author
        self.files = files
        self.user19 = user19
        self.comment24 = comment24 if comment24 is not None else set()
        self.event27 = event27
        
        pass
    @property
    def files(self):
        return self.__files
    @files.setter
    def files(self, files: str):
        self.__files = files

    @property
    def body(self):
        return self.__body
    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def author(self):
        return self.__author
    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def comment24(self):
        return self.__comment24
    @comment24.setter
    def comment24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Post1__comment24", None)
        self.__comment24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "post25"):
                    opp_val = getattr(item, "post25", None)
                    
                    if opp_val == self:
                        setattr(item, "post25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "post25"):
                    opp_val = getattr(item, "post25", None)
                    
                    setattr(item, "post25", self)
                    

    @property
    def user19(self):
        return self.__user19
    @user19.setter
    def user19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Post1__user19", None)
        self.__user19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "post18"):
                opp_val = getattr(old_value, "post18", None)
                if opp_val == self:
                    setattr(old_value, "post18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "post18"):
                opp_val = getattr(value, "post18", None)
                setattr(value, "post18", self)

    @property
    def event27(self):
        return self.__event27
    @event27.setter
    def event27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Post1__event27", None)
        self.__event27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "post26"):
                opp_val = getattr(old_value, "post26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "post26"):
                opp_val = getattr(value, "post26", None)
                if opp_val is None:
                    setattr(value, "post26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class User1:

    def __init__(self, username: str, email: str, name: str, campus: str, isStaff: bool, attribute: str, virtualTour16: "VirtualTour1" = None, post18: "Post1" = None, comment21: "Comment1" = None, event22: "Event1" = None):
        self.username = username
        self.email = email
        self.name = name
        self.campus = campus
        self.isStaff = isStaff
        self.attribute = attribute
        self.virtualTour16 = virtualTour16
        self.post18 = post18
        self.comment21 = comment21
        self.event22 = event22
        
        pass
    @property
    def campus(self):
        return self.__campus
    @campus.setter
    def campus(self, campus: str):
        self.__campus = campus

    @property
    def isStaff(self):
        return self.__isStaff
    @isStaff.setter
    def isStaff(self, isStaff: bool):
        self.__isStaff = isStaff

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def virtualTour16(self):
        return self.__virtualTour16
    @virtualTour16.setter
    def virtualTour16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User1__virtualTour16", None)
        self.__virtualTour16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user17"):
                opp_val = getattr(old_value, "user17", None)
                if opp_val == self:
                    setattr(old_value, "user17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user17"):
                opp_val = getattr(value, "user17", None)
                setattr(value, "user17", self)

    @property
    def event22(self):
        return self.__event22
    @event22.setter
    def event22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User1__event22", None)
        self.__event22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user23"):
                opp_val = getattr(old_value, "user23", None)
                if opp_val == self:
                    setattr(old_value, "user23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user23"):
                opp_val = getattr(value, "user23", None)
                setattr(value, "user23", self)

    @property
    def comment21(self):
        return self.__comment21
    @comment21.setter
    def comment21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User1__comment21", None)
        self.__comment21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user20"):
                opp_val = getattr(old_value, "user20", None)
                if opp_val == self:
                    setattr(old_value, "user20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user20"):
                opp_val = getattr(value, "user20", None)
                setattr(value, "user20", self)

    @property
    def post18(self):
        return self.__post18
    @post18.setter
    def post18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User1__post18", None)
        self.__post18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user19"):
                opp_val = getattr(old_value, "user19", None)
                if opp_val == self:
                    setattr(old_value, "user19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user19"):
                opp_val = getattr(value, "user19", None)
                setattr(value, "user19", self)



class VirtualTour1:

    def __init__(self, URL: str, myClass15: "Guest1" = None, user17: "User1" = None):
        self.URL = URL
        self.myClass15 = myClass15
        self.user17 = user17
        
        pass
    @property
    def URL(self):
        return self.__URL
    @URL.setter
    def URL(self, URL: str):
        self.__URL = URL

    @property
    def user17(self):
        return self.__user17
    @user17.setter
    def user17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VirtualTour1__user17", None)
        self.__user17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "virtualTour16"):
                opp_val = getattr(old_value, "virtualTour16", None)
                if opp_val == self:
                    setattr(old_value, "virtualTour16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "virtualTour16"):
                opp_val = getattr(value, "virtualTour16", None)
                setattr(value, "virtualTour16", self)

    @property
    def myClass15(self):
        return self.__myClass15
    @myClass15.setter
    def myClass15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VirtualTour1__myClass15", None)
        self.__myClass15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myClass214"):
                opp_val = getattr(old_value, "myClass214", None)
                if opp_val == self:
                    setattr(old_value, "myClass214", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myClass214"):
                opp_val = getattr(value, "myClass214", None)
                setattr(value, "myClass214", self)



class Guest1:

    pass


class Comment:

    pass


class Location:

    pass


class Event:

    pass


class Post:

    pass


class Student:

    pass


class Society:

    pass


class Lecturer:

    pass


class Admin:

    pass


class User:

    pass


class VirtualTour:

    pass


class Guest:

    pass
