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
datasetload_TableGroup = Class(name="datasetload_TableGroup", is_abstract=True)
datasetload_Table = Class(name="datasetload_Table", is_abstract=True)
datasetload_DataSource = Class(name="datasetload_DataSource", is_abstract=True)
datasetload_DataSourceJdbc = Class(name="datasetload_DataSourceJdbc")
DataSource = Class(name="DataSource")
datasetload_TableRow = Class(name="datasetload_TableRow", is_abstract=True)

# datasetload_TableGroup class attributes and methods
datasetload_TableGroup_Name: Property = Property(name="Name", type=StringType)
datasetload_TableGroup_m_load: Method = Method(name="load", parameters={})
datasetload_TableGroup_m_refresh: Method = Method(name="refresh", parameters={})
datasetload_TableGroup.attributes={datasetload_TableGroup_Name}
datasetload_TableGroup.methods={datasetload_TableGroup_m_refresh, datasetload_TableGroup_m_load}

# datasetload_Table class attributes and methods
datasetload_Table_Name: Property = Property(name="Name", type=StringType)
datasetload_Table_ParamTableGroupAttributes: Property = Property(name="ParamTableGroupAttributes", type=StringType)
datasetload_Table_SQLStatement: Property = Property(name="SQLStatement", type=StringType)
datasetload_Table_ColumnTableRowAttributes: Property = Property(name="ColumnTableRowAttributes", type=StringType)
datasetload_Table_KeyColumns: Property = Property(name="KeyColumns", type=IntegerType)
datasetload_Table_LastLoad: Property = Property(name="LastLoad", type=DateType)
datasetload_Table_NumberOfRows: Property = Property(name="NumberOfRows", type=IntegerType)
datasetload_Table_m_load: Method = Method(name="load", parameters={})
datasetload_Table_m_newRow: Method = Method(name="newRow", parameters={}, type=StringType)
datasetload_Table_m_addRow: Method = Method(name="addRow", parameters={Parameter(name='datasetload_row', type=StringType)})
datasetload_Table_m_getRow: Method = Method(name="getRow", parameters={Parameter(name='datasetload_key', type=StringType)}, type=StringType)
datasetload_Table_m_removeRow: Method = Method(name="removeRow", parameters={Parameter(name='datasetload_row', type=StringType)})
datasetload_Table_m_refresh: Method = Method(name="refresh", parameters={})
datasetload_Table.attributes={datasetload_Table_NumberOfRows, datasetload_Table_Name, datasetload_Table_ParamTableGroupAttributes, datasetload_Table_ColumnTableRowAttributes, datasetload_Table_SQLStatement, datasetload_Table_KeyColumns, datasetload_Table_LastLoad}
datasetload_Table.methods={datasetload_Table_m_refresh, datasetload_Table_m_addRow, datasetload_Table_m_newRow, datasetload_Table_m_getRow, datasetload_Table_m_removeRow, datasetload_Table_m_load}

# datasetload_DataSource class attributes and methods
datasetload_DataSource_Name: Property = Property(name="Name", type=StringType)
datasetload_DataSource_Connected: Property = Property(name="Connected", type=BooleanType)
datasetload_DataSource_m_connect: Method = Method(name="connect", parameters={})
datasetload_DataSource_m_disconnect: Method = Method(name="disconnect", parameters={})
datasetload_DataSource_m_loadTableImpl: Method = Method(name="loadTableImpl", parameters={Parameter(name='datasetload_table', type=StringType)})
datasetload_DataSource.attributes={datasetload_DataSource_Name, datasetload_DataSource_Connected}
datasetload_DataSource.methods={datasetload_DataSource_m_disconnect, datasetload_DataSource_m_connect, datasetload_DataSource_m_loadTableImpl}

# datasetload_DataSourceJdbc class attributes and methods
datasetload_DataSourceJdbc_DataBaseUser: Property = Property(name="DataBaseUser", type=StringType)
datasetload_DataSourceJdbc_DataBaseUserPwd: Property = Property(name="DataBaseUserPwd", type=StringType)
datasetload_DataSourceJdbc_DefaultSchema: Property = Property(name="DefaultSchema", type=StringType)
datasetload_DataSourceJdbc.attributes={datasetload_DataSourceJdbc_DataBaseUserPwd, datasetload_DataSourceJdbc_DataBaseUser, datasetload_DataSourceJdbc_DefaultSchema}

# DataSource class attributes and methods

# datasetload_TableRow class attributes and methods
datasetload_TableRow_Key: Property = Property(name="Key", type=StringType)
datasetload_TableRow_NewRow: Property = Property(name="NewRow", type=BooleanType)
datasetload_TableRow_RowNumber: Property = Property(name="RowNumber", type=IntegerType)
datasetload_TableRow_m_refresh: Method = Method(name="refresh", parameters={})
datasetload_TableRow.attributes={datasetload_TableRow_NewRow, datasetload_TableRow_Key, datasetload_TableRow_RowNumber}
datasetload_TableRow.methods={datasetload_TableRow_m_refresh}

# Relationships
Tables0: BinaryAssociation = BinaryAssociation(
    name="Tables0",
    ends={
        Property(name="datasetload_Table", type=datasetload_TableGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="datasetload_TableGroup", type=datasetload_Table, multiplicity=Multiplicity(0, 9999))
    }
)
DataSource1: BinaryAssociation = BinaryAssociation(
    name="DataSource1",
    ends={
        Property(name="datasetload_DataSource", type=datasetload_TableGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="datasetload_TableGroup2", type=datasetload_DataSource, multiplicity=Multiplicity(0, 1))
    }
)
TableGroup3: BinaryAssociation = BinaryAssociation(
    name="TableGroup3",
    ends={
        Property(name="datasetload_TableGroup5", type=datasetload_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="datasetload_Table4", type=datasetload_TableGroup, multiplicity=Multiplicity(1, 1))
    }
)
Rows6: BinaryAssociation = BinaryAssociation(
    name="Rows6",
    ends={
        Property(name="datasetload_TableRow", type=datasetload_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="datasetload_Table7", type=datasetload_TableRow, multiplicity=Multiplicity(0, 9999))
    }
)
Table8: BinaryAssociation = BinaryAssociation(
    name="Table8",
    ends={
        Property(name="datasetload_Table10", type=datasetload_TableRow, multiplicity=Multiplicity(1, 1)),
        Property(name="datasetload_TableRow9", type=datasetload_Table, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_datasetload_DataSourceJdbc_DataSource = Generalization(general=DataSource, specific=datasetload_DataSourceJdbc)

# Domain Model
domain_model = DomainModel(
    name="datasetload",
    types={datasetload_TableGroup, datasetload_Table, datasetload_DataSource, datasetload_DataSourceJdbc, DataSource, datasetload_TableRow},
    associations={Tables0, DataSource1, TableGroup3, Rows6, Table8},
    generalizations={gen_datasetload_DataSourceJdbc_DataSource},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)