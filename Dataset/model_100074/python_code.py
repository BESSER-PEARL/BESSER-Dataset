from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class TaskElement:

    pass
class AntScripts_Task(TaskElement):

    pass
class AntScripts_TaskParameter(TaskElement):

    pass
class Attribute:

    pass
class AntScripts_Property:

    def __init__(self, name: str, value: str, location: str, refid: str, resource: str, file: str, url: str, environment: str, classpath: str, classpathref: str, prefix: str):
        self.name = name
        self.value = value
        self.location = location
        self.refid = refid
        self.resource = resource
        self.file = file
        self.url = url
        self.environment = environment
        self.classpath = classpath
        self.classpathref = classpathref
        self.prefix = prefix
        
        pass
    @property
    def classpathref(self):
        return self.__classpathref

    @classpathref.setter
    def classpathref(self, classpathref: str):
        self.__classpathref = classpathref


    @property
    def environment(self):
        return self.__environment

    @environment.setter
    def environment(self, environment: str):
        self.__environment = environment


    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file


    @property
    def resource(self):
        return self.__resource

    @resource.setter
    def resource(self, resource: str):
        self.__resource = resource


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def classpath(self):
        return self.__classpath

    @classpath.setter
    def classpath(self, classpath: str):
        self.__classpath = classpath


    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


    @property
    def refid(self):
        return self.__refid

    @refid.setter
    def refid(self, refid: str):
        self.__refid = refid


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url


    @property
    def prefix(self):
        return self.__prefix

    @prefix.setter
    def prefix(self, prefix: str):
        self.__prefix = prefix


class Target:

    pass
class Property:

    pass
class CommentableElement:

    pass
class DescribableElement:

    pass
class NamedElement:

    pass
class AntScripts_Attribute(NamedElement):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class AntScripts_TaskElement(NamedElement, CommentableElement):

    pass
class AntScripts_Project(NamedElement, DescribableElement, CommentableElement):

    pass
class AntScripts_CommentableElement(ABC):

    def __init__(self, comment: str):
        self.comment = comment
        
        pass
    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment


class Task:

    pass
class AntScripts_Target(NamedElement, DescribableElement, CommentableElement):

    def __init__(self, if_: str, unless: str, AntScripts_Target: set["Task"] = None, AntScripts_Target8: set["Target"] = None):
        self.if_ = if_
        self.unless = unless
        self.AntScripts_Target = AntScripts_Target if AntScripts_Target is not None else set()
        self.AntScripts_Target8 = AntScripts_Target8 if AntScripts_Target8 is not None else set()
        
        pass
    @property
    def unless(self):
        return self.__unless

    @unless.setter
    def unless(self, unless: str):
        self.__unless = unless


    @property
    def if_(self):
        return self.__if_

    @if_.setter
    def if_(self, if_: str):
        self.__if_ = if_


    @property
    def AntScripts_Target(self):
        return self.__AntScripts_Target

    @AntScripts_Target.setter
    def AntScripts_Target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AntScripts_Target__AntScripts_Target", None)
        self.__AntScripts_Target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Task"):
                    opp_val = getattr(item, "Task", None)
                    
                    if opp_val == self:
                        setattr(item, "Task", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Task"):
                    opp_val = getattr(item, "Task", None)
                    
                    setattr(item, "Task", self)
                    

    @property
    def AntScripts_Target8(self):
        return self.__AntScripts_Target8

    @AntScripts_Target8.setter
    def AntScripts_Target8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AntScripts_Target__AntScripts_Target8", None)
        self.__AntScripts_Target8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Target9"):
                    opp_val = getattr(item, "Target9", None)
                    
                    if opp_val == self:
                        setattr(item, "Target9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Target9"):
                    opp_val = getattr(item, "Target9", None)
                    
                    setattr(item, "Target9", self)
                    

class AntScripts_DescribableElement(ABC):

    def __init__(self, description: str):
        self.description = description
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


class AntScripts_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

