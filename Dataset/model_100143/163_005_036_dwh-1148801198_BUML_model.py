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
FieldType: Enumeration = Enumeration(
    name="FieldType",
    literals={
            EnumerationLiteral(name="RELATIVE"),
			EnumerationLiteral(name="ABSOLUTE")
    }
)

# Classes
model_Type = Class(name="model_Type")
NamedElement = Class(name="NamedElement")
DescribedElement = Class(name="DescribedElement")
model_NativeSQLType = Class(name="model_NativeSQLType")
Type = Class(name="Type")
model_NamedElement = Class(name="model_NamedElement")
model_DescribedElement = Class(name="model_DescribedElement")
model_FQNamedElement = Class(name="model_FQNamedElement")
model_SeparatedElement = Class(name="model_SeparatedElement")
model_Database = Class(name="model_Database")
model_User = Class(name="model_User")
model_Schema = Class(name="model_Schema")
model_View = Class(name="model_View")
model_Column = Class(name="model_Column")
model_IColumn = Class(name="model_IColumn")
IColumn = Class(name="IColumn")
model_IFile = Class(name="model_IFile")
model_FileSet = Class(name="model_FileSet")
FQNamedElement = Class(name="FQNamedElement")
model_Domain = Class(name="model_Domain")
model_Table = Class(name="model_Table")
model_SCTFile = Class(name="model_SCTFile")
model_Mapping = Class(name="model_Mapping")
model_MappingImport = Class(name="model_MappingImport")
Mapping = Class(name="Mapping")
model_MappingFile = Class(name="model_MappingFile")
model_MappingExport = Class(name="model_MappingExport")
model_File = Class(name="model_File")
SeparatedElement = Class(name="SeparatedElement")
IFile = Class(name="IFile")
model_Field = Class(name="model_Field")
model_TaskImport = Class(name="model_TaskImport")
Task = Class(name="Task")
model_TaskFile = Class(name="model_TaskFile")
model_MappingSQL = Class(name="model_MappingSQL")
model_TaskSet = Class(name="model_TaskSet")
model_Task = Class(name="model_Task", is_abstract=True)
model_TaskExport = Class(name="model_TaskExport")
model_TaskSQL = Class(name="model_TaskSQL")
model_Site = Class(name="model_Site")

# model_Type class attributes and methods

# NamedElement class attributes and methods

# DescribedElement class attributes and methods

# model_NativeSQLType class attributes and methods

# Type class attributes and methods

# model_NamedElement class attributes and methods
model_NamedElement_name: Property = Property(name="name", type=StringType)
model_NamedElement.attributes={model_NamedElement_name}

# model_DescribedElement class attributes and methods
model_DescribedElement_description: Property = Property(name="description", type=StringType)
model_DescribedElement.attributes={model_DescribedElement_description}

# model_FQNamedElement class attributes and methods
model_FQNamedElement_m_getFQName: Method = Method(name="getFQName", parameters={}, type=StringType)
model_FQNamedElement.methods={model_FQNamedElement_m_getFQName}

# model_SeparatedElement class attributes and methods
model_SeparatedElement_separator: Property = Property(name="separator", type=StringType)
model_SeparatedElement.attributes={model_SeparatedElement_separator}

# model_Database class attributes and methods
model_Database_dsn: Property = Property(name="dsn", type=StringType)
model_Database.attributes={model_Database_dsn}

# model_User class attributes and methods
model_User_password: Property = Property(name="password", type=StringType)
model_User.attributes={model_User_password}

# model_Schema class attributes and methods

# model_View class attributes and methods
model_View_sql: Property = Property(name="sql", type=StringType)
model_View.attributes={model_View_sql}

# model_Column class attributes and methods

# model_IColumn class attributes and methods

# IColumn class attributes and methods

# model_IFile class attributes and methods

# model_FileSet class attributes and methods
model_FileSet_hostname: Property = Property(name="hostname", type=StringType)
model_FileSet.attributes={model_FileSet_hostname}

# FQNamedElement class attributes and methods

# model_Domain class attributes and methods
model_Domain_type: Property = Property(name="type", type=StringType)
model_Domain.attributes={model_Domain_type}

# model_Table class attributes and methods

# model_SCTFile class attributes and methods
model_SCTFile_file: Property = Property(name="file", type=StringType)
model_SCTFile.attributes={model_SCTFile_file}

# model_Mapping class attributes and methods
model_Mapping_expression: Property = Property(name="expression", type=StringType)
model_Mapping.attributes={model_Mapping_expression}

# model_MappingImport class attributes and methods

# Mapping class attributes and methods

# model_MappingFile class attributes and methods

# model_MappingExport class attributes and methods

# model_File class attributes and methods
model_File_files: Property = Property(name="files", type=StringType)
model_File_numberOfHeaderLines: Property = Property(name="numberOfHeaderLines", type=StringType)
model_File.attributes={model_File_numberOfHeaderLines, model_File_files}

# SeparatedElement class attributes and methods

# IFile class attributes and methods

# model_Field class attributes and methods
model_Field_type: Property = Property(name="type", type=StringType)
model_Field_length: Property = Property(name="length", type=StringType)
model_Field_position: Property = Property(name="position", type=StringType)
model_Field.attributes={model_Field_position, model_Field_length, model_Field_type}

# model_TaskImport class attributes and methods

# Task class attributes and methods

# model_TaskFile class attributes and methods

# model_MappingSQL class attributes and methods

# model_TaskSet class attributes and methods

# model_Task class attributes and methods
model_Task_fileName: Property = Property(name="fileName", type=StringType)
model_Task.attributes={model_Task_fileName}

# model_TaskExport class attributes and methods

# model_TaskSQL class attributes and methods

# model_Site class attributes and methods

# Relationships
users0: BinaryAssociation = BinaryAssociation(
    name="users0",
    ends={
        Property(name="model_User", type=model_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Database", type=model_User, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schemas1: BinaryAssociation = BinaryAssociation(
    name="schemas1",
    ends={
        Property(name="model_Schema", type=model_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Database2", type=model_Schema, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tables8: BinaryAssociation = BinaryAssociation(
    name="tables8",
    ends={
        Property(name="model_Schema9", type=model_Table, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="model_Table", type=model_Schema, multiplicity=Multiplicity(1, 1))
    }
)
views10: BinaryAssociation = BinaryAssociation(
    name="views10",
    ends={
        Property(name="model_View", type=model_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Schema11", type=model_View, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns12: BinaryAssociation = BinaryAssociation(
    name="columns12",
    ends={
        Property(name="model_Column", type=model_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Table13", type=model_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type14: BinaryAssociation = BinaryAssociation(
    name="type14",
    ends={
        Property(name="model_Type", type=model_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Column15", type=model_Type, multiplicity=Multiplicity(1, 1))
    }
)
schema3: BinaryAssociation = BinaryAssociation(
    name="schema3",
    ends={
        Property(name="model_Schema5", type=model_User, multiplicity=Multiplicity(1, 1)),
        Property(name="model_User4", type=model_Schema, multiplicity=Multiplicity(0, 1))
    }
)
domains6: BinaryAssociation = BinaryAssociation(
    name="domains6",
    ends={
        Property(name="model_Domain", type=model_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Schema7", type=model_Domain, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns18: BinaryAssociation = BinaryAssociation(
    name="columns18",
    ends={
        Property(name="model_Column19", type=model_SCTFile, multiplicity=Multiplicity(1, 1)),
        Property(name="model_SCTFile", type=model_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
domains20: BinaryAssociation = BinaryAssociation(
    name="domains20",
    ends={
        Property(name="model_Domain22", type=model_SCTFile, multiplicity=Multiplicity(1, 1)),
        Property(name="model_SCTFile21", type=model_Domain, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source23: BinaryAssociation = BinaryAssociation(
    name="source23",
    ends={
        Property(name="model_IColumn", type=model_MappingImport, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MappingImport", type=model_IColumn, multiplicity=Multiplicity(0, 9999))
    }
)
target24: BinaryAssociation = BinaryAssociation(
    name="target24",
    ends={
        Property(name="model_Column26", type=model_MappingImport, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MappingImport25", type=model_Column, multiplicity=Multiplicity(1, 1))
    }
)
source27: BinaryAssociation = BinaryAssociation(
    name="source27",
    ends={
        Property(name="model_Field28", type=model_MappingFile, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MappingFile", type=model_Field, multiplicity=Multiplicity(0, 9999))
    }
)
target29: BinaryAssociation = BinaryAssociation(
    name="target29",
    ends={
        Property(name="model_Field31", type=model_MappingFile, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MappingFile30", type=model_Field, multiplicity=Multiplicity(1, 1))
    }
)
source32: BinaryAssociation = BinaryAssociation(
    name="source32",
    ends={
        Property(name="model_Column33", type=model_MappingExport, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MappingExport", type=model_Column, multiplicity=Multiplicity(0, 9999))
    }
)
files16: BinaryAssociation = BinaryAssociation(
    name="files16",
    ends={
        Property(name="model_IFile", type=model_FileSet, multiplicity=Multiplicity(1, 1)),
        Property(name="model_FileSet", type=model_IFile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fields17: BinaryAssociation = BinaryAssociation(
    name="fields17",
    ends={
        Property(name="model_Field", type=model_File, multiplicity=Multiplicity(1, 1)),
        Property(name="model_File", type=model_Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
preconditions47: BinaryAssociation = BinaryAssociation(
    name="preconditions47",
    ends={
        Property(name="model_Task48", type=model_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Task46", type=model_Task, multiplicity=Multiplicity(0, 9999))
    }
)
source49: BinaryAssociation = BinaryAssociation(
    name="source49",
    ends={
        Property(name="model_IFile50", type=model_TaskImport, multiplicity=Multiplicity(1, 1)),
        Property(name="model_TaskImport", type=model_IFile, multiplicity=Multiplicity(1, 1))
    }
)
target51: BinaryAssociation = BinaryAssociation(
    name="target51",
    ends={
        Property(name="model_Table53", type=model_TaskImport, multiplicity=Multiplicity(1, 1)),
        Property(name="model_TaskImport52", type=model_Table, multiplicity=Multiplicity(1, 1))
    }
)
map54: BinaryAssociation = BinaryAssociation(
    name="map54",
    ends={
        Property(name="model_MappingImport56", type=model_TaskImport, multiplicity=Multiplicity(1, 1)),
        Property(name="model_TaskImport55", type=model_MappingImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source57: BinaryAssociation = BinaryAssociation(
    name="source57",
    ends={
        Property(name="model_File58", type=model_TaskFile, multiplicity=Multiplicity(1, 1)),
        Property(name="model_TaskFile", type=model_File, multiplicity=Multiplicity(1, 1))
    }
)
target59: BinaryAssociation = BinaryAssociation(
    name="target59",
    ends={
        Property(name="model_File61", type=model_TaskFile, multiplicity=Multiplicity(1, 1)),
        Property(name="model_TaskFile60", type=model_File, multiplicity=Multiplicity(1, 1))
    }
)
map62: BinaryAssociation = BinaryAssociation(
    name="map62",
    ends={
        Property(name="model_MappingFile64", type=model_TaskFile, multiplicity=Multiplicity(1, 1)),
        Property(name="model_TaskFile63", type=model_MappingFile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target34: BinaryAssociation = BinaryAssociation(
    name="target34",
    ends={
        Property(name="model_IColumn36", type=model_MappingExport, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MappingExport35", type=model_IColumn, multiplicity=Multiplicity(1, 1))
    }
)
source37: BinaryAssociation = BinaryAssociation(
    name="source37",
    ends={
        Property(name="model_Column38", type=model_MappingSQL, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MappingSQL", type=model_Column, multiplicity=Multiplicity(0, 9999))
    }
)
target39: BinaryAssociation = BinaryAssociation(
    name="target39",
    ends={
        Property(name="model_Column41", type=model_MappingSQL, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MappingSQL40", type=model_Column, multiplicity=Multiplicity(0, 9999))
    }
)
tasks42: BinaryAssociation = BinaryAssociation(
    name="tasks42",
    ends={
        Property(name="model_Task", type=model_TaskSet, multiplicity=Multiplicity(1, 1)),
        Property(name="model_TaskSet", type=model_Task, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
databases81: BinaryAssociation = BinaryAssociation(
    name="databases81",
    ends={
        Property(name="model_Database82", type=model_Site, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Site", type=model_Database, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
preconditions43: BinaryAssociation = BinaryAssociation(
    name="preconditions43",
    ends={
        Property(name="model_Task45", type=model_TaskSet, multiplicity=Multiplicity(1, 1)),
        Property(name="model_TaskSet44", type=model_Task, multiplicity=Multiplicity(0, 9999))
    }
)
fileSets83: BinaryAssociation = BinaryAssociation(
    name="fileSets83",
    ends={
        Property(name="model_FileSet85", type=model_Site, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Site84", type=model_FileSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
taskSets86: BinaryAssociation = BinaryAssociation(
    name="taskSets86",
    ends={
        Property(name="model_TaskSet88", type=model_Site, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Site87", type=model_TaskSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source65: BinaryAssociation = BinaryAssociation(
    name="source65",
    ends={
        Property(name="model_Table66", type=model_TaskExport, multiplicity=Multiplicity(1, 1)),
        Property(name="model_TaskExport", type=model_Table, multiplicity=Multiplicity(1, 1))
    }
)
target67: BinaryAssociation = BinaryAssociation(
    name="target67",
    ends={
        Property(name="model_IFile69", type=model_TaskExport, multiplicity=Multiplicity(1, 1)),
        Property(name="model_TaskExport68", type=model_IFile, multiplicity=Multiplicity(1, 1))
    }
)
map70: BinaryAssociation = BinaryAssociation(
    name="map70",
    ends={
        Property(name="model_MappingExport72", type=model_TaskExport, multiplicity=Multiplicity(1, 1)),
        Property(name="model_TaskExport71", type=model_MappingExport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source73: BinaryAssociation = BinaryAssociation(
    name="source73",
    ends={
        Property(name="model_Table74", type=model_TaskSQL, multiplicity=Multiplicity(1, 1)),
        Property(name="model_TaskSQL", type=model_Table, multiplicity=Multiplicity(1, 1))
    }
)
target75: BinaryAssociation = BinaryAssociation(
    name="target75",
    ends={
        Property(name="model_Table77", type=model_TaskSQL, multiplicity=Multiplicity(1, 1)),
        Property(name="model_TaskSQL76", type=model_Table, multiplicity=Multiplicity(1, 1))
    }
)
map78: BinaryAssociation = BinaryAssociation(
    name="map78",
    ends={
        Property(name="model_MappingSQL80", type=model_TaskSQL, multiplicity=Multiplicity(1, 1)),
        Property(name="model_TaskSQL79", type=model_MappingSQL, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_model_Type_NamedElement = Generalization(general=NamedElement, specific=model_Type)
gen_model_Type_DescribedElement = Generalization(general=DescribedElement, specific=model_Type)
gen_model_NativeSQLType_Type = Generalization(general=Type, specific=model_NativeSQLType)
gen_model_Database_NamedElement = Generalization(general=NamedElement, specific=model_Database)
gen_model_Database_DescribedElement = Generalization(general=DescribedElement, specific=model_Database)
gen_model_View_NamedElement = Generalization(general=NamedElement, specific=model_View)
gen_model_View_DescribedElement = Generalization(general=DescribedElement, specific=model_View)
gen_model_View_FQNamedElement = Generalization(general=FQNamedElement, specific=model_View)
gen_model_Table_NamedElement = Generalization(general=NamedElement, specific=model_Table)
gen_model_Table_DescribedElement = Generalization(general=DescribedElement, specific=model_Table)
gen_model_Table_FQNamedElement = Generalization(general=FQNamedElement, specific=model_Table)
gen_model_IColumn_NamedElement = Generalization(general=NamedElement, specific=model_IColumn)
gen_model_IColumn_DescribedElement = Generalization(general=DescribedElement, specific=model_IColumn)
gen_model_IColumn_FQNamedElement = Generalization(general=FQNamedElement, specific=model_IColumn)
gen_model_Column_IColumn = Generalization(general=IColumn, specific=model_Column)
gen_model_Domain_Type = Generalization(general=Type, specific=model_Domain)
gen_model_Domain_FQNamedElement = Generalization(general=FQNamedElement, specific=model_Domain)
gen_model_IFile_NamedElement = Generalization(general=NamedElement, specific=model_IFile)
gen_model_IFile_DescribedElement = Generalization(general=DescribedElement, specific=model_IFile)
gen_model_FileSet_NamedElement = Generalization(general=NamedElement, specific=model_FileSet)
gen_model_FileSet_DescribedElement = Generalization(general=DescribedElement, specific=model_FileSet)
gen_model_User_NamedElement = Generalization(general=NamedElement, specific=model_User)
gen_model_User_DescribedElement = Generalization(general=DescribedElement, specific=model_User)
gen_model_User_FQNamedElement = Generalization(general=FQNamedElement, specific=model_User)
gen_model_Schema_NamedElement = Generalization(general=NamedElement, specific=model_Schema)
gen_model_Schema_DescribedElement = Generalization(general=DescribedElement, specific=model_Schema)
gen_model_SCTFile_IFile = Generalization(general=IFile, specific=model_SCTFile)
gen_model_MappingImport_Mapping = Generalization(general=Mapping, specific=model_MappingImport)
gen_model_MappingFile_Mapping = Generalization(general=Mapping, specific=model_MappingFile)
gen_model_MappingExport_Mapping = Generalization(general=Mapping, specific=model_MappingExport)
gen_model_File_SeparatedElement = Generalization(general=SeparatedElement, specific=model_File)
gen_model_File_IFile = Generalization(general=IFile, specific=model_File)
gen_model_Field_IColumn = Generalization(general=IColumn, specific=model_Field)
gen_model_Field_SeparatedElement = Generalization(general=SeparatedElement, specific=model_Field)
gen_model_Task_NamedElement = Generalization(general=NamedElement, specific=model_Task)
gen_model_Task_DescribedElement = Generalization(general=DescribedElement, specific=model_Task)
gen_model_TaskImport_Task = Generalization(general=Task, specific=model_TaskImport)
gen_model_TaskFile_Task = Generalization(general=Task, specific=model_TaskFile)
gen_model_MappingSQL_Mapping = Generalization(general=Mapping, specific=model_MappingSQL)
gen_model_TaskSet_NamedElement = Generalization(general=NamedElement, specific=model_TaskSet)
gen_model_TaskSet_DescribedElement = Generalization(general=DescribedElement, specific=model_TaskSet)
gen_model_TaskExport_Task = Generalization(general=Task, specific=model_TaskExport)
gen_model_TaskSQL_Task = Generalization(general=Task, specific=model_TaskSQL)
gen_model_Site_NamedElement = Generalization(general=NamedElement, specific=model_Site)
gen_model_Site_DescribedElement = Generalization(general=DescribedElement, specific=model_Site)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_Type, NamedElement, DescribedElement, model_NativeSQLType, Type, model_NamedElement, model_DescribedElement, model_FQNamedElement, model_SeparatedElement, model_Database, model_User, model_Schema, model_View, model_Column, model_IColumn, IColumn, model_IFile, model_FileSet, FQNamedElement, model_Domain, model_Table, model_SCTFile, model_Mapping, model_MappingImport, Mapping, model_MappingFile, model_MappingExport, model_File, SeparatedElement, IFile, model_Field, model_TaskImport, Task, model_TaskFile, model_MappingSQL, model_TaskSet, model_Task, model_TaskExport, model_TaskSQL, model_Site, FieldType},
    associations={users0, schemas1, tables8, views10, columns12, type14, schema3, domains6, columns18, domains20, source23, target24, source27, target29, source32, files16, fields17, preconditions47, source49, target51, map54, source57, target59, map62, target34, source37, target39, tasks42, databases81, preconditions43, fileSets83, taskSets86, source65, target67, map70, source73, target75, map78},
    generalizations={gen_model_Type_NamedElement, gen_model_Type_DescribedElement, gen_model_NativeSQLType_Type, gen_model_Database_NamedElement, gen_model_Database_DescribedElement, gen_model_View_NamedElement, gen_model_View_DescribedElement, gen_model_View_FQNamedElement, gen_model_Table_NamedElement, gen_model_Table_DescribedElement, gen_model_Table_FQNamedElement, gen_model_IColumn_NamedElement, gen_model_IColumn_DescribedElement, gen_model_IColumn_FQNamedElement, gen_model_Column_IColumn, gen_model_Domain_Type, gen_model_Domain_FQNamedElement, gen_model_IFile_NamedElement, gen_model_IFile_DescribedElement, gen_model_FileSet_NamedElement, gen_model_FileSet_DescribedElement, gen_model_User_NamedElement, gen_model_User_DescribedElement, gen_model_User_FQNamedElement, gen_model_Schema_NamedElement, gen_model_Schema_DescribedElement, gen_model_SCTFile_IFile, gen_model_MappingImport_Mapping, gen_model_MappingFile_Mapping, gen_model_MappingExport_Mapping, gen_model_File_SeparatedElement, gen_model_File_IFile, gen_model_Field_IColumn, gen_model_Field_SeparatedElement, gen_model_Task_NamedElement, gen_model_Task_DescribedElement, gen_model_TaskImport_Task, gen_model_TaskFile_Task, gen_model_MappingSQL_Mapping, gen_model_TaskSet_NamedElement, gen_model_TaskSet_DescribedElement, gen_model_TaskExport_Task, gen_model_TaskSQL_Task, gen_model_Site_NamedElement, gen_model_Site_DescribedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)