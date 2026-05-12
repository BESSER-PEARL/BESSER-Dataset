from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class genmymodelreverse_javax_servlet_http_Part_Interface(ABC):

    pass


class genmymodelreverse_java_sql_Connection_Interface(ABC):

    pass


class genmymodelreverse_javax_servlet_ServletResponse_Interface(ABC):

    pass


class genmymodelreverse_javax_servlet_ServletRequest_Interface(ABC):

    pass


class genmymodelreverse_javax_servlet_FilterConfig_Interface(ABC):

    pass


class genmymodelreverse_javax_servlet_FilterChain_Interface(ABC):

    pass


class genmymodelreverse_javax_servlet_Filter_Interface(ABC):

    pass


class genmymodelreverse_javax_servlet_http_HttpServletResponse_Interface(ABC):

    pass


class genmymodelreverse_javax_servlet_http_HttpServletRequest_Interface(ABC):

    pass


class genmymodelreverse_javax_servlet_http_HttpServlet(ABC):

    pass


class genmymodelreverse_javax_servlet_ServletException:

    pass


class genmymodelreverse_java_sql_ResultSet_Interface(ABC):

    pass


class genmymodelreverse_java_sql_Timestamp:

    pass


class genmymodelreverse_java_sql_Time:

    pass


class genmymodelreverse_java_sql_Date:

    pass


class genmymodelreverse_java_text_ParseException:

    pass


class genmymodelreverse_java_io_Reader(ABC):

    pass


class genmymodelreverse_java_io_IOException:

    pass


class file_ProfilePicture:

    def __init__(self, SAVE_DIR: str, tm15: "network_TransactionManager" = None):
        self.SAVE_DIR = SAVE_DIR
        self.tm15 = tm15
        
        pass
    @property
    def SAVE_DIR(self):
        return self.__SAVE_DIR
    @SAVE_DIR.setter
    def SAVE_DIR(self, SAVE_DIR: str):
        self.__SAVE_DIR = SAVE_DIR

    @property
    def tm15(self):
        return self.__tm15
    @tm15.setter
    def tm15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_file_ProfilePicture__tm15", None)
        self.__tm15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profilepicture14"):
                opp_val = getattr(old_value, "profilepicture14", None)
                if opp_val == self:
                    setattr(old_value, "profilepicture14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profilepicture14"):
                opp_val = getattr(value, "profilepicture14", None)
                setattr(value, "profilepicture14", self)



class file_FileUploadHandler:

    def __init__(self, fileName1: str, SAVE_DIR: str):
        self.fileName1 = fileName1
        self.SAVE_DIR = SAVE_DIR
        
        pass
    @property
    def SAVE_DIR(self):
        return self.__SAVE_DIR
    @SAVE_DIR.setter
    def SAVE_DIR(self, SAVE_DIR: str):
        self.__SAVE_DIR = SAVE_DIR

    @property
    def fileName1(self):
        return self.__fileName1
    @fileName1.setter
    def fileName1(self, fileName1: str):
        self.__fileName1 = fileName1



class utility_PostLikes:

    pass


class utility_LikedOrNot:

    pass


class utility_IdDAO:

    pass


class utility_GetTime:

    pass


class utility_FolderOperations:

    pass


class utility_CheckSentiment:

    pass


class utility_Category:

    pass


class utility_CategoriesAPI:

    pass


class network_UtilityPhone:

    pass


class network_UtilityEmail:

    pass


class network_UsersRegistered:

    def __init__(self, serialVersionUID: int, tm39: "network_TransactionManager" = None):
        self.serialVersionUID = serialVersionUID
        self.tm39 = tm39
        
        pass
    @property
    def serialVersionUID(self):
        return self.__serialVersionUID
    @serialVersionUID.setter
    def serialVersionUID(self, serialVersionUID: int):
        self.__serialVersionUID = serialVersionUID

    @property
    def tm39(self):
        return self.__tm39
    @tm39.setter
    def tm39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_network_UsersRegistered__tm39", None)
        self.__tm39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usersregistered38"):
                opp_val = getattr(old_value, "usersregistered38", None)
                if opp_val == self:
                    setattr(old_value, "usersregistered38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usersregistered38"):
                opp_val = getattr(value, "usersregistered38", None)
                setattr(value, "usersregistered38", self)



class network_UserRegistration:

    def __init__(self, serialVersionUID: int, SAVE_DIR: str):
        self.serialVersionUID = serialVersionUID
        self.SAVE_DIR = SAVE_DIR
        
        pass
    @property
    def SAVE_DIR(self):
        return self.__SAVE_DIR
    @SAVE_DIR.setter
    def SAVE_DIR(self, SAVE_DIR: str):
        self.__SAVE_DIR = SAVE_DIR

    @property
    def serialVersionUID(self):
        return self.__serialVersionUID
    @serialVersionUID.setter
    def serialVersionUID(self, serialVersionUID: int):
        self.__serialVersionUID = serialVersionUID



class network_UpdateProfession:

    def __init__(self, serialVersionUID: int):
        self.serialVersionUID = serialVersionUID
        
        pass
    @property
    def serialVersionUID(self):
        return self.__serialVersionUID
    @serialVersionUID.setter
    def serialVersionUID(self, serialVersionUID: int):
        self.__serialVersionUID = serialVersionUID



class network_Unlike:

    def __init__(self, serialVersionUID: int):
        self.serialVersionUID = serialVersionUID
        
        pass
    @property
    def serialVersionUID(self):
        return self.__serialVersionUID
    @serialVersionUID.setter
    def serialVersionUID(self, serialVersionUID: int):
        self.__serialVersionUID = serialVersionUID



class network_Unfriend:

    def __init__(self, serialVersionUID: int):
        self.serialVersionUID = serialVersionUID
        
        pass
    @property
    def serialVersionUID(self):
        return self.__serialVersionUID
    @serialVersionUID.setter
    def serialVersionUID(self, serialVersionUID: int):
        self.__serialVersionUID = serialVersionUID



class network_TransactionManager:

    def __init__(self, con: genmymodelreverse_java_sql_Connection_Interface, friendsdao30: "dao_FriendsDAO" = None, warningdao0: "dao_WarningDAO" = None, profiledao2: "dao_ProfileDAO" = None, iddao4: "utility_IdDAO" = None, accountbandao6: "dao_AccountBanDAO" = None, adultdetectiondao8: "dao_AdultDetectionDAO" = None, insertcommentmess10: "network_InsertCommentMess" = None, imagesdao12: "dao_ImagesDAO" = None, profilepicture14: "file_ProfilePicture" = None, loginprocess16: "network_LoginProcess" = None, commentdao18: "dao_CommentDAO" = None, professiondao20: "dao_ProfessionDAO" = None, friendrequestsdao22: "dao_FriendRequestsDAO" = None, insertmessage24: "network_InsertMessage" = None, insertcomment26: "network_InsertComment" = None, tabledao28: "dao_TableDAO" = None, messagedao32: "dao_MessageDAO" = None, likesdao34: "dao_LikesDAO" = None, accountbandao236: "dao_AccountBanDAO2" = None, usersregistered38: "network_UsersRegistered" = None, userdao40: "dao_UserDAO" = None):
        self.con = con
        self.friendsdao30 = friendsdao30
        self.warningdao0 = warningdao0
        self.profiledao2 = profiledao2
        self.iddao4 = iddao4
        self.accountbandao6 = accountbandao6
        self.adultdetectiondao8 = adultdetectiondao8
        self.insertcommentmess10 = insertcommentmess10
        self.imagesdao12 = imagesdao12
        self.profilepicture14 = profilepicture14
        self.loginprocess16 = loginprocess16
        self.commentdao18 = commentdao18
        self.professiondao20 = professiondao20
        self.friendrequestsdao22 = friendrequestsdao22
        self.insertmessage24 = insertmessage24
        self.insertcomment26 = insertcomment26
        self.tabledao28 = tabledao28
        self.messagedao32 = messagedao32
        self.likesdao34 = likesdao34
        self.accountbandao236 = accountbandao236
        self.usersregistered38 = usersregistered38
        self.userdao40 = userdao40
        
        pass
    @property
    def con(self):
        return self.__con
    @con.setter
    def con(self, con: genmymodelreverse_java_sql_Connection_Interface):
        self.__con = con

    @property
    def usersregistered38(self):
        return self.__usersregistered38
    @usersregistered38.setter
    def usersregistered38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_network_TransactionManager__usersregistered38", None)
        self.__usersregistered38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tm39"):
                opp_val = getattr(old_value, "tm39", None)
                if opp_val == self:
                    setattr(old_value, "tm39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tm39"):
                opp_val = getattr(value, "tm39", None)
                setattr(value, "tm39", self)

    @property
    def tabledao28(self):
        return self.__tabledao28
    @tabledao28.setter
    def tabledao28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_network_TransactionManager__tabledao28", None)
        self.__tabledao28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tm29"):
                opp_val = getattr(old_value, "tm29", None)
                if opp_val == self:
                    setattr(old_value, "tm29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tm29"):
                opp_val = getattr(value, "tm29", None)
                setattr(value, "tm29", self)

    @property
    def adultdetectiondao8(self):
        return self.__adultdetectiondao8
    @adultdetectiondao8.setter
    def adultdetectiondao8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_network_TransactionManager__adultdetectiondao8", None)
        self.__adultdetectiondao8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tm9"):
                opp_val = getattr(old_value, "tm9", None)
                if opp_val == self:
                    setattr(old_value, "tm9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tm9"):
                opp_val = getattr(value, "tm9", None)
                setattr(value, "tm9", self)

    @property
    def commentdao18(self):
        return self.__commentdao18
    @commentdao18.setter
    def commentdao18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_network_TransactionManager__commentdao18", None)
        self.__commentdao18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tm19"):
                opp_val = getattr(old_value, "tm19", None)
                if opp_val == self:
                    setattr(old_value, "tm19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tm19"):
                opp_val = getattr(value, "tm19", None)
                setattr(value, "tm19", self)

    @property
    def professiondao20(self):
        return self.__professiondao20
    @professiondao20.setter
    def professiondao20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_network_TransactionManager__professiondao20", None)
        self.__professiondao20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tm21"):
                opp_val = getattr(old_value, "tm21", None)
                if opp_val == self:
                    setattr(old_value, "tm21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tm21"):
                opp_val = getattr(value, "tm21", None)
                setattr(value, "tm21", self)

    @property
    def accountbandao6(self):
        return self.__accountbandao6
    @accountbandao6.setter
    def accountbandao6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_network_TransactionManager__accountbandao6", None)
        self.__accountbandao6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tm7"):
                opp_val = getattr(old_value, "tm7", None)
                if opp_val == self:
                    setattr(old_value, "tm7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tm7"):
                opp_val = getattr(value, "tm7", None)
                setattr(value, "tm7", self)

    @property
    def loginprocess16(self):
        return self.__loginprocess16
    @loginprocess16.setter
    def loginprocess16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_network_TransactionManager__loginprocess16", None)
        self.__loginprocess16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tm17"):
                opp_val = getattr(old_value, "tm17", None)
                if opp_val == self:
                    setattr(old_value, "tm17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tm17"):
                opp_val = getattr(value, "tm17", None)
                setattr(value, "tm17", self)

    @property
    def insertcommentmess10(self):
        return self.__insertcommentmess10
    @insertcommentmess10.setter
    def insertcommentmess10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_network_TransactionManager__insertcommentmess10", None)
        self.__insertcommentmess10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tm11"):
                opp_val = getattr(old_value, "tm11", None)
                if opp_val == self:
                    setattr(old_value, "tm11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tm11"):
                opp_val = getattr(value, "tm11", None)
                setattr(value, "tm11", self)

    @property
    def likesdao34(self):
        return self.__likesdao34
    @likesdao34.setter
    def likesdao34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_network_TransactionManager__likesdao34", None)
        self.__likesdao34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tm35"):
                opp_val = getattr(old_value, "tm35", None)
                if opp_val == self:
                    setattr(old_value, "tm35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tm35"):
                opp_val = getattr(value, "tm35", None)
                setattr(value, "tm35", self)

    @property
    def accountbandao236(self):
        return self.__accountbandao236
    @accountbandao236.setter
    def accountbandao236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_network_TransactionManager__accountbandao236", None)
        self.__accountbandao236 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tm37"):
                opp_val = getattr(old_value, "tm37", None)
                if opp_val == self:
                    setattr(old_value, "tm37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tm37"):
                opp_val = getattr(value, "tm37", None)
                setattr(value, "tm37", self)

    @property
    def profilepicture14(self):
        return self.__profilepicture14
    @profilepicture14.setter
    def profilepicture14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_network_TransactionManager__profilepicture14", None)
        self.__profilepicture14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tm15"):
                opp_val = getattr(old_value, "tm15", None)
                if opp_val == self:
                    setattr(old_value, "tm15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tm15"):
                opp_val = getattr(value, "tm15", None)
                setattr(value, "tm15", self)

    @property
    def friendrequestsdao22(self):
        return self.__friendrequestsdao22
    @friendrequestsdao22.setter
    def friendrequestsdao22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_network_TransactionManager__friendrequestsdao22", None)
        self.__friendrequestsdao22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tm23"):
                opp_val = getattr(old_value, "tm23", None)
                if opp_val == self:
                    setattr(old_value, "tm23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tm23"):
                opp_val = getattr(value, "tm23", None)
                setattr(value, "tm23", self)

    @property
    def userdao40(self):
        return self.__userdao40
    @userdao40.setter
    def userdao40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_network_TransactionManager__userdao40", None)
        self.__userdao40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tm41"):
                opp_val = getattr(old_value, "tm41", None)
                if opp_val == self:
                    setattr(old_value, "tm41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tm41"):
                opp_val = getattr(value, "tm41", None)
                setattr(value, "tm41", self)

    @property
    def imagesdao12(self):
        return self.__imagesdao12
    @imagesdao12.setter
    def imagesdao12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_network_TransactionManager__imagesdao12", None)
        self.__imagesdao12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tm13"):
                opp_val = getattr(old_value, "tm13", None)
                if opp_val == self:
                    setattr(old_value, "tm13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tm13"):
                opp_val = getattr(value, "tm13", None)
                setattr(value, "tm13", self)

    @property
    def iddao4(self):
        return self.__iddao4
    @iddao4.setter
    def iddao4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_network_TransactionManager__iddao4", None)
        self.__iddao4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tm5"):
                opp_val = getattr(old_value, "tm5", None)
                if opp_val == self:
                    setattr(old_value, "tm5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tm5"):
                opp_val = getattr(value, "tm5", None)
                setattr(value, "tm5", self)

    @property
    def messagedao32(self):
        return self.__messagedao32
    @messagedao32.setter
    def messagedao32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_network_TransactionManager__messagedao32", None)
        self.__messagedao32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tm33"):
                opp_val = getattr(old_value, "tm33", None)
                if opp_val == self:
                    setattr(old_value, "tm33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tm33"):
                opp_val = getattr(value, "tm33", None)
                setattr(value, "tm33", self)

    @property
    def warningdao0(self):
        return self.__warningdao0
    @warningdao0.setter
    def warningdao0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_network_TransactionManager__warningdao0", None)
        self.__warningdao0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tm1"):
                opp_val = getattr(old_value, "tm1", None)
                if opp_val == self:
                    setattr(old_value, "tm1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tm1"):
                opp_val = getattr(value, "tm1", None)
                setattr(value, "tm1", self)

    @property
    def profiledao2(self):
        return self.__profiledao2
    @profiledao2.setter
    def profiledao2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_network_TransactionManager__profiledao2", None)
        self.__profiledao2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tm3"):
                opp_val = getattr(old_value, "tm3", None)
                if opp_val == self:
                    setattr(old_value, "tm3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tm3"):
                opp_val = getattr(value, "tm3", None)
                setattr(value, "tm3", self)

    @property
    def insertmessage24(self):
        return self.__insertmessage24
    @insertmessage24.setter
    def insertmessage24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_network_TransactionManager__insertmessage24", None)
        self.__insertmessage24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tm25"):
                opp_val = getattr(old_value, "tm25", None)
                if opp_val == self:
                    setattr(old_value, "tm25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tm25"):
                opp_val = getattr(value, "tm25", None)
                setattr(value, "tm25", self)

    @property
    def insertcomment26(self):
        return self.__insertcomment26
    @insertcomment26.setter
    def insertcomment26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_network_TransactionManager__insertcomment26", None)
        self.__insertcomment26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tm27"):
                opp_val = getattr(old_value, "tm27", None)
                if opp_val == self:
                    setattr(old_value, "tm27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tm27"):
                opp_val = getattr(value, "tm27", None)
                setattr(value, "tm27", self)

    @property
    def friendsdao30(self):
        return self.__friendsdao30
    @friendsdao30.setter
    def friendsdao30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_network_TransactionManager__friendsdao30", None)
        self.__friendsdao30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tm31"):
                opp_val = getattr(old_value, "tm31", None)
                if opp_val == self:
                    setattr(old_value, "tm31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tm31"):
                opp_val = getattr(value, "tm31", None)
                setattr(value, "tm31", self)



class network_SendRequest:

    def __init__(self, serialVersionUID: int):
        self.serialVersionUID = serialVersionUID
        
        pass
    @property
    def serialVersionUID(self):
        return self.__serialVersionUID
    @serialVersionUID.setter
    def serialVersionUID(self, serialVersionUID: int):
        self.__serialVersionUID = serialVersionUID



class network_RemovePost:

    def __init__(self, serialVersionUID: int):
        self.serialVersionUID = serialVersionUID
        
        pass
    @property
    def serialVersionUID(self):
        return self.__serialVersionUID
    @serialVersionUID.setter
    def serialVersionUID(self, serialVersionUID: int):
        self.__serialVersionUID = serialVersionUID



class network_RemoveMessage:

    def __init__(self, serialVersionUID: int):
        self.serialVersionUID = serialVersionUID
        
        pass
    @property
    def serialVersionUID(self):
        return self.__serialVersionUID
    @serialVersionUID.setter
    def serialVersionUID(self, serialVersionUID: int):
        self.__serialVersionUID = serialVersionUID



class network_RejectRequest:

    def __init__(self, serialVersionUID: int):
        self.serialVersionUID = serialVersionUID
        
        pass
    @property
    def serialVersionUID(self):
        return self.__serialVersionUID
    @serialVersionUID.setter
    def serialVersionUID(self, serialVersionUID: int):
        self.__serialVersionUID = serialVersionUID



class genmymodelreverse_java_lang_StringBuilder:

    pass


class network_NoCacheFilter:

    pass


class network_MessageUnlike:

    def __init__(self, serialVersionUID: int):
        self.serialVersionUID = serialVersionUID
        
        pass
    @property
    def serialVersionUID(self):
        return self.__serialVersionUID
    @serialVersionUID.setter
    def serialVersionUID(self, serialVersionUID: int):
        self.__serialVersionUID = serialVersionUID



class network_MessageLike:

    def __init__(self, serialVersionUID: int):
        self.serialVersionUID = serialVersionUID
        
        pass
    @property
    def serialVersionUID(self):
        return self.__serialVersionUID
    @serialVersionUID.setter
    def serialVersionUID(self, serialVersionUID: int):
        self.__serialVersionUID = serialVersionUID



class network_LogoutServlet:

    pass


class network_LoginProcess:

    def __init__(self, serialVersionUID: int, tm17: "network_TransactionManager" = None):
        self.serialVersionUID = serialVersionUID
        self.tm17 = tm17
        
        pass
    @property
    def serialVersionUID(self):
        return self.__serialVersionUID
    @serialVersionUID.setter
    def serialVersionUID(self, serialVersionUID: int):
        self.__serialVersionUID = serialVersionUID

    @property
    def tm17(self):
        return self.__tm17
    @tm17.setter
    def tm17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_network_LoginProcess__tm17", None)
        self.__tm17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "loginprocess16"):
                opp_val = getattr(old_value, "loginprocess16", None)
                if opp_val == self:
                    setattr(old_value, "loginprocess16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "loginprocess16"):
                opp_val = getattr(value, "loginprocess16", None)
                setattr(value, "loginprocess16", self)



class network_Like:

    def __init__(self, serialVersionUID: int):
        self.serialVersionUID = serialVersionUID
        
        pass
    @property
    def serialVersionUID(self):
        return self.__serialVersionUID
    @serialVersionUID.setter
    def serialVersionUID(self, serialVersionUID: int):
        self.__serialVersionUID = serialVersionUID



class network_InsertMessage:

    def __init__(self, serialVersionUID: int, tm25: "network_TransactionManager" = None):
        self.serialVersionUID = serialVersionUID
        self.tm25 = tm25
        
        pass
    @property
    def serialVersionUID(self):
        return self.__serialVersionUID
    @serialVersionUID.setter
    def serialVersionUID(self, serialVersionUID: int):
        self.__serialVersionUID = serialVersionUID

    @property
    def tm25(self):
        return self.__tm25
    @tm25.setter
    def tm25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_network_InsertMessage__tm25", None)
        self.__tm25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "insertmessage24"):
                opp_val = getattr(old_value, "insertmessage24", None)
                if opp_val == self:
                    setattr(old_value, "insertmessage24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "insertmessage24"):
                opp_val = getattr(value, "insertmessage24", None)
                setattr(value, "insertmessage24", self)



class network_InsertCommentMess:

    def __init__(self, serialVersionUID: int, tm11: "network_TransactionManager" = None):
        self.serialVersionUID = serialVersionUID
        self.tm11 = tm11
        
        pass
    @property
    def serialVersionUID(self):
        return self.__serialVersionUID
    @serialVersionUID.setter
    def serialVersionUID(self, serialVersionUID: int):
        self.__serialVersionUID = serialVersionUID

    @property
    def tm11(self):
        return self.__tm11
    @tm11.setter
    def tm11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_network_InsertCommentMess__tm11", None)
        self.__tm11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "insertcommentmess10"):
                opp_val = getattr(old_value, "insertcommentmess10", None)
                if opp_val == self:
                    setattr(old_value, "insertcommentmess10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "insertcommentmess10"):
                opp_val = getattr(value, "insertcommentmess10", None)
                setattr(value, "insertcommentmess10", self)



class network_InsertComment:

    def __init__(self, serialVersionUID: int, tm27: "network_TransactionManager" = None):
        self.serialVersionUID = serialVersionUID
        self.tm27 = tm27
        
        pass
    @property
    def serialVersionUID(self):
        return self.__serialVersionUID
    @serialVersionUID.setter
    def serialVersionUID(self, serialVersionUID: int):
        self.__serialVersionUID = serialVersionUID

    @property
    def tm27(self):
        return self.__tm27
    @tm27.setter
    def tm27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_network_InsertComment__tm27", None)
        self.__tm27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "insertcomment26"):
                opp_val = getattr(old_value, "insertcomment26", None)
                if opp_val == self:
                    setattr(old_value, "insertcomment26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "insertcomment26"):
                opp_val = getattr(value, "insertcomment26", None)
                setattr(value, "insertcomment26", self)



class network_DeleteMessComment:

    def __init__(self, serialVersionUID: int):
        self.serialVersionUID = serialVersionUID
        
        pass
    @property
    def serialVersionUID(self):
        return self.__serialVersionUID
    @serialVersionUID.setter
    def serialVersionUID(self, serialVersionUID: int):
        self.__serialVersionUID = serialVersionUID



class network_Delete:

    def __init__(self, serialVersionUID: int):
        self.serialVersionUID = serialVersionUID
        
        pass
    @property
    def serialVersionUID(self):
        return self.__serialVersionUID
    @serialVersionUID.setter
    def serialVersionUID(self, serialVersionUID: int):
        self.__serialVersionUID = serialVersionUID



class network_DateTest:

    pass


class network_AcceptRequest:

    def __init__(self, serialVersionUID: int):
        self.serialVersionUID = serialVersionUID
        
        pass
    @property
    def serialVersionUID(self):
        return self.__serialVersionUID
    @serialVersionUID.setter
    def serialVersionUID(self, serialVersionUID: int):
        self.__serialVersionUID = serialVersionUID



class dao_WarningDAO:

    pass


class dao_UserDAO:

    pass


class dao_TableDAO:

    pass


class dao_ProfileDAO:

    pass


class dao_ProfessionDAO:

    pass


class dao_MessageDAO:

    pass


class dao_LikesDAO:

    pass


class dao_ImagesDAO:

    pass


class dao_FriendsDAO:

    pass


class dao_FriendRequestsDAO:

    pass


class dao_CommentDAO:

    pass


class dao_AdultDetectionDAO:

    pass


class dao_AccountBanDAO2:

    pass


class dao_AccountBanDAO:

    pass


class bean_Warning:

    def __init__(self, id: int, emailFId: str, message: str, category: str, time: genmymodelreverse_java_sql_Time, date: genmymodelreverse_java_sql_Date):
        self.id = id
        self.emailFId = emailFId
        self.message = message
        self.category = category
        self.time = time
        self.date = date
        
        pass
    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: genmymodelreverse_java_sql_Date):
        self.__date = date

    @property
    def category(self):
        return self.__category
    @category.setter
    def category(self, category: str):
        self.__category = category

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
    def time(self):
        return self.__time
    @time.setter
    def time(self, time: genmymodelreverse_java_sql_Time):
        self.__time = time

    @property
    def emailFId(self):
        return self.__emailFId
    @emailFId.setter
    def emailFId(self, emailFId: str):
        self.__emailFId = emailFId



class bean_UserInfo:

    def __init__(self, first: str, last: str, password: str, email: str, phone: str, local: str, permanent: str, dob: str, gender: str):
        self.first = first
        self.last = last
        self.password = password
        self.email = email
        self.phone = phone
        self.local = local
        self.permanent = permanent
        self.dob = dob
        self.gender = gender
        
        pass
    @property
    def first(self):
        return self.__first
    @first.setter
    def first(self, first: str):
        self.__first = first

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
    def last(self):
        return self.__last
    @last.setter
    def last(self, last: str):
        self.__last = last

    @property
    def dob(self):
        return self.__dob
    @dob.setter
    def dob(self, dob: str):
        self.__dob = dob

    @property
    def local(self):
        return self.__local
    @local.setter
    def local(self, local: str):
        self.__local = local

    @property
    def permanent(self):
        return self.__permanent
    @permanent.setter
    def permanent(self, permanent: str):
        self.__permanent = permanent

    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone



class bean_TableBean:

    def __init__(self, postId: int, friendEmail: str, displayed: str):
        self.postId = postId
        self.friendEmail = friendEmail
        self.displayed = displayed
        
        pass
    @property
    def friendEmail(self):
        return self.__friendEmail
    @friendEmail.setter
    def friendEmail(self, friendEmail: str):
        self.__friendEmail = friendEmail

    @property
    def displayed(self):
        return self.__displayed
    @displayed.setter
    def displayed(self, displayed: str):
        self.__displayed = displayed

    @property
    def postId(self):
        return self.__postId
    @postId.setter
    def postId(self, postId: int):
        self.__postId = postId



class bean_ProfileInfo:

    def __init__(self, email: str, first: str, last: str, path: str):
        self.email = email
        self.first = first
        self.last = last
        self.path = path
        
        pass
    @property
    def first(self):
        return self.__first
    @first.setter
    def first(self, first: str):
        self.__first = first

    @property
    def last(self):
        return self.__last
    @last.setter
    def last(self, last: str):
        self.__last = last

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def path(self):
        return self.__path
    @path.setter
    def path(self, path: str):
        self.__path = path



class bean_ProfessionBean:

    def __init__(self, email: str, profession: str, qualification: str, workIn: str):
        self.email = email
        self.profession = profession
        self.qualification = qualification
        self.workIn = workIn
        
        pass
    @property
    def profession(self):
        return self.__profession
    @profession.setter
    def profession(self, profession: str):
        self.__profession = profession

    @property
    def qualification(self):
        return self.__qualification
    @qualification.setter
    def qualification(self, qualification: str):
        self.__qualification = qualification

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def workIn(self):
        return self.__workIn
    @workIn.setter
    def workIn(self, workIn: str):
        self.__workIn = workIn



class bean_MessageLikeBean:

    def __init__(self, id: int, emailFId: str, messageFId: int, time: genmymodelreverse_java_sql_Time, date: genmymodelreverse_java_sql_Date):
        self.id = id
        self.emailFId = emailFId
        self.messageFId = messageFId
        self.time = time
        self.date = date
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time: genmymodelreverse_java_sql_Time):
        self.__time = time

    @property
    def messageFId(self):
        return self.__messageFId
    @messageFId.setter
    def messageFId(self, messageFId: int):
        self.__messageFId = messageFId

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: genmymodelreverse_java_sql_Date):
        self.__date = date

    @property
    def emailFId(self):
        return self.__emailFId
    @emailFId.setter
    def emailFId(self, emailFId: str):
        self.__emailFId = emailFId



class bean_MessageCommentBean:

    def __init__(self, status: str, id: int, messageFId: int, emailFId: str, comment: str, time: genmymodelreverse_java_sql_Time, date: genmymodelreverse_java_sql_Date):
        self.status = status
        self.id = id
        self.messageFId = messageFId
        self.emailFId = emailFId
        self.comment = comment
        self.time = time
        self.date = date
        
        pass
    @property
    def emailFId(self):
        return self.__emailFId
    @emailFId.setter
    def emailFId(self, emailFId: str):
        self.__emailFId = emailFId

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: genmymodelreverse_java_sql_Date):
        self.__date = date

    @property
    def comment(self):
        return self.__comment
    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time: genmymodelreverse_java_sql_Time):
        self.__time = time

    @property
    def messageFId(self):
        return self.__messageFId
    @messageFId.setter
    def messageFId(self, messageFId: int):
        self.__messageFId = messageFId

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status



class bean_MessageBean:

    def __init__(self, id: int, emailFId: str, message: str, time: genmymodelreverse_java_sql_Time, date: genmymodelreverse_java_sql_Date, category: str, recFId: str, imageFId: int, status: str):
        self.id = id
        self.emailFId = emailFId
        self.message = message
        self.time = time
        self.date = date
        self.category = category
        self.recFId = recFId
        self.imageFId = imageFId
        self.status = status
        
        pass
    @property
    def message(self):
        return self.__message
    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def recFId(self):
        return self.__recFId
    @recFId.setter
    def recFId(self, recFId: str):
        self.__recFId = recFId

    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time: genmymodelreverse_java_sql_Time):
        self.__time = time

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: genmymodelreverse_java_sql_Date):
        self.__date = date

    @property
    def emailFId(self):
        return self.__emailFId
    @emailFId.setter
    def emailFId(self, emailFId: str):
        self.__emailFId = emailFId

    @property
    def imageFId(self):
        return self.__imageFId
    @imageFId.setter
    def imageFId(self, imageFId: int):
        self.__imageFId = imageFId

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def category(self):
        return self.__category
    @category.setter
    def category(self, category: str):
        self.__category = category



class bean_LikeBean:

    def __init__(self, id: int, emailFId: str, imageFId: int, time: genmymodelreverse_java_sql_Time, date: genmymodelreverse_java_sql_Date):
        self.id = id
        self.emailFId = emailFId
        self.imageFId = imageFId
        self.time = time
        self.date = date
        
        pass
    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time: genmymodelreverse_java_sql_Time):
        self.__time = time

    @property
    def emailFId(self):
        return self.__emailFId
    @emailFId.setter
    def emailFId(self, emailFId: str):
        self.__emailFId = emailFId

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: genmymodelreverse_java_sql_Date):
        self.__date = date

    @property
    def imageFId(self):
        return self.__imageFId
    @imageFId.setter
    def imageFId(self, imageFId: int):
        self.__imageFId = imageFId

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id



class bean_ImageBean:

    def __init__(self, id: int, imageName: str, emailFId: str, time: genmymodelreverse_java_sql_Time, date: genmymodelreverse_java_sql_Date, messageFId: int):
        self.id = id
        self.imageName = imageName
        self.emailFId = emailFId
        self.time = time
        self.date = date
        self.messageFId = messageFId
        
        pass
    @property
    def messageFId(self):
        return self.__messageFId
    @messageFId.setter
    def messageFId(self, messageFId: int):
        self.__messageFId = messageFId

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: genmymodelreverse_java_sql_Date):
        self.__date = date

    @property
    def emailFId(self):
        return self.__emailFId
    @emailFId.setter
    def emailFId(self, emailFId: str):
        self.__emailFId = emailFId

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time: genmymodelreverse_java_sql_Time):
        self.__time = time

    @property
    def imageName(self):
        return self.__imageName
    @imageName.setter
    def imageName(self, imageName: str):
        self.__imageName = imageName



class bean_Friends:

    def __init__(self, email1: str, email2: str):
        self.email1 = email1
        self.email2 = email2
        
        pass
    @property
    def email2(self):
        return self.__email2
    @email2.setter
    def email2(self, email2: str):
        self.__email2 = email2

    @property
    def email1(self):
        return self.__email1
    @email1.setter
    def email1(self, email1: str):
        self.__email1 = email1



class bean_FriendRequest:

    def __init__(self, id: int, email1: str, email2: str, date: genmymodelreverse_java_sql_Timestamp):
        self.id = id
        self.email1 = email1
        self.email2 = email2
        self.date = date
        
        pass
    @property
    def email2(self):
        return self.__email2
    @email2.setter
    def email2(self, email2: str):
        self.__email2 = email2

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def email1(self):
        return self.__email1
    @email1.setter
    def email1(self, email1: str):
        self.__email1 = email1

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: genmymodelreverse_java_sql_Timestamp):
        self.__date = date



class bean_CommentBean:

    def __init__(self, id: int, imageFId: int, emailFId: str, comment: str, time: genmymodelreverse_java_sql_Time, date: genmymodelreverse_java_sql_Date, status: str):
        self.id = id
        self.imageFId = imageFId
        self.emailFId = emailFId
        self.comment = comment
        self.time = time
        self.date = date
        self.status = status
        
        pass
    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time: genmymodelreverse_java_sql_Time):
        self.__time = time

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: genmymodelreverse_java_sql_Date):
        self.__date = date

    @property
    def comment(self):
        return self.__comment
    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def imageFId(self):
        return self.__imageFId
    @imageFId.setter
    def imageFId(self, imageFId: int):
        self.__imageFId = imageFId

    @property
    def emailFId(self):
        return self.__emailFId
    @emailFId.setter
    def emailFId(self, emailFId: str):
        self.__emailFId = emailFId



class bean_CategoryCounts:

    def __init__(self, sportsCount: int, educationCount: int, entertainmentCount: int, historyCount: int, politicsCount: int):
        self.sportsCount = sportsCount
        self.educationCount = educationCount
        self.entertainmentCount = entertainmentCount
        self.historyCount = historyCount
        self.politicsCount = politicsCount
        
        pass
    @property
    def historyCount(self):
        return self.__historyCount
    @historyCount.setter
    def historyCount(self, historyCount: int):
        self.__historyCount = historyCount

    @property
    def sportsCount(self):
        return self.__sportsCount
    @sportsCount.setter
    def sportsCount(self, sportsCount: int):
        self.__sportsCount = sportsCount

    @property
    def educationCount(self):
        return self.__educationCount
    @educationCount.setter
    def educationCount(self, educationCount: int):
        self.__educationCount = educationCount

    @property
    def entertainmentCount(self):
        return self.__entertainmentCount
    @entertainmentCount.setter
    def entertainmentCount(self, entertainmentCount: int):
        self.__entertainmentCount = entertainmentCount

    @property
    def politicsCount(self):
        return self.__politicsCount
    @politicsCount.setter
    def politicsCount(self, politicsCount: int):
        self.__politicsCount = politicsCount



class data_Sentiment:

    pass


class data_PostClass:

    pass


class data_ClassifySentiment:

    pass
