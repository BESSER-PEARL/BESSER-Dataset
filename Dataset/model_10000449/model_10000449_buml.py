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
Forward = Class(name="Forward")
Backpropagation = Class(name="Backpropagation")
NeuralNetwork = Class(name="NeuralNetwork")
UpdateWeight = Class(name="UpdateWeight")

# Forward class attributes and methods
Forward_Input: Property = Property(name="Input", type=FloatType)
Forward_Weights: Property = Property(name="Weights", type=FloatType)
Forward_BiasesWeigths: Property = Property(name="BiasesWeigths", type=FloatType)
Forward.attributes={Forward_BiasesWeigths, Forward_Weights, Forward_Input}

# Backpropagation class attributes and methods
Backpropagation_output: Property = Property(name="output", type=FloatType)
Backpropagation_target: Property = Property(name="target", type=FloatType)
Backpropagation_Weigths: Property = Property(name="Weigths", type=FloatType)
Backpropagation_BiasesWeigths: Property = Property(name="BiasesWeigths", type=FloatType)
Backpropagation.attributes={Backpropagation_target, Backpropagation_output, Backpropagation_Weigths, Backpropagation_BiasesWeigths}

# NeuralNetwork class attributes and methods

# UpdateWeight class attributes and methods
UpdateWeight_Weights: Property = Property(name="Weights", type=FloatType)
UpdateWeight_BiasesWeigths: Property = Property(name="BiasesWeigths", type=FloatType)
UpdateWeight.attributes={UpdateWeight_BiasesWeigths, UpdateWeight_Weights}

# Relationships
WebUser_Customer: BinaryAssociation = BinaryAssociation(
    name="WebUser_Customer",
    ends={
        Property(name="forward0", type=Forward, multiplicity=Multiplicity(1, 1)),
        Property(name="neuralNetwork1", type=NeuralNetwork, multiplicity=Multiplicity(1, 1))
    }
)
ShoppingCart_LineItem: BinaryAssociation = BinaryAssociation(
    name="ShoppingCart_LineItem",
    ends={
        Property(name="updateWeigths2", type=UpdateWeight, multiplicity=Multiplicity(1, 1)),
        Property(name="backpropagation3", type=Backpropagation, multiplicity=Multiplicity(1, 1))
    }
)
Backpropagation_Forward: BinaryAssociation = BinaryAssociation(
    name="Backpropagation_Forward",
    ends={
        Property(name="forward4", type=Forward, multiplicity=Multiplicity(1, 1)),
        Property(name="backpropagation5", type=Backpropagation, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_37ec1d36_f11c_45e5_aee5_6de5d21adb09",
    types={Forward, Backpropagation, NeuralNetwork, UpdateWeight},
    associations={WebUser_Customer, ShoppingCart_LineItem, Backpropagation_Forward},
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