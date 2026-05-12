from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class User2_Interface:

    pass


class HashTags:

    def __init__(self, allHashTags: str, post9: "Post" = None):
        self.allHashTags = allHashTags
        self.post9 = post9
        
        pass
    @property
    def allHashTags(self):
        return self.__allHashTags
    @allHashTags.setter
    def allHashTags(self, allHashTags: str):
        self.__allHashTags = allHashTags

    @property
    def post9(self):
        return self.__post9
    @post9.setter
    def post9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HashTags__post9", None)
        self.__post9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hashTags8"):
                opp_val = getattr(old_value, "hashTags8", None)
                if opp_val == self:
                    setattr(old_value, "hashTags8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hashTags8"):
                opp_val = getattr(value, "hashTags8", None)
                setattr(value, "hashTags8", self)



class Page:

    def __init__(self, name: str, admin: User, fans: User__, description: str, posts: str, nFans: int, user3: set["User"] = None, post11: "Post" = None):
        self.name = name
        self.admin = admin
        self.fans = fans
        self.description = description
        self.posts = posts
        self.nFans = nFans
        self.user3 = user3 if user3 is not None else set()
        self.post11 = post11
        
        pass
    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def posts(self):
        return self.__posts
    @posts.setter
    def posts(self, posts: str):
        self.__posts = posts

    @property
    def nFans(self):
        return self.__nFans
    @nFans.setter
    def nFans(self, nFans: int):
        self.__nFans = nFans

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def admin(self):
        return self.__admin
    @admin.setter
    def admin(self, admin: User):
        self.__admin = admin

    @property
    def fans(self):
        return self.__fans
    @fans.setter
    def fans(self, fans: User__):
        self.__fans = fans

    @property
    def post11(self):
        return self.__post11
    @post11.setter
    def post11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Page__post11", None)
        self.__post11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "page10"):
                opp_val = getattr(old_value, "page10", None)
                if opp_val == self:
                    setattr(old_value, "page10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "page10"):
                opp_val = getattr(value, "page10", None)
                setattr(value, "page10", self)

    @property
    def user3(self):
        return self.__user3
    @user3.setter
    def user3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Page__user3", None)
        self.__user3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "page2"):
                    opp_val = getattr(item, "page2", None)
                    
                    if opp_val == self:
                        setattr(item, "page2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "page2"):
                    opp_val = getattr(item, "page2", None)
                    
                    setattr(item, "page2", self)
                    



class Post:

    def __init__(self, privateMode: bool, nLikes: int, nComments: int, nShares: int, owner: User, user5: "User" = None, group6: "Group" = None, hashTags8: "HashTags" = None, page10: "Page" = None):
        self.privateMode = privateMode
        self.nLikes = nLikes
        self.nComments = nComments
        self.nShares = nShares
        self.owner = owner
        self.user5 = user5
        self.group6 = group6
        self.hashTags8 = hashTags8
        self.page10 = page10
        
        pass
    @property
    def privateMode(self):
        return self.__privateMode
    @privateMode.setter
    def privateMode(self, privateMode: bool):
        self.__privateMode = privateMode

    @property
    def nLikes(self):
        return self.__nLikes
    @nLikes.setter
    def nLikes(self, nLikes: int):
        self.__nLikes = nLikes

    @property
    def nShares(self):
        return self.__nShares
    @nShares.setter
    def nShares(self, nShares: int):
        self.__nShares = nShares

    @property
    def nComments(self):
        return self.__nComments
    @nComments.setter
    def nComments(self, nComments: int):
        self.__nComments = nComments

    @property
    def owner(self):
        return self.__owner
    @owner.setter
    def owner(self, owner: User):
        self.__owner = owner

    @property
    def page10(self):
        return self.__page10
    @page10.setter
    def page10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Post__page10", None)
        self.__page10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "post11"):
                opp_val = getattr(old_value, "post11", None)
                if opp_val == self:
                    setattr(old_value, "post11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "post11"):
                opp_val = getattr(value, "post11", None)
                setattr(value, "post11", self)

    @property
    def hashTags8(self):
        return self.__hashTags8
    @hashTags8.setter
    def hashTags8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Post__hashTags8", None)
        self.__hashTags8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "post9"):
                opp_val = getattr(old_value, "post9", None)
                if opp_val == self:
                    setattr(old_value, "post9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "post9"):
                opp_val = getattr(value, "post9", None)
                setattr(value, "post9", self)

    @property
    def user5(self):
        return self.__user5
    @user5.setter
    def user5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Post__user5", None)
        self.__user5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "post4"):
                opp_val = getattr(old_value, "post4", None)
                if opp_val == self:
                    setattr(old_value, "post4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "post4"):
                opp_val = getattr(value, "post4", None)
                setattr(value, "post4", self)

    @property
    def group6(self):
        return self.__group6
    @group6.setter
    def group6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Post__group6", None)
        self.__group6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "post7"):
                opp_val = getattr(old_value, "post7", None)
                if opp_val == self:
                    setattr(old_value, "post7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "post7"):
                opp_val = getattr(value, "post7", None)
                setattr(value, "post7", self)



class User__:

    pass


class Group:

    def __init__(self, name: str, description: str, admins: User__, members: User__, nMembers: int, posts: str, user1: set["User"] = None, post7: "Post" = None):
        self.name = name
        self.description = description
        self.admins = admins
        self.members = members
        self.nMembers = nMembers
        self.posts = posts
        self.user1 = user1 if user1 is not None else set()
        self.post7 = post7
        
        pass
    @property
    def admins(self):
        return self.__admins
    @admins.setter
    def admins(self, admins: User__):
        self.__admins = admins

    @property
    def posts(self):
        return self.__posts
    @posts.setter
    def posts(self, posts: str):
        self.__posts = posts

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def members(self):
        return self.__members
    @members.setter
    def members(self, members: User__):
        self.__members = members

    @property
    def nMembers(self):
        return self.__nMembers
    @nMembers.setter
    def nMembers(self, nMembers: int):
        self.__nMembers = nMembers

    @property
    def user1(self):
        return self.__user1
    @user1.setter
    def user1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Group__user1", None)
        self.__user1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "group0"):
                    opp_val = getattr(item, "group0", None)
                    
                    if opp_val == self:
                        setattr(item, "group0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "group0"):
                    opp_val = getattr(item, "group0", None)
                    
                    setattr(item, "group0", self)
                    

    @property
    def post7(self):
        return self.__post7
    @post7.setter
    def post7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Group__post7", None)
        self.__post7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "group6"):
                opp_val = getattr(old_value, "group6", None)
                if opp_val == self:
                    setattr(old_value, "group6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "group6"):
                opp_val = getattr(value, "group6", None)
                setattr(value, "group6", self)



class User:

    def __init__(self, password: str, gender: str, pages: str, groups: str, name: str, username: str, email: str, group0: "Group" = None, page2: "Page" = None, post4: "Post" = None):
        self.password = password
        self.gender = gender
        self.pages = pages
        self.groups = groups
        self.name = name
        self.username = username
        self.email = email
        self.group0 = group0
        self.page2 = page2
        self.post4 = post4
        
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
    def groups(self):
        return self.__groups
    @groups.setter
    def groups(self, groups: str):
        self.__groups = groups

    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pages(self):
        return self.__pages
    @pages.setter
    def pages(self, pages: str):
        self.__pages = pages

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def group0(self):
        return self.__group0
    @group0.setter
    def group0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__group0", None)
        self.__group0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user1"):
                opp_val = getattr(old_value, "user1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user1"):
                opp_val = getattr(value, "user1", None)
                if opp_val is None:
                    setattr(value, "user1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def page2(self):
        return self.__page2
    @page2.setter
    def page2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__page2", None)
        self.__page2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user3"):
                opp_val = getattr(old_value, "user3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user3"):
                opp_val = getattr(value, "user3", None)
                if opp_val is None:
                    setattr(value, "user3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def post4(self):
        return self.__post4
    @post4.setter
    def post4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__post4", None)
        self.__post4 = value
        
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

