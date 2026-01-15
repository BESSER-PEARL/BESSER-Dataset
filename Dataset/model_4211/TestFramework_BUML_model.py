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
testFramework_Greeting = Class(name="testFramework::Greeting")
testFramework_FIRSTACTION = Class(name="testFramework::FIRSTACTION")
testFramework_TABLEACTION = Class(name="testFramework::TABLEACTION")
testFramework_IDENTIFIER = Class(name="testFramework::IDENTIFIER")
testFramework_LABEL = Class(name="testFramework::LABEL")
testFramework_Model = Class(name="testFramework::Model")

# testFramework_Greeting class attributes and methods
testFramework_Greeting_testcaseValue: Property = Property(name="testcaseValue", type=IntegerType)
testFramework_Greeting_summaryDetails: Property = Property(name="summaryDetails", type=StringType)
testFramework_Greeting.attributes={testFramework_Greeting_summaryDetails, testFramework_Greeting_testcaseValue}

# testFramework_FIRSTACTION class attributes and methods
testFramework_FIRSTACTION_checktableAction: Property = Property(name="checktableAction", type=StringType)
testFramework_FIRSTACTION.attributes={testFramework_FIRSTACTION_checktableAction}

# testFramework_TABLEACTION class attributes and methods

# testFramework_IDENTIFIER class attributes and methods
testFramework_IDENTIFIER_identifiervalue: Property = Property(name="identifiervalue", type=StringType)
testFramework_IDENTIFIER.attributes={testFramework_IDENTIFIER_identifiervalue}

# testFramework_LABEL class attributes and methods
testFramework_LABEL_labelvalue: Property = Property(name="labelvalue", type=StringType)
testFramework_LABEL.attributes={testFramework_LABEL_labelvalue}

# testFramework_Model class attributes and methods

# Relationships
greetings0: BinaryAssociation = BinaryAssociation(
    name="greetings0",
    ends={
        Property(name="testFramework_Greeting", type=testFramework_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="testFramework_Model", type=testFramework_Greeting, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action1: BinaryAssociation = BinaryAssociation(
    name="action1",
    ends={
        Property(name="testFramework_FIRSTACTION", type=testFramework_Greeting, multiplicity=Multiplicity(1, 1)),
        Property(name="testFramework_Greeting2", type=testFramework_FIRSTACTION, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nextAction3: BinaryAssociation = BinaryAssociation(
    name="nextAction3",
    ends={
        Property(name="testFramework_TABLEACTION", type=testFramework_FIRSTACTION, multiplicity=Multiplicity(1, 1)),
        Property(name="testFramework_FIRSTACTION4", type=testFramework_TABLEACTION, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifierAction5: BinaryAssociation = BinaryAssociation(
    name="identifierAction5",
    ends={
        Property(name="testFramework_IDENTIFIER", type=testFramework_TABLEACTION, multiplicity=Multiplicity(1, 1)),
        Property(name="testFramework_TABLEACTION6", type=testFramework_IDENTIFIER, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nextAction7: BinaryAssociation = BinaryAssociation(
    name="nextAction7",
    ends={
        Property(name="testFramework_LABEL", type=testFramework_TABLEACTION, multiplicity=Multiplicity(1, 1)),
        Property(name="testFramework_TABLEACTION8", type=testFramework_LABEL, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="testFramework",
    types={testFramework_Greeting, testFramework_FIRSTACTION, testFramework_TABLEACTION, testFramework_IDENTIFIER, testFramework_LABEL, testFramework_Model},
    associations={greetings0, action1, nextAction3, identifierAction5, nextAction7},
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