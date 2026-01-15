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
Datatype: Enumeration = Enumeration(
    name="Datatype",
    literals={
            EnumerationLiteral(name="STRING"),
			EnumerationLiteral(name="DATE"),
			EnumerationLiteral(name="FLOAT"),
			EnumerationLiteral(name="TIMESTAMP"),
			EnumerationLiteral(name="TEXT"),
			EnumerationLiteral(name="DECIMAL"),
			EnumerationLiteral(name="INT"),
			EnumerationLiteral(name="DOUBLE"),
			EnumerationLiteral(name="BOOLEAN"),
			EnumerationLiteral(name="DATETIME"),
			EnumerationLiteral(name="VARCHAR"),
			EnumerationLiteral(name="CHAR"),
			EnumerationLiteral(name="TINYTEXT"),
			EnumerationLiteral(name="BLOB"),
			EnumerationLiteral(name="LONGTEXT"),
			EnumerationLiteral(name="SMALLINT"),
			EnumerationLiteral(name="BIGINT")
    }
)

ConstraintType: Enumeration = Enumeration(
    name="ConstraintType",
    literals={
            EnumerationLiteral(name="FOREIGN_KEY"),
			EnumerationLiteral(name="UNIQUE"),
			EnumerationLiteral(name="COMPOSITE_PRIMARY_KEY"),
			EnumerationLiteral(name="PRIMARY_KEY")
    }
)

# Classes
metamodel_Constraint = Class(name="metamodel::Constraint")
metamodel_Database = Class(name="metamodel::Database")
metamodel_Table = Class(name="metamodel::Table")
metamodel_Sequence = Class(name="metamodel::Sequence")
metamodel_Column = Class(name="metamodel::Column")
metamodel_Row = Class(name="metamodel::Row")
metamodel_Cell = Class(name="metamodel::Cell")

# metamodel_Constraint class attributes and methods
metamodel_Constraint_name: Property = Property(name="name", type=StringType)
metamodel_Constraint_type: Property = Property(name="type", type=StringType)
metamodel_Constraint_reference: Property = Property(name="reference", type=StringType)
metamodel_Constraint.attributes={metamodel_Constraint_reference, metamodel_Constraint_name, metamodel_Constraint_type}

# metamodel_Database class attributes and methods
metamodel_Database_name: Property = Property(name="name", type=StringType)
metamodel_Database.attributes={metamodel_Database_name}

# metamodel_Table class attributes and methods
metamodel_Table_name: Property = Property(name="name", type=StringType)
metamodel_Table.attributes={metamodel_Table_name}

# metamodel_Sequence class attributes and methods
metamodel_Sequence_name: Property = Property(name="name", type=StringType)
metamodel_Sequence_minValue: Property = Property(name="minValue", type=IntegerType)
metamodel_Sequence_maxValue: Property = Property(name="maxValue", type=StringType)
metamodel_Sequence_incrementby: Property = Property(name="incrementby", type=IntegerType)
metamodel_Sequence_startwith: Property = Property(name="startwith", type=StringType)
metamodel_Sequence_currentValue: Property = Property(name="currentValue", type=StringType)
metamodel_Sequence_cycle: Property = Property(name="cycle", type=BooleanType)
metamodel_Sequence.attributes={metamodel_Sequence_maxValue, metamodel_Sequence_startwith, metamodel_Sequence_incrementby, metamodel_Sequence_cycle, metamodel_Sequence_name, metamodel_Sequence_minValue, metamodel_Sequence_currentValue}

# metamodel_Column class attributes and methods
metamodel_Column_name: Property = Property(name="name", type=StringType)
metamodel_Column_type: Property = Property(name="type", type=StringType)
metamodel_Column_nullable: Property = Property(name="nullable", type=BooleanType)
metamodel_Column_size: Property = Property(name="size", type=StringType)
metamodel_Column.attributes={metamodel_Column_nullable, metamodel_Column_name, metamodel_Column_type, metamodel_Column_size}

# metamodel_Row class attributes and methods

# metamodel_Cell class attributes and methods
metamodel_Cell_value: Property = Property(name="value", type=StringType)
metamodel_Cell.attributes={metamodel_Cell_value}

# Relationships
constraints3: BinaryAssociation = BinaryAssociation(
    name="constraints3",
    ends={
        Property(name="metamodel_Constraint", type=metamodel_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Table4", type=metamodel_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table0: BinaryAssociation = BinaryAssociation(
    name="table0",
    ends={
        Property(name="metamodel_Table", type=metamodel_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Database", type=metamodel_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sequences1: BinaryAssociation = BinaryAssociation(
    name="sequences1",
    ends={
        Property(name="metamodel_Sequence", type=metamodel_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Database2", type=metamodel_Sequence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns5: BinaryAssociation = BinaryAssociation(
    name="columns5",
    ends={
        Property(name="metamodel_Column", type=metamodel_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Table6", type=metamodel_Column, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
rows7: BinaryAssociation = BinaryAssociation(
    name="rows7",
    ends={
        Property(name="metamodel_Row", type=metamodel_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Table8", type=metamodel_Row, multiplicity=Multiplicity(0, 9999))
    }
)
References9: BinaryAssociation = BinaryAssociation(
    name="References9",
    ends={
        Property(name="metamodel_Column11", type=metamodel_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Constraint10", type=metamodel_Column, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
constraints12: BinaryAssociation = BinaryAssociation(
    name="constraints12",
    ends={
        Property(name="metamodel_Constraint14", type=metamodel_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Column13", type=metamodel_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cells15: BinaryAssociation = BinaryAssociation(
    name="cells15",
    ends={
        Property(name="metamodel_Cell", type=metamodel_Row, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Row16", type=metamodel_Cell, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
column17: BinaryAssociation = BinaryAssociation(
    name="column17",
    ends={
        Property(name="metamodel_Column19", type=metamodel_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Cell18", type=metamodel_Column, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="metamodel",
    types={metamodel_Constraint, metamodel_Database, metamodel_Table, metamodel_Sequence, metamodel_Column, metamodel_Row, metamodel_Cell, Datatype, ConstraintType},
    associations={constraints3, table0, sequences1, columns5, rows7, References9, constraints12, cells15, column17},
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