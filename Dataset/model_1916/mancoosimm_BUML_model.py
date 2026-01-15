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
			EnumerationLiteral(name="unpacked"),
			EnumerationLiteral(name="config_files")
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
mancoosimm_Configuration = Class(name="mancoosimm::Configuration")
NamedElement = Class(name="NamedElement")
mancoosimm_FileSystem = Class(name="mancoosimm::FileSystem")
mancoosimm_InstalledPackage = Class(name="mancoosimm::InstalledPackage")
mancoosimm_NotInstalledPackage = Class(name="mancoosimm::NotInstalledPackage")
mancoosimm_ConfigFilesPackage = Class(name="mancoosimm::ConfigFilesPackage")
mancoosimm_UnpackedPackage = Class(name="mancoosimm::UnpackedPackage")
mancoosimm_HalfConfiguredPackage = Class(name="mancoosimm::HalfConfiguredPackage")
mancoosimm_HalfInstalledPackage = Class(name="mancoosimm::HalfInstalledPackage")
mancoosimm_HalfConfiguredReinstRequiredPackage = Class(name="mancoosimm::HalfConfiguredReinstRequiredPackage")
mancoosimm_HalfInstalledReinstRequiredPackage = Class(name="mancoosimm::HalfInstalledReinstRequiredPackage")
mancoosimm_Package = Class(name="mancoosimm::Package", is_abstract=True)
mancoosimm_PackageSetting = Class(name="mancoosimm::PackageSetting")
Package = Class(name="Package")
mancoosimm_Environment = Class(name="mancoosimm::Environment")
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
mancoosimm_AndInv = Class(name="mancoosimm::AndInv")
mancoosimm_OrInv = Class(name="mancoosimm::OrInv")
mancoosimm_NotInv = Class(name="mancoosimm::NotInv")
mancoosimm_Invariant = Class(name="mancoosimm::Invariant")
mancoosimm_Atom = Class(name="mancoosimm::Atom")
mancoosimm_Service = Class(name="mancoosimm::Service")
mancoosimm_Alternative = Class(name="mancoosimm::Alternative")
mancoosimm_User = Class(name="mancoosimm::User")
mancoosimm_Group = Class(name="mancoosimm::Group")
mancoosimm_EmacsPackage = Class(name="mancoosimm::EmacsPackage")
mancoosimm_DesktopDB = Class(name="mancoosimm::DesktopDB")
mancoosimm_MimeTypeHandlerCache = Class(name="mancoosimm::MimeTypeHandlerCache")
mancoosimm_LibraryCache = Class(name="mancoosimm::LibraryCache")
mancoosimm_SkeeperCatalog = Class(name="mancoosimm::SkeeperCatalog")
mancoosimm_SGMLCatalog = Class(name="mancoosimm::SGMLCatalog")
mancoosimm_IconCache = Class(name="mancoosimm::IconCache")
mancoosimm_ModuleCache = Class(name="mancoosimm::ModuleCache")
mancoosimm_XFontCache = Class(name="mancoosimm::XFontCache")
mancoosimm_GConf = Class(name="mancoosimm::GConf")
mancoosimm_Menu = Class(name="mancoosimm::Menu")
mancoosimm_ApplicationMenuCatalog = Class(name="mancoosimm::ApplicationMenuCatalog")
mancoosimm_MenuEntry = Class(name="mancoosimm::MenuEntry")
mancoosimm_Boot = Class(name="mancoosimm::Boot")
mancoosimm_InformationFile = Class(name="mancoosimm::InformationFile")
File = Class(name="File")
mancoosimm_MimeTypeHandler = Class(name="mancoosimm::MimeTypeHandler")
mancoosimm_MimeType = Class(name="mancoosimm::MimeType")
mancoosimm_XFont = Class(name="mancoosimm::XFont")
mancoosimm_SharedLibrary = Class(name="mancoosimm::SharedLibrary")
mancoosimm_SGMLDocument = Class(name="mancoosimm::SGMLDocument")
mancoosimm_Module = Class(name="mancoosimm::Module")
mancoosimm_SkeeperDocument = Class(name="mancoosimm::SkeeperDocument")
mancoosimm_SingleConflict = Class(name="mancoosimm::SingleConflict")
Conflict = Class(name="Conflict")
mancoosimm_AndConflict = Class(name="mancoosimm::AndConflict")
mancoosimm_OrConflict = Class(name="mancoosimm::OrConflict")

# mancoosimm_NamedElement class attributes and methods
mancoosimm_NamedElement_name: Property = Property(name="name", type=StringType)
mancoosimm_NamedElement.attributes={mancoosimm_NamedElement_name}

# mancoosimm_Configuration class attributes and methods
mancoosimm_Configuration_creationTime: Property = Property(name="creationTime", type=StringType)
mancoosimm_Configuration_systemType: Property = Property(name="systemType", type=StringType)
mancoosimm_Configuration.attributes={mancoosimm_Configuration_systemType, mancoosimm_Configuration_creationTime}

# NamedElement class attributes and methods

# mancoosimm_FileSystem class attributes and methods

# mancoosimm_InstalledPackage class attributes and methods
mancoosimm_InstalledPackage_installedSize: Property = Property(name="installedSize", type=IntegerType)
mancoosimm_InstalledPackage_maintainer: Property = Property(name="maintainer", type=StringType)
mancoosimm_InstalledPackage_fileSize: Property = Property(name="fileSize", type=IntegerType)
mancoosimm_InstalledPackage_checkSum: Property = Property(name="checkSum", type=StringType)
mancoosimm_InstalledPackage_description: Property = Property(name="description", type=StringType)
mancoosimm_InstalledPackage_section: Property = Property(name="section", type=StringType)
mancoosimm_InstalledPackage_tag: Property = Property(name="tag", type=StringType)
mancoosimm_InstalledPackage_uploaders: Property = Property(name="uploaders", type=StringType)
mancoosimm_InstalledPackage_priority: Property = Property(name="priority", type=StringType)
mancoosimm_InstalledPackage.attributes={mancoosimm_InstalledPackage_maintainer, mancoosimm_InstalledPackage_tag, mancoosimm_InstalledPackage_section, mancoosimm_InstalledPackage_fileSize, mancoosimm_InstalledPackage_installedSize, mancoosimm_InstalledPackage_priority, mancoosimm_InstalledPackage_uploaders, mancoosimm_InstalledPackage_checkSum, mancoosimm_InstalledPackage_description}

# mancoosimm_NotInstalledPackage class attributes and methods

# mancoosimm_ConfigFilesPackage class attributes and methods
mancoosimm_ConfigFilesPackage_maintainer: Property = Property(name="maintainer", type=StringType)
mancoosimm_ConfigFilesPackage_checkSum: Property = Property(name="checkSum", type=StringType)
mancoosimm_ConfigFilesPackage_description: Property = Property(name="description", type=StringType)
mancoosimm_ConfigFilesPackage_section: Property = Property(name="section", type=StringType)
mancoosimm_ConfigFilesPackage_tag: Property = Property(name="tag", type=StringType)
mancoosimm_ConfigFilesPackage_priority: Property = Property(name="priority", type=StringType)
mancoosimm_ConfigFilesPackage_uploaders: Property = Property(name="uploaders", type=StringType)
mancoosimm_ConfigFilesPackage.attributes={mancoosimm_ConfigFilesPackage_maintainer, mancoosimm_ConfigFilesPackage_section, mancoosimm_ConfigFilesPackage_uploaders, mancoosimm_ConfigFilesPackage_description, mancoosimm_ConfigFilesPackage_tag, mancoosimm_ConfigFilesPackage_priority, mancoosimm_ConfigFilesPackage_checkSum}

# mancoosimm_UnpackedPackage class attributes and methods
mancoosimm_UnpackedPackage_maintainer: Property = Property(name="maintainer", type=StringType)
mancoosimm_UnpackedPackage_checkSum: Property = Property(name="checkSum", type=StringType)
mancoosimm_UnpackedPackage_description: Property = Property(name="description", type=StringType)
mancoosimm_UnpackedPackage_section: Property = Property(name="section", type=StringType)
mancoosimm_UnpackedPackage_tag: Property = Property(name="tag", type=StringType)
mancoosimm_UnpackedPackage_priority: Property = Property(name="priority", type=StringType)
mancoosimm_UnpackedPackage_uploaders: Property = Property(name="uploaders", type=StringType)
mancoosimm_UnpackedPackage.attributes={mancoosimm_UnpackedPackage_priority, mancoosimm_UnpackedPackage_uploaders, mancoosimm_UnpackedPackage_checkSum, mancoosimm_UnpackedPackage_description, mancoosimm_UnpackedPackage_section, mancoosimm_UnpackedPackage_tag, mancoosimm_UnpackedPackage_maintainer}

# mancoosimm_HalfConfiguredPackage class attributes and methods

# mancoosimm_HalfInstalledPackage class attributes and methods
mancoosimm_HalfInstalledPackage_maintainer: Property = Property(name="maintainer", type=StringType)
mancoosimm_HalfInstalledPackage_checkSum: Property = Property(name="checkSum", type=StringType)
mancoosimm_HalfInstalledPackage_description: Property = Property(name="description", type=StringType)
mancoosimm_HalfInstalledPackage_section: Property = Property(name="section", type=StringType)
mancoosimm_HalfInstalledPackage_tag: Property = Property(name="tag", type=StringType)
mancoosimm_HalfInstalledPackage_priority: Property = Property(name="priority", type=StringType)
mancoosimm_HalfInstalledPackage_uploaders: Property = Property(name="uploaders", type=StringType)
mancoosimm_HalfInstalledPackage.attributes={mancoosimm_HalfInstalledPackage_tag, mancoosimm_HalfInstalledPackage_priority, mancoosimm_HalfInstalledPackage_checkSum, mancoosimm_HalfInstalledPackage_maintainer, mancoosimm_HalfInstalledPackage_uploaders, mancoosimm_HalfInstalledPackage_description, mancoosimm_HalfInstalledPackage_section}

# mancoosimm_HalfConfiguredReinstRequiredPackage class attributes and methods

# mancoosimm_HalfInstalledReinstRequiredPackage class attributes and methods
mancoosimm_HalfInstalledReinstRequiredPackage_maintainer: Property = Property(name="maintainer", type=StringType)
mancoosimm_HalfInstalledReinstRequiredPackage_checkSum: Property = Property(name="checkSum", type=StringType)
mancoosimm_HalfInstalledReinstRequiredPackage_description: Property = Property(name="description", type=StringType)
mancoosimm_HalfInstalledReinstRequiredPackage_section: Property = Property(name="section", type=StringType)
mancoosimm_HalfInstalledReinstRequiredPackage_tag: Property = Property(name="tag", type=StringType)
mancoosimm_HalfInstalledReinstRequiredPackage_priority: Property = Property(name="priority", type=StringType)
mancoosimm_HalfInstalledReinstRequiredPackage_uploaders: Property = Property(name="uploaders", type=StringType)
mancoosimm_HalfInstalledReinstRequiredPackage.attributes={mancoosimm_HalfInstalledReinstRequiredPackage_priority, mancoosimm_HalfInstalledReinstRequiredPackage_tag, mancoosimm_HalfInstalledReinstRequiredPackage_checkSum, mancoosimm_HalfInstalledReinstRequiredPackage_description, mancoosimm_HalfInstalledReinstRequiredPackage_uploaders, mancoosimm_HalfInstalledReinstRequiredPackage_section, mancoosimm_HalfInstalledReinstRequiredPackage_maintainer}

# mancoosimm_Package class attributes and methods
mancoosimm_Package_version: Property = Property(name="version", type=StringType)
mancoosimm_Package_architecture: Property = Property(name="architecture", type=StringType)
mancoosimm_Package.attributes={mancoosimm_Package_architecture, mancoosimm_Package_version}

# mancoosimm_PackageSetting class attributes and methods

# Package class attributes and methods

# mancoosimm_Environment class attributes and methods

# mancoosimm_SrcPackage class attributes and methods

# mancoosimm_Dependence class attributes and methods

# mancoosimm_VirtualPackage class attributes and methods

# mancoosimm_File class attributes and methods
mancoosimm_File_extension: Property = Property(name="extension", type=StringType)
mancoosimm_File_description: Property = Property(name="description", type=StringType)
mancoosimm_File_size: Property = Property(name="size", type=IntegerType)
mancoosimm_File_suid: Property = Property(name="suid", type=BooleanType)
mancoosimm_File_guid: Property = Property(name="guid", type=BooleanType)
mancoosimm_File_permission: Property = Property(name="permission", type=StringType)
mancoosimm_File_location: Property = Property(name="location", type=StringType)
mancoosimm_File_isMissing: Property = Property(name="isMissing", type=BooleanType)
mancoosimm_File_checkSum: Property = Property(name="checkSum", type=StringType)
mancoosimm_File_isDirectory: Property = Property(name="isDirectory", type=BooleanType)
mancoosimm_File.attributes={mancoosimm_File_isMissing, mancoosimm_File_guid, mancoosimm_File_extension, mancoosimm_File_permission, mancoosimm_File_checkSum, mancoosimm_File_location, mancoosimm_File_description, mancoosimm_File_suid, mancoosimm_File_isDirectory, mancoosimm_File_size}

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
mancoosimm_SingleDep.attributes={mancoosimm_SingleDep_value, mancoosimm_SingleDep_version}

# Dependence class attributes and methods

# mancoosimm_AndInv class attributes and methods

# mancoosimm_OrInv class attributes and methods

# mancoosimm_NotInv class attributes and methods

# mancoosimm_Invariant class attributes and methods

# mancoosimm_Atom class attributes and methods

# mancoosimm_Service class attributes and methods

# mancoosimm_Alternative class attributes and methods

# mancoosimm_User class attributes and methods

# mancoosimm_Group class attributes and methods

# mancoosimm_EmacsPackage class attributes and methods

# mancoosimm_DesktopDB class attributes and methods

# mancoosimm_MimeTypeHandlerCache class attributes and methods

# mancoosimm_LibraryCache class attributes and methods

# mancoosimm_SkeeperCatalog class attributes and methods

# mancoosimm_SGMLCatalog class attributes and methods

# mancoosimm_IconCache class attributes and methods
mancoosimm_IconCache_mtime: Property = Property(name="mtime", type=StringType)
mancoosimm_IconCache.attributes={mancoosimm_IconCache_mtime}

# mancoosimm_ModuleCache class attributes and methods
mancoosimm_ModuleCache_version: Property = Property(name="version", type=StringType)
mancoosimm_ModuleCache.attributes={mancoosimm_ModuleCache_version}

# mancoosimm_XFontCache class attributes and methods
mancoosimm_XFontCache_location: Property = Property(name="location", type=StringType)
mancoosimm_XFontCache.attributes={mancoosimm_XFontCache_location}

# mancoosimm_GConf class attributes and methods

# mancoosimm_Menu class attributes and methods

# mancoosimm_ApplicationMenuCatalog class attributes and methods

# mancoosimm_MenuEntry class attributes and methods

# mancoosimm_Boot class attributes and methods

# mancoosimm_InformationFile class attributes and methods

# File class attributes and methods

# mancoosimm_MimeTypeHandler class attributes and methods

# mancoosimm_MimeType class attributes and methods
mancoosimm_MimeType_extension: Property = Property(name="extension", type=StringType)
mancoosimm_MimeType_name: Property = Property(name="name", type=StringType)
mancoosimm_MimeType.attributes={mancoosimm_MimeType_name, mancoosimm_MimeType_extension}

# mancoosimm_XFont class attributes and methods

# mancoosimm_SharedLibrary class attributes and methods
mancoosimm_SharedLibrary_name: Property = Property(name="name", type=StringType)
mancoosimm_SharedLibrary_version: Property = Property(name="version", type=StringType)
mancoosimm_SharedLibrary.attributes={mancoosimm_SharedLibrary_name, mancoosimm_SharedLibrary_version}

# mancoosimm_SGMLDocument class attributes and methods

# mancoosimm_Module class attributes and methods

# mancoosimm_SkeeperDocument class attributes and methods

# mancoosimm_SingleConflict class attributes and methods
mancoosimm_SingleConflict_value: Property = Property(name="value", type=StringType)
mancoosimm_SingleConflict_version: Property = Property(name="version", type=StringType)
mancoosimm_SingleConflict.attributes={mancoosimm_SingleConflict_value, mancoosimm_SingleConflict_version}

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
sourcePackage21: BinaryAssociation = BinaryAssociation(
    name="sourcePackage21",
    ends={
        Property(name="mancoosimm_SrcPackage", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_InstalledPackage22", type=mancoosimm_SrcPackage, multiplicity=Multiplicity(1, 1))
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
files42: BinaryAssociation = BinaryAssociation(
    name="files42",
    ends={
        Property(name="mancoosimm_File", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_InstalledPackage43", type=mancoosimm_File, multiplicity=Multiplicity(0, 9999))
    }
)
documentationFiles44: BinaryAssociation = BinaryAssociation(
    name="documentationFiles44",
    ends={
        Property(name="DocumentationFile", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="pkg45", type=mancoosimm_DocumentationFile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conflict46: BinaryAssociation = BinaryAssociation(
    name="conflict46",
    ends={
        Property(name="mancoosimm_Conflict", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_InstalledPackage47", type=mancoosimm_Conflict, multiplicity=Multiplicity(0, 1), is_composite=True)
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
orDep63: BinaryAssociation = BinaryAssociation(
    name="orDep63",
    ends={
        Property(name="OrDep", type=mancoosimm_Dependence, multiplicity=Multiplicity(1, 1)),
        Property(name="dependence64", type=mancoosimm_OrDep, multiplicity=Multiplicity(0, 1), is_composite=True)
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
ops70: BinaryAssociation = BinaryAssociation(
    name="ops70",
    ends={
        Property(name="mancoosimm_Dependence71", type=mancoosimm_AndDep, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_AndDep", type=mancoosimm_Dependence, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
buildConflicts53: BinaryAssociation = BinaryAssociation(
    name="buildConflicts53",
    ends={
        Property(name="mancoosimm_BinPackage55", type=mancoosimm_SrcPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_SrcPackage54", type=mancoosimm_BinPackage, multiplicity=Multiplicity(0, 9999))
    }
)
dependence72: BinaryAssociation = BinaryAssociation(
    name="dependence72",
    ends={
        Property(name="Dependence", type=mancoosimm_AndDep, multiplicity=Multiplicity(1, 1)),
        Property(name="andDep", type=mancoosimm_Dependence, multiplicity=Multiplicity(1, 1))
    }
)
ops73: BinaryAssociation = BinaryAssociation(
    name="ops73",
    ends={
        Property(name="mancoosimm_Dependence74", type=mancoosimm_OrDep, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_OrDep", type=mancoosimm_Dependence, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
dependence75: BinaryAssociation = BinaryAssociation(
    name="dependence75",
    ends={
        Property(name="Dependence76", type=mancoosimm_OrDep, multiplicity=Multiplicity(1, 1)),
        Property(name="orDep", type=mancoosimm_Dependence, multiplicity=Multiplicity(1, 1))
    }
)
dependence77: BinaryAssociation = BinaryAssociation(
    name="dependence77",
    ends={
        Property(name="Dependence78", type=mancoosimm_SingleDep, multiplicity=Multiplicity(1, 1)),
        Property(name="singleDep", type=mancoosimm_Dependence, multiplicity=Multiplicity(1, 1))
    }
)
atomEl79: BinaryAssociation = BinaryAssociation(
    name="atomEl79",
    ends={
        Property(name="mancoosimm_Invariant", type=mancoosimm_Atom, multiplicity=Multiplicity(0, 1)),
        Property(name="mancoosimm_Atom", type=mancoosimm_Invariant, multiplicity=Multiplicity(1, 1))
    }
)
and80: BinaryAssociation = BinaryAssociation(
    name="and80",
    ends={
        Property(name="mancoosimm_AndInv", type=mancoosimm_Invariant, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Invariant81", type=mancoosimm_AndInv, multiplicity=Multiplicity(0, 1))
    }
)
or82: BinaryAssociation = BinaryAssociation(
    name="or82",
    ends={
        Property(name="mancoosimm_OrInv", type=mancoosimm_Invariant, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Invariant83", type=mancoosimm_OrInv, multiplicity=Multiplicity(0, 1))
    }
)
not84: BinaryAssociation = BinaryAssociation(
    name="not84",
    ends={
        Property(name="mancoosimm_NotInv", type=mancoosimm_Invariant, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Invariant85", type=mancoosimm_NotInv, multiplicity=Multiplicity(0, 1))
    }
)
left86: BinaryAssociation = BinaryAssociation(
    name="left86",
    ends={
        Property(name="mancoosimm_Invariant88", type=mancoosimm_AndInv, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_AndInv87", type=mancoosimm_Invariant, multiplicity=Multiplicity(1, 1))
    }
)
right89: BinaryAssociation = BinaryAssociation(
    name="right89",
    ends={
        Property(name="mancoosimm_Invariant91", type=mancoosimm_AndInv, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_AndInv90", type=mancoosimm_Invariant, multiplicity=Multiplicity(1, 1))
    }
)
left92: BinaryAssociation = BinaryAssociation(
    name="left92",
    ends={
        Property(name="mancoosimm_Invariant94", type=mancoosimm_OrInv, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_OrInv93", type=mancoosimm_Invariant, multiplicity=Multiplicity(1, 1))
    }
)
right95: BinaryAssociation = BinaryAssociation(
    name="right95",
    ends={
        Property(name="mancoosimm_Invariant97", type=mancoosimm_OrInv, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_OrInv96", type=mancoosimm_Invariant, multiplicity=Multiplicity(1, 1))
    }
)
elem98: BinaryAssociation = BinaryAssociation(
    name="elem98",
    ends={
        Property(name="mancoosimm_Invariant100", type=mancoosimm_NotInv, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_NotInv99", type=mancoosimm_Invariant, multiplicity=Multiplicity(1, 1))
    }
)
runningServices101: BinaryAssociation = BinaryAssociation(
    name="runningServices101",
    ends={
        Property(name="Service", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env", type=mancoosimm_Service, multiplicity=Multiplicity(0, 9999))
    }
)
alternatives102: BinaryAssociation = BinaryAssociation(
    name="alternatives102",
    ends={
        Property(name="Alternative", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env103", type=mancoosimm_Alternative, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
users104: BinaryAssociation = BinaryAssociation(
    name="users104",
    ends={
        Property(name="User", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env105", type=mancoosimm_User, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
groups106: BinaryAssociation = BinaryAssociation(
    name="groups106",
    ends={
        Property(name="Group", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env107", type=mancoosimm_Group, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
emacspkg108: BinaryAssociation = BinaryAssociation(
    name="emacspkg108",
    ends={
        Property(name="EmacsPackage", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env109", type=mancoosimm_EmacsPackage, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
desktopDb112: BinaryAssociation = BinaryAssociation(
    name="desktopDb112",
    ends={
        Property(name="DesktopDB", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env113", type=mancoosimm_DesktopDB, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mimeTypeHandlerCache114: BinaryAssociation = BinaryAssociation(
    name="mimeTypeHandlerCache114",
    ends={
        Property(name="MimeTypeHandlerCache", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env115", type=mancoosimm_MimeTypeHandlerCache, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
libraryCache116: BinaryAssociation = BinaryAssociation(
    name="libraryCache116",
    ends={
        Property(name="LibraryCache", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env117", type=mancoosimm_LibraryCache, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
skeeperCatalog118: BinaryAssociation = BinaryAssociation(
    name="skeeperCatalog118",
    ends={
        Property(name="SkeeperCatalog", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env119", type=mancoosimm_SkeeperCatalog, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sgmlCatalog120: BinaryAssociation = BinaryAssociation(
    name="sgmlCatalog120",
    ends={
        Property(name="SGMLCatalog", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env121", type=mancoosimm_SGMLCatalog, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
configuration122: BinaryAssociation = BinaryAssociation(
    name="configuration122",
    ends={
        Property(name="Configuration", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="environment", type=mancoosimm_Configuration, multiplicity=Multiplicity(1, 1))
    }
)
iconCache110: BinaryAssociation = BinaryAssociation(
    name="iconCache110",
    ends={
        Property(name="IconCache", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env111", type=mancoosimm_IconCache, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
moduleCache123: BinaryAssociation = BinaryAssociation(
    name="moduleCache123",
    ends={
        Property(name="ModuleCache", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env124", type=mancoosimm_ModuleCache, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
xfontCaches125: BinaryAssociation = BinaryAssociation(
    name="xfontCaches125",
    ends={
        Property(name="XFontCache", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env126", type=mancoosimm_XFontCache, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
gconf127: BinaryAssociation = BinaryAssociation(
    name="gconf127",
    ends={
        Property(name="GConf", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env128", type=mancoosimm_GConf, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
menu129: BinaryAssociation = BinaryAssociation(
    name="menu129",
    ends={
        Property(name="Menu", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="env130", type=mancoosimm_Menu, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
root131: BinaryAssociation = BinaryAssociation(
    name="root131",
    ends={
        Property(name="File", type=mancoosimm_FileSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="fs", type=mancoosimm_File, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
configuration132: BinaryAssociation = BinaryAssociation(
    name="configuration132",
    ends={
        Property(name="Configuration133", type=mancoosimm_FileSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="fileSystem", type=mancoosimm_Configuration, multiplicity=Multiplicity(1, 1))
    }
)
allFiles134: BinaryAssociation = BinaryAssociation(
    name="allFiles134",
    ends={
        Property(name="mancoosimm_File135", type=mancoosimm_FileSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_FileSystem", type=mancoosimm_File, multiplicity=Multiplicity(0, 9999))
    }
)
confFiles136: BinaryAssociation = BinaryAssociation(
    name="confFiles136",
    ends={
        Property(name="mancoosimm_File137", type=mancoosimm_GConf, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_GConf", type=mancoosimm_File, multiplicity=Multiplicity(0, 9999))
    }
)
schemas138: BinaryAssociation = BinaryAssociation(
    name="schemas138",
    ends={
        Property(name="mancoosimm_File140", type=mancoosimm_GConf, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_GConf139", type=mancoosimm_File, multiplicity=Multiplicity(0, 9999))
    }
)
env141: BinaryAssociation = BinaryAssociation(
    name="env141",
    ends={
        Property(name="Environment142", type=mancoosimm_GConf, multiplicity=Multiplicity(1, 1)),
        Property(name="gconf", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
menu143: BinaryAssociation = BinaryAssociation(
    name="menu143",
    ends={
        Property(name="Menu144", type=mancoosimm_ApplicationMenuCatalog, multiplicity=Multiplicity(1, 1)),
        Property(name="catalog", type=mancoosimm_Menu, multiplicity=Multiplicity(1, 1))
    }
)
entries145: BinaryAssociation = BinaryAssociation(
    name="entries145",
    ends={
        Property(name="MenuEntry", type=mancoosimm_Menu, multiplicity=Multiplicity(1, 1)),
        Property(name="menu", type=mancoosimm_MenuEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
catalog146: BinaryAssociation = BinaryAssociation(
    name="catalog146",
    ends={
        Property(name="ApplicationMenuCatalog", type=mancoosimm_Menu, multiplicity=Multiplicity(1, 1)),
        Property(name="menu147", type=mancoosimm_ApplicationMenuCatalog, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
env148: BinaryAssociation = BinaryAssociation(
    name="env148",
    ends={
        Property(name="Environment150", type=mancoosimm_Menu, multiplicity=Multiplicity(1, 1)),
        Property(name="menu149", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
executable153: BinaryAssociation = BinaryAssociation(
    name="executable153",
    ends={
        Property(name="mancoosimm_File154", type=mancoosimm_MenuEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_MenuEntry", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
parent156: BinaryAssociation = BinaryAssociation(
    name="parent156",
    ends={
        Property(name="mancoosimm_MenuEntry157", type=mancoosimm_MenuEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_MenuEntry155", type=mancoosimm_MenuEntry, multiplicity=Multiplicity(1, 1))
    }
)
services158: BinaryAssociation = BinaryAssociation(
    name="services158",
    ends={
        Property(name="mancoosimm_Service", type=mancoosimm_Boot, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Boot", type=mancoosimm_Service, multiplicity=Multiplicity(1, 9999))
    }
)
executable159: BinaryAssociation = BinaryAssociation(
    name="executable159",
    ends={
        Property(name="mancoosimm_File161", type=mancoosimm_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Service160", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
env162: BinaryAssociation = BinaryAssociation(
    name="env162",
    ends={
        Property(name="Environment163", type=mancoosimm_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="runningServices", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
menu151: BinaryAssociation = BinaryAssociation(
    name="menu151",
    ends={
        Property(name="Menu152", type=mancoosimm_MenuEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="entries", type=mancoosimm_Menu, multiplicity=Multiplicity(1, 1))
    }
)
fs164: BinaryAssociation = BinaryAssociation(
    name="fs164",
    ends={
        Property(name="FileSystem165", type=mancoosimm_File, multiplicity=Multiplicity(1, 1)),
        Property(name="root", type=mancoosimm_FileSystem, multiplicity=Multiplicity(0, 1))
    }
)
childs167: BinaryAssociation = BinaryAssociation(
    name="childs167",
    ends={
        Property(name="File168", type=mancoosimm_File, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=mancoosimm_File, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent170: BinaryAssociation = BinaryAssociation(
    name="parent170",
    ends={
        Property(name="File171", type=mancoosimm_File, multiplicity=Multiplicity(1, 1)),
        Property(name="childs", type=mancoosimm_File, multiplicity=Multiplicity(0, 1))
    }
)
owner172: BinaryAssociation = BinaryAssociation(
    name="owner172",
    ends={
        Property(name="mancoosimm_User", type=mancoosimm_File, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_File173", type=mancoosimm_User, multiplicity=Multiplicity(1, 1))
    }
)
group174: BinaryAssociation = BinaryAssociation(
    name="group174",
    ends={
        Property(name="mancoosimm_Group", type=mancoosimm_File, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_File175", type=mancoosimm_Group, multiplicity=Multiplicity(1, 1))
    }
)
pkg178: BinaryAssociation = BinaryAssociation(
    name="pkg178",
    ends={
        Property(name="InstalledPackage", type=mancoosimm_DocumentationFile, multiplicity=Multiplicity(1, 1)),
        Property(name="documentationFiles", type=mancoosimm_InstalledPackage, multiplicity=Multiplicity(1, 1))
    }
)
current179: BinaryAssociation = BinaryAssociation(
    name="current179",
    ends={
        Property(name="mancoosimm_File180", type=mancoosimm_Alternative, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Alternative", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
location181: BinaryAssociation = BinaryAssociation(
    name="location181",
    ends={
        Property(name="mancoosimm_File183", type=mancoosimm_Alternative, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Alternative182", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
env184: BinaryAssociation = BinaryAssociation(
    name="env184",
    ends={
        Property(name="Environment185", type=mancoosimm_Alternative, multiplicity=Multiplicity(1, 1)),
        Property(name="alternatives", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
services186: BinaryAssociation = BinaryAssociation(
    name="services186",
    ends={
        Property(name="mancoosimm_Service187", type=mancoosimm_PackageSetting, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_PackageSetting", type=mancoosimm_Service, multiplicity=Multiplicity(0, 9999))
    }
)
files188: BinaryAssociation = BinaryAssociation(
    name="files188",
    ends={
        Property(name="File189", type=mancoosimm_PackageSetting, multiplicity=Multiplicity(1, 1)),
        Property(name="pkgSettings", type=mancoosimm_File, multiplicity=Multiplicity(0, 9999))
    }
)
pkgSettings176: BinaryAssociation = BinaryAssociation(
    name="pkgSettings176",
    ends={
        Property(name="PackageSetting177", type=mancoosimm_File, multiplicity=Multiplicity(1, 1)),
        Property(name="files", type=mancoosimm_PackageSetting, multiplicity=Multiplicity(0, 9999))
    }
)
pkg190: BinaryAssociation = BinaryAssociation(
    name="pkg190",
    ends={
        Property(name="Package", type=mancoosimm_PackageSetting, multiplicity=Multiplicity(1, 1)),
        Property(name="packageSettings", type=mancoosimm_Package, multiplicity=Multiplicity(1, 1))
    }
)
dependences192: BinaryAssociation = BinaryAssociation(
    name="dependences192",
    ends={
        Property(name="mancoosimm_PackageSetting193", type=mancoosimm_PackageSetting, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_PackageSetting191", type=mancoosimm_PackageSetting, multiplicity=Multiplicity(0, 9999))
    }
)
env194: BinaryAssociation = BinaryAssociation(
    name="env194",
    ends={
        Property(name="Environment195", type=mancoosimm_IconCache, multiplicity=Multiplicity(1, 1)),
        Property(name="iconCache", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
icons196: BinaryAssociation = BinaryAssociation(
    name="icons196",
    ends={
        Property(name="mancoosimm_File197", type=mancoosimm_IconCache, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_IconCache", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
env198: BinaryAssociation = BinaryAssociation(
    name="env198",
    ends={
        Property(name="Environment199", type=mancoosimm_DesktopDB, multiplicity=Multiplicity(1, 1)),
        Property(name="desktopDb", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
env202: BinaryAssociation = BinaryAssociation(
    name="env202",
    ends={
        Property(name="Environment203", type=mancoosimm_MimeTypeHandlerCache, multiplicity=Multiplicity(1, 1)),
        Property(name="mimeTypeHandlerCache", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
handlers204: BinaryAssociation = BinaryAssociation(
    name="handlers204",
    ends={
        Property(name="MimeTypeHandler", type=mancoosimm_MimeTypeHandlerCache, multiplicity=Multiplicity(1, 1)),
        Property(name="cache", type=mancoosimm_MimeTypeHandler, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mimeTypes205: BinaryAssociation = BinaryAssociation(
    name="mimeTypes205",
    ends={
        Property(name="MimeType", type=mancoosimm_MimeTypeHandlerCache, multiplicity=Multiplicity(1, 1)),
        Property(name="cache206", type=mancoosimm_MimeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
handler207: BinaryAssociation = BinaryAssociation(
    name="handler207",
    ends={
        Property(name="mancoosimm_File208", type=mancoosimm_MimeTypeHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_MimeTypeHandler", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
type209: BinaryAssociation = BinaryAssociation(
    name="type209",
    ends={
        Property(name="MimeType210", type=mancoosimm_MimeTypeHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="mimeTypeHandlers", type=mancoosimm_MimeType, multiplicity=Multiplicity(0, 1))
    }
)
cache211: BinaryAssociation = BinaryAssociation(
    name="cache211",
    ends={
        Property(name="MimeTypeHandlerCache212", type=mancoosimm_MimeTypeHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="handlers", type=mancoosimm_MimeTypeHandlerCache, multiplicity=Multiplicity(1, 1))
    }
)
applications200: BinaryAssociation = BinaryAssociation(
    name="applications200",
    ends={
        Property(name="mancoosimm_File201", type=mancoosimm_DesktopDB, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_DesktopDB", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
mimeTypeHandlers213: BinaryAssociation = BinaryAssociation(
    name="mimeTypeHandlers213",
    ends={
        Property(name="MimeTypeHandler214", type=mancoosimm_MimeType, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=mancoosimm_MimeTypeHandler, multiplicity=Multiplicity(0, 9999))
    }
)
cache215: BinaryAssociation = BinaryAssociation(
    name="cache215",
    ends={
        Property(name="MimeTypeHandlerCache216", type=mancoosimm_MimeType, multiplicity=Multiplicity(1, 1)),
        Property(name="mimeTypes", type=mancoosimm_MimeTypeHandlerCache, multiplicity=Multiplicity(1, 1))
    }
)
xfonts217: BinaryAssociation = BinaryAssociation(
    name="xfonts217",
    ends={
        Property(name="XFont", type=mancoosimm_XFontCache, multiplicity=Multiplicity(1, 1)),
        Property(name="xfontCache", type=mancoosimm_XFont, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
env218: BinaryAssociation = BinaryAssociation(
    name="env218",
    ends={
        Property(name="Environment219", type=mancoosimm_XFontCache, multiplicity=Multiplicity(1, 1)),
        Property(name="xfontCaches", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
xfontCache220: BinaryAssociation = BinaryAssociation(
    name="xfontCache220",
    ends={
        Property(name="XFontCache221", type=mancoosimm_XFont, multiplicity=Multiplicity(1, 1)),
        Property(name="xfonts", type=mancoosimm_XFontCache, multiplicity=Multiplicity(1, 1))
    }
)
locations224: BinaryAssociation = BinaryAssociation(
    name="locations224",
    ends={
        Property(name="mancoosimm_File225", type=mancoosimm_LibraryCache, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_LibraryCache", type=mancoosimm_File, multiplicity=Multiplicity(0, 9999))
    }
)
sharedLibraries226: BinaryAssociation = BinaryAssociation(
    name="sharedLibraries226",
    ends={
        Property(name="SharedLibrary", type=mancoosimm_LibraryCache, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryCache", type=mancoosimm_SharedLibrary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
env227: BinaryAssociation = BinaryAssociation(
    name="env227",
    ends={
        Property(name="Environment229", type=mancoosimm_LibraryCache, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryCache228", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
file230: BinaryAssociation = BinaryAssociation(
    name="file230",
    ends={
        Property(name="mancoosimm_File231", type=mancoosimm_SharedLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_SharedLibrary", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
libraryCache232: BinaryAssociation = BinaryAssociation(
    name="libraryCache232",
    ends={
        Property(name="LibraryCache233", type=mancoosimm_SharedLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="sharedLibraries", type=mancoosimm_LibraryCache, multiplicity=Multiplicity(1, 1))
    }
)
file222: BinaryAssociation = BinaryAssociation(
    name="file222",
    ends={
        Property(name="mancoosimm_File223", type=mancoosimm_XFont, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_XFont", type=mancoosimm_File, multiplicity=Multiplicity(1, 9999))
    }
)
modules234: BinaryAssociation = BinaryAssociation(
    name="modules234",
    ends={
        Property(name="Module", type=mancoosimm_ModuleCache, multiplicity=Multiplicity(1, 1)),
        Property(name="moduleCache", type=mancoosimm_Module, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
env235: BinaryAssociation = BinaryAssociation(
    name="env235",
    ends={
        Property(name="Environment237", type=mancoosimm_ModuleCache, multiplicity=Multiplicity(1, 1)),
        Property(name="moduleCache236", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
file238: BinaryAssociation = BinaryAssociation(
    name="file238",
    ends={
        Property(name="mancoosimm_File239", type=mancoosimm_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Module", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
moduleCache240: BinaryAssociation = BinaryAssociation(
    name="moduleCache240",
    ends={
        Property(name="ModuleCache241", type=mancoosimm_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="modules", type=mancoosimm_ModuleCache, multiplicity=Multiplicity(1, 1))
    }
)
env242: BinaryAssociation = BinaryAssociation(
    name="env242",
    ends={
        Property(name="Environment243", type=mancoosimm_SGMLCatalog, multiplicity=Multiplicity(1, 1)),
        Property(name="sgmlCatalog", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
documents244: BinaryAssociation = BinaryAssociation(
    name="documents244",
    ends={
        Property(name="mancoosimm_SGMLDocument", type=mancoosimm_SGMLCatalog, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_SGMLCatalog", type=mancoosimm_SGMLDocument, multiplicity=Multiplicity(0, 9999))
    }
)
location245: BinaryAssociation = BinaryAssociation(
    name="location245",
    ends={
        Property(name="mancoosimm_File247", type=mancoosimm_SGMLDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_SGMLDocument246", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
document248: BinaryAssociation = BinaryAssociation(
    name="document248",
    ends={
        Property(name="mancoosimm_File250", type=mancoosimm_SGMLDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_SGMLDocument249", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
env251: BinaryAssociation = BinaryAssociation(
    name="env251",
    ends={
        Property(name="Environment252", type=mancoosimm_SkeeperCatalog, multiplicity=Multiplicity(1, 1)),
        Property(name="skeeperCatalog", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
documents253: BinaryAssociation = BinaryAssociation(
    name="documents253",
    ends={
        Property(name="mancoosimm_SkeeperDocument", type=mancoosimm_SkeeperCatalog, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_SkeeperCatalog", type=mancoosimm_SkeeperDocument, multiplicity=Multiplicity(0, 9999))
    }
)
location254: BinaryAssociation = BinaryAssociation(
    name="location254",
    ends={
        Property(name="mancoosimm_File256", type=mancoosimm_SkeeperDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_SkeeperDocument255", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
document257: BinaryAssociation = BinaryAssociation(
    name="document257",
    ends={
        Property(name="mancoosimm_File259", type=mancoosimm_SkeeperDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_SkeeperDocument258", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
files260: BinaryAssociation = BinaryAssociation(
    name="files260",
    ends={
        Property(name="mancoosimm_File261", type=mancoosimm_EmacsPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_EmacsPackage", type=mancoosimm_File, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
env262: BinaryAssociation = BinaryAssociation(
    name="env262",
    ends={
        Property(name="Environment263", type=mancoosimm_EmacsPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="emacspkg", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
env264: BinaryAssociation = BinaryAssociation(
    name="env264",
    ends={
        Property(name="Environment265", type=mancoosimm_User, multiplicity=Multiplicity(1, 1)),
        Property(name="users", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
groups266: BinaryAssociation = BinaryAssociation(
    name="groups266",
    ends={
        Property(name="Group268", type=mancoosimm_User, multiplicity=Multiplicity(1, 1)),
        Property(name="users267", type=mancoosimm_Group, multiplicity=Multiplicity(1, 9999))
    }
)
home269: BinaryAssociation = BinaryAssociation(
    name="home269",
    ends={
        Property(name="mancoosimm_File271", type=mancoosimm_User, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_User270", type=mancoosimm_File, multiplicity=Multiplicity(1, 1))
    }
)
env272: BinaryAssociation = BinaryAssociation(
    name="env272",
    ends={
        Property(name="Environment273", type=mancoosimm_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="groups", type=mancoosimm_Environment, multiplicity=Multiplicity(1, 1))
    }
)
users274: BinaryAssociation = BinaryAssociation(
    name="users274",
    ends={
        Property(name="User276", type=mancoosimm_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="groups275", type=mancoosimm_User, multiplicity=Multiplicity(0, 9999))
    }
)
conflict277: BinaryAssociation = BinaryAssociation(
    name="conflict277",
    ends={
        Property(name="Conflict", type=mancoosimm_SingleConflict, multiplicity=Multiplicity(1, 1)),
        Property(name="singleConflict", type=mancoosimm_Conflict, multiplicity=Multiplicity(1, 1))
    }
)
andConflict278: BinaryAssociation = BinaryAssociation(
    name="andConflict278",
    ends={
        Property(name="AndConflict", type=mancoosimm_Conflict, multiplicity=Multiplicity(1, 1)),
        Property(name="conflict", type=mancoosimm_AndConflict, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
orConflict279: BinaryAssociation = BinaryAssociation(
    name="orConflict279",
    ends={
        Property(name="OrConflict", type=mancoosimm_Conflict, multiplicity=Multiplicity(1, 1)),
        Property(name="conflict280", type=mancoosimm_OrConflict, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
singleConflict281: BinaryAssociation = BinaryAssociation(
    name="singleConflict281",
    ends={
        Property(name="SingleConflict", type=mancoosimm_Conflict, multiplicity=Multiplicity(1, 1)),
        Property(name="conflict282", type=mancoosimm_SingleConflict, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pkg283: BinaryAssociation = BinaryAssociation(
    name="pkg283",
    ends={
        Property(name="mancoosimm_Package285", type=mancoosimm_Conflict, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_Conflict284", type=mancoosimm_Package, multiplicity=Multiplicity(1, 1))
    }
)
ops286: BinaryAssociation = BinaryAssociation(
    name="ops286",
    ends={
        Property(name="mancoosimm_Conflict287", type=mancoosimm_AndConflict, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_AndConflict", type=mancoosimm_Conflict, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
conflict288: BinaryAssociation = BinaryAssociation(
    name="conflict288",
    ends={
        Property(name="Conflict289", type=mancoosimm_AndConflict, multiplicity=Multiplicity(1, 1)),
        Property(name="andConflict", type=mancoosimm_Conflict, multiplicity=Multiplicity(1, 1))
    }
)
ops290: BinaryAssociation = BinaryAssociation(
    name="ops290",
    ends={
        Property(name="mancoosimm_Conflict291", type=mancoosimm_OrConflict, multiplicity=Multiplicity(1, 1)),
        Property(name="mancoosimm_OrConflict", type=mancoosimm_Conflict, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
conflict292: BinaryAssociation = BinaryAssociation(
    name="conflict292",
    ends={
        Property(name="Conflict293", type=mancoosimm_OrConflict, multiplicity=Multiplicity(1, 1)),
        Property(name="orConflict", type=mancoosimm_Conflict, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_mancoosimm_Configuration_NamedElement = Generalization(general=NamedElement, specific=mancoosimm_Configuration)
gen_mancoosimm_Package_NamedElement = Generalization(general=NamedElement, specific=mancoosimm_Package)
gen_mancoosimm_InstalledPackage_Package = Generalization(general=Package, specific=mancoosimm_InstalledPackage)
gen_mancoosimm_NotInstalledPackage_Package = Generalization(general=Package, specific=mancoosimm_NotInstalledPackage)
gen_mancoosimm_ConfigFilesPackage_Package = Generalization(general=Package, specific=mancoosimm_ConfigFilesPackage)
gen_mancoosimm_HalfConfiguredPackage_UnpackedPackage = Generalization(general=UnpackedPackage, specific=mancoosimm_HalfConfiguredPackage)
gen_mancoosimm_HalfConfiguredReinstRequiredPackage_UnpackedPackage = Generalization(general=UnpackedPackage, specific=mancoosimm_HalfConfiguredReinstRequiredPackage)
gen_mancoosimm_HalfInstalledPackage_Package = Generalization(general=Package, specific=mancoosimm_HalfInstalledPackage)
gen_mancoosimm_HalfInstalledReinstRequiredPackage_Package = Generalization(general=Package, specific=mancoosimm_HalfInstalledReinstRequiredPackage)
gen_mancoosimm_SrcPackage_InstalledPackage = Generalization(general=InstalledPackage, specific=mancoosimm_SrcPackage)
gen_mancoosimm_UnpackedPackage_Package = Generalization(general=Package, specific=mancoosimm_UnpackedPackage)
gen_mancoosimm_VirtualPackage_InstalledPackage = Generalization(general=InstalledPackage, specific=mancoosimm_VirtualPackage)
gen_mancoosimm_AndDep_Dependence = Generalization(general=Dependence, specific=mancoosimm_AndDep)
gen_mancoosimm_BinPackage_InstalledPackage = Generalization(general=InstalledPackage, specific=mancoosimm_BinPackage)
gen_mancoosimm_OrDep_Dependence = Generalization(general=Dependence, specific=mancoosimm_OrDep)
gen_mancoosimm_SingleDep_Dependence = Generalization(general=Dependence, specific=mancoosimm_SingleDep)
gen_mancoosimm_Atom_NamedElement = Generalization(general=NamedElement, specific=mancoosimm_Atom)
gen_mancoosimm_Invariant_NamedElement = Generalization(general=NamedElement, specific=mancoosimm_Invariant)
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
    types={mancoosimm_NamedElement, mancoosimm_Configuration, NamedElement, mancoosimm_FileSystem, mancoosimm_InstalledPackage, mancoosimm_NotInstalledPackage, mancoosimm_ConfigFilesPackage, mancoosimm_UnpackedPackage, mancoosimm_HalfConfiguredPackage, mancoosimm_HalfInstalledPackage, mancoosimm_HalfConfiguredReinstRequiredPackage, mancoosimm_HalfInstalledReinstRequiredPackage, mancoosimm_Package, mancoosimm_PackageSetting, Package, mancoosimm_Environment, mancoosimm_SrcPackage, mancoosimm_Dependence, mancoosimm_VirtualPackage, mancoosimm_File, mancoosimm_DocumentationFile, mancoosimm_Conflict, UnpackedPackage, InstalledPackage, mancoosimm_BinPackage, mancoosimm_AndDep, mancoosimm_OrDep, mancoosimm_SingleDep, Dependence, mancoosimm_AndInv, mancoosimm_OrInv, mancoosimm_NotInv, mancoosimm_Invariant, mancoosimm_Atom, mancoosimm_Service, mancoosimm_Alternative, mancoosimm_User, mancoosimm_Group, mancoosimm_EmacsPackage, mancoosimm_DesktopDB, mancoosimm_MimeTypeHandlerCache, mancoosimm_LibraryCache, mancoosimm_SkeeperCatalog, mancoosimm_SGMLCatalog, mancoosimm_IconCache, mancoosimm_ModuleCache, mancoosimm_XFontCache, mancoosimm_GConf, mancoosimm_Menu, mancoosimm_ApplicationMenuCatalog, mancoosimm_MenuEntry, mancoosimm_Boot, mancoosimm_InformationFile, File, mancoosimm_MimeTypeHandler, mancoosimm_MimeType, mancoosimm_XFont, mancoosimm_SharedLibrary, mancoosimm_SGMLDocument, mancoosimm_Module, mancoosimm_SkeeperDocument, mancoosimm_SingleConflict, Conflict, mancoosimm_AndConflict, mancoosimm_OrConflict, PriorityType, StatusType, VersionType},
    associations={installedPackages3, notInstalledPackages4, configFilesPackages6, unpackedPackages8, halfConfiguredPackages10, halfInstalledPackages12, halfConfiguredReinstRequiredPackages14, halfInstalledReinstRequiredPackages16, configuration18, packageSettings20, fileSystem0, environment1, sourcePackage21, depends23, recommends26, suggests29, enhances32, predepends35, provides37, replaces40, files42, documentationFiles44, conflict46, files48, buildDepends51, srcRef56, impPackage59, andDep62, orDep63, singleDep65, pkg67, ops70, buildConflicts53, dependence72, ops73, dependence75, dependence77, atomEl79, and80, or82, not84, left86, right89, left92, right95, elem98, runningServices101, alternatives102, users104, groups106, emacspkg108, desktopDb112, mimeTypeHandlerCache114, libraryCache116, skeeperCatalog118, sgmlCatalog120, configuration122, iconCache110, moduleCache123, xfontCaches125, gconf127, menu129, root131, configuration132, allFiles134, confFiles136, schemas138, env141, menu143, entries145, catalog146, env148, executable153, parent156, services158, executable159, env162, menu151, fs164, childs167, parent170, owner172, group174, pkg178, current179, location181, env184, services186, files188, pkgSettings176, pkg190, dependences192, env194, icons196, env198, env202, handlers204, mimeTypes205, handler207, type209, cache211, applications200, mimeTypeHandlers213, cache215, xfonts217, env218, xfontCache220, locations224, sharedLibraries226, env227, file230, libraryCache232, file222, modules234, env235, file238, moduleCache240, env242, documents244, location245, document248, env251, documents253, location254, document257, files260, env262, env264, groups266, home269, env272, users274, conflict277, andConflict278, orConflict279, singleConflict281, pkg283, ops286, conflict288, ops290, conflict292},
    generalizations={gen_mancoosimm_Configuration_NamedElement, gen_mancoosimm_Package_NamedElement, gen_mancoosimm_InstalledPackage_Package, gen_mancoosimm_NotInstalledPackage_Package, gen_mancoosimm_ConfigFilesPackage_Package, gen_mancoosimm_HalfConfiguredPackage_UnpackedPackage, gen_mancoosimm_HalfConfiguredReinstRequiredPackage_UnpackedPackage, gen_mancoosimm_HalfInstalledPackage_Package, gen_mancoosimm_HalfInstalledReinstRequiredPackage_Package, gen_mancoosimm_SrcPackage_InstalledPackage, gen_mancoosimm_UnpackedPackage_Package, gen_mancoosimm_VirtualPackage_InstalledPackage, gen_mancoosimm_AndDep_Dependence, gen_mancoosimm_BinPackage_InstalledPackage, gen_mancoosimm_OrDep_Dependence, gen_mancoosimm_SingleDep_Dependence, gen_mancoosimm_Atom_NamedElement, gen_mancoosimm_Invariant_NamedElement, gen_mancoosimm_Environment_NamedElement, gen_mancoosimm_FileSystem_NamedElement, gen_mancoosimm_ApplicationMenuCatalog_NamedElement, gen_mancoosimm_MenuEntry_NamedElement, gen_mancoosimm_Service_NamedElement, gen_mancoosimm_File_NamedElement, gen_mancoosimm_DocumentationFile_File, gen_mancoosimm_InformationFile_File, gen_mancoosimm_Alternative_NamedElement, gen_mancoosimm_PackageSetting_NamedElement, gen_mancoosimm_XFont_NamedElement, gen_mancoosimm_Module_NamedElement, gen_mancoosimm_SGMLCatalog_NamedElement, gen_mancoosimm_SGMLDocument_NamedElement, gen_mancoosimm_SkeeperCatalog_NamedElement, gen_mancoosimm_SkeeperDocument_NamedElement, gen_mancoosimm_EmacsPackage_NamedElement, gen_mancoosimm_User_NamedElement, gen_mancoosimm_Group_NamedElement, gen_mancoosimm_SingleConflict_Conflict, gen_mancoosimm_OrConflict_Conflict, gen_mancoosimm_AndConflict_Conflict},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)