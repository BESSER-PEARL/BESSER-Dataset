from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Class:

    pass


class Another_Login:

    def __init__(self, id: int, user_id: int, facebook_id: int, user35: "Reciever" = None):
        self.id = id
        self.user_id = user_id
        self.facebook_id = facebook_id
        self.user35 = user35
        
        pass
    @property
    def user_id(self):
        return self.__user_id
    @user_id.setter
    def user_id(self, user_id: int):
        self.__user_id = user_id

    @property
    def facebook_id(self):
        return self.__facebook_id
    @facebook_id.setter
    def facebook_id(self, facebook_id: int):
        self.__facebook_id = facebook_id

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def user35(self):
        return self.__user35
    @user35.setter
    def user35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Another_Login__user35", None)
        self.__user35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "another_Login34"):
                opp_val = getattr(old_value, "another_Login34", None)
                if opp_val == self:
                    setattr(old_value, "another_Login34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "another_Login34"):
                opp_val = getattr(value, "another_Login34", None)
                setattr(value, "another_Login34", self)



class Comment:

    def __init__(self, id: int, content: int, post_id: int, user_id: int, creation_date: str, comment_id: int, post14: "Post" = None, user31: "Reciever" = None, comment32: "Comment" = None, comment33: set["Comment"] = None):
        self.id = id
        self.content = content
        self.post_id = post_id
        self.user_id = user_id
        self.creation_date = creation_date
        self.comment_id = comment_id
        self.post14 = post14
        self.user31 = user31
        self.comment32 = comment32
        self.comment33 = comment33 if comment33 is not None else set()
        
        pass
    @property
    def content(self):
        return self.__content
    @content.setter
    def content(self, content: int):
        self.__content = content

    @property
    def post_id(self):
        return self.__post_id
    @post_id.setter
    def post_id(self, post_id: int):
        self.__post_id = post_id

    @property
    def creation_date(self):
        return self.__creation_date
    @creation_date.setter
    def creation_date(self, creation_date: str):
        self.__creation_date = creation_date

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def comment_id(self):
        return self.__comment_id
    @comment_id.setter
    def comment_id(self, comment_id: int):
        self.__comment_id = comment_id

    @property
    def user_id(self):
        return self.__user_id
    @user_id.setter
    def user_id(self, user_id: int):
        self.__user_id = user_id

    @property
    def post14(self):
        return self.__post14
    @post14.setter
    def post14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Comment__post14", None)
        self.__post14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "comment15"):
                opp_val = getattr(old_value, "comment15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "comment15"):
                opp_val = getattr(value, "comment15", None)
                if opp_val is None:
                    setattr(value, "comment15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def comment33(self):
        return self.__comment33
    @comment33.setter
    def comment33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Comment__comment33", None)
        self.__comment33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "comment32"):
                    opp_val = getattr(item, "comment32", None)
                    
                    if opp_val == self:
                        setattr(item, "comment32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "comment32"):
                    opp_val = getattr(item, "comment32", None)
                    
                    setattr(item, "comment32", self)
                    

    @property
    def user31(self):
        return self.__user31
    @user31.setter
    def user31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Comment__user31", None)
        self.__user31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "comment30"):
                opp_val = getattr(old_value, "comment30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "comment30"):
                opp_val = getattr(value, "comment30", None)
                if opp_val is None:
                    setattr(value, "comment30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def comment32(self):
        return self.__comment32
    @comment32.setter
    def comment32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Comment__comment32", None)
        self.__comment32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "comment33"):
                opp_val = getattr(old_value, "comment33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "comment33"):
                opp_val = getattr(value, "comment33", None)
                if opp_val is None:
                    setattr(value, "comment33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Cryptostream:

    def __init__(self, id: int, user_id: int, blocked_user_id: int, user1: "Reciever" = None):
        self.id = id
        self.user_id = user_id
        self.blocked_user_id = blocked_user_id
        self.user1 = user1
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def user_id(self):
        return self.__user_id
    @user_id.setter
    def user_id(self, user_id: int):
        self.__user_id = user_id

    @property
    def blocked_user_id(self):
        return self.__blocked_user_id
    @blocked_user_id.setter
    def blocked_user_id(self, blocked_user_id: int):
        self.__blocked_user_id = blocked_user_id

    @property
    def user1(self):
        return self.__user1
    @user1.setter
    def user1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cryptostream__user1", None)
        self.__user1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blocked_User0"):
                opp_val = getattr(old_value, "blocked_User0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blocked_User0"):
                opp_val = getattr(value, "blocked_User0", None)
                if opp_val is None:
                    setattr(value, "blocked_User0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Following_Hashtag:

    def __init__(self, id: int, user_id: int, hashtag_id: int, hashtag19: "Hashtag" = None, user27: set["Reciever"] = None):
        self.id = id
        self.user_id = user_id
        self.hashtag_id = hashtag_id
        self.hashtag19 = hashtag19
        self.user27 = user27 if user27 is not None else set()
        
        pass
    @property
    def user_id(self):
        return self.__user_id
    @user_id.setter
    def user_id(self, user_id: int):
        self.__user_id = user_id

    @property
    def hashtag_id(self):
        return self.__hashtag_id
    @hashtag_id.setter
    def hashtag_id(self, hashtag_id: int):
        self.__hashtag_id = hashtag_id

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def hashtag19(self):
        return self.__hashtag19
    @hashtag19.setter
    def hashtag19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Following_Hashtag__hashtag19", None)
        self.__hashtag19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "following_Hashtag18"):
                opp_val = getattr(old_value, "following_Hashtag18", None)
                if opp_val == self:
                    setattr(old_value, "following_Hashtag18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "following_Hashtag18"):
                opp_val = getattr(value, "following_Hashtag18", None)
                setattr(value, "following_Hashtag18", self)

    @property
    def user27(self):
        return self.__user27
    @user27.setter
    def user27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Following_Hashtag__user27", None)
        self.__user27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "following_Hashtag26"):
                    opp_val = getattr(item, "following_Hashtag26", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "following_Hashtag26"):
                    opp_val = getattr(item, "following_Hashtag26", None)
                    
                    if opp_val is None:
                        setattr(item, "following_Hashtag26", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Message:

    def __init__(self, id: int, sender_id: int, receiver_id: int, message: str, creation_date: str, date_seen: str, is_deleted: bool, user25: set["Reciever"] = None):
        self.id = id
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.message = message
        self.creation_date = creation_date
        self.date_seen = date_seen
        self.is_deleted = is_deleted
        self.user25 = user25 if user25 is not None else set()
        
        pass
    @property
    def is_deleted(self):
        return self.__is_deleted
    @is_deleted.setter
    def is_deleted(self, is_deleted: bool):
        self.__is_deleted = is_deleted

    @property
    def sender_id(self):
        return self.__sender_id
    @sender_id.setter
    def sender_id(self, sender_id: int):
        self.__sender_id = sender_id

    @property
    def creation_date(self):
        return self.__creation_date
    @creation_date.setter
    def creation_date(self, creation_date: str):
        self.__creation_date = creation_date

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def message(self):
        return self.__message
    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def receiver_id(self):
        return self.__receiver_id
    @receiver_id.setter
    def receiver_id(self, receiver_id: int):
        self.__receiver_id = receiver_id

    @property
    def date_seen(self):
        return self.__date_seen
    @date_seen.setter
    def date_seen(self, date_seen: str):
        self.__date_seen = date_seen

    @property
    def user25(self):
        return self.__user25
    @user25.setter
    def user25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Message__user25", None)
        self.__user25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "message24"):
                    opp_val = getattr(item, "message24", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "message24"):
                    opp_val = getattr(item, "message24", None)
                    
                    if opp_val is None:
                        setattr(item, "message24", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Mention:

    def __init__(self, id: int, post_id: int, user_id: int, user11: "Reciever" = None, post23: "Post" = None):
        self.id = id
        self.post_id = post_id
        self.user_id = user_id
        self.user11 = user11
        self.post23 = post23
        
        pass
    @property
    def user_id(self):
        return self.__user_id
    @user_id.setter
    def user_id(self, user_id: int):
        self.__user_id = user_id

    @property
    def post_id(self):
        return self.__post_id
    @post_id.setter
    def post_id(self, post_id: int):
        self.__post_id = post_id

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def user11(self):
        return self.__user11
    @user11.setter
    def user11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Mention__user11", None)
        self.__user11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mention10"):
                opp_val = getattr(old_value, "mention10", None)
                if opp_val == self:
                    setattr(old_value, "mention10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mention10"):
                opp_val = getattr(value, "mention10", None)
                setattr(value, "mention10", self)

    @property
    def post23(self):
        return self.__post23
    @post23.setter
    def post23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Mention__post23", None)
        self.__post23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mention22"):
                opp_val = getattr(old_value, "mention22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mention22"):
                opp_val = getattr(value, "mention22", None)
                if opp_val is None:
                    setattr(value, "mention22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Like:

    def __init__(self, id: int, post_id: int, user_id: int, date_sent: str, post12: "Post" = None, user29: "Reciever" = None):
        self.id = id
        self.post_id = post_id
        self.user_id = user_id
        self.date_sent = date_sent
        self.post12 = post12
        self.user29 = user29
        
        pass
    @property
    def date_sent(self):
        return self.__date_sent
    @date_sent.setter
    def date_sent(self, date_sent: str):
        self.__date_sent = date_sent

    @property
    def post_id(self):
        return self.__post_id
    @post_id.setter
    def post_id(self, post_id: int):
        self.__post_id = post_id

    @property
    def user_id(self):
        return self.__user_id
    @user_id.setter
    def user_id(self, user_id: int):
        self.__user_id = user_id

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def post12(self):
        return self.__post12
    @post12.setter
    def post12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Like__post12", None)
        self.__post12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "like13"):
                opp_val = getattr(old_value, "like13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "like13"):
                opp_val = getattr(value, "like13", None)
                if opp_val is None:
                    setattr(value, "like13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def user29(self):
        return self.__user29
    @user29.setter
    def user29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Like__user29", None)
        self.__user29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "like28"):
                opp_val = getattr(old_value, "like28", None)
                if opp_val == self:
                    setattr(old_value, "like28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "like28"):
                opp_val = getattr(value, "like28", None)
                setattr(value, "like28", self)



class Hashtag:

    def __init__(self, id: int, tag: str, post16: set["Post"] = None, following_Hashtag18: "Following_Hashtag" = None):
        self.id = id
        self.tag = tag
        self.post16 = post16 if post16 is not None else set()
        self.following_Hashtag18 = following_Hashtag18
        
        pass
    @property
    def tag(self):
        return self.__tag
    @tag.setter
    def tag(self, tag: str):
        self.__tag = tag

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def following_Hashtag18(self):
        return self.__following_Hashtag18
    @following_Hashtag18.setter
    def following_Hashtag18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hashtag__following_Hashtag18", None)
        self.__following_Hashtag18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hashtag19"):
                opp_val = getattr(old_value, "hashtag19", None)
                if opp_val == self:
                    setattr(old_value, "hashtag19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hashtag19"):
                opp_val = getattr(value, "hashtag19", None)
                setattr(value, "hashtag19", self)

    @property
    def post16(self):
        return self.__post16
    @post16.setter
    def post16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hashtag__post16", None)
        self.__post16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hashtag17"):
                    opp_val = getattr(item, "hashtag17", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hashtag17"):
                    opp_val = getattr(item, "hashtag17", None)
                    
                    if opp_val is None:
                        setattr(item, "hashtag17", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Key:

    def __init__(self, id: int, Length: str, Value: str, coordinat_y: int, post20: "Post" = None, sender36: "Sender" = None, reciever38: "Reciever" = None):
        self.id = id
        self.Length = Length
        self.Value = Value
        self.coordinat_y = coordinat_y
        self.post20 = post20
        self.sender36 = sender36
        self.reciever38 = reciever38
        
        pass
    @property
    def coordinat_y(self):
        return self.__coordinat_y
    @coordinat_y.setter
    def coordinat_y(self, coordinat_y: int):
        self.__coordinat_y = coordinat_y

    @property
    def Length(self):
        return self.__Length
    @Length.setter
    def Length(self, Length: str):
        self.__Length = Length

    @property
    def Value(self):
        return self.__Value
    @Value.setter
    def Value(self, Value: str):
        self.__Value = Value

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def sender36(self):
        return self.__sender36
    @sender36.setter
    def sender36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Key__sender36", None)
        self.__sender36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "key37"):
                opp_val = getattr(old_value, "key37", None)
                if opp_val == self:
                    setattr(old_value, "key37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "key37"):
                opp_val = getattr(value, "key37", None)
                setattr(value, "key37", self)

    @property
    def reciever38(self):
        return self.__reciever38
    @reciever38.setter
    def reciever38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Key__reciever38", None)
        self.__reciever38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "key39"):
                opp_val = getattr(old_value, "key39", None)
                if opp_val == self:
                    setattr(old_value, "key39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "key39"):
                opp_val = getattr(value, "key39", None)
                setattr(value, "key39", self)

    @property
    def post20(self):
        return self.__post20
    @post20.setter
    def post20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Key__post20", None)
        self.__post20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "location21"):
                opp_val = getattr(old_value, "location21", None)
                if opp_val == self:
                    setattr(old_value, "location21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "location21"):
                opp_val = getattr(value, "location21", None)
                setattr(value, "location21", self)



class N_Disturb_User:

    def __init__(self, id: int, user_id: int, disturb_user_id: int, user3: "Reciever" = None):
        self.id = id
        self.user_id = user_id
        self.disturb_user_id = disturb_user_id
        self.user3 = user3
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def user_id(self):
        return self.__user_id
    @user_id.setter
    def user_id(self, user_id: int):
        self.__user_id = user_id

    @property
    def disturb_user_id(self):
        return self.__disturb_user_id
    @disturb_user_id.setter
    def disturb_user_id(self, disturb_user_id: int):
        self.__disturb_user_id = disturb_user_id

    @property
    def user3(self):
        return self.__user3
    @user3.setter
    def user3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_N_Disturb_User__user3", None)
        self.__user3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "n_Disturb_User2"):
                opp_val = getattr(old_value, "n_Disturb_User2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "n_Disturb_User2"):
                opp_val = getattr(value, "n_Disturb_User2", None)
                if opp_val is None:
                    setattr(value, "n_Disturb_User2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Post:

    def __init__(self, id: int, text: str, location_id: int, hashtag_id: int, total_like: int, creation_date: str, date_update: str, status: str, like13: set["Like"] = None, comment15: set["Comment"] = None, hashtag17: set["Hashtag"] = None, location21: "Key" = None, mention22: set["Mention"] = None, user8: "Reciever" = None):
        self.id = id
        self.text = text
        self.location_id = location_id
        self.hashtag_id = hashtag_id
        self.total_like = total_like
        self.creation_date = creation_date
        self.date_update = date_update
        self.status = status
        self.like13 = like13 if like13 is not None else set()
        self.comment15 = comment15 if comment15 is not None else set()
        self.hashtag17 = hashtag17 if hashtag17 is not None else set()
        self.location21 = location21
        self.mention22 = mention22 if mention22 is not None else set()
        self.user8 = user8
        
        pass
    @property
    def creation_date(self):
        return self.__creation_date
    @creation_date.setter
    def creation_date(self, creation_date: str):
        self.__creation_date = creation_date

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def date_update(self):
        return self.__date_update
    @date_update.setter
    def date_update(self, date_update: str):
        self.__date_update = date_update

    @property
    def text(self):
        return self.__text
    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def location_id(self):
        return self.__location_id
    @location_id.setter
    def location_id(self, location_id: int):
        self.__location_id = location_id

    @property
    def total_like(self):
        return self.__total_like
    @total_like.setter
    def total_like(self, total_like: int):
        self.__total_like = total_like

    @property
    def hashtag_id(self):
        return self.__hashtag_id
    @hashtag_id.setter
    def hashtag_id(self, hashtag_id: int):
        self.__hashtag_id = hashtag_id

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def user8(self):
        return self.__user8
    @user8.setter
    def user8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Post__user8", None)
        self.__user8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "post9"):
                opp_val = getattr(old_value, "post9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "post9"):
                opp_val = getattr(value, "post9", None)
                if opp_val is None:
                    setattr(value, "post9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def comment15(self):
        return self.__comment15
    @comment15.setter
    def comment15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Post__comment15", None)
        self.__comment15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "post14"):
                    opp_val = getattr(item, "post14", None)
                    
                    if opp_val == self:
                        setattr(item, "post14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "post14"):
                    opp_val = getattr(item, "post14", None)
                    
                    setattr(item, "post14", self)
                    

    @property
    def hashtag17(self):
        return self.__hashtag17
    @hashtag17.setter
    def hashtag17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Post__hashtag17", None)
        self.__hashtag17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "post16"):
                    opp_val = getattr(item, "post16", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "post16"):
                    opp_val = getattr(item, "post16", None)
                    
                    if opp_val is None:
                        setattr(item, "post16", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def location21(self):
        return self.__location21
    @location21.setter
    def location21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Post__location21", None)
        self.__location21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "post20"):
                opp_val = getattr(old_value, "post20", None)
                if opp_val == self:
                    setattr(old_value, "post20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "post20"):
                opp_val = getattr(value, "post20", None)
                setattr(value, "post20", self)

    @property
    def like13(self):
        return self.__like13
    @like13.setter
    def like13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Post__like13", None)
        self.__like13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "post12"):
                    opp_val = getattr(item, "post12", None)
                    
                    if opp_val == self:
                        setattr(item, "post12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "post12"):
                    opp_val = getattr(item, "post12", None)
                    
                    setattr(item, "post12", self)
                    

    @property
    def mention22(self):
        return self.__mention22
    @mention22.setter
    def mention22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Post__mention22", None)
        self.__mention22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "post23"):
                    opp_val = getattr(item, "post23", None)
                    
                    if opp_val == self:
                        setattr(item, "post23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "post23"):
                    opp_val = getattr(item, "post23", None)
                    
                    setattr(item, "post23", self)
                    



class Sender:

    def __init__(self, id: int, user_id: int, following_id: int, status: str, creation_date: str, key37: "Key" = None, user7: set["Reciever"] = None):
        self.id = id
        self.user_id = user_id
        self.following_id = following_id
        self.status = status
        self.creation_date = creation_date
        self.key37 = key37
        self.user7 = user7 if user7 is not None else set()
        
        pass
    @property
    def user_id(self):
        return self.__user_id
    @user_id.setter
    def user_id(self, user_id: int):
        self.__user_id = user_id

    @property
    def creation_date(self):
        return self.__creation_date
    @creation_date.setter
    def creation_date(self, creation_date: str):
        self.__creation_date = creation_date

    @property
    def following_id(self):
        return self.__following_id
    @following_id.setter
    def following_id(self, following_id: int):
        self.__following_id = following_id

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def user7(self):
        return self.__user7
    @user7.setter
    def user7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sender__user7", None)
        self.__user7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "following6"):
                    opp_val = getattr(item, "following6", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "following6"):
                    opp_val = getattr(item, "following6", None)
                    
                    if opp_val is None:
                        setattr(item, "following6", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def key37(self):
        return self.__key37
    @key37.setter
    def key37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sender__key37", None)
        self.__key37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sender36"):
                opp_val = getattr(old_value, "sender36", None)
                if opp_val == self:
                    setattr(old_value, "sender36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sender36"):
                opp_val = getattr(value, "sender36", None)
                setattr(value, "sender36", self)



class Principal:

    def __init__(self, id: int, user_id: int, followers_id: int, status: str, creation_date: str, user5: set["Reciever"] = None, reciever40: "Reciever" = None):
        self.id = id
        self.user_id = user_id
        self.followers_id = followers_id
        self.status = status
        self.creation_date = creation_date
        self.user5 = user5 if user5 is not None else set()
        self.reciever40 = reciever40
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def creation_date(self):
        return self.__creation_date
    @creation_date.setter
    def creation_date(self, creation_date: str):
        self.__creation_date = creation_date

    @property
    def followers_id(self):
        return self.__followers_id
    @followers_id.setter
    def followers_id(self, followers_id: int):
        self.__followers_id = followers_id

    @property
    def user_id(self):
        return self.__user_id
    @user_id.setter
    def user_id(self, user_id: int):
        self.__user_id = user_id

    @property
    def user5(self):
        return self.__user5
    @user5.setter
    def user5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Principal__user5", None)
        self.__user5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "followers4"):
                    opp_val = getattr(item, "followers4", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "followers4"):
                    opp_val = getattr(item, "followers4", None)
                    
                    if opp_val is None:
                        setattr(item, "followers4", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def reciever40(self):
        return self.__reciever40
    @reciever40.setter
    def reciever40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Principal__reciever40", None)
        self.__reciever40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "principal41"):
                opp_val = getattr(old_value, "principal41", None)
                if opp_val == self:
                    setattr(old_value, "principal41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "principal41"):
                opp_val = getattr(value, "principal41", None)
                setattr(value, "principal41", self)



class Reciever:

    def __init__(self, user_id: int, id: int, name: str, surname: str, username: str, mail: str, password: str, phone: str, is_private: bool, is_active: bool, is_admin: bool, mention10: "Mention" = None, message24: set["Message"] = None, following_Hashtag26: set["Following_Hashtag"] = None, like28: "Like" = None, comment30: set["Comment"] = None, another_Login34: "Another_Login" = None, blocked_User0: set["Cryptostream"] = None, n_Disturb_User2: set["N_Disturb_User"] = None, followers4: set["Principal"] = None, following6: set["Sender"] = None, post9: set["Post"] = None, key39: "Key" = None, principal41: "Principal" = None):
        self.user_id = user_id
        self.id = id
        self.name = name
        self.surname = surname
        self.username = username
        self.mail = mail
        self.password = password
        self.phone = phone
        self.is_private = is_private
        self.is_active = is_active
        self.is_admin = is_admin
        self.mention10 = mention10
        self.message24 = message24 if message24 is not None else set()
        self.following_Hashtag26 = following_Hashtag26 if following_Hashtag26 is not None else set()
        self.like28 = like28
        self.comment30 = comment30 if comment30 is not None else set()
        self.another_Login34 = another_Login34
        self.blocked_User0 = blocked_User0 if blocked_User0 is not None else set()
        self.n_Disturb_User2 = n_Disturb_User2 if n_Disturb_User2 is not None else set()
        self.followers4 = followers4 if followers4 is not None else set()
        self.following6 = following6 if following6 is not None else set()
        self.post9 = post9 if post9 is not None else set()
        self.key39 = key39
        self.principal41 = principal41
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def surname(self):
        return self.__surname
    @surname.setter
    def surname(self, surname: str):
        self.__surname = surname

    @property
    def is_active(self):
        return self.__is_active
    @is_active.setter
    def is_active(self, is_active: bool):
        self.__is_active = is_active

    @property
    def user_id(self):
        return self.__user_id
    @user_id.setter
    def user_id(self, user_id: int):
        self.__user_id = user_id

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def mail(self):
        return self.__mail
    @mail.setter
    def mail(self, mail: str):
        self.__mail = mail

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def is_private(self):
        return self.__is_private
    @is_private.setter
    def is_private(self, is_private: bool):
        self.__is_private = is_private

    @property
    def is_admin(self):
        return self.__is_admin
    @is_admin.setter
    def is_admin(self, is_admin: bool):
        self.__is_admin = is_admin

    @property
    def followers4(self):
        return self.__followers4
    @followers4.setter
    def followers4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Reciever__followers4", None)
        self.__followers4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user5"):
                    opp_val = getattr(item, "user5", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user5"):
                    opp_val = getattr(item, "user5", None)
                    
                    if opp_val is None:
                        setattr(item, "user5", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def following_Hashtag26(self):
        return self.__following_Hashtag26
    @following_Hashtag26.setter
    def following_Hashtag26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Reciever__following_Hashtag26", None)
        self.__following_Hashtag26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user27"):
                    opp_val = getattr(item, "user27", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user27"):
                    opp_val = getattr(item, "user27", None)
                    
                    if opp_val is None:
                        setattr(item, "user27", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def another_Login34(self):
        return self.__another_Login34
    @another_Login34.setter
    def another_Login34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Reciever__another_Login34", None)
        self.__another_Login34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user35"):
                opp_val = getattr(old_value, "user35", None)
                if opp_val == self:
                    setattr(old_value, "user35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user35"):
                opp_val = getattr(value, "user35", None)
                setattr(value, "user35", self)

    @property
    def n_Disturb_User2(self):
        return self.__n_Disturb_User2
    @n_Disturb_User2.setter
    def n_Disturb_User2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Reciever__n_Disturb_User2", None)
        self.__n_Disturb_User2 = value if value is not None else set()
        
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
    def following6(self):
        return self.__following6
    @following6.setter
    def following6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Reciever__following6", None)
        self.__following6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user7"):
                    opp_val = getattr(item, "user7", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user7"):
                    opp_val = getattr(item, "user7", None)
                    
                    if opp_val is None:
                        setattr(item, "user7", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def principal41(self):
        return self.__principal41
    @principal41.setter
    def principal41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Reciever__principal41", None)
        self.__principal41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reciever40"):
                opp_val = getattr(old_value, "reciever40", None)
                if opp_val == self:
                    setattr(old_value, "reciever40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reciever40"):
                opp_val = getattr(value, "reciever40", None)
                setattr(value, "reciever40", self)

    @property
    def like28(self):
        return self.__like28
    @like28.setter
    def like28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Reciever__like28", None)
        self.__like28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user29"):
                opp_val = getattr(old_value, "user29", None)
                if opp_val == self:
                    setattr(old_value, "user29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user29"):
                opp_val = getattr(value, "user29", None)
                setattr(value, "user29", self)

    @property
    def message24(self):
        return self.__message24
    @message24.setter
    def message24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Reciever__message24", None)
        self.__message24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user25"):
                    opp_val = getattr(item, "user25", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user25"):
                    opp_val = getattr(item, "user25", None)
                    
                    if opp_val is None:
                        setattr(item, "user25", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def key39(self):
        return self.__key39
    @key39.setter
    def key39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Reciever__key39", None)
        self.__key39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reciever38"):
                opp_val = getattr(old_value, "reciever38", None)
                if opp_val == self:
                    setattr(old_value, "reciever38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reciever38"):
                opp_val = getattr(value, "reciever38", None)
                setattr(value, "reciever38", self)

    @property
    def blocked_User0(self):
        return self.__blocked_User0
    @blocked_User0.setter
    def blocked_User0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Reciever__blocked_User0", None)
        self.__blocked_User0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user1"):
                    opp_val = getattr(item, "user1", None)
                    
                    if opp_val == self:
                        setattr(item, "user1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user1"):
                    opp_val = getattr(item, "user1", None)
                    
                    setattr(item, "user1", self)
                    

    @property
    def comment30(self):
        return self.__comment30
    @comment30.setter
    def comment30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Reciever__comment30", None)
        self.__comment30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user31"):
                    opp_val = getattr(item, "user31", None)
                    
                    if opp_val == self:
                        setattr(item, "user31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user31"):
                    opp_val = getattr(item, "user31", None)
                    
                    setattr(item, "user31", self)
                    

    @property
    def post9(self):
        return self.__post9
    @post9.setter
    def post9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Reciever__post9", None)
        self.__post9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user8"):
                    opp_val = getattr(item, "user8", None)
                    
                    if opp_val == self:
                        setattr(item, "user8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user8"):
                    opp_val = getattr(item, "user8", None)
                    
                    setattr(item, "user8", self)
                    

    @property
    def mention10(self):
        return self.__mention10
    @mention10.setter
    def mention10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Reciever__mention10", None)
        self.__mention10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user11"):
                opp_val = getattr(old_value, "user11", None)
                if opp_val == self:
                    setattr(old_value, "user11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user11"):
                opp_val = getattr(value, "user11", None)
                setattr(value, "user11", self)

