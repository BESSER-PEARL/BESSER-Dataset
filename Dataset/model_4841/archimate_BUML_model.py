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
refinement: Enumeration = Enumeration(
    name="refinement",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR")
    }
)

relationType: Enumeration = Enumeration(
    name="relationType",
    literals={
            EnumerationLiteral(name="association"),
			EnumerationLiteral(name="realization"),
			EnumerationLiteral(name="trigger"),
			EnumerationLiteral(name="composition"),
			EnumerationLiteral(name="influences")
    }
)

# Classes
MotivationElement = Class(name="MotivationElement")
archimate_ArchimateDiagram = Class(name="archimate::ArchimateDiagram")
archimate_ActiveStructureElement = Class(name="archimate::ActiveStructureElement", is_abstract=True)
archimate_MotivationElement = Class(name="archimate::MotivationElement", is_abstract=True)
archimate_BusinessElement = Class(name="archimate::BusinessElement", is_abstract=True)
archimate_StrategyElement = Class(name="archimate::StrategyElement", is_abstract=True)
archimate_Stakeholder = Class(name="archimate::Stakeholder")
ActiveStructureElement = Class(name="ActiveStructureElement")
archimate_Meaning = Class(name="archimate::Meaning")
archimate_Value = Class(name="archimate::Value")
archimate_Constraint = Class(name="archimate::Constraint")
Requirement = Class(name="Requirement")
archimate_Outcome = Class(name="archimate::Outcome")
archimate_Driver = Class(name="archimate::Driver")
archimate_Goal = Class(name="archimate::Goal")
archimate_Assessment = Class(name="archimate::Assessment")
archimate_Principle = Class(name="archimate::Principle")
archimate_Requirement = Class(name="archimate::Requirement")
archimate_Resource = Class(name="archimate::Resource")
StrategyElement = Class(name="StrategyElement")
archimate_BusinessProcess = Class(name="archimate::BusinessProcess")
BusinessElement = Class(name="BusinessElement")

# MotivationElement class attributes and methods

# archimate_ArchimateDiagram class attributes and methods

# archimate_ActiveStructureElement class attributes and methods
archimate_ActiveStructureElement_name: Property = Property(name="name", type=StringType)
archimate_ActiveStructureElement.attributes={archimate_ActiveStructureElement_name}

# archimate_MotivationElement class attributes and methods
archimate_MotivationElement_name: Property = Property(name="name", type=StringType)
archimate_MotivationElement_refinementType: Property = Property(name="refinementType", type=StringType)
archimate_MotivationElement_relationType: Property = Property(name="relationType", type=StringType)
archimate_MotivationElement.attributes={archimate_MotivationElement_name, archimate_MotivationElement_refinementType, archimate_MotivationElement_relationType}

# archimate_BusinessElement class attributes and methods
archimate_BusinessElement_name: Property = Property(name="name", type=StringType)
archimate_BusinessElement_refinementType: Property = Property(name="refinementType", type=StringType)
archimate_BusinessElement_relationType: Property = Property(name="relationType", type=StringType)
archimate_BusinessElement.attributes={archimate_BusinessElement_refinementType, archimate_BusinessElement_relationType, archimate_BusinessElement_name}

# archimate_StrategyElement class attributes and methods
archimate_StrategyElement_name: Property = Property(name="name", type=StringType)
archimate_StrategyElement_refinementType: Property = Property(name="refinementType", type=StringType)
archimate_StrategyElement_relationType: Property = Property(name="relationType", type=StringType)
archimate_StrategyElement.attributes={archimate_StrategyElement_relationType, archimate_StrategyElement_refinementType, archimate_StrategyElement_name}

# archimate_Stakeholder class attributes and methods

# ActiveStructureElement class attributes and methods

# archimate_Meaning class attributes and methods

# archimate_Value class attributes and methods

# archimate_Constraint class attributes and methods

# Requirement class attributes and methods

# archimate_Outcome class attributes and methods

# archimate_Driver class attributes and methods

# archimate_Goal class attributes and methods

# archimate_Assessment class attributes and methods

# archimate_Principle class attributes and methods

# archimate_Requirement class attributes and methods

# archimate_Resource class attributes and methods

# StrategyElement class attributes and methods

# archimate_BusinessProcess class attributes and methods

# BusinessElement class attributes and methods

# Relationships
children20: BinaryAssociation = BinaryAssociation(
    name="children20",
    ends={
        Property(name="archimate_MotivationElement21", type=archimate_MotivationElement, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_MotivationElement19", type=archimate_MotivationElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
negativeInfluence23: BinaryAssociation = BinaryAssociation(
    name="negativeInfluence23",
    ends={
        Property(name="archimate_MotivationElement24", type=archimate_MotivationElement, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_MotivationElement22", type=archimate_MotivationElement, multiplicity=Multiplicity(0, 9999))
    }
)
activestructureelement0: BinaryAssociation = BinaryAssociation(
    name="activestructureelement0",
    ends={
        Property(name="archimate_ActiveStructureElement", type=archimate_ArchimateDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_ArchimateDiagram", type=archimate_ActiveStructureElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
motivationelement1: BinaryAssociation = BinaryAssociation(
    name="motivationelement1",
    ends={
        Property(name="archimate_MotivationElement", type=archimate_ArchimateDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_ArchimateDiagram2", type=archimate_MotivationElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bussinesselement3: BinaryAssociation = BinaryAssociation(
    name="bussinesselement3",
    ends={
        Property(name="archimate_BusinessElement", type=archimate_ArchimateDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_ArchimateDiagram4", type=archimate_BusinessElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
strategyelement5: BinaryAssociation = BinaryAssociation(
    name="strategyelement5",
    ends={
        Property(name="archimate_StrategyElement", type=archimate_ArchimateDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_ArchimateDiagram6", type=archimate_StrategyElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
influences8: BinaryAssociation = BinaryAssociation(
    name="influences8",
    ends={
        Property(name="archimate_ActiveStructureElement9", type=archimate_ActiveStructureElement, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_ActiveStructureElement7", type=archimate_ActiveStructureElement, multiplicity=Multiplicity(0, 9999))
    }
)
target10: BinaryAssociation = BinaryAssociation(
    name="target10",
    ends={
        Property(name="archimate_MotivationElement12", type=archimate_ActiveStructureElement, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_ActiveStructureElement11", type=archimate_MotivationElement, multiplicity=Multiplicity(0, 9999))
    }
)
meaning13: BinaryAssociation = BinaryAssociation(
    name="meaning13",
    ends={
        Property(name="Meaning", type=archimate_Stakeholder, multiplicity=Multiplicity(1, 1)),
        Property(name="stakeholder", type=archimate_Meaning, multiplicity=Multiplicity(0, 9999))
    }
)
value14: BinaryAssociation = BinaryAssociation(
    name="value14",
    ends={
        Property(name="Value", type=archimate_Stakeholder, multiplicity=Multiplicity(1, 1)),
        Property(name="stakeholder15", type=archimate_Value, multiplicity=Multiplicity(0, 9999))
    }
)
influences17: BinaryAssociation = BinaryAssociation(
    name="influences17",
    ends={
        Property(name="archimate_MotivationElement18", type=archimate_MotivationElement, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_MotivationElement16", type=archimate_MotivationElement, multiplicity=Multiplicity(0, 9999))
    }
)
outcome47: BinaryAssociation = BinaryAssociation(
    name="outcome47",
    ends={
        Property(name="archimate_Outcome48", type=archimate_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_Requirement", type=archimate_Outcome, multiplicity=Multiplicity(0, 9999))
    }
)
goal49: BinaryAssociation = BinaryAssociation(
    name="goal49",
    ends={
        Property(name="archimate_Goal51", type=archimate_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_Requirement50", type=archimate_Goal, multiplicity=Multiplicity(0, 9999))
    }
)
children53: BinaryAssociation = BinaryAssociation(
    name="children53",
    ends={
        Property(name="archimate_StrategyElement54", type=archimate_StrategyElement, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_StrategyElement52", type=archimate_StrategyElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stakeholder25: BinaryAssociation = BinaryAssociation(
    name="stakeholder25",
    ends={
        Property(name="Stakeholder", type=archimate_Meaning, multiplicity=Multiplicity(1, 1)),
        Property(name="meaning", type=archimate_Stakeholder, multiplicity=Multiplicity(0, 9999))
    }
)
stakeholder26: BinaryAssociation = BinaryAssociation(
    name="stakeholder26",
    ends={
        Property(name="Stakeholder27", type=archimate_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="value", type=archimate_Stakeholder, multiplicity=Multiplicity(0, 9999))
    }
)
outcome28: BinaryAssociation = BinaryAssociation(
    name="outcome28",
    ends={
        Property(name="Outcome", type=archimate_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="value29", type=archimate_Outcome, multiplicity=Multiplicity(0, 9999))
    }
)
goal30: BinaryAssociation = BinaryAssociation(
    name="goal30",
    ends={
        Property(name="Goal", type=archimate_Driver, multiplicity=Multiplicity(1, 1)),
        Property(name="driver", type=archimate_Goal, multiplicity=Multiplicity(0, 9999))
    }
)
assessment31: BinaryAssociation = BinaryAssociation(
    name="assessment31",
    ends={
        Property(name="Assessment", type=archimate_Driver, multiplicity=Multiplicity(1, 1)),
        Property(name="driver32", type=archimate_Assessment, multiplicity=Multiplicity(0, 9999))
    }
)
goal33: BinaryAssociation = BinaryAssociation(
    name="goal33",
    ends={
        Property(name="Goal34", type=archimate_Assessment, multiplicity=Multiplicity(1, 1)),
        Property(name="assessment", type=archimate_Goal, multiplicity=Multiplicity(0, 9999))
    }
)
driver35: BinaryAssociation = BinaryAssociation(
    name="driver35",
    ends={
        Property(name="Driver", type=archimate_Assessment, multiplicity=Multiplicity(1, 1)),
        Property(name="assessment36", type=archimate_Driver, multiplicity=Multiplicity(0, 9999))
    }
)
driver37: BinaryAssociation = BinaryAssociation(
    name="driver37",
    ends={
        Property(name="Driver38", type=archimate_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="goal", type=archimate_Driver, multiplicity=Multiplicity(0, 9999))
    }
)
assessment39: BinaryAssociation = BinaryAssociation(
    name="assessment39",
    ends={
        Property(name="Assessment41", type=archimate_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="goal40", type=archimate_Assessment, multiplicity=Multiplicity(0, 9999))
    }
)
outcome42: BinaryAssociation = BinaryAssociation(
    name="outcome42",
    ends={
        Property(name="archimate_Goal", type=archimate_Outcome, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_Outcome", type=archimate_Goal, multiplicity=Multiplicity(0, 9999))
    }
)
value43: BinaryAssociation = BinaryAssociation(
    name="value43",
    ends={
        Property(name="Value44", type=archimate_Outcome, multiplicity=Multiplicity(1, 1)),
        Property(name="outcome", type=archimate_Value, multiplicity=Multiplicity(0, 9999))
    }
)
outcome45: BinaryAssociation = BinaryAssociation(
    name="outcome45",
    ends={
        Property(name="archimate_Outcome46", type=archimate_Principle, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_Principle", type=archimate_Outcome, multiplicity=Multiplicity(0, 9999))
    }
)
influences55: BinaryAssociation = BinaryAssociation(
    name="influences55",
    ends={
        Property(name="archimate_MotivationElement57", type=archimate_StrategyElement, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_StrategyElement56", type=archimate_MotivationElement, multiplicity=Multiplicity(0, 9999))
    }
)
children59: BinaryAssociation = BinaryAssociation(
    name="children59",
    ends={
        Property(name="archimate_BusinessElement60", type=archimate_BusinessElement, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_BusinessElement58", type=archimate_BusinessElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
realizes61: BinaryAssociation = BinaryAssociation(
    name="realizes61",
    ends={
        Property(name="archimate_MotivationElement63", type=archimate_BusinessElement, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_BusinessElement62", type=archimate_MotivationElement, multiplicity=Multiplicity(0, 9999))
    }
)
influences64: BinaryAssociation = BinaryAssociation(
    name="influences64",
    ends={
        Property(name="archimate_MotivationElement66", type=archimate_BusinessElement, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_BusinessElement65", type=archimate_MotivationElement, multiplicity=Multiplicity(0, 9999))
    }
)
triggers68: BinaryAssociation = BinaryAssociation(
    name="triggers68",
    ends={
        Property(name="archimate_BusinessElement69", type=archimate_BusinessElement, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_BusinessElement67", type=archimate_BusinessElement, multiplicity=Multiplicity(0, 1))
    }
)
negativeInfluence70: BinaryAssociation = BinaryAssociation(
    name="negativeInfluence70",
    ends={
        Property(name="archimate_MotivationElement72", type=archimate_BusinessElement, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_BusinessElement71", type=archimate_MotivationElement, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_archimate_Meaning_MotivationElement = Generalization(general=MotivationElement, specific=archimate_Meaning)
gen_archimate_Stakeholder_ActiveStructureElement = Generalization(general=ActiveStructureElement, specific=archimate_Stakeholder)
gen_archimate_Constraint_Requirement = Generalization(general=Requirement, specific=archimate_Constraint)
gen_archimate_Value_MotivationElement = Generalization(general=MotivationElement, specific=archimate_Value)
gen_archimate_Driver_MotivationElement = Generalization(general=MotivationElement, specific=archimate_Driver)
gen_archimate_Assessment_MotivationElement = Generalization(general=MotivationElement, specific=archimate_Assessment)
gen_archimate_Goal_MotivationElement = Generalization(general=MotivationElement, specific=archimate_Goal)
gen_archimate_Outcome_MotivationElement = Generalization(general=MotivationElement, specific=archimate_Outcome)
gen_archimate_Principle_MotivationElement = Generalization(general=MotivationElement, specific=archimate_Principle)
gen_archimate_Requirement_MotivationElement = Generalization(general=MotivationElement, specific=archimate_Requirement)
gen_archimate_Resource_StrategyElement = Generalization(general=StrategyElement, specific=archimate_Resource)
gen_archimate_BusinessProcess_BusinessElement = Generalization(general=BusinessElement, specific=archimate_BusinessProcess)

# Domain Model
domain_model = DomainModel(
    name="archimate",
    types={MotivationElement, archimate_ArchimateDiagram, archimate_ActiveStructureElement, archimate_MotivationElement, archimate_BusinessElement, archimate_StrategyElement, archimate_Stakeholder, ActiveStructureElement, archimate_Meaning, archimate_Value, archimate_Constraint, Requirement, archimate_Outcome, archimate_Driver, archimate_Goal, archimate_Assessment, archimate_Principle, archimate_Requirement, archimate_Resource, StrategyElement, archimate_BusinessProcess, BusinessElement, refinement, relationType},
    associations={children20, negativeInfluence23, activestructureelement0, motivationelement1, bussinesselement3, strategyelement5, influences8, target10, meaning13, value14, influences17, outcome47, goal49, children53, stakeholder25, stakeholder26, outcome28, goal30, assessment31, goal33, driver35, driver37, assessment39, outcome42, value43, outcome45, influences55, children59, realizes61, influences64, triggers68, negativeInfluence70},
    generalizations={gen_archimate_Meaning_MotivationElement, gen_archimate_Stakeholder_ActiveStructureElement, gen_archimate_Constraint_Requirement, gen_archimate_Value_MotivationElement, gen_archimate_Driver_MotivationElement, gen_archimate_Assessment_MotivationElement, gen_archimate_Goal_MotivationElement, gen_archimate_Outcome_MotivationElement, gen_archimate_Principle_MotivationElement, gen_archimate_Requirement_MotivationElement, gen_archimate_Resource_StrategyElement, gen_archimate_BusinessProcess_BusinessElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)