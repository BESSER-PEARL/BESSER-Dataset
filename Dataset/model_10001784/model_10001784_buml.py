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
Mines = Class(name="Mines")
genmymodelreverse_java_awt_Graphics = Class(name="genmymodelreverse_java_awt_Graphics", is_abstract=True)
genmymodelreverse_java_awt_event_MouseAdapter = Class(name="genmymodelreverse_java_awt_event_MouseAdapter", is_abstract=True)
genmymodelreverse_java_awt_event_MouseEvent = Class(name="genmymodelreverse_java_awt_event_MouseEvent")
genmymodelreverse_javax_swing_JLabel = Class(name="genmymodelreverse_javax_swing_JLabel")
genmymodelreverse_javax_swing_JPanel = Class(name="genmymodelreverse_javax_swing_JPanel")
genmymodelreverse_javax_swing_JFrame = Class(name="genmymodelreverse_javax_swing_JFrame")
genmymodelreverse_javax_swing_JMenuItem = Class(name="genmymodelreverse_javax_swing_JMenuItem")

# Mines class attributes and methods
Mines_FRAME_HEIGHT: Property = Property(name="FRAME_HEIGHT", type=IntegerType)
Mines_statusbar: Property = Property(name="statusbar", type=genmymodelreverse_javax_swing_JLabel)
Mines_timeBar: Property = Property(name="timeBar", type=genmymodelreverse_javax_swing_JLabel)
Mines_hexCell: Property = Property(name="hexCell", type=genmymodelreverse_javax_swing_JMenuItem)
Mines_FRAME_WIDTH: Property = Property(name="FRAME_WIDTH", type=IntegerType)
Mines.attributes={Mines_FRAME_WIDTH, Mines_hexCell, Mines_statusbar, Mines_FRAME_HEIGHT, Mines_timeBar}

# genmymodelreverse_java_awt_Graphics class attributes and methods

# genmymodelreverse_java_awt_event_MouseAdapter class attributes and methods

# genmymodelreverse_java_awt_event_MouseEvent class attributes and methods

# genmymodelreverse_javax_swing_JLabel class attributes and methods

# genmymodelreverse_javax_swing_JPanel class attributes and methods

# genmymodelreverse_javax_swing_JFrame class attributes and methods

# genmymodelreverse_javax_swing_JMenuItem class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_VBcakHLKEee5HMQDnOR_kg",
    types={Mines, genmymodelreverse_java_awt_Graphics, genmymodelreverse_java_awt_event_MouseAdapter, genmymodelreverse_java_awt_event_MouseEvent, genmymodelreverse_javax_swing_JLabel, genmymodelreverse_javax_swing_JPanel, genmymodelreverse_javax_swing_JFrame, genmymodelreverse_javax_swing_JMenuItem},
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