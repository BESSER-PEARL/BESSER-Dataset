from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class String(Enum):
    pass

############################################
# Definition of Classes
############################################










class Role:

    def __init__(self, RoleID: int, Name: String, Description: str, User19: set["User"] = None):
        self.RoleID = RoleID
        self.Name = Name
        self.Description = Description
        self.User19 = User19 if User19 is not None else set()
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: String):
        self.__Name = Name

    @property
    def Description(self):
        return self.__Description
    @Description.setter
    def Description(self, Description: str):
        self.__Description = Description

    @property
    def RoleID(self):
        return self.__RoleID
    @RoleID.setter
    def RoleID(self, RoleID: int):
        self.__RoleID = RoleID

    @property
    def User19(self):
        return self.__User19
    @User19.setter
    def User19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Role__User19", None)
        self.__User19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Role18"):
                    opp_val = getattr(item, "Role18", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Role18"):
                    opp_val = getattr(item, "Role18", None)
                    
                    if opp_val is None:
                        setattr(item, "Role18", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Attachment:

    def __init__(self, AttachmentID: int, User: User, Project: Project, Created: str, Size: str, Extension: str, Path: str, Name: str, User15: "User" = None, Project17: "Project" = None):
        self.AttachmentID = AttachmentID
        self.User = User
        self.Project = Project
        self.Created = Created
        self.Size = Size
        self.Extension = Extension
        self.Path = Path
        self.Name = Name
        self.User15 = User15
        self.Project17 = Project17
        
        pass
    @property
    def AttachmentID(self):
        return self.__AttachmentID
    @AttachmentID.setter
    def AttachmentID(self, AttachmentID: int):
        self.__AttachmentID = AttachmentID

    @property
    def Extension(self):
        return self.__Extension
    @Extension.setter
    def Extension(self, Extension: str):
        self.__Extension = Extension

    @property
    def Size(self):
        return self.__Size
    @Size.setter
    def Size(self, Size: str):
        self.__Size = Size

    @property
    def Project(self):
        return self.__Project
    @Project.setter
    def Project(self, Project: Project):
        self.__Project = Project

    @property
    def Created(self):
        return self.__Created
    @Created.setter
    def Created(self, Created: str):
        self.__Created = Created

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def User(self):
        return self.__User
    @User.setter
    def User(self, User: User):
        self.__User = User

    @property
    def Path(self):
        return self.__Path
    @Path.setter
    def Path(self, Path: str):
        self.__Path = Path

    @property
    def User15(self):
        return self.__User15
    @User15.setter
    def User15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Attachment__User15", None)
        self.__User15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Attachment14"):
                opp_val = getattr(old_value, "Attachment14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Attachment14"):
                opp_val = getattr(value, "Attachment14", None)
                if opp_val is None:
                    setattr(value, "Attachment14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Project17(self):
        return self.__Project17
    @Project17.setter
    def Project17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Attachment__Project17", None)
        self.__Project17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Attachment16"):
                opp_val = getattr(old_value, "Attachment16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Attachment16"):
                opp_val = getattr(value, "Attachment16", None)
                if opp_val is None:
                    setattr(value, "Attachment16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Comment:

    def __init__(self, CommentID: int, User: User, Project: Project, Created: str, Content: str, Project11: "Project" = None, User13: "User" = None):
        self.CommentID = CommentID
        self.User = User
        self.Project = Project
        self.Created = Created
        self.Content = Content
        self.Project11 = Project11
        self.User13 = User13
        
        pass
    @property
    def CommentID(self):
        return self.__CommentID
    @CommentID.setter
    def CommentID(self, CommentID: int):
        self.__CommentID = CommentID

    @property
    def Project(self):
        return self.__Project
    @Project.setter
    def Project(self, Project: Project):
        self.__Project = Project

    @property
    def User(self):
        return self.__User
    @User.setter
    def User(self, User: User):
        self.__User = User

    @property
    def Created(self):
        return self.__Created
    @Created.setter
    def Created(self, Created: str):
        self.__Created = Created

    @property
    def Content(self):
        return self.__Content
    @Content.setter
    def Content(self, Content: str):
        self.__Content = Content

    @property
    def Project11(self):
        return self.__Project11
    @Project11.setter
    def Project11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Comment__Project11", None)
        self.__Project11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Comment10"):
                opp_val = getattr(old_value, "Comment10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Comment10"):
                opp_val = getattr(value, "Comment10", None)
                if opp_val is None:
                    setattr(value, "Comment10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def User13(self):
        return self.__User13
    @User13.setter
    def User13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Comment__User13", None)
        self.__User13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Comment12"):
                opp_val = getattr(old_value, "Comment12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Comment12"):
                opp_val = getattr(value, "Comment12", None)
                if opp_val is None:
                    setattr(value, "Comment12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Activity:

    def __init__(self, ActivityID: int, User: User, Project: Project, ActivityType: int, ActivitySubType: int, PrevValue: str, NewValue: str, Seen: bool, User7: "User" = None, Project9: "Project" = None):
        self.ActivityID = ActivityID
        self.User = User
        self.Project = Project
        self.ActivityType = ActivityType
        self.ActivitySubType = ActivitySubType
        self.PrevValue = PrevValue
        self.NewValue = NewValue
        self.Seen = Seen
        self.User7 = User7
        self.Project9 = Project9
        
        pass
    @property
    def ActivitySubType(self):
        return self.__ActivitySubType
    @ActivitySubType.setter
    def ActivitySubType(self, ActivitySubType: int):
        self.__ActivitySubType = ActivitySubType

    @property
    def NewValue(self):
        return self.__NewValue
    @NewValue.setter
    def NewValue(self, NewValue: str):
        self.__NewValue = NewValue

    @property
    def Project(self):
        return self.__Project
    @Project.setter
    def Project(self, Project: Project):
        self.__Project = Project

    @property
    def ActivityID(self):
        return self.__ActivityID
    @ActivityID.setter
    def ActivityID(self, ActivityID: int):
        self.__ActivityID = ActivityID

    @property
    def Seen(self):
        return self.__Seen
    @Seen.setter
    def Seen(self, Seen: bool):
        self.__Seen = Seen

    @property
    def User(self):
        return self.__User
    @User.setter
    def User(self, User: User):
        self.__User = User

    @property
    def ActivityType(self):
        return self.__ActivityType
    @ActivityType.setter
    def ActivityType(self, ActivityType: int):
        self.__ActivityType = ActivityType

    @property
    def PrevValue(self):
        return self.__PrevValue
    @PrevValue.setter
    def PrevValue(self, PrevValue: str):
        self.__PrevValue = PrevValue

    @property
    def Project9(self):
        return self.__Project9
    @Project9.setter
    def Project9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activity__Project9", None)
        self.__Project9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Activity8"):
                opp_val = getattr(old_value, "Activity8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Activity8"):
                opp_val = getattr(value, "Activity8", None)
                if opp_val is None:
                    setattr(value, "Activity8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def User7(self):
        return self.__User7
    @User7.setter
    def User7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activity__User7", None)
        self.__User7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Activity6"):
                opp_val = getattr(old_value, "Activity6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Activity6"):
                opp_val = getattr(value, "Activity6", None)
                if opp_val is None:
                    setattr(value, "Activity6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Project:

    def __init__(self, PorjectID: int, Title: str, Created: str, Deadline: str, StatusID: int, PriorityID: int, Author: User, ProjectManager: User, Assignee: User, Description: str, Team___: str, Subscriptions___: str, Comments___: str, Attachments___: str, Activities___: str, User1: "User" = None, User3: "User" = None, User5: "User" = None, Activity8: set["Activity"] = None, Comment10: set["Comment"] = None, Attachment16: set["Attachment"] = None, User20: "User" = None):
        self.PorjectID = PorjectID
        self.Title = Title
        self.Created = Created
        self.Deadline = Deadline
        self.StatusID = StatusID
        self.PriorityID = PriorityID
        self.Author = Author
        self.ProjectManager = ProjectManager
        self.Assignee = Assignee
        self.Description = Description
        self.Team___ = Team___
        self.Subscriptions___ = Subscriptions___
        self.Comments___ = Comments___
        self.Attachments___ = Attachments___
        self.Activities___ = Activities___
        self.User1 = User1
        self.User3 = User3
        self.User5 = User5
        self.Activity8 = Activity8 if Activity8 is not None else set()
        self.Comment10 = Comment10 if Comment10 is not None else set()
        self.Attachment16 = Attachment16 if Attachment16 is not None else set()
        self.User20 = User20
        
        pass
    @property
    def Comments___(self):
        return self.__Comments___
    @Comments___.setter
    def Comments___(self, Comments___: str):
        self.__Comments___ = Comments___

    @property
    def Team___(self):
        return self.__Team___
    @Team___.setter
    def Team___(self, Team___: str):
        self.__Team___ = Team___

    @property
    def Assignee(self):
        return self.__Assignee
    @Assignee.setter
    def Assignee(self, Assignee: User):
        self.__Assignee = Assignee

    @property
    def Title(self):
        return self.__Title
    @Title.setter
    def Title(self, Title: str):
        self.__Title = Title

    @property
    def Subscriptions___(self):
        return self.__Subscriptions___
    @Subscriptions___.setter
    def Subscriptions___(self, Subscriptions___: str):
        self.__Subscriptions___ = Subscriptions___

    @property
    def Author(self):
        return self.__Author
    @Author.setter
    def Author(self, Author: User):
        self.__Author = Author

    @property
    def Description(self):
        return self.__Description
    @Description.setter
    def Description(self, Description: str):
        self.__Description = Description

    @property
    def Activities___(self):
        return self.__Activities___
    @Activities___.setter
    def Activities___(self, Activities___: str):
        self.__Activities___ = Activities___

    @property
    def Attachments___(self):
        return self.__Attachments___
    @Attachments___.setter
    def Attachments___(self, Attachments___: str):
        self.__Attachments___ = Attachments___

    @property
    def PorjectID(self):
        return self.__PorjectID
    @PorjectID.setter
    def PorjectID(self, PorjectID: int):
        self.__PorjectID = PorjectID

    @property
    def PriorityID(self):
        return self.__PriorityID
    @PriorityID.setter
    def PriorityID(self, PriorityID: int):
        self.__PriorityID = PriorityID

    @property
    def Deadline(self):
        return self.__Deadline
    @Deadline.setter
    def Deadline(self, Deadline: str):
        self.__Deadline = Deadline

    @property
    def Created(self):
        return self.__Created
    @Created.setter
    def Created(self, Created: str):
        self.__Created = Created

    @property
    def ProjectManager(self):
        return self.__ProjectManager
    @ProjectManager.setter
    def ProjectManager(self, ProjectManager: User):
        self.__ProjectManager = ProjectManager

    @property
    def StatusID(self):
        return self.__StatusID
    @StatusID.setter
    def StatusID(self, StatusID: int):
        self.__StatusID = StatusID

    @property
    def Activity8(self):
        return self.__Activity8
    @Activity8.setter
    def Activity8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Project__Activity8", None)
        self.__Activity8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Project9"):
                    opp_val = getattr(item, "Project9", None)
                    
                    if opp_val == self:
                        setattr(item, "Project9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Project9"):
                    opp_val = getattr(item, "Project9", None)
                    
                    setattr(item, "Project9", self)
                    

    @property
    def User20(self):
        return self.__User20
    @User20.setter
    def User20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Project__User20", None)
        self.__User20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Project21"):
                opp_val = getattr(old_value, "Project21", None)
                if opp_val == self:
                    setattr(old_value, "Project21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Project21"):
                opp_val = getattr(value, "Project21", None)
                setattr(value, "Project21", self)

    @property
    def User1(self):
        return self.__User1
    @User1.setter
    def User1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Project__User1", None)
        self.__User1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Author0"):
                opp_val = getattr(old_value, "Author0", None)
                if opp_val == self:
                    setattr(old_value, "Author0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Author0"):
                opp_val = getattr(value, "Author0", None)
                setattr(value, "Author0", self)

    @property
    def User3(self):
        return self.__User3
    @User3.setter
    def User3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Project__User3", None)
        self.__User3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProjectMan_2"):
                opp_val = getattr(old_value, "ProjectMan_2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProjectMan_2"):
                opp_val = getattr(value, "ProjectMan_2", None)
                if opp_val is None:
                    setattr(value, "ProjectMan_2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def User5(self):
        return self.__User5
    @User5.setter
    def User5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Project__User5", None)
        self.__User5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Assignee4"):
                opp_val = getattr(old_value, "Assignee4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Assignee4"):
                opp_val = getattr(value, "Assignee4", None)
                if opp_val is None:
                    setattr(value, "Assignee4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Attachment16(self):
        return self.__Attachment16
    @Attachment16.setter
    def Attachment16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Project__Attachment16", None)
        self.__Attachment16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Project17"):
                    opp_val = getattr(item, "Project17", None)
                    
                    if opp_val == self:
                        setattr(item, "Project17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Project17"):
                    opp_val = getattr(item, "Project17", None)
                    
                    setattr(item, "Project17", self)
                    

    @property
    def Comment10(self):
        return self.__Comment10
    @Comment10.setter
    def Comment10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Project__Comment10", None)
        self.__Comment10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Project11"):
                    opp_val = getattr(item, "Project11", None)
                    
                    if opp_val == self:
                        setattr(item, "Project11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Project11"):
                    opp_val = getattr(item, "Project11", None)
                    
                    setattr(item, "Project11", self)
                    



class User:

    def __init__(self, UserID: int, Username: str, Password: str, Firstname: str, Lastname: str, Dateofbirth: str, Email: str, Phone: str, DepartmentID: int, TitleID: int, Active: bool, Settings: str, Position: str, Hiredate: str, About: str, Facebook_link: str, Google_plus_link: str, Linkedin_link: str, Roles___: str, ProjectMan_2: set["Project"] = None, Assignee4: set["Project"] = None, Activity6: set["Activity"] = None, Attachment14: set["Attachment"] = None, Comment12: set["Comment"] = None, Author0: "Project" = None, Role18: set["Role"] = None, Project21: "Project" = None):
        self.UserID = UserID
        self.Username = Username
        self.Password = Password
        self.Firstname = Firstname
        self.Lastname = Lastname
        self.Dateofbirth = Dateofbirth
        self.Email = Email
        self.Phone = Phone
        self.DepartmentID = DepartmentID
        self.TitleID = TitleID
        self.Active = Active
        self.Settings = Settings
        self.Position = Position
        self.Hiredate = Hiredate
        self.About = About
        self.Facebook_link = Facebook_link
        self.Google_plus_link = Google_plus_link
        self.Linkedin_link = Linkedin_link
        self.Roles___ = Roles___
        self.ProjectMan_2 = ProjectMan_2 if ProjectMan_2 is not None else set()
        self.Assignee4 = Assignee4 if Assignee4 is not None else set()
        self.Activity6 = Activity6 if Activity6 is not None else set()
        self.Attachment14 = Attachment14 if Attachment14 is not None else set()
        self.Comment12 = Comment12 if Comment12 is not None else set()
        self.Author0 = Author0
        self.Role18 = Role18 if Role18 is not None else set()
        self.Project21 = Project21
        
        pass
    @property
    def Dateofbirth(self):
        return self.__Dateofbirth
    @Dateofbirth.setter
    def Dateofbirth(self, Dateofbirth: str):
        self.__Dateofbirth = Dateofbirth

    @property
    def Settings(self):
        return self.__Settings
    @Settings.setter
    def Settings(self, Settings: str):
        self.__Settings = Settings

    @property
    def Position(self):
        return self.__Position
    @Position.setter
    def Position(self, Position: str):
        self.__Position = Position

    @property
    def DepartmentID(self):
        return self.__DepartmentID
    @DepartmentID.setter
    def DepartmentID(self, DepartmentID: int):
        self.__DepartmentID = DepartmentID

    @property
    def TitleID(self):
        return self.__TitleID
    @TitleID.setter
    def TitleID(self, TitleID: int):
        self.__TitleID = TitleID

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def UserID(self):
        return self.__UserID
    @UserID.setter
    def UserID(self, UserID: int):
        self.__UserID = UserID

    @property
    def Active(self):
        return self.__Active
    @Active.setter
    def Active(self, Active: bool):
        self.__Active = Active

    @property
    def Roles___(self):
        return self.__Roles___
    @Roles___.setter
    def Roles___(self, Roles___: str):
        self.__Roles___ = Roles___

    @property
    def Linkedin_link(self):
        return self.__Linkedin_link
    @Linkedin_link.setter
    def Linkedin_link(self, Linkedin_link: str):
        self.__Linkedin_link = Linkedin_link

    @property
    def About(self):
        return self.__About
    @About.setter
    def About(self, About: str):
        self.__About = About

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def Facebook_link(self):
        return self.__Facebook_link
    @Facebook_link.setter
    def Facebook_link(self, Facebook_link: str):
        self.__Facebook_link = Facebook_link

    @property
    def Firstname(self):
        return self.__Firstname
    @Firstname.setter
    def Firstname(self, Firstname: str):
        self.__Firstname = Firstname

    @property
    def Username(self):
        return self.__Username
    @Username.setter
    def Username(self, Username: str):
        self.__Username = Username

    @property
    def Google_plus_link(self):
        return self.__Google_plus_link
    @Google_plus_link.setter
    def Google_plus_link(self, Google_plus_link: str):
        self.__Google_plus_link = Google_plus_link

    @property
    def Lastname(self):
        return self.__Lastname
    @Lastname.setter
    def Lastname(self, Lastname: str):
        self.__Lastname = Lastname

    @property
    def Hiredate(self):
        return self.__Hiredate
    @Hiredate.setter
    def Hiredate(self, Hiredate: str):
        self.__Hiredate = Hiredate

    @property
    def Phone(self):
        return self.__Phone
    @Phone.setter
    def Phone(self, Phone: str):
        self.__Phone = Phone

    @property
    def Role18(self):
        return self.__Role18
    @Role18.setter
    def Role18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__Role18", None)
        self.__Role18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "User19"):
                    opp_val = getattr(item, "User19", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "User19"):
                    opp_val = getattr(item, "User19", None)
                    
                    if opp_val is None:
                        setattr(item, "User19", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def Project21(self):
        return self.__Project21
    @Project21.setter
    def Project21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__Project21", None)
        self.__Project21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "User20"):
                opp_val = getattr(old_value, "User20", None)
                if opp_val == self:
                    setattr(old_value, "User20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "User20"):
                opp_val = getattr(value, "User20", None)
                setattr(value, "User20", self)

    @property
    def Attachment14(self):
        return self.__Attachment14
    @Attachment14.setter
    def Attachment14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__Attachment14", None)
        self.__Attachment14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "User15"):
                    opp_val = getattr(item, "User15", None)
                    
                    if opp_val == self:
                        setattr(item, "User15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "User15"):
                    opp_val = getattr(item, "User15", None)
                    
                    setattr(item, "User15", self)
                    

    @property
    def Assignee4(self):
        return self.__Assignee4
    @Assignee4.setter
    def Assignee4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__Assignee4", None)
        self.__Assignee4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "User5"):
                    opp_val = getattr(item, "User5", None)
                    
                    if opp_val == self:
                        setattr(item, "User5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "User5"):
                    opp_val = getattr(item, "User5", None)
                    
                    setattr(item, "User5", self)
                    

    @property
    def Comment12(self):
        return self.__Comment12
    @Comment12.setter
    def Comment12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__Comment12", None)
        self.__Comment12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "User13"):
                    opp_val = getattr(item, "User13", None)
                    
                    if opp_val == self:
                        setattr(item, "User13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "User13"):
                    opp_val = getattr(item, "User13", None)
                    
                    setattr(item, "User13", self)
                    

    @property
    def Author0(self):
        return self.__Author0
    @Author0.setter
    def Author0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__Author0", None)
        self.__Author0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "User1"):
                opp_val = getattr(old_value, "User1", None)
                if opp_val == self:
                    setattr(old_value, "User1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "User1"):
                opp_val = getattr(value, "User1", None)
                setattr(value, "User1", self)

    @property
    def ProjectMan_2(self):
        return self.__ProjectMan_2
    @ProjectMan_2.setter
    def ProjectMan_2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__ProjectMan_2", None)
        self.__ProjectMan_2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "User3"):
                    opp_val = getattr(item, "User3", None)
                    
                    if opp_val == self:
                        setattr(item, "User3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "User3"):
                    opp_val = getattr(item, "User3", None)
                    
                    setattr(item, "User3", self)
                    

    @property
    def Activity6(self):
        return self.__Activity6
    @Activity6.setter
    def Activity6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__Activity6", None)
        self.__Activity6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "User7"):
                    opp_val = getattr(item, "User7", None)
                    
                    if opp_val == self:
                        setattr(item, "User7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "User7"):
                    opp_val = getattr(item, "User7", None)
                    
                    setattr(item, "User7", self)
                    

