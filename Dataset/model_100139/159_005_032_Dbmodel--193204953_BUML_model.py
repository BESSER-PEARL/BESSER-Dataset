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
KudaReplicate: Enumeration = Enumeration(
    name="KudaReplicate",
    literals={
            EnumerationLiteral(name="PUBLISH"),
			EnumerationLiteral(name="PUBLISHSTV"),
			EnumerationLiteral(name="DWH"),
			EnumerationLiteral(name="SNAP")
    }
)

PhysicalDatabase: Enumeration = Enumeration(
    name="PhysicalDatabase",
    literals={
            EnumerationLiteral(name="PDB_ABFRAGE_ARCHIV"),
			EnumerationLiteral(name="PDB_ABFRAGE_BUCH_STAMM"),
			EnumerationLiteral(name="PDB_ABFRAGE_ETV"),
			EnumerationLiteral(name="PDB_ABFRAGE_FZK"),
			EnumerationLiteral(name="PDB_ABFRAGE_MON"),
			EnumerationLiteral(name="PDB_ABFRAGE_PKT_STAMM"),
			EnumerationLiteral(name="PDB_ABFRAGE_VSTI"),
			EnumerationLiteral(name="PDB_AUSW_KOBE_ARCHIV"),
			EnumerationLiteral(name="PDB_AUSW_KOBE_BUCH_STAMM"),
			EnumerationLiteral(name="PDB_AUSW_KOBE_MON"),
			EnumerationLiteral(name="PDB_AUSW_KOBE_PKT_STAMM"),
			EnumerationLiteral(name="PDB_AUSW_KOBE_STATISTIK"),
			EnumerationLiteral(name="PDB_KOBE_AUSW_ADMIN"),
			EnumerationLiteral(name="PDB_KOBE_DATA"),
			EnumerationLiteral(name="PDB_KOBE_DEZ_STAMM"),
			EnumerationLiteral(name="PDB_KOBE_KNDTEST"),
			EnumerationLiteral(name="PDB_KOBE_PMON"),
			EnumerationLiteral(name="PDB_KOBE_STAMM"),
			EnumerationLiteral(name="PDB_KOBE_STEUERUNG"),
			EnumerationLiteral(name="PDB_KOBE_GLOBAL"),
			EnumerationLiteral(name="PDB_KUDA_TRANS_TRANSIT"),
			EnumerationLiteral(name="PDB_MANDANT_BUCH_PROV"),
			EnumerationLiteral(name="PDB_MANDANT_BUCH_STAMM"),
			EnumerationLiteral(name="PDB_MANDANT_MON"),
			EnumerationLiteral(name="PDB_MANDANT_PKT_DATA"),
			EnumerationLiteral(name="PDB_MANDANT_PKT_STAMM"),
			EnumerationLiteral(name="PDB_MANDANT_TAG"),
			EnumerationLiteral(name="PDB_MANDANT_TAG_A"),
			EnumerationLiteral(name="PDB_PART_AUFT"),
			EnumerationLiteral(name="PDB_PART_BUCH_PROV"),
			EnumerationLiteral(name="PDB_PART_BUCH_STAMM"),
			EnumerationLiteral(name="PDB_PART_JAHR"),
			EnumerationLiteral(name="PDB_PART_MON"),
			EnumerationLiteral(name="PDB_PART_PKT_DATA"),
			EnumerationLiteral(name="PDB_PART_PKT_STAMM"),
			EnumerationLiteral(name="PDB_PART_TAG"),
			EnumerationLiteral(name="PDB_PART_TAG_A")
    }
)

Mtype: Enumeration = Enumeration(
    name="Mtype",
    literals={
            EnumerationLiteral(name="KUDA"),
			EnumerationLiteral(name="KOBE")
    }
)

KudaType: Enumeration = Enumeration(
    name="KudaType",
    literals={
            EnumerationLiteral(name="MAIN"),
			EnumerationLiteral(name="PUBLISH"),
			EnumerationLiteral(name="TIPO")
    }
)

KobeType: Enumeration = Enumeration(
    name="KobeType",
    literals={
            EnumerationLiteral(name="KORA"),
			EnumerationLiteral(name="MAIN"),
			EnumerationLiteral(name="AUSW")
    }
)

LockSchema: Enumeration = Enumeration(
    name="LockSchema",
    literals={
            EnumerationLiteral(name="DATAPAGES"),
			EnumerationLiteral(name="DATAROWS"),
			EnumerationLiteral(name="ALLPAGES")
    }
)

# Classes
dbmodel_Import = Class(name="dbmodel_Import")
dbmodel_Subject = Class(name="dbmodel_Subject")
dbmodel_Class = Class(name="dbmodel_Class")
dbmodel_Duplicate = Class(name="dbmodel_Duplicate")
ClassOrDuplicate = Class(name="ClassOrDuplicate")
dbmodel_DbModel = Class(name="dbmodel_DbModel")
dbmodel_Index = Class(name="dbmodel_Index")
dbmodel_Pdb = Class(name="dbmodel_Pdb")
dbmodel_Ltype = Class(name="dbmodel_Ltype")
dbmodel_StructShare = Class(name="dbmodel_StructShare")
dbmodel_StructOverride = Class(name="dbmodel_StructOverride")
dbmodel_Attribute = Class(name="dbmodel_Attribute")
dbmodel_Primkey = Class(name="dbmodel_Primkey")
dbmodel_IndexRef = Class(name="dbmodel_IndexRef")
dbmodel_Type = Class(name="dbmodel_Type")
dbmodel_Stype = Class(name="dbmodel_Stype")
dbmodel_ClassOrDuplicate = Class(name="dbmodel_ClassOrDuplicate")

# dbmodel_Import class attributes and methods
dbmodel_Import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
dbmodel_Import.attributes={dbmodel_Import_importedNamespace}

# dbmodel_Subject class attributes and methods
dbmodel_Subject_name: Property = Property(name="name", type=StringType)
dbmodel_Subject.attributes={dbmodel_Subject_name}

# dbmodel_Class class attributes and methods
dbmodel_Class_descr: Property = Property(name="descr", type=StringType)
dbmodel_Class_noDBio: Property = Property(name="noDBio", type=BooleanType)
dbmodel_Class_publish: Property = Property(name="publish", type=BooleanType)
dbmodel_Class_vmaj: Property = Property(name="vmaj", type=IntegerType)
dbmodel_Class_vmin: Property = Property(name="vmin", type=IntegerType)
dbmodel_Class_pubspec: Property = Property(name="pubspec", type=BooleanType)
dbmodel_Class_pubname: Property = Property(name="pubname", type=StringType)
dbmodel_Class_whereclause: Property = Property(name="whereclause", type=StringType)
dbmodel_Class_aName: Property = Property(name="aName", type=StringType)
dbmodel_Class_archivIndex: Property = Property(name="archivIndex", type=StringType)
dbmodel_Class.attributes={dbmodel_Class_vmin, dbmodel_Class_pubspec, dbmodel_Class_pubname, dbmodel_Class_noDBio, dbmodel_Class_archivIndex, dbmodel_Class_vmaj, dbmodel_Class_descr, dbmodel_Class_aName, dbmodel_Class_publish, dbmodel_Class_whereclause}

# dbmodel_Duplicate class attributes and methods

# ClassOrDuplicate class attributes and methods

# dbmodel_DbModel class attributes and methods
dbmodel_DbModel_kudaType: Property = Property(name="kudaType", type=StringType)
dbmodel_DbModel_kobeType: Property = Property(name="kobeType", type=StringType)
dbmodel_DbModel_version: Property = Property(name="version", type=StringType)
dbmodel_DbModel_doAll: Property = Property(name="doAll", type=BooleanType)
dbmodel_DbModel_name: Property = Property(name="name", type=StringType)
dbmodel_DbModel_mtype: Property = Property(name="mtype", type=StringType)
dbmodel_DbModel.attributes={dbmodel_DbModel_mtype, dbmodel_DbModel_version, dbmodel_DbModel_doAll, dbmodel_DbModel_name, dbmodel_DbModel_kobeType, dbmodel_DbModel_kudaType}

# dbmodel_Index class attributes and methods
dbmodel_Index_kuko: Property = Property(name="kuko", type=BooleanType)
dbmodel_Index_name: Property = Property(name="name", type=StringType)
dbmodel_Index_unique: Property = Property(name="unique", type=BooleanType)
dbmodel_Index.attributes={dbmodel_Index_kuko, dbmodel_Index_name, dbmodel_Index_unique}

# dbmodel_Pdb class attributes and methods
dbmodel_Pdb_name: Property = Property(name="name", type=StringType)
dbmodel_Pdb_lockSchema: Property = Property(name="lockSchema", type=StringType)
dbmodel_Pdb_tablePartitioning: Property = Property(name="tablePartitioning", type=IntegerType)
dbmodel_Pdb.attributes={dbmodel_Pdb_tablePartitioning, dbmodel_Pdb_lockSchema, dbmodel_Pdb_name}

# dbmodel_Ltype class attributes and methods

# dbmodel_StructShare class attributes and methods

# dbmodel_StructOverride class attributes and methods
dbmodel_StructOverride_altname: Property = Property(name="altname", type=StringType)
dbmodel_StructOverride.attributes={dbmodel_StructOverride_altname}

# dbmodel_Attribute class attributes and methods
dbmodel_Attribute_name: Property = Property(name="name", type=StringType)
dbmodel_Attribute_descr: Property = Property(name="descr", type=StringType)
dbmodel_Attribute_foreign: Property = Property(name="foreign", type=BooleanType)
dbmodel_Attribute_exttable: Property = Property(name="exttable", type=StringType)
dbmodel_Attribute_extattr: Property = Property(name="extattr", type=StringType)
dbmodel_Attribute_immutable: Property = Property(name="immutable", type=BooleanType)
dbmodel_Attribute_nullOK: Property = Property(name="nullOK", type=BooleanType)
dbmodel_Attribute_kuko: Property = Property(name="kuko", type=BooleanType)
dbmodel_Attribute_kukoindex: Property = Property(name="kukoindex", type=BooleanType)
dbmodel_Attribute_kukoonly: Property = Property(name="kukoonly", type=BooleanType)
dbmodel_Attribute_shared: Property = Property(name="shared", type=BooleanType)
dbmodel_Attribute_isPublic: Property = Property(name="isPublic", type=BooleanType)
dbmodel_Attribute_optional: Property = Property(name="optional", type=BooleanType)
dbmodel_Attribute_archiv: Property = Property(name="archiv", type=BooleanType)
dbmodel_Attribute_aName: Property = Property(name="aName", type=StringType)
dbmodel_Attribute_sybident: Property = Property(name="sybident", type=BooleanType)
dbmodel_Attribute_isInDB: Property = Property(name="isInDB", type=BooleanType)
dbmodel_Attribute.attributes={dbmodel_Attribute_shared, dbmodel_Attribute_optional, dbmodel_Attribute_aName, dbmodel_Attribute_foreign, dbmodel_Attribute_descr, dbmodel_Attribute_kuko, dbmodel_Attribute_kukoonly, dbmodel_Attribute_immutable, dbmodel_Attribute_isPublic, dbmodel_Attribute_archiv, dbmodel_Attribute_sybident, dbmodel_Attribute_extattr, dbmodel_Attribute_kukoindex, dbmodel_Attribute_isInDB, dbmodel_Attribute_exttable, dbmodel_Attribute_name, dbmodel_Attribute_nullOK}

# dbmodel_Primkey class attributes and methods

# dbmodel_IndexRef class attributes and methods
dbmodel_IndexRef_isPrimkey: Property = Property(name="isPrimkey", type=BooleanType)
dbmodel_IndexRef_clustered: Property = Property(name="clustered", type=BooleanType)
dbmodel_IndexRef.attributes={dbmodel_IndexRef_clustered, dbmodel_IndexRef_isPrimkey}

# dbmodel_Type class attributes and methods

# dbmodel_Stype class attributes and methods

# dbmodel_ClassOrDuplicate class attributes and methods
dbmodel_ClassOrDuplicate_name: Property = Property(name="name", type=StringType)
dbmodel_ClassOrDuplicate_abbrev: Property = Property(name="abbrev", type=StringType)
dbmodel_ClassOrDuplicate_reps: Property = Property(name="reps", type=StringType)
dbmodel_ClassOrDuplicate.attributes={dbmodel_ClassOrDuplicate_reps, dbmodel_ClassOrDuplicate_name, dbmodel_ClassOrDuplicate_abbrev}

# Relationships
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="dbmodel_Import", type=dbmodel_DbModel, multiplicity=Multiplicity(1, 1)),
        Property(name="dbmodel_DbModel", type=dbmodel_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subjects1: BinaryAssociation = BinaryAssociation(
    name="subjects1",
    ends={
        Property(name="dbmodel_Subject", type=dbmodel_DbModel, multiplicity=Multiplicity(1, 1)),
        Property(name="dbmodel_DbModel2", type=dbmodel_Subject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classes3: BinaryAssociation = BinaryAssociation(
    name="classes3",
    ends={
        Property(name="dbmodel_Class", type=dbmodel_DbModel, multiplicity=Multiplicity(1, 1)),
        Property(name="dbmodel_DbModel4", type=dbmodel_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
duplicates5: BinaryAssociation = BinaryAssociation(
    name="duplicates5",
    ends={
        Property(name="dbmodel_Duplicate", type=dbmodel_DbModel, multiplicity=Multiplicity(1, 1)),
        Property(name="dbmodel_DbModel6", type=dbmodel_Duplicate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subject7: BinaryAssociation = BinaryAssociation(
    name="subject7",
    ends={
        Property(name="dbmodel_Subject9", type=dbmodel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="dbmodel_Class8", type=dbmodel_Subject, multiplicity=Multiplicity(0, 1))
    }
)
indices14: BinaryAssociation = BinaryAssociation(
    name="indices14",
    ends={
        Property(name="dbmodel_Index", type=dbmodel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="dbmodel_Class15", type=dbmodel_Index, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pdbs16: BinaryAssociation = BinaryAssociation(
    name="pdbs16",
    ends={
        Property(name="dbmodel_Pdb", type=dbmodel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="dbmodel_Class17", type=dbmodel_Pdb, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
orig18: BinaryAssociation = BinaryAssociation(
    name="orig18",
    ends={
        Property(name="dbmodel_Class20", type=dbmodel_Duplicate, multiplicity=Multiplicity(1, 1)),
        Property(name="dbmodel_Duplicate19", type=dbmodel_Class, multiplicity=Multiplicity(0, 1))
    }
)
type21: BinaryAssociation = BinaryAssociation(
    name="type21",
    ends={
        Property(name="dbmodel_Ltype", type=dbmodel_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="dbmodel_Attribute22", type=dbmodel_Ltype, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
forattr24: BinaryAssociation = BinaryAssociation(
    name="forattr24",
    ends={
        Property(name="dbmodel_Attribute25", type=dbmodel_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="dbmodel_Attribute23", type=dbmodel_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
shrs26: BinaryAssociation = BinaryAssociation(
    name="shrs26",
    ends={
        Property(name="dbmodel_StructShare", type=dbmodel_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="dbmodel_Attribute27", type=dbmodel_StructShare, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ovride28: BinaryAssociation = BinaryAssociation(
    name="ovride28",
    ends={
        Property(name="dbmodel_StructOverride", type=dbmodel_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="dbmodel_Attribute29", type=dbmodel_StructOverride, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes10: BinaryAssociation = BinaryAssociation(
    name="attributes10",
    ends={
        Property(name="dbmodel_Attribute", type=dbmodel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="dbmodel_Class11", type=dbmodel_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primkey12: BinaryAssociation = BinaryAssociation(
    name="primkey12",
    ends={
        Property(name="dbmodel_Primkey", type=dbmodel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="dbmodel_Class13", type=dbmodel_Primkey, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attrs36: BinaryAssociation = BinaryAssociation(
    name="attrs36",
    ends={
        Property(name="dbmodel_Attribute38", type=dbmodel_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="dbmodel_Index37", type=dbmodel_Attribute, multiplicity=Multiplicity(0, 9999))
    }
)
index39: BinaryAssociation = BinaryAssociation(
    name="index39",
    ends={
        Property(name="dbmodel_Index40", type=dbmodel_IndexRef, multiplicity=Multiplicity(1, 1)),
        Property(name="dbmodel_IndexRef", type=dbmodel_Index, multiplicity=Multiplicity(0, 1))
    }
)
attr41: BinaryAssociation = BinaryAssociation(
    name="attr41",
    ends={
        Property(name="dbmodel_Attribute43", type=dbmodel_IndexRef, multiplicity=Multiplicity(1, 1)),
        Property(name="dbmodel_IndexRef42", type=dbmodel_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
indices44: BinaryAssociation = BinaryAssociation(
    name="indices44",
    ends={
        Property(name="dbmodel_IndexRef46", type=dbmodel_Pdb, multiplicity=Multiplicity(1, 1)),
        Property(name="dbmodel_Pdb45", type=dbmodel_IndexRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type47: BinaryAssociation = BinaryAssociation(
    name="type47",
    ends={
        Property(name="dbmodel_Type", type=dbmodel_Ltype, multiplicity=Multiplicity(1, 1)),
        Property(name="dbmodel_Ltype48", type=dbmodel_Type, multiplicity=Multiplicity(0, 1))
    }
)
part49: BinaryAssociation = BinaryAssociation(
    name="part49",
    ends={
        Property(name="dbmodel_Stype", type=dbmodel_StructOverride, multiplicity=Multiplicity(1, 1)),
        Property(name="dbmodel_StructOverride50", type=dbmodel_Stype, multiplicity=Multiplicity(0, 1))
    }
)
attr51: BinaryAssociation = BinaryAssociation(
    name="attr51",
    ends={
        Property(name="dbmodel_Attribute53", type=dbmodel_StructShare, multiplicity=Multiplicity(1, 1)),
        Property(name="dbmodel_StructShare52", type=dbmodel_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
logattr31: BinaryAssociation = BinaryAssociation(
    name="logattr31",
    ends={
        Property(name="dbmodel_Attribute32", type=dbmodel_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="dbmodel_Attribute30", type=dbmodel_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
pkeys33: BinaryAssociation = BinaryAssociation(
    name="pkeys33",
    ends={
        Property(name="dbmodel_Attribute35", type=dbmodel_Primkey, multiplicity=Multiplicity(1, 1)),
        Property(name="dbmodel_Primkey34", type=dbmodel_Attribute, multiplicity=Multiplicity(0, 9999))
    }
)
part54: BinaryAssociation = BinaryAssociation(
    name="part54",
    ends={
        Property(name="dbmodel_Stype56", type=dbmodel_StructShare, multiplicity=Multiplicity(1, 1)),
        Property(name="dbmodel_StructShare55", type=dbmodel_Stype, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_dbmodel_Class_ClassOrDuplicate = Generalization(general=ClassOrDuplicate, specific=dbmodel_Class)
gen_dbmodel_Duplicate_ClassOrDuplicate = Generalization(general=ClassOrDuplicate, specific=dbmodel_Duplicate)

# Domain Model
domain_model = DomainModel(
    name="dbmodel",
    types={dbmodel_Import, dbmodel_Subject, dbmodel_Class, dbmodel_Duplicate, ClassOrDuplicate, dbmodel_DbModel, dbmodel_Index, dbmodel_Pdb, dbmodel_Ltype, dbmodel_StructShare, dbmodel_StructOverride, dbmodel_Attribute, dbmodel_Primkey, dbmodel_IndexRef, dbmodel_Type, dbmodel_Stype, dbmodel_ClassOrDuplicate, KudaReplicate, PhysicalDatabase, Mtype, KudaType, KobeType, LockSchema},
    associations={imports0, subjects1, classes3, duplicates5, subject7, indices14, pdbs16, orig18, type21, forattr24, shrs26, ovride28, attributes10, primkey12, attrs36, index39, attr41, indices44, type47, part49, attr51, logattr31, pkeys33, part54},
    generalizations={gen_dbmodel_Class_ClassOrDuplicate, gen_dbmodel_Duplicate_ClassOrDuplicate},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)