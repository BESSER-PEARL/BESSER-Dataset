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
checkers_Position: Enumeration = Enumeration(
    name="checkers_Position",
    literals={
            
    }
)

# Classes
checkers_CheckerMove = Class(name="checkers_CheckerMove")
checkers_Checkers = Class(name="checkers_Checkers")
checkers_GameWin = Class(name="checkers_GameWin")
checkers_Help = Class(name="checkers_Help")
checkers_IntelliChecker = Class(name="checkers_IntelliChecker")
checkers_PlaySound = Class(name="checkers_PlaySound")
checkers_StartPanel = Class(name="checkers_StartPanel")
checkers_GameEngine = Class(name="checkers_GameEngine")
checkers_CheckerFrame = Class(name="checkers_CheckerFrame")
genmymodelreverse_java_awt_event_ActionEvent = Class(name="genmymodelreverse_java_awt_event_ActionEvent")
genmymodelreverse_javax_swing_JFrame = Class(name="genmymodelreverse_javax_swing_JFrame")
genmymodelreverse_java_util_Vector = Class(name="genmymodelreverse_java_util_Vector")
genmymodelreverse_javax_swing_JPanel = Class(name="genmymodelreverse_javax_swing_JPanel")
genmymodelreverse_java_awt_event_ItemListener_Interface = Class(name="genmymodelreverse_java_awt_event_ItemListener_Interface", is_abstract=True)
genmymodelreverse_java_awt_event_MouseMotionListener_Interface = Class(name="genmymodelreverse_java_awt_event_MouseMotionListener_Interface", is_abstract=True)
genmymodelreverse_java_awt_event_MouseListener_Interface = Class(name="genmymodelreverse_java_awt_event_MouseListener_Interface", is_abstract=True)
genmymodelreverse_javax_swing_JDialog = Class(name="genmymodelreverse_javax_swing_JDialog")
genmymodelreverse_java_lang_Thread = Class(name="genmymodelreverse_java_lang_Thread")
genmymodelreverse_javax_swing_JButton = Class(name="genmymodelreverse_javax_swing_JButton")
genmymodelreverse_java_awt_Graphics = Class(name="genmymodelreverse_java_awt_Graphics", is_abstract=True)
genmymodelreverse_javax_swing_JTextArea = Class(name="genmymodelreverse_javax_swing_JTextArea")
genmymodelreverse_javax_swing_ImageIcon = Class(name="genmymodelreverse_javax_swing_ImageIcon")
genmymodelreverse_javax_swing_ButtonGroup = Class(name="genmymodelreverse_javax_swing_ButtonGroup")
genmymodelreverse_javax_swing_JRadioButton = Class(name="genmymodelreverse_javax_swing_JRadioButton")
genmymodelreverse_javax_swing_JLabel = Class(name="genmymodelreverse_javax_swing_JLabel")
genmymodelreverse_javax_swing_JComboBox = Class(name="genmymodelreverse_javax_swing_JComboBox")
genmymodelreverse_java_awt_Point = Class(name="genmymodelreverse_java_awt_Point")
genmymodelreverse_java_awt_event_ItemEvent = Class(name="genmymodelreverse_java_awt_event_ItemEvent")
genmymodelreverse_java_awt_event_MouseEvent = Class(name="genmymodelreverse_java_awt_event_MouseEvent")
genmymodelreverse_javax_swing_JScrollPane = Class(name="genmymodelreverse_javax_swing_JScrollPane")
genmymodelreverse_java_lang_Exception = Class(name="genmymodelreverse_java_lang_Exception")
Checkers_Start_the_Game_GUI_UseCase = Class(name="Checkers_Start_the_Game_GUI_UseCase")
Checkers_Select__Help__UseCase = Class(name="Checkers_Select__Help__UseCase")
Checkers_Toggle__Sound__UseCase = Class(name="Checkers_Toggle__Sound__UseCase")
Checkers_Select__Difficulty_Level__UseCase = Class(name="Checkers_Select__Difficulty_Level__UseCase")
Checkers_Select__Player_Mode__UseCase = Class(name="Checkers_Select__Player_Mode__UseCase")
Checkers_Start_New_Game_UseCase = Class(name="Checkers_Start_New_Game_UseCase")
Checkers_Move_Game_Pieces_UseCase = Class(name="Checkers_Move_Game_Pieces_UseCase")
Checkers_Close_or_Exit_Game_UseCase = Class(name="Checkers_Close_or_Exit_Game_UseCase")
Human_Player_1_Actor = Class(name="Human_Player_1_Actor")
Human_Player_2_Actor = Class(name="Human_Player_2_Actor")
Computer_Player_1_Actor = Class(name="Computer_Player_1_Actor")

# checkers_CheckerMove class attributes and methods
checkers_CheckerMove_legalMove: Property = Property(name="legalMove", type=IntegerType)
checkers_CheckerMove_illegalMove: Property = Property(name="illegalMove", type=IntegerType)
checkers_CheckerMove_incompleteMove: Property = Property(name="incompleteMove", type=IntegerType)
checkers_CheckerMove.attributes={checkers_CheckerMove_illegalMove, checkers_CheckerMove_legalMove, checkers_CheckerMove_incompleteMove}

# checkers_Checkers class attributes and methods
checkers_Checkers_g: Property = Property(name="g", type=genmymodelreverse_java_awt_Graphics)
checkers_Checkers_msg: Property = Property(name="msg", type=genmymodelreverse_javax_swing_JTextArea)
checkers_Checkers_redN: Property = Property(name="redN", type=genmymodelreverse_javax_swing_ImageIcon)
checkers_Checkers_yellowN: Property = Property(name="yellowN", type=genmymodelreverse_javax_swing_ImageIcon)
checkers_Checkers_redK: Property = Property(name="redK", type=genmymodelreverse_javax_swing_ImageIcon)
checkers_Checkers_yellowK: Property = Property(name="yellowK", type=genmymodelreverse_javax_swing_ImageIcon)
checkers_Checkers_hlp: Property = Property(name="hlp", type=genmymodelreverse_javax_swing_ImageIcon)
checkers_Checkers_snp: Property = Property(name="snp", type=genmymodelreverse_javax_swing_ImageIcon)
checkers_Checkers_mup: Property = Property(name="mup", type=genmymodelreverse_javax_swing_ImageIcon)
checkers_Checkers_nwB: Property = Property(name="nwB", type=genmymodelreverse_javax_swing_JButton)
checkers_Checkers_unB: Property = Property(name="unB", type=genmymodelreverse_javax_swing_JButton)
checkers_Checkers_hlpB: Property = Property(name="hlpB", type=genmymodelreverse_javax_swing_JButton)
checkers_Checkers_snB: Property = Property(name="snB", type=genmymodelreverse_javax_swing_JButton)
checkers_Checkers_players: Property = Property(name="players", type=genmymodelreverse_javax_swing_ButtonGroup)
checkers_Checkers_selectedColor: Property = Property(name="selectedColor", type=StringType)
checkers_Checkers_selectedMode: Property = Property(name="selectedMode", type=IntegerType)
checkers_Checkers_difficulty: Property = Property(name="difficulty", type=IntegerType)
checkers_Checkers_redNormal: Property = Property(name="redNormal", type=IntegerType)
checkers_Checkers_yellowNormal: Property = Property(name="yellowNormal", type=IntegerType)
checkers_Checkers_redKing: Property = Property(name="redKing", type=IntegerType)
checkers_Checkers_yellowKing: Property = Property(name="yellowKing", type=IntegerType)
checkers_Checkers_empty: Property = Property(name="empty", type=IntegerType)
checkers_Checkers_currType: Property = Property(name="currType", type=IntegerType)
checkers_Checkers_movable: Property = Property(name="movable", type=BooleanType)
checkers_Checkers_board: Property = Property(name="board", type=StringType)
checkers_Checkers_preBoard1: Property = Property(name="preBoard1", type=StringType)
checkers_Checkers_preToMove1: Property = Property(name="preToMove1", type=IntegerType)
checkers_Checkers_preBoard2: Property = Property(name="preBoard2", type=StringType)
checkers_Checkers_preToMove2: Property = Property(name="preToMove2", type=IntegerType)
checkers_Checkers_preBoard3: Property = Property(name="preBoard3", type=StringType)
checkers_Checkers_preToMove3: Property = Property(name="preToMove3", type=IntegerType)
checkers_Checkers_endY: Property = Property(name="endY", type=IntegerType)
checkers_Checkers_incomplete: Property = Property(name="incomplete", type=BooleanType)
checkers_Checkers_highlight: Property = Property(name="highlight", type=BooleanType)
checkers_Checkers_toMove: Property = Property(name="toMove", type=IntegerType)
checkers_Checkers_loser: Property = Property(name="loser", type=IntegerType)
checkers_Checkers_silent: Property = Property(name="silent", type=BooleanType)
checkers_Checkers_undoCount: Property = Property(name="undoCount", type=IntegerType)
checkers_Checkers_won: Property = Property(name="won", type=IntegerType)
checkers_Checkers_winPoint: Property = Property(name="winPoint", type=genmymodelreverse_java_awt_Point)
checkers_Checkers_p1: Property = Property(name="p1", type=genmymodelreverse_javax_swing_JRadioButton)
checkers_Checkers_p2: Property = Property(name="p2", type=genmymodelreverse_javax_swing_JRadioButton)
checkers_Checkers_colors: Property = Property(name="colors", type=genmymodelreverse_javax_swing_ButtonGroup)
checkers_Checkers_c1: Property = Property(name="c1", type=genmymodelreverse_javax_swing_JRadioButton)
checkers_Checkers_c2: Property = Property(name="c2", type=genmymodelreverse_javax_swing_JRadioButton)
checkers_Checkers_mode: Property = Property(name="mode", type=genmymodelreverse_javax_swing_JLabel)
checkers_Checkers_col: Property = Property(name="col", type=genmymodelreverse_javax_swing_JLabel)
checkers_Checkers_diff: Property = Property(name="diff", type=genmymodelreverse_javax_swing_JLabel)
checkers_Checkers_rp: Property = Property(name="rp", type=genmymodelreverse_javax_swing_JLabel)
checkers_Checkers_rpt: Property = Property(name="rpt", type=genmymodelreverse_javax_swing_JLabel)
checkers_Checkers_bpt: Property = Property(name="bpt", type=genmymodelreverse_javax_swing_JLabel)
checkers_Checkers_bp: Property = Property(name="bp", type=genmymodelreverse_javax_swing_JLabel)
checkers_Checkers_rk: Property = Property(name="rk", type=genmymodelreverse_javax_swing_JLabel)
checkers_Checkers_rkt: Property = Property(name="rkt", type=genmymodelreverse_javax_swing_JLabel)
checkers_Checkers_bkt: Property = Property(name="bkt", type=genmymodelreverse_javax_swing_JLabel)
checkers_Checkers_bk: Property = Property(name="bk", type=genmymodelreverse_javax_swing_JLabel)
checkers_Checkers_level: Property = Property(name="level", type=genmymodelreverse_javax_swing_JComboBox)
checkers_Checkers.attributes={checkers_Checkers_undoCount, checkers_Checkers_mup, checkers_Checkers_col, checkers_Checkers_rpt, checkers_Checkers_yellowKing, checkers_Checkers_bp, checkers_Checkers_yellowK, checkers_Checkers_selectedMode, checkers_Checkers_yellowNormal, checkers_Checkers_bpt, checkers_Checkers_rk, checkers_Checkers_preToMove2, checkers_Checkers_snB, checkers_Checkers_diff, checkers_Checkers_winPoint, checkers_Checkers_msg, checkers_Checkers_colors, checkers_Checkers_silent, checkers_Checkers_yellowN, checkers_Checkers_preToMove3, checkers_Checkers_rkt, checkers_Checkers_nwB, checkers_Checkers_redN, checkers_Checkers_p2, checkers_Checkers_mode, checkers_Checkers_redKing, checkers_Checkers_hlpB, checkers_Checkers_level, checkers_Checkers_unB, checkers_Checkers_bk, checkers_Checkers_g, checkers_Checkers_preBoard2, checkers_Checkers_difficulty, checkers_Checkers_c1, checkers_Checkers_incomplete, checkers_Checkers_currType, checkers_Checkers_redK, checkers_Checkers_endY, checkers_Checkers_toMove, checkers_Checkers_preToMove1, checkers_Checkers_won, checkers_Checkers_redNormal, checkers_Checkers_empty, checkers_Checkers_c2, checkers_Checkers_snp, checkers_Checkers_loser, checkers_Checkers_highlight, checkers_Checkers_preBoard1, checkers_Checkers_bkt, checkers_Checkers_preBoard3, checkers_Checkers_hlp, checkers_Checkers_players, checkers_Checkers_p1, checkers_Checkers_rp, checkers_Checkers_board, checkers_Checkers_movable, checkers_Checkers_selectedColor}

# checkers_GameWin class attributes and methods
checkers_GameWin_p: Property = Property(name="p", type=genmymodelreverse_java_awt_Point)
checkers_GameWin_masseage: Property = Property(name="masseage", type=genmymodelreverse_javax_swing_JLabel)
checkers_GameWin.attributes={checkers_GameWin_p, checkers_GameWin_masseage}

# checkers_Help class attributes and methods
checkers_Help_hlp: Property = Property(name="hlp", type=genmymodelreverse_javax_swing_JScrollPane)
checkers_Help_txt: Property = Property(name="txt", type=genmymodelreverse_javax_swing_JTextArea)
checkers_Help.attributes={checkers_Help_txt, checkers_Help_hlp}

# checkers_IntelliChecker class attributes and methods

# checkers_PlaySound class attributes and methods
checkers_PlaySound_filename: Property = Property(name="filename", type=StringType)
checkers_PlaySound_EXTERNAL_BUFFER_SIZE: Property = Property(name="EXTERNAL_BUFFER_SIZE", type=IntegerType)
checkers_PlaySound.attributes={checkers_PlaySound_filename, checkers_PlaySound_EXTERNAL_BUFFER_SIZE}

# checkers_StartPanel class attributes and methods

# checkers_GameEngine class attributes and methods
checkers_GameEngine_inf: Property = Property(name="inf", type=IntegerType)
checkers_GameEngine_normal: Property = Property(name="normal", type=IntegerType)
checkers_GameEngine_king: Property = Property(name="king", type=IntegerType)
checkers_GameEngine_pos: Property = Property(name="pos", type=IntegerType)
checkers_GameEngine_edge: Property = Property(name="edge", type=IntegerType)
checkers_GameEngine.attributes={checkers_GameEngine_king, checkers_GameEngine_edge, checkers_GameEngine_normal, checkers_GameEngine_pos, checkers_GameEngine_inf}

# checkers_CheckerFrame class attributes and methods
checkers_CheckerFrame_gamePanel: Property = Property(name="gamePanel", type=StringType)
checkers_CheckerFrame_startButton: Property = Property(name="startButton", type=StringType)
checkers_CheckerFrame.attributes={checkers_CheckerFrame_startButton, checkers_CheckerFrame_gamePanel}

# genmymodelreverse_java_awt_event_ActionEvent class attributes and methods

# genmymodelreverse_javax_swing_JFrame class attributes and methods

# genmymodelreverse_java_util_Vector class attributes and methods

# genmymodelreverse_javax_swing_JPanel class attributes and methods

# genmymodelreverse_java_awt_event_ItemListener_Interface class attributes and methods

# genmymodelreverse_java_awt_event_MouseMotionListener_Interface class attributes and methods

# genmymodelreverse_java_awt_event_MouseListener_Interface class attributes and methods

# genmymodelreverse_javax_swing_JDialog class attributes and methods

# genmymodelreverse_java_lang_Thread class attributes and methods

# genmymodelreverse_javax_swing_JButton class attributes and methods

# genmymodelreverse_java_awt_Graphics class attributes and methods

# genmymodelreverse_javax_swing_JTextArea class attributes and methods

# genmymodelreverse_javax_swing_ImageIcon class attributes and methods

# genmymodelreverse_javax_swing_ButtonGroup class attributes and methods

# genmymodelreverse_javax_swing_JRadioButton class attributes and methods

# genmymodelreverse_javax_swing_JLabel class attributes and methods

# genmymodelreverse_javax_swing_JComboBox class attributes and methods

# genmymodelreverse_java_awt_Point class attributes and methods

# genmymodelreverse_java_awt_event_ItemEvent class attributes and methods

# genmymodelreverse_java_awt_event_MouseEvent class attributes and methods

# genmymodelreverse_javax_swing_JScrollPane class attributes and methods

# genmymodelreverse_java_lang_Exception class attributes and methods

# Checkers_Start_the_Game_GUI_UseCase class attributes and methods

# Checkers_Select__Help__UseCase class attributes and methods

# Checkers_Toggle__Sound__UseCase class attributes and methods

# Checkers_Select__Difficulty_Level__UseCase class attributes and methods

# Checkers_Select__Player_Mode__UseCase class attributes and methods

# Checkers_Start_New_Game_UseCase class attributes and methods

# Checkers_Move_Game_Pieces_UseCase class attributes and methods

# Checkers_Close_or_Exit_Game_UseCase class attributes and methods

# Human_Player_1_Actor class attributes and methods

# Human_Player_2_Actor class attributes and methods

# Computer_Player_1_Actor class attributes and methods

# Relationships
hp_Checkers_Help_0: BinaryAssociation = BinaryAssociation(
    name="hp_Checkers_Help_0",
    ends={
        Property(name="checkers0", type=checkers_Checkers, multiplicity=Multiplicity(0, 1)),
        Property(name="hp1", type=checkers_Help, multiplicity=Multiplicity(0, 1))
    }
)
Computer_Player_1_Move_Game_Pieces: BinaryAssociation = BinaryAssociation(
    name="Computer_Player_1_Move_Game_Pieces",
    ends={
        Property(name="move_Game_Pieces2", type=Checkers_Move_Game_Pieces_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="computer_Player_13", type=Computer_Player_1_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Human_Player_2__Secondary__Move_Game_Pieces: BinaryAssociation = BinaryAssociation(
    name="Human_Player_2__Secondary__Move_Game_Pieces",
    ends={
        Property(name="move_Game_Pieces4", type=Checkers_Move_Game_Pieces_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="human_Player_2__Secondary_5", type=Human_Player_2_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Human_Player_1__Primary__Move_Game_Pieces: BinaryAssociation = BinaryAssociation(
    name="Human_Player_1__Primary__Move_Game_Pieces",
    ends={
        Property(name="move_Game_Pieces6", type=Checkers_Move_Game_Pieces_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="human_Player_1__Primary_7", type=Human_Player_1_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Human_Player_1_Start_the_Game_GUI: BinaryAssociation = BinaryAssociation(
    name="Human_Player_1_Start_the_Game_GUI",
    ends={
        Property(name="start_the_Game_GUI8", type=Checkers_Start_the_Game_GUI_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="human_Player_19", type=Human_Player_1_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Human_Player_1_Select__Help_: BinaryAssociation = BinaryAssociation(
    name="Human_Player_1_Select__Help_",
    ends={
        Property(name="select__Help_10", type=Checkers_Select__Help__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="human_Player_111", type=Human_Player_1_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Human_Player_1_Toggle__Sound_: BinaryAssociation = BinaryAssociation(
    name="Human_Player_1_Toggle__Sound_",
    ends={
        Property(name="toggle__Sound_12", type=Checkers_Toggle__Sound__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="human_Player_113", type=Human_Player_1_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Human_Player_1_Select__Difficulty_Level_: BinaryAssociation = BinaryAssociation(
    name="Human_Player_1_Select__Difficulty_Level_",
    ends={
        Property(name="select__Difficulty_Level_14", type=Checkers_Select__Difficulty_Level__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="human_Player_115", type=Human_Player_1_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Human_Player_1_Select__Player_Mode_: BinaryAssociation = BinaryAssociation(
    name="Human_Player_1_Select__Player_Mode_",
    ends={
        Property(name="select__Player_Mode_16", type=Checkers_Select__Player_Mode__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="human_Player_117", type=Human_Player_1_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Human_Player_1_Start_New_Game: BinaryAssociation = BinaryAssociation(
    name="Human_Player_1_Start_New_Game",
    ends={
        Property(name="start_New_Game18", type=Checkers_Start_New_Game_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="human_Player_119", type=Human_Player_1_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Human_Player_1_Close_or_Exit_Game: BinaryAssociation = BinaryAssociation(
    name="Human_Player_1_Close_or_Exit_Game",
    ends={
        Property(name="close_or_Exit_Game20", type=Checkers_Close_or_Exit_Game_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="human_Player_121", type=Human_Player_1_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Human_Player_2_Start_the_Game_GUI: BinaryAssociation = BinaryAssociation(
    name="Human_Player_2_Start_the_Game_GUI",
    ends={
        Property(name="start_the_Game_GUI22", type=Checkers_Start_the_Game_GUI_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="human_Player_223", type=Human_Player_2_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Human_Player_2_Select__Help_: BinaryAssociation = BinaryAssociation(
    name="Human_Player_2_Select__Help_",
    ends={
        Property(name="select__Help_24", type=Checkers_Select__Help__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="human_Player_225", type=Human_Player_2_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Human_Player_2_Close_or_Exit_Game: BinaryAssociation = BinaryAssociation(
    name="Human_Player_2_Close_or_Exit_Game",
    ends={
        Property(name="close_or_Exit_Game34", type=Checkers_Close_or_Exit_Game_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="human_Player_235", type=Human_Player_2_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Human_Player_2_Toggle__Sound_: BinaryAssociation = BinaryAssociation(
    name="Human_Player_2_Toggle__Sound_",
    ends={
        Property(name="toggle__Sound_26", type=Checkers_Toggle__Sound__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="human_Player_227", type=Human_Player_2_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Human_Player_2_Select__Difficulty_Level_: BinaryAssociation = BinaryAssociation(
    name="Human_Player_2_Select__Difficulty_Level_",
    ends={
        Property(name="select__Difficulty_Level_28", type=Checkers_Select__Difficulty_Level__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="human_Player_229", type=Human_Player_2_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Human_Player_2_Select__Player_Mode_: BinaryAssociation = BinaryAssociation(
    name="Human_Player_2_Select__Player_Mode_",
    ends={
        Property(name="select__Player_Mode_30", type=Checkers_Select__Player_Mode__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="human_Player_231", type=Human_Player_2_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Human_Player_2_Start_New_Game: BinaryAssociation = BinaryAssociation(
    name="Human_Player_2_Start_New_Game",
    ends={
        Property(name="start_New_Game32", type=Checkers_Start_New_Game_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="human_Player_233", type=Human_Player_2_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_3eaf620b_7f77_4027_b9b4_7552d01a2e99",
    types={checkers_CheckerMove, checkers_Checkers, checkers_GameWin, checkers_Help, checkers_IntelliChecker, checkers_PlaySound, checkers_StartPanel, checkers_GameEngine, checkers_CheckerFrame, genmymodelreverse_java_awt_event_ActionEvent, genmymodelreverse_javax_swing_JFrame, genmymodelreverse_java_util_Vector, genmymodelreverse_javax_swing_JPanel, genmymodelreverse_java_awt_event_ItemListener_Interface, genmymodelreverse_java_awt_event_MouseMotionListener_Interface, genmymodelreverse_java_awt_event_MouseListener_Interface, genmymodelreverse_javax_swing_JDialog, genmymodelreverse_java_lang_Thread, genmymodelreverse_javax_swing_JButton, genmymodelreverse_java_awt_Graphics, genmymodelreverse_javax_swing_JTextArea, genmymodelreverse_javax_swing_ImageIcon, genmymodelreverse_javax_swing_ButtonGroup, genmymodelreverse_javax_swing_JRadioButton, genmymodelreverse_javax_swing_JLabel, genmymodelreverse_javax_swing_JComboBox, genmymodelreverse_java_awt_Point, genmymodelreverse_java_awt_event_ItemEvent, genmymodelreverse_java_awt_event_MouseEvent, genmymodelreverse_javax_swing_JScrollPane, genmymodelreverse_java_lang_Exception, Checkers_Start_the_Game_GUI_UseCase, Checkers_Select__Help__UseCase, Checkers_Toggle__Sound__UseCase, Checkers_Select__Difficulty_Level__UseCase, Checkers_Select__Player_Mode__UseCase, Checkers_Start_New_Game_UseCase, Checkers_Move_Game_Pieces_UseCase, Checkers_Close_or_Exit_Game_UseCase, Human_Player_1_Actor, Human_Player_2_Actor, Computer_Player_1_Actor, checkers_Position},
    associations={hp_Checkers_Help_0, Computer_Player_1_Move_Game_Pieces, Human_Player_2__Secondary__Move_Game_Pieces, Human_Player_1__Primary__Move_Game_Pieces, Human_Player_1_Start_the_Game_GUI, Human_Player_1_Select__Help_, Human_Player_1_Toggle__Sound_, Human_Player_1_Select__Difficulty_Level_, Human_Player_1_Select__Player_Mode_, Human_Player_1_Start_New_Game, Human_Player_1_Close_or_Exit_Game, Human_Player_2_Start_the_Game_GUI, Human_Player_2_Select__Help_, Human_Player_2_Close_or_Exit_Game, Human_Player_2_Toggle__Sound_, Human_Player_2_Select__Difficulty_Level_, Human_Player_2_Select__Player_Mode_, Human_Player_2_Start_New_Game},
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