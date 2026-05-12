from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Enum(Enum):
    pass

############################################
# Definition of Classes
############################################










class Rating:

    def __init__(self, value: int, type: Enum, has_ratings12: "User" = None, has_ratings14: "Course" = None, has_ratings16: "Comment" = None):
        self.value = value
        self.type = type
        self.has_ratings12 = has_ratings12
        self.has_ratings14 = has_ratings14
        self.has_ratings16 = has_ratings16
        
        pass
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: Enum):
        self.__type = type

    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def has_ratings16(self):
        return self.__has_ratings16
    @has_ratings16.setter
    def has_ratings16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Rating__has_ratings16", None)
        self.__has_ratings16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rates_comment17"):
                opp_val = getattr(old_value, "rates_comment17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rates_comment17"):
                opp_val = getattr(value, "rates_comment17", None)
                if opp_val is None:
                    setattr(value, "rates_comment17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def has_ratings14(self):
        return self.__has_ratings14
    @has_ratings14.setter
    def has_ratings14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Rating__has_ratings14", None)
        self.__has_ratings14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rates_course15"):
                opp_val = getattr(old_value, "rates_course15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rates_course15"):
                opp_val = getattr(value, "rates_course15", None)
                if opp_val is None:
                    setattr(value, "rates_course15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def has_ratings12(self):
        return self.__has_ratings12
    @has_ratings12.setter
    def has_ratings12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Rating__has_ratings12", None)
        self.__has_ratings12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "has_owner13"):
                opp_val = getattr(old_value, "has_owner13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "has_owner13"):
                opp_val = getattr(value, "has_owner13", None)
                if opp_val is None:
                    setattr(value, "has_owner13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Comment:

    def __init__(self, subject: str, text: str, rates_comment17: set["Rating"] = None, has_comments3: "Section" = None, has_comments7: "Course" = None, has_comments9: "User" = None):
        self.subject = subject
        self.text = text
        self.rates_comment17 = rates_comment17 if rates_comment17 is not None else set()
        self.has_comments3 = has_comments3
        self.has_comments7 = has_comments7
        self.has_comments9 = has_comments9
        
        pass
    @property
    def text(self):
        return self.__text
    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def subject(self):
        return self.__subject
    @subject.setter
    def subject(self, subject: str):
        self.__subject = subject

    @property
    def has_comments9(self):
        return self.__has_comments9
    @has_comments9.setter
    def has_comments9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Comment__has_comments9", None)
        self.__has_comments9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "has_owner8"):
                opp_val = getattr(old_value, "has_owner8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "has_owner8"):
                opp_val = getattr(value, "has_owner8", None)
                if opp_val is None:
                    setattr(value, "has_owner8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rates_comment17(self):
        return self.__rates_comment17
    @rates_comment17.setter
    def rates_comment17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Comment__rates_comment17", None)
        self.__rates_comment17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "has_ratings16"):
                    opp_val = getattr(item, "has_ratings16", None)
                    
                    if opp_val == self:
                        setattr(item, "has_ratings16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "has_ratings16"):
                    opp_val = getattr(item, "has_ratings16", None)
                    
                    setattr(item, "has_ratings16", self)
                    

    @property
    def has_comments3(self):
        return self.__has_comments3
    @has_comments3.setter
    def has_comments3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Comment__has_comments3", None)
        self.__has_comments3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "comments_section2"):
                opp_val = getattr(old_value, "comments_section2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "comments_section2"):
                opp_val = getattr(value, "comments_section2", None)
                if opp_val is None:
                    setattr(value, "comments_section2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def has_comments7(self):
        return self.__has_comments7
    @has_comments7.setter
    def has_comments7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Comment__has_comments7", None)
        self.__has_comments7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "comments_course6"):
                opp_val = getattr(old_value, "comments_course6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "comments_course6"):
                opp_val = getattr(value, "comments_course6", None)
                if opp_val is None:
                    setattr(value, "comments_course6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class SoundQuestion:

    def __init__(self, sound: str):
        self.sound = sound
        
        pass
    @property
    def sound(self):
        return self.__sound
    @sound.setter
    def sound(self, sound: str):
        self.__sound = sound



class ImageQuestion:

    def __init__(self, image: str):
        self.image = image
        
        pass
    @property
    def image(self):
        return self.__image
    @image.setter
    def image(self, image: str):
        self.__image = image



class TextQuestion:

    def __init__(self, text: str, caseSensitive: bool):
        self.text = text
        self.caseSensitive = caseSensitive
        
        pass
    @property
    def text(self):
        return self.__text
    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def caseSensitive(self):
        return self.__caseSensitive
    @caseSensitive.setter
    def caseSensitive(self, caseSensitive: bool):
        self.__caseSensitive = caseSensitive



class Question(ABC):

    def __init__(self, definition: str, explanation: str, has_question1: "Section" = None):
        self.definition = definition
        self.explanation = explanation
        self.has_question1 = has_question1
        
        pass
    @property
    def explanation(self):
        return self.__explanation
    @explanation.setter
    def explanation(self, explanation: str):
        self.__explanation = explanation

    @property
    def definition(self):
        return self.__definition
    @definition.setter
    def definition(self, definition: str):
        self.__definition = definition

    @property
    def has_question1(self):
        return self.__has_question1
    @has_question1.setter
    def has_question1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Question__has_question1", None)
        self.__has_question1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "has_section0"):
                opp_val = getattr(old_value, "has_section0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "has_section0"):
                opp_val = getattr(value, "has_section0", None)
                if opp_val is None:
                    setattr(value, "has_section0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Section:

    def __init__(self, material: str, has_section0: set["Question"] = None, comments_section2: set["Comment"] = None, has_sections5: "Course" = None):
        self.material = material
        self.has_section0 = has_section0 if has_section0 is not None else set()
        self.comments_section2 = comments_section2 if comments_section2 is not None else set()
        self.has_sections5 = has_sections5
        
        pass
    @property
    def material(self):
        return self.__material
    @material.setter
    def material(self, material: str):
        self.__material = material

    @property
    def has_section0(self):
        return self.__has_section0
    @has_section0.setter
    def has_section0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Section__has_section0", None)
        self.__has_section0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "has_question1"):
                    opp_val = getattr(item, "has_question1", None)
                    
                    if opp_val == self:
                        setattr(item, "has_question1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "has_question1"):
                    opp_val = getattr(item, "has_question1", None)
                    
                    setattr(item, "has_question1", self)
                    

    @property
    def comments_section2(self):
        return self.__comments_section2
    @comments_section2.setter
    def comments_section2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Section__comments_section2", None)
        self.__comments_section2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "has_comments3"):
                    opp_val = getattr(item, "has_comments3", None)
                    
                    if opp_val == self:
                        setattr(item, "has_comments3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "has_comments3"):
                    opp_val = getattr(item, "has_comments3", None)
                    
                    setattr(item, "has_comments3", self)
                    

    @property
    def has_sections5(self):
        return self.__has_sections5
    @has_sections5.setter
    def has_sections5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Section__has_sections5", None)
        self.__has_sections5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "has_course4"):
                opp_val = getattr(old_value, "has_course4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "has_course4"):
                opp_val = getattr(value, "has_course4", None)
                if opp_val is None:
                    setattr(value, "has_course4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Course:

    def __init__(self, name: str, description: str, material: str, has_courses11: set["User"] = None, rates_course15: set["Rating"] = None, owns18: "User" = None, has_course4: set["Section"] = None, comments_course6: set["Comment"] = None):
        self.name = name
        self.description = description
        self.material = material
        self.has_courses11 = has_courses11 if has_courses11 is not None else set()
        self.rates_course15 = rates_course15 if rates_course15 is not None else set()
        self.owns18 = owns18
        self.has_course4 = has_course4 if has_course4 is not None else set()
        self.comments_course6 = comments_course6 if comments_course6 is not None else set()
        
        pass
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
    def material(self):
        return self.__material
    @material.setter
    def material(self, material: str):
        self.__material = material

    @property
    def rates_course15(self):
        return self.__rates_course15
    @rates_course15.setter
    def rates_course15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Course__rates_course15", None)
        self.__rates_course15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "has_ratings14"):
                    opp_val = getattr(item, "has_ratings14", None)
                    
                    if opp_val == self:
                        setattr(item, "has_ratings14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "has_ratings14"):
                    opp_val = getattr(item, "has_ratings14", None)
                    
                    setattr(item, "has_ratings14", self)
                    

    @property
    def has_courses11(self):
        return self.__has_courses11
    @has_courses11.setter
    def has_courses11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Course__has_courses11", None)
        self.__has_courses11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "has_users10"):
                    opp_val = getattr(item, "has_users10", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "has_users10"):
                    opp_val = getattr(item, "has_users10", None)
                    
                    if opp_val is None:
                        setattr(item, "has_users10", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def has_course4(self):
        return self.__has_course4
    @has_course4.setter
    def has_course4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Course__has_course4", None)
        self.__has_course4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "has_sections5"):
                    opp_val = getattr(item, "has_sections5", None)
                    
                    if opp_val == self:
                        setattr(item, "has_sections5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "has_sections5"):
                    opp_val = getattr(item, "has_sections5", None)
                    
                    setattr(item, "has_sections5", self)
                    

    @property
    def owns18(self):
        return self.__owns18
    @owns18.setter
    def owns18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Course__owns18", None)
        self.__owns18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "has_owner19"):
                opp_val = getattr(old_value, "has_owner19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "has_owner19"):
                opp_val = getattr(value, "has_owner19", None)
                if opp_val is None:
                    setattr(value, "has_owner19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def comments_course6(self):
        return self.__comments_course6
    @comments_course6.setter
    def comments_course6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Course__comments_course6", None)
        self.__comments_course6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "has_comments7"):
                    opp_val = getattr(item, "has_comments7", None)
                    
                    if opp_val == self:
                        setattr(item, "has_comments7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "has_comments7"):
                    opp_val = getattr(item, "has_comments7", None)
                    
                    setattr(item, "has_comments7", self)
                    



class User:

    def __init__(self, nickname: str, avatar: str, level: int, bio: str, email: str, links: str, has_users10: set["Course"] = None, has_owner13: set["Rating"] = None, has_owner19: set["Course"] = None, has_owner8: set["Comment"] = None):
        self.nickname = nickname
        self.avatar = avatar
        self.level = level
        self.bio = bio
        self.email = email
        self.links = links
        self.has_users10 = has_users10 if has_users10 is not None else set()
        self.has_owner13 = has_owner13 if has_owner13 is not None else set()
        self.has_owner19 = has_owner19 if has_owner19 is not None else set()
        self.has_owner8 = has_owner8 if has_owner8 is not None else set()
        
        pass
    @property
    def level(self):
        return self.__level
    @level.setter
    def level(self, level: int):
        self.__level = level

    @property
    def nickname(self):
        return self.__nickname
    @nickname.setter
    def nickname(self, nickname: str):
        self.__nickname = nickname

    @property
    def links(self):
        return self.__links
    @links.setter
    def links(self, links: str):
        self.__links = links

    @property
    def avatar(self):
        return self.__avatar
    @avatar.setter
    def avatar(self, avatar: str):
        self.__avatar = avatar

    @property
    def bio(self):
        return self.__bio
    @bio.setter
    def bio(self, bio: str):
        self.__bio = bio

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def has_owner13(self):
        return self.__has_owner13
    @has_owner13.setter
    def has_owner13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__has_owner13", None)
        self.__has_owner13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "has_ratings12"):
                    opp_val = getattr(item, "has_ratings12", None)
                    
                    if opp_val == self:
                        setattr(item, "has_ratings12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "has_ratings12"):
                    opp_val = getattr(item, "has_ratings12", None)
                    
                    setattr(item, "has_ratings12", self)
                    

    @property
    def has_owner8(self):
        return self.__has_owner8
    @has_owner8.setter
    def has_owner8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__has_owner8", None)
        self.__has_owner8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "has_comments9"):
                    opp_val = getattr(item, "has_comments9", None)
                    
                    if opp_val == self:
                        setattr(item, "has_comments9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "has_comments9"):
                    opp_val = getattr(item, "has_comments9", None)
                    
                    setattr(item, "has_comments9", self)
                    

    @property
    def has_users10(self):
        return self.__has_users10
    @has_users10.setter
    def has_users10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__has_users10", None)
        self.__has_users10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "has_courses11"):
                    opp_val = getattr(item, "has_courses11", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "has_courses11"):
                    opp_val = getattr(item, "has_courses11", None)
                    
                    if opp_val is None:
                        setattr(item, "has_courses11", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def has_owner19(self):
        return self.__has_owner19
    @has_owner19.setter
    def has_owner19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__has_owner19", None)
        self.__has_owner19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "owns18"):
                    opp_val = getattr(item, "owns18", None)
                    
                    if opp_val == self:
                        setattr(item, "owns18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "owns18"):
                    opp_val = getattr(item, "owns18", None)
                    
                    setattr(item, "owns18", self)
                    

