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
DML_InsertsStatements = Class(name="DML::InsertsStatements")
DML_InsertInto = Class(name="DML::InsertInto")
DML_Registry = Class(name="DML::Registry")
DML_Column = Class(name="DML::Column")
DML_Value = Class(name="DML::Value")

# DML_InsertsStatements class attributes and methods

# DML_InsertInto class attributes and methods
DML_InsertInto_tableName: Property = Property(name="tableName", type=StringType)
DML_InsertInto.attributes={DML_InsertInto_tableName}

# DML_Registry class attributes and methods

# DML_Column class attributes and methods
DML_Column_columnName: Property = Property(name="columnName", type=StringType)
DML_Column.attributes={DML_Column_columnName}

# DML_Value class attributes and methods
DML_Value_value: Property = Property(name="value", type=StringType)
DML_Value.attributes={DML_Value_value}

# Relationships
insertsInto0: BinaryAssociation = BinaryAssociation(
    name="insertsInto0",
    ends={
        Property(name="DML_InsertInto", type=DML_InsertsStatements, multiplicity=Multiplicity(1, 1)),
        Property(name="DML_InsertsStatements", type=DML_InsertInto, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
registry1: BinaryAssociation = BinaryAssociation(
    name="registry1",
    ends={
        Property(name="DML_Registry", type=DML_InsertInto, multiplicity=Multiplicity(1, 1)),
        Property(name="DML_InsertInto2", type=DML_Registry, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
columns3: BinaryAssociation = BinaryAssociation(
    name="columns3",
    ends={
        Property(name="DML_Column", type=DML_InsertInto, multiplicity=Multiplicity(1, 1)),
        Property(name="DML_InsertInto4", type=DML_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
registryValues5: BinaryAssociation = BinaryAssociation(
    name="registryValues5",
    ends={
        Property(name="DML_Value", type=DML_Registry, multiplicity=Multiplicity(1, 1)),
        Property(name="DML_Registry6", type=DML_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
column7: BinaryAssociation = BinaryAssociation(
    name="column7",
    ends={
        Property(name="DML_Column9", type=DML_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="DML_Value8", type=DML_Column, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DML",
    types={DML_InsertsStatements, DML_InsertInto, DML_Registry, DML_Column, DML_Value},
    associations={insertsInto0, registry1, columns3, registryValues5, column7},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)