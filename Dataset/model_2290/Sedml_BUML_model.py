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
sedml_sedML = Class(name="sedml::sedML")
sedml_listOfSimulations = Class(name="sedml::listOfSimulations")
sedml_listOfModels = Class(name="sedml::listOfModels")
sedml_listOfDataGenerators = Class(name="sedml::listOfDataGenerators")
sedml_listOfOutputs = Class(name="sedml::listOfOutputs")
sedml_uniformTimeCourse = Class(name="sedml::uniformTimeCourse")
sedml_listOfTasks = Class(name="sedml::listOfTasks")
sedml_task = Class(name="sedml::task")
sedml_dataGenerator = Class(name="sedml::dataGenerator")
sedml_plot2D = Class(name="sedml::plot2D")
sedml_model = Class(name="sedml::model")
sedml_algorithm = Class(name="sedml::algorithm")
sedml_listOfCurves = Class(name="sedml::listOfCurves")
sedml_curve = Class(name="sedml::curve")
sedml_listOfVariables = Class(name="sedml::listOfVariables")
sedml_math = Class(name="sedml::math")
sedml_variable = Class(name="sedml::variable")

# sedml_sedML class attributes and methods
sedml_sedML_version: Property = Property(name="version", type=IntegerType)
sedml_sedML_level: Property = Property(name="level", type=IntegerType)
sedml_sedML.attributes={sedml_sedML_level, sedml_sedML_version}

# sedml_listOfSimulations class attributes and methods

# sedml_listOfModels class attributes and methods

# sedml_listOfDataGenerators class attributes and methods

# sedml_listOfOutputs class attributes and methods

# sedml_uniformTimeCourse class attributes and methods
sedml_uniformTimeCourse_id: Property = Property(name="id", type=StringType)
sedml_uniformTimeCourse_outputEndTime: Property = Property(name="outputEndTime", type=IntegerType)
sedml_uniformTimeCourse_numberOfPoints: Property = Property(name="numberOfPoints", type=IntegerType)
sedml_uniformTimeCourse_initialTime: Property = Property(name="initialTime", type=IntegerType)
sedml_uniformTimeCourse_outputStartTime: Property = Property(name="outputStartTime", type=IntegerType)
sedml_uniformTimeCourse.attributes={sedml_uniformTimeCourse_initialTime, sedml_uniformTimeCourse_outputStartTime, sedml_uniformTimeCourse_numberOfPoints, sedml_uniformTimeCourse_outputEndTime, sedml_uniformTimeCourse_id}

# sedml_listOfTasks class attributes and methods

# sedml_task class attributes and methods
sedml_task_name: Property = Property(name="name", type=StringType)
sedml_task_id: Property = Property(name="id", type=StringType)
sedml_task.attributes={sedml_task_id, sedml_task_name}

# sedml_dataGenerator class attributes and methods
sedml_dataGenerator_id: Property = Property(name="id", type=StringType)
sedml_dataGenerator_name: Property = Property(name="name", type=StringType)
sedml_dataGenerator.attributes={sedml_dataGenerator_name, sedml_dataGenerator_id}

# sedml_plot2D class attributes and methods
sedml_plot2D_id: Property = Property(name="id", type=StringType)
sedml_plot2D_name: Property = Property(name="name", type=StringType)
sedml_plot2D.attributes={sedml_plot2D_id, sedml_plot2D_name}

# sedml_model class attributes and methods
sedml_model_id: Property = Property(name="id", type=StringType)
sedml_model_language: Property = Property(name="language", type=StringType)
sedml_model_source: Property = Property(name="source", type=StringType)
sedml_model_name: Property = Property(name="name", type=StringType)
sedml_model.attributes={sedml_model_source, sedml_model_id, sedml_model_language, sedml_model_name}

# sedml_algorithm class attributes and methods
sedml_algorithm_kisaoID: Property = Property(name="kisaoID", type=StringType)
sedml_algorithm.attributes={sedml_algorithm_kisaoID}

# sedml_listOfCurves class attributes and methods

# sedml_curve class attributes and methods
sedml_curve_id: Property = Property(name="id", type=StringType)
sedml_curve_logX: Property = Property(name="logX", type=StringType)
sedml_curve_logY: Property = Property(name="logY", type=StringType)
sedml_curve_xDataReference: Property = Property(name="xDataReference", type=StringType)
sedml_curve_yDataReference: Property = Property(name="yDataReference", type=StringType)
sedml_curve.attributes={sedml_curve_yDataReference, sedml_curve_id, sedml_curve_xDataReference, sedml_curve_logX, sedml_curve_logY}

# sedml_listOfVariables class attributes and methods

# sedml_math class attributes and methods
sedml_math_xlms: Property = Property(name="xlms", type=StringType)
sedml_math.attributes={sedml_math_xlms}

# sedml_variable class attributes and methods
sedml_variable_id: Property = Property(name="id", type=StringType)
sedml_variable_target: Property = Property(name="target", type=StringType)
sedml_variable_symbol: Property = Property(name="symbol", type=StringType)
sedml_variable.attributes={sedml_variable_symbol, sedml_variable_id, sedml_variable_target}

# Relationships
listOfSimulations0: BinaryAssociation = BinaryAssociation(
    name="listOfSimulations0",
    ends={
        Property(name="sedml_listOfSimulations", type=sedml_sedML, multiplicity=Multiplicity(1, 1)),
        Property(name="sedml_sedML", type=sedml_listOfSimulations, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
listOfTasks3: BinaryAssociation = BinaryAssociation(
    name="listOfTasks3",
    ends={
        Property(name="sedml_listOfTasks", type=sedml_sedML, multiplicity=Multiplicity(1, 1)),
        Property(name="sedml_sedML4", type=sedml_listOfTasks, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
listOfDataGenerators5: BinaryAssociation = BinaryAssociation(
    name="listOfDataGenerators5",
    ends={
        Property(name="sedml_listOfDataGenerators", type=sedml_sedML, multiplicity=Multiplicity(1, 1)),
        Property(name="sedml_sedML6", type=sedml_listOfDataGenerators, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
listOfOutputs7: BinaryAssociation = BinaryAssociation(
    name="listOfOutputs7",
    ends={
        Property(name="sedml_listOfOutputs", type=sedml_sedML, multiplicity=Multiplicity(1, 1)),
        Property(name="sedml_sedML8", type=sedml_listOfOutputs, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
uniformTimeCourse9: BinaryAssociation = BinaryAssociation(
    name="uniformTimeCourse9",
    ends={
        Property(name="sedml_uniformTimeCourse", type=sedml_listOfSimulations, multiplicity=Multiplicity(1, 1)),
        Property(name="sedml_listOfSimulations10", type=sedml_uniformTimeCourse, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listOfModels1: BinaryAssociation = BinaryAssociation(
    name="listOfModels1",
    ends={
        Property(name="sedml_listOfModels", type=sedml_sedML, multiplicity=Multiplicity(1, 1)),
        Property(name="sedml_sedML2", type=sedml_listOfModels, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
task13: BinaryAssociation = BinaryAssociation(
    name="task13",
    ends={
        Property(name="sedml_task", type=sedml_listOfTasks, multiplicity=Multiplicity(1, 1)),
        Property(name="sedml_listOfTasks14", type=sedml_task, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataGenerator15: BinaryAssociation = BinaryAssociation(
    name="dataGenerator15",
    ends={
        Property(name="sedml_dataGenerator", type=sedml_listOfDataGenerators, multiplicity=Multiplicity(1, 1)),
        Property(name="sedml_listOfDataGenerators16", type=sedml_dataGenerator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
plot2D17: BinaryAssociation = BinaryAssociation(
    name="plot2D17",
    ends={
        Property(name="sedml_plot2D", type=sedml_listOfOutputs, multiplicity=Multiplicity(1, 1)),
        Property(name="sedml_listOfOutputs18", type=sedml_plot2D, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model11: BinaryAssociation = BinaryAssociation(
    name="model11",
    ends={
        Property(name="sedml_model", type=sedml_listOfModels, multiplicity=Multiplicity(1, 1)),
        Property(name="sedml_listOfModels12", type=sedml_model, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
algorithm19: BinaryAssociation = BinaryAssociation(
    name="algorithm19",
    ends={
        Property(name="sedml_algorithm", type=sedml_uniformTimeCourse, multiplicity=Multiplicity(1, 1)),
        Property(name="sedml_uniformTimeCourse20", type=sedml_algorithm, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
modelReference21: BinaryAssociation = BinaryAssociation(
    name="modelReference21",
    ends={
        Property(name="sedml_model23", type=sedml_task, multiplicity=Multiplicity(1, 1)),
        Property(name="sedml_task22", type=sedml_model, multiplicity=Multiplicity(1, 1))
    }
)
simulationReference24: BinaryAssociation = BinaryAssociation(
    name="simulationReference24",
    ends={
        Property(name="sedml_uniformTimeCourse26", type=sedml_task, multiplicity=Multiplicity(1, 1)),
        Property(name="sedml_task25", type=sedml_uniformTimeCourse, multiplicity=Multiplicity(1, 1))
    }
)
listOfCurves27: BinaryAssociation = BinaryAssociation(
    name="listOfCurves27",
    ends={
        Property(name="sedml_listOfCurves", type=sedml_plot2D, multiplicity=Multiplicity(1, 1)),
        Property(name="sedml_plot2D28", type=sedml_listOfCurves, multiplicity=Multiplicity(1, 1))
    }
)
curve29: BinaryAssociation = BinaryAssociation(
    name="curve29",
    ends={
        Property(name="sedml_curve", type=sedml_listOfCurves, multiplicity=Multiplicity(1, 1)),
        Property(name="sedml_listOfCurves30", type=sedml_curve, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listOfVariables31: BinaryAssociation = BinaryAssociation(
    name="listOfVariables31",
    ends={
        Property(name="sedml_listOfVariables", type=sedml_dataGenerator, multiplicity=Multiplicity(1, 1)),
        Property(name="sedml_dataGenerator32", type=sedml_listOfVariables, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
math33: BinaryAssociation = BinaryAssociation(
    name="math33",
    ends={
        Property(name="sedml_math", type=sedml_dataGenerator, multiplicity=Multiplicity(1, 1)),
        Property(name="sedml_dataGenerator34", type=sedml_math, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable35: BinaryAssociation = BinaryAssociation(
    name="variable35",
    ends={
        Property(name="sedml_variable", type=sedml_listOfVariables, multiplicity=Multiplicity(1, 1)),
        Property(name="sedml_listOfVariables36", type=sedml_variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
taskReference37: BinaryAssociation = BinaryAssociation(
    name="taskReference37",
    ends={
        Property(name="sedml_task39", type=sedml_variable, multiplicity=Multiplicity(1, 1)),
        Property(name="sedml_variable38", type=sedml_task, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="sedml",
    types={sedml_sedML, sedml_listOfSimulations, sedml_listOfModels, sedml_listOfDataGenerators, sedml_listOfOutputs, sedml_uniformTimeCourse, sedml_listOfTasks, sedml_task, sedml_dataGenerator, sedml_plot2D, sedml_model, sedml_algorithm, sedml_listOfCurves, sedml_curve, sedml_listOfVariables, sedml_math, sedml_variable},
    associations={listOfSimulations0, listOfTasks3, listOfDataGenerators5, listOfOutputs7, uniformTimeCourse9, listOfModels1, task13, dataGenerator15, plot2D17, model11, algorithm19, modelReference21, simulationReference24, listOfCurves27, curve29, listOfVariables31, math33, variable35, taskReference37},
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