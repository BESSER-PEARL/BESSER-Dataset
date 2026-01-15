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
gama_EGamaModel = Class(name="gama::EGamaModel")
gama_EGamaObject = Class(name="gama::EGamaObject")
gama_EGamaLink = Class(name="gama::EGamaLink")
gama_EFacet = Class(name="gama::EFacet")
gama_ESpecies = Class(name="gama::ESpecies")
EGamaObject = Class(name="EGamaObject")
gama_EVariable = Class(name="gama::EVariable")
gama_EExperimentLink = Class(name="gama::EExperimentLink")
gama_EAspectLink = Class(name="gama::EAspectLink")
gama_EActionLink = Class(name="gama::EActionLink")
gama_EReflexLink = Class(name="gama::EReflexLink")
gama_ESubSpeciesLink = Class(name="gama::ESubSpeciesLink")
gama_EPlanLink = Class(name="gama::EPlanLink")
gama_EStateLink = Class(name="gama::EStateLink")
gama_ETaskLink = Class(name="gama::ETaskLink")
gama_EPerceiveLink = Class(name="gama::EPerceiveLink")
gama_ERuleLink = Class(name="gama::ERuleLink")
gama_EEquationLink = Class(name="gama::EEquationLink")
gama_EAction = Class(name="gama::EAction")
gama_EAspect = Class(name="gama::EAspect")
gama_ELayerAspect = Class(name="gama::ELayerAspect")
gama_EReflex = Class(name="gama::EReflex")
gama_EExperiment = Class(name="gama::EExperiment")
ESpecies = Class(name="ESpecies")
gama_EInheritLink = Class(name="gama::EInheritLink")
gama_EDisplayLink = Class(name="gama::EDisplayLink")
gama_EParameter = Class(name="gama::EParameter")
gama_EMonitor = Class(name="gama::EMonitor")
gama_EGUIExperiment = Class(name="gama::EGUIExperiment")
EExperiment = Class(name="EExperiment")
gama_EBatchExperiment = Class(name="gama::EBatchExperiment")
EGamaLink = Class(name="EGamaLink")
gama_EDisplay = Class(name="gama::EDisplay")
gama_ELayer = Class(name="gama::ELayer")
gama_EWorldAgent = Class(name="gama::EWorldAgent")
gama_EChartLayer = Class(name="gama::EChartLayer")
gama_EPlan = Class(name="gama::EPlan")
gama_EState = Class(name="gama::EState")
gama_ETask = Class(name="gama::ETask")
gama_EGrid = Class(name="gama::EGrid")
gama_EPerceive = Class(name="gama::EPerceive")
gama_ERule = Class(name="gama::ERule")
gama_EEquation = Class(name="gama::EEquation")

# gama_EGamaModel class attributes and methods
gama_EGamaModel_name: Property = Property(name="name", type=StringType)
gama_EGamaModel.attributes={gama_EGamaModel_name}

# gama_EGamaObject class attributes and methods
gama_EGamaObject_name: Property = Property(name="name", type=StringType)
gama_EGamaObject_colorPicto: Property = Property(name="colorPicto", type=StringType)
gama_EGamaObject_hasError: Property = Property(name="hasError", type=StringType)
gama_EGamaObject_error: Property = Property(name="error", type=StringType)
gama_EGamaObject.attributes={gama_EGamaObject_colorPicto, gama_EGamaObject_hasError, gama_EGamaObject_error, gama_EGamaObject_name}

# gama_EGamaLink class attributes and methods

# gama_EFacet class attributes and methods
gama_EFacet_name: Property = Property(name="name", type=StringType)
gama_EFacet_value: Property = Property(name="value", type=StringType)
gama_EFacet.attributes={gama_EFacet_name, gama_EFacet_value}

# gama_ESpecies class attributes and methods
gama_ESpecies_reflexList: Property = Property(name="reflexList", type=StringType)
gama_ESpecies_skills: Property = Property(name="skills", type=StringType)
gama_ESpecies_init: Property = Property(name="init", type=StringType)
gama_ESpecies.attributes={gama_ESpecies_reflexList, gama_ESpecies_init, gama_ESpecies_skills}

# EGamaObject class attributes and methods

# gama_EVariable class attributes and methods
gama_EVariable_init: Property = Property(name="init", type=StringType)
gama_EVariable_min: Property = Property(name="min", type=StringType)
gama_EVariable_max: Property = Property(name="max", type=StringType)
gama_EVariable_update: Property = Property(name="update", type=StringType)
gama_EVariable_function: Property = Property(name="function", type=StringType)
gama_EVariable_type: Property = Property(name="type", type=StringType)
gama_EVariable_name: Property = Property(name="name", type=StringType)
gama_EVariable_hasError: Property = Property(name="hasError", type=StringType)
gama_EVariable_error: Property = Property(name="error", type=StringType)
gama_EVariable.attributes={gama_EVariable_hasError, gama_EVariable_min, gama_EVariable_name, gama_EVariable_max, gama_EVariable_init, gama_EVariable_update, gama_EVariable_error, gama_EVariable_type, gama_EVariable_function}

# gama_EExperimentLink class attributes and methods

# gama_EAspectLink class attributes and methods

# gama_EActionLink class attributes and methods

# gama_EReflexLink class attributes and methods

# gama_ESubSpeciesLink class attributes and methods

# gama_EPlanLink class attributes and methods

# gama_EStateLink class attributes and methods

# gama_ETaskLink class attributes and methods

# gama_EPerceiveLink class attributes and methods

# gama_ERuleLink class attributes and methods

# gama_EEquationLink class attributes and methods

# gama_EAction class attributes and methods
gama_EAction_gamlCode: Property = Property(name="gamlCode", type=StringType)
gama_EAction_returnType: Property = Property(name="returnType", type=StringType)
gama_EAction.attributes={gama_EAction_gamlCode, gama_EAction_returnType}

# gama_EAspect class attributes and methods
gama_EAspect_gamlCode: Property = Property(name="gamlCode", type=StringType)
gama_EAspect_defineGamlCode: Property = Property(name="defineGamlCode", type=BooleanType)
gama_EAspect.attributes={gama_EAspect_defineGamlCode, gama_EAspect_gamlCode}

# gama_ELayerAspect class attributes and methods
gama_ELayerAspect_gamlCode: Property = Property(name="gamlCode", type=StringType)
gama_ELayerAspect_shape: Property = Property(name="shape", type=StringType)
gama_ELayerAspect_color: Property = Property(name="color", type=StringType)
gama_ELayerAspect_empty: Property = Property(name="empty", type=StringType)
gama_ELayerAspect_rotate: Property = Property(name="rotate", type=StringType)
gama_ELayerAspect_size: Property = Property(name="size", type=StringType)
gama_ELayerAspect_width: Property = Property(name="width", type=StringType)
gama_ELayerAspect_heigth: Property = Property(name="heigth", type=StringType)
gama_ELayerAspect_radius: Property = Property(name="radius", type=StringType)
gama_ELayerAspect_path: Property = Property(name="path", type=StringType)
gama_ELayerAspect_text: Property = Property(name="text", type=StringType)
gama_ELayerAspect_type: Property = Property(name="type", type=StringType)
gama_ELayerAspect_expression: Property = Property(name="expression", type=StringType)
gama_ELayerAspect_points: Property = Property(name="points", type=StringType)
gama_ELayerAspect_at: Property = Property(name="at", type=StringType)
gama_ELayerAspect_shapeType: Property = Property(name="shapeType", type=StringType)
gama_ELayerAspect_isColorCst: Property = Property(name="isColorCst", type=StringType)
gama_ELayerAspect_textSize: Property = Property(name="textSize", type=StringType)
gama_ELayerAspect_imageSize: Property = Property(name="imageSize", type=StringType)
gama_ELayerAspect_colorRBG: Property = Property(name="colorRBG", type=StringType)
gama_ELayerAspect_depth: Property = Property(name="depth", type=StringType)
gama_ELayerAspect_texture: Property = Property(name="texture", type=StringType)
gama_ELayerAspect.attributes={gama_ELayerAspect_empty, gama_ELayerAspect_rotate, gama_ELayerAspect_width, gama_ELayerAspect_radius, gama_ELayerAspect_heigth, gama_ELayerAspect_shapeType, gama_ELayerAspect_type, gama_ELayerAspect_color, gama_ELayerAspect_text, gama_ELayerAspect_points, gama_ELayerAspect_imageSize, gama_ELayerAspect_texture, gama_ELayerAspect_size, gama_ELayerAspect_path, gama_ELayerAspect_gamlCode, gama_ELayerAspect_shape, gama_ELayerAspect_at, gama_ELayerAspect_isColorCst, gama_ELayerAspect_depth, gama_ELayerAspect_expression, gama_ELayerAspect_colorRBG, gama_ELayerAspect_textSize}

# gama_EReflex class attributes and methods
gama_EReflex_gamlCode: Property = Property(name="gamlCode", type=StringType)
gama_EReflex.attributes={gama_EReflex_gamlCode}

# gama_EExperiment class attributes and methods

# ESpecies class attributes and methods

# gama_EInheritLink class attributes and methods

# gama_EDisplayLink class attributes and methods

# gama_EParameter class attributes and methods
gama_EParameter_variable: Property = Property(name="variable", type=StringType)
gama_EParameter_min: Property = Property(name="min", type=StringType)
gama_EParameter_init: Property = Property(name="init", type=StringType)
gama_EParameter_step: Property = Property(name="step", type=StringType)
gama_EParameter_max: Property = Property(name="max", type=StringType)
gama_EParameter_among: Property = Property(name="among", type=StringType)
gama_EParameter_category: Property = Property(name="category", type=StringType)
gama_EParameter.attributes={gama_EParameter_min, gama_EParameter_step, gama_EParameter_category, gama_EParameter_max, gama_EParameter_init, gama_EParameter_variable, gama_EParameter_among}

# gama_EMonitor class attributes and methods
gama_EMonitor_value: Property = Property(name="value", type=StringType)
gama_EMonitor.attributes={gama_EMonitor_value}

# gama_EGUIExperiment class attributes and methods

# EExperiment class attributes and methods

# gama_EBatchExperiment class attributes and methods

# EGamaLink class attributes and methods

# gama_EDisplay class attributes and methods
gama_EDisplay_layerList: Property = Property(name="layerList", type=StringType)
gama_EDisplay_gamlCode: Property = Property(name="gamlCode", type=StringType)
gama_EDisplay_defineGamlCode: Property = Property(name="defineGamlCode", type=BooleanType)
gama_EDisplay.attributes={gama_EDisplay_gamlCode, gama_EDisplay_layerList, gama_EDisplay_defineGamlCode}

# gama_ELayer class attributes and methods
gama_ELayer_gamlCode: Property = Property(name="gamlCode", type=StringType)
gama_ELayer_type: Property = Property(name="type", type=StringType)
gama_ELayer_file: Property = Property(name="file", type=StringType)
gama_ELayer_isColorCst: Property = Property(name="isColorCst", type=StringType)
gama_ELayer_colorRBG: Property = Property(name="colorRBG", type=StringType)
gama_ELayer_grid: Property = Property(name="grid", type=StringType)
gama_ELayer_chart_type: Property = Property(name="chart_type", type=StringType)
gama_ELayer_showLines: Property = Property(name="showLines", type=BooleanType)
gama_ELayer_text: Property = Property(name="text", type=StringType)
gama_ELayer_size: Property = Property(name="size", type=StringType)
gama_ELayer_species: Property = Property(name="species", type=StringType)
gama_ELayer_agents: Property = Property(name="agents", type=StringType)
gama_ELayer_aspect: Property = Property(name="aspect", type=StringType)
gama_ELayer_color: Property = Property(name="color", type=StringType)
gama_ELayer.attributes={gama_ELayer_text, gama_ELayer_grid, gama_ELayer_type, gama_ELayer_isColorCst, gama_ELayer_species, gama_ELayer_color, gama_ELayer_file, gama_ELayer_colorRBG, gama_ELayer_size, gama_ELayer_showLines, gama_ELayer_agents, gama_ELayer_gamlCode, gama_ELayer_aspect, gama_ELayer_chart_type}

# gama_EWorldAgent class attributes and methods

# gama_EChartLayer class attributes and methods
gama_EChartLayer_style: Property = Property(name="style", type=StringType)
gama_EChartLayer_color: Property = Property(name="color", type=StringType)
gama_EChartLayer_value: Property = Property(name="value", type=StringType)
gama_EChartLayer.attributes={gama_EChartLayer_color, gama_EChartLayer_value, gama_EChartLayer_style}

# gama_EPlan class attributes and methods
gama_EPlan_gamlCode: Property = Property(name="gamlCode", type=StringType)
gama_EPlan.attributes={gama_EPlan_gamlCode}

# gama_EState class attributes and methods
gama_EState_gamlCode: Property = Property(name="gamlCode", type=StringType)
gama_EState.attributes={gama_EState_gamlCode}

# gama_ETask class attributes and methods
gama_ETask_gamlCode: Property = Property(name="gamlCode", type=StringType)
gama_ETask.attributes={gama_ETask_gamlCode}

# gama_EGrid class attributes and methods

# gama_EPerceive class attributes and methods
gama_EPerceive_gamlCode: Property = Property(name="gamlCode", type=StringType)
gama_EPerceive.attributes={gama_EPerceive_gamlCode}

# gama_ERule class attributes and methods
gama_ERule_gamlCode: Property = Property(name="gamlCode", type=StringType)
gama_ERule.attributes={gama_ERule_gamlCode}

# gama_EEquation class attributes and methods
gama_EEquation_gamlCode: Property = Property(name="gamlCode", type=StringType)
gama_EEquation.attributes={gama_EEquation_gamlCode}

# Relationships
links1: BinaryAssociation = BinaryAssociation(
    name="links1",
    ends={
        Property(name="EGamaLink", type=gama_EGamaModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model2", type=gama_EGamaLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model3: BinaryAssociation = BinaryAssociation(
    name="model3",
    ends={
        Property(name="EGamaModel", type=gama_EGamaObject, multiplicity=Multiplicity(1, 1)),
        Property(name="objects", type=gama_EGamaModel, multiplicity=Multiplicity(1, 1))
    }
)
facets4: BinaryAssociation = BinaryAssociation(
    name="facets4",
    ends={
        Property(name="gama_EFacet", type=gama_EGamaObject, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EGamaObject", type=gama_EFacet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables5: BinaryAssociation = BinaryAssociation(
    name="variables5",
    ends={
        Property(name="gama_EVariable", type=gama_ESpecies, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_ESpecies", type=gama_EVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
experimentLinks6: BinaryAssociation = BinaryAssociation(
    name="experimentLinks6",
    ends={
        Property(name="gama_EExperimentLink", type=gama_ESpecies, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_ESpecies7", type=gama_EExperimentLink, multiplicity=Multiplicity(0, 9999))
    }
)
aspectLinks8: BinaryAssociation = BinaryAssociation(
    name="aspectLinks8",
    ends={
        Property(name="gama_EAspectLink", type=gama_ESpecies, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_ESpecies9", type=gama_EAspectLink, multiplicity=Multiplicity(0, 9999))
    }
)
actionLinks10: BinaryAssociation = BinaryAssociation(
    name="actionLinks10",
    ends={
        Property(name="gama_EActionLink", type=gama_ESpecies, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_ESpecies11", type=gama_EActionLink, multiplicity=Multiplicity(0, 9999))
    }
)
reflexLinks12: BinaryAssociation = BinaryAssociation(
    name="reflexLinks12",
    ends={
        Property(name="gama_EReflexLink", type=gama_ESpecies, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_ESpecies13", type=gama_EReflexLink, multiplicity=Multiplicity(0, 9999))
    }
)
microSpeciesLinks14: BinaryAssociation = BinaryAssociation(
    name="microSpeciesLinks14",
    ends={
        Property(name="gama_ESubSpeciesLink", type=gama_ESpecies, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_ESpecies15", type=gama_ESubSpeciesLink, multiplicity=Multiplicity(0, 9999))
    }
)
macroSpeciesLinks16: BinaryAssociation = BinaryAssociation(
    name="macroSpeciesLinks16",
    ends={
        Property(name="gama_ESubSpeciesLink18", type=gama_ESpecies, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_ESpecies17", type=gama_ESubSpeciesLink, multiplicity=Multiplicity(0, 9999))
    }
)
inheritsFrom20: BinaryAssociation = BinaryAssociation(
    name="inheritsFrom20",
    ends={
        Property(name="gama_ESpecies21", type=gama_ESpecies, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_ESpecies19", type=gama_ESpecies, multiplicity=Multiplicity(0, 1))
    }
)
objects0: BinaryAssociation = BinaryAssociation(
    name="objects0",
    ends={
        Property(name="EGamaObject", type=gama_EGamaModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model", type=gama_EGamaObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
planLinks24: BinaryAssociation = BinaryAssociation(
    name="planLinks24",
    ends={
        Property(name="gama_EPlanLink", type=gama_ESpecies, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_ESpecies25", type=gama_EPlanLink, multiplicity=Multiplicity(0, 9999))
    }
)
stateLinks26: BinaryAssociation = BinaryAssociation(
    name="stateLinks26",
    ends={
        Property(name="gama_EStateLink", type=gama_ESpecies, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_ESpecies27", type=gama_EStateLink, multiplicity=Multiplicity(0, 9999))
    }
)
taskLinks28: BinaryAssociation = BinaryAssociation(
    name="taskLinks28",
    ends={
        Property(name="gama_ETaskLink", type=gama_ESpecies, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_ESpecies29", type=gama_ETaskLink, multiplicity=Multiplicity(0, 9999))
    }
)
perceiveLinks30: BinaryAssociation = BinaryAssociation(
    name="perceiveLinks30",
    ends={
        Property(name="gama_EPerceiveLink", type=gama_ESpecies, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_ESpecies31", type=gama_EPerceiveLink, multiplicity=Multiplicity(0, 9999))
    }
)
ruleLinks32: BinaryAssociation = BinaryAssociation(
    name="ruleLinks32",
    ends={
        Property(name="gama_ERuleLink", type=gama_ESpecies, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_ESpecies33", type=gama_ERuleLink, multiplicity=Multiplicity(0, 9999))
    }
)
equationLinks34: BinaryAssociation = BinaryAssociation(
    name="equationLinks34",
    ends={
        Property(name="gama_EEquationLink", type=gama_ESpecies, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_ESpecies35", type=gama_EEquationLink, multiplicity=Multiplicity(0, 9999))
    }
)
actionLinks36: BinaryAssociation = BinaryAssociation(
    name="actionLinks36",
    ends={
        Property(name="gama_EActionLink37", type=gama_EAction, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EAction", type=gama_EActionLink, multiplicity=Multiplicity(0, 9999))
    }
)
variables38: BinaryAssociation = BinaryAssociation(
    name="variables38",
    ends={
        Property(name="gama_EVariable40", type=gama_EAction, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EAction39", type=gama_EVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
aspectLinks41: BinaryAssociation = BinaryAssociation(
    name="aspectLinks41",
    ends={
        Property(name="gama_EAspectLink42", type=gama_EAspect, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EAspect", type=gama_EAspectLink, multiplicity=Multiplicity(0, 9999))
    }
)
layers43: BinaryAssociation = BinaryAssociation(
    name="layers43",
    ends={
        Property(name="gama_ELayerAspect", type=gama_EAspect, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EAspect44", type=gama_ELayerAspect, multiplicity=Multiplicity(0, 9999))
    }
)
reflexLinks45: BinaryAssociation = BinaryAssociation(
    name="reflexLinks45",
    ends={
        Property(name="gama_EReflexLink46", type=gama_EReflex, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EReflex", type=gama_EReflexLink, multiplicity=Multiplicity(0, 9999))
    }
)
inheritingLinks22: BinaryAssociation = BinaryAssociation(
    name="inheritingLinks22",
    ends={
        Property(name="gama_EInheritLink", type=gama_ESpecies, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_ESpecies23", type=gama_EInheritLink, multiplicity=Multiplicity(0, 9999))
    }
)
displayLinks49: BinaryAssociation = BinaryAssociation(
    name="displayLinks49",
    ends={
        Property(name="gama_EDisplayLink", type=gama_EExperiment, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EExperiment50", type=gama_EDisplayLink, multiplicity=Multiplicity(0, 9999))
    }
)
parameters51: BinaryAssociation = BinaryAssociation(
    name="parameters51",
    ends={
        Property(name="gama_EParameter", type=gama_EExperiment, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EExperiment52", type=gama_EParameter, multiplicity=Multiplicity(0, 9999))
    }
)
monitors53: BinaryAssociation = BinaryAssociation(
    name="monitors53",
    ends={
        Property(name="gama_EMonitor", type=gama_EExperiment, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EExperiment54", type=gama_EMonitor, multiplicity=Multiplicity(0, 9999))
    }
)
target55: BinaryAssociation = BinaryAssociation(
    name="target55",
    ends={
        Property(name="gama_EGamaObject56", type=gama_EGamaLink, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EGamaLink", type=gama_EGamaObject, multiplicity=Multiplicity(1, 1))
    }
)
source57: BinaryAssociation = BinaryAssociation(
    name="source57",
    ends={
        Property(name="gama_EGamaObject59", type=gama_EGamaLink, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EGamaLink58", type=gama_EGamaObject, multiplicity=Multiplicity(1, 1))
    }
)
model60: BinaryAssociation = BinaryAssociation(
    name="model60",
    ends={
        Property(name="EGamaModel61", type=gama_EGamaLink, multiplicity=Multiplicity(1, 1)),
        Property(name="links", type=gama_EGamaModel, multiplicity=Multiplicity(1, 1))
    }
)
macro62: BinaryAssociation = BinaryAssociation(
    name="macro62",
    ends={
        Property(name="gama_ESpecies64", type=gama_ESubSpeciesLink, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_ESubSpeciesLink63", type=gama_ESpecies, multiplicity=Multiplicity(0, 1))
    }
)
micro65: BinaryAssociation = BinaryAssociation(
    name="micro65",
    ends={
        Property(name="gama_ESpecies67", type=gama_ESubSpeciesLink, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_ESubSpeciesLink66", type=gama_ESpecies, multiplicity=Multiplicity(0, 1))
    }
)
action68: BinaryAssociation = BinaryAssociation(
    name="action68",
    ends={
        Property(name="gama_EAction70", type=gama_EActionLink, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EActionLink69", type=gama_EAction, multiplicity=Multiplicity(0, 1))
    }
)
species71: BinaryAssociation = BinaryAssociation(
    name="species71",
    ends={
        Property(name="gama_ESpecies73", type=gama_EActionLink, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EActionLink72", type=gama_ESpecies, multiplicity=Multiplicity(0, 1))
    }
)
experimentLink47: BinaryAssociation = BinaryAssociation(
    name="experimentLink47",
    ends={
        Property(name="gama_EExperimentLink48", type=gama_EExperiment, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EExperiment", type=gama_EExperimentLink, multiplicity=Multiplicity(0, 1))
    }
)
species83: BinaryAssociation = BinaryAssociation(
    name="species83",
    ends={
        Property(name="gama_ESpecies85", type=gama_EReflexLink, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EReflexLink84", type=gama_ESpecies, multiplicity=Multiplicity(0, 1))
    }
)
experiment86: BinaryAssociation = BinaryAssociation(
    name="experiment86",
    ends={
        Property(name="gama_EGUIExperiment", type=gama_EDisplayLink, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EDisplayLink87", type=gama_EGUIExperiment, multiplicity=Multiplicity(0, 1))
    }
)
display88: BinaryAssociation = BinaryAssociation(
    name="display88",
    ends={
        Property(name="gama_EDisplay", type=gama_EDisplayLink, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EDisplayLink89", type=gama_EDisplay, multiplicity=Multiplicity(0, 1))
    }
)
layers90: BinaryAssociation = BinaryAssociation(
    name="layers90",
    ends={
        Property(name="gama_ELayer", type=gama_EDisplay, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EDisplay91", type=gama_ELayer, multiplicity=Multiplicity(0, 9999))
    }
)
displayLink92: BinaryAssociation = BinaryAssociation(
    name="displayLink92",
    ends={
        Property(name="gama_EDisplayLink94", type=gama_EDisplay, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EDisplay93", type=gama_EDisplayLink, multiplicity=Multiplicity(0, 1))
    }
)
owner95: BinaryAssociation = BinaryAssociation(
    name="owner95",
    ends={
        Property(name="gama_EGamaObject97", type=gama_EVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EVariable96", type=gama_EGamaObject, multiplicity=Multiplicity(0, 1))
    }
)
display98: BinaryAssociation = BinaryAssociation(
    name="display98",
    ends={
        Property(name="gama_EDisplay100", type=gama_ELayer, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_ELayer99", type=gama_EDisplay, multiplicity=Multiplicity(0, 1))
    }
)
aspect74: BinaryAssociation = BinaryAssociation(
    name="aspect74",
    ends={
        Property(name="gama_EAspect76", type=gama_EAspectLink, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EAspectLink75", type=gama_EAspect, multiplicity=Multiplicity(0, 1))
    }
)
species77: BinaryAssociation = BinaryAssociation(
    name="species77",
    ends={
        Property(name="gama_ESpecies79", type=gama_EAspectLink, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EAspectLink78", type=gama_ESpecies, multiplicity=Multiplicity(0, 1))
    }
)
reflex80: BinaryAssociation = BinaryAssociation(
    name="reflex80",
    ends={
        Property(name="gama_EReflex82", type=gama_EReflexLink, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EReflexLink81", type=gama_EReflex, multiplicity=Multiplicity(0, 1))
    }
)
chartlayers101: BinaryAssociation = BinaryAssociation(
    name="chartlayers101",
    ends={
        Property(name="gama_EChartLayer", type=gama_ELayer, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_ELayer102", type=gama_EChartLayer, multiplicity=Multiplicity(0, 9999))
    }
)
species103: BinaryAssociation = BinaryAssociation(
    name="species103",
    ends={
        Property(name="gama_ESpecies105", type=gama_EExperimentLink, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EExperimentLink104", type=gama_ESpecies, multiplicity=Multiplicity(0, 1))
    }
)
experiment106: BinaryAssociation = BinaryAssociation(
    name="experiment106",
    ends={
        Property(name="gama_EExperiment108", type=gama_EExperimentLink, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EExperimentLink107", type=gama_EExperiment, multiplicity=Multiplicity(0, 1))
    }
)
aspect109: BinaryAssociation = BinaryAssociation(
    name="aspect109",
    ends={
        Property(name="gama_EAspect111", type=gama_ELayerAspect, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_ELayerAspect110", type=gama_EAspect, multiplicity=Multiplicity(0, 1))
    }
)
child115: BinaryAssociation = BinaryAssociation(
    name="child115",
    ends={
        Property(name="gama_ESpecies117", type=gama_EInheritLink, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EInheritLink116", type=gama_ESpecies, multiplicity=Multiplicity(0, 1))
    }
)
owner118: BinaryAssociation = BinaryAssociation(
    name="owner118",
    ends={
        Property(name="gama_EGamaObject120", type=gama_EFacet, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EFacet119", type=gama_EGamaObject, multiplicity=Multiplicity(0, 1))
    }
)
planLinks121: BinaryAssociation = BinaryAssociation(
    name="planLinks121",
    ends={
        Property(name="gama_EPlanLink122", type=gama_EPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EPlan", type=gama_EPlanLink, multiplicity=Multiplicity(0, 9999))
    }
)
stateLinks123: BinaryAssociation = BinaryAssociation(
    name="stateLinks123",
    ends={
        Property(name="gama_EStateLink124", type=gama_EState, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EState", type=gama_EStateLink, multiplicity=Multiplicity(0, 9999))
    }
)
taskLinks125: BinaryAssociation = BinaryAssociation(
    name="taskLinks125",
    ends={
        Property(name="gama_ETaskLink126", type=gama_ETask, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_ETask", type=gama_ETaskLink, multiplicity=Multiplicity(0, 9999))
    }
)
parent112: BinaryAssociation = BinaryAssociation(
    name="parent112",
    ends={
        Property(name="gama_ESpecies114", type=gama_EInheritLink, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EInheritLink113", type=gama_ESpecies, multiplicity=Multiplicity(0, 1))
    }
)
equationLinks161: BinaryAssociation = BinaryAssociation(
    name="equationLinks161",
    ends={
        Property(name="gama_EEquation", type=gama_EEquationLink, multiplicity=Multiplicity(0, 9999)),
        Property(name="gama_EEquationLink162", type=gama_EEquation, multiplicity=Multiplicity(1, 1))
    }
)
state133: BinaryAssociation = BinaryAssociation(
    name="state133",
    ends={
        Property(name="gama_EState135", type=gama_EStateLink, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EStateLink134", type=gama_EState, multiplicity=Multiplicity(0, 1))
    }
)
equation163: BinaryAssociation = BinaryAssociation(
    name="equation163",
    ends={
        Property(name="gama_EEquation165", type=gama_EEquationLink, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EEquationLink164", type=gama_EEquation, multiplicity=Multiplicity(0, 1))
    }
)
species136: BinaryAssociation = BinaryAssociation(
    name="species136",
    ends={
        Property(name="gama_ESpecies138", type=gama_EStateLink, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EStateLink137", type=gama_ESpecies, multiplicity=Multiplicity(0, 1))
    }
)
task139: BinaryAssociation = BinaryAssociation(
    name="task139",
    ends={
        Property(name="gama_ETask141", type=gama_ETaskLink, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_ETaskLink140", type=gama_ETask, multiplicity=Multiplicity(0, 1))
    }
)
species142: BinaryAssociation = BinaryAssociation(
    name="species142",
    ends={
        Property(name="gama_ESpecies144", type=gama_ETaskLink, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_ETaskLink143", type=gama_ESpecies, multiplicity=Multiplicity(0, 1))
    }
)
perceiveLinks145: BinaryAssociation = BinaryAssociation(
    name="perceiveLinks145",
    ends={
        Property(name="gama_EPerceiveLink146", type=gama_EPerceive, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EPerceive", type=gama_EPerceiveLink, multiplicity=Multiplicity(0, 9999))
    }
)
perceive147: BinaryAssociation = BinaryAssociation(
    name="perceive147",
    ends={
        Property(name="gama_EPerceive149", type=gama_EPerceiveLink, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EPerceiveLink148", type=gama_EPerceive, multiplicity=Multiplicity(0, 1))
    }
)
species150: BinaryAssociation = BinaryAssociation(
    name="species150",
    ends={
        Property(name="gama_ESpecies152", type=gama_EPerceiveLink, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EPerceiveLink151", type=gama_ESpecies, multiplicity=Multiplicity(0, 1))
    }
)
ruleLinks153: BinaryAssociation = BinaryAssociation(
    name="ruleLinks153",
    ends={
        Property(name="gama_ERuleLink154", type=gama_ERule, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_ERule", type=gama_ERuleLink, multiplicity=Multiplicity(0, 9999))
    }
)
rule155: BinaryAssociation = BinaryAssociation(
    name="rule155",
    ends={
        Property(name="gama_ERule157", type=gama_ERuleLink, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_ERuleLink156", type=gama_ERule, multiplicity=Multiplicity(0, 1))
    }
)
species158: BinaryAssociation = BinaryAssociation(
    name="species158",
    ends={
        Property(name="gama_ESpecies160", type=gama_ERuleLink, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_ERuleLink159", type=gama_ESpecies, multiplicity=Multiplicity(0, 1))
    }
)
plan127: BinaryAssociation = BinaryAssociation(
    name="plan127",
    ends={
        Property(name="gama_EPlan129", type=gama_EPlanLink, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EPlanLink128", type=gama_EPlan, multiplicity=Multiplicity(0, 1))
    }
)
species130: BinaryAssociation = BinaryAssociation(
    name="species130",
    ends={
        Property(name="gama_ESpecies132", type=gama_EPlanLink, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EPlanLink131", type=gama_ESpecies, multiplicity=Multiplicity(0, 1))
    }
)
species166: BinaryAssociation = BinaryAssociation(
    name="species166",
    ends={
        Property(name="gama_ESpecies168", type=gama_EEquationLink, multiplicity=Multiplicity(1, 1)),
        Property(name="gama_EEquationLink167", type=gama_ESpecies, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_gama_ESpecies_EGamaObject = Generalization(general=EGamaObject, specific=gama_ESpecies)
gen_gama_EAction_EGamaObject = Generalization(general=EGamaObject, specific=gama_EAction)
gen_gama_EAspect_EGamaObject = Generalization(general=EGamaObject, specific=gama_EAspect)
gen_gama_EReflex_EGamaObject = Generalization(general=EGamaObject, specific=gama_EReflex)
gen_gama_EExperiment_ESpecies = Generalization(general=ESpecies, specific=gama_EExperiment)
gen_gama_EGUIExperiment_EExperiment = Generalization(general=EExperiment, specific=gama_EGUIExperiment)
gen_gama_EBatchExperiment_EExperiment = Generalization(general=EExperiment, specific=gama_EBatchExperiment)
gen_gama_ESubSpeciesLink_EGamaLink = Generalization(general=EGamaLink, specific=gama_ESubSpeciesLink)
gen_gama_EActionLink_EGamaLink = Generalization(general=EGamaLink, specific=gama_EActionLink)
gen_gama_EAspectLink_EGamaLink = Generalization(general=EGamaLink, specific=gama_EAspectLink)
gen_gama_EDisplayLink_EGamaLink = Generalization(general=EGamaLink, specific=gama_EDisplayLink)
gen_gama_EDisplay_EGamaObject = Generalization(general=EGamaObject, specific=gama_EDisplay)
gen_gama_EWorldAgent_ESpecies = Generalization(general=ESpecies, specific=gama_EWorldAgent)
gen_gama_ELayer_EGamaObject = Generalization(general=EGamaObject, specific=gama_ELayer)
gen_gama_EReflexLink_EGamaLink = Generalization(general=EGamaLink, specific=gama_EReflexLink)
gen_gama_EExperimentLink_EGamaLink = Generalization(general=EGamaLink, specific=gama_EExperimentLink)
gen_gama_ELayerAspect_EGamaObject = Generalization(general=EGamaObject, specific=gama_ELayerAspect)
gen_gama_EChartLayer_EGamaObject = Generalization(general=EGamaObject, specific=gama_EChartLayer)
gen_gama_EParameter_EGamaObject = Generalization(general=EGamaObject, specific=gama_EParameter)
gen_gama_EMonitor_EGamaObject = Generalization(general=EGamaObject, specific=gama_EMonitor)
gen_gama_EPlan_EGamaObject = Generalization(general=EGamaObject, specific=gama_EPlan)
gen_gama_EState_EGamaObject = Generalization(general=EGamaObject, specific=gama_EState)
gen_gama_ETask_EGamaObject = Generalization(general=EGamaObject, specific=gama_ETask)
gen_gama_EInheritLink_EGamaLink = Generalization(general=EGamaLink, specific=gama_EInheritLink)
gen_gama_EStateLink_EGamaLink = Generalization(general=EGamaLink, specific=gama_EStateLink)
gen_gama_EEquationLink_EGamaLink = Generalization(general=EGamaLink, specific=gama_EEquationLink)
gen_gama_ETaskLink_EGamaLink = Generalization(general=EGamaLink, specific=gama_ETaskLink)
gen_gama_EGrid_ESpecies = Generalization(general=ESpecies, specific=gama_EGrid)
gen_gama_EPerceive_EGamaObject = Generalization(general=EGamaObject, specific=gama_EPerceive)
gen_gama_EPerceiveLink_EGamaLink = Generalization(general=EGamaLink, specific=gama_EPerceiveLink)
gen_gama_ERule_EGamaObject = Generalization(general=EGamaObject, specific=gama_ERule)
gen_gama_ERuleLink_EGamaLink = Generalization(general=EGamaLink, specific=gama_ERuleLink)
gen_gama_EPlanLink_EGamaLink = Generalization(general=EGamaLink, specific=gama_EPlanLink)
gen_gama_EEquation_EGamaObject = Generalization(general=EGamaObject, specific=gama_EEquation)

# Domain Model
domain_model = DomainModel(
    name="gama",
    types={gama_EGamaModel, gama_EGamaObject, gama_EGamaLink, gama_EFacet, gama_ESpecies, EGamaObject, gama_EVariable, gama_EExperimentLink, gama_EAspectLink, gama_EActionLink, gama_EReflexLink, gama_ESubSpeciesLink, gama_EPlanLink, gama_EStateLink, gama_ETaskLink, gama_EPerceiveLink, gama_ERuleLink, gama_EEquationLink, gama_EAction, gama_EAspect, gama_ELayerAspect, gama_EReflex, gama_EExperiment, ESpecies, gama_EInheritLink, gama_EDisplayLink, gama_EParameter, gama_EMonitor, gama_EGUIExperiment, EExperiment, gama_EBatchExperiment, EGamaLink, gama_EDisplay, gama_ELayer, gama_EWorldAgent, gama_EChartLayer, gama_EPlan, gama_EState, gama_ETask, gama_EGrid, gama_EPerceive, gama_ERule, gama_EEquation},
    associations={links1, model3, facets4, variables5, experimentLinks6, aspectLinks8, actionLinks10, reflexLinks12, microSpeciesLinks14, macroSpeciesLinks16, inheritsFrom20, objects0, planLinks24, stateLinks26, taskLinks28, perceiveLinks30, ruleLinks32, equationLinks34, actionLinks36, variables38, aspectLinks41, layers43, reflexLinks45, inheritingLinks22, displayLinks49, parameters51, monitors53, target55, source57, model60, macro62, micro65, action68, species71, experimentLink47, species83, experiment86, display88, layers90, displayLink92, owner95, display98, aspect74, species77, reflex80, chartlayers101, species103, experiment106, aspect109, child115, owner118, planLinks121, stateLinks123, taskLinks125, parent112, equationLinks161, state133, equation163, species136, task139, species142, perceiveLinks145, perceive147, species150, ruleLinks153, rule155, species158, plan127, species130, species166},
    generalizations={gen_gama_ESpecies_EGamaObject, gen_gama_EAction_EGamaObject, gen_gama_EAspect_EGamaObject, gen_gama_EReflex_EGamaObject, gen_gama_EExperiment_ESpecies, gen_gama_EGUIExperiment_EExperiment, gen_gama_EBatchExperiment_EExperiment, gen_gama_ESubSpeciesLink_EGamaLink, gen_gama_EActionLink_EGamaLink, gen_gama_EAspectLink_EGamaLink, gen_gama_EDisplayLink_EGamaLink, gen_gama_EDisplay_EGamaObject, gen_gama_EWorldAgent_ESpecies, gen_gama_ELayer_EGamaObject, gen_gama_EReflexLink_EGamaLink, gen_gama_EExperimentLink_EGamaLink, gen_gama_ELayerAspect_EGamaObject, gen_gama_EChartLayer_EGamaObject, gen_gama_EParameter_EGamaObject, gen_gama_EMonitor_EGamaObject, gen_gama_EPlan_EGamaObject, gen_gama_EState_EGamaObject, gen_gama_ETask_EGamaObject, gen_gama_EInheritLink_EGamaLink, gen_gama_EStateLink_EGamaLink, gen_gama_EEquationLink_EGamaLink, gen_gama_ETaskLink_EGamaLink, gen_gama_EGrid_ESpecies, gen_gama_EPerceive_EGamaObject, gen_gama_EPerceiveLink_EGamaLink, gen_gama_ERule_EGamaObject, gen_gama_ERuleLink_EGamaLink, gen_gama_EPlanLink_EGamaLink, gen_gama_EEquation_EGamaObject},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)