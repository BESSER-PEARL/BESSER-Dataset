from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class IssueStatus(Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"
class VersionStatus(Enum):
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETE = "COMPLETE"
class IssueType(Enum):
    ENHANCEMENT = "ENHANCEMENT"
    BUG = "BUG"
    WONT_FIX = "WONT_FIX"
    HELP_REQUIRED = "HELP_REQUIRED"
    DUPLICATE = "DUPLICATE"


############################################
# Definition of Classes
############################################

class Identifiable:

    pass
class trackit_Version(Identifiable):

    def __init__(self, name: str, status: str, trackit_Version: "trackit_Product" = None, trackit_Version18: "trackit_Product" = None, versionsAffected: set["trackit_Issue"] = None, Version: "trackit_Issue" = None):
        self.name = name
        self.status = status
        self.trackit_Version = trackit_Version
        self.trackit_Version18 = trackit_Version18
        self.versionsAffected = versionsAffected if versionsAffected is not None else set()
        self.Version = Version
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def trackit_Version(self):
        return self.__trackit_Version

    @trackit_Version.setter
    def trackit_Version(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Version__trackit_Version", None)
        self.__trackit_Version = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trackit_Product16"):
                opp_val = getattr(old_value, "trackit_Product16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trackit_Product16"):
                opp_val = getattr(value, "trackit_Product16", None)
                if opp_val is None:
                    setattr(value, "trackit_Product16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Version(self):
        return self.__Version

    @Version.setter
    def Version(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Version__Version", None)
        self.__Version = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "issues"):
                opp_val = getattr(old_value, "issues", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "issues"):
                opp_val = getattr(value, "issues", None)
                if opp_val is None:
                    setattr(value, "issues", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def trackit_Version18(self):
        return self.__trackit_Version18

    @trackit_Version18.setter
    def trackit_Version18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Version__trackit_Version18", None)
        self.__trackit_Version18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trackit_Product19"):
                opp_val = getattr(old_value, "trackit_Product19", None)
                if opp_val == self:
                    setattr(old_value, "trackit_Product19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trackit_Product19"):
                opp_val = getattr(value, "trackit_Product19", None)
                setattr(value, "trackit_Product19", self)

    @property
    def versionsAffected(self):
        return self.__versionsAffected

    @versionsAffected.setter
    def versionsAffected(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Version__versionsAffected", None)
        self.__versionsAffected = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Issue21"):
                    opp_val = getattr(item, "Issue21", None)
                    
                    if opp_val == self:
                        setattr(item, "Issue21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Issue21"):
                    opp_val = getattr(item, "Issue21", None)
                    
                    setattr(item, "Issue21", self)
                    

class trackit_Comment(Identifiable):

    def __init__(self, text: str, dateCreated: str, Comment: "trackit_Member" = None, Comment29: "trackit_Issue" = None, comments: "trackit_Issue" = None, comments43: "trackit_Member" = None, Comment47: "trackit_Comment" = None, replies: "trackit_Comment" = None, Comment50: "trackit_Comment" = None, parent: set["trackit_Comment"] = None):
        self.text = text
        self.dateCreated = dateCreated
        self.Comment = Comment
        self.Comment29 = Comment29
        self.comments = comments
        self.comments43 = comments43
        self.Comment47 = Comment47
        self.replies = replies
        self.Comment50 = Comment50
        self.parent = parent if parent is not None else set()
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def dateCreated(self) -> str:
        return self.__dateCreated

    @dateCreated.setter
    def dateCreated(self, dateCreated: str):
        self.__dateCreated = dateCreated

    @property
    def comments43(self):
        return self.__comments43

    @comments43.setter
    def comments43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Comment__comments43", None)
        self.__comments43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Member44"):
                opp_val = getattr(old_value, "Member44", None)
                if opp_val == self:
                    setattr(old_value, "Member44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Member44"):
                opp_val = getattr(value, "Member44", None)
                setattr(value, "Member44", self)

    @property
    def Comment29(self):
        return self.__Comment29

    @Comment29.setter
    def Comment29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Comment__Comment29", None)
        self.__Comment29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "issue"):
                opp_val = getattr(old_value, "issue", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "issue"):
                opp_val = getattr(value, "issue", None)
                if opp_val is None:
                    setattr(value, "issue", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Comment(self):
        return self.__Comment

    @Comment.setter
    def Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Comment__Comment", None)
        self.__Comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "author9"):
                opp_val = getattr(old_value, "author9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "author9"):
                opp_val = getattr(value, "author9", None)
                if opp_val is None:
                    setattr(value, "author9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def comments(self):
        return self.__comments

    @comments.setter
    def comments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Comment__comments", None)
        self.__comments = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Issue41"):
                opp_val = getattr(old_value, "Issue41", None)
                if opp_val == self:
                    setattr(old_value, "Issue41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Issue41"):
                opp_val = getattr(value, "Issue41", None)
                setattr(value, "Issue41", self)

    @property
    def Comment50(self):
        return self.__Comment50

    @Comment50.setter
    def Comment50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Comment__Comment50", None)
        self.__Comment50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent"):
                opp_val = getattr(old_value, "parent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent"):
                opp_val = getattr(value, "parent", None)
                if opp_val is None:
                    setattr(value, "parent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def replies(self):
        return self.__replies

    @replies.setter
    def replies(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Comment__replies", None)
        self.__replies = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Comment47"):
                opp_val = getattr(old_value, "Comment47", None)
                if opp_val == self:
                    setattr(old_value, "Comment47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Comment47"):
                opp_val = getattr(value, "Comment47", None)
                setattr(value, "Comment47", self)

    @property
    def Comment47(self):
        return self.__Comment47

    @Comment47.setter
    def Comment47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Comment__Comment47", None)
        self.__Comment47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "replies"):
                opp_val = getattr(old_value, "replies", None)
                if opp_val == self:
                    setattr(old_value, "replies", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "replies"):
                opp_val = getattr(value, "replies", None)
                setattr(value, "replies", self)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Comment__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Comment50"):
                    opp_val = getattr(item, "Comment50", None)
                    
                    if opp_val == self:
                        setattr(item, "Comment50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Comment50"):
                    opp_val = getattr(item, "Comment50", None)
                    
                    setattr(item, "Comment50", self)
                    

class trackit_Identifiable(ABC):

    def __init__(self, uuid: str):
        self.uuid = uuid
        
    @property
    def uuid(self) -> str:
        return self.__uuid

    @uuid.setter
    def uuid(self, uuid: str):
        self.__uuid = uuid

class trackit_Member(Identifiable):

    def __init__(self, firstName: str, lastName: str, fullName: str, trackit_Member: "trackit_IssueTracker" = None, author: set["trackit_Issue"] = None, author9: set["trackit_Comment"] = None, assignedTo: set["trackit_Issue"] = None, trackit_Member14: "trackit_Team" = None, Member: "trackit_Issue" = None, Member27: "trackit_Issue" = None, Member44: "trackit_Comment" = None):
        self.firstName = firstName
        self.lastName = lastName
        self.fullName = fullName
        self.trackit_Member = trackit_Member
        self.author = author if author is not None else set()
        self.author9 = author9 if author9 is not None else set()
        self.assignedTo = assignedTo if assignedTo is not None else set()
        self.trackit_Member14 = trackit_Member14
        self.Member = Member
        self.Member27 = Member27
        self.Member44 = Member44
        
    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def fullName(self) -> str:
        return self.__fullName

    @fullName.setter
    def fullName(self, fullName: str):
        self.__fullName = fullName

    @property
    def author9(self):
        return self.__author9

    @author9.setter
    def author9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Member__author9", None)
        self.__author9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Comment"):
                    opp_val = getattr(item, "Comment", None)
                    
                    if opp_val == self:
                        setattr(item, "Comment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Comment"):
                    opp_val = getattr(item, "Comment", None)
                    
                    setattr(item, "Comment", self)
                    

    @property
    def trackit_Member14(self):
        return self.__trackit_Member14

    @trackit_Member14.setter
    def trackit_Member14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Member__trackit_Member14", None)
        self.__trackit_Member14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trackit_Team13"):
                opp_val = getattr(old_value, "trackit_Team13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trackit_Team13"):
                opp_val = getattr(value, "trackit_Team13", None)
                if opp_val is None:
                    setattr(value, "trackit_Team13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Member44(self):
        return self.__Member44

    @Member44.setter
    def Member44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Member__Member44", None)
        self.__Member44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "comments43"):
                opp_val = getattr(old_value, "comments43", None)
                if opp_val == self:
                    setattr(old_value, "comments43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "comments43"):
                opp_val = getattr(value, "comments43", None)
                setattr(value, "comments43", self)

    @property
    def assignedTo(self):
        return self.__assignedTo

    @assignedTo.setter
    def assignedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Member__assignedTo", None)
        self.__assignedTo = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Issue11"):
                    opp_val = getattr(item, "Issue11", None)
                    
                    if opp_val == self:
                        setattr(item, "Issue11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Issue11"):
                    opp_val = getattr(item, "Issue11", None)
                    
                    setattr(item, "Issue11", self)
                    

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Member__author", None)
        self.__author = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Issue"):
                    opp_val = getattr(item, "Issue", None)
                    
                    if opp_val == self:
                        setattr(item, "Issue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Issue"):
                    opp_val = getattr(item, "Issue", None)
                    
                    setattr(item, "Issue", self)
                    

    @property
    def Member27(self):
        return self.__Member27

    @Member27.setter
    def Member27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Member__Member27", None)
        self.__Member27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "issuesAssigned"):
                opp_val = getattr(old_value, "issuesAssigned", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "issuesAssigned"):
                opp_val = getattr(value, "issuesAssigned", None)
                if opp_val is None:
                    setattr(value, "issuesAssigned", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def trackit_Member(self):
        return self.__trackit_Member

    @trackit_Member.setter
    def trackit_Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Member__trackit_Member", None)
        self.__trackit_Member = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trackit_IssueTracker6"):
                opp_val = getattr(old_value, "trackit_IssueTracker6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trackit_IssueTracker6"):
                opp_val = getattr(value, "trackit_IssueTracker6", None)
                if opp_val is None:
                    setattr(value, "trackit_IssueTracker6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Member(self):
        return self.__Member

    @Member.setter
    def Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Member__Member", None)
        self.__Member = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "issuesCreated"):
                opp_val = getattr(old_value, "issuesCreated", None)
                if opp_val == self:
                    setattr(old_value, "issuesCreated", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "issuesCreated"):
                opp_val = getattr(value, "issuesCreated", None)
                setattr(value, "issuesCreated", self)

class trackit_Issue(Identifiable):

    def __init__(self, title: str, description: str, dateCreated: str, status: str, issueType: str, trackit_Issue: "trackit_IssueTracker" = None, Issue: "trackit_Member" = None, Issue11: "trackit_Member" = None, Issue21: "trackit_Version" = None, issuesCreated: "trackit_Member" = None, Issue25: "trackit_Issue" = None, blocking: set["trackit_Issue"] = None, issuesAssigned: set["trackit_Member"] = None, issue: set["trackit_Comment"] = None, trackit_Issue32: "trackit_Issue" = None, trackit_Issue30: set["trackit_Issue"] = None, trackit_Issue35: "trackit_Issue" = None, trackit_Issue33: set["trackit_Issue"] = None, issues: set["trackit_Version"] = None, Issue39: "trackit_Issue" = None, blockers: set["trackit_Issue"] = None, Issue41: "trackit_Comment" = None):
        self.title = title
        self.description = description
        self.dateCreated = dateCreated
        self.status = status
        self.issueType = issueType
        self.trackit_Issue = trackit_Issue
        self.Issue = Issue
        self.Issue11 = Issue11
        self.Issue21 = Issue21
        self.issuesCreated = issuesCreated
        self.Issue25 = Issue25
        self.blocking = blocking if blocking is not None else set()
        self.issuesAssigned = issuesAssigned if issuesAssigned is not None else set()
        self.issue = issue if issue is not None else set()
        self.trackit_Issue32 = trackit_Issue32
        self.trackit_Issue30 = trackit_Issue30 if trackit_Issue30 is not None else set()
        self.trackit_Issue35 = trackit_Issue35
        self.trackit_Issue33 = trackit_Issue33 if trackit_Issue33 is not None else set()
        self.issues = issues if issues is not None else set()
        self.Issue39 = Issue39
        self.blockers = blockers if blockers is not None else set()
        self.Issue41 = Issue41
        
    @property
    def dateCreated(self) -> str:
        return self.__dateCreated

    @dateCreated.setter
    def dateCreated(self, dateCreated: str):
        self.__dateCreated = dateCreated

    @property
    def issueType(self) -> str:
        return self.__issueType

    @issueType.setter
    def issueType(self, issueType: str):
        self.__issueType = issueType

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def Issue25(self):
        return self.__Issue25

    @Issue25.setter
    def Issue25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Issue__Issue25", None)
        self.__Issue25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blocking"):
                opp_val = getattr(old_value, "blocking", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blocking"):
                opp_val = getattr(value, "blocking", None)
                if opp_val is None:
                    setattr(value, "blocking", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Issue21(self):
        return self.__Issue21

    @Issue21.setter
    def Issue21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Issue__Issue21", None)
        self.__Issue21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "versionsAffected"):
                opp_val = getattr(old_value, "versionsAffected", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "versionsAffected"):
                opp_val = getattr(value, "versionsAffected", None)
                if opp_val is None:
                    setattr(value, "versionsAffected", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def trackit_Issue33(self):
        return self.__trackit_Issue33

    @trackit_Issue33.setter
    def trackit_Issue33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Issue__trackit_Issue33", None)
        self.__trackit_Issue33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trackit_Issue35"):
                    opp_val = getattr(item, "trackit_Issue35", None)
                    
                    if opp_val == self:
                        setattr(item, "trackit_Issue35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trackit_Issue35"):
                    opp_val = getattr(item, "trackit_Issue35", None)
                    
                    setattr(item, "trackit_Issue35", self)
                    

    @property
    def Issue11(self):
        return self.__Issue11

    @Issue11.setter
    def Issue11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Issue__Issue11", None)
        self.__Issue11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assignedTo"):
                opp_val = getattr(old_value, "assignedTo", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assignedTo"):
                opp_val = getattr(value, "assignedTo", None)
                if opp_val is None:
                    setattr(value, "assignedTo", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def trackit_Issue32(self):
        return self.__trackit_Issue32

    @trackit_Issue32.setter
    def trackit_Issue32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Issue__trackit_Issue32", None)
        self.__trackit_Issue32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trackit_Issue30"):
                opp_val = getattr(old_value, "trackit_Issue30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trackit_Issue30"):
                opp_val = getattr(value, "trackit_Issue30", None)
                if opp_val is None:
                    setattr(value, "trackit_Issue30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Issue39(self):
        return self.__Issue39

    @Issue39.setter
    def Issue39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Issue__Issue39", None)
        self.__Issue39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blockers"):
                opp_val = getattr(old_value, "blockers", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blockers"):
                opp_val = getattr(value, "blockers", None)
                if opp_val is None:
                    setattr(value, "blockers", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def blocking(self):
        return self.__blocking

    @blocking.setter
    def blocking(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Issue__blocking", None)
        self.__blocking = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Issue25"):
                    opp_val = getattr(item, "Issue25", None)
                    
                    if opp_val == self:
                        setattr(item, "Issue25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Issue25"):
                    opp_val = getattr(item, "Issue25", None)
                    
                    setattr(item, "Issue25", self)
                    

    @property
    def issues(self):
        return self.__issues

    @issues.setter
    def issues(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Issue__issues", None)
        self.__issues = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Version"):
                    opp_val = getattr(item, "Version", None)
                    
                    if opp_val == self:
                        setattr(item, "Version", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Version"):
                    opp_val = getattr(item, "Version", None)
                    
                    setattr(item, "Version", self)
                    

    @property
    def Issue(self):
        return self.__Issue

    @Issue.setter
    def Issue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Issue__Issue", None)
        self.__Issue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "author"):
                opp_val = getattr(old_value, "author", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "author"):
                opp_val = getattr(value, "author", None)
                if opp_val is None:
                    setattr(value, "author", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def blockers(self):
        return self.__blockers

    @blockers.setter
    def blockers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Issue__blockers", None)
        self.__blockers = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Issue39"):
                    opp_val = getattr(item, "Issue39", None)
                    
                    if opp_val == self:
                        setattr(item, "Issue39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Issue39"):
                    opp_val = getattr(item, "Issue39", None)
                    
                    setattr(item, "Issue39", self)
                    

    @property
    def trackit_Issue35(self):
        return self.__trackit_Issue35

    @trackit_Issue35.setter
    def trackit_Issue35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Issue__trackit_Issue35", None)
        self.__trackit_Issue35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trackit_Issue33"):
                opp_val = getattr(old_value, "trackit_Issue33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trackit_Issue33"):
                opp_val = getattr(value, "trackit_Issue33", None)
                if opp_val is None:
                    setattr(value, "trackit_Issue33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Issue41(self):
        return self.__Issue41

    @Issue41.setter
    def Issue41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Issue__Issue41", None)
        self.__Issue41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "comments"):
                opp_val = getattr(old_value, "comments", None)
                if opp_val == self:
                    setattr(old_value, "comments", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "comments"):
                opp_val = getattr(value, "comments", None)
                setattr(value, "comments", self)

    @property
    def issuesCreated(self):
        return self.__issuesCreated

    @issuesCreated.setter
    def issuesCreated(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Issue__issuesCreated", None)
        self.__issuesCreated = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Member"):
                opp_val = getattr(old_value, "Member", None)
                if opp_val == self:
                    setattr(old_value, "Member", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Member"):
                opp_val = getattr(value, "Member", None)
                setattr(value, "Member", self)

    @property
    def issue(self):
        return self.__issue

    @issue.setter
    def issue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Issue__issue", None)
        self.__issue = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Comment29"):
                    opp_val = getattr(item, "Comment29", None)
                    
                    if opp_val == self:
                        setattr(item, "Comment29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Comment29"):
                    opp_val = getattr(item, "Comment29", None)
                    
                    setattr(item, "Comment29", self)
                    

    @property
    def issuesAssigned(self):
        return self.__issuesAssigned

    @issuesAssigned.setter
    def issuesAssigned(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Issue__issuesAssigned", None)
        self.__issuesAssigned = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Member27"):
                    opp_val = getattr(item, "Member27", None)
                    
                    if opp_val == self:
                        setattr(item, "Member27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Member27"):
                    opp_val = getattr(item, "Member27", None)
                    
                    setattr(item, "Member27", self)
                    

    @property
    def trackit_Issue(self):
        return self.__trackit_Issue

    @trackit_Issue.setter
    def trackit_Issue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Issue__trackit_Issue", None)
        self.__trackit_Issue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trackit_IssueTracker4"):
                opp_val = getattr(old_value, "trackit_IssueTracker4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trackit_IssueTracker4"):
                opp_val = getattr(value, "trackit_IssueTracker4", None)
                if opp_val is None:
                    setattr(value, "trackit_IssueTracker4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def trackit_Issue30(self):
        return self.__trackit_Issue30

    @trackit_Issue30.setter
    def trackit_Issue30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Issue__trackit_Issue30", None)
        self.__trackit_Issue30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trackit_Issue32"):
                    opp_val = getattr(item, "trackit_Issue32", None)
                    
                    if opp_val == self:
                        setattr(item, "trackit_Issue32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trackit_Issue32"):
                    opp_val = getattr(item, "trackit_Issue32", None)
                    
                    setattr(item, "trackit_Issue32", self)
                    

class trackit_Product(Identifiable):

    def __init__(self, name: str, trackit_Product: "trackit_IssueTracker" = None, trackit_Product16: set["trackit_Version"] = None, trackit_Product19: "trackit_Version" = None):
        self.name = name
        self.trackit_Product = trackit_Product
        self.trackit_Product16 = trackit_Product16 if trackit_Product16 is not None else set()
        self.trackit_Product19 = trackit_Product19
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def trackit_Product(self):
        return self.__trackit_Product

    @trackit_Product.setter
    def trackit_Product(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Product__trackit_Product", None)
        self.__trackit_Product = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trackit_IssueTracker2"):
                opp_val = getattr(old_value, "trackit_IssueTracker2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trackit_IssueTracker2"):
                opp_val = getattr(value, "trackit_IssueTracker2", None)
                if opp_val is None:
                    setattr(value, "trackit_IssueTracker2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def trackit_Product16(self):
        return self.__trackit_Product16

    @trackit_Product16.setter
    def trackit_Product16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Product__trackit_Product16", None)
        self.__trackit_Product16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trackit_Version"):
                    opp_val = getattr(item, "trackit_Version", None)
                    
                    if opp_val == self:
                        setattr(item, "trackit_Version", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trackit_Version"):
                    opp_val = getattr(item, "trackit_Version", None)
                    
                    setattr(item, "trackit_Version", self)
                    

    @property
    def trackit_Product19(self):
        return self.__trackit_Product19

    @trackit_Product19.setter
    def trackit_Product19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Product__trackit_Product19", None)
        self.__trackit_Product19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trackit_Version18"):
                opp_val = getattr(old_value, "trackit_Version18", None)
                if opp_val == self:
                    setattr(old_value, "trackit_Version18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trackit_Version18"):
                opp_val = getattr(value, "trackit_Version18", None)
                setattr(value, "trackit_Version18", self)

class trackit_Team(Identifiable):

    def __init__(self, teamName: str, trackit_Team: "trackit_IssueTracker" = None, trackit_Team13: set["trackit_Member"] = None):
        self.teamName = teamName
        self.trackit_Team = trackit_Team
        self.trackit_Team13 = trackit_Team13 if trackit_Team13 is not None else set()
        
    @property
    def teamName(self) -> str:
        return self.__teamName

    @teamName.setter
    def teamName(self, teamName: str):
        self.__teamName = teamName

    @property
    def trackit_Team(self):
        return self.__trackit_Team

    @trackit_Team.setter
    def trackit_Team(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Team__trackit_Team", None)
        self.__trackit_Team = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trackit_IssueTracker"):
                opp_val = getattr(old_value, "trackit_IssueTracker", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trackit_IssueTracker"):
                opp_val = getattr(value, "trackit_IssueTracker", None)
                if opp_val is None:
                    setattr(value, "trackit_IssueTracker", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def trackit_Team13(self):
        return self.__trackit_Team13

    @trackit_Team13.setter
    def trackit_Team13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_Team__trackit_Team13", None)
        self.__trackit_Team13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trackit_Member14"):
                    opp_val = getattr(item, "trackit_Member14", None)
                    
                    if opp_val == self:
                        setattr(item, "trackit_Member14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trackit_Member14"):
                    opp_val = getattr(item, "trackit_Member14", None)
                    
                    setattr(item, "trackit_Member14", self)
                    

class trackit_IssueTracker:

    def __init__(self, projectName: str, trackit_IssueTracker: set["trackit_Team"] = None, trackit_IssueTracker2: set["trackit_Product"] = None, trackit_IssueTracker4: set["trackit_Issue"] = None, trackit_IssueTracker6: set["trackit_Member"] = None):
        self.projectName = projectName
        self.trackit_IssueTracker = trackit_IssueTracker if trackit_IssueTracker is not None else set()
        self.trackit_IssueTracker2 = trackit_IssueTracker2 if trackit_IssueTracker2 is not None else set()
        self.trackit_IssueTracker4 = trackit_IssueTracker4 if trackit_IssueTracker4 is not None else set()
        self.trackit_IssueTracker6 = trackit_IssueTracker6 if trackit_IssueTracker6 is not None else set()
        
    @property
    def projectName(self) -> str:
        return self.__projectName

    @projectName.setter
    def projectName(self, projectName: str):
        self.__projectName = projectName

    @property
    def trackit_IssueTracker6(self):
        return self.__trackit_IssueTracker6

    @trackit_IssueTracker6.setter
    def trackit_IssueTracker6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_IssueTracker__trackit_IssueTracker6", None)
        self.__trackit_IssueTracker6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trackit_Member"):
                    opp_val = getattr(item, "trackit_Member", None)
                    
                    if opp_val == self:
                        setattr(item, "trackit_Member", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trackit_Member"):
                    opp_val = getattr(item, "trackit_Member", None)
                    
                    setattr(item, "trackit_Member", self)
                    

    @property
    def trackit_IssueTracker4(self):
        return self.__trackit_IssueTracker4

    @trackit_IssueTracker4.setter
    def trackit_IssueTracker4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_IssueTracker__trackit_IssueTracker4", None)
        self.__trackit_IssueTracker4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trackit_Issue"):
                    opp_val = getattr(item, "trackit_Issue", None)
                    
                    if opp_val == self:
                        setattr(item, "trackit_Issue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trackit_Issue"):
                    opp_val = getattr(item, "trackit_Issue", None)
                    
                    setattr(item, "trackit_Issue", self)
                    

    @property
    def trackit_IssueTracker2(self):
        return self.__trackit_IssueTracker2

    @trackit_IssueTracker2.setter
    def trackit_IssueTracker2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_IssueTracker__trackit_IssueTracker2", None)
        self.__trackit_IssueTracker2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trackit_Product"):
                    opp_val = getattr(item, "trackit_Product", None)
                    
                    if opp_val == self:
                        setattr(item, "trackit_Product", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trackit_Product"):
                    opp_val = getattr(item, "trackit_Product", None)
                    
                    setattr(item, "trackit_Product", self)
                    

    @property
    def trackit_IssueTracker(self):
        return self.__trackit_IssueTracker

    @trackit_IssueTracker.setter
    def trackit_IssueTracker(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trackit_IssueTracker__trackit_IssueTracker", None)
        self.__trackit_IssueTracker = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trackit_Team"):
                    opp_val = getattr(item, "trackit_Team", None)
                    
                    if opp_val == self:
                        setattr(item, "trackit_Team", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trackit_Team"):
                    opp_val = getattr(item, "trackit_Team", None)
                    
                    setattr(item, "trackit_Team", self)
                    
