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
AssistantMVC_Exam = Class(name="AssistantMVC::Exam")
AssistantMVC_ExamItem = Class(name="AssistantMVC::ExamItem")
AssistantMVC_Controller = Class(name="AssistantMVC::Controller")
AssistantMVC_Open = Class(name="AssistantMVC::Open")
ExamItem = Class(name="ExamItem")
AssistantMVC_MultipleChoice = Class(name="AssistantMVC::MultipleChoice")
AssistantMVC_Observer = Class(name="AssistantMVC::Observer")
Observer = Class(name="Observer")
AssistantMVC_View = Class(name="AssistantMVC::View")
AssistantMVC_ExamController = Class(name="AssistantMVC::ExamController")
Controller = Class(name="Controller")
AssistantMVC_ExamItemController = Class(name="AssistantMVC::ExamItemController")
AssistantMVC_MultipleChoiceController = Class(name="AssistantMVC::MultipleChoiceController")
ExamItemController = Class(name="ExamItemController")
AssistantMVC_ExamView = Class(name="AssistantMVC::ExamView")
View = Class(name="View")
AssistantMVC_ExamItemView = Class(name="AssistantMVC::ExamItemView")
AssistantMVC_OpenView = Class(name="AssistantMVC::OpenView")
ExamView = Class(name="ExamView")
AssistantMVC_MultipleChoiceView = Class(name="AssistantMVC::MultipleChoiceView")
ExamItemView = Class(name="ExamItemView")
AssistantMVC_ArrowShape = Class(name="AssistantMVC::ArrowShape")
AssistantMVC_Subgraph = Class(name="AssistantMVC::Subgraph")
AssistantMVC_OpenController = Class(name="AssistantMVC::OpenController")

# AssistantMVC_Exam class attributes and methods
AssistantMVC_Exam_question: Property = Property(name="question", type=StringType)
AssistantMVC_Exam.attributes={AssistantMVC_Exam_question}

# AssistantMVC_ExamItem class attributes and methods
AssistantMVC_ExamItem_optional: Property = Property(name="optional", type=BooleanType)
AssistantMVC_ExamItem.attributes={AssistantMVC_ExamItem_optional}

# AssistantMVC_Controller class attributes and methods

# AssistantMVC_Open class attributes and methods

# ExamItem class attributes and methods

# AssistantMVC_MultipleChoice class attributes and methods

# AssistantMVC_Observer class attributes and methods

# Observer class attributes and methods

# AssistantMVC_View class attributes and methods
AssistantMVC_View_fontName: Property = Property(name="fontName", type=StringType)
AssistantMVC_View_fontColor: Property = Property(name="fontColor", type=StringType)
AssistantMVC_View.attributes={AssistantMVC_View_fontColor, AssistantMVC_View_fontName}

# AssistantMVC_ExamController class attributes and methods

# Controller class attributes and methods

# AssistantMVC_ExamItemController class attributes and methods

# AssistantMVC_MultipleChoiceController class attributes and methods

# ExamItemController class attributes and methods

# AssistantMVC_ExamView class attributes and methods

# View class attributes and methods

# AssistantMVC_ExamItemView class attributes and methods

# AssistantMVC_OpenView class attributes and methods

# ExamView class attributes and methods

# AssistantMVC_MultipleChoiceView class attributes and methods

# ExamItemView class attributes and methods

# AssistantMVC_ArrowShape class attributes and methods
AssistantMVC_ArrowShape_value: Property = Property(name="value", type=StringType)
AssistantMVC_ArrowShape_question: Property = Property(name="question", type=StringType)
AssistantMVC_ArrowShape.attributes={AssistantMVC_ArrowShape_question, AssistantMVC_ArrowShape_value}

# AssistantMVC_Subgraph class attributes and methods

# AssistantMVC_OpenController class attributes and methods

# Relationships
examItems0: BinaryAssociation = BinaryAssociation(
    name="examItems0",
    ends={
        Property(name="AssistantMVC_ExamItem", type=AssistantMVC_Exam, multiplicity=Multiplicity(1, 1)),
        Property(name="AssistantMVC_Exam", type=AssistantMVC_ExamItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controllers1: BinaryAssociation = BinaryAssociation(
    name="controllers1",
    ends={
        Property(name="AssistantMVC_Controller", type=AssistantMVC_Exam, multiplicity=Multiplicity(1, 1)),
        Property(name="AssistantMVC_Exam2", type=AssistantMVC_Controller, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
views3: BinaryAssociation = BinaryAssociation(
    name="views3",
    ends={
        Property(name="AssistantMVC_View", type=AssistantMVC_Exam, multiplicity=Multiplicity(1, 1)),
        Property(name="AssistantMVC_Exam4", type=AssistantMVC_View, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controller5: BinaryAssociation = BinaryAssociation(
    name="controller5",
    ends={
        Property(name="AssistantMVC_Controller7", type=AssistantMVC_View, multiplicity=Multiplicity(1, 1)),
        Property(name="AssistantMVC_View6", type=AssistantMVC_Controller, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_AssistantMVC_Open_ExamItem = Generalization(general=ExamItem, specific=AssistantMVC_Open)
gen_AssistantMVC_MultipleChoice_ExamItem = Generalization(general=ExamItem, specific=AssistantMVC_MultipleChoice)
gen_AssistantMVC_Controller_Observer = Generalization(general=Observer, specific=AssistantMVC_Controller)
gen_AssistantMVC_ExamController_Controller = Generalization(general=Controller, specific=AssistantMVC_ExamController)
gen_AssistantMVC_ExamItemController_Controller = Generalization(general=Controller, specific=AssistantMVC_ExamItemController)
gen_AssistantMVC_MultipleChoiceController_ExamItemController = Generalization(general=ExamItemController, specific=AssistantMVC_MultipleChoiceController)
gen_AssistantMVC_View_Observer = Generalization(general=Observer, specific=AssistantMVC_View)
gen_AssistantMVC_ExamView_View = Generalization(general=View, specific=AssistantMVC_ExamView)
gen_AssistantMVC_ExamItemView_View = Generalization(general=View, specific=AssistantMVC_ExamItemView)
gen_AssistantMVC_OpenView_ExamView = Generalization(general=ExamView, specific=AssistantMVC_OpenView)
gen_AssistantMVC_MultipleChoiceView_ExamItemView = Generalization(general=ExamItemView, specific=AssistantMVC_MultipleChoiceView)
gen_AssistantMVC_OpenController_ExamItemController = Generalization(general=ExamItemController, specific=AssistantMVC_OpenController)

# Domain Model
domain_model = DomainModel(
    name="AssistantMVC",
    types={AssistantMVC_Exam, AssistantMVC_ExamItem, AssistantMVC_Controller, AssistantMVC_Open, ExamItem, AssistantMVC_MultipleChoice, AssistantMVC_Observer, Observer, AssistantMVC_View, AssistantMVC_ExamController, Controller, AssistantMVC_ExamItemController, AssistantMVC_MultipleChoiceController, ExamItemController, AssistantMVC_ExamView, View, AssistantMVC_ExamItemView, AssistantMVC_OpenView, ExamView, AssistantMVC_MultipleChoiceView, ExamItemView, AssistantMVC_ArrowShape, AssistantMVC_Subgraph, AssistantMVC_OpenController},
    associations={examItems0, controllers1, views3, controller5},
    generalizations={gen_AssistantMVC_Open_ExamItem, gen_AssistantMVC_MultipleChoice_ExamItem, gen_AssistantMVC_Controller_Observer, gen_AssistantMVC_ExamController_Controller, gen_AssistantMVC_ExamItemController_Controller, gen_AssistantMVC_MultipleChoiceController_ExamItemController, gen_AssistantMVC_View_Observer, gen_AssistantMVC_ExamView_View, gen_AssistantMVC_ExamItemView_View, gen_AssistantMVC_OpenView_ExamView, gen_AssistantMVC_MultipleChoiceView_ExamItemView, gen_AssistantMVC_OpenController_ExamItemController},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)