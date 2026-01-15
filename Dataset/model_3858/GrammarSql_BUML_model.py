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
grammarSql_Reference = Class(name="grammarSql::Reference")
grammarSql_Model = Class(name="grammarSql::Model")
grammarSql_Table = Class(name="grammarSql::Table")
grammarSql_EObject = Class(name="grammarSql::EObject")
grammarSql_Column = Class(name="grammarSql::Column")
grammarSql_PrimaryKey = Class(name="grammarSql::PrimaryKey")
grammarSql_ForeignKey = Class(name="grammarSql::ForeignKey")

# grammarSql_Reference class attributes and methods

# grammarSql_Model class attributes and methods

# grammarSql_Table class attributes and methods
grammarSql_Table_name: Property = Property(name="name", type=StringType)
grammarSql_Table.attributes={grammarSql_Table_name}

# grammarSql_EObject class attributes and methods

# grammarSql_Column class attributes and methods
grammarSql_Column_name: Property = Property(name="name", type=StringType)
grammarSql_Column_type: Property = Property(name="type", type=StringType)
grammarSql_Column_isNotNull: Property = Property(name="isNotNull", type=BooleanType)
grammarSql_Column.attributes={grammarSql_Column_name, grammarSql_Column_type, grammarSql_Column_isNotNull}

# grammarSql_PrimaryKey class attributes and methods

# grammarSql_ForeignKey class attributes and methods

# Relationships
localColumns4: BinaryAssociation = BinaryAssociation(
    name="localColumns4",
    ends={
        Property(name="grammarSql_ForeignKey", type=grammarSql_Column, multiplicity=Multiplicity(0, 9999)),
        Property(name="grammarSql_Column5", type=grammarSql_ForeignKey, multiplicity=Multiplicity(1, 1))
    }
)
ref6: BinaryAssociation = BinaryAssociation(
    name="ref6",
    ends={
        Property(name="grammarSql_Reference", type=grammarSql_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="grammarSql_ForeignKey7", type=grammarSql_Reference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fromT8: BinaryAssociation = BinaryAssociation(
    name="fromT8",
    ends={
        Property(name="grammarSql_Table10", type=grammarSql_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="grammarSql_Reference9", type=grammarSql_Table, multiplicity=Multiplicity(0, 9999))
    }
)
fromC11: BinaryAssociation = BinaryAssociation(
    name="fromC11",
    ends={
        Property(name="grammarSql_Column13", type=grammarSql_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="grammarSql_Reference12", type=grammarSql_Column, multiplicity=Multiplicity(0, 9999))
    }
)
tables0: BinaryAssociation = BinaryAssociation(
    name="tables0",
    ends={
        Property(name="grammarSql_Table", type=grammarSql_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="grammarSql_Model", type=grammarSql_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="grammarSql_EObject", type=grammarSql_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="grammarSql_Table2", type=grammarSql_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
col3: BinaryAssociation = BinaryAssociation(
    name="col3",
    ends={
        Property(name="grammarSql_Column", type=grammarSql_PrimaryKey, multiplicity=Multiplicity(1, 1)),
        Property(name="grammarSql_PrimaryKey", type=grammarSql_Column, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="grammarSql",
    types={grammarSql_Reference, grammarSql_Model, grammarSql_Table, grammarSql_EObject, grammarSql_Column, grammarSql_PrimaryKey, grammarSql_ForeignKey},
    associations={localColumns4, ref6, fromT8, fromC11, tables0, elements1, col3},
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