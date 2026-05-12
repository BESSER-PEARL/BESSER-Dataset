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
Make_Element = Class(name="Make_Element", is_abstract=True)
Make_Rule = Class(name="Make_Rule")
Dependency = Class(name="Dependency")
ShellLine = Class(name="ShellLine")
Make_Macro = Class(name="Make_Macro")
Make_ShellLine = Class(name="Make_ShellLine")
Rule = Class(name="Rule")
Make_Comment = Class(name="Make_Comment")
Make_Dependency = Class(name="Make_Dependency", is_abstract=True)
Make_RuleDep = Class(name="Make_RuleDep")
Make_Makefile = Class(name="Make_Makefile")
Comment = Class(name="Comment")
Element = Class(name="Element")
Make_FileDep = Class(name="Make_FileDep")

# Make_Element class attributes and methods
Make_Element_name: Property = Property(name="name", type=StringType)
Make_Element.attributes={Make_Element_name}

# Make_Rule class attributes and methods

# Dependency class attributes and methods

# ShellLine class attributes and methods

# Make_Macro class attributes and methods
Make_Macro_value: Property = Property(name="value", type=StringType)
Make_Macro.attributes={Make_Macro_value}

# Make_ShellLine class attributes and methods
Make_ShellLine_command: Property = Property(name="command", type=StringType)
Make_ShellLine_display: Property = Property(name="display", type=StringType)
Make_ShellLine.attributes={Make_ShellLine_command, Make_ShellLine_display}

# Rule class attributes and methods

# Make_Comment class attributes and methods
Make_Comment_text: Property = Property(name="text", type=StringType)
Make_Comment.attributes={Make_Comment_text}

# Make_Dependency class attributes and methods

# Make_RuleDep class attributes and methods

# Make_Makefile class attributes and methods
Make_Makefile_name: Property = Property(name="name", type=StringType)
Make_Makefile.attributes={Make_Makefile_name}

# Comment class attributes and methods

# Element class attributes and methods

# Make_FileDep class attributes and methods
Make_FileDep_name: Property = Property(name="name", type=StringType)
Make_FileDep.attributes={Make_FileDep_name}

# Relationships
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="Element", type=Make_Makefile, multiplicity=Multiplicity(1, 1)),
        Property(name="Make_Makefile2", type=Element, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
dependencies3: BinaryAssociation = BinaryAssociation(
    name="dependencies3",
    ends={
        Property(name="Dependency", type=Make_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="Make_Rule", type=Dependency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
shellLines4: BinaryAssociation = BinaryAssociation(
    name="shellLines4",
    ends={
        Property(name="ShellLine", type=Make_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="ruleShellLine", type=ShellLine, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ruleShellLine5: BinaryAssociation = BinaryAssociation(
    name="ruleShellLine5",
    ends={
        Property(name="Rule", type=Make_ShellLine, multiplicity=Multiplicity(1, 1)),
        Property(name="shellLines", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
ruledep6: BinaryAssociation = BinaryAssociation(
    name="ruledep6",
    ends={
        Property(name="Rule7", type=Make_RuleDep, multiplicity=Multiplicity(1, 1)),
        Property(name="Make_RuleDep", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
comment0: BinaryAssociation = BinaryAssociation(
    name="comment0",
    ends={
        Property(name="Comment", type=Make_Makefile, multiplicity=Multiplicity(1, 1)),
        Property(name="Make_Makefile", type=Comment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_Make_Rule_Element = Generalization(general=Element, specific=Make_Rule)
gen_Make_Macro_Element = Generalization(general=Element, specific=Make_Macro)
gen_Make_RuleDep_Dependency = Generalization(general=Dependency, specific=Make_RuleDep)
gen_Make_FileDep_Dependency = Generalization(general=Dependency, specific=Make_FileDep)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={Make_Element, Make_Rule, Dependency, ShellLine, Make_Macro, Make_ShellLine, Rule, Make_Comment, Make_Dependency, Make_RuleDep, Make_Makefile, Comment, Element, Make_FileDep},
    associations={elements1, dependencies3, shellLines4, ruleShellLine5, ruledep6, comment0},
    generalizations={gen_Make_Rule_Element, gen_Make_Macro_Element, gen_Make_RuleDep_Dependency, gen_Make_FileDep_Dependency},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)