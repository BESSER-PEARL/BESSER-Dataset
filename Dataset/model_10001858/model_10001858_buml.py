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
window = Class(name="window")
cursor = Class(name="cursor")
choice_window = Class(name="choice_window")
game_board = Class(name="game_board")
game_board1 = Class(name="game_board1")
sudoku_board = Class(name="sudoku_board")
save = Class(name="save")
load = Class(name="load")
sudoku_board1 = Class(name="sudoku_board1")
sudoku_validator = Class(name="sudoku_validator")
cursor1 = Class(name="cursor1")

# window class attributes and methods
window__main: Property = Property(name="_main", type=StringType)
window_current: Property = Property(name="current", type=cursor)
window_x: Property = Property(name="x", type=IntegerType)
window_y: Property = Property(name="y", type=IntegerType)
window_columns: Property = Property(name="columns", type=IntegerType)
window_lines: Property = Property(name="lines", type=IntegerType)
window.attributes={window_current, window_columns, window_lines, window_x, window_y, window__main}

# cursor class attributes and methods

# choice_window class attributes and methods
choice_window_names_3_: Property = Property(name="names_3_", type=StringType)
choice_window_prompt_3_: Property = Property(name="prompt_3_", type=cursor)
choice_window_response_3_: Property = Property(name="response_3_", type=StringType)
choice_window.attributes={choice_window_response_3_, choice_window_prompt_3_, choice_window_names_3_}

# game_board class attributes and methods

# game_board1 class attributes and methods
game_board1_board: Property = Property(name="board", type=sudoku_board)
game_board1.attributes={game_board1_board}

# sudoku_board class attributes and methods

# save class attributes and methods
save_file_name: Property = Property(name="file_name", type=StringType)
save.attributes={save_file_name}

# load class attributes and methods
load_file_name: Property = Property(name="file_name", type=StringType)
load.attributes={load_file_name}

# sudoku_board1 class attributes and methods
sudoku_board1_board_9__9_: Property = Property(name="board_9__9_", type=IntegerType)
sudoku_board1_fixed_9__9_: Property = Property(name="fixed_9__9_", type=IntegerType)
sudoku_board1.attributes={sudoku_board1_fixed_9__9_, sudoku_board1_board_9__9_}

# sudoku_validator class attributes and methods

# cursor1 class attributes and methods
cursor1_pos_x: Property = Property(name="pos_x", type=IntegerType)
cursor1_pos_y: Property = Property(name="pos_y", type=IntegerType)
cursor1_limit_y: Property = Property(name="limit_y", type=StringType)
cursor1_limit_x: Property = Property(name="limit_x", type=IntegerType)
cursor1.attributes={cursor1_limit_y, cursor1_limit_x, cursor1_pos_y, cursor1_pos_x}

# Domain Model
domain_model = DomainModel(
    name="__dDc8AdyEeipbtix_oa2Dg",
    types={window, cursor, choice_window, game_board, game_board1, sudoku_board, save, load, sudoku_board1, sudoku_validator, cursor1},
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