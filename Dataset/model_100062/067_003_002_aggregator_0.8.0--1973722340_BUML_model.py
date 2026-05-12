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
BuildType: Enumeration = Enumeration(
    name="BuildType",
    literals={
            EnumerationLiteral(name="Continuous"),
			EnumerationLiteral(name="Nightly"),
			EnumerationLiteral(name="Integration"),
			EnumerationLiteral(name="Stable"),
			EnumerationLiteral(name="Release"),
			EnumerationLiteral(name="Maintenance")
    }
)

ARCH: Enumeration = Enumeration(
    name="ARCH",
    literals={
            EnumerationLiteral(name="x86"),
			EnumerationLiteral(name="ppc"),
			EnumerationLiteral(name="x86_64"),
			EnumerationLiteral(name="ppc64"),
			EnumerationLiteral(name="sparc"),
			EnumerationLiteral(name="ia64_32"),
			EnumerationLiteral(name="s390"),
			EnumerationLiteral(name="s390x")
    }
)

ArchiveFormat: Enumeration = Enumeration(
    name="ArchiveFormat",
    literals={
            EnumerationLiteral(name="zip"),
			EnumerationLiteral(name="tar")
    }
)

OS: Enumeration = Enumeration(
    name="OS",
    literals={
            EnumerationLiteral(name="win32"),
			EnumerationLiteral(name="linux"),
			EnumerationLiteral(name="macosx"),
			EnumerationLiteral(name="solaris"),
			EnumerationLiteral(name="hpux"),
			EnumerationLiteral(name="aix")
    }
)

WS: Enumeration = Enumeration(
    name="WS",
    literals={
            EnumerationLiteral(name="cocoa"),
			EnumerationLiteral(name="motif"),
			EnumerationLiteral(name="win32"),
			EnumerationLiteral(name="gtk"),
			EnumerationLiteral(name="carbon")
    }
)

# Classes
build_Platform = Class(name="build_Platform")
build_Config = Class(name="build_Config")
build_Map = Class(name="build_Map")
build_Category = Class(name="build_Category")
build_Contribution = Class(name="build_Contribution")
build_Product = Class(name="build_Product")
build_Compiler = Class(name="build_Compiler")
build_Promotion = Class(name="build_Promotion")
build_Contact = Class(name="build_Contact")
build_Build = Class(name="build_Build")
build_Feature = Class(name="build_Feature")
build_Bundle = Class(name="build_Bundle")
InstallationUnit = Class(name="InstallationUnit")
build_Repository = Class(name="build_Repository")
build_InstallationUnit = Class(name="build_InstallationUnit", is_abstract=True)

# build_Platform class attributes and methods
build_Platform_file: Property = Property(name="file", type=StringType)
build_Platform_location: Property = Property(name="location", type=StringType)
build_Platform_deltapack: Property = Property(name="deltapack", type=StringType)
build_Platform.attributes={build_Platform_file, build_Platform_location, build_Platform_deltapack}

# build_Config class attributes and methods
build_Config_os: Property = Property(name="os", type=StringType)
build_Config_ws: Property = Property(name="ws", type=StringType)
build_Config_arch: Property = Property(name="arch", type=StringType)
build_Config_archiveFormat: Property = Property(name="archiveFormat", type=StringType)
build_Config.attributes={build_Config_archiveFormat, build_Config_ws, build_Config_os, build_Config_arch}

# build_Map class attributes and methods
build_Map_root: Property = Property(name="root", type=StringType)
build_Map_repo: Property = Property(name="repo", type=StringType)
build_Map_tag: Property = Property(name="tag", type=StringType)
build_Map.attributes={build_Map_repo, build_Map_root, build_Map_tag}

# build_Category class attributes and methods
build_Category_name: Property = Property(name="name", type=StringType)
build_Category_label: Property = Property(name="label", type=StringType)
build_Category_description: Property = Property(name="description", type=StringType)
build_Category.attributes={build_Category_description, build_Category_name, build_Category_label}

# build_Contribution class attributes and methods
build_Contribution_label: Property = Property(name="label", type=StringType)
build_Contribution.attributes={build_Contribution_label}

# build_Product class attributes and methods

# build_Compiler class attributes and methods
build_Compiler_args: Property = Property(name="args", type=StringType)
build_Compiler_sourceVersion: Property = Property(name="sourceVersion", type=StringType)
build_Compiler_targetVersion: Property = Property(name="targetVersion", type=StringType)
build_Compiler_verbose: Property = Property(name="verbose", type=BooleanType)
build_Compiler_failOnError: Property = Property(name="failOnError", type=BooleanType)
build_Compiler_debugInfo: Property = Property(name="debugInfo", type=BooleanType)
build_Compiler.attributes={build_Compiler_args, build_Compiler_verbose, build_Compiler_targetVersion, build_Compiler_debugInfo, build_Compiler_failOnError, build_Compiler_sourceVersion}

# build_Promotion class attributes and methods
build_Promotion_uploadDirectory: Property = Property(name="uploadDirectory", type=StringType)
build_Promotion_downloadDirectory: Property = Property(name="downloadDirectory", type=StringType)
build_Promotion_incubating: Property = Property(name="incubating", type=BooleanType)
build_Promotion_baseURL: Property = Property(name="baseURL", type=StringType)
build_Promotion_buildAlias: Property = Property(name="buildAlias", type=StringType)
build_Promotion.attributes={build_Promotion_incubating, build_Promotion_downloadDirectory, build_Promotion_uploadDirectory, build_Promotion_baseURL, build_Promotion_buildAlias}

# build_Contact class attributes and methods
build_Contact_name: Property = Property(name="name", type=StringType)
build_Contact_email: Property = Property(name="email", type=StringType)
build_Contact.attributes={build_Contact_name, build_Contact_email}

# build_Build class attributes and methods
build_Build_buildRoot: Property = Property(name="buildRoot", type=StringType)
build_Build_fetchTag: Property = Property(name="fetchTag", type=StringType)
build_Build_label: Property = Property(name="label", type=StringType)
build_Build_date: Property = Property(name="date", type=StringType)
build_Build_time: Property = Property(name="time", type=StringType)
build_Build_launchVM: Property = Property(name="launchVM", type=StringType)
build_Build_builderURL: Property = Property(name="builderURL", type=StringType)
build_Build_sendmail: Property = Property(name="sendmail", type=BooleanType)
build_Build_type: Property = Property(name="type", type=StringType)
build_Build.attributes={build_Build_fetchTag, build_Build_time, build_Build_label, build_Build_date, build_Build_sendmail, build_Build_launchVM, build_Build_type, build_Build_builderURL, build_Build_buildRoot}

# build_Feature class attributes and methods
build_Feature_inProduct: Property = Property(name="inProduct", type=BooleanType)
build_Feature.attributes={build_Feature_inProduct}

# build_Bundle class attributes and methods

# InstallationUnit class attributes and methods

# build_Repository class attributes and methods
build_Repository_location: Property = Property(name="location", type=StringType)
build_Repository_label: Property = Property(name="label", type=StringType)
build_Repository.attributes={build_Repository_label, build_Repository_location}

# build_InstallationUnit class attributes and methods
build_InstallationUnit_id: Property = Property(name="id", type=StringType)
build_InstallationUnit_version: Property = Property(name="version", type=StringType)
build_InstallationUnit.attributes={build_InstallationUnit_version, build_InstallationUnit_id}

# Relationships
platforms0: BinaryAssociation = BinaryAssociation(
    name="platforms0",
    ends={
        Property(name="build_Platform", type=build_Build, multiplicity=Multiplicity(1, 1)),
        Property(name="build_Build", type=build_Platform, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
configs1: BinaryAssociation = BinaryAssociation(
    name="configs1",
    ends={
        Property(name="build_Config", type=build_Build, multiplicity=Multiplicity(1, 1)),
        Property(name="build_Build2", type=build_Config, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
map3: BinaryAssociation = BinaryAssociation(
    name="map3",
    ends={
        Property(name="build_Map", type=build_Build, multiplicity=Multiplicity(1, 1)),
        Property(name="build_Build4", type=build_Map, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
categories5: BinaryAssociation = BinaryAssociation(
    name="categories5",
    ends={
        Property(name="build_Category", type=build_Build, multiplicity=Multiplicity(1, 1)),
        Property(name="build_Build6", type=build_Category, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contributions7: BinaryAssociation = BinaryAssociation(
    name="contributions7",
    ends={
        Property(name="build_Contribution", type=build_Build, multiplicity=Multiplicity(1, 1)),
        Property(name="build_Build8", type=build_Contribution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
product9: BinaryAssociation = BinaryAssociation(
    name="product9",
    ends={
        Property(name="build_Product", type=build_Build, multiplicity=Multiplicity(1, 1)),
        Property(name="build_Build10", type=build_Product, multiplicity=Multiplicity(0, 1))
    }
)
base11: BinaryAssociation = BinaryAssociation(
    name="base11",
    ends={
        Property(name="build_Platform13", type=build_Build, multiplicity=Multiplicity(1, 1)),
        Property(name="build_Build12", type=build_Platform, multiplicity=Multiplicity(1, 1))
    }
)
builder14: BinaryAssociation = BinaryAssociation(
    name="builder14",
    ends={
        Property(name="build_Platform16", type=build_Build, multiplicity=Multiplicity(1, 1)),
        Property(name="build_Build15", type=build_Platform, multiplicity=Multiplicity(1, 1))
    }
)
compiler17: BinaryAssociation = BinaryAssociation(
    name="compiler17",
    ends={
        Property(name="build_Compiler", type=build_Build, multiplicity=Multiplicity(1, 1)),
        Property(name="build_Build18", type=build_Compiler, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
promotion19: BinaryAssociation = BinaryAssociation(
    name="promotion19",
    ends={
        Property(name="build_Promotion", type=build_Build, multiplicity=Multiplicity(1, 1)),
        Property(name="build_Build20", type=build_Promotion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
buildmaster21: BinaryAssociation = BinaryAssociation(
    name="buildmaster21",
    ends={
        Property(name="build_Contact", type=build_Build, multiplicity=Multiplicity(1, 1)),
        Property(name="build_Build22", type=build_Contact, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultMailList23: BinaryAssociation = BinaryAssociation(
    name="defaultMailList23",
    ends={
        Property(name="build_Contact25", type=build_Build, multiplicity=Multiplicity(1, 1)),
        Property(name="build_Build24", type=build_Contact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
config26: BinaryAssociation = BinaryAssociation(
    name="config26",
    ends={
        Property(name="build_Config28", type=build_Platform, multiplicity=Multiplicity(1, 1)),
        Property(name="build_Platform27", type=build_Config, multiplicity=Multiplicity(0, 1))
    }
)
features29: BinaryAssociation = BinaryAssociation(
    name="features29",
    ends={
        Property(name="Feature", type=build_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="category", type=build_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
contacts30: BinaryAssociation = BinaryAssociation(
    name="contacts30",
    ends={
        Property(name="build_Contact32", type=build_Contribution, multiplicity=Multiplicity(1, 1)),
        Property(name="build_Contribution31", type=build_Contact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features33: BinaryAssociation = BinaryAssociation(
    name="features33",
    ends={
        Property(name="build_Feature", type=build_Contribution, multiplicity=Multiplicity(1, 1)),
        Property(name="build_Contribution34", type=build_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repositories35: BinaryAssociation = BinaryAssociation(
    name="repositories35",
    ends={
        Property(name="build_Repository", type=build_Contribution, multiplicity=Multiplicity(1, 1)),
        Property(name="build_Contribution36", type=build_Repository, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bundles37: BinaryAssociation = BinaryAssociation(
    name="bundles37",
    ends={
        Property(name="build_Bundle", type=build_Contribution, multiplicity=Multiplicity(1, 1)),
        Property(name="build_Contribution38", type=build_Bundle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
products39: BinaryAssociation = BinaryAssociation(
    name="products39",
    ends={
        Property(name="build_Product41", type=build_Contribution, multiplicity=Multiplicity(1, 1)),
        Property(name="build_Contribution40", type=build_Product, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
category42: BinaryAssociation = BinaryAssociation(
    name="category42",
    ends={
        Property(name="Category", type=build_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="features", type=build_Category, multiplicity=Multiplicity(0, 9999))
    }
)
repo43: BinaryAssociation = BinaryAssociation(
    name="repo43",
    ends={
        Property(name="build_Repository44", type=build_InstallationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="build_InstallationUnit", type=build_Repository, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_build_Feature_InstallationUnit = Generalization(general=InstallationUnit, specific=build_Feature)
gen_build_Bundle_InstallationUnit = Generalization(general=InstallationUnit, specific=build_Bundle)
gen_build_Product_InstallationUnit = Generalization(general=InstallationUnit, specific=build_Product)

# Domain Model
domain_model = DomainModel(
    name="build",
    types={build_Platform, build_Config, build_Map, build_Category, build_Contribution, build_Product, build_Compiler, build_Promotion, build_Contact, build_Build, build_Feature, build_Bundle, InstallationUnit, build_Repository, build_InstallationUnit, BuildType, ARCH, ArchiveFormat, OS, WS},
    associations={platforms0, configs1, map3, categories5, contributions7, product9, base11, builder14, compiler17, promotion19, buildmaster21, defaultMailList23, config26, features29, contacts30, features33, repositories35, bundles37, products39, category42, repo43},
    generalizations={gen_build_Feature_InstallationUnit, gen_build_Bundle_InstallationUnit, gen_build_Product_InstallationUnit},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)