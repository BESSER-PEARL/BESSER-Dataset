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
Ant_Project = Class(name="Ant_Project")
Ant_Target = Class(name="Ant_Target")
Ant_Path = Class(name="Ant_Path")
Ant_Property = Class(name="Ant_Property", is_abstract=True)
Ant_TaskDef = Class(name="Ant_TaskDef")
Ant_PropertyName = Class(name="Ant_PropertyName")
Property_ = Class(name="Property")
Ant_PropertyValue = Class(name="Ant_PropertyValue")
PropertyName = Class(name="PropertyName")
Ant_PropertyLocation = Class(name="Ant_PropertyLocation")
Ant_PropertyFile = Class(name="Ant_PropertyFile")
Ant_PropertyEnv = Class(name="Ant_PropertyEnv")
InExcludes = Class(name="InExcludes")
Ant_Excludes = Class(name="Ant_Excludes")
Ant_IncludesFile = Class(name="Ant_IncludesFile")
Ant_ExcludesFile = Class(name="Ant_ExcludesFile")
Ant_FileList = Class(name="Ant_FileList")
Ant_Filter = Class(name="Ant_Filter")
Ant_FiltersFile = Class(name="Ant_FiltersFile")
Ant_PathElement = Class(name="Ant_PathElement")
Ant_Task = Class(name="Ant_Task", is_abstract=True)
Ant_Pattern = Class(name="Ant_Pattern", is_abstract=True)
Ant_Basic = Class(name="Ant_Basic", is_abstract=True)
Pattern = Class(name="Pattern")
Ant_Mapper = Class(name="Ant_Mapper")
Basic = Class(name="Basic")
Ant_InExcludes = Class(name="Ant_InExcludes", is_abstract=True)
Ant_Includes = Class(name="Ant_Includes")
Ant_ClassPath = Class(name="Ant_ClassPath")
Ant_Set = Class(name="Ant_Set", is_abstract=True)
Ant_PatternSet = Class(name="Ant_PatternSet")
Set = Class(name="Set")
Ant_FileSet = Class(name="Ant_FileSet")
Ant_FilterSet = Class(name="Ant_FilterSet")
Ant_MiscellaneousTask = Class(name="Ant_MiscellaneousTask", is_abstract=True)
PreDefinedTask = Class(name="PreDefinedTask")
Ant_Echo = Class(name="Ant_Echo")
MiscellaneousTask = Class(name="MiscellaneousTask")
Ant_Tstamp = Class(name="Ant_Tstamp")
Ant_FormatTstamp = Class(name="Ant_FormatTstamp")
Ant_NewTask = Class(name="Ant_NewTask")
Task = Class(name="Task")
Ant_Attribut = Class(name="Ant_Attribut")
Ant_PreDefinedTask = Class(name="Ant_PreDefinedTask", is_abstract=True)
Ant_Java = Class(name="Ant_Java")
ExecutionTask = Class(name="ExecutionTask")
Ant_ArchiveTask = Class(name="Ant_ArchiveTask", is_abstract=True)
Ant_Jar = Class(name="Ant_Jar")
ArchiveTask = Class(name="ArchiveTask")
Ant_FileTask = Class(name="Ant_FileTask", is_abstract=True)
Ant_Mkdir = Class(name="Ant_Mkdir")
FileTask = Class(name="FileTask")
Ant_CompileTask = Class(name="Ant_CompileTask", is_abstract=True)
Ant_Javac = Class(name="Ant_Javac")
CompileTask = Class(name="CompileTask")
Ant_DocumentationTask = Class(name="Ant_DocumentationTask", is_abstract=True)
Ant_Javadoc = Class(name="Ant_Javadoc")
DocumentationTask = Class(name="DocumentationTask")
Ant_Delete = Class(name="Ant_Delete")
Ant_Copy = Class(name="Ant_Copy")
Ant_ExecutionTask = Class(name="Ant_ExecutionTask", is_abstract=True)
Ant_Exec = Class(name="Ant_Exec")

# Ant_Project class attributes and methods
Ant_Project_name: Property = Property(name="name", type=StringType)
Ant_Project_basedir: Property = Property(name="basedir", type=StringType)
Ant_Project_description: Property = Property(name="description", type=StringType)
Ant_Project.attributes={Ant_Project_name, Ant_Project_basedir, Ant_Project_description}

# Ant_Target class attributes and methods
Ant_Target_name: Property = Property(name="name", type=StringType)
Ant_Target_description: Property = Property(name="description", type=StringType)
Ant_Target_unless: Property = Property(name="unless", type=StringType)
Ant_Target_ifCondition: Property = Property(name="ifCondition", type=StringType)
Ant_Target.attributes={Ant_Target_description, Ant_Target_ifCondition, Ant_Target_unless, Ant_Target_name}

# Ant_Path class attributes and methods
Ant_Path_id: Property = Property(name="id", type=StringType)
Ant_Path_refid: Property = Property(name="refid", type=StringType)
Ant_Path.attributes={Ant_Path_refid, Ant_Path_id}

# Ant_Property class attributes and methods

# Ant_TaskDef class attributes and methods
Ant_TaskDef_name: Property = Property(name="name", type=StringType)
Ant_TaskDef_classname: Property = Property(name="classname", type=StringType)
Ant_TaskDef.attributes={Ant_TaskDef_classname, Ant_TaskDef_name}

# Ant_PropertyName class attributes and methods
Ant_PropertyName_name: Property = Property(name="name", type=StringType)
Ant_PropertyName.attributes={Ant_PropertyName_name}

# Property class attributes and methods

# Ant_PropertyValue class attributes and methods
Ant_PropertyValue_value: Property = Property(name="value", type=StringType)
Ant_PropertyValue.attributes={Ant_PropertyValue_value}

# PropertyName class attributes and methods

# Ant_PropertyLocation class attributes and methods
Ant_PropertyLocation_location: Property = Property(name="location", type=StringType)
Ant_PropertyLocation.attributes={Ant_PropertyLocation_location}

# Ant_PropertyFile class attributes and methods
Ant_PropertyFile_file: Property = Property(name="file", type=StringType)
Ant_PropertyFile.attributes={Ant_PropertyFile_file}

# Ant_PropertyEnv class attributes and methods
Ant_PropertyEnv_environment: Property = Property(name="environment", type=StringType)
Ant_PropertyEnv.attributes={Ant_PropertyEnv_environment}

# InExcludes class attributes and methods

# Ant_Excludes class attributes and methods

# Ant_IncludesFile class attributes and methods

# Ant_ExcludesFile class attributes and methods

# Ant_FileList class attributes and methods
Ant_FileList_dir: Property = Property(name="dir", type=StringType)
Ant_FileList_files: Property = Property(name="files", type=StringType)
Ant_FileList.attributes={Ant_FileList_dir, Ant_FileList_files}

# Ant_Filter class attributes and methods
Ant_Filter_token: Property = Property(name="token", type=StringType)
Ant_Filter_value: Property = Property(name="value", type=StringType)
Ant_Filter.attributes={Ant_Filter_value, Ant_Filter_token}

# Ant_FiltersFile class attributes and methods
Ant_FiltersFile_file: Property = Property(name="file", type=StringType)
Ant_FiltersFile.attributes={Ant_FiltersFile_file}

# Ant_PathElement class attributes and methods
Ant_PathElement_path: Property = Property(name="path", type=StringType)
Ant_PathElement_location: Property = Property(name="location", type=StringType)
Ant_PathElement.attributes={Ant_PathElement_path, Ant_PathElement_location}

# Ant_Task class attributes and methods

# Ant_Pattern class attributes and methods

# Ant_Basic class attributes and methods

# Pattern class attributes and methods

# Ant_Mapper class attributes and methods
Ant_Mapper_type: Property = Property(name="type", type=StringType)
Ant_Mapper_classname: Property = Property(name="classname", type=StringType)
Ant_Mapper_classpath: Property = Property(name="classpath", type=StringType)
Ant_Mapper_classpathref: Property = Property(name="classpathref", type=StringType)
Ant_Mapper_from_: Property = Property(name="from_", type=StringType)
Ant_Mapper_to: Property = Property(name="to", type=StringType)
Ant_Mapper.attributes={Ant_Mapper_classname, Ant_Mapper_to, Ant_Mapper_from_, Ant_Mapper_type, Ant_Mapper_classpathref, Ant_Mapper_classpath}

# Basic class attributes and methods

# Ant_InExcludes class attributes and methods
Ant_InExcludes_name: Property = Property(name="name", type=StringType)
Ant_InExcludes_ifCondition: Property = Property(name="ifCondition", type=StringType)
Ant_InExcludes_unless: Property = Property(name="unless", type=StringType)
Ant_InExcludes.attributes={Ant_InExcludes_unless, Ant_InExcludes_name, Ant_InExcludes_ifCondition}

# Ant_Includes class attributes and methods

# Ant_ClassPath class attributes and methods
Ant_ClassPath_refid: Property = Property(name="refid", type=StringType)
Ant_ClassPath.attributes={Ant_ClassPath_refid}

# Ant_Set class attributes and methods

# Ant_PatternSet class attributes and methods

# Set class attributes and methods

# Ant_FileSet class attributes and methods
Ant_FileSet_dir: Property = Property(name="dir", type=StringType)
Ant_FileSet.attributes={Ant_FileSet_dir}

# Ant_FilterSet class attributes and methods
Ant_FilterSet_starttoken: Property = Property(name="starttoken", type=StringType)
Ant_FilterSet_endtoken: Property = Property(name="endtoken", type=StringType)
Ant_FilterSet.attributes={Ant_FilterSet_endtoken, Ant_FilterSet_starttoken}

# Ant_MiscellaneousTask class attributes and methods

# PreDefinedTask class attributes and methods

# Ant_Echo class attributes and methods
Ant_Echo_message: Property = Property(name="message", type=StringType)
Ant_Echo_file: Property = Property(name="file", type=StringType)
Ant_Echo_append: Property = Property(name="append", type=StringType)
Ant_Echo.attributes={Ant_Echo_append, Ant_Echo_message, Ant_Echo_file}

# MiscellaneousTask class attributes and methods

# Ant_Tstamp class attributes and methods

# Ant_FormatTstamp class attributes and methods
Ant_FormatTstamp_property: Property = Property(name="property", type=StringType)
Ant_FormatTstamp_pattern: Property = Property(name="pattern", type=StringType)
Ant_FormatTstamp_offset: Property = Property(name="offset", type=StringType)
Ant_FormatTstamp_unit: Property = Property(name="unit", type=StringType)
Ant_FormatTstamp_locale: Property = Property(name="locale", type=StringType)
Ant_FormatTstamp.attributes={Ant_FormatTstamp_property, Ant_FormatTstamp_offset, Ant_FormatTstamp_pattern, Ant_FormatTstamp_unit, Ant_FormatTstamp_locale}

# Ant_NewTask class attributes and methods

# Task class attributes and methods

# Ant_Attribut class attributes and methods
Ant_Attribut_name: Property = Property(name="name", type=StringType)
Ant_Attribut_value: Property = Property(name="value", type=StringType)
Ant_Attribut.attributes={Ant_Attribut_value, Ant_Attribut_name}

# Ant_PreDefinedTask class attributes and methods
Ant_PreDefinedTask_id: Property = Property(name="id", type=StringType)
Ant_PreDefinedTask_taskname: Property = Property(name="taskname", type=StringType)
Ant_PreDefinedTask_description: Property = Property(name="description", type=StringType)
Ant_PreDefinedTask.attributes={Ant_PreDefinedTask_id, Ant_PreDefinedTask_taskname, Ant_PreDefinedTask_description}

# Ant_Java class attributes and methods
Ant_Java_fork: Property = Property(name="fork", type=StringType)
Ant_Java_classname: Property = Property(name="classname", type=StringType)
Ant_Java_jar: Property = Property(name="jar", type=StringType)
Ant_Java.attributes={Ant_Java_classname, Ant_Java_jar, Ant_Java_fork}

# ExecutionTask class attributes and methods

# Ant_ArchiveTask class attributes and methods

# Ant_Jar class attributes and methods
Ant_Jar_jarfile: Property = Property(name="jarfile", type=StringType)
Ant_Jar_basedir: Property = Property(name="basedir", type=StringType)
Ant_Jar_compress: Property = Property(name="compress", type=StringType)
Ant_Jar_encoding: Property = Property(name="encoding", type=StringType)
Ant_Jar_manifest: Property = Property(name="manifest", type=StringType)
Ant_Jar.attributes={Ant_Jar_compress, Ant_Jar_manifest, Ant_Jar_encoding, Ant_Jar_jarfile, Ant_Jar_basedir}

# ArchiveTask class attributes and methods

# Ant_FileTask class attributes and methods

# Ant_Mkdir class attributes and methods
Ant_Mkdir_dir: Property = Property(name="dir", type=StringType)
Ant_Mkdir.attributes={Ant_Mkdir_dir}

# FileTask class attributes and methods

# Ant_CompileTask class attributes and methods

# Ant_Javac class attributes and methods
Ant_Javac_srcdir: Property = Property(name="srcdir", type=StringType)
Ant_Javac_destdir: Property = Property(name="destdir", type=StringType)
Ant_Javac_debug: Property = Property(name="debug", type=StringType)
Ant_Javac_fork: Property = Property(name="fork", type=StringType)
Ant_Javac_optimize: Property = Property(name="optimize", type=StringType)
Ant_Javac_deprecation: Property = Property(name="deprecation", type=StringType)
Ant_Javac.attributes={Ant_Javac_deprecation, Ant_Javac_fork, Ant_Javac_destdir, Ant_Javac_optimize, Ant_Javac_srcdir, Ant_Javac_debug}

# CompileTask class attributes and methods

# Ant_DocumentationTask class attributes and methods

# Ant_Javadoc class attributes and methods
Ant_Javadoc_version: Property = Property(name="version", type=StringType)
Ant_Javadoc_use: Property = Property(name="use", type=StringType)
Ant_Javadoc_windowtitle: Property = Property(name="windowtitle", type=StringType)
Ant_Javadoc_sourcepath: Property = Property(name="sourcepath", type=StringType)
Ant_Javadoc_destdir: Property = Property(name="destdir", type=StringType)
Ant_Javadoc_packagenames: Property = Property(name="packagenames", type=StringType)
Ant_Javadoc_defaultexcludes: Property = Property(name="defaultexcludes", type=StringType)
Ant_Javadoc_author: Property = Property(name="author", type=StringType)
Ant_Javadoc.attributes={Ant_Javadoc_defaultexcludes, Ant_Javadoc_packagenames, Ant_Javadoc_author, Ant_Javadoc_windowtitle, Ant_Javadoc_destdir, Ant_Javadoc_version, Ant_Javadoc_sourcepath, Ant_Javadoc_use}

# DocumentationTask class attributes and methods

# Ant_Delete class attributes and methods
Ant_Delete_file: Property = Property(name="file", type=StringType)
Ant_Delete_dir: Property = Property(name="dir", type=StringType)
Ant_Delete_verbose: Property = Property(name="verbose", type=StringType)
Ant_Delete_quiet: Property = Property(name="quiet", type=StringType)
Ant_Delete_failonerror: Property = Property(name="failonerror", type=StringType)
Ant_Delete_includeEmptyDirs: Property = Property(name="includeEmptyDirs", type=StringType)
Ant_Delete_includes: Property = Property(name="includes", type=StringType)
Ant_Delete_includesfile: Property = Property(name="includesfile", type=StringType)
Ant_Delete_excludes: Property = Property(name="excludes", type=StringType)
Ant_Delete_excludesfile: Property = Property(name="excludesfile", type=StringType)
Ant_Delete_defaultexcludes: Property = Property(name="defaultexcludes", type=StringType)
Ant_Delete.attributes={Ant_Delete_dir, Ant_Delete_defaultexcludes, Ant_Delete_includeEmptyDirs, Ant_Delete_verbose, Ant_Delete_failonerror, Ant_Delete_excludes, Ant_Delete_excludesfile, Ant_Delete_includes, Ant_Delete_quiet, Ant_Delete_includesfile, Ant_Delete_file}

# Ant_Copy class attributes and methods
Ant_Copy_file: Property = Property(name="file", type=StringType)
Ant_Copy_presservelastmodified: Property = Property(name="presservelastmodified", type=StringType)
Ant_Copy_tofile: Property = Property(name="tofile", type=StringType)
Ant_Copy_todir: Property = Property(name="todir", type=StringType)
Ant_Copy_overwrite: Property = Property(name="overwrite", type=StringType)
Ant_Copy_filtering: Property = Property(name="filtering", type=StringType)
Ant_Copy_flatten: Property = Property(name="flatten", type=StringType)
Ant_Copy_includeEmptyDirs: Property = Property(name="includeEmptyDirs", type=StringType)
Ant_Copy.attributes={Ant_Copy_flatten, Ant_Copy_presservelastmodified, Ant_Copy_overwrite, Ant_Copy_filtering, Ant_Copy_includeEmptyDirs, Ant_Copy_todir, Ant_Copy_file, Ant_Copy_tofile}

# Ant_ExecutionTask class attributes and methods

# Ant_Exec class attributes and methods
Ant_Exec_executable: Property = Property(name="executable", type=StringType)
Ant_Exec_dir: Property = Property(name="dir", type=StringType)
Ant_Exec.attributes={Ant_Exec_executable, Ant_Exec_dir}

# Relationships
targets7: BinaryAssociation = BinaryAssociation(
    name="targets7",
    ends={
        Property(name="Ant_Target9", type=Ant_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="Ant_Project8", type=Ant_Target, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
default0: BinaryAssociation = BinaryAssociation(
    name="default0",
    ends={
        Property(name="Ant_Target", type=Ant_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="Ant_Project", type=Ant_Target, multiplicity=Multiplicity(1, 1))
    }
)
path1: BinaryAssociation = BinaryAssociation(
    name="path1",
    ends={
        Property(name="Ant_Path", type=Ant_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="Ant_Project2", type=Ant_Path, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties3: BinaryAssociation = BinaryAssociation(
    name="properties3",
    ends={
        Property(name="Ant_Property", type=Ant_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="Ant_Project4", type=Ant_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
taskdef5: BinaryAssociation = BinaryAssociation(
    name="taskdef5",
    ends={
        Property(name="Ant_TaskDef", type=Ant_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="Ant_Project6", type=Ant_TaskDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
depends11: BinaryAssociation = BinaryAssociation(
    name="depends11",
    ends={
        Property(name="Ant_Target12", type=Ant_Target, multiplicity=Multiplicity(1, 1)),
        Property(name="Ant_Target10", type=Ant_Target, multiplicity=Multiplicity(0, 9999))
    }
)
tasks13: BinaryAssociation = BinaryAssociation(
    name="tasks13",
    ends={
        Property(name="Task", type=Ant_Target, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=Ant_Task, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
path25: BinaryAssociation = BinaryAssociation(
    name="path25",
    ends={
        Property(name="Ant_Path26", type=Ant_Path, multiplicity=Multiplicity(1, 1)),
        Property(name="Ant_Path24", type=Ant_Path, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pathElement27: BinaryAssociation = BinaryAssociation(
    name="pathElement27",
    ends={
        Property(name="Ant_PathElement", type=Ant_Path, multiplicity=Multiplicity(1, 1)),
        Property(name="Ant_Path28", type=Ant_PathElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fileset29: BinaryAssociation = BinaryAssociation(
    name="fileset29",
    ends={
        Property(name="Ant_FileSet31", type=Ant_Path, multiplicity=Multiplicity(1, 1)),
        Property(name="Ant_Path30", type=Ant_FileSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pathElement32: BinaryAssociation = BinaryAssociation(
    name="pathElement32",
    ends={
        Property(name="Ant_PathElement33", type=Ant_ClassPath, multiplicity=Multiplicity(1, 1)),
        Property(name="Ant_ClassPath", type=Ant_PathElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inexcludes14: BinaryAssociation = BinaryAssociation(
    name="inexcludes14",
    ends={
        Property(name="Ant_InExcludes", type=Ant_PatternSet, multiplicity=Multiplicity(1, 1)),
        Property(name="Ant_PatternSet", type=Ant_InExcludes, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
patternset15: BinaryAssociation = BinaryAssociation(
    name="patternset15",
    ends={
        Property(name="Ant_PatternSet16", type=Ant_FileSet, multiplicity=Multiplicity(1, 1)),
        Property(name="Ant_FileSet", type=Ant_PatternSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
include17: BinaryAssociation = BinaryAssociation(
    name="include17",
    ends={
        Property(name="Ant_Includes", type=Ant_FileSet, multiplicity=Multiplicity(1, 1)),
        Property(name="Ant_FileSet18", type=Ant_Includes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exclude19: BinaryAssociation = BinaryAssociation(
    name="exclude19",
    ends={
        Property(name="Ant_Excludes", type=Ant_FileSet, multiplicity=Multiplicity(1, 1)),
        Property(name="Ant_FileSet20", type=Ant_Excludes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
filter21: BinaryAssociation = BinaryAssociation(
    name="filter21",
    ends={
        Property(name="Ant_Filter", type=Ant_FilterSet, multiplicity=Multiplicity(1, 1)),
        Property(name="Ant_FilterSet", type=Ant_Filter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
filtersfile22: BinaryAssociation = BinaryAssociation(
    name="filtersfile22",
    ends={
        Property(name="Ant_FiltersFile", type=Ant_FilterSet, multiplicity=Multiplicity(1, 1)),
        Property(name="Ant_FilterSet23", type=Ant_FiltersFile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classPath42: BinaryAssociation = BinaryAssociation(
    name="classPath42",
    ends={
        Property(name="Ant_ClassPath43", type=Ant_Java, multiplicity=Multiplicity(1, 1)),
        Property(name="Ant_Java", type=Ant_ClassPath, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
format44: BinaryAssociation = BinaryAssociation(
    name="format44",
    ends={
        Property(name="Ant_FormatTstamp", type=Ant_Tstamp, multiplicity=Multiplicity(1, 1)),
        Property(name="Ant_Tstamp", type=Ant_FormatTstamp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fileset34: BinaryAssociation = BinaryAssociation(
    name="fileset34",
    ends={
        Property(name="Ant_FileSet36", type=Ant_ClassPath, multiplicity=Multiplicity(1, 1)),
        Property(name="Ant_ClassPath35", type=Ant_FileSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target37: BinaryAssociation = BinaryAssociation(
    name="target37",
    ends={
        Property(name="Target", type=Ant_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="tasks", type=Ant_Target, multiplicity=Multiplicity(1, 1))
    }
)
taskName38: BinaryAssociation = BinaryAssociation(
    name="taskName38",
    ends={
        Property(name="Ant_TaskDef39", type=Ant_NewTask, multiplicity=Multiplicity(1, 1)),
        Property(name="Ant_NewTask", type=Ant_TaskDef, multiplicity=Multiplicity(1, 1))
    }
)
attributes40: BinaryAssociation = BinaryAssociation(
    name="attributes40",
    ends={
        Property(name="Ant_Attribut", type=Ant_NewTask, multiplicity=Multiplicity(1, 1)),
        Property(name="Ant_NewTask41", type=Ant_Attribut, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inExcludes45: BinaryAssociation = BinaryAssociation(
    name="inExcludes45",
    ends={
        Property(name="Ant_InExcludes46", type=Ant_Javac, multiplicity=Multiplicity(1, 1)),
        Property(name="Ant_Javac", type=Ant_InExcludes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classPath47: BinaryAssociation = BinaryAssociation(
    name="classPath47",
    ends={
        Property(name="Ant_ClassPath49", type=Ant_Javac, multiplicity=Multiplicity(1, 1)),
        Property(name="Ant_Javac48", type=Ant_ClassPath, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fileset50: BinaryAssociation = BinaryAssociation(
    name="fileset50",
    ends={
        Property(name="Ant_FileSet51", type=Ant_Copy, multiplicity=Multiplicity(1, 1)),
        Property(name="Ant_Copy", type=Ant_FileSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
filterset52: BinaryAssociation = BinaryAssociation(
    name="filterset52",
    ends={
        Property(name="Ant_FilterSet54", type=Ant_Copy, multiplicity=Multiplicity(1, 1)),
        Property(name="Ant_Copy53", type=Ant_FilterSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mapper55: BinaryAssociation = BinaryAssociation(
    name="mapper55",
    ends={
        Property(name="Ant_Mapper", type=Ant_Copy, multiplicity=Multiplicity(1, 1)),
        Property(name="Ant_Copy56", type=Ant_Mapper, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_Ant_PropertyName_Property = Generalization(general=Property_, specific=Ant_PropertyName)
gen_Ant_PropertyValue_PropertyName = Generalization(general=PropertyName, specific=Ant_PropertyValue)
gen_Ant_PropertyLocation_PropertyName = Generalization(general=PropertyName, specific=Ant_PropertyLocation)
gen_Ant_PropertyFile_Property = Generalization(general=Property_, specific=Ant_PropertyFile)
gen_Ant_PropertyEnv_Property = Generalization(general=Property_, specific=Ant_PropertyEnv)
gen_Ant_Includes_InExcludes = Generalization(general=InExcludes, specific=Ant_Includes)
gen_Ant_Excludes_InExcludes = Generalization(general=InExcludes, specific=Ant_Excludes)
gen_Ant_IncludesFile_InExcludes = Generalization(general=InExcludes, specific=Ant_IncludesFile)
gen_Ant_ExcludesFile_InExcludes = Generalization(general=InExcludes, specific=Ant_ExcludesFile)
gen_Ant_FileList_Basic = Generalization(general=Basic, specific=Ant_FileList)
gen_Ant_Filter_Basic = Generalization(general=Basic, specific=Ant_Filter)
gen_Ant_FiltersFile_Basic = Generalization(general=Basic, specific=Ant_FiltersFile)
gen_Ant_PathElement_Basic = Generalization(general=Basic, specific=Ant_PathElement)
gen_Ant_Basic_Pattern = Generalization(general=Pattern, specific=Ant_Basic)
gen_Ant_Mapper_Basic = Generalization(general=Basic, specific=Ant_Mapper)
gen_Ant_InExcludes_Basic = Generalization(general=Basic, specific=Ant_InExcludes)
gen_Ant_Path_Set = Generalization(general=Set, specific=Ant_Path)
gen_Ant_ClassPath_Set = Generalization(general=Set, specific=Ant_ClassPath)
gen_Ant_Set_Pattern = Generalization(general=Pattern, specific=Ant_Set)
gen_Ant_PatternSet_Set = Generalization(general=Set, specific=Ant_PatternSet)
gen_Ant_FileSet_Set = Generalization(general=Set, specific=Ant_FileSet)
gen_Ant_FilterSet_Set = Generalization(general=Set, specific=Ant_FilterSet)
gen_Ant_MiscellaneousTask_PreDefinedTask = Generalization(general=PreDefinedTask, specific=Ant_MiscellaneousTask)
gen_Ant_Echo_MiscellaneousTask = Generalization(general=MiscellaneousTask, specific=Ant_Echo)
gen_Ant_Tstamp_MiscellaneousTask = Generalization(general=MiscellaneousTask, specific=Ant_Tstamp)
gen_Ant_NewTask_Task = Generalization(general=Task, specific=Ant_NewTask)
gen_Ant_PreDefinedTask_Task = Generalization(general=Task, specific=Ant_PreDefinedTask)
gen_Ant_Java_ExecutionTask = Generalization(general=ExecutionTask, specific=Ant_Java)
gen_Ant_ArchiveTask_PreDefinedTask = Generalization(general=PreDefinedTask, specific=Ant_ArchiveTask)
gen_Ant_Jar_ArchiveTask = Generalization(general=ArchiveTask, specific=Ant_Jar)
gen_Ant_FileTask_PreDefinedTask = Generalization(general=PreDefinedTask, specific=Ant_FileTask)
gen_Ant_Mkdir_FileTask = Generalization(general=FileTask, specific=Ant_Mkdir)
gen_Ant_CompileTask_PreDefinedTask = Generalization(general=PreDefinedTask, specific=Ant_CompileTask)
gen_Ant_Javac_CompileTask = Generalization(general=CompileTask, specific=Ant_Javac)
gen_Ant_DocumentationTask_PreDefinedTask = Generalization(general=PreDefinedTask, specific=Ant_DocumentationTask)
gen_Ant_Javadoc_DocumentationTask = Generalization(general=DocumentationTask, specific=Ant_Javadoc)
gen_Ant_Copy_FileTask = Generalization(general=FileTask, specific=Ant_Copy)
gen_Ant_Delete_FileTask = Generalization(general=FileTask, specific=Ant_Delete)
gen_Ant_ExecutionTask_PreDefinedTask = Generalization(general=PreDefinedTask, specific=Ant_ExecutionTask)
gen_Ant_Exec_ExecutionTask = Generalization(general=ExecutionTask, specific=Ant_Exec)

# Domain Model
domain_model = DomainModel(
    name="Ant",
    types={Ant_Project, Ant_Target, Ant_Path, Ant_Property, Ant_TaskDef, Ant_PropertyName, Property_, Ant_PropertyValue, PropertyName, Ant_PropertyLocation, Ant_PropertyFile, Ant_PropertyEnv, InExcludes, Ant_Excludes, Ant_IncludesFile, Ant_ExcludesFile, Ant_FileList, Ant_Filter, Ant_FiltersFile, Ant_PathElement, Ant_Task, Ant_Pattern, Ant_Basic, Pattern, Ant_Mapper, Basic, Ant_InExcludes, Ant_Includes, Ant_ClassPath, Ant_Set, Ant_PatternSet, Set, Ant_FileSet, Ant_FilterSet, Ant_MiscellaneousTask, PreDefinedTask, Ant_Echo, MiscellaneousTask, Ant_Tstamp, Ant_FormatTstamp, Ant_NewTask, Task, Ant_Attribut, Ant_PreDefinedTask, Ant_Java, ExecutionTask, Ant_ArchiveTask, Ant_Jar, ArchiveTask, Ant_FileTask, Ant_Mkdir, FileTask, Ant_CompileTask, Ant_Javac, CompileTask, Ant_DocumentationTask, Ant_Javadoc, DocumentationTask, Ant_Delete, Ant_Copy, Ant_ExecutionTask, Ant_Exec},
    associations={targets7, default0, path1, properties3, taskdef5, depends11, tasks13, path25, pathElement27, fileset29, pathElement32, inexcludes14, patternset15, include17, exclude19, filter21, filtersfile22, classPath42, format44, fileset34, target37, taskName38, attributes40, inExcludes45, classPath47, fileset50, filterset52, mapper55},
    generalizations={gen_Ant_PropertyName_Property, gen_Ant_PropertyValue_PropertyName, gen_Ant_PropertyLocation_PropertyName, gen_Ant_PropertyFile_Property, gen_Ant_PropertyEnv_Property, gen_Ant_Includes_InExcludes, gen_Ant_Excludes_InExcludes, gen_Ant_IncludesFile_InExcludes, gen_Ant_ExcludesFile_InExcludes, gen_Ant_FileList_Basic, gen_Ant_Filter_Basic, gen_Ant_FiltersFile_Basic, gen_Ant_PathElement_Basic, gen_Ant_Basic_Pattern, gen_Ant_Mapper_Basic, gen_Ant_InExcludes_Basic, gen_Ant_Path_Set, gen_Ant_ClassPath_Set, gen_Ant_Set_Pattern, gen_Ant_PatternSet_Set, gen_Ant_FileSet_Set, gen_Ant_FilterSet_Set, gen_Ant_MiscellaneousTask_PreDefinedTask, gen_Ant_Echo_MiscellaneousTask, gen_Ant_Tstamp_MiscellaneousTask, gen_Ant_NewTask_Task, gen_Ant_PreDefinedTask_Task, gen_Ant_Java_ExecutionTask, gen_Ant_ArchiveTask_PreDefinedTask, gen_Ant_Jar_ArchiveTask, gen_Ant_FileTask_PreDefinedTask, gen_Ant_Mkdir_FileTask, gen_Ant_CompileTask_PreDefinedTask, gen_Ant_Javac_CompileTask, gen_Ant_DocumentationTask_PreDefinedTask, gen_Ant_Javadoc_DocumentationTask, gen_Ant_Copy_FileTask, gen_Ant_Delete_FileTask, gen_Ant_ExecutionTask_PreDefinedTask, gen_Ant_Exec_ExecutionTask},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)