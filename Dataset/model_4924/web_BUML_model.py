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

# Enumerations
ReleaseType: Enumeration = Enumeration(
    name="ReleaseType",
    literals={
            EnumerationLiteral(name="nightly"),
			EnumerationLiteral(name="milestone"),
			EnumerationLiteral(name="release")
    }
)

VersionState: Enumeration = Enumeration(
    name="VersionState",
    literals={
            EnumerationLiteral(name="IN_DEVELOPMENT"),
			EnumerationLiteral(name="RELEASED"),
			EnumerationLiteral(name="PLANNED")
    }
)

# Classes
web_Site = Class(name="web::Site")
web_Page = Class(name="web::Page", is_abstract=True)
web_FooterEntry = Class(name="web::FooterEntry")
web_NewsEntry = Class(name="web::NewsEntry")
web_Version = Class(name="web::Version")
web_Gallery = Class(name="web::Gallery")
web_Content = Class(name="web::Content", is_abstract=True)
web_HtmlContent = Class(name="web::HtmlContent")
Content = Class(name="Content")
Container = Class(name="Container")
web_Container = Class(name="web::Container", is_abstract=True)
web_NewsFeedPage = Class(name="web::NewsFeedPage")
Page = Class(name="Page")
web_ContentPage = Class(name="web::ContentPage")
web_Release = Class(name="web::Release")
web_Author = Class(name="web::Author")
web_Link = Class(name="web::Link")
web_ReleaseSection = Class(name="web::ReleaseSection")
web_Image = Class(name="web::Image")
web_GalleryContent = Class(name="web::GalleryContent")
web_SocialBar = Class(name="web::SocialBar")
web_SocialInformation = Class(name="web::SocialInformation")

# web_Site class attributes and methods
web_Site_name: Property = Property(name="name", type=StringType)
web_Site_description: Property = Property(name="description", type=StringType)
web_Site.attributes={web_Site_description, web_Site_name}

# web_Page class attributes and methods
web_Page_id: Property = Property(name="id", type=StringType)
web_Page_name: Property = Property(name="name", type=StringType)
web_Page.attributes={web_Page_name, web_Page_id}

# web_FooterEntry class attributes and methods
web_FooterEntry_name: Property = Property(name="name", type=StringType)
web_FooterEntry_link: Property = Property(name="link", type=StringType)
web_FooterEntry.attributes={web_FooterEntry_name, web_FooterEntry_link}

# web_NewsEntry class attributes and methods
web_NewsEntry_title: Property = Property(name="title", type=StringType)
web_NewsEntry_date: Property = Property(name="date", type=DateType)
web_NewsEntry_description: Property = Property(name="description", type=StringType)
web_NewsEntry.attributes={web_NewsEntry_date, web_NewsEntry_title, web_NewsEntry_description}

# web_Version class attributes and methods
web_Version_name: Property = Property(name="name", type=StringType)
web_Version_state: Property = Property(name="state", type=StringType)
web_Version.attributes={web_Version_name, web_Version_state}

# web_Gallery class attributes and methods
web_Gallery_label: Property = Property(name="label", type=StringType)
web_Gallery.attributes={web_Gallery_label}

# web_Content class attributes and methods

# web_HtmlContent class attributes and methods
web_HtmlContent_data: Property = Property(name="data", type=StringType)
web_HtmlContent.attributes={web_HtmlContent_data}

# Content class attributes and methods

# Container class attributes and methods

# web_Container class attributes and methods

# web_NewsFeedPage class attributes and methods

# Page class attributes and methods

# web_ContentPage class attributes and methods

# web_Release class attributes and methods
web_Release_buildId: Property = Property(name="buildId", type=StringType)
web_Release_type: Property = Property(name="type", type=StringType)
web_Release_name: Property = Property(name="name", type=StringType)
web_Release_releaseNotesLink: Property = Property(name="releaseNotesLink", type=StringType)
web_Release_javadoc: Property = Property(name="javadoc", type=BooleanType)
web_Release_baseName: Property = Property(name="baseName", type=StringType)
web_Release_date: Property = Property(name="date", type=DateType)
web_Release_unqualifiedName: Property = Property(name="unqualifiedName", type=StringType)
web_Release_alternateMsiName: Property = Property(name="alternateMsiName", type=StringType)
web_Release.attributes={web_Release_alternateMsiName, web_Release_date, web_Release_javadoc, web_Release_type, web_Release_releaseNotesLink, web_Release_baseName, web_Release_unqualifiedName, web_Release_name, web_Release_buildId}

# web_Author class attributes and methods
web_Author_email: Property = Property(name="email", type=StringType)
web_Author_name: Property = Property(name="name", type=StringType)
web_Author_plusLink: Property = Property(name="plusLink", type=StringType)
web_Author.attributes={web_Author_plusLink, web_Author_name, web_Author_email}

# web_Link class attributes and methods
web_Link_target: Property = Property(name="target", type=StringType)
web_Link_label: Property = Property(name="label", type=StringType)
web_Link.attributes={web_Link_target, web_Link_label}

# web_ReleaseSection class attributes and methods

# web_Image class attributes and methods
web_Image_label: Property = Property(name="label", type=StringType)
web_Image_src: Property = Property(name="src", type=StringType)
web_Image.attributes={web_Image_label, web_Image_src}

# web_GalleryContent class attributes and methods

# web_SocialBar class attributes and methods

# web_SocialInformation class attributes and methods
web_SocialInformation_url: Property = Property(name="url", type=StringType)
web_SocialInformation_plusUrl: Property = Property(name="plusUrl", type=StringType)
web_SocialInformation_facebookUrl: Property = Property(name="facebookUrl", type=StringType)
web_SocialInformation_twitterUrl: Property = Property(name="twitterUrl", type=StringType)
web_SocialInformation.attributes={web_SocialInformation_plusUrl, web_SocialInformation_twitterUrl, web_SocialInformation_facebookUrl, web_SocialInformation_url}

# Relationships
pages0: BinaryAssociation = BinaryAssociation(
    name="pages0",
    ends={
        Property(name="Page", type=web_Site, multiplicity=Multiplicity(1, 1)),
        Property(name="site", type=web_Page, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
footer1: BinaryAssociation = BinaryAssociation(
    name="footer1",
    ends={
        Property(name="web_FooterEntry", type=web_Site, multiplicity=Multiplicity(1, 1)),
        Property(name="web_Site", type=web_FooterEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
versions8: BinaryAssociation = BinaryAssociation(
    name="versions8",
    ends={
        Property(name="web_Version", type=web_Site, multiplicity=Multiplicity(1, 1)),
        Property(name="web_Site9", type=web_Version, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
galleries10: BinaryAssociation = BinaryAssociation(
    name="galleries10",
    ends={
        Property(name="web_Gallery", type=web_Site, multiplicity=Multiplicity(1, 1)),
        Property(name="web_Site11", type=web_Gallery, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
site12: BinaryAssociation = BinaryAssociation(
    name="site12",
    ends={
        Property(name="Site", type=web_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="pages", type=web_Site, multiplicity=Multiplicity(0, 1))
    }
)
author13: BinaryAssociation = BinaryAssociation(
    name="author13",
    ends={
        Property(name="web_Author15", type=web_NewsEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="web_NewsEntry14", type=web_Author, multiplicity=Multiplicity(1, 1))
    }
)
content16: BinaryAssociation = BinaryAssociation(
    name="content16",
    ends={
        Property(name="web_Content", type=web_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="web_Container", type=web_Content, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
news2: BinaryAssociation = BinaryAssociation(
    name="news2",
    ends={
        Property(name="web_NewsEntry", type=web_Site, multiplicity=Multiplicity(1, 1)),
        Property(name="web_Site3", type=web_NewsEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
version17: BinaryAssociation = BinaryAssociation(
    name="version17",
    ends={
        Property(name="Version", type=web_Release, multiplicity=Multiplicity(1, 1)),
        Property(name="releases", type=web_Version, multiplicity=Multiplicity(0, 1))
    }
)
author4: BinaryAssociation = BinaryAssociation(
    name="author4",
    ends={
        Property(name="web_Author", type=web_Site, multiplicity=Multiplicity(1, 1)),
        Property(name="web_Site5", type=web_Author, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
links6: BinaryAssociation = BinaryAssociation(
    name="links6",
    ends={
        Property(name="web_Link", type=web_Site, multiplicity=Multiplicity(1, 1)),
        Property(name="web_Site7", type=web_Link, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
release18: BinaryAssociation = BinaryAssociation(
    name="release18",
    ends={
        Property(name="web_Release", type=web_ReleaseSection, multiplicity=Multiplicity(1, 1)),
        Property(name="web_ReleaseSection", type=web_Release, multiplicity=Multiplicity(0, 1))
    }
)
releases19: BinaryAssociation = BinaryAssociation(
    name="releases19",
    ends={
        Property(name="Release", type=web_Version, multiplicity=Multiplicity(1, 1)),
        Property(name="version", type=web_Release, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
images20: BinaryAssociation = BinaryAssociation(
    name="images20",
    ends={
        Property(name="web_Image", type=web_Gallery, multiplicity=Multiplicity(1, 1)),
        Property(name="web_Gallery21", type=web_Image, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
gallery22: BinaryAssociation = BinaryAssociation(
    name="gallery22",
    ends={
        Property(name="web_Gallery23", type=web_GalleryContent, multiplicity=Multiplicity(1, 1)),
        Property(name="web_GalleryContent", type=web_Gallery, multiplicity=Multiplicity(1, 1))
    }
)
information24: BinaryAssociation = BinaryAssociation(
    name="information24",
    ends={
        Property(name="web_SocialInformation", type=web_SocialBar, multiplicity=Multiplicity(1, 1)),
        Property(name="web_SocialBar", type=web_SocialInformation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_web_HtmlContent_Content = Generalization(general=Content, specific=web_HtmlContent)
gen_web_NewsEntry_Container = Generalization(general=Container, specific=web_NewsEntry)
gen_web_NewsFeedPage_Page = Generalization(general=Page, specific=web_NewsFeedPage)
gen_web_ContentPage_Container = Generalization(general=Container, specific=web_ContentPage)
gen_web_ContentPage_Page = Generalization(general=Page, specific=web_ContentPage)
gen_web_ReleaseSection_Content = Generalization(general=Content, specific=web_ReleaseSection)
gen_web_GalleryContent_Content = Generalization(general=Content, specific=web_GalleryContent)
gen_web_SocialBar_Content = Generalization(general=Content, specific=web_SocialBar)

# Domain Model
domain_model = DomainModel(
    name="web",
    types={web_Site, web_Page, web_FooterEntry, web_NewsEntry, web_Version, web_Gallery, web_Content, web_HtmlContent, Content, Container, web_Container, web_NewsFeedPage, Page, web_ContentPage, web_Release, web_Author, web_Link, web_ReleaseSection, web_Image, web_GalleryContent, web_SocialBar, web_SocialInformation, ReleaseType, VersionState},
    associations={pages0, footer1, versions8, galleries10, site12, author13, content16, news2, version17, author4, links6, release18, releases19, images20, gallery22, information24},
    generalizations={gen_web_HtmlContent_Content, gen_web_NewsEntry_Container, gen_web_NewsFeedPage_Page, gen_web_ContentPage_Container, gen_web_ContentPage_Page, gen_web_ReleaseSection_Content, gen_web_GalleryContent_Content, gen_web_SocialBar_Content},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)