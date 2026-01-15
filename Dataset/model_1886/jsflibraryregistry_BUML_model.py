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
JSFVersion: Enumeration = Enumeration(
    name="JSFVersion",
    literals={
            EnumerationLiteral(name="UNKNOWN"),
			EnumerationLiteral(name="v1_1"),
			EnumerationLiteral(name="v1_2")
    }
)

# Classes
jsflibraryregistry_JSFLibraryRegistry = Class(name="jsflibraryregistry::JSFLibraryRegistry")
jsflibraryregistry_PluginProvidedJSFLibrary = Class(name="jsflibraryregistry::PluginProvidedJSFLibrary")
jsflibraryregistry_ArchiveFile = Class(name="jsflibraryregistry::ArchiveFile")
jsflibraryregistry_JSFLibrary = Class(name="jsflibraryregistry::JSFLibrary")
JSFLibrary = Class(name="JSFLibrary")

# jsflibraryregistry_JSFLibraryRegistry class attributes and methods
jsflibraryregistry_JSFLibraryRegistry_DefaultImplementationID: Property = Property(name="DefaultImplementationID", type=StringType)
jsflibraryregistry_JSFLibraryRegistry_m_getJSFLibraryByID: Method = Method(name="getJSFLibraryByID", parameters={Parameter(name='ID')}, type=StringType)
jsflibraryregistry_JSFLibraryRegistry_m_getJSFLibrariesByName: Method = Method(name="getJSFLibrariesByName", parameters={Parameter(name='name')}, type=StringType)
jsflibraryregistry_JSFLibraryRegistry_m_getImplJSFLibraries: Method = Method(name="getImplJSFLibraries", parameters={}, type=StringType)
jsflibraryregistry_JSFLibraryRegistry_m_getNonImplJSFLibraries: Method = Method(name="getNonImplJSFLibraries", parameters={}, type=StringType)
jsflibraryregistry_JSFLibraryRegistry_m_getAllJSFLibraries: Method = Method(name="getAllJSFLibraries", parameters={}, type=StringType)
jsflibraryregistry_JSFLibraryRegistry_m_addJSFLibrary: Method = Method(name="addJSFLibrary", parameters={Parameter(name='library')}, type=BooleanType)
jsflibraryregistry_JSFLibraryRegistry_m_removeJSFLibrary: Method = Method(name="removeJSFLibrary", parameters={Parameter(name='library')}, type=BooleanType)
jsflibraryregistry_JSFLibraryRegistry_m_getDefaultImplementation: Method = Method(name="getDefaultImplementation", parameters={}, type=StringType)
jsflibraryregistry_JSFLibraryRegistry_m_setDefaultImplementation: Method = Method(name="setDefaultImplementation", parameters={Parameter(name='implementation')})
jsflibraryregistry_JSFLibraryRegistry.attributes={jsflibraryregistry_JSFLibraryRegistry_DefaultImplementationID}
jsflibraryregistry_JSFLibraryRegistry.methods={jsflibraryregistry_JSFLibraryRegistry_m_getNonImplJSFLibraries, jsflibraryregistry_JSFLibraryRegistry_m_getAllJSFLibraries, jsflibraryregistry_JSFLibraryRegistry_m_getImplJSFLibraries, jsflibraryregistry_JSFLibraryRegistry_m_addJSFLibrary, jsflibraryregistry_JSFLibraryRegistry_m_getJSFLibrariesByName, jsflibraryregistry_JSFLibraryRegistry_m_getJSFLibraryByID, jsflibraryregistry_JSFLibraryRegistry_m_getDefaultImplementation, jsflibraryregistry_JSFLibraryRegistry_m_setDefaultImplementation, jsflibraryregistry_JSFLibraryRegistry_m_removeJSFLibrary}

# jsflibraryregistry_PluginProvidedJSFLibrary class attributes and methods
jsflibraryregistry_PluginProvidedJSFLibrary_pluginID: Property = Property(name="pluginID", type=StringType)
jsflibraryregistry_PluginProvidedJSFLibrary_Label: Property = Property(name="Label", type=StringType)
jsflibraryregistry_PluginProvidedJSFLibrary.attributes={jsflibraryregistry_PluginProvidedJSFLibrary_Label, jsflibraryregistry_PluginProvidedJSFLibrary_pluginID}

# jsflibraryregistry_ArchiveFile class attributes and methods
jsflibraryregistry_ArchiveFile_RelativeToWorkspace: Property = Property(name="RelativeToWorkspace", type=BooleanType)
jsflibraryregistry_ArchiveFile_SourceLocation: Property = Property(name="SourceLocation", type=StringType)
jsflibraryregistry_ArchiveFile_RelativeDestLocation: Property = Property(name="RelativeDestLocation", type=StringType)
jsflibraryregistry_ArchiveFile_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
jsflibraryregistry_ArchiveFile_m_getPath: Method = Method(name="getPath", parameters={}, type=StringType)
jsflibraryregistry_ArchiveFile_m_exists: Method = Method(name="exists", parameters={}, type=BooleanType)
jsflibraryregistry_ArchiveFile_m_equals: Method = Method(name="equals", parameters={Parameter(name='object')}, type=BooleanType)
jsflibraryregistry_ArchiveFile_m_hashCode: Method = Method(name="hashCode", parameters={}, type=IntegerType)
jsflibraryregistry_ArchiveFile_m_copyTo: Method = Method(name="copyTo", parameters={Parameter(name='baseDestLocation')}, type=BooleanType)
jsflibraryregistry_ArchiveFile_m_getResolvedSourceLocation: Method = Method(name="getResolvedSourceLocation", parameters={}, type=StringType)
jsflibraryregistry_ArchiveFile.attributes={jsflibraryregistry_ArchiveFile_SourceLocation, jsflibraryregistry_ArchiveFile_RelativeDestLocation, jsflibraryregistry_ArchiveFile_RelativeToWorkspace}
jsflibraryregistry_ArchiveFile.methods={jsflibraryregistry_ArchiveFile_m_exists, jsflibraryregistry_ArchiveFile_m_hashCode, jsflibraryregistry_ArchiveFile_m_getResolvedSourceLocation, jsflibraryregistry_ArchiveFile_m_getPath, jsflibraryregistry_ArchiveFile_m_getName, jsflibraryregistry_ArchiveFile_m_copyTo, jsflibraryregistry_ArchiveFile_m_equals}

# jsflibraryregistry_JSFLibrary class attributes and methods
jsflibraryregistry_JSFLibrary_ID: Property = Property(name="ID", type=StringType)
jsflibraryregistry_JSFLibrary_Name: Property = Property(name="Name", type=StringType)
jsflibraryregistry_JSFLibrary_JSFVersion: Property = Property(name="JSFVersion", type=StringType)
jsflibraryregistry_JSFLibrary_Deployed: Property = Property(name="Deployed", type=BooleanType)
jsflibraryregistry_JSFLibrary_Implementation: Property = Property(name="Implementation", type=BooleanType)
jsflibraryregistry_JSFLibrary_m_containsArchiveFile: Method = Method(name="containsArchiveFile", parameters={Parameter(name='fullPath')}, type=BooleanType)
jsflibraryregistry_JSFLibrary_m_getWorkingCopy: Method = Method(name="getWorkingCopy", parameters={}, type=StringType)
jsflibraryregistry_JSFLibrary_m_updateValues: Method = Method(name="updateValues", parameters={Parameter(name='otherLibrary')})
jsflibraryregistry_JSFLibrary_m_copyTo: Method = Method(name="copyTo", parameters={Parameter(name='baseDestLocation')}, type=BooleanType)
jsflibraryregistry_JSFLibrary_m_getLabel: Method = Method(name="getLabel", parameters={}, type=StringType)
jsflibraryregistry_JSFLibrary.attributes={jsflibraryregistry_JSFLibrary_JSFVersion, jsflibraryregistry_JSFLibrary_ID, jsflibraryregistry_JSFLibrary_Implementation, jsflibraryregistry_JSFLibrary_Deployed, jsflibraryregistry_JSFLibrary_Name}
jsflibraryregistry_JSFLibrary.methods={jsflibraryregistry_JSFLibrary_m_getLabel, jsflibraryregistry_JSFLibrary_m_copyTo, jsflibraryregistry_JSFLibrary_m_containsArchiveFile, jsflibraryregistry_JSFLibrary_m_getWorkingCopy, jsflibraryregistry_JSFLibrary_m_updateValues}

# JSFLibrary class attributes and methods

# Relationships
PluginProvidedJSFLibraries1: BinaryAssociation = BinaryAssociation(
    name="PluginProvidedJSFLibraries1",
    ends={
        Property(name="jsflibraryregistry_PluginProvidedJSFLibrary", type=jsflibraryregistry_JSFLibraryRegistry, multiplicity=Multiplicity(1, 1)),
        Property(name="jsflibraryregistry_JSFLibraryRegistry2", type=jsflibraryregistry_PluginProvidedJSFLibrary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ArchiveFiles3: BinaryAssociation = BinaryAssociation(
    name="ArchiveFiles3",
    ends={
        Property(name="ArchiveFile", type=jsflibraryregistry_JSFLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="JSFLibrary", type=jsflibraryregistry_ArchiveFile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
JSFLibraries0: BinaryAssociation = BinaryAssociation(
    name="JSFLibraries0",
    ends={
        Property(name="jsflibraryregistry_JSFLibrary", type=jsflibraryregistry_JSFLibraryRegistry, multiplicity=Multiplicity(1, 1)),
        Property(name="jsflibraryregistry_JSFLibraryRegistry", type=jsflibraryregistry_JSFLibrary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
JSFLibrary4: BinaryAssociation = BinaryAssociation(
    name="JSFLibrary4",
    ends={
        Property(name="JSFLibrary5", type=jsflibraryregistry_ArchiveFile, multiplicity=Multiplicity(1, 1)),
        Property(name="ArchiveFiles", type=jsflibraryregistry_JSFLibrary, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_jsflibraryregistry_PluginProvidedJSFLibrary_JSFLibrary = Generalization(general=JSFLibrary, specific=jsflibraryregistry_PluginProvidedJSFLibrary)

# Domain Model
domain_model = DomainModel(
    name="jsflibraryregistry",
    types={jsflibraryregistry_JSFLibraryRegistry, jsflibraryregistry_PluginProvidedJSFLibrary, jsflibraryregistry_ArchiveFile, jsflibraryregistry_JSFLibrary, JSFLibrary, JSFVersion},
    associations={PluginProvidedJSFLibraries1, ArchiveFiles3, JSFLibraries0, JSFLibrary4},
    generalizations={gen_jsflibraryregistry_PluginProvidedJSFLibrary_JSFLibrary},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)