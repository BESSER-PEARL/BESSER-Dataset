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
Action: Enumeration = Enumeration(
    name="Action",
    literals={
            EnumerationLiteral(name="SET_DEFAULT"),
			EnumerationLiteral(name="CASCADE"),
			EnumerationLiteral(name="RESTRICT"),
			EnumerationLiteral(name="NO_ACTION"),
			EnumerationLiteral(name="SET_NULL")
    }
)

ReferencingType: Enumeration = Enumeration(
    name="ReferencingType",
    literals={
            EnumerationLiteral(name="DEFAULT"),
			EnumerationLiteral(name="PARTIAL"),
			EnumerationLiteral(name="FULL")
    }
)

DeferrableAct: Enumeration = Enumeration(
    name="DeferrableAct",
    literals={
            EnumerationLiteral(name="DEFFERABLE"),
			EnumerationLiteral(name="NOT_DEFFERABLE")
    }
)

DeferredAct: Enumeration = Enumeration(
    name="DeferredAct",
    literals={
            EnumerationLiteral(name="INITIALLY_IMMEDIATE"),
			EnumerationLiteral(name="INITIALLY_DEFERRED")
    }
)

# Classes
rdbms_SystemDataType = Class(name="rdbms::SystemDataType")
rdbms_Database = Class(name="rdbms::Database")
ModelElement = Class(name="ModelElement")
rdbms_UserDefinedDataType = Class(name="rdbms::UserDefinedDataType")
rdbms_Table = Class(name="rdbms::Table")
rdbms_ForeignKey = Class(name="rdbms::ForeignKey")
rdbms_PrimaryKeyCon = Class(name="rdbms::PrimaryKeyCon")
rdbms_UniqueCon = Class(name="rdbms::UniqueCon")
rdbms_Column = Class(name="rdbms::Column")
rdbms_CheckCon = Class(name="rdbms::CheckCon")
rdbms_PKeyAndUnique = Class(name="rdbms::PKeyAndUnique", is_abstract=True)
rdbms_DataType = Class(name="rdbms::DataType", is_abstract=True)
Constraints = Class(name="Constraints")
rdbms_Constraints = Class(name="rdbms::Constraints", is_abstract=True)
PKeyAndUnique = Class(name="PKeyAndUnique")
DataType = Class(name="DataType")
rdbms_ModelElement = Class(name="rdbms::ModelElement", is_abstract=True)

# rdbms_SystemDataType class attributes and methods
rdbms_SystemDataType_predefinedLength: Property = Property(name="predefinedLength", type=IntegerType)
rdbms_SystemDataType_predefinedDecPlaces: Property = Property(name="predefinedDecPlaces", type=IntegerType)
rdbms_SystemDataType.attributes={rdbms_SystemDataType_predefinedLength, rdbms_SystemDataType_predefinedDecPlaces}

# rdbms_Database class attributes and methods

# ModelElement class attributes and methods

# rdbms_UserDefinedDataType class attributes and methods
rdbms_UserDefinedDataType_precision: Property = Property(name="precision", type=IntegerType)
rdbms_UserDefinedDataType_length: Property = Property(name="length", type=IntegerType)
rdbms_UserDefinedDataType_defaultValue: Property = Property(name="defaultValue", type=StringType)
rdbms_UserDefinedDataType.attributes={rdbms_UserDefinedDataType_precision, rdbms_UserDefinedDataType_length, rdbms_UserDefinedDataType_defaultValue}

# rdbms_Table class attributes and methods

# rdbms_ForeignKey class attributes and methods
rdbms_ForeignKey_updateActionRHS: Property = Property(name="updateActionRHS", type=StringType)
rdbms_ForeignKey_deleteActionRHS: Property = Property(name="deleteActionRHS", type=StringType)
rdbms_ForeignKey_match: Property = Property(name="match", type=StringType)
rdbms_ForeignKey_inverseReferentialIntegrityCon: Property = Property(name="inverseReferentialIntegrityCon", type=BooleanType)
rdbms_ForeignKey.attributes={rdbms_ForeignKey_inverseReferentialIntegrityCon, rdbms_ForeignKey_deleteActionRHS, rdbms_ForeignKey_updateActionRHS, rdbms_ForeignKey_match}

# rdbms_PrimaryKeyCon class attributes and methods

# rdbms_UniqueCon class attributes and methods

# rdbms_Column class attributes and methods
rdbms_Column_default: Property = Property(name="default", type=StringType)
rdbms_Column_nullable: Property = Property(name="nullable", type=BooleanType)
rdbms_Column_precision: Property = Property(name="precision", type=IntegerType)
rdbms_Column_length: Property = Property(name="length", type=IntegerType)
rdbms_Column.attributes={rdbms_Column_default, rdbms_Column_precision, rdbms_Column_nullable, rdbms_Column_length}

# rdbms_CheckCon class attributes and methods
rdbms_CheckCon_checkCondition: Property = Property(name="checkCondition", type=StringType)
rdbms_CheckCon.attributes={rdbms_CheckCon_checkCondition}

# rdbms_PKeyAndUnique class attributes and methods

# rdbms_DataType class attributes and methods

# Constraints class attributes and methods

# rdbms_Constraints class attributes and methods
rdbms_Constraints_deferrable: Property = Property(name="deferrable", type=StringType)
rdbms_Constraints_deferred: Property = Property(name="deferred", type=StringType)
rdbms_Constraints.attributes={rdbms_Constraints_deferred, rdbms_Constraints_deferrable}

# PKeyAndUnique class attributes and methods

# DataType class attributes and methods

# rdbms_ModelElement class attributes and methods
rdbms_ModelElement_name: Property = Property(name="name", type=StringType)
rdbms_ModelElement.attributes={rdbms_ModelElement_name}

# Relationships
userDefinedDataTypes0: BinaryAssociation = BinaryAssociation(
    name="userDefinedDataTypes0",
    ends={
        Property(name="rdbms_UserDefinedDataType", type=rdbms_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_Database", type=rdbms_UserDefinedDataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tables1: BinaryAssociation = BinaryAssociation(
    name="tables1",
    ends={
        Property(name="rdbms_Table", type=rdbms_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_Database2", type=rdbms_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataTypes3: BinaryAssociation = BinaryAssociation(
    name="dataTypes3",
    ends={
        Property(name="rdbms_SystemDataType", type=rdbms_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_Database4", type=rdbms_SystemDataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tableFKs5: BinaryAssociation = BinaryAssociation(
    name="tableFKs5",
    ends={
        Property(name="ForeignKey", type=rdbms_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="FKTable", type=rdbms_ForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tablePK6: BinaryAssociation = BinaryAssociation(
    name="tablePK6",
    ends={
        Property(name="rdbms_PrimaryKeyCon", type=rdbms_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_Table7", type=rdbms_PrimaryKeyCon, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tableUQ8: BinaryAssociation = BinaryAssociation(
    name="tableUQ8",
    ends={
        Property(name="rdbms_UniqueCon", type=rdbms_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_Table9", type=rdbms_UniqueCon, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns10: BinaryAssociation = BinaryAssociation(
    name="columns10",
    ends={
        Property(name="rdbms_Column", type=rdbms_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_Table11", type=rdbms_Column, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
tableCHs12: BinaryAssociation = BinaryAssociation(
    name="tableCHs12",
    ends={
        Property(name="rdbms_CheckCon", type=rdbms_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_Table13", type=rdbms_CheckCon, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columnInPKandUQ14: BinaryAssociation = BinaryAssociation(
    name="columnInPKandUQ14",
    ends={
        Property(name="rdbms_PKeyAndUnique", type=rdbms_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_Column15", type=rdbms_PKeyAndUnique, multiplicity=Multiplicity(0, 1))
    }
)
columnInFK16: BinaryAssociation = BinaryAssociation(
    name="columnInFK16",
    ends={
        Property(name="rdbms_ForeignKey", type=rdbms_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_Column17", type=rdbms_ForeignKey, multiplicity=Multiplicity(0, 1))
    }
)
columnDataType18: BinaryAssociation = BinaryAssociation(
    name="columnDataType18",
    ends={
        Property(name="rdbms_DataType", type=rdbms_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_Column19", type=rdbms_DataType, multiplicity=Multiplicity(1, 1))
    }
)
rhsKey20: BinaryAssociation = BinaryAssociation(
    name="rhsKey20",
    ends={
        Property(name="rdbms_PKeyAndUnique22", type=rdbms_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_ForeignKey21", type=rdbms_PKeyAndUnique, multiplicity=Multiplicity(1, 1))
    }
)
lhsAttr23: BinaryAssociation = BinaryAssociation(
    name="lhsAttr23",
    ends={
        Property(name="rdbms_Column25", type=rdbms_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_ForeignKey24", type=rdbms_Column, multiplicity=Multiplicity(1, 9999))
    }
)
refersTo26: BinaryAssociation = BinaryAssociation(
    name="refersTo26",
    ends={
        Property(name="rdbms_Table28", type=rdbms_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_ForeignKey27", type=rdbms_Table, multiplicity=Multiplicity(1, 1))
    }
)
FKTable29: BinaryAssociation = BinaryAssociation(
    name="FKTable29",
    ends={
        Property(name="Table", type=rdbms_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="tableFKs", type=rdbms_Table, multiplicity=Multiplicity(1, 1))
    }
)
PKandUQColumns30: BinaryAssociation = BinaryAssociation(
    name="PKandUQColumns30",
    ends={
        Property(name="rdbms_Column32", type=rdbms_PKeyAndUnique, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_PKeyAndUnique31", type=rdbms_Column, multiplicity=Multiplicity(1, 9999))
    }
)
dataType33: BinaryAssociation = BinaryAssociation(
    name="dataType33",
    ends={
        Property(name="rdbms_SystemDataType35", type=rdbms_UserDefinedDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_UserDefinedDataType34", type=rdbms_SystemDataType, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_rdbms_Database_ModelElement = Generalization(general=ModelElement, specific=rdbms_Database)
gen_rdbms_Table_ModelElement = Generalization(general=ModelElement, specific=rdbms_Table)
gen_rdbms_Column_ModelElement = Generalization(general=ModelElement, specific=rdbms_Column)
gen_rdbms_ForeignKey_Constraints = Generalization(general=Constraints, specific=rdbms_ForeignKey)
gen_rdbms_Constraints_ModelElement = Generalization(general=ModelElement, specific=rdbms_Constraints)
gen_rdbms_CheckCon_Constraints = Generalization(general=Constraints, specific=rdbms_CheckCon)
gen_rdbms_PKeyAndUnique_Constraints = Generalization(general=Constraints, specific=rdbms_PKeyAndUnique)
gen_rdbms_PrimaryKeyCon_PKeyAndUnique = Generalization(general=PKeyAndUnique, specific=rdbms_PrimaryKeyCon)
gen_rdbms_UniqueCon_PKeyAndUnique = Generalization(general=PKeyAndUnique, specific=rdbms_UniqueCon)
gen_rdbms_SystemDataType_DataType = Generalization(general=DataType, specific=rdbms_SystemDataType)
gen_rdbms_UserDefinedDataType_DataType = Generalization(general=DataType, specific=rdbms_UserDefinedDataType)
gen_rdbms_DataType_ModelElement = Generalization(general=ModelElement, specific=rdbms_DataType)

# Domain Model
domain_model = DomainModel(
    name="rdbms",
    types={rdbms_SystemDataType, rdbms_Database, ModelElement, rdbms_UserDefinedDataType, rdbms_Table, rdbms_ForeignKey, rdbms_PrimaryKeyCon, rdbms_UniqueCon, rdbms_Column, rdbms_CheckCon, rdbms_PKeyAndUnique, rdbms_DataType, Constraints, rdbms_Constraints, PKeyAndUnique, DataType, rdbms_ModelElement, Action, ReferencingType, DeferrableAct, DeferredAct},
    associations={userDefinedDataTypes0, tables1, dataTypes3, tableFKs5, tablePK6, tableUQ8, columns10, tableCHs12, columnInPKandUQ14, columnInFK16, columnDataType18, rhsKey20, lhsAttr23, refersTo26, FKTable29, PKandUQColumns30, dataType33},
    generalizations={gen_rdbms_Database_ModelElement, gen_rdbms_Table_ModelElement, gen_rdbms_Column_ModelElement, gen_rdbms_ForeignKey_Constraints, gen_rdbms_Constraints_ModelElement, gen_rdbms_CheckCon_Constraints, gen_rdbms_PKeyAndUnique_Constraints, gen_rdbms_PrimaryKeyCon_PKeyAndUnique, gen_rdbms_UniqueCon_PKeyAndUnique, gen_rdbms_SystemDataType_DataType, gen_rdbms_UserDefinedDataType_DataType, gen_rdbms_DataType_ModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)