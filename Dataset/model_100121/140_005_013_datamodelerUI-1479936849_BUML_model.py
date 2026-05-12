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
ui_project_Project = Class(name="ui_project_Project")
schema_FunctionalElement = Class(name="schema_FunctionalElement")
schema_DataModelerNamedElement = Class(name="schema_DataModelerNamedElement")
ui_diagram_DMDiagram = Class(name="ui_diagram_DMDiagram")
Diagram = Class(name="Diagram")
Database = Class(name="Database")
Schema = Class(name="Schema")

# ui_project_Project class attributes and methods
ui_project_Project_application: Property = Property(name="application", type=StringType)
ui_project_Project_description: Property = Property(name="description", type=StringType)
ui_project_Project_m_isValid: Method = Method(name="isValid", parameters={Parameter(name='ui_diagnostics', type=StringType), Parameter(name='ui_context', type=StringType)}, type=BooleanType)
ui_project_Project.attributes={ui_project_Project_application, ui_project_Project_description}
ui_project_Project.methods={ui_project_Project_m_isValid}

# schema_FunctionalElement class attributes and methods

# schema_DataModelerNamedElement class attributes and methods

# ui_diagram_DMDiagram class attributes and methods

# Diagram class attributes and methods

# Database class attributes and methods

# Schema class attributes and methods

# Relationships
database0: BinaryAssociation = BinaryAssociation(
    name="database0",
    ends={
        Property(name="Database", type=ui_project_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="ui_project_Project", type=Database, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
schemas1: BinaryAssociation = BinaryAssociation(
    name="schemas1",
    ends={
        Property(name="Schema", type=ui_project_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="ui_project_Project2", type=Schema, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_ui_project_Project_schema_FunctionalElement = Generalization(general=schema_FunctionalElement, specific=ui_project_Project)
gen_ui_project_Project_schema_DataModelerNamedElement = Generalization(general=schema_DataModelerNamedElement, specific=ui_project_Project)
gen_ui_diagram_DMDiagram_Diagram = Generalization(general=Diagram, specific=ui_diagram_DMDiagram)

# Domain Model
domain_model = DomainModel(
    name="ui",
    types={ui_project_Project, schema_FunctionalElement, schema_DataModelerNamedElement, ui_diagram_DMDiagram, Diagram, Database, Schema},
    associations={database0, schemas1},
    generalizations={gen_ui_project_Project_schema_FunctionalElement, gen_ui_project_Project_schema_DataModelerNamedElement, gen_ui_diagram_DMDiagram_Diagram},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)