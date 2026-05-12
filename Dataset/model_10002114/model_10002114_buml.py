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
Game_PlantationType: Enumeration = Enumeration(
    name="Game_PlantationType",
    literals={
            
    }
)

# Classes
Piece = Class(name="Piece")
Colonist = Class(name="Colonist")
Good = Class(name="Good")
Role = Class(name="Role")
Governor = Class(name="Governor")
VictoryPoint = Class(name="VictoryPoint")
Doubloon = Class(name="Doubloon")
Game_TradingHouse = Class(name="Game_TradingHouse")
Game_SupplyBoard = Class(name="Game_SupplyBoard")
Game_ColonistShip = Class(name="Game_ColonistShip")
Game_ShippingShip = Class(name="Game_ShippingShip")
Game_ColonistZone = Class(name="Game_ColonistZone")
Game_Building = Class(name="Game_Building")
Game_PlayerBoard = Class(name="Game_PlayerBoard")
Game_PlantationSupply = Class(name="Game_PlantationSupply")
Game_Plantation = Class(name="Game_Plantation")
Game_IColonistBoard_Interface = Class(name="Game_IColonistBoard_Interface")
Game_IBoard_Interface = Class(name="Game_IBoard_Interface")
Game_GoodZone = Class(name="Game_GoodZone")

# Piece class attributes and methods

# Colonist class attributes and methods

# Good class attributes and methods

# Role class attributes and methods

# Governor class attributes and methods

# VictoryPoint class attributes and methods

# Doubloon class attributes and methods

# Game_TradingHouse class attributes and methods

# Game_SupplyBoard class attributes and methods

# Game_ColonistShip class attributes and methods
Game_ColonistShip_ColonistZone: Property = Property(name="ColonistZone", type=Game_ColonistZone)
Game_ColonistShip_Num_Colonists: Property = Property(name="Num_Colonists", type=IntegerType)
Game_ColonistShip.attributes={Game_ColonistShip_ColonistZone, Game_ColonistShip_Num_Colonists}

# Game_ShippingShip class attributes and methods
Game_ShippingShip_Size: Property = Property(name="Size", type=IntegerType)
Game_ShippingShip.attributes={Game_ShippingShip_Size}

# Game_ColonistZone class attributes and methods
Game_ColonistZone_Stackable: Property = Property(name="Stackable", type=BooleanType)
Game_ColonistZone_Pieces: Property = Property(name="Pieces", type=Colonist)
Game_ColonistZone_MaxColonists: Property = Property(name="MaxColonists", type=IntegerType)
Game_ColonistZone.attributes={Game_ColonistZone_Pieces, Game_ColonistZone_MaxColonists, Game_ColonistZone_Stackable}

# Game_Building class attributes and methods
Game_Building_Type: Property = Property(name="Type", type=StringType)
Game_Building_Cost: Property = Property(name="Cost", type=IntegerType)
Game_Building_VictoryPoints: Property = Property(name="VictoryPoints", type=IntegerType)
Game_Building_Size: Property = Property(name="Size", type=IntegerType)
Game_Building_ColonistZones: Property = Property(name="ColonistZones", type=Game_ColonistZone)
Game_Building_MaxColonists: Property = Property(name="MaxColonists", type=IntegerType)
Game_Building_HasProduced: Property = Property(name="HasProduced", type=BooleanType)
Game_Building.attributes={Game_Building_VictoryPoints, Game_Building_Type, Game_Building_Size, Game_Building_HasProduced, Game_Building_MaxColonists, Game_Building_ColonistZones, Game_Building_Cost}

# Game_PlayerBoard class attributes and methods
Game_PlayerBoard_PlayerID: Property = Property(name="PlayerID", type=IntegerType)
Game_PlayerBoard_ColonistZone: Property = Property(name="ColonistZone", type=Game_ColonistZone)
Game_PlayerBoard.attributes={Game_PlayerBoard_PlayerID, Game_PlayerBoard_ColonistZone}

# Game_PlantationSupply class attributes and methods

# Game_Plantation class attributes and methods
Game_Plantation_Type: Property = Property(name="Type", type=Game_PlantationType)
Game_Plantation_ColonistZone: Property = Property(name="ColonistZone", type=Game_ColonistZone)
Game_Plantation_HasProduced: Property = Property(name="HasProduced", type=BooleanType)
Game_Plantation.attributes={Game_Plantation_HasProduced, Game_Plantation_ColonistZone, Game_Plantation_Type}

# Game_IColonistBoard_Interface class attributes and methods

# Game_IBoard_Interface class attributes and methods

# Game_GoodZone class attributes and methods
Game_GoodZone_Stackable: Property = Property(name="Stackable", type=BooleanType)
Game_GoodZone_Pieces: Property = Property(name="Pieces", type=Good)
Game_GoodZone.attributes={Game_GoodZone_Stackable, Game_GoodZone_Pieces}

# Domain Model
domain_model = DomainModel(
    name="_pE620ICTEei_m5BAOg12zA",
    types={Piece, Colonist, Good, Role, Governor, VictoryPoint, Doubloon, Game_TradingHouse, Game_SupplyBoard, Game_ColonistShip, Game_ShippingShip, Game_ColonistZone, Game_Building, Game_PlayerBoard, Game_PlantationSupply, Game_Plantation, Game_IColonistBoard_Interface, Game_IBoard_Interface, Game_GoodZone, Game_PlantationType},
    associations={},
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