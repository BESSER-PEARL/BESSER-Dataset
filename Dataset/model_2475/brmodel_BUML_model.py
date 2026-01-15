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
brmodel_Model = Class(name="brmodel::Model")
brmodel_Rule = Class(name="brmodel::Rule")
brmodel_Statement = Class(name="brmodel::Statement")
brmodel_ReachableMethod = Class(name="brmodel::ReachableMethod")
brmodel_ReachableVariable = Class(name="brmodel::ReachableVariable")
Method_ = Class(name="Method")
Trace = Class(name="Trace")
brmodel_SlicedVariable = Class(name="brmodel::SlicedVariable")
brmodel_RulePart = Class(name="brmodel::RulePart")
brmodel_RelatedMethod = Class(name="brmodel::RelatedMethod")
Variable = Class(name="Variable")
brmodel_RelatedVariable = Class(name="brmodel::RelatedVariable")
brmodel_Variable = Class(name="brmodel::Variable", is_abstract=True)
brmodel_Trace = Class(name="brmodel::Trace")
brmodel_EObject = Class(name="brmodel::EObject")
brmodel_Method = Class(name="brmodel::Method", is_abstract=True)

# brmodel_Model class attributes and methods

# brmodel_Rule class attributes and methods
brmodel_Rule_id: Property = Property(name="id", type=StringType)
brmodel_Rule.attributes={brmodel_Rule_id}

# brmodel_Statement class attributes and methods
brmodel_Statement_textContent: Property = Property(name="textContent", type=StringType)
brmodel_Statement.attributes={brmodel_Statement_textContent}

# brmodel_ReachableMethod class attributes and methods
brmodel_ReachableMethod_distance: Property = Property(name="distance", type=StringType)
brmodel_ReachableMethod.attributes={brmodel_ReachableMethod_distance}

# brmodel_ReachableVariable class attributes and methods

# Method class attributes and methods

# Trace class attributes and methods

# brmodel_SlicedVariable class attributes and methods

# brmodel_RulePart class attributes and methods
brmodel_RulePart_granularity: Property = Property(name="granularity", type=StringType)
brmodel_RulePart.attributes={brmodel_RulePart_granularity}

# brmodel_RelatedMethod class attributes and methods

# Variable class attributes and methods

# brmodel_RelatedVariable class attributes and methods

# brmodel_Variable class attributes and methods
brmodel_Variable_name: Property = Property(name="name", type=StringType)
brmodel_Variable.attributes={brmodel_Variable_name}

# brmodel_Trace class attributes and methods

# brmodel_EObject class attributes and methods

# brmodel_Method class attributes and methods
brmodel_Method_class: Property = Property(name="class", type=StringType)
brmodel_Method_name: Property = Property(name="name", type=StringType)
brmodel_Method.attributes={brmodel_Method_name, brmodel_Method_class}

# Relationships
rules0: BinaryAssociation = BinaryAssociation(
    name="rules0",
    ends={
        Property(name="brmodel_Rule", type=brmodel_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="brmodel_Model", type=brmodel_Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relatedStatements7: BinaryAssociation = BinaryAssociation(
    name="relatedStatements7",
    ends={
        Property(name="brmodel_Statement", type=brmodel_RulePart, multiplicity=Multiplicity(1, 1)),
        Property(name="brmodel_RulePart8", type=brmodel_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action9: BinaryAssociation = BinaryAssociation(
    name="action9",
    ends={
        Property(name="brmodel_Statement11", type=brmodel_RulePart, multiplicity=Multiplicity(1, 1)),
        Property(name="brmodel_RulePart10", type=brmodel_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reachableMethods12: BinaryAssociation = BinaryAssociation(
    name="reachableMethods12",
    ends={
        Property(name="brmodel_ReachableMethod", type=brmodel_RulePart, multiplicity=Multiplicity(1, 1)),
        Property(name="brmodel_RulePart13", type=brmodel_ReachableMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relatedVariables14: BinaryAssociation = BinaryAssociation(
    name="relatedVariables14",
    ends={
        Property(name="brmodel_ReachableVariable", type=brmodel_RulePart, multiplicity=Multiplicity(1, 1)),
        Property(name="brmodel_RulePart15", type=brmodel_ReachableVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
slicedVariable1: BinaryAssociation = BinaryAssociation(
    name="slicedVariable1",
    ends={
        Property(name="brmodel_SlicedVariable", type=brmodel_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="brmodel_Rule2", type=brmodel_SlicedVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ruleParts3: BinaryAssociation = BinaryAssociation(
    name="ruleParts3",
    ends={
        Property(name="brmodel_RulePart", type=brmodel_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="brmodel_Rule4", type=brmodel_RulePart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relatedMethod5: BinaryAssociation = BinaryAssociation(
    name="relatedMethod5",
    ends={
        Property(name="brmodel_RelatedMethod", type=brmodel_RulePart, multiplicity=Multiplicity(1, 1)),
        Property(name="brmodel_RulePart6", type=brmodel_RelatedMethod, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
linkToCode16: BinaryAssociation = BinaryAssociation(
    name="linkToCode16",
    ends={
        Property(name="brmodel_EObject", type=brmodel_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="brmodel_Trace", type=brmodel_EObject, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_brmodel_RelatedMethod_Method = Generalization(general=Method_, specific=brmodel_RelatedMethod)
gen_brmodel_Statement_Trace = Generalization(general=Trace, specific=brmodel_Statement)
gen_brmodel_Method_Trace = Generalization(general=Trace, specific=brmodel_Method)
gen_brmodel_ReachableMethod_Method = Generalization(general=Method_, specific=brmodel_ReachableMethod)
gen_brmodel_SlicedVariable_Variable = Generalization(general=Variable, specific=brmodel_SlicedVariable)
gen_brmodel_RelatedVariable_Variable = Generalization(general=Variable, specific=brmodel_RelatedVariable)
gen_brmodel_ReachableVariable_Variable = Generalization(general=Variable, specific=brmodel_ReachableVariable)
gen_brmodel_Variable_Trace = Generalization(general=Trace, specific=brmodel_Variable)

# Domain Model
domain_model = DomainModel(
    name="brmodel",
    types={brmodel_Model, brmodel_Rule, brmodel_Statement, brmodel_ReachableMethod, brmodel_ReachableVariable, Method_, Trace, brmodel_SlicedVariable, brmodel_RulePart, brmodel_RelatedMethod, Variable, brmodel_RelatedVariable, brmodel_Variable, brmodel_Trace, brmodel_EObject, brmodel_Method},
    associations={rules0, relatedStatements7, action9, reachableMethods12, relatedVariables14, slicedVariable1, ruleParts3, relatedMethod5, linkToCode16},
    generalizations={gen_brmodel_RelatedMethod_Method, gen_brmodel_Statement_Trace, gen_brmodel_Method_Trace, gen_brmodel_ReachableMethod_Method, gen_brmodel_SlicedVariable_Variable, gen_brmodel_RelatedVariable_Variable, gen_brmodel_ReachableVariable_Variable, gen_brmodel_Variable_Trace},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)