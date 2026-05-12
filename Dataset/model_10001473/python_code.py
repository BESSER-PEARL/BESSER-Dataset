from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Invitation:

    pass


class Tag:

    pass


class CommentTopic:

    pass


class Topic:

    pass


class Group:

    pass


class Message:

    pass


class Vote:

    def __init__(self, tipo: bool, post5: "Post" = None, comment7: "Comment" = None, topic13: "Topic" = None):
        self.tipo = tipo
        self.post5 = post5
        self.comment7 = comment7
        self.topic13 = topic13
        
        pass
    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self, tipo: bool):
        self.__tipo = tipo

    @property
    def comment7(self):
        return self.__comment7
    @comment7.setter
    def comment7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Vote__comment7", None)
        self.__comment7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vote6"):
                opp_val = getattr(old_value, "vote6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vote6"):
                opp_val = getattr(value, "vote6", None)
                if opp_val is None:
                    setattr(value, "vote6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def post5(self):
        return self.__post5
    @post5.setter
    def post5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Vote__post5", None)
        self.__post5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vote4"):
                opp_val = getattr(old_value, "vote4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vote4"):
                opp_val = getattr(value, "vote4", None)
                if opp_val is None:
                    setattr(value, "vote4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def topic13(self):
        return self.__topic13
    @topic13.setter
    def topic13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Vote__topic13", None)
        self.__topic13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vote12"):
                opp_val = getattr(old_value, "vote12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vote12"):
                opp_val = getattr(value, "vote12", None)
                if opp_val is None:
                    setattr(value, "vote12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Comment:

    def __init__(self, userName: str, comment: str, date: str, vote6: set["Vote"] = None, post15: "Post" = None):
        self.userName = userName
        self.comment = comment
        self.date = date
        self.vote6 = vote6 if vote6 is not None else set()
        self.post15 = post15
        
        pass
    @property
    def comment(self):
        return self.__comment
    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def userName(self):
        return self.__userName
    @userName.setter
    def userName(self, userName: str):
        self.__userName = userName

    @property
    def vote6(self):
        return self.__vote6
    @vote6.setter
    def vote6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Comment__vote6", None)
        self.__vote6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "comment7"):
                    opp_val = getattr(item, "comment7", None)
                    
                    if opp_val == self:
                        setattr(item, "comment7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "comment7"):
                    opp_val = getattr(item, "comment7", None)
                    
                    setattr(item, "comment7", self)
                    

    @property
    def post15(self):
        return self.__post15
    @post15.setter
    def post15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Comment__post15", None)
        self.__post15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "comment14"):
                opp_val = getattr(old_value, "comment14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "comment14"):
                opp_val = getattr(value, "comment14", None)
                if opp_val is None:
                    setattr(value, "comment14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Post:

    def __init__(self, userName: str, content: str, Date: str, user3: "User" = None, vote4: set["Vote"] = None, comment14: set["Comment"] = None):
        self.userName = userName
        self.content = content
        self.Date = Date
        self.user3 = user3
        self.vote4 = vote4 if vote4 is not None else set()
        self.comment14 = comment14 if comment14 is not None else set()
        
        pass
    @property
    def userName(self):
        return self.__userName
    @userName.setter
    def userName(self, userName: str):
        self.__userName = userName

    @property
    def content(self):
        return self.__content
    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: str):
        self.__Date = Date

    @property
    def user3(self):
        return self.__user3
    @user3.setter
    def user3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Post__user3", None)
        self.__user3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "post2"):
                opp_val = getattr(old_value, "post2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "post2"):
                opp_val = getattr(value, "post2", None)
                if opp_val is None:
                    setattr(value, "post2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vote4(self):
        return self.__vote4
    @vote4.setter
    def vote4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Post__vote4", None)
        self.__vote4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "post5"):
                    opp_val = getattr(item, "post5", None)
                    
                    if opp_val == self:
                        setattr(item, "post5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "post5"):
                    opp_val = getattr(item, "post5", None)
                    
                    setattr(item, "post5", self)
                    

    @property
    def comment14(self):
        return self.__comment14
    @comment14.setter
    def comment14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Post__comment14", None)
        self.__comment14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "post15"):
                    opp_val = getattr(item, "post15", None)
                    
                    if opp_val == self:
                        setattr(item, "post15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "post15"):
                    opp_val = getattr(item, "post15", None)
                    
                    setattr(item, "post15", self)
                    



class Rol:

    def __init__(self, nombre: str, user0: set["User"] = None):
        self.nombre = nombre
        self.user0 = user0 if user0 is not None else set()
        
        pass
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def user0(self):
        return self.__user0
    @user0.setter
    def user0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Rol__user0", None)
        self.__user0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rol1"):
                    opp_val = getattr(item, "rol1", None)
                    
                    if opp_val == self:
                        setattr(item, "rol1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rol1"):
                    opp_val = getattr(item, "rol1", None)
                    
                    setattr(item, "rol1", self)
                    



class User:

    def __init__(self, userName: str, email: str, password: str, rol1: "Rol" = None, post2: set["Post"] = None, message8: set["Message"] = None, group11: set["Group"] = None, user20: "User" = None, friends21: set["User"] = None, invitation22: set["Invitation"] = None):
        self.userName = userName
        self.email = email
        self.password = password
        self.rol1 = rol1
        self.post2 = post2 if post2 is not None else set()
        self.message8 = message8 if message8 is not None else set()
        self.group11 = group11 if group11 is not None else set()
        self.user20 = user20
        self.friends21 = friends21 if friends21 is not None else set()
        self.invitation22 = invitation22 if invitation22 is not None else set()
        
        pass
    @property
    def userName(self):
        return self.__userName
    @userName.setter
    def userName(self, userName: str):
        self.__userName = userName

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def message8(self):
        return self.__message8
    @message8.setter
    def message8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__message8", None)
        self.__message8 = value if value is not None else set()
        
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
                    

    @property
    def friends21(self):
        return self.__friends21
    @friends21.setter
    def friends21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__friends21", None)
        self.__friends21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user20"):
                    opp_val = getattr(item, "user20", None)
                    
                    if opp_val == self:
                        setattr(item, "user20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user20"):
                    opp_val = getattr(item, "user20", None)
                    
                    setattr(item, "user20", self)
                    

    @property
    def invitation22(self):
        return self.__invitation22
    @invitation22.setter
    def invitation22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__invitation22", None)
        self.__invitation22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user23"):
                    opp_val = getattr(item, "user23", None)
                    
                    if opp_val == self:
                        setattr(item, "user23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user23"):
                    opp_val = getattr(item, "user23", None)
                    
                    setattr(item, "user23", self)
                    

    @property
    def user20(self):
        return self.__user20
    @user20.setter
    def user20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__user20", None)
        self.__user20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "friends21"):
                opp_val = getattr(old_value, "friends21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "friends21"):
                opp_val = getattr(value, "friends21", None)
                if opp_val is None:
                    setattr(value, "friends21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def group11(self):
        return self.__group11
    @group11.setter
    def group11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__group11", None)
        self.__group11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user10"):
                    opp_val = getattr(item, "user10", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user10"):
                    opp_val = getattr(item, "user10", None)
                    
                    if opp_val is None:
                        setattr(item, "user10", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

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
    def rol1(self):
        return self.__rol1
    @rol1.setter
    def rol1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__rol1", None)
        self.__rol1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user0"):
                opp_val = getattr(old_value, "user0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user0"):
                opp_val = getattr(value, "user0", None)
                if opp_val is None:
                    setattr(value, "user0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

