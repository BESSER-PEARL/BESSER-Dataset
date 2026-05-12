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
mmb_Model = Class(name="mmb_Model")
mmb_Automaton = Class(name="mmb_Automaton")
mmb_Mode = Class(name="mmb_Mode")
mmb_Transition = Class(name="mmb_Transition")
mmb_Modification = Class(name="mmb_Modification")

# mmb_Model class attributes and methods
mmb_Model_Name: Property = Property(name="Name", type=StringType)
mmb_Model.attributes={mmb_Model_Name}

# mmb_Automaton class attributes and methods
mmb_Automaton_Name: Property = Property(name="Name", type=StringType)
mmb_Automaton.attributes={mmb_Automaton_Name}

# mmb_Mode class attributes and methods
mmb_Mode_Name: Property = Property(name="Name", type=StringType)
mmb_Mode_InitialState: Property = Property(name="InitialState", type=BooleanType)
mmb_Mode_Shape: Property = Property(name="Shape", type=StringType)
mmb_Mode_Dimension: Property = Property(name="Dimension", type=FloatType)
mmb_Mode.attributes={mmb_Mode_Shape, mmb_Mode_Name, mmb_Mode_Dimension, mmb_Mode_InitialState}

# mmb_Transition class attributes and methods
mmb_Transition_Event: Property = Property(name="Event", type=StringType)
mmb_Transition.attributes={mmb_Transition_Event}

# mmb_Modification class attributes and methods
mmb_Modification_VarName: Property = Property(name="VarName", type=StringType)
mmb_Modification_VarType: Property = Property(name="VarType", type=StringType)
mmb_Modification.attributes={mmb_Modification_VarType, mmb_Modification_VarName}

# Relationships
automata0: BinaryAssociation = BinaryAssociation(
    name="automata0",
    ends={
        Property(name="mmb_Automaton", type=mmb_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="mmb_Model", type=mmb_Automaton, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
targetMode10: BinaryAssociation = BinaryAssociation(
    name="targetMode10",
    ends={
        Property(name="mmb_Mode12", type=mmb_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="mmb_Transition11", type=mmb_Mode, multiplicity=Multiplicity(1, 1))
    }
)
modes1: BinaryAssociation = BinaryAssociation(
    name="modes1",
    ends={
        Property(name="mmb_Mode", type=mmb_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="mmb_Automaton2", type=mmb_Mode, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
transistions3: BinaryAssociation = BinaryAssociation(
    name="transistions3",
    ends={
        Property(name="mmb_Transition", type=mmb_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="mmb_Automaton4", type=mmb_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Modifications5: BinaryAssociation = BinaryAssociation(
    name="Modifications5",
    ends={
        Property(name="mmb_Modification", type=mmb_Mode, multiplicity=Multiplicity(1, 1)),
        Property(name="mmb_Mode6", type=mmb_Modification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceMode7: BinaryAssociation = BinaryAssociation(
    name="sourceMode7",
    ends={
        Property(name="mmb_Mode9", type=mmb_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="mmb_Transition8", type=mmb_Mode, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="mmb",
    types={mmb_Model, mmb_Automaton, mmb_Mode, mmb_Transition, mmb_Modification},
    associations={automata0, targetMode10, modes1, transistions3, Modifications5, sourceMode7},
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