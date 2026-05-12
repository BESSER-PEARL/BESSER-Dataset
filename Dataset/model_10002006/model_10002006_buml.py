####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
data_ClassifySentiment = Class(name="data_ClassifySentiment")
data_PostClass = Class(name="data_PostClass")
data_Sentiment = Class(name="data_Sentiment")
bean_CategoryCounts = Class(name="bean_CategoryCounts")
bean_CommentBean = Class(name="bean_CommentBean")
bean_FriendRequest = Class(name="bean_FriendRequest")
bean_Friends = Class(name="bean_Friends")
bean_ImageBean = Class(name="bean_ImageBean")
bean_LikeBean = Class(name="bean_LikeBean")
bean_MessageBean = Class(name="bean_MessageBean")
bean_MessageCommentBean = Class(name="bean_MessageCommentBean")
bean_MessageLikeBean = Class(name="bean_MessageLikeBean")
bean_ProfessionBean = Class(name="bean_ProfessionBean")
bean_ProfileInfo = Class(name="bean_ProfileInfo")
bean_TableBean = Class(name="bean_TableBean")
bean_UserInfo = Class(name="bean_UserInfo")
bean_Warning = Class(name="bean_Warning")
dao_AccountBanDAO = Class(name="dao_AccountBanDAO")
dao_AccountBanDAO2 = Class(name="dao_AccountBanDAO2")
dao_AdultDetectionDAO = Class(name="dao_AdultDetectionDAO")
dao_CommentDAO = Class(name="dao_CommentDAO")
dao_FriendRequestsDAO = Class(name="dao_FriendRequestsDAO")
dao_FriendsDAO = Class(name="dao_FriendsDAO")
dao_ImagesDAO = Class(name="dao_ImagesDAO")
dao_LikesDAO = Class(name="dao_LikesDAO")
dao_MessageDAO = Class(name="dao_MessageDAO")
dao_ProfessionDAO = Class(name="dao_ProfessionDAO")
dao_ProfileDAO = Class(name="dao_ProfileDAO")
dao_TableDAO = Class(name="dao_TableDAO")
dao_UserDAO = Class(name="dao_UserDAO")
dao_WarningDAO = Class(name="dao_WarningDAO")
network_AcceptRequest = Class(name="network_AcceptRequest")
network_DateTest = Class(name="network_DateTest")
network_Delete = Class(name="network_Delete")
network_DeleteMessComment = Class(name="network_DeleteMessComment")
network_InsertComment = Class(name="network_InsertComment")
network_InsertCommentMess = Class(name="network_InsertCommentMess")
network_InsertMessage = Class(name="network_InsertMessage")
network_Like = Class(name="network_Like")
network_LoginProcess = Class(name="network_LoginProcess")
network_LogoutServlet = Class(name="network_LogoutServlet")
network_MessageLike = Class(name="network_MessageLike")
network_MessageUnlike = Class(name="network_MessageUnlike")
network_NoCacheFilter = Class(name="network_NoCacheFilter")
genmymodelreverse_java_lang_StringBuilder = Class(name="genmymodelreverse_java_lang_StringBuilder")
network_RejectRequest = Class(name="network_RejectRequest")
network_RemoveMessage = Class(name="network_RemoveMessage")
network_RemovePost = Class(name="network_RemovePost")
network_SendRequest = Class(name="network_SendRequest")
network_TransactionManager = Class(name="network_TransactionManager")
network_Unfriend = Class(name="network_Unfriend")
network_Unlike = Class(name="network_Unlike")
network_UpdateProfession = Class(name="network_UpdateProfession")
network_UserRegistration = Class(name="network_UserRegistration")
network_UsersRegistered = Class(name="network_UsersRegistered")
network_UtilityEmail = Class(name="network_UtilityEmail")
network_UtilityPhone = Class(name="network_UtilityPhone")
utility_CategoriesAPI = Class(name="utility_CategoriesAPI")
utility_Category = Class(name="utility_Category")
utility_CheckSentiment = Class(name="utility_CheckSentiment")
utility_FolderOperations = Class(name="utility_FolderOperations")
utility_GetTime = Class(name="utility_GetTime")
utility_IdDAO = Class(name="utility_IdDAO")
utility_LikedOrNot = Class(name="utility_LikedOrNot")
utility_PostLikes = Class(name="utility_PostLikes")
file_FileUploadHandler = Class(name="file_FileUploadHandler")
file_ProfilePicture = Class(name="file_ProfilePicture")
genmymodelreverse_java_io_IOException = Class(name="genmymodelreverse_java_io_IOException")
genmymodelreverse_java_io_Reader = Class(name="genmymodelreverse_java_io_Reader", is_abstract=True)
genmymodelreverse_java_text_ParseException = Class(name="genmymodelreverse_java_text_ParseException")
genmymodelreverse_java_sql_Date = Class(name="genmymodelreverse_java_sql_Date")
genmymodelreverse_java_sql_Time = Class(name="genmymodelreverse_java_sql_Time")
genmymodelreverse_java_sql_Timestamp = Class(name="genmymodelreverse_java_sql_Timestamp")
genmymodelreverse_java_sql_ResultSet_Interface = Class(name="genmymodelreverse_java_sql_ResultSet_Interface", is_abstract=True)
genmymodelreverse_javax_servlet_ServletException = Class(name="genmymodelreverse_javax_servlet_ServletException")
genmymodelreverse_javax_servlet_http_HttpServlet = Class(name="genmymodelreverse_javax_servlet_http_HttpServlet", is_abstract=True)
genmymodelreverse_javax_servlet_http_HttpServletRequest_Interface = Class(name="genmymodelreverse_javax_servlet_http_HttpServletRequest_Interface", is_abstract=True)
genmymodelreverse_javax_servlet_http_HttpServletResponse_Interface = Class(name="genmymodelreverse_javax_servlet_http_HttpServletResponse_Interface", is_abstract=True)
genmymodelreverse_javax_servlet_Filter_Interface = Class(name="genmymodelreverse_javax_servlet_Filter_Interface", is_abstract=True)
genmymodelreverse_javax_servlet_FilterChain_Interface = Class(name="genmymodelreverse_javax_servlet_FilterChain_Interface", is_abstract=True)
genmymodelreverse_javax_servlet_FilterConfig_Interface = Class(name="genmymodelreverse_javax_servlet_FilterConfig_Interface", is_abstract=True)
genmymodelreverse_javax_servlet_ServletRequest_Interface = Class(name="genmymodelreverse_javax_servlet_ServletRequest_Interface", is_abstract=True)
genmymodelreverse_javax_servlet_ServletResponse_Interface = Class(name="genmymodelreverse_javax_servlet_ServletResponse_Interface", is_abstract=True)
genmymodelreverse_java_sql_Connection_Interface = Class(name="genmymodelreverse_java_sql_Connection_Interface", is_abstract=True)
genmymodelreverse_javax_servlet_http_Part_Interface = Class(name="genmymodelreverse_javax_servlet_http_Part_Interface", is_abstract=True)

# data_ClassifySentiment class attributes and methods

# data_PostClass class attributes and methods

# data_Sentiment class attributes and methods

# bean_CategoryCounts class attributes and methods
bean_CategoryCounts_sportsCount: Property = Property(name="sportsCount", type=IntegerType)
bean_CategoryCounts_educationCount: Property = Property(name="educationCount", type=IntegerType)
bean_CategoryCounts_entertainmentCount: Property = Property(name="entertainmentCount", type=IntegerType)
bean_CategoryCounts_historyCount: Property = Property(name="historyCount", type=IntegerType)
bean_CategoryCounts_politicsCount: Property = Property(name="politicsCount", type=IntegerType)
bean_CategoryCounts.attributes={bean_CategoryCounts_entertainmentCount, bean_CategoryCounts_politicsCount, bean_CategoryCounts_educationCount, bean_CategoryCounts_historyCount, bean_CategoryCounts_sportsCount}

# bean_CommentBean class attributes and methods
bean_CommentBean_id: Property = Property(name="id", type=IntegerType)
bean_CommentBean_imageFId: Property = Property(name="imageFId", type=IntegerType)
bean_CommentBean_emailFId: Property = Property(name="emailFId", type=StringType)
bean_CommentBean_comment: Property = Property(name="comment", type=StringType)
bean_CommentBean_time: Property = Property(name="time", type=genmymodelreverse_java_sql_Time)
bean_CommentBean_date: Property = Property(name="date", type=genmymodelreverse_java_sql_Date)
bean_CommentBean_status: Property = Property(name="status", type=StringType)
bean_CommentBean.attributes={bean_CommentBean_time, bean_CommentBean_imageFId, bean_CommentBean_status, bean_CommentBean_comment, bean_CommentBean_id, bean_CommentBean_date, bean_CommentBean_emailFId}

# bean_FriendRequest class attributes and methods
bean_FriendRequest_id: Property = Property(name="id", type=IntegerType)
bean_FriendRequest_email1: Property = Property(name="email1", type=StringType)
bean_FriendRequest_email2: Property = Property(name="email2", type=StringType)
bean_FriendRequest_date: Property = Property(name="date", type=genmymodelreverse_java_sql_Timestamp)
bean_FriendRequest.attributes={bean_FriendRequest_email2, bean_FriendRequest_date, bean_FriendRequest_id, bean_FriendRequest_email1}

# bean_Friends class attributes and methods
bean_Friends_email1: Property = Property(name="email1", type=StringType)
bean_Friends_email2: Property = Property(name="email2", type=StringType)
bean_Friends.attributes={bean_Friends_email1, bean_Friends_email2}

# bean_ImageBean class attributes and methods
bean_ImageBean_id: Property = Property(name="id", type=IntegerType)
bean_ImageBean_imageName: Property = Property(name="imageName", type=StringType)
bean_ImageBean_emailFId: Property = Property(name="emailFId", type=StringType)
bean_ImageBean_time: Property = Property(name="time", type=genmymodelreverse_java_sql_Time)
bean_ImageBean_date: Property = Property(name="date", type=genmymodelreverse_java_sql_Date)
bean_ImageBean_messageFId: Property = Property(name="messageFId", type=IntegerType)
bean_ImageBean.attributes={bean_ImageBean_messageFId, bean_ImageBean_time, bean_ImageBean_id, bean_ImageBean_emailFId, bean_ImageBean_date, bean_ImageBean_imageName}

# bean_LikeBean class attributes and methods
bean_LikeBean_id: Property = Property(name="id", type=IntegerType)
bean_LikeBean_emailFId: Property = Property(name="emailFId", type=StringType)
bean_LikeBean_imageFId: Property = Property(name="imageFId", type=IntegerType)
bean_LikeBean_time: Property = Property(name="time", type=genmymodelreverse_java_sql_Time)
bean_LikeBean_date: Property = Property(name="date", type=genmymodelreverse_java_sql_Date)
bean_LikeBean.attributes={bean_LikeBean_date, bean_LikeBean_emailFId, bean_LikeBean_time, bean_LikeBean_id, bean_LikeBean_imageFId}

# bean_MessageBean class attributes and methods
bean_MessageBean_id: Property = Property(name="id", type=IntegerType)
bean_MessageBean_emailFId: Property = Property(name="emailFId", type=StringType)
bean_MessageBean_message: Property = Property(name="message", type=StringType)
bean_MessageBean_time: Property = Property(name="time", type=genmymodelreverse_java_sql_Time)
bean_MessageBean_date: Property = Property(name="date", type=genmymodelreverse_java_sql_Date)
bean_MessageBean_category: Property = Property(name="category", type=StringType)
bean_MessageBean_recFId: Property = Property(name="recFId", type=StringType)
bean_MessageBean_imageFId: Property = Property(name="imageFId", type=IntegerType)
bean_MessageBean_status: Property = Property(name="status", type=StringType)
bean_MessageBean.attributes={bean_MessageBean_category, bean_MessageBean_imageFId, bean_MessageBean_emailFId, bean_MessageBean_status, bean_MessageBean_date, bean_MessageBean_message, bean_MessageBean_id, bean_MessageBean_time, bean_MessageBean_recFId}

# bean_MessageCommentBean class attributes and methods
bean_MessageCommentBean_id: Property = Property(name="id", type=IntegerType)
bean_MessageCommentBean_messageFId: Property = Property(name="messageFId", type=IntegerType)
bean_MessageCommentBean_emailFId: Property = Property(name="emailFId", type=StringType)
bean_MessageCommentBean_comment: Property = Property(name="comment", type=StringType)
bean_MessageCommentBean_time: Property = Property(name="time", type=genmymodelreverse_java_sql_Time)
bean_MessageCommentBean_date: Property = Property(name="date", type=genmymodelreverse_java_sql_Date)
bean_MessageCommentBean_status: Property = Property(name="status", type=StringType)
bean_MessageCommentBean.attributes={bean_MessageCommentBean_id, bean_MessageCommentBean_comment, bean_MessageCommentBean_status, bean_MessageCommentBean_emailFId, bean_MessageCommentBean_messageFId, bean_MessageCommentBean_time, bean_MessageCommentBean_date}

# bean_MessageLikeBean class attributes and methods
bean_MessageLikeBean_id: Property = Property(name="id", type=IntegerType)
bean_MessageLikeBean_emailFId: Property = Property(name="emailFId", type=StringType)
bean_MessageLikeBean_messageFId: Property = Property(name="messageFId", type=IntegerType)
bean_MessageLikeBean_time: Property = Property(name="time", type=genmymodelreverse_java_sql_Time)
bean_MessageLikeBean_date: Property = Property(name="date", type=genmymodelreverse_java_sql_Date)
bean_MessageLikeBean.attributes={bean_MessageLikeBean_date, bean_MessageLikeBean_id, bean_MessageLikeBean_messageFId, bean_MessageLikeBean_time, bean_MessageLikeBean_emailFId}

# bean_ProfessionBean class attributes and methods
bean_ProfessionBean_email: Property = Property(name="email", type=StringType)
bean_ProfessionBean_profession: Property = Property(name="profession", type=StringType)
bean_ProfessionBean_qualification: Property = Property(name="qualification", type=StringType)
bean_ProfessionBean_workIn: Property = Property(name="workIn", type=StringType)
bean_ProfessionBean.attributes={bean_ProfessionBean_qualification, bean_ProfessionBean_workIn, bean_ProfessionBean_profession, bean_ProfessionBean_email}

# bean_ProfileInfo class attributes and methods
bean_ProfileInfo_email: Property = Property(name="email", type=StringType)
bean_ProfileInfo_first: Property = Property(name="first", type=StringType)
bean_ProfileInfo_last: Property = Property(name="last", type=StringType)
bean_ProfileInfo_path: Property = Property(name="path", type=StringType)
bean_ProfileInfo.attributes={bean_ProfileInfo_last, bean_ProfileInfo_path, bean_ProfileInfo_email, bean_ProfileInfo_first}

# bean_TableBean class attributes and methods
bean_TableBean_postId: Property = Property(name="postId", type=IntegerType)
bean_TableBean_friendEmail: Property = Property(name="friendEmail", type=StringType)
bean_TableBean_displayed: Property = Property(name="displayed", type=StringType)
bean_TableBean.attributes={bean_TableBean_postId, bean_TableBean_displayed, bean_TableBean_friendEmail}

# bean_UserInfo class attributes and methods
bean_UserInfo_first: Property = Property(name="first", type=StringType)
bean_UserInfo_last: Property = Property(name="last", type=StringType)
bean_UserInfo_password: Property = Property(name="password", type=StringType)
bean_UserInfo_email: Property = Property(name="email", type=StringType)
bean_UserInfo_phone: Property = Property(name="phone", type=StringType)
bean_UserInfo_local: Property = Property(name="local", type=StringType)
bean_UserInfo_permanent: Property = Property(name="permanent", type=StringType)
bean_UserInfo_dob: Property = Property(name="dob", type=StringType)
bean_UserInfo_gender: Property = Property(name="gender", type=StringType)
bean_UserInfo.attributes={bean_UserInfo_local, bean_UserInfo_phone, bean_UserInfo_last, bean_UserInfo_gender, bean_UserInfo_password, bean_UserInfo_permanent, bean_UserInfo_dob, bean_UserInfo_first, bean_UserInfo_email}

# bean_Warning class attributes and methods
bean_Warning_id: Property = Property(name="id", type=IntegerType)
bean_Warning_emailFId: Property = Property(name="emailFId", type=StringType)
bean_Warning_message: Property = Property(name="message", type=StringType)
bean_Warning_category: Property = Property(name="category", type=StringType)
bean_Warning_time: Property = Property(name="time", type=genmymodelreverse_java_sql_Time)
bean_Warning_date: Property = Property(name="date", type=genmymodelreverse_java_sql_Date)
bean_Warning.attributes={bean_Warning_emailFId, bean_Warning_time, bean_Warning_message, bean_Warning_category, bean_Warning_date, bean_Warning_id}

# dao_AccountBanDAO class attributes and methods

# dao_AccountBanDAO2 class attributes and methods

# dao_AdultDetectionDAO class attributes and methods

# dao_CommentDAO class attributes and methods

# dao_FriendRequestsDAO class attributes and methods

# dao_FriendsDAO class attributes and methods

# dao_ImagesDAO class attributes and methods

# dao_LikesDAO class attributes and methods

# dao_MessageDAO class attributes and methods

# dao_ProfessionDAO class attributes and methods

# dao_ProfileDAO class attributes and methods

# dao_TableDAO class attributes and methods

# dao_UserDAO class attributes and methods

# dao_WarningDAO class attributes and methods

# network_AcceptRequest class attributes and methods
network_AcceptRequest_serialVersionUID: Property = Property(name="serialVersionUID", type=IntegerType)
network_AcceptRequest.attributes={network_AcceptRequest_serialVersionUID}

# network_DateTest class attributes and methods

# network_Delete class attributes and methods
network_Delete_serialVersionUID: Property = Property(name="serialVersionUID", type=IntegerType)
network_Delete.attributes={network_Delete_serialVersionUID}

# network_DeleteMessComment class attributes and methods
network_DeleteMessComment_serialVersionUID: Property = Property(name="serialVersionUID", type=IntegerType)
network_DeleteMessComment.attributes={network_DeleteMessComment_serialVersionUID}

# network_InsertComment class attributes and methods
network_InsertComment_serialVersionUID: Property = Property(name="serialVersionUID", type=IntegerType)
network_InsertComment.attributes={network_InsertComment_serialVersionUID}

# network_InsertCommentMess class attributes and methods
network_InsertCommentMess_serialVersionUID: Property = Property(name="serialVersionUID", type=IntegerType)
network_InsertCommentMess.attributes={network_InsertCommentMess_serialVersionUID}

# network_InsertMessage class attributes and methods
network_InsertMessage_serialVersionUID: Property = Property(name="serialVersionUID", type=IntegerType)
network_InsertMessage.attributes={network_InsertMessage_serialVersionUID}

# network_Like class attributes and methods
network_Like_serialVersionUID: Property = Property(name="serialVersionUID", type=IntegerType)
network_Like.attributes={network_Like_serialVersionUID}

# network_LoginProcess class attributes and methods
network_LoginProcess_serialVersionUID: Property = Property(name="serialVersionUID", type=IntegerType)
network_LoginProcess.attributes={network_LoginProcess_serialVersionUID}

# network_LogoutServlet class attributes and methods

# network_MessageLike class attributes and methods
network_MessageLike_serialVersionUID: Property = Property(name="serialVersionUID", type=IntegerType)
network_MessageLike.attributes={network_MessageLike_serialVersionUID}

# network_MessageUnlike class attributes and methods
network_MessageUnlike_serialVersionUID: Property = Property(name="serialVersionUID", type=IntegerType)
network_MessageUnlike.attributes={network_MessageUnlike_serialVersionUID}

# network_NoCacheFilter class attributes and methods

# genmymodelreverse_java_lang_StringBuilder class attributes and methods

# network_RejectRequest class attributes and methods
network_RejectRequest_serialVersionUID: Property = Property(name="serialVersionUID", type=IntegerType)
network_RejectRequest.attributes={network_RejectRequest_serialVersionUID}

# network_RemoveMessage class attributes and methods
network_RemoveMessage_serialVersionUID: Property = Property(name="serialVersionUID", type=IntegerType)
network_RemoveMessage.attributes={network_RemoveMessage_serialVersionUID}

# network_RemovePost class attributes and methods
network_RemovePost_serialVersionUID: Property = Property(name="serialVersionUID", type=IntegerType)
network_RemovePost.attributes={network_RemovePost_serialVersionUID}

# network_SendRequest class attributes and methods
network_SendRequest_serialVersionUID: Property = Property(name="serialVersionUID", type=IntegerType)
network_SendRequest.attributes={network_SendRequest_serialVersionUID}

# network_TransactionManager class attributes and methods
network_TransactionManager_con: Property = Property(name="con", type=genmymodelreverse_java_sql_Connection_Interface)
network_TransactionManager.attributes={network_TransactionManager_con}

# network_Unfriend class attributes and methods
network_Unfriend_serialVersionUID: Property = Property(name="serialVersionUID", type=IntegerType)
network_Unfriend.attributes={network_Unfriend_serialVersionUID}

# network_Unlike class attributes and methods
network_Unlike_serialVersionUID: Property = Property(name="serialVersionUID", type=IntegerType)
network_Unlike.attributes={network_Unlike_serialVersionUID}

# network_UpdateProfession class attributes and methods
network_UpdateProfession_serialVersionUID: Property = Property(name="serialVersionUID", type=IntegerType)
network_UpdateProfession.attributes={network_UpdateProfession_serialVersionUID}

# network_UserRegistration class attributes and methods
network_UserRegistration_serialVersionUID: Property = Property(name="serialVersionUID", type=IntegerType)
network_UserRegistration_SAVE_DIR: Property = Property(name="SAVE_DIR", type=StringType)
network_UserRegistration.attributes={network_UserRegistration_SAVE_DIR, network_UserRegistration_serialVersionUID}

# network_UsersRegistered class attributes and methods
network_UsersRegistered_serialVersionUID: Property = Property(name="serialVersionUID", type=IntegerType)
network_UsersRegistered.attributes={network_UsersRegistered_serialVersionUID}

# network_UtilityEmail class attributes and methods

# network_UtilityPhone class attributes and methods

# utility_CategoriesAPI class attributes and methods

# utility_Category class attributes and methods

# utility_CheckSentiment class attributes and methods

# utility_FolderOperations class attributes and methods

# utility_GetTime class attributes and methods

# utility_IdDAO class attributes and methods

# utility_LikedOrNot class attributes and methods

# utility_PostLikes class attributes and methods

# file_FileUploadHandler class attributes and methods
file_FileUploadHandler_fileName1: Property = Property(name="fileName1", type=StringType)
file_FileUploadHandler_SAVE_DIR: Property = Property(name="SAVE_DIR", type=StringType)
file_FileUploadHandler.attributes={file_FileUploadHandler_SAVE_DIR, file_FileUploadHandler_fileName1}

# file_ProfilePicture class attributes and methods
file_ProfilePicture_SAVE_DIR: Property = Property(name="SAVE_DIR", type=StringType)
file_ProfilePicture.attributes={file_ProfilePicture_SAVE_DIR}

# genmymodelreverse_java_io_IOException class attributes and methods

# genmymodelreverse_java_io_Reader class attributes and methods

# genmymodelreverse_java_text_ParseException class attributes and methods

# genmymodelreverse_java_sql_Date class attributes and methods

# genmymodelreverse_java_sql_Time class attributes and methods

# genmymodelreverse_java_sql_Timestamp class attributes and methods

# genmymodelreverse_java_sql_ResultSet_Interface class attributes and methods

# genmymodelreverse_javax_servlet_ServletException class attributes and methods

# genmymodelreverse_javax_servlet_http_HttpServlet class attributes and methods

# genmymodelreverse_javax_servlet_http_HttpServletRequest_Interface class attributes and methods

# genmymodelreverse_javax_servlet_http_HttpServletResponse_Interface class attributes and methods

# genmymodelreverse_javax_servlet_Filter_Interface class attributes and methods

# genmymodelreverse_javax_servlet_FilterChain_Interface class attributes and methods

# genmymodelreverse_javax_servlet_FilterConfig_Interface class attributes and methods

# genmymodelreverse_javax_servlet_ServletRequest_Interface class attributes and methods

# genmymodelreverse_javax_servlet_ServletResponse_Interface class attributes and methods

# genmymodelreverse_java_sql_Connection_Interface class attributes and methods

# genmymodelreverse_javax_servlet_http_Part_Interface class attributes and methods

# Relationships
tm_WarningDAO_TransactionManager_16: BinaryAssociation = BinaryAssociation(
    name="tm_WarningDAO_TransactionManager_16",
    ends={
        Property(name="warningdao0", type=dao_WarningDAO, multiplicity=Multiplicity(0, 1)),
        Property(name="tm1", type=network_TransactionManager, multiplicity=Multiplicity(0, 1))
    }
)
tm_ProfileDAO_TransactionManager_5: BinaryAssociation = BinaryAssociation(
    name="tm_ProfileDAO_TransactionManager_5",
    ends={
        Property(name="profiledao2", type=dao_ProfileDAO, multiplicity=Multiplicity(0, 1)),
        Property(name="tm3", type=network_TransactionManager, multiplicity=Multiplicity(0, 1))
    }
)
tm_IdDAO_TransactionManager_6: BinaryAssociation = BinaryAssociation(
    name="tm_IdDAO_TransactionManager_6",
    ends={
        Property(name="iddao4", type=utility_IdDAO, multiplicity=Multiplicity(0, 1)),
        Property(name="tm5", type=network_TransactionManager, multiplicity=Multiplicity(0, 1))
    }
)
tm_AccountBanDAO_TransactionManager_19: BinaryAssociation = BinaryAssociation(
    name="tm_AccountBanDAO_TransactionManager_19",
    ends={
        Property(name="accountbandao6", type=dao_AccountBanDAO, multiplicity=Multiplicity(0, 1)),
        Property(name="tm7", type=network_TransactionManager, multiplicity=Multiplicity(0, 1))
    }
)
tm_AdultDetectionDAO_TransactionManager_4: BinaryAssociation = BinaryAssociation(
    name="tm_AdultDetectionDAO_TransactionManager_4",
    ends={
        Property(name="adultdetectiondao8", type=dao_AdultDetectionDAO, multiplicity=Multiplicity(0, 1)),
        Property(name="tm9", type=network_TransactionManager, multiplicity=Multiplicity(0, 1))
    }
)
tm_InsertCommentMess_TransactionManager_15: BinaryAssociation = BinaryAssociation(
    name="tm_InsertCommentMess_TransactionManager_15",
    ends={
        Property(name="insertcommentmess10", type=network_InsertCommentMess, multiplicity=Multiplicity(0, 1)),
        Property(name="tm11", type=network_TransactionManager, multiplicity=Multiplicity(0, 1))
    }
)
tm_ImagesDAO_TransactionManager_10: BinaryAssociation = BinaryAssociation(
    name="tm_ImagesDAO_TransactionManager_10",
    ends={
        Property(name="imagesdao12", type=dao_ImagesDAO, multiplicity=Multiplicity(0, 1)),
        Property(name="tm13", type=network_TransactionManager, multiplicity=Multiplicity(0, 1))
    }
)
tm_ProfilePicture_TransactionManager_0: BinaryAssociation = BinaryAssociation(
    name="tm_ProfilePicture_TransactionManager_0",
    ends={
        Property(name="profilepicture14", type=file_ProfilePicture, multiplicity=Multiplicity(0, 1)),
        Property(name="tm15", type=network_TransactionManager, multiplicity=Multiplicity(0, 1))
    }
)
tm_LoginProcess_TransactionManager_7: BinaryAssociation = BinaryAssociation(
    name="tm_LoginProcess_TransactionManager_7",
    ends={
        Property(name="loginprocess16", type=network_LoginProcess, multiplicity=Multiplicity(0, 1)),
        Property(name="tm17", type=network_TransactionManager, multiplicity=Multiplicity(0, 1))
    }
)
tm_CommentDAO_TransactionManager_2: BinaryAssociation = BinaryAssociation(
    name="tm_CommentDAO_TransactionManager_2",
    ends={
        Property(name="commentdao18", type=dao_CommentDAO, multiplicity=Multiplicity(0, 1)),
        Property(name="tm19", type=network_TransactionManager, multiplicity=Multiplicity(0, 1))
    }
)
tm_ProfessionDAO_TransactionManager_13: BinaryAssociation = BinaryAssociation(
    name="tm_ProfessionDAO_TransactionManager_13",
    ends={
        Property(name="professiondao20", type=dao_ProfessionDAO, multiplicity=Multiplicity(0, 1)),
        Property(name="tm21", type=network_TransactionManager, multiplicity=Multiplicity(0, 1))
    }
)
tm_FriendRequestsDAO_TransactionManager_9: BinaryAssociation = BinaryAssociation(
    name="tm_FriendRequestsDAO_TransactionManager_9",
    ends={
        Property(name="friendrequestsdao22", type=dao_FriendRequestsDAO, multiplicity=Multiplicity(0, 1)),
        Property(name="tm23", type=network_TransactionManager, multiplicity=Multiplicity(0, 1))
    }
)
tm_InsertMessage_TransactionManager_12: BinaryAssociation = BinaryAssociation(
    name="tm_InsertMessage_TransactionManager_12",
    ends={
        Property(name="insertmessage24", type=network_InsertMessage, multiplicity=Multiplicity(0, 1)),
        Property(name="tm25", type=network_TransactionManager, multiplicity=Multiplicity(0, 1))
    }
)
tm_InsertComment_TransactionManager_18: BinaryAssociation = BinaryAssociation(
    name="tm_InsertComment_TransactionManager_18",
    ends={
        Property(name="insertcomment26", type=network_InsertComment, multiplicity=Multiplicity(0, 1)),
        Property(name="tm27", type=network_TransactionManager, multiplicity=Multiplicity(0, 1))
    }
)
tm_TableDAO_TransactionManager_3: BinaryAssociation = BinaryAssociation(
    name="tm_TableDAO_TransactionManager_3",
    ends={
        Property(name="tabledao28", type=dao_TableDAO, multiplicity=Multiplicity(0, 1)),
        Property(name="tm29", type=network_TransactionManager, multiplicity=Multiplicity(0, 1))
    }
)
tm_FriendsDAO_TransactionManager_1: BinaryAssociation = BinaryAssociation(
    name="tm_FriendsDAO_TransactionManager_1",
    ends={
        Property(name="friendsdao30", type=dao_FriendsDAO, multiplicity=Multiplicity(0, 1)),
        Property(name="tm31", type=network_TransactionManager, multiplicity=Multiplicity(0, 1))
    }
)
tm_MessageDAO_TransactionManager_11: BinaryAssociation = BinaryAssociation(
    name="tm_MessageDAO_TransactionManager_11",
    ends={
        Property(name="messagedao32", type=dao_MessageDAO, multiplicity=Multiplicity(0, 1)),
        Property(name="tm33", type=network_TransactionManager, multiplicity=Multiplicity(0, 1))
    }
)
tm_LikesDAO_TransactionManager_20: BinaryAssociation = BinaryAssociation(
    name="tm_LikesDAO_TransactionManager_20",
    ends={
        Property(name="likesdao34", type=dao_LikesDAO, multiplicity=Multiplicity(0, 1)),
        Property(name="tm35", type=network_TransactionManager, multiplicity=Multiplicity(0, 1))
    }
)
tm_AccountBanDAO2_TransactionManager_14: BinaryAssociation = BinaryAssociation(
    name="tm_AccountBanDAO2_TransactionManager_14",
    ends={
        Property(name="accountbandao236", type=dao_AccountBanDAO2, multiplicity=Multiplicity(0, 1)),
        Property(name="tm37", type=network_TransactionManager, multiplicity=Multiplicity(0, 1))
    }
)
tm_UsersRegistered_TransactionManager_8: BinaryAssociation = BinaryAssociation(
    name="tm_UsersRegistered_TransactionManager_8",
    ends={
        Property(name="usersregistered38", type=network_UsersRegistered, multiplicity=Multiplicity(0, 1)),
        Property(name="tm39", type=network_TransactionManager, multiplicity=Multiplicity(0, 1))
    }
)
tm_UserDAO_TransactionManager_17: BinaryAssociation = BinaryAssociation(
    name="tm_UserDAO_TransactionManager_17",
    ends={
        Property(name="userdao40", type=dao_UserDAO, multiplicity=Multiplicity(0, 1)),
        Property(name="tm41", type=network_TransactionManager, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_iqBtwK3gEemHYc7DDM2g2A",
    types={data_ClassifySentiment, data_PostClass, data_Sentiment, bean_CategoryCounts, bean_CommentBean, bean_FriendRequest, bean_Friends, bean_ImageBean, bean_LikeBean, bean_MessageBean, bean_MessageCommentBean, bean_MessageLikeBean, bean_ProfessionBean, bean_ProfileInfo, bean_TableBean, bean_UserInfo, bean_Warning, dao_AccountBanDAO, dao_AccountBanDAO2, dao_AdultDetectionDAO, dao_CommentDAO, dao_FriendRequestsDAO, dao_FriendsDAO, dao_ImagesDAO, dao_LikesDAO, dao_MessageDAO, dao_ProfessionDAO, dao_ProfileDAO, dao_TableDAO, dao_UserDAO, dao_WarningDAO, network_AcceptRequest, network_DateTest, network_Delete, network_DeleteMessComment, network_InsertComment, network_InsertCommentMess, network_InsertMessage, network_Like, network_LoginProcess, network_LogoutServlet, network_MessageLike, network_MessageUnlike, network_NoCacheFilter, genmymodelreverse_java_lang_StringBuilder, network_RejectRequest, network_RemoveMessage, network_RemovePost, network_SendRequest, network_TransactionManager, network_Unfriend, network_Unlike, network_UpdateProfession, network_UserRegistration, network_UsersRegistered, network_UtilityEmail, network_UtilityPhone, utility_CategoriesAPI, utility_Category, utility_CheckSentiment, utility_FolderOperations, utility_GetTime, utility_IdDAO, utility_LikedOrNot, utility_PostLikes, file_FileUploadHandler, file_ProfilePicture, genmymodelreverse_java_io_IOException, genmymodelreverse_java_io_Reader, genmymodelreverse_java_text_ParseException, genmymodelreverse_java_sql_Date, genmymodelreverse_java_sql_Time, genmymodelreverse_java_sql_Timestamp, genmymodelreverse_java_sql_ResultSet_Interface, genmymodelreverse_javax_servlet_ServletException, genmymodelreverse_javax_servlet_http_HttpServlet, genmymodelreverse_javax_servlet_http_HttpServletRequest_Interface, genmymodelreverse_javax_servlet_http_HttpServletResponse_Interface, genmymodelreverse_javax_servlet_Filter_Interface, genmymodelreverse_javax_servlet_FilterChain_Interface, genmymodelreverse_javax_servlet_FilterConfig_Interface, genmymodelreverse_javax_servlet_ServletRequest_Interface, genmymodelreverse_javax_servlet_ServletResponse_Interface, genmymodelreverse_java_sql_Connection_Interface, genmymodelreverse_javax_servlet_http_Part_Interface},
    associations={tm_WarningDAO_TransactionManager_16, tm_ProfileDAO_TransactionManager_5, tm_IdDAO_TransactionManager_6, tm_AccountBanDAO_TransactionManager_19, tm_AdultDetectionDAO_TransactionManager_4, tm_InsertCommentMess_TransactionManager_15, tm_ImagesDAO_TransactionManager_10, tm_ProfilePicture_TransactionManager_0, tm_LoginProcess_TransactionManager_7, tm_CommentDAO_TransactionManager_2, tm_ProfessionDAO_TransactionManager_13, tm_FriendRequestsDAO_TransactionManager_9, tm_InsertMessage_TransactionManager_12, tm_InsertComment_TransactionManager_18, tm_TableDAO_TransactionManager_3, tm_FriendsDAO_TransactionManager_1, tm_MessageDAO_TransactionManager_11, tm_LikesDAO_TransactionManager_20, tm_AccountBanDAO2_TransactionManager_14, tm_UsersRegistered_TransactionManager_8, tm_UserDAO_TransactionManager_17},
    generalizations={},
    metadata=None
)

###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)