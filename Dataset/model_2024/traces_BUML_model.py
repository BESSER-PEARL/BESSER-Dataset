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
traces_SimulatorRun = Class(name="traces::SimulatorRun")
traces_Variable = Class(name="traces::Variable")
traces_Value = Class(name="traces::Value")

# traces_SimulatorRun class attributes and methods
traces_SimulatorRun_id: Property = Property(name="id", type=IntegerType)
traces_SimulatorRun_timestamp: Property = Property(name="timestamp", type=DateType)
traces_SimulatorRun_behaviorName: Property = Property(name="behaviorName", type=StringType)
traces_SimulatorRun.attributes={traces_SimulatorRun_behaviorName, traces_SimulatorRun_timestamp, traces_SimulatorRun_id}

# traces_Variable class attributes and methods
traces_Variable_name: Property = Property(name="name", type=StringType)
traces_Variable.attributes={traces_Variable_name}

# traces_Value class attributes and methods
traces_Value_clockMin: Property = Property(name="clockMin", type=FloatType)
traces_Value_clockMax: Property = Property(name="clockMax", type=FloatType)
traces_Value_valueMin: Property = Property(name="valueMin", type=FloatType)
traces_Value_valueMax: Property = Property(name="valueMax", type=FloatType)
traces_Value.attributes={traces_Value_clockMax, traces_Value_valueMax, traces_Value_clockMin, traces_Value_valueMin}

# Relationships
variables0: BinaryAssociation = BinaryAssociation(
    name="variables0",
    ends={
        Property(name="Variable", type=traces_SimulatorRun, multiplicity=Multiplicity(1, 1)),
        Property(name="run", type=traces_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
run1: BinaryAssociation = BinaryAssociation(
    name="run1",
    ends={
        Property(name="SimulatorRun", type=traces_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="variables", type=traces_SimulatorRun, multiplicity=Multiplicity(1, 1))
    }
)
values2: BinaryAssociation = BinaryAssociation(
    name="values2",
    ends={
        Property(name="Value", type=traces_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="variable", type=traces_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable3: BinaryAssociation = BinaryAssociation(
    name="variable3",
    ends={
        Property(name="Variable4", type=traces_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="values", type=traces_Variable, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="traces",
    types={traces_SimulatorRun, traces_Variable, traces_Value},
    associations={variables0, run1, values2, variable3},
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