from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class BZ_BZEvent:

    def __init__(self, author: str, date: date, field: str, oldValue: str, newValue: str, issueId: int, events: "BZ_BZIssue" = None, BZEvent: "BZ_BZIssue" = None):
        self.author = author
        self.date = date
        self.field = field
        self.oldValue = oldValue
        self.newValue = newValue
        self.issueId = issueId
        self.events = events
        self.BZEvent = BZEvent
        
        pass
    @property
    def issueId(self):
        return self.__issueId

    @issueId.setter
    def issueId(self, issueId: int):
        self.__issueId = issueId


    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date


    @property
    def oldValue(self):
        return self.__oldValue

    @oldValue.setter
    def oldValue(self, oldValue: str):
        self.__oldValue = oldValue


    @property
    def field(self):
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field


    @property
    def newValue(self):
        return self.__newValue

    @newValue.setter
    def newValue(self, newValue: str):
        self.__newValue = newValue


    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author


    @property
    def events(self):
        return self.__events

    @events.setter
    def events(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BZ_BZEvent__events", None)
        self.__events = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BZIssue32"):
                opp_val = getattr(old_value, "BZIssue32", None)
                if opp_val == self:
                    setattr(old_value, "BZIssue32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BZIssue32"):
                opp_val = getattr(value, "BZIssue32", None)
                setattr(value, "BZIssue32", self)

    @property
    def BZEvent(self):
        return self.__BZEvent

    @BZEvent.setter
    def BZEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BZ_BZEvent__BZEvent", None)
        self.__BZEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "issue22"):
                opp_val = getattr(old_value, "issue22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "issue22"):
                opp_val = getattr(value, "issue22", None)
                if opp_val is None:
                    setattr(value, "issue22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BZ_BZComment:

    def __init__(self, issueId: int, commentId: str, commentAuthor: str, commentTime: date, commentHTML: str, commentText: str, comments: "BZ_BZIssue" = None, BZComment: "BZ_BZIssue" = None):
        self.issueId = issueId
        self.commentId = commentId
        self.commentAuthor = commentAuthor
        self.commentTime = commentTime
        self.commentHTML = commentHTML
        self.commentText = commentText
        self.comments = comments
        self.BZComment = BZComment
        
        pass
    @property
    def commentId(self):
        return self.__commentId

    @commentId.setter
    def commentId(self, commentId: str):
        self.__commentId = commentId


    @property
    def issueId(self):
        return self.__issueId

    @issueId.setter
    def issueId(self, issueId: int):
        self.__issueId = issueId


    @property
    def commentAuthor(self):
        return self.__commentAuthor

    @commentAuthor.setter
    def commentAuthor(self, commentAuthor: str):
        self.__commentAuthor = commentAuthor


    @property
    def commentText(self):
        return self.__commentText

    @commentText.setter
    def commentText(self, commentText: str):
        self.__commentText = commentText


    @property
    def commentTime(self):
        return self.__commentTime

    @commentTime.setter
    def commentTime(self, commentTime: date):
        self.__commentTime = commentTime


    @property
    def commentHTML(self):
        return self.__commentHTML

    @commentHTML.setter
    def commentHTML(self, commentHTML: str):
        self.__commentHTML = commentHTML


    @property
    def comments(self):
        return self.__comments

    @comments.setter
    def comments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BZ_BZComment__comments", None)
        self.__comments = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BZIssue30"):
                opp_val = getattr(old_value, "BZIssue30", None)
                if opp_val == self:
                    setattr(old_value, "BZIssue30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BZIssue30"):
                opp_val = getattr(value, "BZIssue30", None)
                setattr(value, "BZIssue30", self)

    @property
    def BZComment(self):
        return self.__BZComment

    @BZComment.setter
    def BZComment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BZ_BZComment__BZComment", None)
        self.__BZComment = value
        
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

class BZ_BZIssue:

    def __init__(self, issueId: int, issueTitle: str, issueURL: str, status: str, productName: str, componentName: str, classification: str, version: str, platform: str, importance: str, milestone: str, assignedTo: str, keywords: str, referenceURL: str, dependsOn: str, blocks: str, reportedBy: str, reportedByUsername: str, reportedOn: date, lastModifiedOn: date, ccList: str, seeAlso: str, latestCommit: str, versionFixedIn: str, BZIssue12: "BZ_BZComponent" = None, BZIssue: "BZ_BZRepo" = None, BZIssue10: "BZ_BZProduct" = None, issues27: "BZ_BZProduct" = None, BZIssue30: "BZ_BZComment" = None, BZIssue32: "BZ_BZEvent" = None, issues: "BZ_BZRepo" = None, issue: set["BZ_BZComment"] = None, issue22: set["BZ_BZEvent"] = None, issues24: "BZ_BZComponent" = None):
        self.issueId = issueId
        self.issueTitle = issueTitle
        self.issueURL = issueURL
        self.status = status
        self.productName = productName
        self.componentName = componentName
        self.classification = classification
        self.version = version
        self.platform = platform
        self.importance = importance
        self.milestone = milestone
        self.assignedTo = assignedTo
        self.keywords = keywords
        self.referenceURL = referenceURL
        self.dependsOn = dependsOn
        self.blocks = blocks
        self.reportedBy = reportedBy
        self.reportedByUsername = reportedByUsername
        self.reportedOn = reportedOn
        self.lastModifiedOn = lastModifiedOn
        self.ccList = ccList
        self.seeAlso = seeAlso
        self.latestCommit = latestCommit
        self.versionFixedIn = versionFixedIn
        self.BZIssue12 = BZIssue12
        self.BZIssue = BZIssue
        self.BZIssue10 = BZIssue10
        self.issues27 = issues27
        self.BZIssue30 = BZIssue30
        self.BZIssue32 = BZIssue32
        self.issues = issues
        self.issue = issue if issue is not None else set()
        self.issue22 = issue22 if issue22 is not None else set()
        self.issues24 = issues24
        
        pass
    @property
    def blocks(self):
        return self.__blocks

    @blocks.setter
    def blocks(self, blocks: str):
        self.__blocks = blocks


    @property
    def issueId(self):
        return self.__issueId

    @issueId.setter
    def issueId(self, issueId: int):
        self.__issueId = issueId


    @property
    def ccList(self):
        return self.__ccList

    @ccList.setter
    def ccList(self, ccList: str):
        self.__ccList = ccList


    @property
    def issueURL(self):
        return self.__issueURL

    @issueURL.setter
    def issueURL(self, issueURL: str):
        self.__issueURL = issueURL


    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status


    @property
    def versionFixedIn(self):
        return self.__versionFixedIn

    @versionFixedIn.setter
    def versionFixedIn(self, versionFixedIn: str):
        self.__versionFixedIn = versionFixedIn


    @property
    def lastModifiedOn(self):
        return self.__lastModifiedOn

    @lastModifiedOn.setter
    def lastModifiedOn(self, lastModifiedOn: date):
        self.__lastModifiedOn = lastModifiedOn


    @property
    def issueTitle(self):
        return self.__issueTitle

    @issueTitle.setter
    def issueTitle(self, issueTitle: str):
        self.__issueTitle = issueTitle


    @property
    def reportedByUsername(self):
        return self.__reportedByUsername

    @reportedByUsername.setter
    def reportedByUsername(self, reportedByUsername: str):
        self.__reportedByUsername = reportedByUsername


    @property
    def productName(self):
        return self.__productName

    @productName.setter
    def productName(self, productName: str):
        self.__productName = productName


    @property
    def latestCommit(self):
        return self.__latestCommit

    @latestCommit.setter
    def latestCommit(self, latestCommit: str):
        self.__latestCommit = latestCommit


    @property
    def componentName(self):
        return self.__componentName

    @componentName.setter
    def componentName(self, componentName: str):
        self.__componentName = componentName


    @property
    def keywords(self):
        return self.__keywords

    @keywords.setter
    def keywords(self, keywords: str):
        self.__keywords = keywords


    @property
    def importance(self):
        return self.__importance

    @importance.setter
    def importance(self, importance: str):
        self.__importance = importance


    @property
    def milestone(self):
        return self.__milestone

    @milestone.setter
    def milestone(self, milestone: str):
        self.__milestone = milestone


    @property
    def seeAlso(self):
        return self.__seeAlso

    @seeAlso.setter
    def seeAlso(self, seeAlso: str):
        self.__seeAlso = seeAlso


    @property
    def dependsOn(self):
        return self.__dependsOn

    @dependsOn.setter
    def dependsOn(self, dependsOn: str):
        self.__dependsOn = dependsOn


    @property
    def assignedTo(self):
        return self.__assignedTo

    @assignedTo.setter
    def assignedTo(self, assignedTo: str):
        self.__assignedTo = assignedTo


    @property
    def referenceURL(self):
        return self.__referenceURL

    @referenceURL.setter
    def referenceURL(self, referenceURL: str):
        self.__referenceURL = referenceURL


    @property
    def classification(self):
        return self.__classification

    @classification.setter
    def classification(self, classification: str):
        self.__classification = classification


    @property
    def platform(self):
        return self.__platform

    @platform.setter
    def platform(self, platform: str):
        self.__platform = platform


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def reportedBy(self):
        return self.__reportedBy

    @reportedBy.setter
    def reportedBy(self, reportedBy: str):
        self.__reportedBy = reportedBy


    @property
    def reportedOn(self):
        return self.__reportedOn

    @reportedOn.setter
    def reportedOn(self, reportedOn: date):
        self.__reportedOn = reportedOn


    @property
    def issues27(self):
        return self.__issues27

    @issues27.setter
    def issues27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BZ_BZIssue__issues27", None)
        self.__issues27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BZProduct28"):
                opp_val = getattr(old_value, "BZProduct28", None)
                if opp_val == self:
                    setattr(old_value, "BZProduct28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BZProduct28"):
                opp_val = getattr(value, "BZProduct28", None)
                setattr(value, "BZProduct28", self)

    @property
    def issue(self):
        return self.__issue

    @issue.setter
    def issue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BZ_BZIssue__issue", None)
        self.__issue = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BZComment"):
                    opp_val = getattr(item, "BZComment", None)
                    
                    if opp_val == self:
                        setattr(item, "BZComment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BZComment"):
                    opp_val = getattr(item, "BZComment", None)
                    
                    setattr(item, "BZComment", self)
                    

    @property
    def issues24(self):
        return self.__issues24

    @issues24.setter
    def issues24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BZ_BZIssue__issues24", None)
        self.__issues24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BZComponent25"):
                opp_val = getattr(old_value, "BZComponent25", None)
                if opp_val == self:
                    setattr(old_value, "BZComponent25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BZComponent25"):
                opp_val = getattr(value, "BZComponent25", None)
                setattr(value, "BZComponent25", self)

    @property
    def BZIssue12(self):
        return self.__BZIssue12

    @BZIssue12.setter
    def BZIssue12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BZ_BZIssue__BZIssue12", None)
        self.__BZIssue12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component"):
                opp_val = getattr(old_value, "component", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component"):
                opp_val = getattr(value, "component", None)
                if opp_val is None:
                    setattr(value, "component", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BZIssue10(self):
        return self.__BZIssue10

    @BZIssue10.setter
    def BZIssue10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BZ_BZIssue__BZIssue10", None)
        self.__BZIssue10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product9"):
                opp_val = getattr(old_value, "product9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product9"):
                opp_val = getattr(value, "product9", None)
                if opp_val is None:
                    setattr(value, "product9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def issue22(self):
        return self.__issue22

    @issue22.setter
    def issue22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BZ_BZIssue__issue22", None)
        self.__issue22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BZEvent"):
                    opp_val = getattr(item, "BZEvent", None)
                    
                    if opp_val == self:
                        setattr(item, "BZEvent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BZEvent"):
                    opp_val = getattr(item, "BZEvent", None)
                    
                    setattr(item, "BZEvent", self)
                    

    @property
    def issues(self):
        return self.__issues

    @issues.setter
    def issues(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BZ_BZIssue__issues", None)
        self.__issues = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BZRepo19"):
                opp_val = getattr(old_value, "BZRepo19", None)
                if opp_val == self:
                    setattr(old_value, "BZRepo19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BZRepo19"):
                opp_val = getattr(value, "BZRepo19", None)
                setattr(value, "BZRepo19", self)

    @property
    def BZIssue(self):
        return self.__BZIssue

    @BZIssue.setter
    def BZIssue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BZ_BZIssue__BZIssue", None)
        self.__BZIssue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repo4"):
                opp_val = getattr(old_value, "repo4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repo4"):
                opp_val = getattr(value, "repo4", None)
                if opp_val is None:
                    setattr(value, "repo4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BZIssue32(self):
        return self.__BZIssue32

    @BZIssue32.setter
    def BZIssue32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BZ_BZIssue__BZIssue32", None)
        self.__BZIssue32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "events"):
                opp_val = getattr(old_value, "events", None)
                if opp_val == self:
                    setattr(old_value, "events", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "events"):
                opp_val = getattr(value, "events", None)
                setattr(value, "events", self)

    @property
    def BZIssue30(self):
        return self.__BZIssue30

    @BZIssue30.setter
    def BZIssue30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BZ_BZIssue__BZIssue30", None)
        self.__BZIssue30 = value
        
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

class BZ_BZComponent:

    def __init__(self, componentId: str, componentURL: str, componentDescription: str, defaultAssignee: str, component: set["BZ_BZIssue"] = None, components: "BZ_BZProduct" = None, components16: "BZ_BZRepo" = None, BZComponent: "BZ_BZRepo" = None, BZComponent7: "BZ_BZProduct" = None, BZComponent25: "BZ_BZIssue" = None):
        self.componentId = componentId
        self.componentURL = componentURL
        self.componentDescription = componentDescription
        self.defaultAssignee = defaultAssignee
        self.component = component if component is not None else set()
        self.components = components
        self.components16 = components16
        self.BZComponent = BZComponent
        self.BZComponent7 = BZComponent7
        self.BZComponent25 = BZComponent25
        
        pass
    @property
    def componentURL(self):
        return self.__componentURL

    @componentURL.setter
    def componentURL(self, componentURL: str):
        self.__componentURL = componentURL


    @property
    def componentDescription(self):
        return self.__componentDescription

    @componentDescription.setter
    def componentDescription(self, componentDescription: str):
        self.__componentDescription = componentDescription


    @property
    def defaultAssignee(self):
        return self.__defaultAssignee

    @defaultAssignee.setter
    def defaultAssignee(self, defaultAssignee: str):
        self.__defaultAssignee = defaultAssignee


    @property
    def componentId(self):
        return self.__componentId

    @componentId.setter
    def componentId(self, componentId: str):
        self.__componentId = componentId


    @property
    def component(self):
        return self.__component

    @component.setter
    def component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BZ_BZComponent__component", None)
        self.__component = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BZIssue12"):
                    opp_val = getattr(item, "BZIssue12", None)
                    
                    if opp_val == self:
                        setattr(item, "BZIssue12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BZIssue12"):
                    opp_val = getattr(item, "BZIssue12", None)
                    
                    setattr(item, "BZIssue12", self)
                    

    @property
    def BZComponent(self):
        return self.__BZComponent

    @BZComponent.setter
    def BZComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BZ_BZComponent__BZComponent", None)
        self.__BZComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repo2"):
                opp_val = getattr(old_value, "repo2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repo2"):
                opp_val = getattr(value, "repo2", None)
                if opp_val is None:
                    setattr(value, "repo2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def components16(self):
        return self.__components16

    @components16.setter
    def components16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BZ_BZComponent__components16", None)
        self.__components16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BZRepo17"):
                opp_val = getattr(old_value, "BZRepo17", None)
                if opp_val == self:
                    setattr(old_value, "BZRepo17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BZRepo17"):
                opp_val = getattr(value, "BZRepo17", None)
                setattr(value, "BZRepo17", self)

    @property
    def BZComponent25(self):
        return self.__BZComponent25

    @BZComponent25.setter
    def BZComponent25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BZ_BZComponent__BZComponent25", None)
        self.__BZComponent25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "issues24"):
                opp_val = getattr(old_value, "issues24", None)
                if opp_val == self:
                    setattr(old_value, "issues24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "issues24"):
                opp_val = getattr(value, "issues24", None)
                setattr(value, "issues24", self)

    @property
    def components(self):
        return self.__components

    @components.setter
    def components(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BZ_BZComponent__components", None)
        self.__components = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BZProduct14"):
                opp_val = getattr(old_value, "BZProduct14", None)
                if opp_val == self:
                    setattr(old_value, "BZProduct14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BZProduct14"):
                opp_val = getattr(value, "BZProduct14", None)
                setattr(value, "BZProduct14", self)

    @property
    def BZComponent7(self):
        return self.__BZComponent7

    @BZComponent7.setter
    def BZComponent7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BZ_BZComponent__BZComponent7", None)
        self.__BZComponent7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product"):
                opp_val = getattr(old_value, "product", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product"):
                opp_val = getattr(value, "product", None)
                if opp_val is None:
                    setattr(value, "product", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BZ_BZProduct:

    def __init__(self, productId: str, productDescription: str, productURL: str, BZProduct: "BZ_BZRepo" = None, BZProduct14: "BZ_BZComponent" = None, products: "BZ_BZRepo" = None, product: set["BZ_BZComponent"] = None, product9: set["BZ_BZIssue"] = None, BZProduct28: "BZ_BZIssue" = None):
        self.productId = productId
        self.productDescription = productDescription
        self.productURL = productURL
        self.BZProduct = BZProduct
        self.BZProduct14 = BZProduct14
        self.products = products
        self.product = product if product is not None else set()
        self.product9 = product9 if product9 is not None else set()
        self.BZProduct28 = BZProduct28
        
        pass
    @property
    def productDescription(self):
        return self.__productDescription

    @productDescription.setter
    def productDescription(self, productDescription: str):
        self.__productDescription = productDescription


    @property
    def productId(self):
        return self.__productId

    @productId.setter
    def productId(self, productId: str):
        self.__productId = productId


    @property
    def productURL(self):
        return self.__productURL

    @productURL.setter
    def productURL(self, productURL: str):
        self.__productURL = productURL


    @property
    def BZProduct(self):
        return self.__BZProduct

    @BZProduct.setter
    def BZProduct(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BZ_BZProduct__BZProduct", None)
        self.__BZProduct = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repo"):
                opp_val = getattr(old_value, "repo", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repo"):
                opp_val = getattr(value, "repo", None)
                if opp_val is None:
                    setattr(value, "repo", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def product(self):
        return self.__product

    @product.setter
    def product(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BZ_BZProduct__product", None)
        self.__product = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BZComponent7"):
                    opp_val = getattr(item, "BZComponent7", None)
                    
                    if opp_val == self:
                        setattr(item, "BZComponent7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BZComponent7"):
                    opp_val = getattr(item, "BZComponent7", None)
                    
                    setattr(item, "BZComponent7", self)
                    

    @property
    def product9(self):
        return self.__product9

    @product9.setter
    def product9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BZ_BZProduct__product9", None)
        self.__product9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BZIssue10"):
                    opp_val = getattr(item, "BZIssue10", None)
                    
                    if opp_val == self:
                        setattr(item, "BZIssue10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BZIssue10"):
                    opp_val = getattr(item, "BZIssue10", None)
                    
                    setattr(item, "BZIssue10", self)
                    

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BZ_BZProduct__products", None)
        self.__products = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BZRepo"):
                opp_val = getattr(old_value, "BZRepo", None)
                if opp_val == self:
                    setattr(old_value, "BZRepo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BZRepo"):
                opp_val = getattr(value, "BZRepo", None)
                setattr(value, "BZRepo", self)

    @property
    def BZProduct28(self):
        return self.__BZProduct28

    @BZProduct28.setter
    def BZProduct28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BZ_BZProduct__BZProduct28", None)
        self.__BZProduct28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "issues27"):
                opp_val = getattr(old_value, "issues27", None)
                if opp_val == self:
                    setattr(old_value, "issues27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "issues27"):
                opp_val = getattr(value, "issues27", None)
                setattr(value, "issues27", self)

    @property
    def BZProduct14(self):
        return self.__BZProduct14

    @BZProduct14.setter
    def BZProduct14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BZ_BZProduct__BZProduct14", None)
        self.__BZProduct14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "components"):
                opp_val = getattr(old_value, "components", None)
                if opp_val == self:
                    setattr(old_value, "components", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "components"):
                opp_val = getattr(value, "components", None)
                setattr(value, "components", self)

class BZ_BZRepo:

    def __init__(self, repoURL: str, repo: set["BZ_BZProduct"] = None, BZRepo17: "BZ_BZComponent" = None, repo2: set["BZ_BZComponent"] = None, repo4: set["BZ_BZIssue"] = None, BZRepo: "BZ_BZProduct" = None, BZRepo19: "BZ_BZIssue" = None):
        self.repoURL = repoURL
        self.repo = repo if repo is not None else set()
        self.BZRepo17 = BZRepo17
        self.repo2 = repo2 if repo2 is not None else set()
        self.repo4 = repo4 if repo4 is not None else set()
        self.BZRepo = BZRepo
        self.BZRepo19 = BZRepo19
        
        pass
    @property
    def repoURL(self):
        return self.__repoURL

    @repoURL.setter
    def repoURL(self, repoURL: str):
        self.__repoURL = repoURL


    @property
    def BZRepo19(self):
        return self.__BZRepo19

    @BZRepo19.setter
    def BZRepo19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BZ_BZRepo__BZRepo19", None)
        self.__BZRepo19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "issues"):
                opp_val = getattr(old_value, "issues", None)
                if opp_val == self:
                    setattr(old_value, "issues", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "issues"):
                opp_val = getattr(value, "issues", None)
                setattr(value, "issues", self)

    @property
    def repo2(self):
        return self.__repo2

    @repo2.setter
    def repo2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BZ_BZRepo__repo2", None)
        self.__repo2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BZComponent"):
                    opp_val = getattr(item, "BZComponent", None)
                    
                    if opp_val == self:
                        setattr(item, "BZComponent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BZComponent"):
                    opp_val = getattr(item, "BZComponent", None)
                    
                    setattr(item, "BZComponent", self)
                    

    @property
    def BZRepo(self):
        return self.__BZRepo

    @BZRepo.setter
    def BZRepo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BZ_BZRepo__BZRepo", None)
        self.__BZRepo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "products"):
                opp_val = getattr(old_value, "products", None)
                if opp_val == self:
                    setattr(old_value, "products", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "products"):
                opp_val = getattr(value, "products", None)
                setattr(value, "products", self)

    @property
    def repo4(self):
        return self.__repo4

    @repo4.setter
    def repo4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BZ_BZRepo__repo4", None)
        self.__repo4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BZIssue"):
                    opp_val = getattr(item, "BZIssue", None)
                    
                    if opp_val == self:
                        setattr(item, "BZIssue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BZIssue"):
                    opp_val = getattr(item, "BZIssue", None)
                    
                    setattr(item, "BZIssue", self)
                    

    @property
    def repo(self):
        return self.__repo

    @repo.setter
    def repo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BZ_BZRepo__repo", None)
        self.__repo = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BZProduct"):
                    opp_val = getattr(item, "BZProduct", None)
                    
                    if opp_val == self:
                        setattr(item, "BZProduct", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BZProduct"):
                    opp_val = getattr(item, "BZProduct", None)
                    
                    setattr(item, "BZProduct", self)
                    

    @property
    def BZRepo17(self):
        return self.__BZRepo17

    @BZRepo17.setter
    def BZRepo17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BZ_BZRepo__BZRepo17", None)
        self.__BZRepo17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "components16"):
                opp_val = getattr(old_value, "components16", None)
                if opp_val == self:
                    setattr(old_value, "components16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "components16"):
                opp_val = getattr(value, "components16", None)
                setattr(value, "components16", self)
