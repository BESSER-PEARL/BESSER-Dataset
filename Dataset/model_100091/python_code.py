from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class MavenProject_Person(ABC):

    def __init__(self, name: str, email: str, url: str, organization: str, organizationUrl: str, roles: str, timezone: str, properties: str):
        self.name = name
        self.email = email
        self.url = url
        self.organization = organization
        self.organizationUrl = organizationUrl
        self.roles = roles
        self.timezone = timezone
        self.properties = properties
        
        pass
    @property
    def properties(self):
        return self.__properties

    @properties.setter
    def properties(self, properties: str):
        self.__properties = properties


    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def timezone(self):
        return self.__timezone

    @timezone.setter
    def timezone(self, timezone: str):
        self.__timezone = timezone


    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email


    @property
    def organization(self):
        return self.__organization

    @organization.setter
    def organization(self, organization: str):
        self.__organization = organization


    @property
    def organizationUrl(self):
        return self.__organizationUrl

    @organizationUrl.setter
    def organizationUrl(self, organizationUrl: str):
        self.__organizationUrl = organizationUrl


    @property
    def roles(self):
        return self.__roles

    @roles.setter
    def roles(self, roles: str):
        self.__roles = roles


class MavenProject_Resource:

    def __init__(self, filtering: str, directory: str, includes: str, excludes: str, targetPath: str):
        self.filtering = filtering
        self.directory = directory
        self.includes = includes
        self.excludes = excludes
        self.targetPath = targetPath
        
        pass
    @property
    def directory(self):
        return self.__directory

    @directory.setter
    def directory(self, directory: str):
        self.__directory = directory


    @property
    def filtering(self):
        return self.__filtering

    @filtering.setter
    def filtering(self, filtering: str):
        self.__filtering = filtering


    @property
    def includes(self):
        return self.__includes

    @includes.setter
    def includes(self, includes: str):
        self.__includes = includes


    @property
    def excludes(self):
        return self.__excludes

    @excludes.setter
    def excludes(self, excludes: str):
        self.__excludes = excludes


    @property
    def targetPath(self):
        return self.__targetPath

    @targetPath.setter
    def targetPath(self, targetPath: str):
        self.__targetPath = targetPath


class Resource:

    pass
class MavenProject_Build:

    def __init__(self, defaultGoal: str, sourceDirectory: str, unitTestSourceDirectory: str, MavenProject_Build: set["Resource"] = None, MavenProject_Build9: set["Resource"] = None):
        self.defaultGoal = defaultGoal
        self.sourceDirectory = sourceDirectory
        self.unitTestSourceDirectory = unitTestSourceDirectory
        self.MavenProject_Build = MavenProject_Build if MavenProject_Build is not None else set()
        self.MavenProject_Build9 = MavenProject_Build9 if MavenProject_Build9 is not None else set()
        
        pass
    @property
    def unitTestSourceDirectory(self):
        return self.__unitTestSourceDirectory

    @unitTestSourceDirectory.setter
    def unitTestSourceDirectory(self, unitTestSourceDirectory: str):
        self.__unitTestSourceDirectory = unitTestSourceDirectory


    @property
    def defaultGoal(self):
        return self.__defaultGoal

    @defaultGoal.setter
    def defaultGoal(self, defaultGoal: str):
        self.__defaultGoal = defaultGoal


    @property
    def sourceDirectory(self):
        return self.__sourceDirectory

    @sourceDirectory.setter
    def sourceDirectory(self, sourceDirectory: str):
        self.__sourceDirectory = sourceDirectory


    @property
    def MavenProject_Build(self):
        return self.__MavenProject_Build

    @MavenProject_Build.setter
    def MavenProject_Build(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenProject_Build__MavenProject_Build", None)
        self.__MavenProject_Build = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Resource"):
                    opp_val = getattr(item, "Resource", None)
                    
                    if opp_val == self:
                        setattr(item, "Resource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Resource"):
                    opp_val = getattr(item, "Resource", None)
                    
                    setattr(item, "Resource", self)
                    

    @property
    def MavenProject_Build9(self):
        return self.__MavenProject_Build9

    @MavenProject_Build9.setter
    def MavenProject_Build9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenProject_Build__MavenProject_Build9", None)
        self.__MavenProject_Build9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Resource10"):
                    opp_val = getattr(item, "Resource10", None)
                    
                    if opp_val == self:
                        setattr(item, "Resource10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Resource10"):
                    opp_val = getattr(item, "Resource10", None)
                    
                    setattr(item, "Resource10", self)
                    

class Project:

    pass
class Build:

    pass
class Person:

    pass
class MavenProject_Developer(Person):

    def __init__(self, id: str, Person: "MavenProject_Project" = None):
        self.id = id
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


class MavenProject_Contributor(Person):

    pass
class MailingList:

    pass
class MavenProject_MailingList:

    def __init__(self, name: str, subscribe: str, unsubscribe: str, post: str, archive: str, otherArchives: str):
        self.name = name
        self.subscribe = subscribe
        self.unsubscribe = unsubscribe
        self.post = post
        self.archive = archive
        self.otherArchives = otherArchives
        
        pass
    @property
    def otherArchives(self):
        return self.__otherArchives

    @otherArchives.setter
    def otherArchives(self, otherArchives: str):
        self.__otherArchives = otherArchives


    @property
    def unsubscribe(self):
        return self.__unsubscribe

    @unsubscribe.setter
    def unsubscribe(self, unsubscribe: str):
        self.__unsubscribe = unsubscribe


    @property
    def archive(self):
        return self.__archive

    @archive.setter
    def archive(self, archive: str):
        self.__archive = archive


    @property
    def subscribe(self):
        return self.__subscribe

    @subscribe.setter
    def subscribe(self, subscribe: str):
        self.__subscribe = subscribe


    @property
    def post(self):
        return self.__post

    @post.setter
    def post(self, post: str):
        self.__post = post


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class MavenProject_Project:

    def __init__(self, id: str, groupId: str, artifactId: str, name: str, description: str, MavenProject_Project: set["MailingList"] = None, MavenProject_Project2: set["Person"] = None, MavenProject_Project4: "Build" = None, MavenProject_Project6: set["Project"] = None):
        self.id = id
        self.groupId = groupId
        self.artifactId = artifactId
        self.name = name
        self.description = description
        self.MavenProject_Project = MavenProject_Project if MavenProject_Project is not None else set()
        self.MavenProject_Project2 = MavenProject_Project2 if MavenProject_Project2 is not None else set()
        self.MavenProject_Project4 = MavenProject_Project4
        self.MavenProject_Project6 = MavenProject_Project6 if MavenProject_Project6 is not None else set()
        
        pass
    @property
    def groupId(self):
        return self.__groupId

    @groupId.setter
    def groupId(self, groupId: str):
        self.__groupId = groupId


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def artifactId(self):
        return self.__artifactId

    @artifactId.setter
    def artifactId(self, artifactId: str):
        self.__artifactId = artifactId


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def MavenProject_Project2(self):
        return self.__MavenProject_Project2

    @MavenProject_Project2.setter
    def MavenProject_Project2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenProject_Project__MavenProject_Project2", None)
        self.__MavenProject_Project2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person"):
                    opp_val = getattr(item, "Person", None)
                    
                    if opp_val == self:
                        setattr(item, "Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person"):
                    opp_val = getattr(item, "Person", None)
                    
                    setattr(item, "Person", self)
                    

    @property
    def MavenProject_Project6(self):
        return self.__MavenProject_Project6

    @MavenProject_Project6.setter
    def MavenProject_Project6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenProject_Project__MavenProject_Project6", None)
        self.__MavenProject_Project6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Project"):
                    opp_val = getattr(item, "Project", None)
                    
                    if opp_val == self:
                        setattr(item, "Project", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Project"):
                    opp_val = getattr(item, "Project", None)
                    
                    setattr(item, "Project", self)
                    

    @property
    def MavenProject_Project(self):
        return self.__MavenProject_Project

    @MavenProject_Project.setter
    def MavenProject_Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenProject_Project__MavenProject_Project", None)
        self.__MavenProject_Project = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MailingList"):
                    opp_val = getattr(item, "MailingList", None)
                    
                    if opp_val == self:
                        setattr(item, "MailingList", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MailingList"):
                    opp_val = getattr(item, "MailingList", None)
                    
                    setattr(item, "MailingList", self)
                    

    @property
    def MavenProject_Project4(self):
        return self.__MavenProject_Project4

    @MavenProject_Project4.setter
    def MavenProject_Project4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenProject_Project__MavenProject_Project4", None)
        self.__MavenProject_Project4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Build"):
                opp_val = getattr(old_value, "Build", None)
                if opp_val == self:
                    setattr(old_value, "Build", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Build"):
                opp_val = getattr(value, "Build", None)
                setattr(value, "Build", self)
