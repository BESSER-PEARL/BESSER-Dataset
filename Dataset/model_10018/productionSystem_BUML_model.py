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
ProductionSystem_Raw = Class(name="ProductionSystem_Raw")
Piece = Class(name="Piece")
ProductionSystem_Processed = Class(name="ProductionSystem_Processed")
ProductionSystem_Machine = Class(name="ProductionSystem_Machine")
ProductionSystem_Conveyor = Class(name="ProductionSystem_Conveyor")
ProductionSystem_Piece = Class(name="ProductionSystem_Piece", is_abstract=True)

# ProductionSystem_Raw class attributes and methods

# Piece class attributes and methods

# ProductionSystem_Processed class attributes and methods

# ProductionSystem_Machine class attributes and methods
ProductionSystem_Machine_id: Property = Property(name="id", type=StringType)
ProductionSystem_Machine.attributes={ProductionSystem_Machine_id}

# ProductionSystem_Conveyor class attributes and methods
ProductionSystem_Conveyor_capacity: Property = Property(name="capacity", type=IntegerType)
ProductionSystem_Conveyor_id: Property = Property(name="id", type=StringType)
ProductionSystem_Conveyor.attributes={ProductionSystem_Conveyor_capacity, ProductionSystem_Conveyor_id}

# ProductionSystem_Piece class attributes and methods
ProductionSystem_Piece_id: Property = Property(name="id", type=StringType)
ProductionSystem_Piece.attributes={ProductionSystem_Piece_id}

# Relationships
ic0: BinaryAssociation = BinaryAssociation(
    name="ic0",
    ends={
        Property(name="Conveyor", type=ProductionSystem_Machine, multiplicity=Multiplicity(1, 1)),
        Property(name="om", type=ProductionSystem_Conveyor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
oc1: BinaryAssociation = BinaryAssociation(
    name="oc1",
    ends={
        Property(name="Conveyor2", type=ProductionSystem_Machine, multiplicity=Multiplicity(1, 1)),
        Property(name="im", type=ProductionSystem_Conveyor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
piece3: BinaryAssociation = BinaryAssociation(
    name="piece3",
    ends={
        Property(name="Piece", type=ProductionSystem_Conveyor, multiplicity=Multiplicity(1, 1)),
        Property(name="conveyor", type=ProductionSystem_Piece, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
next5: BinaryAssociation = BinaryAssociation(
    name="next5",
    ends={
        Property(name="Conveyor6", type=ProductionSystem_Conveyor, multiplicity=Multiplicity(1, 1)),
        Property(name="prev", type=ProductionSystem_Conveyor, multiplicity=Multiplicity(0, 9999))
    }
)
prev8: BinaryAssociation = BinaryAssociation(
    name="prev8",
    ends={
        Property(name="Conveyor9", type=ProductionSystem_Conveyor, multiplicity=Multiplicity(1, 1)),
        Property(name="next", type=ProductionSystem_Conveyor, multiplicity=Multiplicity(0, 1))
    }
)
im10: BinaryAssociation = BinaryAssociation(
    name="im10",
    ends={
        Property(name="Machine", type=ProductionSystem_Conveyor, multiplicity=Multiplicity(1, 1)),
        Property(name="oc", type=ProductionSystem_Machine, multiplicity=Multiplicity(0, 1))
    }
)
om11: BinaryAssociation = BinaryAssociation(
    name="om11",
    ends={
        Property(name="Machine12", type=ProductionSystem_Conveyor, multiplicity=Multiplicity(1, 1)),
        Property(name="ic", type=ProductionSystem_Machine, multiplicity=Multiplicity(0, 1))
    }
)
conveyor13: BinaryAssociation = BinaryAssociation(
    name="conveyor13",
    ends={
        Property(name="Conveyor14", type=ProductionSystem_Piece, multiplicity=Multiplicity(1, 1)),
        Property(name="piece", type=ProductionSystem_Conveyor, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_ProductionSystem_Raw_Piece = Generalization(general=Piece, specific=ProductionSystem_Raw)
gen_ProductionSystem_Processed_Piece = Generalization(general=Piece, specific=ProductionSystem_Processed)


# OCL Constraints
conveyorInv: Constraint = Constraint(
    name="conveyorInv",
    context=ProductionSystem_Conveyor,
    expression="context Conveyor inv: Conveyor.allInstances()->forAll(var | var.piece->size()<=var.capacity) and Piece.allInstances()->forAll(z| z.conveyor->size() =1)",
    language="OCL"
)

# Domain Model
domain_model = DomainModel(
    name="ProductionSystem",
    types={ProductionSystem_Raw, Piece, ProductionSystem_Processed, ProductionSystem_Machine, ProductionSystem_Conveyor, ProductionSystem_Piece},
    associations={ic0, oc1, piece3, next5, prev8, im10, om11, conveyor13},
    constraints={conveyorInv},
    generalizations={gen_ProductionSystem_Raw_Piece, gen_ProductionSystem_Processed_Piece},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)