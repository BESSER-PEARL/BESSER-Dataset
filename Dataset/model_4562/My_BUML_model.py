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
Legolang_controlflow_operator = Class(name="Legolang::controlflow::operator")
Legolang_controlflow_opUnaire = Class(name="Legolang::controlflow::opUnaire")
controlflow_operator = Class(name="controlflow::operator")
controlflow_ExprBool = Class(name="controlflow::ExprBool")
Legolang_controlflow_opBinaire = Class(name="Legolang::controlflow::opBinaire")
operator = Class(name="operator")
opBinaire = Class(name="opBinaire")
Legolang_Robot_OrderRobot = Class(name="Legolang::Robot::OrderRobot")
Expr = Class(name="Expr")
Legolang_Robot_move = Class(name="Legolang::Robot::move")
OrderRobot = Class(name="OrderRobot")
Legolang_Robot_bip = Class(name="Legolang::Robot::bip")
Legolang_Robot_turn = Class(name="Legolang::Robot::turn")
Legolang_Robot_stopEngine = Class(name="Legolang::Robot::stopEngine")
Legolang_Robot_display = Class(name="Legolang::Robot::display")
Legolang_Robot_turnAngle = Class(name="Legolang::Robot::turnAngle")
Legolang_Robot_obstacle = Class(name="Legolang::Robot::obstacle")
Legolang_Robot_hasTurned = Class(name="Legolang::Robot::hasTurned")
Legolang_controlflow_tantqueue = Class(name="Legolang::controlflow::tantqueue")
ExprBool = Class(name="ExprBool")
Legolang_controlflow_si = Class(name="Legolang::controlflow::si")
Legolang_controlflow_Expr = Class(name="Legolang::controlflow::Expr")
tantqueue = Class(name="tantqueue")
Legolang_controlflow_not = Class(name="Legolang::controlflow::not")
opUnaire = Class(name="opUnaire")
Legolang_controlflow_and = Class(name="Legolang::controlflow::and")
Legolang_controlflow_ExprBool = Class(name="Legolang::controlflow::ExprBool")
Legolang_controlflow_Program = Class(name="Legolang::controlflow::Program")

# Legolang_controlflow_operator class attributes and methods

# Legolang_controlflow_opUnaire class attributes and methods

# controlflow_operator class attributes and methods

# controlflow_ExprBool class attributes and methods

# Legolang_controlflow_opBinaire class attributes and methods

# operator class attributes and methods

# opBinaire class attributes and methods

# Legolang_Robot_OrderRobot class attributes and methods

# Expr class attributes and methods

# Legolang_Robot_move class attributes and methods

# OrderRobot class attributes and methods

# Legolang_Robot_bip class attributes and methods

# Legolang_Robot_turn class attributes and methods

# Legolang_Robot_stopEngine class attributes and methods

# Legolang_Robot_display class attributes and methods

# Legolang_Robot_turnAngle class attributes and methods

# Legolang_Robot_obstacle class attributes and methods

# Legolang_Robot_hasTurned class attributes and methods

# Legolang_controlflow_tantqueue class attributes and methods

# ExprBool class attributes and methods

# Legolang_controlflow_si class attributes and methods

# Legolang_controlflow_Expr class attributes and methods

# tantqueue class attributes and methods

# Legolang_controlflow_not class attributes and methods

# opUnaire class attributes and methods

# Legolang_controlflow_and class attributes and methods

# Legolang_controlflow_ExprBool class attributes and methods

# Legolang_controlflow_Program class attributes and methods

# Relationships
fonction11: BinaryAssociation = BinaryAssociation(
    name="fonction11",
    ends={
        Property(name="OrderRobot", type=Legolang_controlflow_Expr, multiplicity=Multiplicity(1, 1)),
        Property(name="Legolang_controlflow_Expr12", type=OrderRobot, multiplicity=Multiplicity(0, 9999))
    }
)
EReference00: BinaryAssociation = BinaryAssociation(
    name="EReference00",
    ends={
        Property(name="Expr", type=Legolang_Robot_OrderRobot, multiplicity=Multiplicity(1, 1)),
        Property(name="Legolang_Robot_OrderRobot", type=Expr, multiplicity=Multiplicity(0, 9999))
    }
)
instrTTque1: BinaryAssociation = BinaryAssociation(
    name="instrTTque1",
    ends={
        Property(name="Expr2", type=Legolang_controlflow_tantqueue, multiplicity=Multiplicity(1, 1)),
        Property(name="Legolang_controlflow_tantqueue", type=Expr, multiplicity=Multiplicity(0, 1))
    }
)
Cdt3: BinaryAssociation = BinaryAssociation(
    name="Cdt3",
    ends={
        Property(name="ExprBool", type=Legolang_controlflow_tantqueue, multiplicity=Multiplicity(1, 1)),
        Property(name="Legolang_controlflow_tantqueue4", type=ExprBool, multiplicity=Multiplicity(0, 1))
    }
)
cdt5: BinaryAssociation = BinaryAssociation(
    name="cdt5",
    ends={
        Property(name="ExprBool6", type=Legolang_controlflow_si, multiplicity=Multiplicity(1, 1)),
        Property(name="Legolang_controlflow_si", type=ExprBool, multiplicity=Multiplicity(0, 1))
    }
)
instrSi7: BinaryAssociation = BinaryAssociation(
    name="instrSi7",
    ends={
        Property(name="Expr9", type=Legolang_controlflow_si, multiplicity=Multiplicity(1, 1)),
        Property(name="Legolang_controlflow_si8", type=Expr, multiplicity=Multiplicity(0, 9999))
    }
)
EReference010: BinaryAssociation = BinaryAssociation(
    name="EReference010",
    ends={
        Property(name="tantqueue", type=Legolang_controlflow_Expr, multiplicity=Multiplicity(1, 1)),
        Property(name="Legolang_controlflow_Expr", type=tantqueue, multiplicity=Multiplicity(0, 1))
    }
)
EReference013: BinaryAssociation = BinaryAssociation(
    name="EReference013",
    ends={
        Property(name="opBinaire", type=Legolang_controlflow_opBinaire, multiplicity=Multiplicity(1, 1)),
        Property(name="Legolang_controlflow_opBinaire", type=opBinaire, multiplicity=Multiplicity(0, 1))
    }
)
LeftSon14: BinaryAssociation = BinaryAssociation(
    name="LeftSon14",
    ends={
        Property(name="ExprBool16", type=Legolang_controlflow_opBinaire, multiplicity=Multiplicity(1, 1)),
        Property(name="Legolang_controlflow_opBinaire15", type=ExprBool, multiplicity=Multiplicity(1, 1))
    }
)
RightSon17: BinaryAssociation = BinaryAssociation(
    name="RightSon17",
    ends={
        Property(name="ExprBool19", type=Legolang_controlflow_opBinaire, multiplicity=Multiplicity(1, 1)),
        Property(name="Legolang_controlflow_opBinaire18", type=ExprBool, multiplicity=Multiplicity(1, 1))
    }
)
EReference220: BinaryAssociation = BinaryAssociation(
    name="EReference220",
    ends={
        Property(name="tantqueue21", type=Legolang_controlflow_ExprBool, multiplicity=Multiplicity(1, 1)),
        Property(name="Legolang_controlflow_ExprBool", type=tantqueue, multiplicity=Multiplicity(0, 1))
    }
)
EReferenc022: BinaryAssociation = BinaryAssociation(
    name="EReferenc022",
    ends={
        Property(name="Expr23", type=Legolang_controlflow_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="Legolang_controlflow_Program", type=Expr, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_Legolang_controlflow_opUnaire_controlflow_operator = Generalization(general=controlflow_operator, specific=Legolang_controlflow_opUnaire)
gen_Legolang_controlflow_opUnaire_controlflow_ExprBool = Generalization(general=controlflow_ExprBool, specific=Legolang_controlflow_opUnaire)
gen_Legolang_controlflow_opBinaire_operator = Generalization(general=operator, specific=Legolang_controlflow_opBinaire)
gen_Legolang_Robot_move_OrderRobot = Generalization(general=OrderRobot, specific=Legolang_Robot_move)
gen_Legolang_Robot_bip_OrderRobot = Generalization(general=OrderRobot, specific=Legolang_Robot_bip)
gen_Legolang_Robot_turn_OrderRobot = Generalization(general=OrderRobot, specific=Legolang_Robot_turn)
gen_Legolang_Robot_stopEngine_OrderRobot = Generalization(general=OrderRobot, specific=Legolang_Robot_stopEngine)
gen_Legolang_Robot_display_OrderRobot = Generalization(general=OrderRobot, specific=Legolang_Robot_display)
gen_Legolang_Robot_turnAngle_OrderRobot = Generalization(general=OrderRobot, specific=Legolang_Robot_turnAngle)
gen_Legolang_Robot_obstacle_OrderRobot = Generalization(general=OrderRobot, specific=Legolang_Robot_obstacle)
gen_Legolang_Robot_hasTurned_OrderRobot = Generalization(general=OrderRobot, specific=Legolang_Robot_hasTurned)
gen_Legolang_controlflow_tantqueue_Expr = Generalization(general=Expr, specific=Legolang_controlflow_tantqueue)
gen_Legolang_controlflow_si_Expr = Generalization(general=Expr, specific=Legolang_controlflow_si)
gen_Legolang_controlflow_not_opUnaire = Generalization(general=opUnaire, specific=Legolang_controlflow_not)
gen_Legolang_controlflow_and_opBinaire = Generalization(general=opBinaire, specific=Legolang_controlflow_and)
gen_Legolang_controlflow_ExprBool_Expr = Generalization(general=Expr, specific=Legolang_controlflow_ExprBool)

# Domain Model
domain_model = DomainModel(
    name="Legolang",
    types={Legolang_controlflow_operator, Legolang_controlflow_opUnaire, controlflow_operator, controlflow_ExprBool, Legolang_controlflow_opBinaire, operator, opBinaire, Legolang_Robot_OrderRobot, Expr, Legolang_Robot_move, OrderRobot, Legolang_Robot_bip, Legolang_Robot_turn, Legolang_Robot_stopEngine, Legolang_Robot_display, Legolang_Robot_turnAngle, Legolang_Robot_obstacle, Legolang_Robot_hasTurned, Legolang_controlflow_tantqueue, ExprBool, Legolang_controlflow_si, Legolang_controlflow_Expr, tantqueue, Legolang_controlflow_not, opUnaire, Legolang_controlflow_and, Legolang_controlflow_ExprBool, Legolang_controlflow_Program},
    associations={fonction11, EReference00, instrTTque1, Cdt3, cdt5, instrSi7, EReference010, EReference013, LeftSon14, RightSon17, EReference220, EReferenc022},
    generalizations={gen_Legolang_controlflow_opUnaire_controlflow_operator, gen_Legolang_controlflow_opUnaire_controlflow_ExprBool, gen_Legolang_controlflow_opBinaire_operator, gen_Legolang_Robot_move_OrderRobot, gen_Legolang_Robot_bip_OrderRobot, gen_Legolang_Robot_turn_OrderRobot, gen_Legolang_Robot_stopEngine_OrderRobot, gen_Legolang_Robot_display_OrderRobot, gen_Legolang_Robot_turnAngle_OrderRobot, gen_Legolang_Robot_obstacle_OrderRobot, gen_Legolang_Robot_hasTurned_OrderRobot, gen_Legolang_controlflow_tantqueue_Expr, gen_Legolang_controlflow_si_Expr, gen_Legolang_controlflow_not_opUnaire, gen_Legolang_controlflow_and_opBinaire, gen_Legolang_controlflow_ExprBool_Expr},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)