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
MavenProject_Project = Class(name="MavenProject_Project")
MavenProject_MailingList = Class(name="MavenProject_MailingList")
MailingList = Class(name="MailingList")
Person = Class(name="Person")
Build = Class(name="Build")
Project = Class(name="Project")
MavenProject_Build = Class(name="MavenProject_Build")
Resource = Class(name="Resource")
MavenProject_Resource = Class(name="MavenProject_Resource")
MavenProject_Person = Class(name="MavenProject_Person", is_abstract=True)
MavenProject_Developer = Class(name="MavenProject_Developer")
MavenProject_Contributor = Class(name="MavenProject_Contributor")

# MavenProject_Project class attributes and methods
MavenProject_Project_id: Property = Property(name="id", type=StringType)
MavenProject_Project_groupId: Property = Property(name="groupId", type=StringType)
MavenProject_Project_artifactId: Property = Property(name="artifactId", type=StringType)
MavenProject_Project_name: Property = Property(name="name", type=StringType)
MavenProject_Project_description: Property = Property(name="description", type=StringType)
MavenProject_Project.attributes={MavenProject_Project_artifactId, MavenProject_Project_name, MavenProject_Project_id, MavenProject_Project_description, MavenProject_Project_groupId}

# MavenProject_MailingList class attributes and methods
MavenProject_MailingList_name: Property = Property(name="name", type=StringType)
MavenProject_MailingList_subscribe: Property = Property(name="subscribe", type=StringType)
MavenProject_MailingList_unsubscribe: Property = Property(name="unsubscribe", type=StringType)
MavenProject_MailingList_post: Property = Property(name="post", type=StringType)
MavenProject_MailingList_archive: Property = Property(name="archive", type=StringType)
MavenProject_MailingList_otherArchives: Property = Property(name="otherArchives", type=StringType)
MavenProject_MailingList.attributes={MavenProject_MailingList_archive, MavenProject_MailingList_name, MavenProject_MailingList_unsubscribe, MavenProject_MailingList_post, MavenProject_MailingList_otherArchives, MavenProject_MailingList_subscribe}

# MailingList class attributes and methods

# Person class attributes and methods

# Build class attributes and methods

# Project class attributes and methods

# MavenProject_Build class attributes and methods
MavenProject_Build_defaultGoal: Property = Property(name="defaultGoal", type=StringType)
MavenProject_Build_sourceDirectory: Property = Property(name="sourceDirectory", type=StringType)
MavenProject_Build_unitTestSourceDirectory: Property = Property(name="unitTestSourceDirectory", type=StringType)
MavenProject_Build.attributes={MavenProject_Build_defaultGoal, MavenProject_Build_sourceDirectory, MavenProject_Build_unitTestSourceDirectory}

# Resource class attributes and methods

# MavenProject_Resource class attributes and methods
MavenProject_Resource_filtering: Property = Property(name="filtering", type=StringType)
MavenProject_Resource_directory: Property = Property(name="directory", type=StringType)
MavenProject_Resource_includes: Property = Property(name="includes", type=StringType)
MavenProject_Resource_excludes: Property = Property(name="excludes", type=StringType)
MavenProject_Resource_targetPath: Property = Property(name="targetPath", type=StringType)
MavenProject_Resource.attributes={MavenProject_Resource_excludes, MavenProject_Resource_filtering, MavenProject_Resource_includes, MavenProject_Resource_targetPath, MavenProject_Resource_directory}

# MavenProject_Person class attributes and methods
MavenProject_Person_name: Property = Property(name="name", type=StringType)
MavenProject_Person_email: Property = Property(name="email", type=StringType)
MavenProject_Person_url: Property = Property(name="url", type=StringType)
MavenProject_Person_organization: Property = Property(name="organization", type=StringType)
MavenProject_Person_organizationUrl: Property = Property(name="organizationUrl", type=StringType)
MavenProject_Person_roles: Property = Property(name="roles", type=StringType)
MavenProject_Person_timezone: Property = Property(name="timezone", type=StringType)
MavenProject_Person_properties: Property = Property(name="properties", type=StringType)
MavenProject_Person.attributes={MavenProject_Person_email, MavenProject_Person_organizationUrl, MavenProject_Person_roles, MavenProject_Person_timezone, MavenProject_Person_name, MavenProject_Person_properties, MavenProject_Person_url, MavenProject_Person_organization}

# MavenProject_Developer class attributes and methods
MavenProject_Developer_id: Property = Property(name="id", type=StringType)
MavenProject_Developer.attributes={MavenProject_Developer_id}

# MavenProject_Contributor class attributes and methods

# Relationships
mailingLists0: BinaryAssociation = BinaryAssociation(
    name="mailingLists0",
    ends={
        Property(name="MailingList", type=MavenProject_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="MavenProject_Project", type=MailingList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
developersAndContributors1: BinaryAssociation = BinaryAssociation(
    name="developersAndContributors1",
    ends={
        Property(name="Person", type=MavenProject_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="MavenProject_Project2", type=Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
build3: BinaryAssociation = BinaryAssociation(
    name="build3",
    ends={
        Property(name="Build", type=MavenProject_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="MavenProject_Project4", type=Build, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dependencies5: BinaryAssociation = BinaryAssociation(
    name="dependencies5",
    ends={
        Property(name="Project", type=MavenProject_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="MavenProject_Project6", type=Project, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uniTest7: BinaryAssociation = BinaryAssociation(
    name="uniTest7",
    ends={
        Property(name="Resource", type=MavenProject_Build, multiplicity=Multiplicity(1, 1)),
        Property(name="MavenProject_Build", type=Resource, multiplicity=Multiplicity(0, 9999))
    }
)
resources8: BinaryAssociation = BinaryAssociation(
    name="resources8",
    ends={
        Property(name="Resource10", type=MavenProject_Build, multiplicity=Multiplicity(1, 1)),
        Property(name="MavenProject_Build9", type=Resource, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_MavenProject_Developer_Person = Generalization(general=Person, specific=MavenProject_Developer)
gen_MavenProject_Contributor_Person = Generalization(general=Person, specific=MavenProject_Contributor)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={MavenProject_Project, MavenProject_MailingList, MailingList, Person, Build, Project, MavenProject_Build, Resource, MavenProject_Resource, MavenProject_Person, MavenProject_Developer, MavenProject_Contributor},
    associations={mailingLists0, developersAndContributors1, build3, dependencies5, uniTest7, resources8},
    generalizations={gen_MavenProject_Developer_Person, gen_MavenProject_Contributor_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)