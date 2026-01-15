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
model_Table = Class(name="model::Table")
model_Column = Class(name="model::Column")
model_Diagram = Class(name="model::Diagram")
model_Constraint = Class(name="model::Constraint")

# model_Table class attributes and methods
model_Table_name: Property = Property(name="name", type=StringType)
model_Table.attributes={model_Table_name}

# model_Column class attributes and methods
model_Column_name: Property = Property(name="name", type=StringType)
model_Column.attributes={model_Column_name}

# model_Diagram class attributes and methods

# model_Constraint class attributes and methods

# Relationships
columns0: BinaryAssociation = BinaryAssociation(
    name="columns0",
    ends={
        Property(name="model_Column", type=model_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Table", type=model_Column, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
TableDiagram6: BinaryAssociation = BinaryAssociation(
    name="TableDiagram6",
    ends={
        Property(name="model_Table7", type=model_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Diagram", type=model_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Source8: BinaryAssociation = BinaryAssociation(
    name="Source8",
    ends={
        Property(name="model_Table10", type=model_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Constraint9", type=model_Table, multiplicity=Multiplicity(0, 1))
    }
)
Target11: BinaryAssociation = BinaryAssociation(
    name="Target11",
    ends={
        Property(name="model_Table13", type=model_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Constraint12", type=model_Table, multiplicity=Multiplicity(0, 1))
    }
)
sourceConstraints1: BinaryAssociation = BinaryAssociation(
    name="sourceConstraints1",
    ends={
        Property(name="model_Constraint", type=model_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Table2", type=model_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetConstraint3: BinaryAssociation = BinaryAssociation(
    name="targetConstraint3",
    ends={
        Property(name="model_Constraint5", type=model_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Table4", type=model_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_Table, model_Column, model_Diagram, model_Constraint},
    associations={columns0, TableDiagram6, Source8, Target11, sourceConstraints1, targetConstraint3},
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