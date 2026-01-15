from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class VersionState(Enum):
    IN_DEVELOPMENT = "IN_DEVELOPMENT"
    RELEASED = "RELEASED"
    PLANNED = "PLANNED"
class ReleaseType(Enum):
    nightly = "nightly"
    milestone = "milestone"
    release = "release"


############################################
# Definition of Classes
############################################

class web_Image:

    def __init__(self, src: str, label: str, web_Image: "web_Gallery" = None):
        self.src = src
        self.label = label
        self.web_Image = web_Image
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def src(self) -> str:
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src

    @property
    def web_Image(self):
        return self.__web_Image

    @web_Image.setter
    def web_Image(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_web_Image__web_Image", None)
        self.__web_Image = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "web_Gallery21"):
                opp_val = getattr(old_value, "web_Gallery21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "web_Gallery21"):
                opp_val = getattr(value, "web_Gallery21", None)
                if opp_val is None:
                    setattr(value, "web_Gallery21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class web_SocialInformation:

    def __init__(self, url: str, plusUrl: str, facebookUrl: str, twitterUrl: str, web_SocialInformation: "web_SocialBar" = None):
        self.url = url
        self.plusUrl = plusUrl
        self.facebookUrl = facebookUrl
        self.twitterUrl = twitterUrl
        self.web_SocialInformation = web_SocialInformation
        
    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def twitterUrl(self) -> str:
        return self.__twitterUrl

    @twitterUrl.setter
    def twitterUrl(self, twitterUrl: str):
        self.__twitterUrl = twitterUrl

    @property
    def plusUrl(self) -> str:
        return self.__plusUrl

    @plusUrl.setter
    def plusUrl(self, plusUrl: str):
        self.__plusUrl = plusUrl

    @property
    def facebookUrl(self) -> str:
        return self.__facebookUrl

    @facebookUrl.setter
    def facebookUrl(self, facebookUrl: str):
        self.__facebookUrl = facebookUrl

    @property
    def web_SocialInformation(self):
        return self.__web_SocialInformation

    @web_SocialInformation.setter
    def web_SocialInformation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_web_SocialInformation__web_SocialInformation", None)
        self.__web_SocialInformation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "web_SocialBar"):
                opp_val = getattr(old_value, "web_SocialBar", None)
                if opp_val == self:
                    setattr(old_value, "web_SocialBar", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "web_SocialBar"):
                opp_val = getattr(value, "web_SocialBar", None)
                setattr(value, "web_SocialBar", self)

class Container:

    pass
class Content:

    pass
class web_SocialBar(Content):

    pass
class web_ReleaseSection(Content):

    pass
class web_GalleryContent(Content):

    pass
class web_HtmlContent(Content):

    def __init__(self, data: str):
        self.data = data
        
    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data

class web_Content(ABC):

    pass
class web_Gallery:

    def __init__(self, label: str, web_Gallery: "web_Site" = None, web_Gallery23: "web_GalleryContent" = None, web_Gallery21: set["web_Image"] = None):
        self.label = label
        self.web_Gallery = web_Gallery
        self.web_Gallery23 = web_Gallery23
        self.web_Gallery21 = web_Gallery21 if web_Gallery21 is not None else set()
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def web_Gallery(self):
        return self.__web_Gallery

    @web_Gallery.setter
    def web_Gallery(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_web_Gallery__web_Gallery", None)
        self.__web_Gallery = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "web_Site11"):
                opp_val = getattr(old_value, "web_Site11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "web_Site11"):
                opp_val = getattr(value, "web_Site11", None)
                if opp_val is None:
                    setattr(value, "web_Site11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def web_Gallery23(self):
        return self.__web_Gallery23

    @web_Gallery23.setter
    def web_Gallery23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_web_Gallery__web_Gallery23", None)
        self.__web_Gallery23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "web_GalleryContent"):
                opp_val = getattr(old_value, "web_GalleryContent", None)
                if opp_val == self:
                    setattr(old_value, "web_GalleryContent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "web_GalleryContent"):
                opp_val = getattr(value, "web_GalleryContent", None)
                setattr(value, "web_GalleryContent", self)

    @property
    def web_Gallery21(self):
        return self.__web_Gallery21

    @web_Gallery21.setter
    def web_Gallery21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_web_Gallery__web_Gallery21", None)
        self.__web_Gallery21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "web_Image"):
                    opp_val = getattr(item, "web_Image", None)
                    
                    if opp_val == self:
                        setattr(item, "web_Image", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "web_Image"):
                    opp_val = getattr(item, "web_Image", None)
                    
                    setattr(item, "web_Image", self)
                    

class web_Version:

    def __init__(self, name: str, state: str, web_Version: "web_Site" = None, Version: "web_Release" = None, version: set["web_Release"] = None):
        self.name = name
        self.state = state
        self.web_Version = web_Version
        self.Version = Version
        self.version = version if version is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def web_Version(self):
        return self.__web_Version

    @web_Version.setter
    def web_Version(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_web_Version__web_Version", None)
        self.__web_Version = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "web_Site9"):
                opp_val = getattr(old_value, "web_Site9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "web_Site9"):
                opp_val = getattr(value, "web_Site9", None)
                if opp_val is None:
                    setattr(value, "web_Site9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_web_Version__version", None)
        self.__version = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Release"):
                    opp_val = getattr(item, "Release", None)
                    
                    if opp_val == self:
                        setattr(item, "Release", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Release"):
                    opp_val = getattr(item, "Release", None)
                    
                    setattr(item, "Release", self)
                    

    @property
    def Version(self):
        return self.__Version

    @Version.setter
    def Version(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_web_Version__Version", None)
        self.__Version = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "releases"):
                opp_val = getattr(old_value, "releases", None)
                if opp_val == self:
                    setattr(old_value, "releases", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "releases"):
                opp_val = getattr(value, "releases", None)
                setattr(value, "releases", self)

class web_Link:

    def __init__(self, target: str, label: str, web_Link: "web_Site" = None):
        self.target = target
        self.label = label
        self.web_Link = web_Link
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def target(self) -> str:
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target

    @property
    def web_Link(self):
        return self.__web_Link

    @web_Link.setter
    def web_Link(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_web_Link__web_Link", None)
        self.__web_Link = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "web_Site7"):
                opp_val = getattr(old_value, "web_Site7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "web_Site7"):
                opp_val = getattr(value, "web_Site7", None)
                if opp_val is None:
                    setattr(value, "web_Site7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class web_Author:

    def __init__(self, email: str, name: str, plusLink: str, web_Author: "web_Site" = None, web_Author15: "web_NewsEntry" = None):
        self.email = email
        self.name = name
        self.plusLink = plusLink
        self.web_Author = web_Author
        self.web_Author15 = web_Author15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def plusLink(self) -> str:
        return self.__plusLink

    @plusLink.setter
    def plusLink(self, plusLink: str):
        self.__plusLink = plusLink

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def web_Author15(self):
        return self.__web_Author15

    @web_Author15.setter
    def web_Author15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_web_Author__web_Author15", None)
        self.__web_Author15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "web_NewsEntry14"):
                opp_val = getattr(old_value, "web_NewsEntry14", None)
                if opp_val == self:
                    setattr(old_value, "web_NewsEntry14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "web_NewsEntry14"):
                opp_val = getattr(value, "web_NewsEntry14", None)
                setattr(value, "web_NewsEntry14", self)

    @property
    def web_Author(self):
        return self.__web_Author

    @web_Author.setter
    def web_Author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_web_Author__web_Author", None)
        self.__web_Author = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "web_Site5"):
                opp_val = getattr(old_value, "web_Site5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "web_Site5"):
                opp_val = getattr(value, "web_Site5", None)
                if opp_val is None:
                    setattr(value, "web_Site5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class web_Release:

    def __init__(self, buildId: str, type: str, name: str, releaseNotesLink: str, date: date, unqualifiedName: str, alternateMsiName: str, javadoc: bool, releases: "web_Version" = None, web_Release: "web_ReleaseSection" = None, Release: "web_Version" = None):
        self.buildId = buildId
        self.type = type
        self.name = name
        self.releaseNotesLink = releaseNotesLink
        self.date = date
        self.unqualifiedName = unqualifiedName
        self.alternateMsiName = alternateMsiName
        self.javadoc = javadoc
        self.releases = releases
        self.web_Release = web_Release
        self.Release = Release
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def alternateMsiName(self) -> str:
        return self.__alternateMsiName

    @alternateMsiName.setter
    def alternateMsiName(self, alternateMsiName: str):
        self.__alternateMsiName = alternateMsiName

    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def releaseNotesLink(self) -> str:
        return self.__releaseNotesLink

    @releaseNotesLink.setter
    def releaseNotesLink(self, releaseNotesLink: str):
        self.__releaseNotesLink = releaseNotesLink

    @property
    def javadoc(self) -> bool:
        return self.__javadoc

    @javadoc.setter
    def javadoc(self, javadoc: bool):
        self.__javadoc = javadoc

    @property
    def unqualifiedName(self) -> str:
        return self.__unqualifiedName

    @unqualifiedName.setter
    def unqualifiedName(self, unqualifiedName: str):
        self.__unqualifiedName = unqualifiedName

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def buildId(self) -> str:
        return self.__buildId

    @buildId.setter
    def buildId(self, buildId: str):
        self.__buildId = buildId

    @property
    def Release(self):
        return self.__Release

    @Release.setter
    def Release(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_web_Release__Release", None)
        self.__Release = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "version"):
                opp_val = getattr(old_value, "version", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "version"):
                opp_val = getattr(value, "version", None)
                if opp_val is None:
                    setattr(value, "version", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def releases(self):
        return self.__releases

    @releases.setter
    def releases(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_web_Release__releases", None)
        self.__releases = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Version"):
                opp_val = getattr(old_value, "Version", None)
                if opp_val == self:
                    setattr(old_value, "Version", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Version"):
                opp_val = getattr(value, "Version", None)
                setattr(value, "Version", self)

    @property
    def web_Release(self):
        return self.__web_Release

    @web_Release.setter
    def web_Release(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_web_Release__web_Release", None)
        self.__web_Release = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "web_ReleaseSection"):
                opp_val = getattr(old_value, "web_ReleaseSection", None)
                if opp_val == self:
                    setattr(old_value, "web_ReleaseSection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "web_ReleaseSection"):
                opp_val = getattr(value, "web_ReleaseSection", None)
                setattr(value, "web_ReleaseSection", self)

class Page:

    pass
class web_ContentPage(Page, Container):

    pass
class web_NewsFeedPage(Page):

    pass
class web_Container(ABC):

    pass
class web_NewsEntry(Container):

    def __init__(self, description: str, title: str, date: date, web_NewsEntry: "web_Site" = None, web_NewsEntry14: "web_Author" = None):
        self.description = description
        self.title = title
        self.date = date
        self.web_NewsEntry = web_NewsEntry
        self.web_NewsEntry14 = web_NewsEntry14
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def web_NewsEntry14(self):
        return self.__web_NewsEntry14

    @web_NewsEntry14.setter
    def web_NewsEntry14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_web_NewsEntry__web_NewsEntry14", None)
        self.__web_NewsEntry14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "web_Author15"):
                opp_val = getattr(old_value, "web_Author15", None)
                if opp_val == self:
                    setattr(old_value, "web_Author15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "web_Author15"):
                opp_val = getattr(value, "web_Author15", None)
                setattr(value, "web_Author15", self)

    @property
    def web_NewsEntry(self):
        return self.__web_NewsEntry

    @web_NewsEntry.setter
    def web_NewsEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_web_NewsEntry__web_NewsEntry", None)
        self.__web_NewsEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "web_Site3"):
                opp_val = getattr(old_value, "web_Site3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "web_Site3"):
                opp_val = getattr(value, "web_Site3", None)
                if opp_val is None:
                    setattr(value, "web_Site3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class web_FooterEntry:

    def __init__(self, name: str, link: str, web_FooterEntry: "web_Site" = None):
        self.name = name
        self.link = link
        self.web_FooterEntry = web_FooterEntry
        
    @property
    def link(self) -> str:
        return self.__link

    @link.setter
    def link(self, link: str):
        self.__link = link

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def web_FooterEntry(self):
        return self.__web_FooterEntry

    @web_FooterEntry.setter
    def web_FooterEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_web_FooterEntry__web_FooterEntry", None)
        self.__web_FooterEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "web_Site"):
                opp_val = getattr(old_value, "web_Site", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "web_Site"):
                opp_val = getattr(value, "web_Site", None)
                if opp_val is None:
                    setattr(value, "web_Site", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class web_Page(ABC):

    def __init__(self, id: str, name: str, Page: "web_Site" = None, pages: "web_Site" = None):
        self.id = id
        self.name = name
        self.Page = Page
        self.pages = pages
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_web_Page__pages", None)
        self.__pages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Site"):
                opp_val = getattr(old_value, "Site", None)
                if opp_val == self:
                    setattr(old_value, "Site", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Site"):
                opp_val = getattr(value, "Site", None)
                setattr(value, "Site", self)

    @property
    def Page(self):
        return self.__Page

    @Page.setter
    def Page(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_web_Page__Page", None)
        self.__Page = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "site"):
                opp_val = getattr(old_value, "site", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "site"):
                opp_val = getattr(value, "site", None)
                if opp_val is None:
                    setattr(value, "site", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class web_Site:

    def __init__(self, name: str, description: str, site: set["web_Page"] = None, web_Site: set["web_FooterEntry"] = None, web_Site3: set["web_NewsEntry"] = None, web_Site5: set["web_Author"] = None, web_Site7: set["web_Link"] = None, web_Site9: set["web_Version"] = None, web_Site11: set["web_Gallery"] = None, Site: "web_Page" = None):
        self.name = name
        self.description = description
        self.site = site if site is not None else set()
        self.web_Site = web_Site if web_Site is not None else set()
        self.web_Site3 = web_Site3 if web_Site3 is not None else set()
        self.web_Site5 = web_Site5 if web_Site5 is not None else set()
        self.web_Site7 = web_Site7 if web_Site7 is not None else set()
        self.web_Site9 = web_Site9 if web_Site9 is not None else set()
        self.web_Site11 = web_Site11 if web_Site11 is not None else set()
        self.Site = Site
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def web_Site9(self):
        return self.__web_Site9

    @web_Site9.setter
    def web_Site9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_web_Site__web_Site9", None)
        self.__web_Site9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "web_Version"):
                    opp_val = getattr(item, "web_Version", None)
                    
                    if opp_val == self:
                        setattr(item, "web_Version", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "web_Version"):
                    opp_val = getattr(item, "web_Version", None)
                    
                    setattr(item, "web_Version", self)
                    

    @property
    def web_Site3(self):
        return self.__web_Site3

    @web_Site3.setter
    def web_Site3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_web_Site__web_Site3", None)
        self.__web_Site3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "web_NewsEntry"):
                    opp_val = getattr(item, "web_NewsEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "web_NewsEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "web_NewsEntry"):
                    opp_val = getattr(item, "web_NewsEntry", None)
                    
                    setattr(item, "web_NewsEntry", self)
                    

    @property
    def web_Site5(self):
        return self.__web_Site5

    @web_Site5.setter
    def web_Site5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_web_Site__web_Site5", None)
        self.__web_Site5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "web_Author"):
                    opp_val = getattr(item, "web_Author", None)
                    
                    if opp_val == self:
                        setattr(item, "web_Author", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "web_Author"):
                    opp_val = getattr(item, "web_Author", None)
                    
                    setattr(item, "web_Author", self)
                    

    @property
    def web_Site(self):
        return self.__web_Site

    @web_Site.setter
    def web_Site(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_web_Site__web_Site", None)
        self.__web_Site = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "web_FooterEntry"):
                    opp_val = getattr(item, "web_FooterEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "web_FooterEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "web_FooterEntry"):
                    opp_val = getattr(item, "web_FooterEntry", None)
                    
                    setattr(item, "web_FooterEntry", self)
                    

    @property
    def site(self):
        return self.__site

    @site.setter
    def site(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_web_Site__site", None)
        self.__site = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Page"):
                    opp_val = getattr(item, "Page", None)
                    
                    if opp_val == self:
                        setattr(item, "Page", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Page"):
                    opp_val = getattr(item, "Page", None)
                    
                    setattr(item, "Page", self)
                    

    @property
    def web_Site11(self):
        return self.__web_Site11

    @web_Site11.setter
    def web_Site11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_web_Site__web_Site11", None)
        self.__web_Site11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "web_Gallery"):
                    opp_val = getattr(item, "web_Gallery", None)
                    
                    if opp_val == self:
                        setattr(item, "web_Gallery", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "web_Gallery"):
                    opp_val = getattr(item, "web_Gallery", None)
                    
                    setattr(item, "web_Gallery", self)
                    

    @property
    def Site(self):
        return self.__Site

    @Site.setter
    def Site(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_web_Site__Site", None)
        self.__Site = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pages"):
                opp_val = getattr(old_value, "pages", None)
                if opp_val == self:
                    setattr(old_value, "pages", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pages"):
                opp_val = getattr(value, "pages", None)
                setattr(value, "pages", self)

    @property
    def web_Site7(self):
        return self.__web_Site7

    @web_Site7.setter
    def web_Site7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_web_Site__web_Site7", None)
        self.__web_Site7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "web_Link"):
                    opp_val = getattr(item, "web_Link", None)
                    
                    if opp_val == self:
                        setattr(item, "web_Link", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "web_Link"):
                    opp_val = getattr(item, "web_Link", None)
                    
                    setattr(item, "web_Link", self)
                    
