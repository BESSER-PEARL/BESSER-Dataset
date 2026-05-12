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
sourcecleaner_Java = Class(name="sourcecleaner_Java")
sourcecleaner_Manifest = Class(name="sourcecleaner_Manifest")
sourcecleaner_Build = Class(name="sourcecleaner_Build")
sourcecleaner_Plugin = Class(name="sourcecleaner_Plugin")
sourcecleaner_Configuration = Class(name="sourcecleaner_Configuration")
sourcecleaner_Project = Class(name="sourcecleaner_Project")
LocatedElement = Class(name="LocatedElement")
sourcecleaner_ClassPath = Class(name="sourcecleaner_ClassPath")
sourcecleaner_Export = Class(name="sourcecleaner_Export")
sourcecleaner_Extension = Class(name="sourcecleaner_Extension")
sourcecleaner_ExtensionPoint = Class(name="sourcecleaner_ExtensionPoint")
sourcecleaner_Schema = Class(name="sourcecleaner_Schema")
sourcecleaner_LocatedElement = Class(name="sourcecleaner_LocatedElement", is_abstract=True)
sourcecleaner_Source = Class(name="sourcecleaner_Source", is_abstract=True)
Source = Class(name="Source")
sourcecleaner_Dependency = Class(name="sourcecleaner_Dependency")
sourcecleaner_ExtensionAttribute = Class(name="sourcecleaner_ExtensionAttribute")
sourcecleaner_ExtensionReference = Class(name="sourcecleaner_ExtensionReference")

# sourcecleaner_Java class attributes and methods
sourcecleaner_Java_package: Property = Property(name="package", type=StringType)
sourcecleaner_Java.attributes={sourcecleaner_Java_package}

# sourcecleaner_Manifest class attributes and methods
sourcecleaner_Manifest_lazy: Property = Property(name="lazy", type=BooleanType)
sourcecleaner_Manifest_executionEnvironment: Property = Property(name="executionEnvironment", type=StringType)
sourcecleaner_Manifest_diagraph: Property = Property(name="diagraph", type=BooleanType)
sourcecleaner_Manifest_symbolicName: Property = Property(name="symbolicName", type=StringType)
sourcecleaner_Manifest_singleton: Property = Property(name="singleton", type=BooleanType)
sourcecleaner_Manifest_vendor: Property = Property(name="vendor", type=StringType)
sourcecleaner_Manifest_version: Property = Property(name="version", type=StringType)
sourcecleaner_Manifest_versionId: Property = Property(name="versionId", type=StringType)
sourcecleaner_Manifest_versionQualifier: Property = Property(name="versionQualifier", type=StringType)
sourcecleaner_Manifest.attributes={sourcecleaner_Manifest_lazy, sourcecleaner_Manifest_singleton, sourcecleaner_Manifest_symbolicName, sourcecleaner_Manifest_executionEnvironment, sourcecleaner_Manifest_versionQualifier, sourcecleaner_Manifest_versionId, sourcecleaner_Manifest_vendor, sourcecleaner_Manifest_version, sourcecleaner_Manifest_diagraph}

# sourcecleaner_Build class attributes and methods

# sourcecleaner_Plugin class attributes and methods
sourcecleaner_Plugin_extra: Property = Property(name="extra", type=StringType)
sourcecleaner_Plugin.attributes={sourcecleaner_Plugin_extra}

# sourcecleaner_Configuration class attributes and methods
sourcecleaner_Configuration_location: Property = Property(name="location", type=StringType)
sourcecleaner_Configuration_temp: Property = Property(name="temp", type=StringType)
sourcecleaner_Configuration.attributes={sourcecleaner_Configuration_temp, sourcecleaner_Configuration_location}

# sourcecleaner_Project class attributes and methods
sourcecleaner_Project_id: Property = Property(name="id", type=IntegerType)
sourcecleaner_Project_workspace: Property = Property(name="workspace", type=StringType)
sourcecleaner_Project.attributes={sourcecleaner_Project_id, sourcecleaner_Project_workspace}

# LocatedElement class attributes and methods

# sourcecleaner_ClassPath class attributes and methods
sourcecleaner_ClassPath_name: Property = Property(name="name", type=StringType)
sourcecleaner_ClassPath.attributes={sourcecleaner_ClassPath_name}

# sourcecleaner_Export class attributes and methods
sourcecleaner_Export_name: Property = Property(name="name", type=StringType)
sourcecleaner_Export.attributes={sourcecleaner_Export_name}

# sourcecleaner_Extension class attributes and methods
sourcecleaner_Extension_pointId: Property = Property(name="pointId", type=StringType)
sourcecleaner_Extension_clazz: Property = Property(name="clazz", type=StringType)
sourcecleaner_Extension_id: Property = Property(name="id", type=StringType)
sourcecleaner_Extension_name: Property = Property(name="name", type=StringType)
sourcecleaner_Extension_extra: Property = Property(name="extra", type=StringType)
sourcecleaner_Extension_diagraph: Property = Property(name="diagraph", type=BooleanType)
sourcecleaner_Extension.attributes={sourcecleaner_Extension_clazz, sourcecleaner_Extension_extra, sourcecleaner_Extension_name, sourcecleaner_Extension_diagraph, sourcecleaner_Extension_pointId, sourcecleaner_Extension_id}

# sourcecleaner_ExtensionPoint class attributes and methods
sourcecleaner_ExtensionPoint_id: Property = Property(name="id", type=StringType)
sourcecleaner_ExtensionPoint_name: Property = Property(name="name", type=StringType)
sourcecleaner_ExtensionPoint_schema: Property = Property(name="schema", type=StringType)
sourcecleaner_ExtensionPoint_diagraph: Property = Property(name="diagraph", type=BooleanType)
sourcecleaner_ExtensionPoint.attributes={sourcecleaner_ExtensionPoint_diagraph, sourcecleaner_ExtensionPoint_id, sourcecleaner_ExtensionPoint_name, sourcecleaner_ExtensionPoint_schema}

# sourcecleaner_Schema class attributes and methods
sourcecleaner_Schema_extensionName: Property = Property(name="extensionName", type=StringType)
sourcecleaner_Schema_extensionId: Property = Property(name="extensionId", type=StringType)
sourcecleaner_Schema_pluginName: Property = Property(name="pluginName", type=StringType)
sourcecleaner_Schema.attributes={sourcecleaner_Schema_pluginName, sourcecleaner_Schema_extensionName, sourcecleaner_Schema_extensionId}

# sourcecleaner_LocatedElement class attributes and methods
sourcecleaner_LocatedElement_absolutePath: Property = Property(name="absolutePath", type=StringType)
sourcecleaner_LocatedElement_name: Property = Property(name="name", type=StringType)
sourcecleaner_LocatedElement.attributes={sourcecleaner_LocatedElement_name, sourcecleaner_LocatedElement_absolutePath}

# sourcecleaner_Source class attributes and methods
sourcecleaner_Source_comment: Property = Property(name="comment", type=StringType)
sourcecleaner_Source_handled: Property = Property(name="handled", type=BooleanType)
sourcecleaner_Source_mark: Property = Property(name="mark", type=BooleanType)
sourcecleaner_Source_content: Property = Property(name="content", type=StringType)
sourcecleaner_Source.attributes={sourcecleaner_Source_comment, sourcecleaner_Source_mark, sourcecleaner_Source_content, sourcecleaner_Source_handled}

# Source class attributes and methods

# sourcecleaner_Dependency class attributes and methods
sourcecleaner_Dependency_name: Property = Property(name="name", type=StringType)
sourcecleaner_Dependency_version: Property = Property(name="version", type=StringType)
sourcecleaner_Dependency_reexport: Property = Property(name="reexport", type=BooleanType)
sourcecleaner_Dependency_diagraph: Property = Property(name="diagraph", type=BooleanType)
sourcecleaner_Dependency.attributes={sourcecleaner_Dependency_reexport, sourcecleaner_Dependency_version, sourcecleaner_Dependency_diagraph, sourcecleaner_Dependency_name}

# sourcecleaner_ExtensionAttribute class attributes and methods
sourcecleaner_ExtensionAttribute_name: Property = Property(name="name", type=StringType)
sourcecleaner_ExtensionAttribute_value: Property = Property(name="value", type=StringType)
sourcecleaner_ExtensionAttribute.attributes={sourcecleaner_ExtensionAttribute_value, sourcecleaner_ExtensionAttribute_name}

# sourcecleaner_ExtensionReference class attributes and methods
sourcecleaner_ExtensionReference_name: Property = Property(name="name", type=StringType)
sourcecleaner_ExtensionReference_java: Property = Property(name="java", type=StringType)
sourcecleaner_ExtensionReference_package: Property = Property(name="package", type=StringType)
sourcecleaner_ExtensionReference_project: Property = Property(name="project", type=StringType)
sourcecleaner_ExtensionReference.attributes={sourcecleaner_ExtensionReference_package, sourcecleaner_ExtensionReference_name, sourcecleaner_ExtensionReference_project, sourcecleaner_ExtensionReference_java}

# Relationships
sources1: BinaryAssociation = BinaryAssociation(
    name="sources1",
    ends={
        Property(name="Java", type=sourcecleaner_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="project", type=sourcecleaner_Java, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
manifest2: BinaryAssociation = BinaryAssociation(
    name="manifest2",
    ends={
        Property(name="sourcecleaner_Manifest", type=sourcecleaner_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="sourcecleaner_Project3", type=sourcecleaner_Manifest, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
build4: BinaryAssociation = BinaryAssociation(
    name="build4",
    ends={
        Property(name="sourcecleaner_Build", type=sourcecleaner_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="sourcecleaner_Project5", type=sourcecleaner_Build, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
plugin6: BinaryAssociation = BinaryAssociation(
    name="plugin6",
    ends={
        Property(name="Plugin", type=sourcecleaner_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="project7", type=sourcecleaner_Plugin, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
projects0: BinaryAssociation = BinaryAssociation(
    name="projects0",
    ends={
        Property(name="sourcecleaner_Project", type=sourcecleaner_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="sourcecleaner_Configuration", type=sourcecleaner_Project, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependencies11: BinaryAssociation = BinaryAssociation(
    name="dependencies11",
    ends={
        Property(name="requerant", type=sourcecleaner_Dependency, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="Dependency", type=sourcecleaner_Manifest, multiplicity=Multiplicity(1, 1))
    }
)
classpathes12: BinaryAssociation = BinaryAssociation(
    name="classpathes12",
    ends={
        Property(name="sourcecleaner_ClassPath", type=sourcecleaner_Manifest, multiplicity=Multiplicity(1, 1)),
        Property(name="sourcecleaner_Manifest13", type=sourcecleaner_ClassPath, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exports14: BinaryAssociation = BinaryAssociation(
    name="exports14",
    ends={
        Property(name="sourcecleaner_Export", type=sourcecleaner_Manifest, multiplicity=Multiplicity(1, 1)),
        Property(name="sourcecleaner_Manifest15", type=sourcecleaner_Export, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensionPoint16: BinaryAssociation = BinaryAssociation(
    name="extensionPoint16",
    ends={
        Property(name="ExtensionPoint", type=sourcecleaner_Extension, multiplicity=Multiplicity(1, 1)),
        Property(name="extensions", type=sourcecleaner_ExtensionPoint, multiplicity=Multiplicity(0, 1))
    }
)
schema8: BinaryAssociation = BinaryAssociation(
    name="schema8",
    ends={
        Property(name="Schema", type=sourcecleaner_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="project9", type=sourcecleaner_Schema, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
project10: BinaryAssociation = BinaryAssociation(
    name="project10",
    ends={
        Property(name="Project", type=sourcecleaner_Java, multiplicity=Multiplicity(1, 1)),
        Property(name="sources", type=sourcecleaner_Project, multiplicity=Multiplicity(0, 1))
    }
)
extensions23: BinaryAssociation = BinaryAssociation(
    name="extensions23",
    ends={
        Property(name="Extension", type=sourcecleaner_ExtensionPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="extensionPoint", type=sourcecleaner_Extension, multiplicity=Multiplicity(0, 9999))
    }
)
plugin24: BinaryAssociation = BinaryAssociation(
    name="plugin24",
    ends={
        Property(name="Plugin25", type=sourcecleaner_ExtensionPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="extensionPoints", type=sourcecleaner_Plugin, multiplicity=Multiplicity(0, 1))
    }
)
extensions26: BinaryAssociation = BinaryAssociation(
    name="extensions26",
    ends={
        Property(name="sourcecleaner_Extension27", type=sourcecleaner_Plugin, multiplicity=Multiplicity(1, 1)),
        Property(name="sourcecleaner_Plugin", type=sourcecleaner_Extension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensionPoints28: BinaryAssociation = BinaryAssociation(
    name="extensionPoints28",
    ends={
        Property(name="ExtensionPoint29", type=sourcecleaner_Plugin, multiplicity=Multiplicity(1, 1)),
        Property(name="plugin", type=sourcecleaner_ExtensionPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes17: BinaryAssociation = BinaryAssociation(
    name="attributes17",
    ends={
        Property(name="sourcecleaner_ExtensionAttribute", type=sourcecleaner_Extension, multiplicity=Multiplicity(1, 1)),
        Property(name="sourcecleaner_Extension", type=sourcecleaner_ExtensionAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implements18: BinaryAssociation = BinaryAssociation(
    name="implements18",
    ends={
        Property(name="sourcecleaner_Java", type=sourcecleaner_Extension, multiplicity=Multiplicity(1, 1)),
        Property(name="sourcecleaner_Extension19", type=sourcecleaner_Java, multiplicity=Multiplicity(0, 1))
    }
)
dependency20: BinaryAssociation = BinaryAssociation(
    name="dependency20",
    ends={
        Property(name="sourcecleaner_Manifest21", type=sourcecleaner_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="sourcecleaner_Dependency", type=sourcecleaner_Manifest, multiplicity=Multiplicity(0, 1))
    }
)
requerant22: BinaryAssociation = BinaryAssociation(
    name="requerant22",
    ends={
        Property(name="Manifest", type=sourcecleaner_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="dependencies", type=sourcecleaner_Manifest, multiplicity=Multiplicity(0, 1))
    }
)
project30: BinaryAssociation = BinaryAssociation(
    name="project30",
    ends={
        Property(name="Project32", type=sourcecleaner_Plugin, multiplicity=Multiplicity(1, 1)),
        Property(name="plugin31", type=sourcecleaner_Project, multiplicity=Multiplicity(0, 1))
    }
)
references33: BinaryAssociation = BinaryAssociation(
    name="references33",
    ends={
        Property(name="ExtensionReference", type=sourcecleaner_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema", type=sourcecleaner_ExtensionReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
project34: BinaryAssociation = BinaryAssociation(
    name="project34",
    ends={
        Property(name="Project36", type=sourcecleaner_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema35", type=sourcecleaner_Project, multiplicity=Multiplicity(0, 1))
    }
)
schema37: BinaryAssociation = BinaryAssociation(
    name="schema37",
    ends={
        Property(name="Schema38", type=sourcecleaner_ExtensionReference, multiplicity=Multiplicity(1, 1)),
        Property(name="references", type=sourcecleaner_Schema, multiplicity=Multiplicity(0, 1))
    }
)
javaclass39: BinaryAssociation = BinaryAssociation(
    name="javaclass39",
    ends={
        Property(name="sourcecleaner_Java40", type=sourcecleaner_ExtensionReference, multiplicity=Multiplicity(1, 1)),
        Property(name="sourcecleaner_ExtensionReference", type=sourcecleaner_Java, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_sourcecleaner_Project_LocatedElement = Generalization(general=LocatedElement, specific=sourcecleaner_Project)
gen_sourcecleaner_Source_LocatedElement = Generalization(general=LocatedElement, specific=sourcecleaner_Source)
gen_sourcecleaner_Java_Source = Generalization(general=Source, specific=sourcecleaner_Java)
gen_sourcecleaner_Manifest_Source = Generalization(general=Source, specific=sourcecleaner_Manifest)
gen_sourcecleaner_Plugin_Source = Generalization(general=Source, specific=sourcecleaner_Plugin)
gen_sourcecleaner_Build_Source = Generalization(general=Source, specific=sourcecleaner_Build)
gen_sourcecleaner_Schema_Source = Generalization(general=Source, specific=sourcecleaner_Schema)

# Domain Model
domain_model = DomainModel(
    name="sourcecleaner",
    types={sourcecleaner_Java, sourcecleaner_Manifest, sourcecleaner_Build, sourcecleaner_Plugin, sourcecleaner_Configuration, sourcecleaner_Project, LocatedElement, sourcecleaner_ClassPath, sourcecleaner_Export, sourcecleaner_Extension, sourcecleaner_ExtensionPoint, sourcecleaner_Schema, sourcecleaner_LocatedElement, sourcecleaner_Source, Source, sourcecleaner_Dependency, sourcecleaner_ExtensionAttribute, sourcecleaner_ExtensionReference},
    associations={sources1, manifest2, build4, plugin6, projects0, dependencies11, classpathes12, exports14, extensionPoint16, schema8, project10, extensions23, plugin24, extensions26, extensionPoints28, attributes17, implements18, dependency20, requerant22, project30, references33, project34, schema37, javaclass39},
    generalizations={gen_sourcecleaner_Project_LocatedElement, gen_sourcecleaner_Source_LocatedElement, gen_sourcecleaner_Java_Source, gen_sourcecleaner_Manifest_Source, gen_sourcecleaner_Plugin_Source, gen_sourcecleaner_Build_Source, gen_sourcecleaner_Schema_Source},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)