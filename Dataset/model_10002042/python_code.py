from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class GUI:

    pass


class CreditCard:

    pass


class PayPal:

    pass


class PaymentMethod:

    pass


class HashTags1:

    def __init__(self, allHashTags: str, post44: "Post1" = None):
        self.allHashTags = allHashTags
        self.post44 = post44
        
        pass
    @property
    def allHashTags(self):
        return self.__allHashTags
    @allHashTags.setter
    def allHashTags(self, allHashTags: str):
        self.__allHashTags = allHashTags

    @property
    def post44(self):
        return self.__post44
    @post44.setter
    def post44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HashTags1__post44", None)
        self.__post44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hashTags45"):
                opp_val = getattr(old_value, "hashTags45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hashTags45"):
                opp_val = getattr(value, "hashTags45", None)
                if opp_val is None:
                    setattr(value, "hashTags45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Post1:

    def __init__(self, CommentContainer: str, privateMode: bool, nLikes: int, nComments: int, nShares: int, owner: User, LikeContainer_int_: str, system_Controller34: "System_Controller" = None, hashTags45: set["HashTags1"] = None):
        self.CommentContainer = CommentContainer
        self.privateMode = privateMode
        self.nLikes = nLikes
        self.nComments = nComments
        self.nShares = nShares
        self.owner = owner
        self.LikeContainer_int_ = LikeContainer_int_
        self.system_Controller34 = system_Controller34
        self.hashTags45 = hashTags45 if hashTags45 is not None else set()
        
        pass
    @property
    def privateMode(self):
        return self.__privateMode
    @privateMode.setter
    def privateMode(self, privateMode: bool):
        self.__privateMode = privateMode

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
    def nLikes(self):
        return self.__nLikes
    @nLikes.setter
    def nLikes(self, nLikes: int):
        self.__nLikes = nLikes

    @property
    def owner(self):
        return self.__owner
    @owner.setter
    def owner(self, owner: User):
        self.__owner = owner

    @property
    def CommentContainer(self):
        return self.__CommentContainer
    @CommentContainer.setter
    def CommentContainer(self, CommentContainer: str):
        self.__CommentContainer = CommentContainer

    @property
    def LikeContainer_int_(self):
        return self.__LikeContainer_int_
    @LikeContainer_int_.setter
    def LikeContainer_int_(self, LikeContainer_int_: str):
        self.__LikeContainer_int_ = LikeContainer_int_

    @property
    def system_Controller34(self):
        return self.__system_Controller34
    @system_Controller34.setter
    def system_Controller34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Post1__system_Controller34", None)
        self.__system_Controller34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "post35"):
                opp_val = getattr(old_value, "post35", None)
                if opp_val == self:
                    setattr(old_value, "post35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "post35"):
                opp_val = getattr(value, "post35", None)
                setattr(value, "post35", self)

    @property
    def hashTags45(self):
        return self.__hashTags45
    @hashTags45.setter
    def hashTags45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Post1__hashTags45", None)
        self.__hashTags45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "post44"):
                    opp_val = getattr(item, "post44", None)
                    
                    if opp_val == self:
                        setattr(item, "post44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "post44"):
                    opp_val = getattr(item, "post44", None)
                    
                    setattr(item, "post44", self)
                    



class Group1:

    def __init__(self, name: str, description: str, admins: User__, members: User__, nMembers: int, posts: str, system_Controller36: "System_Controller" = None):
        self.name = name
        self.description = description
        self.admins = admins
        self.members = members
        self.nMembers = nMembers
        self.posts = posts
        self.system_Controller36 = system_Controller36
        
        pass
    @property
    def members(self):
        return self.__members
    @members.setter
    def members(self, members: User__):
        self.__members = members

    @property
    def posts(self):
        return self.__posts
    @posts.setter
    def posts(self, posts: str):
        self.__posts = posts

    @property
    def nMembers(self):
        return self.__nMembers
    @nMembers.setter
    def nMembers(self, nMembers: int):
        self.__nMembers = nMembers

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
    def admins(self):
        return self.__admins
    @admins.setter
    def admins(self, admins: User__):
        self.__admins = admins

    @property
    def system_Controller36(self):
        return self.__system_Controller36
    @system_Controller36.setter
    def system_Controller36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Group1__system_Controller36", None)
        self.__system_Controller36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "group37"):
                opp_val = getattr(old_value, "group37", None)
                if opp_val == self:
                    setattr(old_value, "group37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "group37"):
                opp_val = getattr(value, "group37", None)
                setattr(value, "group37", self)



class Search:

    pass


class Message:

    def __init__(self, SenderID: int, MessageContent: str, Time: int, ReceiverID: int, Seen: bool, Deliverd: bool, system_Controller40: "System_Controller" = None):
        self.SenderID = SenderID
        self.MessageContent = MessageContent
        self.Time = Time
        self.ReceiverID = ReceiverID
        self.Seen = Seen
        self.Deliverd = Deliverd
        self.system_Controller40 = system_Controller40
        
        pass
    @property
    def ReceiverID(self):
        return self.__ReceiverID
    @ReceiverID.setter
    def ReceiverID(self, ReceiverID: int):
        self.__ReceiverID = ReceiverID

    @property
    def Seen(self):
        return self.__Seen
    @Seen.setter
    def Seen(self, Seen: bool):
        self.__Seen = Seen

    @property
    def MessageContent(self):
        return self.__MessageContent
    @MessageContent.setter
    def MessageContent(self, MessageContent: str):
        self.__MessageContent = MessageContent

    @property
    def Deliverd(self):
        return self.__Deliverd
    @Deliverd.setter
    def Deliverd(self, Deliverd: bool):
        self.__Deliverd = Deliverd

    @property
    def Time(self):
        return self.__Time
    @Time.setter
    def Time(self, Time: int):
        self.__Time = Time

    @property
    def SenderID(self):
        return self.__SenderID
    @SenderID.setter
    def SenderID(self, SenderID: int):
        self.__SenderID = SenderID

    @property
    def system_Controller40(self):
        return self.__system_Controller40
    @system_Controller40.setter
    def system_Controller40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Message__system_Controller40", None)
        self.__system_Controller40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "message41"):
                opp_val = getattr(old_value, "message41", None)
                if opp_val == self:
                    setattr(old_value, "message41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "message41"):
                opp_val = getattr(value, "message41", None)
                setattr(value, "message41", self)



class Page1:

    def __init__(self, name: str, admin: User, fans: User__, description: str, posts: str, nFans: int, system_Controller42: "System_Controller" = None):
        self.name = name
        self.admin = admin
        self.fans = fans
        self.description = description
        self.posts = posts
        self.nFans = nFans
        self.system_Controller42 = system_Controller42
        
        pass
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
    def fans(self):
        return self.__fans
    @fans.setter
    def fans(self, fans: User__):
        self.__fans = fans

    @property
    def admin(self):
        return self.__admin
    @admin.setter
    def admin(self, admin: User):
        self.__admin = admin

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
    def system_Controller42(self):
        return self.__system_Controller42
    @system_Controller42.setter
    def system_Controller42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Page1__system_Controller42", None)
        self.__system_Controller42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "page43"):
                opp_val = getattr(old_value, "page43", None)
                if opp_val == self:
                    setattr(old_value, "page43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "page43"):
                opp_val = getattr(value, "page43", None)
                setattr(value, "page43", self)



class System_Controller:

    def __init__(self, GiveResponse: bool, Database_Connection: bool, post35: "Post1" = None, group37: "Group1" = None, search39: "Search" = None, message41: "Message" = None, page43: "Page1" = None, user_Controller47: "User_Controller" = None):
        self.GiveResponse = GiveResponse
        self.Database_Connection = Database_Connection
        self.post35 = post35
        self.group37 = group37
        self.search39 = search39
        self.message41 = message41
        self.page43 = page43
        self.user_Controller47 = user_Controller47
        
        pass
    @property
    def Database_Connection(self):
        return self.__Database_Connection
    @Database_Connection.setter
    def Database_Connection(self, Database_Connection: bool):
        self.__Database_Connection = Database_Connection

    @property
    def GiveResponse(self):
        return self.__GiveResponse
    @GiveResponse.setter
    def GiveResponse(self, GiveResponse: bool):
        self.__GiveResponse = GiveResponse

    @property
    def search39(self):
        return self.__search39
    @search39.setter
    def search39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System_Controller__search39", None)
        self.__search39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system_Controller38"):
                opp_val = getattr(old_value, "system_Controller38", None)
                if opp_val == self:
                    setattr(old_value, "system_Controller38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system_Controller38"):
                opp_val = getattr(value, "system_Controller38", None)
                setattr(value, "system_Controller38", self)

    @property
    def post35(self):
        return self.__post35
    @post35.setter
    def post35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System_Controller__post35", None)
        self.__post35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system_Controller34"):
                opp_val = getattr(old_value, "system_Controller34", None)
                if opp_val == self:
                    setattr(old_value, "system_Controller34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system_Controller34"):
                opp_val = getattr(value, "system_Controller34", None)
                setattr(value, "system_Controller34", self)

    @property
    def message41(self):
        return self.__message41
    @message41.setter
    def message41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System_Controller__message41", None)
        self.__message41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system_Controller40"):
                opp_val = getattr(old_value, "system_Controller40", None)
                if opp_val == self:
                    setattr(old_value, "system_Controller40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system_Controller40"):
                opp_val = getattr(value, "system_Controller40", None)
                setattr(value, "system_Controller40", self)

    @property
    def group37(self):
        return self.__group37
    @group37.setter
    def group37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System_Controller__group37", None)
        self.__group37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system_Controller36"):
                opp_val = getattr(old_value, "system_Controller36", None)
                if opp_val == self:
                    setattr(old_value, "system_Controller36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system_Controller36"):
                opp_val = getattr(value, "system_Controller36", None)
                setattr(value, "system_Controller36", self)

    @property
    def user_Controller47(self):
        return self.__user_Controller47
    @user_Controller47.setter
    def user_Controller47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System_Controller__user_Controller47", None)
        self.__user_Controller47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system_Controller46"):
                opp_val = getattr(old_value, "system_Controller46", None)
                if opp_val == self:
                    setattr(old_value, "system_Controller46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system_Controller46"):
                opp_val = getattr(value, "system_Controller46", None)
                setattr(value, "system_Controller46", self)

    @property
    def page43(self):
        return self.__page43
    @page43.setter
    def page43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System_Controller__page43", None)
        self.__page43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system_Controller42"):
                opp_val = getattr(old_value, "system_Controller42", None)
                if opp_val == self:
                    setattr(old_value, "system_Controller42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system_Controller42"):
                opp_val = getattr(value, "system_Controller42", None)
                setattr(value, "system_Controller42", self)



class User_Controller:

    pass


class Premium_User:

    pass


class Normal_User1:

    pass


class User1:

    def __init__(self, UserID: int, Full_Name: str, username: str, email: str, Gender: str, password: str, Age: int, pages: str, groups: str, Messages: str, Friends: List_User__Interface, FriendRequests: str, Privacy: str, user_Controller31: "User_Controller" = None, paymentMethod33: "PaymentMethod" = None):
        self.UserID = UserID
        self.Full_Name = Full_Name
        self.username = username
        self.email = email
        self.Gender = Gender
        self.password = password
        self.Age = Age
        self.pages = pages
        self.groups = groups
        self.Messages = Messages
        self.Friends = Friends
        self.FriendRequests = FriendRequests
        self.Privacy = Privacy
        self.user_Controller31 = user_Controller31
        self.paymentMethod33 = paymentMethod33
        
        pass
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def Full_Name(self):
        return self.__Full_Name
    @Full_Name.setter
    def Full_Name(self, Full_Name: str):
        self.__Full_Name = Full_Name

    @property
    def Friends(self):
        return self.__Friends
    @Friends.setter
    def Friends(self, Friends: List_User__Interface):
        self.__Friends = Friends

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def FriendRequests(self):
        return self.__FriendRequests
    @FriendRequests.setter
    def FriendRequests(self, FriendRequests: str):
        self.__FriendRequests = FriendRequests

    @property
    def Privacy(self):
        return self.__Privacy
    @Privacy.setter
    def Privacy(self, Privacy: str):
        self.__Privacy = Privacy

    @property
    def Age(self):
        return self.__Age
    @Age.setter
    def Age(self, Age: int):
        self.__Age = Age

    @property
    def groups(self):
        return self.__groups
    @groups.setter
    def groups(self, groups: str):
        self.__groups = groups

    @property
    def Messages(self):
        return self.__Messages
    @Messages.setter
    def Messages(self, Messages: str):
        self.__Messages = Messages

    @property
    def UserID(self):
        return self.__UserID
    @UserID.setter
    def UserID(self, UserID: int):
        self.__UserID = UserID

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def Gender(self):
        return self.__Gender
    @Gender.setter
    def Gender(self, Gender: str):
        self.__Gender = Gender

    @property
    def pages(self):
        return self.__pages
    @pages.setter
    def pages(self, pages: str):
        self.__pages = pages

    @property
    def user_Controller31(self):
        return self.__user_Controller31
    @user_Controller31.setter
    def user_Controller31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User1__user_Controller31", None)
        self.__user_Controller31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user30"):
                opp_val = getattr(old_value, "user30", None)
                if opp_val == self:
                    setattr(old_value, "user30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user30"):
                opp_val = getattr(value, "user30", None)
                setattr(value, "user30", self)

    @property
    def paymentMethod33(self):
        return self.__paymentMethod33
    @paymentMethod33.setter
    def paymentMethod33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User1__paymentMethod33", None)
        self.__paymentMethod33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user32"):
                opp_val = getattr(old_value, "user32", None)
                if opp_val == self:
                    setattr(old_value, "user32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user32"):
                opp_val = getattr(value, "user32", None)
                setattr(value, "user32", self)



class List_User__Interface:

    pass


class Listeener:

    pass


class Post2:

    pass


class Premuim_User:

    pass


class Normal_User:

    pass


class System_Control:

    pass


class System_Controller_System_Controller:

    def __init__(self, GiveResponse: bool, Database_Connection: bool):
        self.GiveResponse = GiveResponse
        self.Database_Connection = Database_Connection
        
        pass
    @property
    def Database_Connection(self):
        return self.__Database_Connection
    @Database_Connection.setter
    def Database_Connection(self, Database_Connection: bool):
        self.__Database_Connection = Database_Connection

    @property
    def GiveResponse(self):
        return self.__GiveResponse
    @GiveResponse.setter
    def GiveResponse(self, GiveResponse: bool):
        self.__GiveResponse = GiveResponse



class System_Controller_User_Controller:

    pass


class Back_End_API_CreditCard:

    pass


class Back_End_API_PayPal:

    pass


class Back_End_API_PaymentMethod:

    pass


class GUI_GUI:

    pass


class User_Interactions_Search:

    pass


class User_Interactions_Message:

    def __init__(self, SenderID: int, ReceiverID: int, MessageContent: str, Time: int, Seen: bool, Deliverd: bool, user19: "Users_User" = None):
        self.SenderID = SenderID
        self.ReceiverID = ReceiverID
        self.MessageContent = MessageContent
        self.Time = Time
        self.Seen = Seen
        self.Deliverd = Deliverd
        self.user19 = user19
        
        pass
    @property
    def MessageContent(self):
        return self.__MessageContent
    @MessageContent.setter
    def MessageContent(self, MessageContent: str):
        self.__MessageContent = MessageContent

    @property
    def ReceiverID(self):
        return self.__ReceiverID
    @ReceiverID.setter
    def ReceiverID(self, ReceiverID: int):
        self.__ReceiverID = ReceiverID

    @property
    def SenderID(self):
        return self.__SenderID
    @SenderID.setter
    def SenderID(self, SenderID: int):
        self.__SenderID = SenderID

    @property
    def Seen(self):
        return self.__Seen
    @Seen.setter
    def Seen(self, Seen: bool):
        self.__Seen = Seen

    @property
    def Time(self):
        return self.__Time
    @Time.setter
    def Time(self, Time: int):
        self.__Time = Time

    @property
    def Deliverd(self):
        return self.__Deliverd
    @Deliverd.setter
    def Deliverd(self, Deliverd: bool):
        self.__Deliverd = Deliverd

    @property
    def user19(self):
        return self.__user19
    @user19.setter
    def user19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User_Interactions_Message__user19", None)
        self.__user19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "message18"):
                opp_val = getattr(old_value, "message18", None)
                if opp_val == self:
                    setattr(old_value, "message18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "message18"):
                opp_val = getattr(value, "message18", None)
                setattr(value, "message18", self)



class User_Interactions_HashTags:

    def __init__(self, allHashTags: str, post21: "User_Interactions_Post" = None):
        self.allHashTags = allHashTags
        self.post21 = post21
        
        pass
    @property
    def allHashTags(self):
        return self.__allHashTags
    @allHashTags.setter
    def allHashTags(self, allHashTags: str):
        self.__allHashTags = allHashTags

    @property
    def post21(self):
        return self.__post21
    @post21.setter
    def post21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User_Interactions_HashTags__post21", None)
        self.__post21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hashTags20"):
                opp_val = getattr(old_value, "hashTags20", None)
                if opp_val == self:
                    setattr(old_value, "hashTags20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hashTags20"):
                opp_val = getattr(value, "hashTags20", None)
                setattr(value, "hashTags20", self)



class User_Interactions_Post:

    def __init__(self, privateMode: bool, nLikes: int, nComments: int, nShares: int, owner: User, user15: "Users_User" = None, hashTags20: "User_Interactions_HashTags" = None, group23: "User_Interactions_Group" = None, page25: "User_Interactions_Page" = None):
        self.privateMode = privateMode
        self.nLikes = nLikes
        self.nComments = nComments
        self.nShares = nShares
        self.owner = owner
        self.user15 = user15
        self.hashTags20 = hashTags20
        self.group23 = group23
        self.page25 = page25
        
        pass
    @property
    def nShares(self):
        return self.__nShares
    @nShares.setter
    def nShares(self, nShares: int):
        self.__nShares = nShares

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
    def owner(self):
        return self.__owner
    @owner.setter
    def owner(self, owner: User):
        self.__owner = owner

    @property
    def nComments(self):
        return self.__nComments
    @nComments.setter
    def nComments(self, nComments: int):
        self.__nComments = nComments

    @property
    def user15(self):
        return self.__user15
    @user15.setter
    def user15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User_Interactions_Post__user15", None)
        self.__user15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "post14"):
                opp_val = getattr(old_value, "post14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "post14"):
                opp_val = getattr(value, "post14", None)
                if opp_val is None:
                    setattr(value, "post14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hashTags20(self):
        return self.__hashTags20
    @hashTags20.setter
    def hashTags20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User_Interactions_Post__hashTags20", None)
        self.__hashTags20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "post21"):
                opp_val = getattr(old_value, "post21", None)
                if opp_val == self:
                    setattr(old_value, "post21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "post21"):
                opp_val = getattr(value, "post21", None)
                setattr(value, "post21", self)

    @property
    def group23(self):
        return self.__group23
    @group23.setter
    def group23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User_Interactions_Post__group23", None)
        self.__group23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "post22"):
                opp_val = getattr(old_value, "post22", None)
                if opp_val == self:
                    setattr(old_value, "post22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "post22"):
                opp_val = getattr(value, "post22", None)
                setattr(value, "post22", self)

    @property
    def page25(self):
        return self.__page25
    @page25.setter
    def page25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User_Interactions_Post__page25", None)
        self.__page25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "post24"):
                opp_val = getattr(old_value, "post24", None)
                if opp_val == self:
                    setattr(old_value, "post24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "post24"):
                opp_val = getattr(value, "post24", None)
                setattr(value, "post24", self)



class User_Interactions_Group:

    def __init__(self, name: str, description: str, admins: User__, members: User__, nMembers: int, posts: str, user13: set["Users_User"] = None, post22: "User_Interactions_Post" = None):
        self.name = name
        self.description = description
        self.admins = admins
        self.members = members
        self.nMembers = nMembers
        self.posts = posts
        self.user13 = user13 if user13 is not None else set()
        self.post22 = post22
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def user13(self):
        return self.__user13
    @user13.setter
    def user13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User_Interactions_Group__user13", None)
        self.__user13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "group12"):
                    opp_val = getattr(item, "group12", None)
                    
                    if opp_val == self:
                        setattr(item, "group12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "group12"):
                    opp_val = getattr(item, "group12", None)
                    
                    setattr(item, "group12", self)
                    

    @property
    def post22(self):
        return self.__post22
    @post22.setter
    def post22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User_Interactions_Group__post22", None)
        self.__post22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "group23"):
                opp_val = getattr(old_value, "group23", None)
                if opp_val == self:
                    setattr(old_value, "group23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "group23"):
                opp_val = getattr(value, "group23", None)
                setattr(value, "group23", self)



class User_Interactions_Page:

    def __init__(self, posts: str, nFans: int, name: str, admin: User, fans: User__, description: str, user17: set["Users_User"] = None, post24: "User_Interactions_Post" = None):
        self.posts = posts
        self.nFans = nFans
        self.name = name
        self.admin = admin
        self.fans = fans
        self.description = description
        self.user17 = user17 if user17 is not None else set()
        self.post24 = post24
        
        pass
    @property
    def posts(self):
        return self.__posts
    @posts.setter
    def posts(self, posts: str):
        self.__posts = posts

    @property
    def admin(self):
        return self.__admin
    @admin.setter
    def admin(self, admin: User):
        self.__admin = admin

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
    def nFans(self):
        return self.__nFans
    @nFans.setter
    def nFans(self, nFans: int):
        self.__nFans = nFans

    @property
    def fans(self):
        return self.__fans
    @fans.setter
    def fans(self, fans: User__):
        self.__fans = fans

    @property
    def user17(self):
        return self.__user17
    @user17.setter
    def user17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User_Interactions_Page__user17", None)
        self.__user17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "page16"):
                    opp_val = getattr(item, "page16", None)
                    
                    if opp_val == self:
                        setattr(item, "page16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "page16"):
                    opp_val = getattr(item, "page16", None)
                    
                    setattr(item, "page16", self)
                    

    @property
    def post24(self):
        return self.__post24
    @post24.setter
    def post24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User_Interactions_Page__post24", None)
        self.__post24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "page25"):
                opp_val = getattr(old_value, "page25", None)
                if opp_val == self:
                    setattr(old_value, "page25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "page25"):
                opp_val = getattr(value, "page25", None)
                setattr(value, "page25", self)



class Users_Premium_User:

    pass


class Users_Normal_User:

    pass


class Users_User:

    def __init__(self, UserID: int, Full_Name: str, username: str, email: str, Gender: str, password: str, Age: int, pages: str, groups: str, Messages: str, Friends: List_User__Interface, FriendRequests: str, Privacy: str, group12: "User_Interactions_Group" = None, post14: set["User_Interactions_Post"] = None, page16: "User_Interactions_Page" = None, message18: "User_Interactions_Message" = None, search27: "User_Interactions_Search" = None):
        self.UserID = UserID
        self.Full_Name = Full_Name
        self.username = username
        self.email = email
        self.Gender = Gender
        self.password = password
        self.Age = Age
        self.pages = pages
        self.groups = groups
        self.Messages = Messages
        self.Friends = Friends
        self.FriendRequests = FriendRequests
        self.Privacy = Privacy
        self.group12 = group12
        self.post14 = post14 if post14 is not None else set()
        self.page16 = page16
        self.message18 = message18
        self.search27 = search27
        
        pass
    @property
    def FriendRequests(self):
        return self.__FriendRequests
    @FriendRequests.setter
    def FriendRequests(self, FriendRequests: str):
        self.__FriendRequests = FriendRequests

    @property
    def Full_Name(self):
        return self.__Full_Name
    @Full_Name.setter
    def Full_Name(self, Full_Name: str):
        self.__Full_Name = Full_Name

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

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
    def Age(self):
        return self.__Age
    @Age.setter
    def Age(self, Age: int):
        self.__Age = Age

    @property
    def Messages(self):
        return self.__Messages
    @Messages.setter
    def Messages(self, Messages: str):
        self.__Messages = Messages

    @property
    def pages(self):
        return self.__pages
    @pages.setter
    def pages(self, pages: str):
        self.__pages = pages

    @property
    def Privacy(self):
        return self.__Privacy
    @Privacy.setter
    def Privacy(self, Privacy: str):
        self.__Privacy = Privacy

    @property
    def Gender(self):
        return self.__Gender
    @Gender.setter
    def Gender(self, Gender: str):
        self.__Gender = Gender

    @property
    def Friends(self):
        return self.__Friends
    @Friends.setter
    def Friends(self, Friends: List_User__Interface):
        self.__Friends = Friends

    @property
    def UserID(self):
        return self.__UserID
    @UserID.setter
    def UserID(self, UserID: int):
        self.__UserID = UserID

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def message18(self):
        return self.__message18
    @message18.setter
    def message18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Users_User__message18", None)
        self.__message18 = value
        
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

    @property
    def post14(self):
        return self.__post14
    @post14.setter
    def post14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Users_User__post14", None)
        self.__post14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user15"):
                    opp_val = getattr(item, "user15", None)
                    
                    if opp_val == self:
                        setattr(item, "user15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user15"):
                    opp_val = getattr(item, "user15", None)
                    
                    setattr(item, "user15", self)
                    

    @property
    def page16(self):
        return self.__page16
    @page16.setter
    def page16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Users_User__page16", None)
        self.__page16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user17"):
                opp_val = getattr(old_value, "user17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user17"):
                opp_val = getattr(value, "user17", None)
                if opp_val is None:
                    setattr(value, "user17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def search27(self):
        return self.__search27
    @search27.setter
    def search27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Users_User__search27", None)
        self.__search27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user26"):
                opp_val = getattr(old_value, "user26", None)
                if opp_val == self:
                    setattr(old_value, "user26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user26"):
                opp_val = getattr(value, "user26", None)
                setattr(value, "user26", self)

    @property
    def group12(self):
        return self.__group12
    @group12.setter
    def group12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Users_User__group12", None)
        self.__group12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user13"):
                opp_val = getattr(old_value, "user13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user13"):
                opp_val = getattr(value, "user13", None)
                if opp_val is None:
                    setattr(value, "user13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



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

    def __init__(self, name: str, admin: User, fans: User__, description: str, posts: str, nFans: int, post11: "Post" = None, user3: set["User"] = None):
        self.name = name
        self.admin = admin
        self.fans = fans
        self.description = description
        self.posts = posts
        self.nFans = nFans
        self.post11 = post11
        self.user3 = user3 if user3 is not None else set()
        
        pass
    @property
    def admin(self):
        return self.__admin
    @admin.setter
    def admin(self, admin: User):
        self.__admin = admin

    @property
    def nFans(self):
        return self.__nFans
    @nFans.setter
    def nFans(self, nFans: int):
        self.__nFans = nFans

    @property
    def posts(self):
        return self.__posts
    @posts.setter
    def posts(self, posts: str):
        self.__posts = posts

    @property
    def fans(self):
        return self.__fans
    @fans.setter
    def fans(self, fans: User__):
        self.__fans = fans

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
    def nShares(self):
        return self.__nShares
    @nShares.setter
    def nShares(self, nShares: int):
        self.__nShares = nShares

    @property
    def owner(self):
        return self.__owner
    @owner.setter
    def owner(self, owner: User):
        self.__owner = owner

    @property
    def privateMode(self):
        return self.__privateMode
    @privateMode.setter
    def privateMode(self, privateMode: bool):
        self.__privateMode = privateMode

    @property
    def nComments(self):
        return self.__nComments
    @nComments.setter
    def nComments(self, nComments: int):
        self.__nComments = nComments

    @property
    def nLikes(self):
        return self.__nLikes
    @nLikes.setter
    def nLikes(self, nLikes: int):
        self.__nLikes = nLikes

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

    def __init__(self, name: str, description: str, admins: User__, members: User__, nMembers: int, posts: str, post7: "Post" = None, user1: set["User"] = None):
        self.name = name
        self.description = description
        self.admins = admins
        self.members = members
        self.nMembers = nMembers
        self.posts = posts
        self.post7 = post7
        self.user1 = user1 if user1 is not None else set()
        
        pass
    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

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
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def nMembers(self):
        return self.__nMembers
    @nMembers.setter
    def nMembers(self, nMembers: int):
        self.__nMembers = nMembers

    @property
    def members(self):
        return self.__members
    @members.setter
    def members(self, members: User__):
        self.__members = members

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
                    



class User:

    def __init__(self, pages: str, name: str, username: str, email: str, password: str, gender: str, groups: str, post4: "Post" = None, group0: "Group" = None, page2: "Page" = None):
        self.pages = pages
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.gender = gender
        self.groups = groups
        self.post4 = post4
        self.group0 = group0
        self.page2 = page2
        
        pass
    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def groups(self):
        return self.__groups
    @groups.setter
    def groups(self, groups: str):
        self.__groups = groups

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

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

