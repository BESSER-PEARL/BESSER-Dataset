from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class SkillRequestStatus(Enum):
    OPEN = "OPEN"
    MATCHED = "MATCHED"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"
class UserSkillLevel(Enum):
    NOVICE = "NOVICE"
    COMPETENT = "COMPETENT"
    PROFICIENT = "PROFICIENT"
    EXPERT = "EXPERT"
    AUTHORITY = "AUTHORITY"
class SkillMatchStatus(Enum):
    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    COMPLETED = "COMPLETED"
    REJECTED = "REJECTED"
class TechSkillLevel(Enum):
    BEGINNER = "BEGINNER"
    INTERMEDIATE = "INTERMEDIATE"
    ADVANCED = "ADVANCED"
    EXPERT = "EXPERT"
    MASTERCLASS = "MASTERCLASS"
class SessionType(Enum):
    ONLINE = "ONLINE"
    OFFLINE = "OFFLINE"
    HYBRID = "HYBRID"

############################################
# Definition of Classes
############################################










class Session:

    def __init__(self, sessionId: int, sessionDate: date, duration: int, sessionType: SessionType, review: "Review" = None):
        self.sessionId = sessionId
        self.sessionDate = sessionDate
        self.duration = duration
        self.sessionType = sessionType
        self.review = review
        
        pass
    @property
    def sessionDate(self):
        return self.__sessionDate
    @sessionDate.setter
    def sessionDate(self, sessionDate: date):
        self.__sessionDate = sessionDate

    @property
    def sessionId(self):
        return self.__sessionId
    @sessionId.setter
    def sessionId(self, sessionId: int):
        self.__sessionId = sessionId

    @property
    def sessionType(self):
        return self.__sessionType
    @sessionType.setter
    def sessionType(self, sessionType: SessionType):
        self.__sessionType = sessionType

    @property
    def duration(self):
        return self.__duration
    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration

    @property
    def review(self):
        return self.__review
    @review.setter
    def review(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Session__review", None)
        self.__review = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "session_1"):
                opp_val = getattr(old_value, "session_1", None)
                if opp_val == self:
                    setattr(old_value, "session_1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "session_1"):
                opp_val = getattr(value, "session_1", None)
                setattr(value, "session_1", self)



class Review:

    def __init__(self, reviewId: int, rating: int, comments: str):
        self.reviewId = reviewId
        self.rating = rating
        self.comments = comments
        
        pass
    @property
    def comments(self):
        return self.__comments
    @comments.setter
    def comments(self, comments: str):
        self.__comments = comments

    @property
    def rating(self):
        return self.__rating
    @rating.setter
    def rating(self, rating: int):
        self.__rating = rating

    @property
    def reviewId(self):
        return self.__reviewId
    @reviewId.setter
    def reviewId(self, reviewId: int):
        self.__reviewId = reviewId



class SkillMatch:

    def __init__(self, matchId: int, createdDate: date, startDate: date, status: SkillMatchStatus, session: set["Session"] = None):
        self.matchId = matchId
        self.createdDate = createdDate
        self.startDate = startDate
        self.status = status
        self.session = session if session is not None else set()
        
        pass
    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: SkillMatchStatus):
        self.__status = status

    @property
    def startDate(self):
        return self.__startDate
    @startDate.setter
    def startDate(self, startDate: date):
        self.__startDate = startDate

    @property
    def createdDate(self):
        return self.__createdDate
    @createdDate.setter
    def createdDate(self, createdDate: date):
        self.__createdDate = createdDate

    @property
    def matchId(self):
        return self.__matchId
    @matchId.setter
    def matchId(self, matchId: int):
        self.__matchId = matchId

    @property
    def session(self):
        return self.__session
    @session.setter
    def session(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SkillMatch__session", None)
        self.__session = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "skillmatch_1"):
                    opp_val = getattr(item, "skillmatch_1", None)
                    
                    if opp_val == self:
                        setattr(item, "skillmatch_1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "skillmatch_1"):
                    opp_val = getattr(item, "skillmatch_1", None)
                    
                    setattr(item, "skillmatch_1", self)
                    



class SkillRequest:

    def __init__(self, requestId: int, createdDate: date, status: SkillRequestStatus, deadlineDate: date, skillmatch_2: "SkillMatch" = None, skill_1: "Skill" = None):
        self.requestId = requestId
        self.createdDate = createdDate
        self.status = status
        self.deadlineDate = deadlineDate
        self.skillmatch_2 = skillmatch_2
        self.skill_1 = skill_1
        
        pass
    @property
    def deadlineDate(self):
        return self.__deadlineDate
    @deadlineDate.setter
    def deadlineDate(self, deadlineDate: date):
        self.__deadlineDate = deadlineDate

    @property
    def requestId(self):
        return self.__requestId
    @requestId.setter
    def requestId(self, requestId: int):
        self.__requestId = requestId

    @property
    def createdDate(self):
        return self.__createdDate
    @createdDate.setter
    def createdDate(self, createdDate: date):
        self.__createdDate = createdDate

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: SkillRequestStatus):
        self.__status = status

    @property
    def skill_1(self):
        return self.__skill_1
    @skill_1.setter
    def skill_1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SkillRequest__skill_1", None)
        self.__skill_1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "skillrequest_2"):
                opp_val = getattr(old_value, "skillrequest_2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "skillrequest_2"):
                opp_val = getattr(value, "skillrequest_2", None)
                if opp_val is None:
                    setattr(value, "skillrequest_2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def skillmatch_2(self):
        return self.__skillmatch_2
    @skillmatch_2.setter
    def skillmatch_2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SkillRequest__skillmatch_2", None)
        self.__skillmatch_2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "skillrequest_1"):
                opp_val = getattr(old_value, "skillrequest_1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "skillrequest_1"):
                opp_val = getattr(value, "skillrequest_1", None)
                if opp_val is None:
                    setattr(value, "skillrequest_1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Skill:

    def __init__(self, skillId: int, skillName: str, category: str, description: str, skillLevel: TechSkillLevel, estimatedDuration: int, skillrequest_2: set["SkillRequest"] = None):
        self.skillId = skillId
        self.skillName = skillName
        self.category = category
        self.description = description
        self.skillLevel = skillLevel
        self.estimatedDuration = estimatedDuration
        self.skillrequest_2 = skillrequest_2 if skillrequest_2 is not None else set()
        
        pass
    @property
    def skillName(self):
        return self.__skillName
    @skillName.setter
    def skillName(self, skillName: str):
        self.__skillName = skillName

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def skillId(self):
        return self.__skillId
    @skillId.setter
    def skillId(self, skillId: int):
        self.__skillId = skillId

    @property
    def category(self):
        return self.__category
    @category.setter
    def category(self, category: str):
        self.__category = category

    @property
    def estimatedDuration(self):
        return self.__estimatedDuration
    @estimatedDuration.setter
    def estimatedDuration(self, estimatedDuration: int):
        self.__estimatedDuration = estimatedDuration

    @property
    def skillLevel(self):
        return self.__skillLevel
    @skillLevel.setter
    def skillLevel(self, skillLevel: TechSkillLevel):
        self.__skillLevel = skillLevel

    @property
    def skillrequest_2(self):
        return self.__skillrequest_2
    @skillrequest_2.setter
    def skillrequest_2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Skill__skillrequest_2", None)
        self.__skillrequest_2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "skill_1"):
                    opp_val = getattr(item, "skill_1", None)
                    
                    if opp_val == self:
                        setattr(item, "skill_1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "skill_1"):
                    opp_val = getattr(item, "skill_1", None)
                    
                    setattr(item, "skill_1", self)
                    



class UserSkill:

    def __init__(self, skillId: int, skillLevel: UserSkillLevel, yearsOfExperience: int, certification: bool, skill: "Skill" = None):
        self.skillId = skillId
        self.skillLevel = skillLevel
        self.yearsOfExperience = yearsOfExperience
        self.certification = certification
        self.skill = skill
        
        pass
    @property
    def yearsOfExperience(self):
        return self.__yearsOfExperience
    @yearsOfExperience.setter
    def yearsOfExperience(self, yearsOfExperience: int):
        self.__yearsOfExperience = yearsOfExperience

    @property
    def skillLevel(self):
        return self.__skillLevel
    @skillLevel.setter
    def skillLevel(self, skillLevel: UserSkillLevel):
        self.__skillLevel = skillLevel

    @property
    def certification(self):
        return self.__certification
    @certification.setter
    def certification(self, certification: bool):
        self.__certification = certification

    @property
    def skillId(self):
        return self.__skillId
    @skillId.setter
    def skillId(self, skillId: int):
        self.__skillId = skillId

    @property
    def skill(self):
        return self.__skill
    @skill.setter
    def skill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UserSkill__skill", None)
        self.__skill = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "userskill_1"):
                opp_val = getattr(old_value, "userskill_1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "userskill_1"):
                opp_val = getattr(value, "userskill_1", None)
                if opp_val is None:
                    setattr(value, "userskill_1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class User:

    def __init__(self, userId: int, userName: str, emailId: str, skillrequest: set["SkillRequest"] = None, userskill: set["UserSkill"] = None):
        self.userId = userId
        self.userName = userName
        self.emailId = emailId
        self.skillrequest = skillrequest if skillrequest is not None else set()
        self.userskill = userskill if userskill is not None else set()
        
        pass
    @property
    def userId(self):
        return self.__userId
    @userId.setter
    def userId(self, userId: int):
        self.__userId = userId

    @property
    def userName(self):
        return self.__userName
    @userName.setter
    def userName(self, userName: str):
        self.__userName = userName

    @property
    def emailId(self):
        return self.__emailId
    @emailId.setter
    def emailId(self, emailId: str):
        self.__emailId = emailId

    @property
    def userskill(self):
        return self.__userskill
    @userskill.setter
    def userskill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__userskill", None)
        self.__userskill = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user"):
                    opp_val = getattr(item, "user", None)
                    
                    if opp_val == self:
                        setattr(item, "user", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user"):
                    opp_val = getattr(item, "user", None)
                    
                    setattr(item, "user", self)
                    

    @property
    def skillrequest(self):
        return self.__skillrequest
    @skillrequest.setter
    def skillrequest(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__skillrequest", None)
        self.__skillrequest = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user_1"):
                    opp_val = getattr(item, "user_1", None)
                    
                    if opp_val == self:
                        setattr(item, "user_1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user_1"):
                    opp_val = getattr(item, "user_1", None)
                    
                    setattr(item, "user_1", self)
                    

