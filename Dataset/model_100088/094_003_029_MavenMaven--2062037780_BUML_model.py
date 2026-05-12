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
MavenMaven_AntTaskDef = Class(name="MavenMaven_AntTaskDef")
MavenMaven_PrePostGoal = Class(name="MavenMaven_PrePostGoal", is_abstract=True)
ContentsGoal = Class(name="ContentsGoal")
MavenMaven_AntPropertyName = Class(name="MavenMaven_AntPropertyName", is_abstract=True)
AntProperty = Class(name="AntProperty")
MavenMaven_AntPropertyValue = Class(name="MavenMaven_AntPropertyValue")
AntPropertyName = Class(name="AntPropertyName")
MavenMaven_Project = Class(name="MavenMaven_Project")
MavenMaven_Xmlns = Class(name="MavenMaven_Xmlns")
MavenMaven_Goal = Class(name="MavenMaven_Goal")
MavenMaven_Path = Class(name="MavenMaven_Path")
MavenMaven_AntProperty = Class(name="MavenMaven_AntProperty", is_abstract=True)
AbstractGoal = Class(name="AbstractGoal")
MavenMaven_PreGoal = Class(name="MavenMaven_PreGoal")
PrePostGoal = Class(name="PrePostGoal")
MavenMaven_PostGoal = Class(name="MavenMaven_PostGoal")
MavenMaven_Pattern = Class(name="MavenMaven_Pattern", is_abstract=True)
MavenMaven_AntPropertyLocation = Class(name="MavenMaven_AntPropertyLocation")
MavenMaven_AntPropertyFile = Class(name="MavenMaven_AntPropertyFile")
MavenMaven_AntPropertyEnv = Class(name="MavenMaven_AntPropertyEnv")
MavenMaven_JellyCommand = Class(name="MavenMaven_JellyCommand", is_abstract=True)
MavenMaven_JellySet = Class(name="MavenMaven_JellySet")
JellyCommand = Class(name="JellyCommand")
MavenMaven_AbstractGoal = Class(name="MavenMaven_AbstractGoal", is_abstract=True)
MavenMaven_ContentsGoal = Class(name="MavenMaven_ContentsGoal", is_abstract=True)
MavenMaven_AttainGoal = Class(name="MavenMaven_AttainGoal")
MavenMaven_FiltersFile = Class(name="MavenMaven_FiltersFile")
MavenMaven_PathElement = Class(name="MavenMaven_PathElement")
MavenMaven_Set = Class(name="MavenMaven_Set", is_abstract=True)
MavenMaven_PatternSet = Class(name="MavenMaven_PatternSet")
Set = Class(name="Set")
MavenMaven_FileSet = Class(name="MavenMaven_FileSet")
MavenMaven_Basic = Class(name="MavenMaven_Basic", is_abstract=True)
Pattern = Class(name="Pattern")
MavenMaven_Mapper = Class(name="MavenMaven_Mapper")
Basic = Class(name="Basic")
MavenMaven_InExcludes = Class(name="MavenMaven_InExcludes", is_abstract=True)
MavenMaven_Includes = Class(name="MavenMaven_Includes")
InExcludes = Class(name="InExcludes")
MavenMaven_Excludes = Class(name="MavenMaven_Excludes")
MavenMaven_IncludesFile = Class(name="MavenMaven_IncludesFile")
MavenMaven_ExcludesFile = Class(name="MavenMaven_ExcludesFile")
MavenMaven_FileList = Class(name="MavenMaven_FileList")
MavenMaven_Filter = Class(name="MavenMaven_Filter")
MavenMaven_ClassPath = Class(name="MavenMaven_ClassPath")
MavenMaven_Task = Class(name="MavenMaven_Task", is_abstract=True)
MavenMaven_NewTask = Class(name="MavenMaven_NewTask")
Task = Class(name="Task")
MavenMaven_FilterSet = Class(name="MavenMaven_FilterSet")
MavenMaven_MiscellaneousTask = Class(name="MavenMaven_MiscellaneousTask", is_abstract=True)
MavenMaven_Echo = Class(name="MavenMaven_Echo")
MiscellaneousTask = Class(name="MiscellaneousTask")
MavenMaven_Tstamp = Class(name="MavenMaven_Tstamp")
MavenMaven_FormatTstamp = Class(name="MavenMaven_FormatTstamp")
MavenMaven_CompileTask = Class(name="MavenMaven_CompileTask", is_abstract=True)
MavenMaven_Attribut = Class(name="MavenMaven_Attribut")
MavenMaven_PreDefinedTask = Class(name="MavenMaven_PreDefinedTask", is_abstract=True)
MavenMaven_ExecutionTask = Class(name="MavenMaven_ExecutionTask", is_abstract=True)
PreDefinedTask = Class(name="PreDefinedTask")
MavenMaven_Exec = Class(name="MavenMaven_Exec")
ExecutionTask = Class(name="ExecutionTask")
MavenMaven_Java = Class(name="MavenMaven_Java")
MavenMaven_ArchiveTask = Class(name="MavenMaven_ArchiveTask", is_abstract=True)
MavenMaven_Jar = Class(name="MavenMaven_Jar")
ArchiveTask = Class(name="ArchiveTask")
MavenMaven_FileTask = Class(name="MavenMaven_FileTask", is_abstract=True)
MavenMaven_Mkdir = Class(name="MavenMaven_Mkdir")
FileTask = Class(name="FileTask")
MavenMaven_Copy = Class(name="MavenMaven_Copy")
MavenMaven_Javac = Class(name="MavenMaven_Javac")
CompileTask = Class(name="CompileTask")
MavenMaven_DocumentationTask = Class(name="MavenMaven_DocumentationTask", is_abstract=True)
MavenMaven_Javadoc = Class(name="MavenMaven_Javadoc")
DocumentationTask = Class(name="DocumentationTask")
MavenMaven_Delete = Class(name="MavenMaven_Delete")

# MavenMaven_AntTaskDef class attributes and methods
MavenMaven_AntTaskDef_name: Property = Property(name="name", type=StringType)
MavenMaven_AntTaskDef_classname: Property = Property(name="classname", type=StringType)
MavenMaven_AntTaskDef.attributes={MavenMaven_AntTaskDef_name, MavenMaven_AntTaskDef_classname}

# MavenMaven_PrePostGoal class attributes and methods

# ContentsGoal class attributes and methods

# MavenMaven_AntPropertyName class attributes and methods
MavenMaven_AntPropertyName_name: Property = Property(name="name", type=StringType)
MavenMaven_AntPropertyName.attributes={MavenMaven_AntPropertyName_name}

# AntProperty class attributes and methods

# MavenMaven_AntPropertyValue class attributes and methods
MavenMaven_AntPropertyValue_value: Property = Property(name="value", type=StringType)
MavenMaven_AntPropertyValue.attributes={MavenMaven_AntPropertyValue_value}

# AntPropertyName class attributes and methods

# MavenMaven_Project class attributes and methods

# MavenMaven_Xmlns class attributes and methods
MavenMaven_Xmlns_name: Property = Property(name="name", type=StringType)
MavenMaven_Xmlns_value: Property = Property(name="value", type=StringType)
MavenMaven_Xmlns.attributes={MavenMaven_Xmlns_value, MavenMaven_Xmlns_name}

# MavenMaven_Goal class attributes and methods
MavenMaven_Goal_name: Property = Property(name="name", type=StringType)
MavenMaven_Goal.attributes={MavenMaven_Goal_name}

# MavenMaven_Path class attributes and methods
MavenMaven_Path_id: Property = Property(name="id", type=StringType)
MavenMaven_Path_refid: Property = Property(name="refid", type=StringType)
MavenMaven_Path.attributes={MavenMaven_Path_refid, MavenMaven_Path_id}

# MavenMaven_AntProperty class attributes and methods

# AbstractGoal class attributes and methods

# MavenMaven_PreGoal class attributes and methods

# PrePostGoal class attributes and methods

# MavenMaven_PostGoal class attributes and methods

# MavenMaven_Pattern class attributes and methods

# MavenMaven_AntPropertyLocation class attributes and methods
MavenMaven_AntPropertyLocation_location: Property = Property(name="location", type=StringType)
MavenMaven_AntPropertyLocation.attributes={MavenMaven_AntPropertyLocation_location}

# MavenMaven_AntPropertyFile class attributes and methods
MavenMaven_AntPropertyFile_file: Property = Property(name="file", type=StringType)
MavenMaven_AntPropertyFile.attributes={MavenMaven_AntPropertyFile_file}

# MavenMaven_AntPropertyEnv class attributes and methods
MavenMaven_AntPropertyEnv_environment: Property = Property(name="environment", type=StringType)
MavenMaven_AntPropertyEnv.attributes={MavenMaven_AntPropertyEnv_environment}

# MavenMaven_JellyCommand class attributes and methods

# MavenMaven_JellySet class attributes and methods
MavenMaven_JellySet_var: Property = Property(name="var", type=StringType)
MavenMaven_JellySet_value: Property = Property(name="value", type=StringType)
MavenMaven_JellySet.attributes={MavenMaven_JellySet_var, MavenMaven_JellySet_value}

# JellyCommand class attributes and methods

# MavenMaven_AbstractGoal class attributes and methods

# MavenMaven_ContentsGoal class attributes and methods

# MavenMaven_AttainGoal class attributes and methods

# MavenMaven_FiltersFile class attributes and methods
MavenMaven_FiltersFile_file: Property = Property(name="file", type=StringType)
MavenMaven_FiltersFile.attributes={MavenMaven_FiltersFile_file}

# MavenMaven_PathElement class attributes and methods
MavenMaven_PathElement_path: Property = Property(name="path", type=StringType)
MavenMaven_PathElement_location: Property = Property(name="location", type=StringType)
MavenMaven_PathElement.attributes={MavenMaven_PathElement_location, MavenMaven_PathElement_path}

# MavenMaven_Set class attributes and methods

# MavenMaven_PatternSet class attributes and methods

# Set class attributes and methods

# MavenMaven_FileSet class attributes and methods
MavenMaven_FileSet_dir: Property = Property(name="dir", type=StringType)
MavenMaven_FileSet.attributes={MavenMaven_FileSet_dir}

# MavenMaven_Basic class attributes and methods

# Pattern class attributes and methods

# MavenMaven_Mapper class attributes and methods
MavenMaven_Mapper_type: Property = Property(name="type", type=StringType)
MavenMaven_Mapper_classname: Property = Property(name="classname", type=StringType)
MavenMaven_Mapper_classpath: Property = Property(name="classpath", type=StringType)
MavenMaven_Mapper_classpathref: Property = Property(name="classpathref", type=StringType)
MavenMaven_Mapper_from_: Property = Property(name="from_", type=StringType)
MavenMaven_Mapper_to: Property = Property(name="to", type=StringType)
MavenMaven_Mapper.attributes={MavenMaven_Mapper_classname, MavenMaven_Mapper_classpath, MavenMaven_Mapper_from_, MavenMaven_Mapper_to, MavenMaven_Mapper_classpathref, MavenMaven_Mapper_type}

# Basic class attributes and methods

# MavenMaven_InExcludes class attributes and methods
MavenMaven_InExcludes_name: Property = Property(name="name", type=StringType)
MavenMaven_InExcludes_ifCondition: Property = Property(name="ifCondition", type=StringType)
MavenMaven_InExcludes_unless: Property = Property(name="unless", type=StringType)
MavenMaven_InExcludes.attributes={MavenMaven_InExcludes_name, MavenMaven_InExcludes_ifCondition, MavenMaven_InExcludes_unless}

# MavenMaven_Includes class attributes and methods

# InExcludes class attributes and methods

# MavenMaven_Excludes class attributes and methods

# MavenMaven_IncludesFile class attributes and methods

# MavenMaven_ExcludesFile class attributes and methods

# MavenMaven_FileList class attributes and methods
MavenMaven_FileList_dir: Property = Property(name="dir", type=StringType)
MavenMaven_FileList_files: Property = Property(name="files", type=StringType)
MavenMaven_FileList.attributes={MavenMaven_FileList_dir, MavenMaven_FileList_files}

# MavenMaven_Filter class attributes and methods
MavenMaven_Filter_token: Property = Property(name="token", type=StringType)
MavenMaven_Filter_value: Property = Property(name="value", type=StringType)
MavenMaven_Filter.attributes={MavenMaven_Filter_value, MavenMaven_Filter_token}

# MavenMaven_ClassPath class attributes and methods
MavenMaven_ClassPath_refid: Property = Property(name="refid", type=StringType)
MavenMaven_ClassPath.attributes={MavenMaven_ClassPath_refid}

# MavenMaven_Task class attributes and methods

# MavenMaven_NewTask class attributes and methods

# Task class attributes and methods

# MavenMaven_FilterSet class attributes and methods
MavenMaven_FilterSet_starttoken: Property = Property(name="starttoken", type=StringType)
MavenMaven_FilterSet_endtoken: Property = Property(name="endtoken", type=StringType)
MavenMaven_FilterSet.attributes={MavenMaven_FilterSet_endtoken, MavenMaven_FilterSet_starttoken}

# MavenMaven_MiscellaneousTask class attributes and methods

# MavenMaven_Echo class attributes and methods
MavenMaven_Echo_message: Property = Property(name="message", type=StringType)
MavenMaven_Echo_file: Property = Property(name="file", type=StringType)
MavenMaven_Echo_append: Property = Property(name="append", type=StringType)
MavenMaven_Echo.attributes={MavenMaven_Echo_message, MavenMaven_Echo_file, MavenMaven_Echo_append}

# MiscellaneousTask class attributes and methods

# MavenMaven_Tstamp class attributes and methods

# MavenMaven_FormatTstamp class attributes and methods
MavenMaven_FormatTstamp_property: Property = Property(name="property", type=StringType)
MavenMaven_FormatTstamp_pattern: Property = Property(name="pattern", type=StringType)
MavenMaven_FormatTstamp_offset: Property = Property(name="offset", type=StringType)
MavenMaven_FormatTstamp_unit: Property = Property(name="unit", type=StringType)
MavenMaven_FormatTstamp_locale: Property = Property(name="locale", type=StringType)
MavenMaven_FormatTstamp.attributes={MavenMaven_FormatTstamp_pattern, MavenMaven_FormatTstamp_locale, MavenMaven_FormatTstamp_offset, MavenMaven_FormatTstamp_property, MavenMaven_FormatTstamp_unit}

# MavenMaven_CompileTask class attributes and methods

# MavenMaven_Attribut class attributes and methods
MavenMaven_Attribut_name: Property = Property(name="name", type=StringType)
MavenMaven_Attribut_value: Property = Property(name="value", type=StringType)
MavenMaven_Attribut.attributes={MavenMaven_Attribut_name, MavenMaven_Attribut_value}

# MavenMaven_PreDefinedTask class attributes and methods
MavenMaven_PreDefinedTask_id: Property = Property(name="id", type=StringType)
MavenMaven_PreDefinedTask_taskname: Property = Property(name="taskname", type=StringType)
MavenMaven_PreDefinedTask_description: Property = Property(name="description", type=StringType)
MavenMaven_PreDefinedTask.attributes={MavenMaven_PreDefinedTask_id, MavenMaven_PreDefinedTask_description, MavenMaven_PreDefinedTask_taskname}

# MavenMaven_ExecutionTask class attributes and methods

# PreDefinedTask class attributes and methods

# MavenMaven_Exec class attributes and methods
MavenMaven_Exec_executable: Property = Property(name="executable", type=StringType)
MavenMaven_Exec_dir: Property = Property(name="dir", type=StringType)
MavenMaven_Exec.attributes={MavenMaven_Exec_executable, MavenMaven_Exec_dir}

# ExecutionTask class attributes and methods

# MavenMaven_Java class attributes and methods
MavenMaven_Java_classname: Property = Property(name="classname", type=StringType)
MavenMaven_Java_jar: Property = Property(name="jar", type=StringType)
MavenMaven_Java_fork: Property = Property(name="fork", type=StringType)
MavenMaven_Java.attributes={MavenMaven_Java_jar, MavenMaven_Java_fork, MavenMaven_Java_classname}

# MavenMaven_ArchiveTask class attributes and methods

# MavenMaven_Jar class attributes and methods
MavenMaven_Jar_jarfile: Property = Property(name="jarfile", type=StringType)
MavenMaven_Jar_basedir: Property = Property(name="basedir", type=StringType)
MavenMaven_Jar_compress: Property = Property(name="compress", type=StringType)
MavenMaven_Jar_encoding: Property = Property(name="encoding", type=StringType)
MavenMaven_Jar_manifest: Property = Property(name="manifest", type=StringType)
MavenMaven_Jar.attributes={MavenMaven_Jar_manifest, MavenMaven_Jar_basedir, MavenMaven_Jar_jarfile, MavenMaven_Jar_encoding, MavenMaven_Jar_compress}

# ArchiveTask class attributes and methods

# MavenMaven_FileTask class attributes and methods

# MavenMaven_Mkdir class attributes and methods
MavenMaven_Mkdir_dir: Property = Property(name="dir", type=StringType)
MavenMaven_Mkdir.attributes={MavenMaven_Mkdir_dir}

# FileTask class attributes and methods

# MavenMaven_Copy class attributes and methods
MavenMaven_Copy_file: Property = Property(name="file", type=StringType)
MavenMaven_Copy_presservelastmodified: Property = Property(name="presservelastmodified", type=StringType)
MavenMaven_Copy_tofile: Property = Property(name="tofile", type=StringType)
MavenMaven_Copy_todir: Property = Property(name="todir", type=StringType)
MavenMaven_Copy_overwrite: Property = Property(name="overwrite", type=StringType)
MavenMaven_Copy_filtering: Property = Property(name="filtering", type=StringType)
MavenMaven_Copy_flatten: Property = Property(name="flatten", type=StringType)
MavenMaven_Copy_includeEmptyDirs: Property = Property(name="includeEmptyDirs", type=StringType)
MavenMaven_Copy.attributes={MavenMaven_Copy_todir, MavenMaven_Copy_flatten, MavenMaven_Copy_filtering, MavenMaven_Copy_tofile, MavenMaven_Copy_overwrite, MavenMaven_Copy_file, MavenMaven_Copy_includeEmptyDirs, MavenMaven_Copy_presservelastmodified}

# MavenMaven_Javac class attributes and methods
MavenMaven_Javac_srcdir: Property = Property(name="srcdir", type=StringType)
MavenMaven_Javac_destdir: Property = Property(name="destdir", type=StringType)
MavenMaven_Javac_debug: Property = Property(name="debug", type=StringType)
MavenMaven_Javac_fork: Property = Property(name="fork", type=StringType)
MavenMaven_Javac_optimize: Property = Property(name="optimize", type=StringType)
MavenMaven_Javac_deprecation: Property = Property(name="deprecation", type=StringType)
MavenMaven_Javac.attributes={MavenMaven_Javac_deprecation, MavenMaven_Javac_optimize, MavenMaven_Javac_srcdir, MavenMaven_Javac_destdir, MavenMaven_Javac_fork, MavenMaven_Javac_debug}

# CompileTask class attributes and methods

# MavenMaven_DocumentationTask class attributes and methods

# MavenMaven_Javadoc class attributes and methods
MavenMaven_Javadoc_sourcepath: Property = Property(name="sourcepath", type=StringType)
MavenMaven_Javadoc_destdir: Property = Property(name="destdir", type=StringType)
MavenMaven_Javadoc_packagenames: Property = Property(name="packagenames", type=StringType)
MavenMaven_Javadoc_defaultexcludes: Property = Property(name="defaultexcludes", type=StringType)
MavenMaven_Javadoc_author: Property = Property(name="author", type=StringType)
MavenMaven_Javadoc_version: Property = Property(name="version", type=StringType)
MavenMaven_Javadoc_use: Property = Property(name="use", type=StringType)
MavenMaven_Javadoc_windowtitle: Property = Property(name="windowtitle", type=StringType)
MavenMaven_Javadoc.attributes={MavenMaven_Javadoc_packagenames, MavenMaven_Javadoc_destdir, MavenMaven_Javadoc_author, MavenMaven_Javadoc_version, MavenMaven_Javadoc_use, MavenMaven_Javadoc_windowtitle, MavenMaven_Javadoc_sourcepath, MavenMaven_Javadoc_defaultexcludes}

# DocumentationTask class attributes and methods

# MavenMaven_Delete class attributes and methods
MavenMaven_Delete_defaultexcludes: Property = Property(name="defaultexcludes", type=StringType)
MavenMaven_Delete_file: Property = Property(name="file", type=StringType)
MavenMaven_Delete_dir: Property = Property(name="dir", type=StringType)
MavenMaven_Delete_verbose: Property = Property(name="verbose", type=StringType)
MavenMaven_Delete_quiet: Property = Property(name="quiet", type=StringType)
MavenMaven_Delete_failonerror: Property = Property(name="failonerror", type=StringType)
MavenMaven_Delete_includeEmptyDirs: Property = Property(name="includeEmptyDirs", type=StringType)
MavenMaven_Delete_includes: Property = Property(name="includes", type=StringType)
MavenMaven_Delete_includesfile: Property = Property(name="includesfile", type=StringType)
MavenMaven_Delete_excludes: Property = Property(name="excludes", type=StringType)
MavenMaven_Delete_excludesfile: Property = Property(name="excludesfile", type=StringType)
MavenMaven_Delete.attributes={MavenMaven_Delete_failonerror, MavenMaven_Delete_dir, MavenMaven_Delete_file, MavenMaven_Delete_quiet, MavenMaven_Delete_includesfile, MavenMaven_Delete_verbose, MavenMaven_Delete_defaultexcludes, MavenMaven_Delete_includeEmptyDirs, MavenMaven_Delete_excludes, MavenMaven_Delete_includes, MavenMaven_Delete_excludesfile}

# Relationships
taskdefs7: BinaryAssociation = BinaryAssociation(
    name="taskdefs7",
    ends={
        Property(name="MavenMaven_AntTaskDef", type=MavenMaven_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="MavenMaven_Project8", type=MavenMaven_AntTaskDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
prePostGoals9: BinaryAssociation = BinaryAssociation(
    name="prePostGoals9",
    ends={
        Property(name="MavenMaven_PrePostGoal", type=MavenMaven_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="MavenMaven_Project10", type=MavenMaven_PrePostGoal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
goals11: BinaryAssociation = BinaryAssociation(
    name="goals11",
    ends={
        Property(name="MavenMaven_Goal13", type=MavenMaven_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="MavenMaven_Project12", type=MavenMaven_Goal, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
xmlns0: BinaryAssociation = BinaryAssociation(
    name="xmlns0",
    ends={
        Property(name="MavenMaven_Xmlns", type=MavenMaven_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="MavenMaven_Project", type=MavenMaven_Xmlns, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
default1: BinaryAssociation = BinaryAssociation(
    name="default1",
    ends={
        Property(name="MavenMaven_Goal", type=MavenMaven_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="MavenMaven_Project2", type=MavenMaven_Goal, multiplicity=Multiplicity(0, 1))
    }
)
path3: BinaryAssociation = BinaryAssociation(
    name="path3",
    ends={
        Property(name="MavenMaven_Path", type=MavenMaven_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="MavenMaven_Project4", type=MavenMaven_Path, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties5: BinaryAssociation = BinaryAssociation(
    name="properties5",
    ends={
        Property(name="MavenMaven_AntProperty", type=MavenMaven_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="MavenMaven_Project6", type=MavenMaven_AntProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
centralGoal17: BinaryAssociation = BinaryAssociation(
    name="centralGoal17",
    ends={
        Property(name="Goal", type=MavenMaven_PreGoal, multiplicity=Multiplicity(1, 1)),
        Property(name="preGoal", type=MavenMaven_Goal, multiplicity=Multiplicity(1, 1))
    }
)
centralGoal18: BinaryAssociation = BinaryAssociation(
    name="centralGoal18",
    ends={
        Property(name="Goal19", type=MavenMaven_PostGoal, multiplicity=Multiplicity(1, 1)),
        Property(name="postGoal", type=MavenMaven_Goal, multiplicity=Multiplicity(1, 1))
    }
)
preGoal20: BinaryAssociation = BinaryAssociation(
    name="preGoal20",
    ends={
        Property(name="PreGoal", type=MavenMaven_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="centralGoal", type=MavenMaven_PreGoal, multiplicity=Multiplicity(0, 1))
    }
)
postGoal21: BinaryAssociation = BinaryAssociation(
    name="postGoal21",
    ends={
        Property(name="PostGoal", type=MavenMaven_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="centralGoal22", type=MavenMaven_PostGoal, multiplicity=Multiplicity(0, 1))
    }
)
contentsGoal14: BinaryAssociation = BinaryAssociation(
    name="contentsGoal14",
    ends={
        Property(name="MavenMaven_ContentsGoal", type=MavenMaven_AbstractGoal, multiplicity=Multiplicity(1, 1)),
        Property(name="MavenMaven_AbstractGoal", type=MavenMaven_ContentsGoal, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
attainGoal15: BinaryAssociation = BinaryAssociation(
    name="attainGoal15",
    ends={
        Property(name="MavenMaven_Goal16", type=MavenMaven_AttainGoal, multiplicity=Multiplicity(1, 1)),
        Property(name="MavenMaven_AttainGoal", type=MavenMaven_Goal, multiplicity=Multiplicity(1, 1))
    }
)
inexcludes23: BinaryAssociation = BinaryAssociation(
    name="inexcludes23",
    ends={
        Property(name="MavenMaven_InExcludes", type=MavenMaven_PatternSet, multiplicity=Multiplicity(1, 1)),
        Property(name="MavenMaven_PatternSet", type=MavenMaven_InExcludes, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
patternset24: BinaryAssociation = BinaryAssociation(
    name="patternset24",
    ends={
        Property(name="MavenMaven_PatternSet25", type=MavenMaven_FileSet, multiplicity=Multiplicity(1, 1)),
        Property(name="MavenMaven_FileSet", type=MavenMaven_PatternSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
include26: BinaryAssociation = BinaryAssociation(
    name="include26",
    ends={
        Property(name="MavenMaven_Includes", type=MavenMaven_FileSet, multiplicity=Multiplicity(1, 1)),
        Property(name="MavenMaven_FileSet27", type=MavenMaven_Includes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exclude28: BinaryAssociation = BinaryAssociation(
    name="exclude28",
    ends={
        Property(name="MavenMaven_Excludes", type=MavenMaven_FileSet, multiplicity=Multiplicity(1, 1)),
        Property(name="MavenMaven_FileSet29", type=MavenMaven_Excludes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fileset38: BinaryAssociation = BinaryAssociation(
    name="fileset38",
    ends={
        Property(name="MavenMaven_FileSet40", type=MavenMaven_Path, multiplicity=Multiplicity(1, 1)),
        Property(name="MavenMaven_Path39", type=MavenMaven_FileSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pathElement41: BinaryAssociation = BinaryAssociation(
    name="pathElement41",
    ends={
        Property(name="MavenMaven_PathElement42", type=MavenMaven_ClassPath, multiplicity=Multiplicity(1, 1)),
        Property(name="MavenMaven_ClassPath", type=MavenMaven_PathElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fileset43: BinaryAssociation = BinaryAssociation(
    name="fileset43",
    ends={
        Property(name="MavenMaven_FileSet45", type=MavenMaven_ClassPath, multiplicity=Multiplicity(1, 1)),
        Property(name="MavenMaven_ClassPath44", type=MavenMaven_FileSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
filter30: BinaryAssociation = BinaryAssociation(
    name="filter30",
    ends={
        Property(name="MavenMaven_Filter", type=MavenMaven_FilterSet, multiplicity=Multiplicity(1, 1)),
        Property(name="MavenMaven_FilterSet", type=MavenMaven_Filter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
filtersfile31: BinaryAssociation = BinaryAssociation(
    name="filtersfile31",
    ends={
        Property(name="MavenMaven_FiltersFile", type=MavenMaven_FilterSet, multiplicity=Multiplicity(1, 1)),
        Property(name="MavenMaven_FilterSet32", type=MavenMaven_FiltersFile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
path34: BinaryAssociation = BinaryAssociation(
    name="path34",
    ends={
        Property(name="MavenMaven_Path35", type=MavenMaven_Path, multiplicity=Multiplicity(1, 1)),
        Property(name="MavenMaven_Path33", type=MavenMaven_Path, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pathElement36: BinaryAssociation = BinaryAssociation(
    name="pathElement36",
    ends={
        Property(name="MavenMaven_PathElement", type=MavenMaven_Path, multiplicity=Multiplicity(1, 1)),
        Property(name="MavenMaven_Path37", type=MavenMaven_PathElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
format52: BinaryAssociation = BinaryAssociation(
    name="format52",
    ends={
        Property(name="MavenMaven_FormatTstamp", type=MavenMaven_Tstamp, multiplicity=Multiplicity(1, 1)),
        Property(name="MavenMaven_Tstamp", type=MavenMaven_FormatTstamp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
taskName46: BinaryAssociation = BinaryAssociation(
    name="taskName46",
    ends={
        Property(name="MavenMaven_AntTaskDef47", type=MavenMaven_NewTask, multiplicity=Multiplicity(1, 1)),
        Property(name="MavenMaven_NewTask", type=MavenMaven_AntTaskDef, multiplicity=Multiplicity(1, 1))
    }
)
attributes48: BinaryAssociation = BinaryAssociation(
    name="attributes48",
    ends={
        Property(name="MavenMaven_Attribut", type=MavenMaven_NewTask, multiplicity=Multiplicity(1, 1)),
        Property(name="MavenMaven_NewTask49", type=MavenMaven_Attribut, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classPath50: BinaryAssociation = BinaryAssociation(
    name="classPath50",
    ends={
        Property(name="MavenMaven_ClassPath51", type=MavenMaven_Java, multiplicity=Multiplicity(1, 1)),
        Property(name="MavenMaven_Java", type=MavenMaven_ClassPath, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inExcludes53: BinaryAssociation = BinaryAssociation(
    name="inExcludes53",
    ends={
        Property(name="MavenMaven_InExcludes54", type=MavenMaven_Javac, multiplicity=Multiplicity(1, 1)),
        Property(name="MavenMaven_Javac", type=MavenMaven_InExcludes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classPath55: BinaryAssociation = BinaryAssociation(
    name="classPath55",
    ends={
        Property(name="MavenMaven_ClassPath57", type=MavenMaven_Javac, multiplicity=Multiplicity(1, 1)),
        Property(name="MavenMaven_Javac56", type=MavenMaven_ClassPath, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fileset58: BinaryAssociation = BinaryAssociation(
    name="fileset58",
    ends={
        Property(name="MavenMaven_FileSet59", type=MavenMaven_Copy, multiplicity=Multiplicity(1, 1)),
        Property(name="MavenMaven_Copy", type=MavenMaven_FileSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
filterset60: BinaryAssociation = BinaryAssociation(
    name="filterset60",
    ends={
        Property(name="MavenMaven_FilterSet62", type=MavenMaven_Copy, multiplicity=Multiplicity(1, 1)),
        Property(name="MavenMaven_Copy61", type=MavenMaven_FilterSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mapper63: BinaryAssociation = BinaryAssociation(
    name="mapper63",
    ends={
        Property(name="MavenMaven_Mapper", type=MavenMaven_Copy, multiplicity=Multiplicity(1, 1)),
        Property(name="MavenMaven_Copy64", type=MavenMaven_Mapper, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_MavenMaven_AntProperty_ContentsGoal = Generalization(general=ContentsGoal, specific=MavenMaven_AntProperty)
gen_MavenMaven_AntPropertyName_AntProperty = Generalization(general=AntProperty, specific=MavenMaven_AntPropertyName)
gen_MavenMaven_AntPropertyValue_AntPropertyName = Generalization(general=AntPropertyName, specific=MavenMaven_AntPropertyValue)
gen_MavenMaven_PrePostGoal_AbstractGoal = Generalization(general=AbstractGoal, specific=MavenMaven_PrePostGoal)
gen_MavenMaven_PreGoal_PrePostGoal = Generalization(general=PrePostGoal, specific=MavenMaven_PreGoal)
gen_MavenMaven_PostGoal_PrePostGoal = Generalization(general=PrePostGoal, specific=MavenMaven_PostGoal)
gen_MavenMaven_Goal_AbstractGoal = Generalization(general=AbstractGoal, specific=MavenMaven_Goal)
gen_MavenMaven_AntPropertyLocation_AntPropertyName = Generalization(general=AntPropertyName, specific=MavenMaven_AntPropertyLocation)
gen_MavenMaven_AntPropertyFile_AntProperty = Generalization(general=AntProperty, specific=MavenMaven_AntPropertyFile)
gen_MavenMaven_AntPropertyEnv_AntProperty = Generalization(general=AntProperty, specific=MavenMaven_AntPropertyEnv)
gen_MavenMaven_JellyCommand_ContentsGoal = Generalization(general=ContentsGoal, specific=MavenMaven_JellyCommand)
gen_MavenMaven_JellySet_JellyCommand = Generalization(general=JellyCommand, specific=MavenMaven_JellySet)
gen_MavenMaven_AttainGoal_ContentsGoal = Generalization(general=ContentsGoal, specific=MavenMaven_AttainGoal)
gen_MavenMaven_FiltersFile_Basic = Generalization(general=Basic, specific=MavenMaven_FiltersFile)
gen_MavenMaven_PathElement_Basic = Generalization(general=Basic, specific=MavenMaven_PathElement)
gen_MavenMaven_Set_Pattern = Generalization(general=Pattern, specific=MavenMaven_Set)
gen_MavenMaven_PatternSet_Set = Generalization(general=Set, specific=MavenMaven_PatternSet)
gen_MavenMaven_FileSet_Set = Generalization(general=Set, specific=MavenMaven_FileSet)
gen_MavenMaven_Basic_Pattern = Generalization(general=Pattern, specific=MavenMaven_Basic)
gen_MavenMaven_Mapper_Basic = Generalization(general=Basic, specific=MavenMaven_Mapper)
gen_MavenMaven_InExcludes_Basic = Generalization(general=Basic, specific=MavenMaven_InExcludes)
gen_MavenMaven_Includes_InExcludes = Generalization(general=InExcludes, specific=MavenMaven_Includes)
gen_MavenMaven_Excludes_InExcludes = Generalization(general=InExcludes, specific=MavenMaven_Excludes)
gen_MavenMaven_IncludesFile_InExcludes = Generalization(general=InExcludes, specific=MavenMaven_IncludesFile)
gen_MavenMaven_ExcludesFile_InExcludes = Generalization(general=InExcludes, specific=MavenMaven_ExcludesFile)
gen_MavenMaven_FileList_Basic = Generalization(general=Basic, specific=MavenMaven_FileList)
gen_MavenMaven_Filter_Basic = Generalization(general=Basic, specific=MavenMaven_Filter)
gen_MavenMaven_ClassPath_Set = Generalization(general=Set, specific=MavenMaven_ClassPath)
gen_MavenMaven_Task_ContentsGoal = Generalization(general=ContentsGoal, specific=MavenMaven_Task)
gen_MavenMaven_AntTaskDef_ContentsGoal = Generalization(general=ContentsGoal, specific=MavenMaven_AntTaskDef)
gen_MavenMaven_NewTask_Task = Generalization(general=Task, specific=MavenMaven_NewTask)
gen_MavenMaven_FilterSet_Set = Generalization(general=Set, specific=MavenMaven_FilterSet)
gen_MavenMaven_Path_Set = Generalization(general=Set, specific=MavenMaven_Path)
gen_MavenMaven_MiscellaneousTask_PreDefinedTask = Generalization(general=PreDefinedTask, specific=MavenMaven_MiscellaneousTask)
gen_MavenMaven_Echo_MiscellaneousTask = Generalization(general=MiscellaneousTask, specific=MavenMaven_Echo)
gen_MavenMaven_Tstamp_MiscellaneousTask = Generalization(general=MiscellaneousTask, specific=MavenMaven_Tstamp)
gen_MavenMaven_CompileTask_PreDefinedTask = Generalization(general=PreDefinedTask, specific=MavenMaven_CompileTask)
gen_MavenMaven_PreDefinedTask_Task = Generalization(general=Task, specific=MavenMaven_PreDefinedTask)
gen_MavenMaven_ExecutionTask_PreDefinedTask = Generalization(general=PreDefinedTask, specific=MavenMaven_ExecutionTask)
gen_MavenMaven_Exec_ExecutionTask = Generalization(general=ExecutionTask, specific=MavenMaven_Exec)
gen_MavenMaven_Java_ExecutionTask = Generalization(general=ExecutionTask, specific=MavenMaven_Java)
gen_MavenMaven_ArchiveTask_PreDefinedTask = Generalization(general=PreDefinedTask, specific=MavenMaven_ArchiveTask)
gen_MavenMaven_Jar_ArchiveTask = Generalization(general=ArchiveTask, specific=MavenMaven_Jar)
gen_MavenMaven_FileTask_PreDefinedTask = Generalization(general=PreDefinedTask, specific=MavenMaven_FileTask)
gen_MavenMaven_Mkdir_FileTask = Generalization(general=FileTask, specific=MavenMaven_Mkdir)
gen_MavenMaven_Copy_FileTask = Generalization(general=FileTask, specific=MavenMaven_Copy)
gen_MavenMaven_Javac_CompileTask = Generalization(general=CompileTask, specific=MavenMaven_Javac)
gen_MavenMaven_DocumentationTask_PreDefinedTask = Generalization(general=PreDefinedTask, specific=MavenMaven_DocumentationTask)
gen_MavenMaven_Javadoc_DocumentationTask = Generalization(general=DocumentationTask, specific=MavenMaven_Javadoc)
gen_MavenMaven_Delete_FileTask = Generalization(general=FileTask, specific=MavenMaven_Delete)

# Domain Model
domain_model = DomainModel(
    name="MavenMaven",
    types={MavenMaven_AntTaskDef, MavenMaven_PrePostGoal, ContentsGoal, MavenMaven_AntPropertyName, AntProperty, MavenMaven_AntPropertyValue, AntPropertyName, MavenMaven_Project, MavenMaven_Xmlns, MavenMaven_Goal, MavenMaven_Path, MavenMaven_AntProperty, AbstractGoal, MavenMaven_PreGoal, PrePostGoal, MavenMaven_PostGoal, MavenMaven_Pattern, MavenMaven_AntPropertyLocation, MavenMaven_AntPropertyFile, MavenMaven_AntPropertyEnv, MavenMaven_JellyCommand, MavenMaven_JellySet, JellyCommand, MavenMaven_AbstractGoal, MavenMaven_ContentsGoal, MavenMaven_AttainGoal, MavenMaven_FiltersFile, MavenMaven_PathElement, MavenMaven_Set, MavenMaven_PatternSet, Set, MavenMaven_FileSet, MavenMaven_Basic, Pattern, MavenMaven_Mapper, Basic, MavenMaven_InExcludes, MavenMaven_Includes, InExcludes, MavenMaven_Excludes, MavenMaven_IncludesFile, MavenMaven_ExcludesFile, MavenMaven_FileList, MavenMaven_Filter, MavenMaven_ClassPath, MavenMaven_Task, MavenMaven_NewTask, Task, MavenMaven_FilterSet, MavenMaven_MiscellaneousTask, MavenMaven_Echo, MiscellaneousTask, MavenMaven_Tstamp, MavenMaven_FormatTstamp, MavenMaven_CompileTask, MavenMaven_Attribut, MavenMaven_PreDefinedTask, MavenMaven_ExecutionTask, PreDefinedTask, MavenMaven_Exec, ExecutionTask, MavenMaven_Java, MavenMaven_ArchiveTask, MavenMaven_Jar, ArchiveTask, MavenMaven_FileTask, MavenMaven_Mkdir, FileTask, MavenMaven_Copy, MavenMaven_Javac, CompileTask, MavenMaven_DocumentationTask, MavenMaven_Javadoc, DocumentationTask, MavenMaven_Delete},
    associations={taskdefs7, prePostGoals9, goals11, xmlns0, default1, path3, properties5, centralGoal17, centralGoal18, preGoal20, postGoal21, contentsGoal14, attainGoal15, inexcludes23, patternset24, include26, exclude28, fileset38, pathElement41, fileset43, filter30, filtersfile31, path34, pathElement36, format52, taskName46, attributes48, classPath50, inExcludes53, classPath55, fileset58, filterset60, mapper63},
    generalizations={gen_MavenMaven_AntProperty_ContentsGoal, gen_MavenMaven_AntPropertyName_AntProperty, gen_MavenMaven_AntPropertyValue_AntPropertyName, gen_MavenMaven_PrePostGoal_AbstractGoal, gen_MavenMaven_PreGoal_PrePostGoal, gen_MavenMaven_PostGoal_PrePostGoal, gen_MavenMaven_Goal_AbstractGoal, gen_MavenMaven_AntPropertyLocation_AntPropertyName, gen_MavenMaven_AntPropertyFile_AntProperty, gen_MavenMaven_AntPropertyEnv_AntProperty, gen_MavenMaven_JellyCommand_ContentsGoal, gen_MavenMaven_JellySet_JellyCommand, gen_MavenMaven_AttainGoal_ContentsGoal, gen_MavenMaven_FiltersFile_Basic, gen_MavenMaven_PathElement_Basic, gen_MavenMaven_Set_Pattern, gen_MavenMaven_PatternSet_Set, gen_MavenMaven_FileSet_Set, gen_MavenMaven_Basic_Pattern, gen_MavenMaven_Mapper_Basic, gen_MavenMaven_InExcludes_Basic, gen_MavenMaven_Includes_InExcludes, gen_MavenMaven_Excludes_InExcludes, gen_MavenMaven_IncludesFile_InExcludes, gen_MavenMaven_ExcludesFile_InExcludes, gen_MavenMaven_FileList_Basic, gen_MavenMaven_Filter_Basic, gen_MavenMaven_ClassPath_Set, gen_MavenMaven_Task_ContentsGoal, gen_MavenMaven_AntTaskDef_ContentsGoal, gen_MavenMaven_NewTask_Task, gen_MavenMaven_FilterSet_Set, gen_MavenMaven_Path_Set, gen_MavenMaven_MiscellaneousTask_PreDefinedTask, gen_MavenMaven_Echo_MiscellaneousTask, gen_MavenMaven_Tstamp_MiscellaneousTask, gen_MavenMaven_CompileTask_PreDefinedTask, gen_MavenMaven_PreDefinedTask_Task, gen_MavenMaven_ExecutionTask_PreDefinedTask, gen_MavenMaven_Exec_ExecutionTask, gen_MavenMaven_Java_ExecutionTask, gen_MavenMaven_ArchiveTask_PreDefinedTask, gen_MavenMaven_Jar_ArchiveTask, gen_MavenMaven_FileTask_PreDefinedTask, gen_MavenMaven_Mkdir_FileTask, gen_MavenMaven_Copy_FileTask, gen_MavenMaven_Javac_CompileTask, gen_MavenMaven_DocumentationTask_PreDefinedTask, gen_MavenMaven_Javadoc_DocumentationTask, gen_MavenMaven_Delete_FileTask},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)