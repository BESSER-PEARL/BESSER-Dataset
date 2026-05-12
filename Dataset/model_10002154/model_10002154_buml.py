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
Board = Class(name="Board")
MinesAdapter = Class(name="MinesAdapter")
Mines = Class(name="Mines")
genmymodelreverse_java_awt_Graphics = Class(name="genmymodelreverse_java_awt_Graphics", is_abstract=True)
genmymodelreverse_java_awt_event_MouseAdapter = Class(name="genmymodelreverse_java_awt_event_MouseAdapter", is_abstract=True)
genmymodelreverse_java_awt_event_MouseEvent = Class(name="genmymodelreverse_java_awt_event_MouseEvent")
genmymodelreverse_javax_swing_JLabel = Class(name="genmymodelreverse_javax_swing_JLabel")
genmymodelreverse_javax_swing_JPanel = Class(name="genmymodelreverse_javax_swing_JPanel")
genmymodelreverse_javax_swing_JFrame = Class(name="genmymodelreverse_javax_swing_JFrame")
genmymodelreverse_javax_swing_JMenuItem = Class(name="genmymodelreverse_javax_swing_JMenuItem")

# Board class attributes and methods
Board_NUM_IMAGES: Property = Property(name="NUM_IMAGES", type=IntegerType)
Board_CELL_SIZE: Property = Property(name="CELL_SIZE", type=IntegerType)
Board_COVER_FOR_CELL: Property = Property(name="COVER_FOR_CELL", type=IntegerType)
Board_MARK_FOR_CELL: Property = Property(name="MARK_FOR_CELL", type=IntegerType)
Board_EMPTY_CELL: Property = Property(name="EMPTY_CELL", type=IntegerType)
Board_MINE_CELL: Property = Property(name="MINE_CELL", type=IntegerType)
Board_COVERED_MINE_CELL: Property = Property(name="COVERED_MINE_CELL", type=IntegerType)
Board_MARKED_MINE_CELL: Property = Property(name="MARKED_MINE_CELL", type=IntegerType)
Board_DRAW_MINE: Property = Property(name="DRAW_MINE", type=IntegerType)
Board_DRAW_COVER: Property = Property(name="DRAW_COVER", type=IntegerType)
Board_DRAW_MARK: Property = Property(name="DRAW_MARK", type=IntegerType)
Board_DRAW_WRONG_MARK: Property = Property(name="DRAW_WRONG_MARK", type=IntegerType)
Board_N_MINES: Property = Property(name="N_MINES", type=IntegerType)
Board_N_ROWS: Property = Property(name="N_ROWS", type=IntegerType)
Board_N_COLS: Property = Property(name="N_COLS", type=IntegerType)
Board_field: Property = Property(name="field", type=StringType)
Board_inGame: Property = Property(name="inGame", type=BooleanType)
Board_mines_left: Property = Property(name="mines_left", type=IntegerType)
Board_img: Property = Property(name="img", type=StringType)
Board_all_cells: Property = Property(name="all_cells", type=IntegerType)
Board_statusbar: Property = Property(name="statusbar", type=genmymodelreverse_javax_swing_JLabel)
Board_timeBar: Property = Property(name="timeBar", type=genmymodelreverse_javax_swing_JLabel)
Board.attributes={Board_all_cells, Board_DRAW_MINE, Board_MARKED_MINE_CELL, Board_COVER_FOR_CELL, Board_statusbar, Board_mines_left, Board_MINE_CELL, Board_img, Board_timeBar, Board_EMPTY_CELL, Board_CELL_SIZE, Board_field, Board_inGame, Board_MARK_FOR_CELL, Board_N_COLS, Board_DRAW_COVER, Board_DRAW_MARK, Board_DRAW_WRONG_MARK, Board_COVERED_MINE_CELL, Board_N_ROWS, Board_NUM_IMAGES, Board_N_MINES}

# MinesAdapter class attributes and methods

# Mines class attributes and methods
Mines_FRAME_WIDTH: Property = Property(name="FRAME_WIDTH", type=IntegerType)
Mines_FRAME_HEIGHT: Property = Property(name="FRAME_HEIGHT", type=IntegerType)
Mines_statusbar: Property = Property(name="statusbar", type=genmymodelreverse_javax_swing_JLabel)
Mines_timeBar: Property = Property(name="timeBar", type=genmymodelreverse_javax_swing_JLabel)
Mines_hexCell: Property = Property(name="hexCell", type=genmymodelreverse_javax_swing_JMenuItem)
Mines.attributes={Mines_statusbar, Mines_FRAME_WIDTH, Mines_FRAME_HEIGHT, Mines_hexCell, Mines_timeBar}

# genmymodelreverse_java_awt_Graphics class attributes and methods

# genmymodelreverse_java_awt_event_MouseAdapter class attributes and methods

# genmymodelreverse_java_awt_event_MouseEvent class attributes and methods

# genmymodelreverse_javax_swing_JLabel class attributes and methods

# genmymodelreverse_javax_swing_JPanel class attributes and methods

# genmymodelreverse_javax_swing_JFrame class attributes and methods

# genmymodelreverse_javax_swing_JMenuItem class attributes and methods

# Relationships
game_Mines_Board_0: BinaryAssociation = BinaryAssociation(
    name="game_Mines_Board_0",
    ends={
        Property(name="mines0", type=Mines, multiplicity=Multiplicity(0, 1)),
        Property(name="game1", type=Board, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_sz178HLOEee5HMQDnOR_kg",
    types={Board, MinesAdapter, Mines, genmymodelreverse_java_awt_Graphics, genmymodelreverse_java_awt_event_MouseAdapter, genmymodelreverse_java_awt_event_MouseEvent, genmymodelreverse_javax_swing_JLabel, genmymodelreverse_javax_swing_JPanel, genmymodelreverse_javax_swing_JFrame, genmymodelreverse_javax_swing_JMenuItem},
    associations={game_Mines_Board_0},
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