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
LibrarySourceType: Enumeration = Enumeration(
    name="LibrarySourceType",
    literals={
            EnumerationLiteral(name="ZipFile"),
			EnumerationLiteral(name="Folder"),
			EnumerationLiteral(name="JavascriptFile")
    }
)

# Classes
basic_TypeItem = Class(name="basic::TypeItem", is_abstract=True)
basic_Alias = Class(name="basic::Alias")
TypeItem = Class(name="TypeItem")
basic_File = Class(name="basic::File")
basic_Layout = Class(name="basic::Layout")
basic_Feature = Class(name="basic::Feature")
basic_Widget = Class(name="basic::Widget")
Alias = Class(name="Alias")
basic_Plugin = Class(name="basic::Plugin")
basic_ExtJSProject = Class(name="basic::ExtJSProject")
basic_ExecutionEnvironment = Class(name="basic::ExecutionEnvironment")
basic_Library = Class(name="basic::Library")
basic_LibrarySource = Class(name="basic::LibrarySource")
basic_Event = Class(name="basic::Event")
basic_Parameter = Class(name="basic::Parameter")
basic_CoreVersionDefault = Class(name="basic::CoreVersionDefault")

# basic_TypeItem class attributes and methods
basic_TypeItem_sourceStart: Property = Property(name="sourceStart", type=IntegerType)
basic_TypeItem_sourceEnd: Property = Property(name="sourceEnd", type=IntegerType)
basic_TypeItem_typeName: Property = Property(name="typeName", type=StringType)
basic_TypeItem.attributes={basic_TypeItem_sourceStart, basic_TypeItem_typeName, basic_TypeItem_sourceEnd}

# basic_Alias class attributes and methods
basic_Alias_rawName: Property = Property(name="rawName", type=StringType)
basic_Alias_name: Property = Property(name="name", type=StringType)
basic_Alias.attributes={basic_Alias_rawName, basic_Alias_name}

# TypeItem class attributes and methods

# basic_File class attributes and methods
basic_File_name: Property = Property(name="name", type=StringType)
basic_File_m_cleanAliases: Method = Method(name="cleanAliases", parameters={})
basic_File_m_addAlias: Method = Method(name="addAlias", parameters={Parameter(name='sourceStart'), Parameter(name='name'), Parameter(name='sourceEnd'), Parameter(name='type')})
basic_File.attributes={basic_File_name}
basic_File.methods={basic_File_m_addAlias, basic_File_m_cleanAliases}

# basic_Layout class attributes and methods

# basic_Feature class attributes and methods

# basic_Widget class attributes and methods

# Alias class attributes and methods

# basic_Plugin class attributes and methods

# basic_ExtJSProject class attributes and methods
basic_ExtJSProject_name: Property = Property(name="name", type=StringType)
basic_ExtJSProject.attributes={basic_ExtJSProject_name}

# basic_ExecutionEnvironment class attributes and methods
basic_ExecutionEnvironment_name: Property = Property(name="name", type=StringType)
basic_ExecutionEnvironment_builtin: Property = Property(name="builtin", type=BooleanType)
basic_ExecutionEnvironment_versions: Property = Property(name="versions", type=StringType)
basic_ExecutionEnvironment_corePath: Property = Property(name="corePath", type=StringType)
basic_ExecutionEnvironment_coreType: Property = Property(name="coreType", type=StringType)
basic_ExecutionEnvironment_libraries: Property = Property(name="libraries", type=StringType)
basic_ExecutionEnvironment_facet: Property = Property(name="facet", type=StringType)
basic_ExecutionEnvironment.attributes={basic_ExecutionEnvironment_builtin, basic_ExecutionEnvironment_corePath, basic_ExecutionEnvironment_coreType, basic_ExecutionEnvironment_facet, basic_ExecutionEnvironment_versions, basic_ExecutionEnvironment_libraries, basic_ExecutionEnvironment_name}

# basic_Library class attributes and methods
basic_Library_name: Property = Property(name="name", type=StringType)
basic_Library_builtin: Property = Property(name="builtin", type=BooleanType)
basic_Library_versions: Property = Property(name="versions", type=StringType)
basic_Library_senchaTouchVersions: Property = Property(name="senchaTouchVersions", type=StringType)
basic_Library.attributes={basic_Library_builtin, basic_Library_senchaTouchVersions, basic_Library_name, basic_Library_versions}

# basic_LibrarySource class attributes and methods
basic_LibrarySource_type: Property = Property(name="type", type=StringType)
basic_LibrarySource_path: Property = Property(name="path", type=StringType)
basic_LibrarySource_inclusions: Property = Property(name="inclusions", type=StringType)
basic_LibrarySource_exclusions: Property = Property(name="exclusions", type=StringType)
basic_LibrarySource.attributes={basic_LibrarySource_type, basic_LibrarySource_path, basic_LibrarySource_exclusions, basic_LibrarySource_inclusions}

# basic_Event class attributes and methods
basic_Event_name: Property = Property(name="name", type=StringType)
basic_Event_description: Property = Property(name="description", type=StringType)
basic_Event.attributes={basic_Event_description, basic_Event_name}

# basic_Parameter class attributes and methods
basic_Parameter_description: Property = Property(name="description", type=StringType)
basic_Parameter_name: Property = Property(name="name", type=StringType)
basic_Parameter_type: Property = Property(name="type", type=StringType)
basic_Parameter.attributes={basic_Parameter_name, basic_Parameter_description, basic_Parameter_type}

# basic_CoreVersionDefault class attributes and methods
basic_CoreVersionDefault_version: Property = Property(name="version", type=StringType)
basic_CoreVersionDefault_facet: Property = Property(name="facet", type=StringType)
basic_CoreVersionDefault_coreLib: Property = Property(name="coreLib", type=StringType)
basic_CoreVersionDefault.attributes={basic_CoreVersionDefault_coreLib, basic_CoreVersionDefault_version, basic_CoreVersionDefault_facet}

# Relationships
files0: BinaryAssociation = BinaryAssociation(
    name="files0",
    ends={
        Property(name="basic_File", type=basic_ExtJSProject, multiplicity=Multiplicity(1, 1)),
        Property(name="basic_ExtJSProject", type=basic_File, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
aliases1: BinaryAssociation = BinaryAssociation(
    name="aliases1",
    ends={
        Property(name="basic_Alias", type=basic_File, multiplicity=Multiplicity(1, 1)),
        Property(name="basic_File2", type=basic_Alias, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sources4: BinaryAssociation = BinaryAssociation(
    name="sources4",
    ends={
        Property(name="basic_LibrarySource", type=basic_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="basic_Library", type=basic_LibrarySource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters3: BinaryAssociation = BinaryAssociation(
    name="parameters3",
    ends={
        Property(name="basic_Parameter", type=basic_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="basic_Event", type=basic_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
files5: BinaryAssociation = BinaryAssociation(
    name="files5",
    ends={
        Property(name="basic_File7", type=basic_LibrarySource, multiplicity=Multiplicity(1, 1)),
        Property(name="basic_LibrarySource6", type=basic_File, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_basic_Alias_TypeItem = Generalization(general=TypeItem, specific=basic_Alias)
gen_basic_Layout_Alias = Generalization(general=Alias, specific=basic_Layout)
gen_basic_Feature_Alias = Generalization(general=Alias, specific=basic_Feature)
gen_basic_Widget_Alias = Generalization(general=Alias, specific=basic_Widget)
gen_basic_Plugin_Alias = Generalization(general=Alias, specific=basic_Plugin)
gen_basic_Event_TypeItem = Generalization(general=TypeItem, specific=basic_Event)

# Domain Model
domain_model = DomainModel(
    name="basic",
    types={basic_TypeItem, basic_Alias, TypeItem, basic_File, basic_Layout, basic_Feature, basic_Widget, Alias, basic_Plugin, basic_ExtJSProject, basic_ExecutionEnvironment, basic_Library, basic_LibrarySource, basic_Event, basic_Parameter, basic_CoreVersionDefault, LibrarySourceType},
    associations={files0, aliases1, sources4, parameters3, files5},
    generalizations={gen_basic_Alias_TypeItem, gen_basic_Layout_Alias, gen_basic_Feature_Alias, gen_basic_Widget_Alias, gen_basic_Plugin_Alias, gen_basic_Event_TypeItem},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)