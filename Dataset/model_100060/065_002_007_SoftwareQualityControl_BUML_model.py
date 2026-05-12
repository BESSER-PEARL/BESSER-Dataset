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
BugStatusType: Enumeration = Enumeration(
    name="BugStatusType",
    literals={
            EnumerationLiteral(name="bst_open"),
			EnumerationLiteral(name="bst_closed"),
			EnumerationLiteral(name="bst_skipped")
    }
)

# Classes
SoftwareQualityControl_ControlType = Class(name="SoftwareQualityControl_ControlType", is_abstract=True)
SoftwareQualityControl_BugTracking = Class(name="SoftwareQualityControl_BugTracking")
Bug = Class(name="Bug")
SoftwareQualityControl_DateType = Class(name="SoftwareQualityControl_DateType")
SoftwareQualityControl_ControlsSequence = Class(name="SoftwareQualityControl_ControlsSequence")
Control = Class(name="Control")
SoftwareQualityControl_Control = Class(name="SoftwareQualityControl_Control")
ControlsSequence = Class(name="ControlsSequence")
DateType = Class(name="DateType")
ControlType = Class(name="ControlType")
SoftwareQualityControl_Bug = Class(name="SoftwareQualityControl_Bug")
BugTracking = Class(name="BugTracking")

# SoftwareQualityControl_ControlType class attributes and methods

# SoftwareQualityControl_BugTracking class attributes and methods

# Bug class attributes and methods

# SoftwareQualityControl_DateType class attributes and methods
SoftwareQualityControl_DateType_day: Property = Property(name="day", type=StringType)
SoftwareQualityControl_DateType_month: Property = Property(name="month", type=StringType)
SoftwareQualityControl_DateType_year: Property = Property(name="year", type=StringType)
SoftwareQualityControl_DateType.attributes={SoftwareQualityControl_DateType_year, SoftwareQualityControl_DateType_month, SoftwareQualityControl_DateType_day}

# SoftwareQualityControl_ControlsSequence class attributes and methods

# Control class attributes and methods

# SoftwareQualityControl_Control class attributes and methods
SoftwareQualityControl_Control_responsible: Property = Property(name="responsible", type=StringType)
SoftwareQualityControl_Control_component: Property = Property(name="component", type=StringType)
SoftwareQualityControl_Control_developmentPhase: Property = Property(name="developmentPhase", type=StringType)
SoftwareQualityControl_Control_scope: Property = Property(name="scope", type=StringType)
SoftwareQualityControl_Control_controlledElt: Property = Property(name="controlledElt", type=StringType)
SoftwareQualityControl_Control_eltRef: Property = Property(name="eltRef", type=StringType)
SoftwareQualityControl_Control_eltAuthor: Property = Property(name="eltAuthor", type=StringType)
SoftwareQualityControl_Control_formRef: Property = Property(name="formRef", type=StringType)
SoftwareQualityControl_Control.attributes={SoftwareQualityControl_Control_scope, SoftwareQualityControl_Control_formRef, SoftwareQualityControl_Control_eltRef, SoftwareQualityControl_Control_developmentPhase, SoftwareQualityControl_Control_eltAuthor, SoftwareQualityControl_Control_responsible, SoftwareQualityControl_Control_controlledElt, SoftwareQualityControl_Control_component}

# ControlsSequence class attributes and methods

# DateType class attributes and methods

# ControlType class attributes and methods

# SoftwareQualityControl_Bug class attributes and methods
SoftwareQualityControl_Bug_number: Property = Property(name="number", type=StringType)
SoftwareQualityControl_Bug_componentVersion: Property = Property(name="componentVersion", type=StringType)
SoftwareQualityControl_Bug_description: Property = Property(name="description", type=StringType)
SoftwareQualityControl_Bug_status: Property = Property(name="status", type=StringType)
SoftwareQualityControl_Bug_originator: Property = Property(name="originator", type=StringType)
SoftwareQualityControl_Bug_responsible: Property = Property(name="responsible", type=StringType)
SoftwareQualityControl_Bug_commentsAnswers: Property = Property(name="commentsAnswers", type=StringType)
SoftwareQualityControl_Bug_openDate: Property = Property(name="openDate", type=StringType)
SoftwareQualityControl_Bug_closeDate: Property = Property(name="closeDate", type=StringType)
SoftwareQualityControl_Bug.attributes={SoftwareQualityControl_Bug_number, SoftwareQualityControl_Bug_responsible, SoftwareQualityControl_Bug_commentsAnswers, SoftwareQualityControl_Bug_closeDate, SoftwareQualityControl_Bug_openDate, SoftwareQualityControl_Bug_description, SoftwareQualityControl_Bug_componentVersion, SoftwareQualityControl_Bug_originator, SoftwareQualityControl_Bug_status}

# BugTracking class attributes and methods

# Relationships
type3: BinaryAssociation = BinaryAssociation(
    name="type3",
    ends={
        Property(name="ControlType", type=SoftwareQualityControl_Control, multiplicity=Multiplicity(1, 1)),
        Property(name="ct_control", type=ControlType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ct_control4: BinaryAssociation = BinaryAssociation(
    name="ct_control4",
    ends={
        Property(name="Control5", type=SoftwareQualityControl_ControlType, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=Control, multiplicity=Multiplicity(1, 1))
    }
)
controls0: BinaryAssociation = BinaryAssociation(
    name="controls0",
    ends={
        Property(name="Control", type=SoftwareQualityControl_ControlsSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="c_controlsSequence", type=Control, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
c_controlsSequence1: BinaryAssociation = BinaryAssociation(
    name="c_controlsSequence1",
    ends={
        Property(name="ControlsSequence", type=SoftwareQualityControl_Control, multiplicity=Multiplicity(1, 1)),
        Property(name="controls", type=ControlsSequence, multiplicity=Multiplicity(1, 1))
    }
)
date2: BinaryAssociation = BinaryAssociation(
    name="date2",
    ends={
        Property(name="DateType", type=SoftwareQualityControl_Control, multiplicity=Multiplicity(1, 1)),
        Property(name="SoftwareQualityControl_Control", type=DateType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bugs6: BinaryAssociation = BinaryAssociation(
    name="bugs6",
    ends={
        Property(name="Bug", type=SoftwareQualityControl_BugTracking, multiplicity=Multiplicity(1, 1)),
        Property(name="b_bugTracking", type=Bug, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
b_bugTracking7: BinaryAssociation = BinaryAssociation(
    name="b_bugTracking7",
    ends={
        Property(name="BugTracking", type=SoftwareQualityControl_Bug, multiplicity=Multiplicity(1, 1)),
        Property(name="bugs", type=BugTracking, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_SoftwareQualityControl_BugTracking_ControlType = Generalization(general=ControlType, specific=SoftwareQualityControl_BugTracking)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={SoftwareQualityControl_ControlType, SoftwareQualityControl_BugTracking, Bug, SoftwareQualityControl_DateType, SoftwareQualityControl_ControlsSequence, Control, SoftwareQualityControl_Control, ControlsSequence, DateType, ControlType, SoftwareQualityControl_Bug, BugTracking, BugStatusType},
    associations={type3, ct_control4, controls0, c_controlsSequence1, date2, bugs6, b_bugTracking7},
    generalizations={gen_SoftwareQualityControl_BugTracking_ControlType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)