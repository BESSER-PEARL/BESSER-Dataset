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
PriorityType: Enumeration = Enumeration(
    name="PriorityType",
    literals={
            EnumerationLiteral(name="standard"),
			EnumerationLiteral(name="required"),
			EnumerationLiteral(name="important"),
			EnumerationLiteral(name="optional"),
			EnumerationLiteral(name="extra")
    }
)

StatusType: Enumeration = Enumeration(
    name="StatusType",
    literals={
            EnumerationLiteral(name="installed"),
			EnumerationLiteral(name="not_installed"),
			EnumerationLiteral(name="half_configured"),
			EnumerationLiteral(name="half_installed"),
			EnumerationLiteral(name="config_files"),
			EnumerationLiteral(name="unpacked")
    }
)

VersionType: Enumeration = Enumeration(
    name="VersionType",
    literals={
            EnumerationLiteral(name="eq"),
			EnumerationLiteral(name="ge"),
			EnumerationLiteral(name="le"),
			EnumerationLiteral(name="lt"),
			EnumerationLiteral(name="llt"),
			EnumerationLiteral(name="gt"),
			EnumerationLiteral(name="ggt")
    }
)

# Classes
mancoosimm_NamedElement = Class(name="mancoosimm::NamedElement", is_abstract=True)
mancoosimm_NotInstalledPackage = Class(name="mancoosimm::NotInstalledPackage")
mancoosimm_ConfigFilesPackage = Class(name="mancoosimm::ConfigFilesPackage")
mancoosimm_Configuration = Class(name="mancoosimm::Configuration")
NamedElement = Class(name="NamedElement")
mancoosimm_FileSystem = Class(name="mancoosimm::FileSystem")
mancoosimm_Environment = Class(name="mancoosimm::Environment")
mancoosimm_InstalledPackage = Class(name="mancoosimm::InstalledPackage")
Package = Class(name="Package")
mancoosimm_UnpackedPackage = Class(name="mancoosimm::UnpackedPackage")
mancoosimm_HalfConfiguredPackage = Class(name="mancoosimm::HalfConfiguredPackage")
mancoosimm_HalfInstalledPackage = Class(name="mancoosimm::HalfInstalledPackage")
mancoosimm_Package = Class(name="mancoosimm::Package", is_abstract=True)
mancoosimm_PackageSetting = Class(name="mancoosimm::PackageSetting")
mancoosimm_SrcPackage = Class(name="mancoosimm::SrcPackage")
mancoosimm_Dependence = Class(name="mancoosimm::Dependence", is_abstract=True)
mancoosimm_VirtualPackage = Class(name="mancoosimm::VirtualPackage")
mancoosimm_File = Class(name="mancoosimm::File")
mancoosimm_DocumentationFile = Class(name="mancoosimm::DocumentationFile")
mancoosimm_Conflict = Class(name="mancoosimm::Conflict", is_abstract=True)
UnpackedPackage = Class(name="UnpackedPackage")
InstalledPackage = Class(name="InstalledPackage")
mancoosimm_BinPackage = Class(name="mancoosimm::BinPackage")
mancoosimm_AndDep = Class(name="mancoosimm::AndDep")
mancoosimm_OrDep = Class(name="mancoosimm::OrDep")
mancoosimm_SingleDep = Class(name="mancoosimm::SingleDep")
Dependence = Class(name="Dependence")
mancoosimm_Atom = Class(name="mancoosimm::Atom")
mancoosimm_AndInv = Class(name="mancoosimm::AndInv")
mancoosimm_OrInv = Class(name="mancoosimm::OrInv")
mancoosimm_NotInv = Class(name="mancoosimm::NotInv")
mancoosimm_Invariant = Class(name="mancoosimm::Invariant")
mancoosimm_Service = Class(name="mancoosimm::Service")
mancoosimm_DesktopDB = Class(name="mancoosimm::DesktopDB")
mancoosimm_MimeTypeHandlerCache = Class(name="mancoosimm::MimeTypeHandlerCache")
mancoosimm_LibraryCache = Class(name="mancoosimm::LibraryCache")
mancoosimm_Alternative = Class(name="mancoosimm::Alternative")
mancoosimm_User = Class(name="mancoosimm::User")
mancoosimm_Group = Class(name="mancoosimm::Group")
mancoosimm_EmacsPackage = Class(name="mancoosimm::EmacsPackage")
mancoosimm_IconCache = Class(name="mancoosimm::IconCache")
mancoosimm_GConf = Class(name="mancoosimm::GConf")
mancoosimm_Menu = Class(name="mancoosimm::Menu")
mancoosimm_SkeeperCatalog = Class(name="mancoosimm::SkeeperCatalog")
mancoosimm_SGMLCatalog = Class(name="mancoosimm::SGMLCatalog")
mancoosimm_ModuleCache = Class(name="mancoosimm::ModuleCache")
mancoosimm_XFontCache = Class(name="mancoosimm::XFontCache")
mancoosimm_ApplicationMenuCatalog = Class(name="mancoosimm::ApplicationMenuCatalog")
mancoosimm_MenuEntry = Class(name="mancoosimm::MenuEntry")
mancoosimm_Boot = Class(name="mancoosimm::Boot")
File = Class(name="File")
mancoosimm_InformationFile = Class(name="mancoosimm::InformationFile")
mancoosimm_MimeTypeHandler = Class(name="mancoosimm::MimeTypeHandler")
mancoosimm_MimeType = Class(name="mancoosimm::MimeType")
mancoosimm_XFont = Class(name="mancoosimm::XFont")
mancoosimm_SharedLibrary = Class(name="mancoosimm::SharedLibrary")
mancoosimm_Module = Class(name="mancoosimm::Module")
mancoosimm_SGMLDocument = Class(name="mancoosimm::SGMLDocument")
mancoosimm_SkeeperDocument = Class(name="mancoosimm::SkeeperDocument")
mancoosimm_SingleConflict = Class(name="mancoosimm::SingleConflict")
Conflict = Class(name="Conflict")
mancoosimm_AndConflict = Class(name="mancoosimm::AndConflict")
mancoosimm_OrConflict = Class(name="mancoosimm::OrConflict")

# mancoosimm_NamedElement class attributes and methods
mancoosimm_NamedElement_name: Property = Property(name="name", type=StringType)
mancoosimm_NamedElement.attributes={mancoosimm_NamedElement_name}

# mancoosimm_NotInstalledPackage class attributes and methods

# mancoosimm_ConfigFilesPackage class attributes and methods
mancoosimm_ConfigFilesPackage_maintainer: Property = Property(name="maintainer", type=StringType)
mancoosimm_ConfigFilesPackage_checkSum: Property = Property(name="checkSum", type=StringType)
mancoosimm_ConfigFilesPackage_description: Property = Property(name="description", type=StringType)
mancoosimm_ConfigFilesPackage_section: Property = Property(name="section", type=StringType)
mancoosimm_ConfigFilesPackage_tag: Property = Property(name="tag", type=StringType)
mancoosimm_ConfigFilesPackage_priority: Property = Property(name="priority", type=StringType)
mancoosimm_ConfigFilesPackage_uploaders: Property = Property(name="uploaders", type=StringType)
mancoosimm_ConfigFilesPackage.attributes={mancoosimm_ConfigFilesPackage_priority, mancoosimm_ConfigFilesPackage_tag, mancoosimm_ConfigFilesPackage_maintainer, mancoosimm_ConfigFilesPackage_description, mancoosimm_ConfigFilesPackage_section, mancoosimm_ConfigFilesPackage_checkSum, mancoosimm_ConfigFilesPackage_uploaders}

# mancoosimm_Configuration class attributes and methods
mancoosimm_Configuration_creationTime: Property = Property(name="creationTime", type=StringType)
mancoosimm_Configuration_systemType: Property = Property(name="systemType", type=StringType)
mancoosimm_Configuration.attributes={mancoosimm_Configuration_systemType, mancoosimm_Configuration_creationTime}

# NamedElement class attributes and methods

# mancoosimm_FileSystem class attributes and methods

# mancoosimm_Environment class attributes and methods

# mancoosimm_InstalledPackage class attributes and methods
mancoosimm_InstalledPackage_installedSize: Property = Property(name="installedSize", type=IntegerType)
mancoosimm_InstalledPackage_maintainer: Property = Property(name="maintainer", type=StringType)
mancoosimm_InstalledPackage_fileSize: Property = Property(name="fileSize", type=IntegerType)
mancoosimm_InstalledPackage_checkSum: Property = Property(name="checkSum", type=StringType)
mancoosimm_InstalledPackage_description: Property = Property(name="description", type=StringType)
mancoosimm_InstalledPackage_section: Property = Property(name="section", type=StringType)
mancoosimm_InstalledPackage_tag: Property = Property(name="tag", type=StringType)
mancoosimm_InstalledPackage_priority: Property = Property(name="priority", type=StringType)
mancoosimm_InstalledPackage_uploaders: Property = Property(name="uploaders", type=StringType)
mancoosimm_InstalledPackage.attributes={mancoosimm_InstalledPackage_checkSum, mancoosimm_InstalledPackage_description, mancoosimm_InstalledPackage_section, mancoosimm_InstalledPackage_tag, mancoosimm_InstalledPackage_maintainer, mancoosimm_InstalledPackage_priority, mancoosimm_InstalledPackage_installedSize, mancoosimm_InstalledPackage_uploaders, mancoosimm_InstalledPackage_fileSize}

# Package class attributes and methods

# mancoosimm_UnpackedPackage class attributes and methods
mancoosimm_UnpackedPackage_priority: Property = Property(name="priority", type=StringType)
mancoosimm_UnpackedPackage_uploaders: Property = Property(name="uploaders", type=StringType)
mancoosimm_UnpackedPackage_maintainer: Property = Property(name="maintainer", type=StringType)
mancoosimm_UnpackedPackage_checkSum: Property = Property(name="checkSum", type=StringType)
mancoosimm_UnpackedPackage_description: Property = Property(name="description", type=StringType)
mancoosimm_UnpackedPackage_section: Property = Property(name="section", type=StringType)
mancoosimm_UnpackedPackage_tag: Property = Property(name="tag", type=StringType)
mancoosimm_UnpackedPackage.attributes={mancoosimm_UnpackedPackage_checkSum, mancoosimm_UnpackedPackage_priority, mancoosimm_UnpackedPackage_section, mancoosimm_UnpackedPackage_description, mancoosimm_UnpackedPackage_uploaders, mancoosimm_UnpackedPackage_tag, mancoosimm_UnpackedPackage_maintainer}

# mancoosimm_HalfConfiguredPackage class attributes and methods

# mancoosimm_HalfInstalledPackage class attributes and methods
mancoosimm_HalfInstalledPackage_maintainer: Property = Property(name="maintainer", type=StringType)
mancoosimm_HalfInstalledPackage_checkSum: Property = Property(name="checkSum", type=StringType)
mancoosimm_HalfInstalledPackage_description: Property = Property(name="description", type=StringType)
mancoosimm_HalfInstalledPackage_section: Property = Property(name="section", type=StringType)
mancoosimm_HalfInstalledPackage_tag: Property = Property(name="tag", type=StringType)
mancoosimm_HalfInstalledPackage_priority: Property = Property(name="priority", type=StringType)
mancoosimm_HalfInstalledPackage_uploaders: Property = Property(name="uploaders", type=StringType)
mancoosimm_HalfInstalledPackage.attributes={mancoosimm_HalfInstalledPackage_checkSum, mancoosimm_HalfInstalledPackage_maintainer, mancoosimm_HalfInstalledPackage_priority, mancoosimm_HalfInstalledPackage_section, mancoosimm_HalfInstalledPackage_description, mancoosimm_HalfInstalledPackage_tag, mancoosimm_HalfInstalledPackage_uploaders}

# mancoosimm_Package class attributes and methods
mancoosimm_Package_architecture: Property = Property(name="architecture", type=StringType)
mancoosimm_Package_version: Property = Property(name="version", type=StringType)
mancoosimm_Package.attributes={mancoosimm_Package_version, mancoosimm_Package_architecture}

# mancoosimm_PackageSetting class attributes and methods

# mancoosimm_SrcPackage class attributes and methods

# mancoosimm_Dependence class attributes and methods

# mancoosimm_VirtualPackage class attributes and methods

# mancoosimm_File class attributes and methods
mancoosimm_File_size: Property = Property(name="size", type=IntegerType)
mancoosimm_File_extension: Property = Property(name="extension", type=StringType)
mancoosimm_File_description: Property = Property(name="description", type=StringType)
mancoosimm_File_checkSum: Property = Property(name="checkSum", type=StringType)
mancoosimm_File_isDirectory: Property = Property(name="isDirectory", type=BooleanType)
mancoosimm_File_suid: Property = Property(name="suid", type=BooleanType)
mancoosimm_File_guid: Property = Property(name="guid", type=BooleanType)
mancoosimm_File_permission: Property = Property(name="permission", type=StringType)
mancoosimm_File_location: Property = Property(name="location", type=StringType)
mancoosimm_File_isMissing: Property = Property(name="isMissing", type=BooleanType)
mancoosimm_File.attributes={mancoosimm_File_suid, mancoosimm_File_description, mancoosimm_File_size, mancoosimm_File_permission, mancoosimm_File_location, mancoosimm_File_isMissing, mancoosimm_File_extension, mancoosimm_File_guid, mancoosimm_File_isDirectory, mancoosimm_File_checkSum}

# mancoosimm_DocumentationFile class attributes and methods

# mancoosimm_Conflict class attributes and methods

# UnpackedPackage class attributes and methods

# InstalledPackage class attributes and methods

# mancoosimm_BinPackage class attributes and methods

# mancoosimm_AndDep class attributes and methods

# mancoosimm_OrDep class attributes and methods

# mancoosimm_SingleDep class attributes and methods
mancoosimm_SingleDep_version: Property = Property(name="version", type=StringType)
mancoosimm_SingleDep_value: Property = Property(name="value", type=StringType)
mancoosimm_SingleDep.attributes={mancoosimm_SingleDep_version, mancoosimm_SingleDep_value}

# Dependence class attributes and methods

# mancoosimm_Atom class attributes and methods

# mancoosimm_AndInv class attributes and methods

# mancoosimm_OrInv class attributes and methods

# mancoosimm_NotInv class attributes and methods

# mancoosimm_Invariant class attributes and methods

# mancoosimm_Service class attributes and methods

# mancoosimm_DesktopDB class attributes and methods

# mancoosimm_MimeTypeHandlerCache class attributes and methods

# mancoosimm_LibraryCache class attributes and methods

# mancoosimm_Alternative class attributes and methods

# mancoosimm_User class attributes and methods

# mancoosimm_Group class attributes and methods

# mancoosimm_EmacsPackage class attributes and methods

# mancoosimm_IconCache class attributes and methods
mancoosimm_IconCache_mtime: Property = Property(name="mtime", type=StringType)
mancoosimm_IconCache.attributes={mancoosimm_IconCache_mtime}

# mancoosimm_GConf class attributes and methods

# mancoosimm_Menu class attributes and methods

# mancoosimm_SkeeperCatalog class attributes and methods

# mancoosimm_SGMLCatalog class attributes and methods

# mancoosimm_ModuleCache class attributes and methods
mancoosimm_ModuleCache_version: Property = Property(name="version", type=StringType)
mancoosimm_ModuleCache.attributes={mancoosimm_ModuleCache_version}

# mancoosimm_XFontCache class attributes and methods
mancoosimm_XFontCache_location: Property = Property(name="location", type=StringType)
mancoosimm_XFontCache.attributes={mancoosimm_XFontCache_location}

# mancoosimm_ApplicationMenuCatalog class attributes and methods

# mancoosimm_MenuEntry class attributes and methods

# mancoosimm_Boot class attributes and methods

# File class attributes and methods

# mancoosimm_InformationFile class attributes and methods

# mancoosimm_MimeTypeHandler class attributes and methods

# mancoosimm_MimeType class attributes and methods
mancoosimm_MimeType_name: Property = Property(name="name", type=StringType)
mancoosimm_MimeType_extension: Property = Property(name="extension", type=StringType)
mancoosimm_MimeType.attributes={mancoosimm_MimeType_name, mancoosimm_MimeType_extension}

# mancoosimm_XFont class attributes and methods

# mancoosimm_SharedLibrary class attributes and methods
mancoosimm_SharedLibrary_name: Property = Property(name="name", type=StringType)
mancoosimm_SharedLibrary_version: Property = Property(name="version", type=StringType)
mancoosimm_SharedLibrary.attributes={mancoosimm_SharedLibrary_name, mancoosimm_SharedLibrary_version}

# mancoosimm_Module class attributes and methods

# mancoosimm_SGMLDocument class attributes and methods

# mancoosimm_SkeeperDocument class attributes and methods

# mancoosimm_SingleConflict class attributes and methods
mancoosimm_SingleConflict_version: Property = Property(name="version", type=StringType)
mancoosimm_SingleConflict_value: Property = Property(name="value", type=StringType)
mancoosimm_SingleConflict.attributes={mancoosimm_SingleConflict_value, mancoosimm_SingleConflict_version}

# Conflict class attributes and methods

# mancoosimm_AndConflict class attributes and methods

# mancoosimm_OrConflict class attributes and methods

# Relationships
installedPackages3: BinaryAssociation = BinaryAssociation(
    name="installedPackages3",
    ends={
        Property(name="mancoosimm_Configuration", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="mancoosimm_InstalledPackage", type=mancoosimm_Configuration, multiplicity=Multiplicity(1, 1))
    }
)
notInstalledPackages4: BinaryAssociation = BinaryAssociation(
    name="notInstalledPackages4",
    ends={
        Property(name="mancoosimm_NotInstalledPackage", type=mancoosimm_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Configuration5", type=mancoosimm_NotInstalledPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
configFilesPackages6: BinaryAssociation = BinaryAssociation(
    name="configFilesPackages6",
    ends={
        Property(name="mancoosimm_ConfigFilesPackage", type=mancoosimm_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Configuration7", type=mancoosimm_ConfigFilesPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fileSystem0: BinaryAssociation = BinaryAssociation(
    name="fileSystem0",
    ends={
        Property(name="FileSystem", type=mancoosimm_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="configuration", type=mancoosimm_FileSystem, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
environment1: BinaryAssociation = BinaryAssociation(
    name="environment1",
    ends={
        Property(name="Environment", type=mancoosimm_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="configuration2", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
packageSettings16: BinaryAssociation = BinaryAssociation(
    name="packageSettings16",
    ends={
        Property(name="PackageSetting", type=mancoosimm_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="pkg", type=mancoosimm_PackageSetting, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unpackedPackages8: BinaryAssociation = BinaryAssociation(
    name="unpackedPackages8",
    ends={
        Property(name="mancoosimm_UnpackedPackage", type=mancoosimm_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Configuration9", type=mancoosimm_UnpackedPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
halfConfiguredPackages10: BinaryAssociation = BinaryAssociation(
    name="halfConfiguredPackages10",
    ends={
        Property(name="mancoosimm_HalfConfiguredPackage", type=mancoosimm_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Configuration11", type=mancoosimm_HalfConfiguredPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
halfInstalledPackages12: BinaryAssociation = BinaryAssociation(
    name="halfInstalledPackages12",
    ends={
        Property(name="mancoosimm_HalfInstalledPackage", type=mancoosimm_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Configuration13", type=mancoosimm_HalfInstalledPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
configuration14: BinaryAssociation = BinaryAssociation(
    name="configuration14",
    ends={
        Property(name="mancoosimm_Configuration15", type=mancoosimm_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Package", type=mancoosimm_Configuration, multiplicity=Multiplicity(0, 1))
    }
)
recommends22: BinaryAssociation = BinaryAssociation(
    name="recommends22",
    ends={
        Property(name="mancoosimm_InstalledPackage23", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_InstalledPackage21", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(0, 9999))
    }
)
suggests25: BinaryAssociation = BinaryAssociation(
    name="suggests25",
    ends={
        Property(name="mancoosimm_InstalledPackage26", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_InstalledPackage24", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(0, 9999))
    }
)
enhances28: BinaryAssociation = BinaryAssociation(
    name="enhances28",
    ends={
        Property(name="mancoosimm_InstalledPackage29", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_InstalledPackage27", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(0, 9999))
    }
)
sourcePackage17: BinaryAssociation = BinaryAssociation(
    name="sourcePackage17",
    ends={
        Property(name="mancoosimm_SrcPackage", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_InstalledPackage18", type=mancoosimm_SrcPackage, multiplicity=Multiplicity(1, 1))
    }
)
depends19: BinaryAssociation = BinaryAssociation(
    name="depends19",
    ends={
        Property(name="mancoosimm_Dependence", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_InstalledPackage20", type=mancoosimm_Dependence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conflict42: BinaryAssociation = BinaryAssociation(
    name="conflict42",
    ends={
        Property(name="mancoosimm_Conflict", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_InstalledPackage43", type=mancoosimm_Conflict, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
predepends31: BinaryAssociation = BinaryAssociation(
    name="predepends31",
    ends={
        Property(name="mancoosimm_InstalledPackage32", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_InstalledPackage30", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(0, 9999))
    }
)
provides33: BinaryAssociation = BinaryAssociation(
    name="provides33",
    ends={
        Property(name="mancoosimm_VirtualPackage", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_InstalledPackage34", type=mancoosimm_VirtualPackage, multiplicity=Multiplicity(1, 1))
    }
)
replaces36: BinaryAssociation = BinaryAssociation(
    name="replaces36",
    ends={
        Property(name="mancoosimm_InstalledPackage37", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_InstalledPackage35", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(0, 9999))
    }
)
files38: BinaryAssociation = BinaryAssociation(
    name="files38",
    ends={
        Property(name="mancoosimm_File", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_InstalledPackage39", type=mancoosimm_File, multiplicity=Multiplicity(0, 9999))
    }
)
documentationFiles40: BinaryAssociation = BinaryAssociation(
    name="documentationFiles40",
    ends={
        Property(name="DocumentationFile", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="pkg41", type=mancoosimm_DocumentationFile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
files44: BinaryAssociation = BinaryAssociation(
    name="files44",
    ends={
        Property(name="mancoosimm_File46", type=mancoosimm_UnpackedPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_UnpackedPackage45", type=mancoosimm_File, multiplicity=Multiplicity(0, 9999))
    }
)
buildConflicts49: BinaryAssociation = BinaryAssociation(
    name="buildConflicts49",
    ends={
        Property(name="mancoosimm_SrcPackage50", type=mancoosimm_BinPackage, multiplicity=Multiplicity(0, 9999)),
        Property(name="mancoosimm_BinPackage51", type=mancoosimm_SrcPackage, multiplicity=Multiplicity(1, 1))
    }
)
srcRef52: BinaryAssociation = BinaryAssociation(
    name="srcRef52",
    ends={
        Property(name="mancoosimm_SrcPackage54", type=mancoosimm_BinPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_BinPackage53", type=mancoosimm_SrcPackage, multiplicity=Multiplicity(1, 1))
    }
)
buildDepends47: BinaryAssociation = BinaryAssociation(
    name="buildDepends47",
    ends={
        Property(name="mancoosimm_BinPackage", type=mancoosimm_SrcPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_SrcPackage48", type=mancoosimm_BinPackage, multiplicity=Multiplicity(0, 9999))
    }
)
ops66: BinaryAssociation = BinaryAssociation(
    name="ops66",
    ends={
        Property(name="mancoosimm_Dependence67", type=mancoosimm_AndDep, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_AndDep", type=mancoosimm_Dependence, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
dependence68: BinaryAssociation = BinaryAssociation(
    name="dependence68",
    ends={
        Property(name="Dependence", type=mancoosimm_AndDep, multiplicity=Multiplicity(1, 1)),
        Property(name="andDep", type=mancoosimm_Dependence, multiplicity=Multiplicity(1, 1))
    }
)
impPackage55: BinaryAssociation = BinaryAssociation(
    name="impPackage55",
    ends={
        Property(name="mancoosimm_InstalledPackage57", type=mancoosimm_VirtualPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_VirtualPackage56", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(1, 9999))
    }
)
ops69: BinaryAssociation = BinaryAssociation(
    name="ops69",
    ends={
        Property(name="mancoosimm_Dependence70", type=mancoosimm_OrDep, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_OrDep", type=mancoosimm_Dependence, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
andDep58: BinaryAssociation = BinaryAssociation(
    name="andDep58",
    ends={
        Property(name="AndDep", type=mancoosimm_Dependence, multiplicity=Multiplicity(1, 1)),
        Property(name="dependence", type=mancoosimm_AndDep, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
orDep59: BinaryAssociation = BinaryAssociation(
    name="orDep59",
    ends={
        Property(name="OrDep", type=mancoosimm_Dependence, multiplicity=Multiplicity(1, 1)),
        Property(name="dependence60", type=mancoosimm_OrDep, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
singleDep61: BinaryAssociation = BinaryAssociation(
    name="singleDep61",
    ends={
        Property(name="SingleDep", type=mancoosimm_Dependence, multiplicity=Multiplicity(1, 1)),
        Property(name="dependence62", type=mancoosimm_SingleDep, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
pkg63: BinaryAssociation = BinaryAssociation(
    name="pkg63",
    ends={
        Property(name="mancoosimm_Package65", type=mancoosimm_Dependence, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Dependence64", type=mancoosimm_Package, multiplicity=Multiplicity(1, 1))
    }
)
atomEl75: BinaryAssociation = BinaryAssociation(
    name="atomEl75",
    ends={
        Property(name="mancoosimm_Atom", type=mancoosimm_Invariant, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Invariant", type=mancoosimm_Atom, multiplicity=Multiplicity(0, 1))
    }
)
and76: BinaryAssociation = BinaryAssociation(
    name="and76",
    ends={
        Property(name="mancoosimm_AndInv", type=mancoosimm_Invariant, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Invariant77", type=mancoosimm_AndInv, multiplicity=Multiplicity(0, 1))
    }
)
or78: BinaryAssociation = BinaryAssociation(
    name="or78",
    ends={
        Property(name="mancoosimm_OrInv", type=mancoosimm_Invariant, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Invariant79", type=mancoosimm_OrInv, multiplicity=Multiplicity(0, 1))
    }
)
dependence71: BinaryAssociation = BinaryAssociation(
    name="dependence71",
    ends={
        Property(name="Dependence72", type=mancoosimm_OrDep, multiplicity=Multiplicity(1, 1)),
        Property(name="orDep", type=mancoosimm_Dependence, multiplicity=Multiplicity(1, 1))
    }
)
dependence73: BinaryAssociation = BinaryAssociation(
    name="dependence73",
    ends={
        Property(name="Dependence74", type=mancoosimm_SingleDep, multiplicity=Multiplicity(1, 1)),
        Property(name="singleDep", type=mancoosimm_Dependence, multiplicity=Multiplicity(1, 1))
    }
)
elem94: BinaryAssociation = BinaryAssociation(
    name="elem94",
    ends={
        Property(name="mancoosimm_Invariant96", type=mancoosimm_NotInv, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_NotInv95", type=mancoosimm_Invariant, multiplicity=Multiplicity(1, 1))
    }
)
runningServices97: BinaryAssociation = BinaryAssociation(
    name="runningServices97",
    ends={
        Property(name="Service", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env", type=mancoosimm_Service, multiplicity=Multiplicity(0, 9999))
    }
)
not80: BinaryAssociation = BinaryAssociation(
    name="not80",
    ends={
        Property(name="mancoosimm_NotInv", type=mancoosimm_Invariant, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Invariant81", type=mancoosimm_NotInv, multiplicity=Multiplicity(0, 1))
    }
)
left82: BinaryAssociation = BinaryAssociation(
    name="left82",
    ends={
        Property(name="mancoosimm_Invariant84", type=mancoosimm_AndInv, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_AndInv83", type=mancoosimm_Invariant, multiplicity=Multiplicity(1, 1))
    }
)
right85: BinaryAssociation = BinaryAssociation(
    name="right85",
    ends={
        Property(name="mancoosimm_Invariant87", type=mancoosimm_AndInv, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_AndInv86", type=mancoosimm_Invariant, multiplicity=Multiplicity(1, 1))
    }
)
left88: BinaryAssociation = BinaryAssociation(
    name="left88",
    ends={
        Property(name="mancoosimm_Invariant90", type=mancoosimm_OrInv, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_OrInv89", type=mancoosimm_Invariant, multiplicity=Multiplicity(1, 1))
    }
)
right91: BinaryAssociation = BinaryAssociation(
    name="right91",
    ends={
        Property(name="mancoosimm_Invariant93", type=mancoosimm_OrInv, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_OrInv92", type=mancoosimm_Invariant, multiplicity=Multiplicity(1, 1))
    }
)
desktopDb108: BinaryAssociation = BinaryAssociation(
    name="desktopDb108",
    ends={
        Property(name="DesktopDB", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env109", type=mancoosimm_DesktopDB, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mimeTypeHandlerCache110: BinaryAssociation = BinaryAssociation(
    name="mimeTypeHandlerCache110",
    ends={
        Property(name="MimeTypeHandlerCache", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env111", type=mancoosimm_MimeTypeHandlerCache, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
libraryCache112: BinaryAssociation = BinaryAssociation(
    name="libraryCache112",
    ends={
        Property(name="LibraryCache", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env113", type=mancoosimm_LibraryCache, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
alternatives98: BinaryAssociation = BinaryAssociation(
    name="alternatives98",
    ends={
        Property(name="Alternative", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env99", type=mancoosimm_Alternative, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
users100: BinaryAssociation = BinaryAssociation(
    name="users100",
    ends={
        Property(name="User", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env101", type=mancoosimm_User, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
groups102: BinaryAssociation = BinaryAssociation(
    name="groups102",
    ends={
        Property(name="Group", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env103", type=mancoosimm_Group, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
emacspkg104: BinaryAssociation = BinaryAssociation(
    name="emacspkg104",
    ends={
        Property(name="EmacsPackage", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env105", type=mancoosimm_EmacsPackage, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iconCache106: BinaryAssociation = BinaryAssociation(
    name="iconCache106",
    ends={
        Property(name="IconCache", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env107", type=mancoosimm_IconCache, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
gconf123: BinaryAssociation = BinaryAssociation(
    name="gconf123",
    ends={
        Property(name="GConf", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env124", type=mancoosimm_GConf, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
menu125: BinaryAssociation = BinaryAssociation(
    name="menu125",
    ends={
        Property(name="Menu", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env126", type=mancoosimm_Menu, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
skeeperCatalog114: BinaryAssociation = BinaryAssociation(
    name="skeeperCatalog114",
    ends={
        Property(name="SkeeperCatalog", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env115", type=mancoosimm_SkeeperCatalog, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sgmlCatalog116: BinaryAssociation = BinaryAssociation(
    name="sgmlCatalog116",
    ends={
        Property(name="SGMLCatalog", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env117", type=mancoosimm_SGMLCatalog, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
configuration118: BinaryAssociation = BinaryAssociation(
    name="configuration118",
    ends={
        Property(name="Configuration", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="environment", type=mancoosimm_Configuration, multiplicity=Multiplicity(1, 1))
    }
)
moduleCache119: BinaryAssociation = BinaryAssociation(
    name="moduleCache119",
    ends={
        Property(name="ModuleCache", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env120", type=mancoosimm_ModuleCache, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
xfontCaches121: BinaryAssociation = BinaryAssociation(
    name="xfontCaches121",
    ends={
        Property(name="XFontCache", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env122", type=mancoosimm_XFontCache, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
menu139: BinaryAssociation = BinaryAssociation(
    name="menu139",
    ends={
        Property(name="Menu140", type=mancoosimm_ApplicationMenuCatalog, multiplicity=Multiplicity(1, 1)),
        Property(name="catalog", type=mancoosimm_Menu, multiplicity=Multiplicity(1, 1))
    }
)
entries141: BinaryAssociation = BinaryAssociation(
    name="entries141",
    ends={
        Property(name="MenuEntry", type=mancoosimm_Menu, multiplicity=Multiplicity(1, 1)),
        Property(name="menu", type=mancoosimm_MenuEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
root127: BinaryAssociation = BinaryAssociation(
    name="root127",
    ends={
        Property(name="File", type=mancoosimm_FileSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="fs", type=mancoosimm_File, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
configuration128: BinaryAssociation = BinaryAssociation(
    name="configuration128",
    ends={
        Property(name="Configuration129", type=mancoosimm_FileSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="fileSystem", type=mancoosimm_Configuration, multiplicity=Multiplicity(1, 1))
    }
)
allFiles130: BinaryAssociation = BinaryAssociation(
    name="allFiles130",
    ends={
        Property(name="mancoosimm_File131", type=mancoosimm_FileSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_FileSystem", type=mancoosimm_File, multiplicity=Multiplicity(0, 9999))
    }
)
confFiles132: BinaryAssociation = BinaryAssociation(
    name="confFiles132",
    ends={
        Property(name="mancoosimm_File133", type=mancoosimm_GConf, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_GConf", type=mancoosimm_File, multiplicity=Multiplicity(0, 9999))
    }
)
schemas134: BinaryAssociation = BinaryAssociation(
    name="schemas134",
    ends={
        Property(name="mancoosimm_File136", type=mancoosimm_GConf, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_GConf135", type=mancoosimm_File, multiplicity=Multiplicity(0, 9999))
    }
)
env137: BinaryAssociation = BinaryAssociation(
    name="env137",
    ends={
        Property(name="Environment138", type=mancoosimm_GConf, multiplicity=Multiplicity(1, 1)),
        Property(name="gconf", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
catalog142: BinaryAssociation = BinaryAssociation(
    name="catalog142",
    ends={
        Property(name="ApplicationMenuCatalog", type=mancoosimm_Menu, multiplicity=Multiplicity(1, 1)),
        Property(name="menu143", type=mancoosimm_ApplicationMenuCatalog, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
env144: BinaryAssociation = BinaryAssociation(
    name="env144",
    ends={
        Property(name="Environment146", type=mancoosimm_Menu, multiplicity=Multiplicity(1, 1)),
        Property(name="menu145", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
menu147: BinaryAssociation = BinaryAssociation(
    name="menu147",
    ends={
        Property(name="Menu148", type=mancoosimm_MenuEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="entries", type=mancoosimm_Menu, multiplicity=Multiplicity(1, 1))
    }
)
services154: BinaryAssociation = BinaryAssociation(
    name="services154",
    ends={
        Property(name="mancoosimm_Service", type=mancoosimm_Boot, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Boot", type=mancoosimm_Service, multiplicity=Multiplicity(1, 9999))
    }
)
executable149: BinaryAssociation = BinaryAssociation(
    name="executable149",
    ends={
        Property(name="mancoosimm_File150", type=mancoosimm_MenuEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_MenuEntry", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
parent152: BinaryAssociation = BinaryAssociation(
    name="parent152",
    ends={
        Property(name="mancoosimm_MenuEntry153", type=mancoosimm_MenuEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_MenuEntry151", type=mancoosimm_MenuEntry, multiplicity=Multiplicity(1, 1))
    }
)
executable155: BinaryAssociation = BinaryAssociation(
    name="executable155",
    ends={
        Property(name="mancoosimm_File157", type=mancoosimm_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Service156", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
env158: BinaryAssociation = BinaryAssociation(
    name="env158",
    ends={
        Property(name="Environment159", type=mancoosimm_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="runningServices", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
fs160: BinaryAssociation = BinaryAssociation(
    name="fs160",
    ends={
        Property(name="FileSystem161", type=mancoosimm_File, multiplicity=Multiplicity(1, 1)),
        Property(name="root", type=mancoosimm_FileSystem, multiplicity=Multiplicity(0, 1))
    }
)
pkgSettings172: BinaryAssociation = BinaryAssociation(
    name="pkgSettings172",
    ends={
        Property(name="files", type=mancoosimm_PackageSetting, multiplicity=Multiplicity(0, 9999)),
        Property(name="PackageSetting173", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
childs163: BinaryAssociation = BinaryAssociation(
    name="childs163",
    ends={
        Property(name="File164", type=mancoosimm_File, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=mancoosimm_File, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent166: BinaryAssociation = BinaryAssociation(
    name="parent166",
    ends={
        Property(name="File167", type=mancoosimm_File, multiplicity=Multiplicity(1, 1)),
        Property(name="childs", type=mancoosimm_File, multiplicity=Multiplicity(0, 1))
    }
)
owner168: BinaryAssociation = BinaryAssociation(
    name="owner168",
    ends={
        Property(name="mancoosimm_User", type=mancoosimm_File, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_File169", type=mancoosimm_User, multiplicity=Multiplicity(1, 1))
    }
)
group170: BinaryAssociation = BinaryAssociation(
    name="group170",
    ends={
        Property(name="mancoosimm_Group", type=mancoosimm_File, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_File171", type=mancoosimm_Group, multiplicity=Multiplicity(1, 1))
    }
)
location177: BinaryAssociation = BinaryAssociation(
    name="location177",
    ends={
        Property(name="mancoosimm_File179", type=mancoosimm_Alternative, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Alternative178", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
pkg174: BinaryAssociation = BinaryAssociation(
    name="pkg174",
    ends={
        Property(name="InstalledPackage", type=mancoosimm_DocumentationFile, multiplicity=Multiplicity(1, 1)),
        Property(name="documentationFiles", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(1, 1))
    }
)
current175: BinaryAssociation = BinaryAssociation(
    name="current175",
    ends={
        Property(name="mancoosimm_File176", type=mancoosimm_Alternative, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Alternative", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
env180: BinaryAssociation = BinaryAssociation(
    name="env180",
    ends={
        Property(name="Environment181", type=mancoosimm_Alternative, multiplicity=Multiplicity(1, 1)),
        Property(name="alternatives", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
services182: BinaryAssociation = BinaryAssociation(
    name="services182",
    ends={
        Property(name="mancoosimm_Service183", type=mancoosimm_PackageSetting, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_PackageSetting", type=mancoosimm_Service, multiplicity=Multiplicity(0, 9999))
    }
)
files184: BinaryAssociation = BinaryAssociation(
    name="files184",
    ends={
        Property(name="File185", type=mancoosimm_PackageSetting, multiplicity=Multiplicity(1, 1)),
        Property(name="pkgSettings", type=mancoosimm_File, multiplicity=Multiplicity(0, 9999))
    }
)
pkg186: BinaryAssociation = BinaryAssociation(
    name="pkg186",
    ends={
        Property(name="Package", type=mancoosimm_PackageSetting, multiplicity=Multiplicity(1, 1)),
        Property(name="packageSettings", type=mancoosimm_Package, multiplicity=Multiplicity(1, 1))
    }
)
dependences188: BinaryAssociation = BinaryAssociation(
    name="dependences188",
    ends={
        Property(name="mancoosimm_PackageSetting189", type=mancoosimm_PackageSetting, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_PackageSetting187", type=mancoosimm_PackageSetting, multiplicity=Multiplicity(0, 9999))
    }
)
env190: BinaryAssociation = BinaryAssociation(
    name="env190",
    ends={
        Property(name="Environment191", type=mancoosimm_IconCache, multiplicity=Multiplicity(1, 1)),
        Property(name="iconCache", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
icons192: BinaryAssociation = BinaryAssociation(
    name="icons192",
    ends={
        Property(name="mancoosimm_File193", type=mancoosimm_IconCache, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_IconCache", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
env194: BinaryAssociation = BinaryAssociation(
    name="env194",
    ends={
        Property(name="Environment195", type=mancoosimm_DesktopDB, multiplicity=Multiplicity(1, 1)),
        Property(name="desktopDb", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
handler203: BinaryAssociation = BinaryAssociation(
    name="handler203",
    ends={
        Property(name="mancoosimm_File204", type=mancoosimm_MimeTypeHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_MimeTypeHandler", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
applications196: BinaryAssociation = BinaryAssociation(
    name="applications196",
    ends={
        Property(name="mancoosimm_File197", type=mancoosimm_DesktopDB, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_DesktopDB", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
env198: BinaryAssociation = BinaryAssociation(
    name="env198",
    ends={
        Property(name="Environment199", type=mancoosimm_MimeTypeHandlerCache, multiplicity=Multiplicity(1, 1)),
        Property(name="mimeTypeHandlerCache", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
handlers200: BinaryAssociation = BinaryAssociation(
    name="handlers200",
    ends={
        Property(name="MimeTypeHandler", type=mancoosimm_MimeTypeHandlerCache, multiplicity=Multiplicity(1, 1)),
        Property(name="cache", type=mancoosimm_MimeTypeHandler, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mimeTypes201: BinaryAssociation = BinaryAssociation(
    name="mimeTypes201",
    ends={
        Property(name="MimeType", type=mancoosimm_MimeTypeHandlerCache, multiplicity=Multiplicity(1, 1)),
        Property(name="cache202", type=mancoosimm_MimeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cache211: BinaryAssociation = BinaryAssociation(
    name="cache211",
    ends={
        Property(name="MimeTypeHandlerCache212", type=mancoosimm_MimeType, multiplicity=Multiplicity(1, 1)),
        Property(name="mimeTypes", type=mancoosimm_MimeTypeHandlerCache, multiplicity=Multiplicity(1, 1))
    }
)
type205: BinaryAssociation = BinaryAssociation(
    name="type205",
    ends={
        Property(name="MimeType206", type=mancoosimm_MimeTypeHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="mimeTypeHandlers", type=mancoosimm_MimeType, multiplicity=Multiplicity(0, 1))
    }
)
cache207: BinaryAssociation = BinaryAssociation(
    name="cache207",
    ends={
        Property(name="MimeTypeHandlerCache208", type=mancoosimm_MimeTypeHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="handlers", type=mancoosimm_MimeTypeHandlerCache, multiplicity=Multiplicity(1, 1))
    }
)
mimeTypeHandlers209: BinaryAssociation = BinaryAssociation(
    name="mimeTypeHandlers209",
    ends={
        Property(name="MimeTypeHandler210", type=mancoosimm_MimeType, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=mancoosimm_MimeTypeHandler, multiplicity=Multiplicity(0, 9999))
    }
)
xfonts213: BinaryAssociation = BinaryAssociation(
    name="xfonts213",
    ends={
        Property(name="XFont", type=mancoosimm_XFontCache, multiplicity=Multiplicity(1, 1)),
        Property(name="xfontCache", type=mancoosimm_XFont, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
env214: BinaryAssociation = BinaryAssociation(
    name="env214",
    ends={
        Property(name="Environment215", type=mancoosimm_XFontCache, multiplicity=Multiplicity(1, 1)),
        Property(name="xfontCaches", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
xfontCache216: BinaryAssociation = BinaryAssociation(
    name="xfontCache216",
    ends={
        Property(name="XFontCache217", type=mancoosimm_XFont, multiplicity=Multiplicity(1, 1)),
        Property(name="xfonts", type=mancoosimm_XFontCache, multiplicity=Multiplicity(1, 1))
    }
)
file218: BinaryAssociation = BinaryAssociation(
    name="file218",
    ends={
        Property(name="mancoosimm_File219", type=mancoosimm_XFont, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_XFont", type=mancoosimm_File, multiplicity=Multiplicity(1, 9999))
    }
)
locations220: BinaryAssociation = BinaryAssociation(
    name="locations220",
    ends={
        Property(name="mancoosimm_File221", type=mancoosimm_LibraryCache, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_LibraryCache", type=mancoosimm_File, multiplicity=Multiplicity(0, 9999))
    }
)
sharedLibraries222: BinaryAssociation = BinaryAssociation(
    name="sharedLibraries222",
    ends={
        Property(name="SharedLibrary", type=mancoosimm_LibraryCache, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryCache", type=mancoosimm_SharedLibrary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
env223: BinaryAssociation = BinaryAssociation(
    name="env223",
    ends={
        Property(name="Environment225", type=mancoosimm_LibraryCache, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryCache224", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
file226: BinaryAssociation = BinaryAssociation(
    name="file226",
    ends={
        Property(name="mancoosimm_File227", type=mancoosimm_SharedLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_SharedLibrary", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
libraryCache228: BinaryAssociation = BinaryAssociation(
    name="libraryCache228",
    ends={
        Property(name="LibraryCache229", type=mancoosimm_SharedLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="sharedLibraries", type=mancoosimm_LibraryCache, multiplicity=Multiplicity(1, 1))
    }
)
modules230: BinaryAssociation = BinaryAssociation(
    name="modules230",
    ends={
        Property(name="Module", type=mancoosimm_ModuleCache, multiplicity=Multiplicity(1, 1)),
        Property(name="moduleCache", type=mancoosimm_Module, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
env231: BinaryAssociation = BinaryAssociation(
    name="env231",
    ends={
        Property(name="Environment233", type=mancoosimm_ModuleCache, multiplicity=Multiplicity(1, 1)),
        Property(name="moduleCache232", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
moduleCache236: BinaryAssociation = BinaryAssociation(
    name="moduleCache236",
    ends={
        Property(name="ModuleCache237", type=mancoosimm_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="modules", type=mancoosimm_ModuleCache, multiplicity=Multiplicity(1, 1))
    }
)
env238: BinaryAssociation = BinaryAssociation(
    name="env238",
    ends={
        Property(name="Environment239", type=mancoosimm_SGMLCatalog, multiplicity=Multiplicity(1, 1)),
        Property(name="sgmlCatalog", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
documents240: BinaryAssociation = BinaryAssociation(
    name="documents240",
    ends={
        Property(name="mancoosimm_SGMLDocument", type=mancoosimm_SGMLCatalog, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_SGMLCatalog", type=mancoosimm_SGMLDocument, multiplicity=Multiplicity(0, 9999))
    }
)
location241: BinaryAssociation = BinaryAssociation(
    name="location241",
    ends={
        Property(name="mancoosimm_File243", type=mancoosimm_SGMLDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_SGMLDocument242", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
document244: BinaryAssociation = BinaryAssociation(
    name="document244",
    ends={
        Property(name="mancoosimm_File246", type=mancoosimm_SGMLDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_SGMLDocument245", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
env247: BinaryAssociation = BinaryAssociation(
    name="env247",
    ends={
        Property(name="Environment248", type=mancoosimm_SkeeperCatalog, multiplicity=Multiplicity(1, 1)),
        Property(name="skeeperCatalog", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
file234: BinaryAssociation = BinaryAssociation(
    name="file234",
    ends={
        Property(name="mancoosimm_File235", type=mancoosimm_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Module", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
documents249: BinaryAssociation = BinaryAssociation(
    name="documents249",
    ends={
        Property(name="mancoosimm_SkeeperDocument", type=mancoosimm_SkeeperCatalog, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_SkeeperCatalog", type=mancoosimm_SkeeperDocument, multiplicity=Multiplicity(0, 9999))
    }
)
location250: BinaryAssociation = BinaryAssociation(
    name="location250",
    ends={
        Property(name="mancoosimm_File252", type=mancoosimm_SkeeperDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_SkeeperDocument251", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
document253: BinaryAssociation = BinaryAssociation(
    name="document253",
    ends={
        Property(name="mancoosimm_File255", type=mancoosimm_SkeeperDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_SkeeperDocument254", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
files256: BinaryAssociation = BinaryAssociation(
    name="files256",
    ends={
        Property(name="mancoosimm_File257", type=mancoosimm_EmacsPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_EmacsPackage", type=mancoosimm_File, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
env258: BinaryAssociation = BinaryAssociation(
    name="env258",
    ends={
        Property(name="Environment259", type=mancoosimm_EmacsPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="emacspkg", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
env260: BinaryAssociation = BinaryAssociation(
    name="env260",
    ends={
        Property(name="Environment261", type=mancoosimm_User, multiplicity=Multiplicity(1, 1)),
        Property(name="users", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
groups262: BinaryAssociation = BinaryAssociation(
    name="groups262",
    ends={
        Property(name="Group264", type=mancoosimm_User, multiplicity=Multiplicity(1, 1)),
        Property(name="users263", type=mancoosimm_Group, multiplicity=Multiplicity(1, 9999))
    }
)
home265: BinaryAssociation = BinaryAssociation(
    name="home265",
    ends={
        Property(name="mancoosimm_File267", type=mancoosimm_User, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_User266", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
env268: BinaryAssociation = BinaryAssociation(
    name="env268",
    ends={
        Property(name="Environment269", type=mancoosimm_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="groups", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
users270: BinaryAssociation = BinaryAssociation(
    name="users270",
    ends={
        Property(name="User272", type=mancoosimm_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="groups271", type=mancoosimm_User, multiplicity=Multiplicity(0, 9999))
    }
)
conflict273: BinaryAssociation = BinaryAssociation(
    name="conflict273",
    ends={
        Property(name="Conflict", type=mancoosimm_SingleConflict, multiplicity=Multiplicity(1, 1)),
        Property(name="singleConflict", type=mancoosimm_Conflict, multiplicity=Multiplicity(1, 1))
    }
)
andConflict274: BinaryAssociation = BinaryAssociation(
    name="andConflict274",
    ends={
        Property(name="AndConflict", type=mancoosimm_Conflict, multiplicity=Multiplicity(1, 1)),
        Property(name="conflict", type=mancoosimm_AndConflict, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
orConflict275: BinaryAssociation = BinaryAssociation(
    name="orConflict275",
    ends={
        Property(name="OrConflict", type=mancoosimm_Conflict, multiplicity=Multiplicity(1, 1)),
        Property(name="conflict276", type=mancoosimm_OrConflict, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
singleConflict277: BinaryAssociation = BinaryAssociation(
    name="singleConflict277",
    ends={
        Property(name="SingleConflict", type=mancoosimm_Conflict, multiplicity=Multiplicity(1, 1)),
        Property(name="conflict278", type=mancoosimm_SingleConflict, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pkg279: BinaryAssociation = BinaryAssociation(
    name="pkg279",
    ends={
        Property(name="mancoosimm_Package281", type=mancoosimm_Conflict, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Conflict280", type=mancoosimm_Package, multiplicity=Multiplicity(1, 1))
    }
)
ops282: BinaryAssociation = BinaryAssociation(
    name="ops282",
    ends={
        Property(name="mancoosimm_Conflict283", type=mancoosimm_AndConflict, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_AndConflict", type=mancoosimm_Conflict, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
conflict284: BinaryAssociation = BinaryAssociation(
    name="conflict284",
    ends={
        Property(name="Conflict285", type=mancoosimm_AndConflict, multiplicity=Multiplicity(1, 1)),
        Property(name="andConflict", type=mancoosimm_Conflict, multiplicity=Multiplicity(1, 1))
    }
)
ops286: BinaryAssociation = BinaryAssociation(
    name="ops286",
    ends={
        Property(name="mancoosimm_Conflict287", type=mancoosimm_OrConflict, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_OrConflict", type=mancoosimm_Conflict, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
conflict288: BinaryAssociation = BinaryAssociation(
    name="conflict288",
    ends={
        Property(name="Conflict289", type=mancoosimm_OrConflict, multiplicity=Multiplicity(1, 1)),
        Property(name="orConflict", type=mancoosimm_Conflict, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_mancoosimm_Configuration_NamedElement = Generalization(general=NamedElement, specific=mancoosimm_Configuration)
gen_mancoosimm_InstalledPackage_Package = Generalization(general=Package, specific=mancoosimm_InstalledPackage)
gen_mancoosimm_Package_NamedElement = Generalization(general=NamedElement, specific=mancoosimm_Package)
gen_mancoosimm_NotInstalledPackage_Package = Generalization(general=Package, specific=mancoosimm_NotInstalledPackage)
gen_mancoosimm_ConfigFilesPackage_Package = Generalization(general=Package, specific=mancoosimm_ConfigFilesPackage)
gen_mancoosimm_HalfConfiguredPackage_UnpackedPackage = Generalization(general=UnpackedPackage, specific=mancoosimm_HalfConfiguredPackage)
gen_mancoosimm_HalfInstalledPackage_Package = Generalization(general=Package, specific=mancoosimm_HalfInstalledPackage)
gen_mancoosimm_UnpackedPackage_Package = Generalization(general=Package, specific=mancoosimm_UnpackedPackage)
gen_mancoosimm_BinPackage_InstalledPackage = Generalization(general=InstalledPackage, specific=mancoosimm_BinPackage)
gen_mancoosimm_VirtualPackage_InstalledPackage = Generalization(general=InstalledPackage, specific=mancoosimm_VirtualPackage)
gen_mancoosimm_SrcPackage_InstalledPackage = Generalization(general=InstalledPackage, specific=mancoosimm_SrcPackage)
gen_mancoosimm_OrDep_Dependence = Generalization(general=Dependence, specific=mancoosimm_OrDep)
gen_mancoosimm_AndDep_Dependence = Generalization(general=Dependence, specific=mancoosimm_AndDep)
gen_mancoosimm_SingleDep_Dependence = Generalization(general=Dependence, specific=mancoosimm_SingleDep)
gen_mancoosimm_Invariant_NamedElement = Generalization(general=NamedElement, specific=mancoosimm_Invariant)
gen_mancoosimm_Environment_NamedElement = Generalization(general=NamedElement, specific=mancoosimm_Environment)
gen_mancoosimm_Atom_NamedElement = Generalization(general=NamedElement, specific=mancoosimm_Atom)
gen_mancoosimm_FileSystem_NamedElement = Generalization(general=NamedElement, specific=mancoosimm_FileSystem)
gen_mancoosimm_ApplicationMenuCatalog_NamedElement = Generalization(general=NamedElement, specific=mancoosimm_ApplicationMenuCatalog)
gen_mancoosimm_MenuEntry_NamedElement = Generalization(general=NamedElement, specific=mancoosimm_MenuEntry)
gen_mancoosimm_Service_NamedElement = Generalization(general=NamedElement, specific=mancoosimm_Service)
gen_mancoosimm_File_NamedElement = Generalization(general=NamedElement, specific=mancoosimm_File)
gen_mancoosimm_DocumentationFile_File = Generalization(general=File, specific=mancoosimm_DocumentationFile)
gen_mancoosimm_InformationFile_File = Generalization(general=File, specific=mancoosimm_InformationFile)
gen_mancoosimm_Alternative_NamedElement = Generalization(general=NamedElement, specific=mancoosimm_Alternative)
gen_mancoosimm_PackageSetting_NamedElement = Generalization(general=NamedElement, specific=mancoosimm_PackageSetting)
gen_mancoosimm_XFont_NamedElement = Generalization(general=NamedElement, specific=mancoosimm_XFont)
gen_mancoosimm_Module_NamedElement = Generalization(general=NamedElement, specific=mancoosimm_Module)
gen_mancoosimm_SGMLCatalog_NamedElement = Generalization(general=NamedElement, specific=mancoosimm_SGMLCatalog)
gen_mancoosimm_SGMLDocument_NamedElement = Generalization(general=NamedElement, specific=mancoosimm_SGMLDocument)
gen_mancoosimm_SkeeperCatalog_NamedElement = Generalization(general=NamedElement, specific=mancoosimm_SkeeperCatalog)
gen_mancoosimm_SkeeperDocument_NamedElement = Generalization(general=NamedElement, specific=mancoosimm_SkeeperDocument)
gen_mancoosimm_EmacsPackage_NamedElement = Generalization(general=NamedElement, specific=mancoosimm_EmacsPackage)
gen_mancoosimm_User_NamedElement = Generalization(general=NamedElement, specific=mancoosimm_User)
gen_mancoosimm_Group_NamedElement = Generalization(general=NamedElement, specific=mancoosimm_Group)
gen_mancoosimm_SingleConflict_Conflict = Generalization(general=Conflict, specific=mancoosimm_SingleConflict)
gen_mancoosimm_AndConflict_Conflict = Generalization(general=Conflict, specific=mancoosimm_AndConflict)
gen_mancoosimm_OrConflict_Conflict = Generalization(general=Conflict, specific=mancoosimm_OrConflict)

# Domain Model
domain_model = DomainModel(
    name="mancoosimm",
    types={mancoosimm_NamedElement, mancoosimm_NotInstalledPackage, mancoosimm_ConfigFilesPackage, mancoosimm_Configuration, NamedElement, mancoosimm_FileSystem, mancoosimm_Environment, mancoosimm_InstalledPackage, Package, mancoosimm_UnpackedPackage, mancoosimm_HalfConfiguredPackage, mancoosimm_HalfInstalledPackage, mancoosimm_Package, mancoosimm_PackageSetting, mancoosimm_SrcPackage, mancoosimm_Dependence, mancoosimm_VirtualPackage, mancoosimm_File, mancoosimm_DocumentationFile, mancoosimm_Conflict, UnpackedPackage, InstalledPackage, mancoosimm_BinPackage, mancoosimm_AndDep, mancoosimm_OrDep, mancoosimm_SingleDep, Dependence, mancoosimm_Atom, mancoosimm_AndInv, mancoosimm_OrInv, mancoosimm_NotInv, mancoosimm_Invariant, mancoosimm_Service, mancoosimm_DesktopDB, mancoosimm_MimeTypeHandlerCache, mancoosimm_LibraryCache, mancoosimm_Alternative, mancoosimm_User, mancoosimm_Group, mancoosimm_EmacsPackage, mancoosimm_IconCache, mancoosimm_GConf, mancoosimm_Menu, mancoosimm_SkeeperCatalog, mancoosimm_SGMLCatalog, mancoosimm_ModuleCache, mancoosimm_XFontCache, mancoosimm_ApplicationMenuCatalog, mancoosimm_MenuEntry, mancoosimm_Boot, File, mancoosimm_InformationFile, mancoosimm_MimeTypeHandler, mancoosimm_MimeType, mancoosimm_XFont, mancoosimm_SharedLibrary, mancoosimm_Module, mancoosimm_SGMLDocument, mancoosimm_SkeeperDocument, mancoosimm_SingleConflict, Conflict, mancoosimm_AndConflict, mancoosimm_OrConflict, PriorityType, StatusType, VersionType},
    associations={installedPackages3, notInstalledPackages4, configFilesPackages6, fileSystem0, environment1, packageSettings16, unpackedPackages8, halfConfiguredPackages10, halfInstalledPackages12, configuration14, recommends22, suggests25, enhances28, sourcePackage17, depends19, conflict42, predepends31, provides33, replaces36, files38, documentationFiles40, files44, buildConflicts49, srcRef52, buildDepends47, ops66, dependence68, impPackage55, ops69, andDep58, orDep59, singleDep61, pkg63, atomEl75, and76, or78, dependence71, dependence73, elem94, runningServices97, not80, left82, right85, left88, right91, desktopDb108, mimeTypeHandlerCache110, libraryCache112, alternatives98, users100, groups102, emacspkg104, iconCache106, gconf123, menu125, skeeperCatalog114, sgmlCatalog116, configuration118, moduleCache119, xfontCaches121, menu139, entries141, root127, configuration128, allFiles130, confFiles132, schemas134, env137, catalog142, env144, menu147, services154, executable149, parent152, executable155, env158, fs160, pkgSettings172, childs163, parent166, owner168, group170, location177, pkg174, current175, env180, services182, files184, pkg186, dependences188, env190, icons192, env194, handler203, applications196, env198, handlers200, mimeTypes201, cache211, type205, cache207, mimeTypeHandlers209, xfonts213, env214, xfontCache216, file218, locations220, sharedLibraries222, env223, file226, libraryCache228, modules230, env231, moduleCache236, env238, documents240, location241, document244, env247, file234, documents249, location250, document253, files256, env258, env260, groups262, home265, env268, users270, conflict273, andConflict274, orConflict275, singleConflict277, pkg279, ops282, conflict284, ops286, conflict288},
    generalizations={gen_mancoosimm_Configuration_NamedElement, gen_mancoosimm_InstalledPackage_Package, gen_mancoosimm_Package_NamedElement, gen_mancoosimm_NotInstalledPackage_Package, gen_mancoosimm_ConfigFilesPackage_Package, gen_mancoosimm_HalfConfiguredPackage_UnpackedPackage, gen_mancoosimm_HalfInstalledPackage_Package, gen_mancoosimm_UnpackedPackage_Package, gen_mancoosimm_BinPackage_InstalledPackage, gen_mancoosimm_VirtualPackage_InstalledPackage, gen_mancoosimm_SrcPackage_InstalledPackage, gen_mancoosimm_OrDep_Dependence, gen_mancoosimm_AndDep_Dependence, gen_mancoosimm_SingleDep_Dependence, gen_mancoosimm_Invariant_NamedElement, gen_mancoosimm_Environment_NamedElement, gen_mancoosimm_Atom_NamedElement, gen_mancoosimm_FileSystem_NamedElement, gen_mancoosimm_ApplicationMenuCatalog_NamedElement, gen_mancoosimm_MenuEntry_NamedElement, gen_mancoosimm_Service_NamedElement, gen_mancoosimm_File_NamedElement, gen_mancoosimm_DocumentationFile_File, gen_mancoosimm_InformationFile_File, gen_mancoosimm_Alternative_NamedElement, gen_mancoosimm_PackageSetting_NamedElement, gen_mancoosimm_XFont_NamedElement, gen_mancoosimm_Module_NamedElement, gen_mancoosimm_SGMLCatalog_NamedElement, gen_mancoosimm_SGMLDocument_NamedElement, gen_mancoosimm_SkeeperCatalog_NamedElement, gen_mancoosimm_SkeeperDocument_NamedElement, gen_mancoosimm_EmacsPackage_NamedElement, gen_mancoosimm_User_NamedElement, gen_mancoosimm_Group_NamedElement, gen_mancoosimm_SingleConflict_Conflict, gen_mancoosimm_AndConflict_Conflict, gen_mancoosimm_OrConflict_Conflict},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)