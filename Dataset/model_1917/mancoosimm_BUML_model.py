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
mancoosimm_InstalledPackage = Class(name="mancoosimm::InstalledPackage")
mancoosimm_NotInstalledPackage = Class(name="mancoosimm::NotInstalledPackage")
mancoosimm_Configuration = Class(name="mancoosimm::Configuration")
NamedElement = Class(name="NamedElement")
mancoosimm_FileSystem = Class(name="mancoosimm::FileSystem")
mancoosimm_Environment = Class(name="mancoosimm::Environment")
mancoosimm_HalfConfiguredReinstRequiredPackage = Class(name="mancoosimm::HalfConfiguredReinstRequiredPackage")
mancoosimm_HalfInstalledReinstRequiredPackage = Class(name="mancoosimm::HalfInstalledReinstRequiredPackage")
mancoosimm_ConfigFilesPackage = Class(name="mancoosimm::ConfigFilesPackage")
mancoosimm_UnpackedPackage = Class(name="mancoosimm::UnpackedPackage")
mancoosimm_HalfConfiguredPackage = Class(name="mancoosimm::HalfConfiguredPackage")
mancoosimm_HalfInstalledPackage = Class(name="mancoosimm::HalfInstalledPackage")
mancoosimm_SrcPackage = Class(name="mancoosimm::SrcPackage")
mancoosimm_Package = Class(name="mancoosimm::Package", is_abstract=True)
mancoosimm_PackageSetting = Class(name="mancoosimm::PackageSetting")
Package = Class(name="Package")
mancoosimm_Dependence = Class(name="mancoosimm::Dependence", is_abstract=True)
mancoosimm_DocumentationFile = Class(name="mancoosimm::DocumentationFile")
mancoosimm_VirtualPackage = Class(name="mancoosimm::VirtualPackage")
mancoosimm_Conflict = Class(name="mancoosimm::Conflict", is_abstract=True)
mancoosimm_File = Class(name="mancoosimm::File")
UnpackedPackage = Class(name="UnpackedPackage")
InstalledPackage = Class(name="InstalledPackage")
mancoosimm_BinPackage = Class(name="mancoosimm::BinPackage")
mancoosimm_AndDep = Class(name="mancoosimm::AndDep")
mancoosimm_OrDep = Class(name="mancoosimm::OrDep")
mancoosimm_SingleDep = Class(name="mancoosimm::SingleDep")
Dependence = Class(name="Dependence")
mancoosimm_Invariant = Class(name="mancoosimm::Invariant")
mancoosimm_Atom = Class(name="mancoosimm::Atom")
mancoosimm_AndInv = Class(name="mancoosimm::AndInv")
mancoosimm_OrInv = Class(name="mancoosimm::OrInv")
mancoosimm_NotInv = Class(name="mancoosimm::NotInv")
mancoosimm_Service = Class(name="mancoosimm::Service")
mancoosimm_Alternative = Class(name="mancoosimm::Alternative")
mancoosimm_User = Class(name="mancoosimm::User")
mancoosimm_Group = Class(name="mancoosimm::Group")
mancoosimm_EmacsPackage = Class(name="mancoosimm::EmacsPackage")
mancoosimm_IconCache = Class(name="mancoosimm::IconCache")
mancoosimm_DesktopDB = Class(name="mancoosimm::DesktopDB")
mancoosimm_MimeTypeHandlerCache = Class(name="mancoosimm::MimeTypeHandlerCache")
mancoosimm_LibraryCache = Class(name="mancoosimm::LibraryCache")
mancoosimm_SkeeperCatalog = Class(name="mancoosimm::SkeeperCatalog")
mancoosimm_SGMLCatalog = Class(name="mancoosimm::SGMLCatalog")
mancoosimm_ModuleCache = Class(name="mancoosimm::ModuleCache")
mancoosimm_GConf = Class(name="mancoosimm::GConf")
mancoosimm_Menu = Class(name="mancoosimm::Menu")
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

# mancoosimm_InstalledPackage class attributes and methods
mancoosimm_InstalledPackage_tag: Property = Property(name="tag", type=StringType)
mancoosimm_InstalledPackage_priority: Property = Property(name="priority", type=StringType)
mancoosimm_InstalledPackage_uploaders: Property = Property(name="uploaders", type=StringType)
mancoosimm_InstalledPackage_installedSize: Property = Property(name="installedSize", type=IntegerType)
mancoosimm_InstalledPackage_maintainer: Property = Property(name="maintainer", type=StringType)
mancoosimm_InstalledPackage_fileSize: Property = Property(name="fileSize", type=IntegerType)
mancoosimm_InstalledPackage_checkSum: Property = Property(name="checkSum", type=StringType)
mancoosimm_InstalledPackage_description: Property = Property(name="description", type=StringType)
mancoosimm_InstalledPackage_section: Property = Property(name="section", type=StringType)
mancoosimm_InstalledPackage.attributes={mancoosimm_InstalledPackage_maintainer, mancoosimm_InstalledPackage_priority, mancoosimm_InstalledPackage_fileSize, mancoosimm_InstalledPackage_checkSum, mancoosimm_InstalledPackage_section, mancoosimm_InstalledPackage_tag, mancoosimm_InstalledPackage_description, mancoosimm_InstalledPackage_installedSize, mancoosimm_InstalledPackage_uploaders}

# mancoosimm_NotInstalledPackage class attributes and methods

# mancoosimm_Configuration class attributes and methods
mancoosimm_Configuration_creationTime: Property = Property(name="creationTime", type=StringType)
mancoosimm_Configuration_systemType: Property = Property(name="systemType", type=StringType)
mancoosimm_Configuration.attributes={mancoosimm_Configuration_creationTime, mancoosimm_Configuration_systemType}

# NamedElement class attributes and methods

# mancoosimm_FileSystem class attributes and methods

# mancoosimm_Environment class attributes and methods

# mancoosimm_HalfConfiguredReinstRequiredPackage class attributes and methods

# mancoosimm_HalfInstalledReinstRequiredPackage class attributes and methods
mancoosimm_HalfInstalledReinstRequiredPackage_maintainer: Property = Property(name="maintainer", type=StringType)
mancoosimm_HalfInstalledReinstRequiredPackage_section: Property = Property(name="section", type=StringType)
mancoosimm_HalfInstalledReinstRequiredPackage_tag: Property = Property(name="tag", type=StringType)
mancoosimm_HalfInstalledReinstRequiredPackage_priority: Property = Property(name="priority", type=StringType)
mancoosimm_HalfInstalledReinstRequiredPackage_uploaders: Property = Property(name="uploaders", type=StringType)
mancoosimm_HalfInstalledReinstRequiredPackage_checkSum: Property = Property(name="checkSum", type=StringType)
mancoosimm_HalfInstalledReinstRequiredPackage_description: Property = Property(name="description", type=StringType)
mancoosimm_HalfInstalledReinstRequiredPackage.attributes={mancoosimm_HalfInstalledReinstRequiredPackage_section, mancoosimm_HalfInstalledReinstRequiredPackage_tag, mancoosimm_HalfInstalledReinstRequiredPackage_maintainer, mancoosimm_HalfInstalledReinstRequiredPackage_description, mancoosimm_HalfInstalledReinstRequiredPackage_uploaders, mancoosimm_HalfInstalledReinstRequiredPackage_checkSum, mancoosimm_HalfInstalledReinstRequiredPackage_priority}

# mancoosimm_ConfigFilesPackage class attributes and methods
mancoosimm_ConfigFilesPackage_maintainer: Property = Property(name="maintainer", type=StringType)
mancoosimm_ConfigFilesPackage_checkSum: Property = Property(name="checkSum", type=StringType)
mancoosimm_ConfigFilesPackage_description: Property = Property(name="description", type=StringType)
mancoosimm_ConfigFilesPackage_section: Property = Property(name="section", type=StringType)
mancoosimm_ConfigFilesPackage_tag: Property = Property(name="tag", type=StringType)
mancoosimm_ConfigFilesPackage_priority: Property = Property(name="priority", type=StringType)
mancoosimm_ConfigFilesPackage_uploaders: Property = Property(name="uploaders", type=StringType)
mancoosimm_ConfigFilesPackage.attributes={mancoosimm_ConfigFilesPackage_uploaders, mancoosimm_ConfigFilesPackage_description, mancoosimm_ConfigFilesPackage_checkSum, mancoosimm_ConfigFilesPackage_section, mancoosimm_ConfigFilesPackage_maintainer, mancoosimm_ConfigFilesPackage_priority, mancoosimm_ConfigFilesPackage_tag}

# mancoosimm_UnpackedPackage class attributes and methods
mancoosimm_UnpackedPackage_maintainer: Property = Property(name="maintainer", type=StringType)
mancoosimm_UnpackedPackage_checkSum: Property = Property(name="checkSum", type=StringType)
mancoosimm_UnpackedPackage_tag: Property = Property(name="tag", type=StringType)
mancoosimm_UnpackedPackage_priority: Property = Property(name="priority", type=StringType)
mancoosimm_UnpackedPackage_uploaders: Property = Property(name="uploaders", type=StringType)
mancoosimm_UnpackedPackage_description: Property = Property(name="description", type=StringType)
mancoosimm_UnpackedPackage_section: Property = Property(name="section", type=StringType)
mancoosimm_UnpackedPackage.attributes={mancoosimm_UnpackedPackage_uploaders, mancoosimm_UnpackedPackage_maintainer, mancoosimm_UnpackedPackage_checkSum, mancoosimm_UnpackedPackage_description, mancoosimm_UnpackedPackage_section, mancoosimm_UnpackedPackage_tag, mancoosimm_UnpackedPackage_priority}

# mancoosimm_HalfConfiguredPackage class attributes and methods

# mancoosimm_HalfInstalledPackage class attributes and methods
mancoosimm_HalfInstalledPackage_maintainer: Property = Property(name="maintainer", type=StringType)
mancoosimm_HalfInstalledPackage_checkSum: Property = Property(name="checkSum", type=StringType)
mancoosimm_HalfInstalledPackage_description: Property = Property(name="description", type=StringType)
mancoosimm_HalfInstalledPackage_section: Property = Property(name="section", type=StringType)
mancoosimm_HalfInstalledPackage_tag: Property = Property(name="tag", type=StringType)
mancoosimm_HalfInstalledPackage_priority: Property = Property(name="priority", type=StringType)
mancoosimm_HalfInstalledPackage_uploaders: Property = Property(name="uploaders", type=StringType)
mancoosimm_HalfInstalledPackage.attributes={mancoosimm_HalfInstalledPackage_description, mancoosimm_HalfInstalledPackage_checkSum, mancoosimm_HalfInstalledPackage_tag, mancoosimm_HalfInstalledPackage_priority, mancoosimm_HalfInstalledPackage_uploaders, mancoosimm_HalfInstalledPackage_maintainer, mancoosimm_HalfInstalledPackage_section}

# mancoosimm_SrcPackage class attributes and methods

# mancoosimm_Package class attributes and methods
mancoosimm_Package_version: Property = Property(name="version", type=StringType)
mancoosimm_Package_architecture: Property = Property(name="architecture", type=StringType)
mancoosimm_Package.attributes={mancoosimm_Package_version, mancoosimm_Package_architecture}

# mancoosimm_PackageSetting class attributes and methods

# Package class attributes and methods

# mancoosimm_Dependence class attributes and methods

# mancoosimm_DocumentationFile class attributes and methods

# mancoosimm_VirtualPackage class attributes and methods

# mancoosimm_Conflict class attributes and methods

# mancoosimm_File class attributes and methods
mancoosimm_File_extension: Property = Property(name="extension", type=StringType)
mancoosimm_File_description: Property = Property(name="description", type=StringType)
mancoosimm_File_checkSum: Property = Property(name="checkSum", type=StringType)
mancoosimm_File_isDirectory: Property = Property(name="isDirectory", type=BooleanType)
mancoosimm_File_suid: Property = Property(name="suid", type=BooleanType)
mancoosimm_File_guid: Property = Property(name="guid", type=BooleanType)
mancoosimm_File_permission: Property = Property(name="permission", type=StringType)
mancoosimm_File_location: Property = Property(name="location", type=StringType)
mancoosimm_File_size: Property = Property(name="size", type=IntegerType)
mancoosimm_File_isMissing: Property = Property(name="isMissing", type=BooleanType)
mancoosimm_File.attributes={mancoosimm_File_checkSum, mancoosimm_File_permission, mancoosimm_File_isMissing, mancoosimm_File_extension, mancoosimm_File_size, mancoosimm_File_description, mancoosimm_File_guid, mancoosimm_File_suid, mancoosimm_File_location, mancoosimm_File_isDirectory}

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

# mancoosimm_Invariant class attributes and methods

# mancoosimm_Atom class attributes and methods

# mancoosimm_AndInv class attributes and methods

# mancoosimm_OrInv class attributes and methods

# mancoosimm_NotInv class attributes and methods

# mancoosimm_Service class attributes and methods

# mancoosimm_Alternative class attributes and methods

# mancoosimm_User class attributes and methods

# mancoosimm_Group class attributes and methods

# mancoosimm_EmacsPackage class attributes and methods

# mancoosimm_IconCache class attributes and methods
mancoosimm_IconCache_mtime: Property = Property(name="mtime", type=StringType)
mancoosimm_IconCache.attributes={mancoosimm_IconCache_mtime}

# mancoosimm_DesktopDB class attributes and methods

# mancoosimm_MimeTypeHandlerCache class attributes and methods

# mancoosimm_LibraryCache class attributes and methods

# mancoosimm_SkeeperCatalog class attributes and methods

# mancoosimm_SGMLCatalog class attributes and methods

# mancoosimm_ModuleCache class attributes and methods
mancoosimm_ModuleCache_version: Property = Property(name="version", type=StringType)
mancoosimm_ModuleCache.attributes={mancoosimm_ModuleCache_version}

# mancoosimm_GConf class attributes and methods

# mancoosimm_Menu class attributes and methods

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
mancoosimm_MimeType.attributes={mancoosimm_MimeType_extension, mancoosimm_MimeType_name}

# mancoosimm_XFont class attributes and methods

# mancoosimm_SharedLibrary class attributes and methods
mancoosimm_SharedLibrary_name: Property = Property(name="name", type=StringType)
mancoosimm_SharedLibrary_version: Property = Property(name="version", type=StringType)
mancoosimm_SharedLibrary.attributes={mancoosimm_SharedLibrary_version, mancoosimm_SharedLibrary_name}

# mancoosimm_Module class attributes and methods

# mancoosimm_SGMLDocument class attributes and methods

# mancoosimm_SkeeperDocument class attributes and methods

# mancoosimm_SingleConflict class attributes and methods
mancoosimm_SingleConflict_version: Property = Property(name="version", type=StringType)
mancoosimm_SingleConflict_value: Property = Property(name="value", type=StringType)
mancoosimm_SingleConflict.attributes={mancoosimm_SingleConflict_version, mancoosimm_SingleConflict_value}

# Conflict class attributes and methods

# mancoosimm_AndConflict class attributes and methods

# mancoosimm_OrConflict class attributes and methods

# Relationships
installedPackages3: BinaryAssociation = BinaryAssociation(
    name="installedPackages3",
    ends={
        Property(name="mancoosimm_InstalledPackage", type=mancoosimm_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Configuration", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
halfConfiguredReinstRequiredPackages14: BinaryAssociation = BinaryAssociation(
    name="halfConfiguredReinstRequiredPackages14",
    ends={
        Property(name="mancoosimm_HalfConfiguredReinstRequiredPackage", type=mancoosimm_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Configuration15", type=mancoosimm_HalfConfiguredReinstRequiredPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
halfInstalledReinstRequiredPackages16: BinaryAssociation = BinaryAssociation(
    name="halfInstalledReinstRequiredPackages16",
    ends={
        Property(name="mancoosimm_HalfInstalledReinstRequiredPackage", type=mancoosimm_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Configuration17", type=mancoosimm_HalfInstalledReinstRequiredPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
sourcePackage21: BinaryAssociation = BinaryAssociation(
    name="sourcePackage21",
    ends={
        Property(name="mancoosimm_SrcPackage", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_InstalledPackage22", type=mancoosimm_SrcPackage, multiplicity=Multiplicity(1, 1))
    }
)
configuration18: BinaryAssociation = BinaryAssociation(
    name="configuration18",
    ends={
        Property(name="mancoosimm_Configuration19", type=mancoosimm_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Package", type=mancoosimm_Configuration, multiplicity=Multiplicity(0, 1))
    }
)
packageSettings20: BinaryAssociation = BinaryAssociation(
    name="packageSettings20",
    ends={
        Property(name="PackageSetting", type=mancoosimm_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="pkg", type=mancoosimm_PackageSetting, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
depends23: BinaryAssociation = BinaryAssociation(
    name="depends23",
    ends={
        Property(name="mancoosimm_Dependence", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_InstalledPackage24", type=mancoosimm_Dependence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
recommends26: BinaryAssociation = BinaryAssociation(
    name="recommends26",
    ends={
        Property(name="mancoosimm_InstalledPackage27", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_InstalledPackage25", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(0, 9999))
    }
)
suggests29: BinaryAssociation = BinaryAssociation(
    name="suggests29",
    ends={
        Property(name="mancoosimm_InstalledPackage30", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_InstalledPackage28", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(0, 9999))
    }
)
enhances32: BinaryAssociation = BinaryAssociation(
    name="enhances32",
    ends={
        Property(name="mancoosimm_InstalledPackage33", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_InstalledPackage31", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(0, 9999))
    }
)
predepends35: BinaryAssociation = BinaryAssociation(
    name="predepends35",
    ends={
        Property(name="mancoosimm_InstalledPackage36", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_InstalledPackage34", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(0, 9999))
    }
)
documentationFiles44: BinaryAssociation = BinaryAssociation(
    name="documentationFiles44",
    ends={
        Property(name="DocumentationFile", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="pkg45", type=mancoosimm_DocumentationFile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
provides37: BinaryAssociation = BinaryAssociation(
    name="provides37",
    ends={
        Property(name="mancoosimm_VirtualPackage", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_InstalledPackage38", type=mancoosimm_VirtualPackage, multiplicity=Multiplicity(1, 1))
    }
)
replaces40: BinaryAssociation = BinaryAssociation(
    name="replaces40",
    ends={
        Property(name="mancoosimm_InstalledPackage41", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_InstalledPackage39", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(0, 9999))
    }
)
conflict46: BinaryAssociation = BinaryAssociation(
    name="conflict46",
    ends={
        Property(name="mancoosimm_Conflict", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_InstalledPackage47", type=mancoosimm_Conflict, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
files42: BinaryAssociation = BinaryAssociation(
    name="files42",
    ends={
        Property(name="mancoosimm_File", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_InstalledPackage43", type=mancoosimm_File, multiplicity=Multiplicity(0, 9999))
    }
)
files48: BinaryAssociation = BinaryAssociation(
    name="files48",
    ends={
        Property(name="mancoosimm_File50", type=mancoosimm_UnpackedPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_UnpackedPackage49", type=mancoosimm_File, multiplicity=Multiplicity(0, 9999))
    }
)
buildDepends51: BinaryAssociation = BinaryAssociation(
    name="buildDepends51",
    ends={
        Property(name="mancoosimm_BinPackage", type=mancoosimm_SrcPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_SrcPackage52", type=mancoosimm_BinPackage, multiplicity=Multiplicity(0, 9999))
    }
)
buildConflicts53: BinaryAssociation = BinaryAssociation(
    name="buildConflicts53",
    ends={
        Property(name="mancoosimm_BinPackage55", type=mancoosimm_SrcPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_SrcPackage54", type=mancoosimm_BinPackage, multiplicity=Multiplicity(0, 9999))
    }
)
srcRef56: BinaryAssociation = BinaryAssociation(
    name="srcRef56",
    ends={
        Property(name="mancoosimm_SrcPackage58", type=mancoosimm_BinPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_BinPackage57", type=mancoosimm_SrcPackage, multiplicity=Multiplicity(1, 1))
    }
)
impPackage59: BinaryAssociation = BinaryAssociation(
    name="impPackage59",
    ends={
        Property(name="mancoosimm_InstalledPackage61", type=mancoosimm_VirtualPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_VirtualPackage60", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(1, 9999))
    }
)
andDep62: BinaryAssociation = BinaryAssociation(
    name="andDep62",
    ends={
        Property(name="AndDep", type=mancoosimm_Dependence, multiplicity=Multiplicity(1, 1)),
        Property(name="dependence", type=mancoosimm_AndDep, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
singleDep65: BinaryAssociation = BinaryAssociation(
    name="singleDep65",
    ends={
        Property(name="SingleDep", type=mancoosimm_Dependence, multiplicity=Multiplicity(1, 1)),
        Property(name="dependence66", type=mancoosimm_SingleDep, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
pkg67: BinaryAssociation = BinaryAssociation(
    name="pkg67",
    ends={
        Property(name="mancoosimm_Package69", type=mancoosimm_Dependence, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Dependence68", type=mancoosimm_Package, multiplicity=Multiplicity(1, 1))
    }
)
owner71: BinaryAssociation = BinaryAssociation(
    name="owner71",
    ends={
        Property(name="mancoosimm_Dependence72", type=mancoosimm_Dependence, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Dependence70", type=mancoosimm_Dependence, multiplicity=Multiplicity(0, 1))
    }
)
ownerPkg73: BinaryAssociation = BinaryAssociation(
    name="ownerPkg73",
    ends={
        Property(name="mancoosimm_Package75", type=mancoosimm_Dependence, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Dependence74", type=mancoosimm_Package, multiplicity=Multiplicity(1, 1))
    }
)
ops76: BinaryAssociation = BinaryAssociation(
    name="ops76",
    ends={
        Property(name="mancoosimm_Dependence77", type=mancoosimm_AndDep, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_AndDep", type=mancoosimm_Dependence, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
dependence78: BinaryAssociation = BinaryAssociation(
    name="dependence78",
    ends={
        Property(name="Dependence", type=mancoosimm_AndDep, multiplicity=Multiplicity(1, 1)),
        Property(name="andDep", type=mancoosimm_Dependence, multiplicity=Multiplicity(1, 1))
    }
)
ops79: BinaryAssociation = BinaryAssociation(
    name="ops79",
    ends={
        Property(name="mancoosimm_Dependence80", type=mancoosimm_OrDep, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_OrDep", type=mancoosimm_Dependence, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
dependence81: BinaryAssociation = BinaryAssociation(
    name="dependence81",
    ends={
        Property(name="Dependence82", type=mancoosimm_OrDep, multiplicity=Multiplicity(1, 1)),
        Property(name="orDep", type=mancoosimm_Dependence, multiplicity=Multiplicity(1, 1))
    }
)
orDep63: BinaryAssociation = BinaryAssociation(
    name="orDep63",
    ends={
        Property(name="OrDep", type=mancoosimm_Dependence, multiplicity=Multiplicity(1, 1)),
        Property(name="dependence64", type=mancoosimm_OrDep, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
atomEl85: BinaryAssociation = BinaryAssociation(
    name="atomEl85",
    ends={
        Property(name="mancoosimm_Atom", type=mancoosimm_Invariant, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Invariant", type=mancoosimm_Atom, multiplicity=Multiplicity(0, 1))
    }
)
and86: BinaryAssociation = BinaryAssociation(
    name="and86",
    ends={
        Property(name="mancoosimm_AndInv", type=mancoosimm_Invariant, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Invariant87", type=mancoosimm_AndInv, multiplicity=Multiplicity(0, 1))
    }
)
or88: BinaryAssociation = BinaryAssociation(
    name="or88",
    ends={
        Property(name="mancoosimm_OrInv", type=mancoosimm_Invariant, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Invariant89", type=mancoosimm_OrInv, multiplicity=Multiplicity(0, 1))
    }
)
not90: BinaryAssociation = BinaryAssociation(
    name="not90",
    ends={
        Property(name="mancoosimm_NotInv", type=mancoosimm_Invariant, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Invariant91", type=mancoosimm_NotInv, multiplicity=Multiplicity(0, 1))
    }
)
left92: BinaryAssociation = BinaryAssociation(
    name="left92",
    ends={
        Property(name="mancoosimm_Invariant94", type=mancoosimm_AndInv, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_AndInv93", type=mancoosimm_Invariant, multiplicity=Multiplicity(1, 1))
    }
)
right95: BinaryAssociation = BinaryAssociation(
    name="right95",
    ends={
        Property(name="mancoosimm_Invariant97", type=mancoosimm_AndInv, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_AndInv96", type=mancoosimm_Invariant, multiplicity=Multiplicity(1, 1))
    }
)
left98: BinaryAssociation = BinaryAssociation(
    name="left98",
    ends={
        Property(name="mancoosimm_Invariant100", type=mancoosimm_OrInv, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_OrInv99", type=mancoosimm_Invariant, multiplicity=Multiplicity(1, 1))
    }
)
dependence83: BinaryAssociation = BinaryAssociation(
    name="dependence83",
    ends={
        Property(name="Dependence84", type=mancoosimm_SingleDep, multiplicity=Multiplicity(1, 1)),
        Property(name="singleDep", type=mancoosimm_Dependence, multiplicity=Multiplicity(1, 1))
    }
)
elem104: BinaryAssociation = BinaryAssociation(
    name="elem104",
    ends={
        Property(name="mancoosimm_Invariant106", type=mancoosimm_NotInv, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_NotInv105", type=mancoosimm_Invariant, multiplicity=Multiplicity(1, 1))
    }
)
runningServices107: BinaryAssociation = BinaryAssociation(
    name="runningServices107",
    ends={
        Property(name="Service", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env", type=mancoosimm_Service, multiplicity=Multiplicity(0, 9999))
    }
)
alternatives108: BinaryAssociation = BinaryAssociation(
    name="alternatives108",
    ends={
        Property(name="Alternative", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env109", type=mancoosimm_Alternative, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
users110: BinaryAssociation = BinaryAssociation(
    name="users110",
    ends={
        Property(name="User", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env111", type=mancoosimm_User, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
groups112: BinaryAssociation = BinaryAssociation(
    name="groups112",
    ends={
        Property(name="Group", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env113", type=mancoosimm_Group, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
emacspkg114: BinaryAssociation = BinaryAssociation(
    name="emacspkg114",
    ends={
        Property(name="EmacsPackage", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env115", type=mancoosimm_EmacsPackage, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iconCache116: BinaryAssociation = BinaryAssociation(
    name="iconCache116",
    ends={
        Property(name="IconCache", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env117", type=mancoosimm_IconCache, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
desktopDb118: BinaryAssociation = BinaryAssociation(
    name="desktopDb118",
    ends={
        Property(name="DesktopDB", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env119", type=mancoosimm_DesktopDB, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right101: BinaryAssociation = BinaryAssociation(
    name="right101",
    ends={
        Property(name="mancoosimm_Invariant103", type=mancoosimm_OrInv, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_OrInv102", type=mancoosimm_Invariant, multiplicity=Multiplicity(1, 1))
    }
)
mimeTypeHandlerCache120: BinaryAssociation = BinaryAssociation(
    name="mimeTypeHandlerCache120",
    ends={
        Property(name="MimeTypeHandlerCache", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env121", type=mancoosimm_MimeTypeHandlerCache, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
libraryCache122: BinaryAssociation = BinaryAssociation(
    name="libraryCache122",
    ends={
        Property(name="LibraryCache", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env123", type=mancoosimm_LibraryCache, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
skeeperCatalog124: BinaryAssociation = BinaryAssociation(
    name="skeeperCatalog124",
    ends={
        Property(name="SkeeperCatalog", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env125", type=mancoosimm_SkeeperCatalog, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sgmlCatalog126: BinaryAssociation = BinaryAssociation(
    name="sgmlCatalog126",
    ends={
        Property(name="SGMLCatalog", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env127", type=mancoosimm_SGMLCatalog, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
configuration128: BinaryAssociation = BinaryAssociation(
    name="configuration128",
    ends={
        Property(name="Configuration", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="environment", type=mancoosimm_Configuration, multiplicity=Multiplicity(1, 1))
    }
)
moduleCache129: BinaryAssociation = BinaryAssociation(
    name="moduleCache129",
    ends={
        Property(name="ModuleCache", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env130", type=mancoosimm_ModuleCache, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
xfontCaches131: BinaryAssociation = BinaryAssociation(
    name="xfontCaches131",
    ends={
        Property(name="XFontCache", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env132", type=mancoosimm_XFontCache, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
gconf133: BinaryAssociation = BinaryAssociation(
    name="gconf133",
    ends={
        Property(name="GConf", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env134", type=mancoosimm_GConf, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
menu135: BinaryAssociation = BinaryAssociation(
    name="menu135",
    ends={
        Property(name="Menu", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env136", type=mancoosimm_Menu, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
root137: BinaryAssociation = BinaryAssociation(
    name="root137",
    ends={
        Property(name="File", type=mancoosimm_FileSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="fs", type=mancoosimm_File, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
configuration138: BinaryAssociation = BinaryAssociation(
    name="configuration138",
    ends={
        Property(name="Configuration139", type=mancoosimm_FileSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="fileSystem", type=mancoosimm_Configuration, multiplicity=Multiplicity(1, 1))
    }
)
allFiles140: BinaryAssociation = BinaryAssociation(
    name="allFiles140",
    ends={
        Property(name="mancoosimm_File141", type=mancoosimm_FileSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_FileSystem", type=mancoosimm_File, multiplicity=Multiplicity(0, 9999))
    }
)
confFiles142: BinaryAssociation = BinaryAssociation(
    name="confFiles142",
    ends={
        Property(name="mancoosimm_File143", type=mancoosimm_GConf, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_GConf", type=mancoosimm_File, multiplicity=Multiplicity(0, 9999))
    }
)
schemas144: BinaryAssociation = BinaryAssociation(
    name="schemas144",
    ends={
        Property(name="mancoosimm_File146", type=mancoosimm_GConf, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_GConf145", type=mancoosimm_File, multiplicity=Multiplicity(0, 9999))
    }
)
menu149: BinaryAssociation = BinaryAssociation(
    name="menu149",
    ends={
        Property(name="Menu150", type=mancoosimm_ApplicationMenuCatalog, multiplicity=Multiplicity(1, 1)),
        Property(name="catalog", type=mancoosimm_Menu, multiplicity=Multiplicity(1, 1))
    }
)
entries151: BinaryAssociation = BinaryAssociation(
    name="entries151",
    ends={
        Property(name="MenuEntry", type=mancoosimm_Menu, multiplicity=Multiplicity(1, 1)),
        Property(name="menu", type=mancoosimm_MenuEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
catalog152: BinaryAssociation = BinaryAssociation(
    name="catalog152",
    ends={
        Property(name="ApplicationMenuCatalog", type=mancoosimm_Menu, multiplicity=Multiplicity(1, 1)),
        Property(name="menu153", type=mancoosimm_ApplicationMenuCatalog, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
env154: BinaryAssociation = BinaryAssociation(
    name="env154",
    ends={
        Property(name="Environment156", type=mancoosimm_Menu, multiplicity=Multiplicity(1, 1)),
        Property(name="menu155", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
menu157: BinaryAssociation = BinaryAssociation(
    name="menu157",
    ends={
        Property(name="Menu158", type=mancoosimm_MenuEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="entries", type=mancoosimm_Menu, multiplicity=Multiplicity(1, 1))
    }
)
executable159: BinaryAssociation = BinaryAssociation(
    name="executable159",
    ends={
        Property(name="mancoosimm_File160", type=mancoosimm_MenuEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_MenuEntry", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
parent162: BinaryAssociation = BinaryAssociation(
    name="parent162",
    ends={
        Property(name="mancoosimm_MenuEntry163", type=mancoosimm_MenuEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_MenuEntry161", type=mancoosimm_MenuEntry, multiplicity=Multiplicity(1, 1))
    }
)
env147: BinaryAssociation = BinaryAssociation(
    name="env147",
    ends={
        Property(name="Environment148", type=mancoosimm_GConf, multiplicity=Multiplicity(1, 1)),
        Property(name="gconf", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
services164: BinaryAssociation = BinaryAssociation(
    name="services164",
    ends={
        Property(name="mancoosimm_Service", type=mancoosimm_Boot, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Boot", type=mancoosimm_Service, multiplicity=Multiplicity(1, 9999))
    }
)
executable165: BinaryAssociation = BinaryAssociation(
    name="executable165",
    ends={
        Property(name="mancoosimm_File167", type=mancoosimm_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Service166", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
env168: BinaryAssociation = BinaryAssociation(
    name="env168",
    ends={
        Property(name="Environment169", type=mancoosimm_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="runningServices", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
fs170: BinaryAssociation = BinaryAssociation(
    name="fs170",
    ends={
        Property(name="FileSystem171", type=mancoosimm_File, multiplicity=Multiplicity(1, 1)),
        Property(name="root", type=mancoosimm_FileSystem, multiplicity=Multiplicity(0, 1))
    }
)
childs173: BinaryAssociation = BinaryAssociation(
    name="childs173",
    ends={
        Property(name="File174", type=mancoosimm_File, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=mancoosimm_File, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent176: BinaryAssociation = BinaryAssociation(
    name="parent176",
    ends={
        Property(name="File177", type=mancoosimm_File, multiplicity=Multiplicity(1, 1)),
        Property(name="childs", type=mancoosimm_File, multiplicity=Multiplicity(0, 1))
    }
)
owner178: BinaryAssociation = BinaryAssociation(
    name="owner178",
    ends={
        Property(name="mancoosimm_User", type=mancoosimm_File, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_File179", type=mancoosimm_User, multiplicity=Multiplicity(1, 1))
    }
)
group180: BinaryAssociation = BinaryAssociation(
    name="group180",
    ends={
        Property(name="mancoosimm_Group", type=mancoosimm_File, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_File181", type=mancoosimm_Group, multiplicity=Multiplicity(1, 1))
    }
)
pkgSettings182: BinaryAssociation = BinaryAssociation(
    name="pkgSettings182",
    ends={
        Property(name="PackageSetting183", type=mancoosimm_File, multiplicity=Multiplicity(1, 1)),
        Property(name="files", type=mancoosimm_PackageSetting, multiplicity=Multiplicity(0, 9999))
    }
)
pkg184: BinaryAssociation = BinaryAssociation(
    name="pkg184",
    ends={
        Property(name="InstalledPackage", type=mancoosimm_DocumentationFile, multiplicity=Multiplicity(1, 1)),
        Property(name="documentationFiles", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(1, 1))
    }
)
current185: BinaryAssociation = BinaryAssociation(
    name="current185",
    ends={
        Property(name="mancoosimm_File186", type=mancoosimm_Alternative, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Alternative", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
location187: BinaryAssociation = BinaryAssociation(
    name="location187",
    ends={
        Property(name="mancoosimm_File189", type=mancoosimm_Alternative, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Alternative188", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
env190: BinaryAssociation = BinaryAssociation(
    name="env190",
    ends={
        Property(name="Environment191", type=mancoosimm_Alternative, multiplicity=Multiplicity(1, 1)),
        Property(name="alternatives", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
services192: BinaryAssociation = BinaryAssociation(
    name="services192",
    ends={
        Property(name="mancoosimm_Service193", type=mancoosimm_PackageSetting, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_PackageSetting", type=mancoosimm_Service, multiplicity=Multiplicity(0, 9999))
    }
)
files194: BinaryAssociation = BinaryAssociation(
    name="files194",
    ends={
        Property(name="File195", type=mancoosimm_PackageSetting, multiplicity=Multiplicity(1, 1)),
        Property(name="pkgSettings", type=mancoosimm_File, multiplicity=Multiplicity(0, 9999))
    }
)
pkg196: BinaryAssociation = BinaryAssociation(
    name="pkg196",
    ends={
        Property(name="Package", type=mancoosimm_PackageSetting, multiplicity=Multiplicity(1, 1)),
        Property(name="packageSettings", type=mancoosimm_Package, multiplicity=Multiplicity(1, 1))
    }
)
dependences198: BinaryAssociation = BinaryAssociation(
    name="dependences198",
    ends={
        Property(name="mancoosimm_PackageSetting199", type=mancoosimm_PackageSetting, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_PackageSetting197", type=mancoosimm_PackageSetting, multiplicity=Multiplicity(0, 9999))
    }
)
env200: BinaryAssociation = BinaryAssociation(
    name="env200",
    ends={
        Property(name="Environment201", type=mancoosimm_IconCache, multiplicity=Multiplicity(1, 1)),
        Property(name="iconCache", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
icons202: BinaryAssociation = BinaryAssociation(
    name="icons202",
    ends={
        Property(name="mancoosimm_File203", type=mancoosimm_IconCache, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_IconCache", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
env204: BinaryAssociation = BinaryAssociation(
    name="env204",
    ends={
        Property(name="Environment205", type=mancoosimm_DesktopDB, multiplicity=Multiplicity(1, 1)),
        Property(name="desktopDb", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
applications206: BinaryAssociation = BinaryAssociation(
    name="applications206",
    ends={
        Property(name="mancoosimm_File207", type=mancoosimm_DesktopDB, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_DesktopDB", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
env208: BinaryAssociation = BinaryAssociation(
    name="env208",
    ends={
        Property(name="Environment209", type=mancoosimm_MimeTypeHandlerCache, multiplicity=Multiplicity(1, 1)),
        Property(name="mimeTypeHandlerCache", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
handlers210: BinaryAssociation = BinaryAssociation(
    name="handlers210",
    ends={
        Property(name="MimeTypeHandler", type=mancoosimm_MimeTypeHandlerCache, multiplicity=Multiplicity(1, 1)),
        Property(name="cache", type=mancoosimm_MimeTypeHandler, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mimeTypes211: BinaryAssociation = BinaryAssociation(
    name="mimeTypes211",
    ends={
        Property(name="MimeType", type=mancoosimm_MimeTypeHandlerCache, multiplicity=Multiplicity(1, 1)),
        Property(name="cache212", type=mancoosimm_MimeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
handler213: BinaryAssociation = BinaryAssociation(
    name="handler213",
    ends={
        Property(name="mancoosimm_File214", type=mancoosimm_MimeTypeHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_MimeTypeHandler", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
type215: BinaryAssociation = BinaryAssociation(
    name="type215",
    ends={
        Property(name="MimeType216", type=mancoosimm_MimeTypeHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="mimeTypeHandlers", type=mancoosimm_MimeType, multiplicity=Multiplicity(0, 1))
    }
)
cache217: BinaryAssociation = BinaryAssociation(
    name="cache217",
    ends={
        Property(name="MimeTypeHandlerCache218", type=mancoosimm_MimeTypeHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="handlers", type=mancoosimm_MimeTypeHandlerCache, multiplicity=Multiplicity(1, 1))
    }
)
mimeTypeHandlers219: BinaryAssociation = BinaryAssociation(
    name="mimeTypeHandlers219",
    ends={
        Property(name="MimeTypeHandler220", type=mancoosimm_MimeType, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=mancoosimm_MimeTypeHandler, multiplicity=Multiplicity(0, 9999))
    }
)
cache221: BinaryAssociation = BinaryAssociation(
    name="cache221",
    ends={
        Property(name="MimeTypeHandlerCache222", type=mancoosimm_MimeType, multiplicity=Multiplicity(1, 1)),
        Property(name="mimeTypes", type=mancoosimm_MimeTypeHandlerCache, multiplicity=Multiplicity(1, 1))
    }
)
xfonts223: BinaryAssociation = BinaryAssociation(
    name="xfonts223",
    ends={
        Property(name="XFont", type=mancoosimm_XFontCache, multiplicity=Multiplicity(1, 1)),
        Property(name="xfontCache", type=mancoosimm_XFont, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
env224: BinaryAssociation = BinaryAssociation(
    name="env224",
    ends={
        Property(name="Environment225", type=mancoosimm_XFontCache, multiplicity=Multiplicity(1, 1)),
        Property(name="xfontCaches", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
xfontCache226: BinaryAssociation = BinaryAssociation(
    name="xfontCache226",
    ends={
        Property(name="XFontCache227", type=mancoosimm_XFont, multiplicity=Multiplicity(1, 1)),
        Property(name="xfonts", type=mancoosimm_XFontCache, multiplicity=Multiplicity(1, 1))
    }
)
file228: BinaryAssociation = BinaryAssociation(
    name="file228",
    ends={
        Property(name="mancoosimm_File229", type=mancoosimm_XFont, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_XFont", type=mancoosimm_File, multiplicity=Multiplicity(1, 9999))
    }
)
locations230: BinaryAssociation = BinaryAssociation(
    name="locations230",
    ends={
        Property(name="mancoosimm_File231", type=mancoosimm_LibraryCache, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_LibraryCache", type=mancoosimm_File, multiplicity=Multiplicity(0, 9999))
    }
)
sharedLibraries232: BinaryAssociation = BinaryAssociation(
    name="sharedLibraries232",
    ends={
        Property(name="SharedLibrary", type=mancoosimm_LibraryCache, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryCache", type=mancoosimm_SharedLibrary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
env233: BinaryAssociation = BinaryAssociation(
    name="env233",
    ends={
        Property(name="Environment235", type=mancoosimm_LibraryCache, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryCache234", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
file236: BinaryAssociation = BinaryAssociation(
    name="file236",
    ends={
        Property(name="mancoosimm_File237", type=mancoosimm_SharedLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_SharedLibrary", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
libraryCache238: BinaryAssociation = BinaryAssociation(
    name="libraryCache238",
    ends={
        Property(name="LibraryCache239", type=mancoosimm_SharedLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="sharedLibraries", type=mancoosimm_LibraryCache, multiplicity=Multiplicity(1, 1))
    }
)
modules240: BinaryAssociation = BinaryAssociation(
    name="modules240",
    ends={
        Property(name="Module", type=mancoosimm_ModuleCache, multiplicity=Multiplicity(1, 1)),
        Property(name="moduleCache", type=mancoosimm_Module, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
env241: BinaryAssociation = BinaryAssociation(
    name="env241",
    ends={
        Property(name="Environment243", type=mancoosimm_ModuleCache, multiplicity=Multiplicity(1, 1)),
        Property(name="moduleCache242", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
file244: BinaryAssociation = BinaryAssociation(
    name="file244",
    ends={
        Property(name="mancoosimm_File245", type=mancoosimm_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Module", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
moduleCache246: BinaryAssociation = BinaryAssociation(
    name="moduleCache246",
    ends={
        Property(name="ModuleCache247", type=mancoosimm_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="modules", type=mancoosimm_ModuleCache, multiplicity=Multiplicity(1, 1))
    }
)
documents250: BinaryAssociation = BinaryAssociation(
    name="documents250",
    ends={
        Property(name="mancoosimm_SGMLDocument", type=mancoosimm_SGMLCatalog, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_SGMLCatalog", type=mancoosimm_SGMLDocument, multiplicity=Multiplicity(0, 9999))
    }
)
location251: BinaryAssociation = BinaryAssociation(
    name="location251",
    ends={
        Property(name="mancoosimm_File253", type=mancoosimm_SGMLDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_SGMLDocument252", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
document254: BinaryAssociation = BinaryAssociation(
    name="document254",
    ends={
        Property(name="mancoosimm_File256", type=mancoosimm_SGMLDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_SGMLDocument255", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
env257: BinaryAssociation = BinaryAssociation(
    name="env257",
    ends={
        Property(name="Environment258", type=mancoosimm_SkeeperCatalog, multiplicity=Multiplicity(1, 1)),
        Property(name="skeeperCatalog", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
env248: BinaryAssociation = BinaryAssociation(
    name="env248",
    ends={
        Property(name="Environment249", type=mancoosimm_SGMLCatalog, multiplicity=Multiplicity(1, 1)),
        Property(name="sgmlCatalog", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
documents259: BinaryAssociation = BinaryAssociation(
    name="documents259",
    ends={
        Property(name="mancoosimm_SkeeperDocument", type=mancoosimm_SkeeperCatalog, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_SkeeperCatalog", type=mancoosimm_SkeeperDocument, multiplicity=Multiplicity(0, 9999))
    }
)
location260: BinaryAssociation = BinaryAssociation(
    name="location260",
    ends={
        Property(name="mancoosimm_File262", type=mancoosimm_SkeeperDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_SkeeperDocument261", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
document263: BinaryAssociation = BinaryAssociation(
    name="document263",
    ends={
        Property(name="mancoosimm_File265", type=mancoosimm_SkeeperDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_SkeeperDocument264", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
files266: BinaryAssociation = BinaryAssociation(
    name="files266",
    ends={
        Property(name="mancoosimm_File267", type=mancoosimm_EmacsPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_EmacsPackage", type=mancoosimm_File, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
env268: BinaryAssociation = BinaryAssociation(
    name="env268",
    ends={
        Property(name="Environment269", type=mancoosimm_EmacsPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="emacspkg", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
env270: BinaryAssociation = BinaryAssociation(
    name="env270",
    ends={
        Property(name="Environment271", type=mancoosimm_User, multiplicity=Multiplicity(1, 1)),
        Property(name="users", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
groups272: BinaryAssociation = BinaryAssociation(
    name="groups272",
    ends={
        Property(name="Group274", type=mancoosimm_User, multiplicity=Multiplicity(1, 1)),
        Property(name="users273", type=mancoosimm_Group, multiplicity=Multiplicity(1, 9999))
    }
)
home275: BinaryAssociation = BinaryAssociation(
    name="home275",
    ends={
        Property(name="mancoosimm_File277", type=mancoosimm_User, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_User276", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
env278: BinaryAssociation = BinaryAssociation(
    name="env278",
    ends={
        Property(name="groups", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="Environment279", type=mancoosimm_Group, multiplicity=Multiplicity(1, 1))
    }
)
users280: BinaryAssociation = BinaryAssociation(
    name="users280",
    ends={
        Property(name="User282", type=mancoosimm_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="groups281", type=mancoosimm_User, multiplicity=Multiplicity(0, 9999))
    }
)
conflict283: BinaryAssociation = BinaryAssociation(
    name="conflict283",
    ends={
        Property(name="Conflict", type=mancoosimm_SingleConflict, multiplicity=Multiplicity(1, 1)),
        Property(name="singleConflict", type=mancoosimm_Conflict, multiplicity=Multiplicity(1, 1))
    }
)
andConflict284: BinaryAssociation = BinaryAssociation(
    name="andConflict284",
    ends={
        Property(name="AndConflict", type=mancoosimm_Conflict, multiplicity=Multiplicity(1, 1)),
        Property(name="conflict", type=mancoosimm_AndConflict, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
orConflict285: BinaryAssociation = BinaryAssociation(
    name="orConflict285",
    ends={
        Property(name="OrConflict", type=mancoosimm_Conflict, multiplicity=Multiplicity(1, 1)),
        Property(name="conflict286", type=mancoosimm_OrConflict, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
singleConflict287: BinaryAssociation = BinaryAssociation(
    name="singleConflict287",
    ends={
        Property(name="SingleConflict", type=mancoosimm_Conflict, multiplicity=Multiplicity(1, 1)),
        Property(name="conflict288", type=mancoosimm_SingleConflict, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pkg289: BinaryAssociation = BinaryAssociation(
    name="pkg289",
    ends={
        Property(name="mancoosimm_Package291", type=mancoosimm_Conflict, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Conflict290", type=mancoosimm_Package, multiplicity=Multiplicity(1, 1))
    }
)
owner293: BinaryAssociation = BinaryAssociation(
    name="owner293",
    ends={
        Property(name="mancoosimm_Conflict294", type=mancoosimm_Conflict, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Conflict292", type=mancoosimm_Conflict, multiplicity=Multiplicity(0, 1))
    }
)
ownerPkg295: BinaryAssociation = BinaryAssociation(
    name="ownerPkg295",
    ends={
        Property(name="mancoosimm_Package297", type=mancoosimm_Conflict, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Conflict296", type=mancoosimm_Package, multiplicity=Multiplicity(1, 1))
    }
)
conflict300: BinaryAssociation = BinaryAssociation(
    name="conflict300",
    ends={
        Property(name="Conflict301", type=mancoosimm_AndConflict, multiplicity=Multiplicity(1, 1)),
        Property(name="andConflict", type=mancoosimm_Conflict, multiplicity=Multiplicity(1, 1))
    }
)
ops302: BinaryAssociation = BinaryAssociation(
    name="ops302",
    ends={
        Property(name="mancoosimm_Conflict303", type=mancoosimm_OrConflict, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_OrConflict", type=mancoosimm_Conflict, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
conflict304: BinaryAssociation = BinaryAssociation(
    name="conflict304",
    ends={
        Property(name="Conflict305", type=mancoosimm_OrConflict, multiplicity=Multiplicity(1, 1)),
        Property(name="orConflict", type=mancoosimm_Conflict, multiplicity=Multiplicity(1, 1))
    }
)
ops298: BinaryAssociation = BinaryAssociation(
    name="ops298",
    ends={
        Property(name="mancoosimm_Conflict299", type=mancoosimm_AndConflict, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_AndConflict", type=mancoosimm_Conflict, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)

# Generalizations
gen_mancoosimm_Configuration_NamedElement = Generalization(general=NamedElement, specific=mancoosimm_Configuration)
gen_mancoosimm_Package_NamedElement = Generalization(general=NamedElement, specific=mancoosimm_Package)
gen_mancoosimm_InstalledPackage_Package = Generalization(general=Package, specific=mancoosimm_InstalledPackage)
gen_mancoosimm_NotInstalledPackage_Package = Generalization(general=Package, specific=mancoosimm_NotInstalledPackage)
gen_mancoosimm_ConfigFilesPackage_Package = Generalization(general=Package, specific=mancoosimm_ConfigFilesPackage)
gen_mancoosimm_UnpackedPackage_Package = Generalization(general=Package, specific=mancoosimm_UnpackedPackage)
gen_mancoosimm_HalfConfiguredPackage_UnpackedPackage = Generalization(general=UnpackedPackage, specific=mancoosimm_HalfConfiguredPackage)
gen_mancoosimm_HalfConfiguredReinstRequiredPackage_UnpackedPackage = Generalization(general=UnpackedPackage, specific=mancoosimm_HalfConfiguredReinstRequiredPackage)
gen_mancoosimm_HalfInstalledPackage_Package = Generalization(general=Package, specific=mancoosimm_HalfInstalledPackage)
gen_mancoosimm_HalfInstalledReinstRequiredPackage_Package = Generalization(general=Package, specific=mancoosimm_HalfInstalledReinstRequiredPackage)
gen_mancoosimm_SrcPackage_InstalledPackage = Generalization(general=InstalledPackage, specific=mancoosimm_SrcPackage)
gen_mancoosimm_BinPackage_InstalledPackage = Generalization(general=InstalledPackage, specific=mancoosimm_BinPackage)
gen_mancoosimm_VirtualPackage_InstalledPackage = Generalization(general=InstalledPackage, specific=mancoosimm_VirtualPackage)
gen_mancoosimm_AndDep_Dependence = Generalization(general=Dependence, specific=mancoosimm_AndDep)
gen_mancoosimm_OrDep_Dependence = Generalization(general=Dependence, specific=mancoosimm_OrDep)
gen_mancoosimm_SingleDep_Dependence = Generalization(general=Dependence, specific=mancoosimm_SingleDep)
gen_mancoosimm_Invariant_NamedElement = Generalization(general=NamedElement, specific=mancoosimm_Invariant)
gen_mancoosimm_Atom_NamedElement = Generalization(general=NamedElement, specific=mancoosimm_Atom)
gen_mancoosimm_Environment_NamedElement = Generalization(general=NamedElement, specific=mancoosimm_Environment)
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
gen_mancoosimm_OrConflict_Conflict = Generalization(general=Conflict, specific=mancoosimm_OrConflict)
gen_mancoosimm_AndConflict_Conflict = Generalization(general=Conflict, specific=mancoosimm_AndConflict)

# Domain Model
domain_model = DomainModel(
    name="mancoosimm",
    types={mancoosimm_NamedElement, mancoosimm_InstalledPackage, mancoosimm_NotInstalledPackage, mancoosimm_Configuration, NamedElement, mancoosimm_FileSystem, mancoosimm_Environment, mancoosimm_HalfConfiguredReinstRequiredPackage, mancoosimm_HalfInstalledReinstRequiredPackage, mancoosimm_ConfigFilesPackage, mancoosimm_UnpackedPackage, mancoosimm_HalfConfiguredPackage, mancoosimm_HalfInstalledPackage, mancoosimm_SrcPackage, mancoosimm_Package, mancoosimm_PackageSetting, Package, mancoosimm_Dependence, mancoosimm_DocumentationFile, mancoosimm_VirtualPackage, mancoosimm_Conflict, mancoosimm_File, UnpackedPackage, InstalledPackage, mancoosimm_BinPackage, mancoosimm_AndDep, mancoosimm_OrDep, mancoosimm_SingleDep, Dependence, mancoosimm_Invariant, mancoosimm_Atom, mancoosimm_AndInv, mancoosimm_OrInv, mancoosimm_NotInv, mancoosimm_Service, mancoosimm_Alternative, mancoosimm_User, mancoosimm_Group, mancoosimm_EmacsPackage, mancoosimm_IconCache, mancoosimm_DesktopDB, mancoosimm_MimeTypeHandlerCache, mancoosimm_LibraryCache, mancoosimm_SkeeperCatalog, mancoosimm_SGMLCatalog, mancoosimm_ModuleCache, mancoosimm_GConf, mancoosimm_Menu, mancoosimm_XFontCache, mancoosimm_ApplicationMenuCatalog, mancoosimm_MenuEntry, mancoosimm_Boot, File, mancoosimm_InformationFile, mancoosimm_MimeTypeHandler, mancoosimm_MimeType, mancoosimm_XFont, mancoosimm_SharedLibrary, mancoosimm_Module, mancoosimm_SGMLDocument, mancoosimm_SkeeperDocument, mancoosimm_SingleConflict, Conflict, mancoosimm_AndConflict, mancoosimm_OrConflict, PriorityType, StatusType, VersionType},
    associations={installedPackages3, fileSystem0, environment1, halfConfiguredReinstRequiredPackages14, halfInstalledReinstRequiredPackages16, notInstalledPackages4, configFilesPackages6, unpackedPackages8, halfConfiguredPackages10, halfInstalledPackages12, sourcePackage21, configuration18, packageSettings20, depends23, recommends26, suggests29, enhances32, predepends35, documentationFiles44, provides37, replaces40, conflict46, files42, files48, buildDepends51, buildConflicts53, srcRef56, impPackage59, andDep62, singleDep65, pkg67, owner71, ownerPkg73, ops76, dependence78, ops79, dependence81, orDep63, atomEl85, and86, or88, not90, left92, right95, left98, dependence83, elem104, runningServices107, alternatives108, users110, groups112, emacspkg114, iconCache116, desktopDb118, right101, mimeTypeHandlerCache120, libraryCache122, skeeperCatalog124, sgmlCatalog126, configuration128, moduleCache129, xfontCaches131, gconf133, menu135, root137, configuration138, allFiles140, confFiles142, schemas144, menu149, entries151, catalog152, env154, menu157, executable159, parent162, env147, services164, executable165, env168, fs170, childs173, parent176, owner178, group180, pkgSettings182, pkg184, current185, location187, env190, services192, files194, pkg196, dependences198, env200, icons202, env204, applications206, env208, handlers210, mimeTypes211, handler213, type215, cache217, mimeTypeHandlers219, cache221, xfonts223, env224, xfontCache226, file228, locations230, sharedLibraries232, env233, file236, libraryCache238, modules240, env241, file244, moduleCache246, documents250, location251, document254, env257, env248, documents259, location260, document263, files266, env268, env270, groups272, home275, env278, users280, conflict283, andConflict284, orConflict285, singleConflict287, pkg289, owner293, ownerPkg295, conflict300, ops302, conflict304, ops298},
    generalizations={gen_mancoosimm_Configuration_NamedElement, gen_mancoosimm_Package_NamedElement, gen_mancoosimm_InstalledPackage_Package, gen_mancoosimm_NotInstalledPackage_Package, gen_mancoosimm_ConfigFilesPackage_Package, gen_mancoosimm_UnpackedPackage_Package, gen_mancoosimm_HalfConfiguredPackage_UnpackedPackage, gen_mancoosimm_HalfConfiguredReinstRequiredPackage_UnpackedPackage, gen_mancoosimm_HalfInstalledPackage_Package, gen_mancoosimm_HalfInstalledReinstRequiredPackage_Package, gen_mancoosimm_SrcPackage_InstalledPackage, gen_mancoosimm_BinPackage_InstalledPackage, gen_mancoosimm_VirtualPackage_InstalledPackage, gen_mancoosimm_AndDep_Dependence, gen_mancoosimm_OrDep_Dependence, gen_mancoosimm_SingleDep_Dependence, gen_mancoosimm_Invariant_NamedElement, gen_mancoosimm_Atom_NamedElement, gen_mancoosimm_Environment_NamedElement, gen_mancoosimm_FileSystem_NamedElement, gen_mancoosimm_ApplicationMenuCatalog_NamedElement, gen_mancoosimm_MenuEntry_NamedElement, gen_mancoosimm_Service_NamedElement, gen_mancoosimm_File_NamedElement, gen_mancoosimm_DocumentationFile_File, gen_mancoosimm_InformationFile_File, gen_mancoosimm_Alternative_NamedElement, gen_mancoosimm_PackageSetting_NamedElement, gen_mancoosimm_XFont_NamedElement, gen_mancoosimm_Module_NamedElement, gen_mancoosimm_SGMLCatalog_NamedElement, gen_mancoosimm_SGMLDocument_NamedElement, gen_mancoosimm_SkeeperCatalog_NamedElement, gen_mancoosimm_SkeeperDocument_NamedElement, gen_mancoosimm_EmacsPackage_NamedElement, gen_mancoosimm_User_NamedElement, gen_mancoosimm_Group_NamedElement, gen_mancoosimm_SingleConflict_Conflict, gen_mancoosimm_OrConflict_Conflict, gen_mancoosimm_AndConflict_Conflict},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)