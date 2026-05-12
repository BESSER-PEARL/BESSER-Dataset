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
Model = Class(name="Model")
felhaszn_l__Actor = Class(name="felhaszn_l__Actor")
LoadGameWidget = Class(name="LoadGameWidget")
SaveGameWidget = Class(name="SaveGameWidget")
Class_ = Class(name="Class")
Persistence = Class(name="Persistence")

# Model class attributes and methods
Model_gameTable: Property = Property(name="gameTable", type=StringType)
Model_gameSize: Property = Property(name="gameSize", type=StringType)
Model_steps: Property = Property(name="steps", type=StringType)
Model_playerNr: Property = Property(name="playerNr", type=StringType)
Model_gameOver: Property = Property(name="gameOver", type=BooleanType)
Model_pl1points: Property = Property(name="pl1points", type=StringType)
Model_pl2points: Property = Property(name="pl2points", type=StringType)
Model_selected: Property = Property(name="selected", type=StringType)
Model_goodselected: Property = Property(name="goodselected", type=BooleanType)
Model_pl1: Property = Property(name="pl1", type=StringType)
Model_pl2: Property = Property(name="pl2", type=StringType)
Model.attributes={Model_gameOver, Model_pl2, Model_goodselected, Model_pl1, Model_pl1points, Model_selected, Model_gameTable, Model_pl2points, Model_gameSize, Model_steps, Model_playerNr}

# felhaszn_l__Actor class attributes and methods

# LoadGameWidget class attributes and methods

# SaveGameWidget class attributes and methods
SaveGameWidget_okButton: Property = Property(name="okButton", type=StringType)
SaveGameWidget_cancelButton: Property = Property(name="cancelButton", type=StringType)
SaveGameWidget__listWidget: Property = Property(name="_listWidget", type=StringType)
SaveGameWidget.attributes={SaveGameWidget_cancelButton, SaveGameWidget_okButton, SaveGameWidget__listWidget}

# Class class attributes and methods

# Persistence class attributes and methods

# Relationships
Class_Model: BinaryAssociation = BinaryAssociation(
    name="Class_Model",
    ends={
        Property(name="model2", type=Model, multiplicity=Multiplicity(0, 1)),
        Property(name="class3", type=Class_, multiplicity=Multiplicity(0, 1))
    }
)
Class_SaveGameWidget: BinaryAssociation = BinaryAssociation(
    name="Class_SaveGameWidget",
    ends={
        Property(name="saveGameWidget4", type=SaveGameWidget, multiplicity=Multiplicity(0, 1)),
        Property(name="class5", type=Class_, multiplicity=Multiplicity(0, 1))
    }
)
Model_Persistence: BinaryAssociation = BinaryAssociation(
    name="Model_Persistence",
    ends={
        Property(name="_dataAccess6", type=Persistence, multiplicity=Multiplicity(0, 1)),
        Property(name="model7", type=Model, multiplicity=Multiplicity(0, 1))
    }
)
Class_LoadGameWidget: BinaryAssociation = BinaryAssociation(
    name="Class_LoadGameWidget",
    ends={
        Property(name="loadGameWidget0", type=LoadGameWidget, multiplicity=Multiplicity(0, 1)),
        Property(name="class1", type=Class_, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_WJKFoOBcEeeAyLDAJ12_fg",
    types={Model, felhaszn_l__Actor, LoadGameWidget, SaveGameWidget, Class_, Persistence},
    associations={Class_Model, Class_SaveGameWidget, Model_Persistence, Class_LoadGameWidget},
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