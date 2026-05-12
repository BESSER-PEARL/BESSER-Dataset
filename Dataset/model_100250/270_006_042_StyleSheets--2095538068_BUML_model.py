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
stylesheets_StyleSheetReference = Class(name="stylesheets_StyleSheetReference")
StyleSheet = Class(name="StyleSheet")
stylesheets_EmbeddedStyleSheet = Class(name="stylesheets_EmbeddedStyleSheet")
stylesheets_ModelStyleSheets = Class(name="stylesheets_ModelStyleSheets")
EModelElement = Class(name="EModelElement")
stylesheets_StyleSheet = Class(name="stylesheets_StyleSheet", is_abstract=True)
stylesheets_WorkspaceThemes = Class(name="stylesheets_WorkspaceThemes")
stylesheets_Theme = Class(name="stylesheets_Theme")

# stylesheets_StyleSheetReference class attributes and methods
stylesheets_StyleSheetReference_path: Property = Property(name="path", type=StringType)
stylesheets_StyleSheetReference.attributes={stylesheets_StyleSheetReference_path}

# StyleSheet class attributes and methods

# stylesheets_EmbeddedStyleSheet class attributes and methods
stylesheets_EmbeddedStyleSheet_label: Property = Property(name="label", type=StringType)
stylesheets_EmbeddedStyleSheet_content: Property = Property(name="content", type=StringType)
stylesheets_EmbeddedStyleSheet.attributes={stylesheets_EmbeddedStyleSheet_content, stylesheets_EmbeddedStyleSheet_label}

# stylesheets_ModelStyleSheets class attributes and methods

# EModelElement class attributes and methods

# stylesheets_StyleSheet class attributes and methods

# stylesheets_WorkspaceThemes class attributes and methods

# stylesheets_Theme class attributes and methods
stylesheets_Theme_id: Property = Property(name="id", type=StringType)
stylesheets_Theme_label: Property = Property(name="label", type=StringType)
stylesheets_Theme_icon: Property = Property(name="icon", type=StringType)
stylesheets_Theme.attributes={stylesheets_Theme_icon, stylesheets_Theme_label, stylesheets_Theme_id}

# Relationships
stylesheets0: BinaryAssociation = BinaryAssociation(
    name="stylesheets0",
    ends={
        Property(name="stylesheets_StyleSheet", type=stylesheets_ModelStyleSheets, multiplicity=Multiplicity(1, 1)),
        Property(name="stylesheets_ModelStyleSheets", type=stylesheets_StyleSheet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stylesheets2: BinaryAssociation = BinaryAssociation(
    name="stylesheets2",
    ends={
        Property(name="stylesheets_StyleSheet4", type=stylesheets_Theme, multiplicity=Multiplicity(1, 1)),
        Property(name="stylesheets_Theme3", type=stylesheets_StyleSheet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
themes1: BinaryAssociation = BinaryAssociation(
    name="themes1",
    ends={
        Property(name="stylesheets_Theme", type=stylesheets_WorkspaceThemes, multiplicity=Multiplicity(1, 1)),
        Property(name="stylesheets_WorkspaceThemes", type=stylesheets_Theme, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_stylesheets_StyleSheetReference_StyleSheet = Generalization(general=StyleSheet, specific=stylesheets_StyleSheetReference)
gen_stylesheets_EmbeddedStyleSheet_StyleSheet = Generalization(general=StyleSheet, specific=stylesheets_EmbeddedStyleSheet)
gen_stylesheets_ModelStyleSheets_EModelElement = Generalization(general=EModelElement, specific=stylesheets_ModelStyleSheets)
gen_stylesheets_WorkspaceThemes_EModelElement = Generalization(general=EModelElement, specific=stylesheets_WorkspaceThemes)

# Domain Model
domain_model = DomainModel(
    name="stylesheets",
    types={stylesheets_StyleSheetReference, StyleSheet, stylesheets_EmbeddedStyleSheet, stylesheets_ModelStyleSheets, EModelElement, stylesheets_StyleSheet, stylesheets_WorkspaceThemes, stylesheets_Theme},
    associations={stylesheets0, stylesheets2, themes1},
    generalizations={gen_stylesheets_StyleSheetReference_StyleSheet, gen_stylesheets_EmbeddedStyleSheet_StyleSheet, gen_stylesheets_ModelStyleSheets_EModelElement, gen_stylesheets_WorkspaceThemes_EModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)