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
SDBEngine: Enumeration = Enumeration(
    name="SDBEngine",
    literals={
            EnumerationLiteral(name="INNODB"),
			EnumerationLiteral(name="MYISAM")
    }
)

SSimpleTypes: Enumeration = Enumeration(
    name="SSimpleTypes",
    literals={
            EnumerationLiteral(name="INT"),
			EnumerationLiteral(name="TINY_INT"),
			EnumerationLiteral(name="SMALL_INT"),
			EnumerationLiteral(name="FOTO"),
			EnumerationLiteral(name="Currency"),
			EnumerationLiteral(name="Coordinate"),
			EnumerationLiteral(name="MEDIUM_INT"),
			EnumerationLiteral(name="BOOLEAN"),
			EnumerationLiteral(name="BLOB"),
			EnumerationLiteral(name="DATETIME"),
			EnumerationLiteral(name="DATE"),
			EnumerationLiteral(name="TIME"),
			EnumerationLiteral(name="POLYGON"),
			EnumerationLiteral(name="POINT")
    }
)

SIndex: Enumeration = Enumeration(
    name="SIndex",
    literals={
            EnumerationLiteral(name="NO"),
			EnumerationLiteral(name="YES"),
			EnumerationLiteral(name="UNIQUE"),
			EnumerationLiteral(name="SPATIAL")
    }
)

# Classes
sqlDSL_SArtifact = Class(name="sqlDSL_SArtifact")
sqlDSL_SModel = Class(name="sqlDSL_SModel")
sqlDSL_SSettings = Class(name="sqlDSL_SSettings")
sqlDSL_STableMember = Class(name="sqlDSL_STableMember")
sqlDSL_SColumnProps = Class(name="sqlDSL_SColumnProps")
sqlDSL_SColumn = Class(name="sqlDSL_SColumn")
STableMember = Class(name="STableMember")
sqlDSL_SExtDeclaredSQLType = Class(name="sqlDSL_SExtDeclaredSQLType")
sqlDSL_STable = Class(name="sqlDSL_STable")
SArtifact = Class(name="SArtifact")
sqlDSL_SInlinedSQLType = Class(name="sqlDSL_SInlinedSQLType")
sqlDSL_SJoinColumn = Class(name="sqlDSL_SJoinColumn")
sqlDSL_SEnum = Class(name="sqlDSL_SEnum")
SExtDeclaredSQLType = Class(name="SExtDeclaredSQLType")
sqlDSL_SEnumLiteral = Class(name="sqlDSL_SEnumLiteral")
sqlDSL_SString = Class(name="sqlDSL_SString")
SInlinedSQLType = Class(name="SInlinedSQLType")
sqlDSL_SDecimal = Class(name="sqlDSL_SDecimal")

# sqlDSL_SArtifact class attributes and methods
sqlDSL_SArtifact_name: Property = Property(name="name", type=StringType)
sqlDSL_SArtifact.attributes={sqlDSL_SArtifact_name}

# sqlDSL_SModel class attributes and methods
sqlDSL_SModel_generatedFile: Property = Property(name="generatedFile", type=StringType)
sqlDSL_SModel.attributes={sqlDSL_SModel_generatedFile}

# sqlDSL_SSettings class attributes and methods
sqlDSL_SSettings_schema: Property = Property(name="schema", type=StringType)
sqlDSL_SSettings_javapackage: Property = Property(name="javapackage", type=StringType)
sqlDSL_SSettings_engine: Property = Property(name="engine", type=StringType)
sqlDSL_SSettings.attributes={sqlDSL_SSettings_javapackage, sqlDSL_SSettings_schema, sqlDSL_SSettings_engine}

# sqlDSL_STableMember class attributes and methods
sqlDSL_STableMember_name: Property = Property(name="name", type=StringType)
sqlDSL_STableMember.attributes={sqlDSL_STableMember_name}

# sqlDSL_SColumnProps class attributes and methods
sqlDSL_SColumnProps_nullable: Property = Property(name="nullable", type=BooleanType)
sqlDSL_SColumnProps_aes: Property = Property(name="aes", type=BooleanType)
sqlDSL_SColumnProps_index: Property = Property(name="index", type=StringType)
sqlDSL_SColumnProps_javacolumn: Property = Property(name="javacolumn", type=StringType)
sqlDSL_SColumnProps.attributes={sqlDSL_SColumnProps_nullable, sqlDSL_SColumnProps_javacolumn, sqlDSL_SColumnProps_aes, sqlDSL_SColumnProps_index}

# sqlDSL_SColumn class attributes and methods
sqlDSL_SColumn_simpleType: Property = Property(name="simpleType", type=StringType)
sqlDSL_SColumn.attributes={sqlDSL_SColumn_simpleType}

# STableMember class attributes and methods

# sqlDSL_SExtDeclaredSQLType class attributes and methods

# sqlDSL_STable class attributes and methods
sqlDSL_STable_cached: Property = Property(name="cached", type=BooleanType)
sqlDSL_STable_prefix: Property = Property(name="prefix", type=StringType)
sqlDSL_STable_entityname: Property = Property(name="entityname", type=StringType)
sqlDSL_STable.attributes={sqlDSL_STable_cached, sqlDSL_STable_prefix, sqlDSL_STable_entityname}

# SArtifact class attributes and methods

# sqlDSL_SInlinedSQLType class attributes and methods
sqlDSL_SInlinedSQLType_value: Property = Property(name="value", type=IntegerType)
sqlDSL_SInlinedSQLType.attributes={sqlDSL_SInlinedSQLType_value}

# sqlDSL_SJoinColumn class attributes and methods

# sqlDSL_SEnum class attributes and methods

# SExtDeclaredSQLType class attributes and methods

# sqlDSL_SEnumLiteral class attributes and methods
sqlDSL_SEnumLiteral_name: Property = Property(name="name", type=StringType)
sqlDSL_SEnumLiteral_value: Property = Property(name="value", type=IntegerType)
sqlDSL_SEnumLiteral.attributes={sqlDSL_SEnumLiteral_name, sqlDSL_SEnumLiteral_value}

# sqlDSL_SString class attributes and methods

# SInlinedSQLType class attributes and methods

# sqlDSL_SDecimal class attributes and methods

# Relationships
settings0: BinaryAssociation = BinaryAssociation(
    name="settings0",
    ends={
        Property(name="sqlDSL_SSettings", type=sqlDSL_SModel, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlDSL_SModel", type=sqlDSL_SSettings, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
artifact1: BinaryAssociation = BinaryAssociation(
    name="artifact1",
    ends={
        Property(name="sqlDSL_SArtifact", type=sqlDSL_SModel, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlDSL_SModel2", type=sqlDSL_SArtifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns5: BinaryAssociation = BinaryAssociation(
    name="columns5",
    ends={
        Property(name="sqlDSL_STableMember", type=sqlDSL_STable, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlDSL_STable6", type=sqlDSL_STableMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
props7: BinaryAssociation = BinaryAssociation(
    name="props7",
    ends={
        Property(name="sqlDSL_SColumnProps", type=sqlDSL_STableMember, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlDSL_STableMember8", type=sqlDSL_SColumnProps, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extType9: BinaryAssociation = BinaryAssociation(
    name="extType9",
    ends={
        Property(name="sqlDSL_SExtDeclaredSQLType", type=sqlDSL_SColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlDSL_SColumn", type=sqlDSL_SExtDeclaredSQLType, multiplicity=Multiplicity(0, 1))
    }
)
settings3: BinaryAssociation = BinaryAssociation(
    name="settings3",
    ends={
        Property(name="sqlDSL_SSettings4", type=sqlDSL_STable, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlDSL_STable", type=sqlDSL_SSettings, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referencedType12: BinaryAssociation = BinaryAssociation(
    name="referencedType12",
    ends={
        Property(name="sqlDSL_STable13", type=sqlDSL_SJoinColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlDSL_SJoinColumn", type=sqlDSL_STable, multiplicity=Multiplicity(0, 1))
    }
)
inlinedType10: BinaryAssociation = BinaryAssociation(
    name="inlinedType10",
    ends={
        Property(name="sqlDSL_SInlinedSQLType", type=sqlDSL_SColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlDSL_SColumn11", type=sqlDSL_SInlinedSQLType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
literals14: BinaryAssociation = BinaryAssociation(
    name="literals14",
    ends={
        Property(name="sqlDSL_SEnumLiteral", type=sqlDSL_SEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlDSL_SEnum", type=sqlDSL_SEnumLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_sqlDSL_SColumn_STableMember = Generalization(general=STableMember, specific=sqlDSL_SColumn)
gen_sqlDSL_STable_SArtifact = Generalization(general=SArtifact, specific=sqlDSL_STable)
gen_sqlDSL_SJoinColumn_STableMember = Generalization(general=STableMember, specific=sqlDSL_SJoinColumn)
gen_sqlDSL_SEnum_SArtifact = Generalization(general=SArtifact, specific=sqlDSL_SEnum)
gen_sqlDSL_SEnum_SExtDeclaredSQLType = Generalization(general=SExtDeclaredSQLType, specific=sqlDSL_SEnum)
gen_sqlDSL_SString_SInlinedSQLType = Generalization(general=SInlinedSQLType, specific=sqlDSL_SString)
gen_sqlDSL_SDecimal_SInlinedSQLType = Generalization(general=SInlinedSQLType, specific=sqlDSL_SDecimal)

# Domain Model
domain_model = DomainModel(
    name="sqlDSL",
    types={sqlDSL_SArtifact, sqlDSL_SModel, sqlDSL_SSettings, sqlDSL_STableMember, sqlDSL_SColumnProps, sqlDSL_SColumn, STableMember, sqlDSL_SExtDeclaredSQLType, sqlDSL_STable, SArtifact, sqlDSL_SInlinedSQLType, sqlDSL_SJoinColumn, sqlDSL_SEnum, SExtDeclaredSQLType, sqlDSL_SEnumLiteral, sqlDSL_SString, SInlinedSQLType, sqlDSL_SDecimal, SDBEngine, SSimpleTypes, SIndex},
    associations={settings0, artifact1, columns5, props7, extType9, settings3, referencedType12, inlinedType10, literals14},
    generalizations={gen_sqlDSL_SColumn_STableMember, gen_sqlDSL_STable_SArtifact, gen_sqlDSL_SJoinColumn_STableMember, gen_sqlDSL_SEnum_SArtifact, gen_sqlDSL_SEnum_SExtDeclaredSQLType, gen_sqlDSL_SString_SInlinedSQLType, gen_sqlDSL_SDecimal_SInlinedSQLType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)