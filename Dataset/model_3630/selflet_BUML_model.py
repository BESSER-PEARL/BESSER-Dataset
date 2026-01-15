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
Mode: Enumeration = Enumeration(
    name="Mode",
    literals={
            EnumerationLiteral(name="CanDo"),
			EnumerationLiteral(name="CanTeach"),
			EnumerationLiteral(name="Both"),
			EnumerationLiteral(name="KnowsWhoCanBoth"),
			EnumerationLiteral(name="KnowsWhoCanDo"),
			EnumerationLiteral(name="KnowsWhoCanTeach"),
			EnumerationLiteral(name="None")
    }
)

Type: Enumeration = Enumeration(
    name="Type",
    literals={
            EnumerationLiteral(name="double"),
			EnumerationLiteral(name="integer"),
			EnumerationLiteral(name="string"),
			EnumerationLiteral(name="boolean"),
			EnumerationLiteral(name="ServiceAskMode"),
			EnumerationLiteral(name="ServiceOfferMode"),
			EnumerationLiteral(name="Double1"),
			EnumerationLiteral(name="Integer1"),
			EnumerationLiteral(name="String1"),
			EnumerationLiteral(name="Boolean1")
    }
)

# Classes
selflet_Active = Class(name="selflet::Active")
selflet_Behavior = Class(name="selflet::Behavior")
selflet_Abilities = Class(name="selflet::Abilities")
selflet_Ability = Class(name="selflet::Ability")
selflet_Methods = Class(name="selflet::Methods")
selflet_Actions = Class(name="selflet::Actions")
selflet_Action = Class(name="selflet::Action")
selflet_CPUUtilization = Class(name="selflet::CPUUtilization")
selflet_Empty = Class(name="selflet::Empty")
selflet_GeneralKnowledge = Class(name="selflet::GeneralKnowledge")
selflet_Service = Class(name="selflet::Service")
selflet_Conditions = Class(name="selflet::Conditions")
selflet_Condition = Class(name="selflet::Condition")
selflet_SelfLetProperty = Class(name="selflet::SelfLetProperty")
selflet_Input = Class(name="selflet::Input")
selflet_Parameter = Class(name="selflet::Parameter")
selflet_Method = Class(name="selflet::Method")
selflet_Reds = Class(name="selflet::Reds")
selflet_OfferMode = Class(name="selflet::OfferMode")
selflet_Output = Class(name="selflet::Output")
selflet_Rules = Class(name="selflet::Rules")
selflet_Rule = Class(name="selflet::Rule")
selflet_Selflet = Class(name="selflet::Selflet")
selflet_SelfletProperties = Class(name="selflet::SelfletProperties")
selflet_SelfletResources = Class(name="selflet::SelfletResources")
selflet_TypeKnowledge = Class(name="selflet::TypeKnowledge")
selflet_Services = Class(name="selflet::Services")
selflet_ElementaryBehavior = Class(name="selflet::ElementaryBehavior")
Behavior = Class(name="Behavior")
selflet_State = Class(name="selflet::State")
selflet_ComplexBehavior = Class(name="selflet::ComplexBehavior")
selflet_InitialState = Class(name="selflet::InitialState")
State = Class(name="State")
selflet_FinalState = Class(name="selflet::FinalState")
selflet_AbilityState = Class(name="selflet::AbilityState")
selflet_IntermediateState = Class(name="selflet::IntermediateState")

# selflet_Active class attributes and methods
selflet_Active_mainService: Property = Property(name="mainService", type=StringType)
selflet_Active.attributes={selflet_Active_mainService}

# selflet_Behavior class attributes and methods
selflet_Behavior_elementaryBehaviorCost: Property = Property(name="elementaryBehaviorCost", type=StringType)
selflet_Behavior_elementaryBehaviorCPUTime: Property = Property(name="elementaryBehaviorCPUTime", type=StringType)
selflet_Behavior_fileName: Property = Property(name="fileName", type=StringType)
selflet_Behavior_isDefaultBehavior: Property = Property(name="isDefaultBehavior", type=StringType)
selflet_Behavior_name: Property = Property(name="name", type=StringType)
selflet_Behavior.attributes={selflet_Behavior_elementaryBehaviorCost, selflet_Behavior_isDefaultBehavior, selflet_Behavior_fileName, selflet_Behavior_elementaryBehaviorCPUTime, selflet_Behavior_name}

# selflet_Abilities class attributes and methods

# selflet_Ability class attributes and methods
selflet_Ability_service: Property = Property(name="service", type=StringType)
selflet_Ability_file: Property = Property(name="file", type=StringType)
selflet_Ability.attributes={selflet_Ability_service, selflet_Ability_file}

# selflet_Methods class attributes and methods

# selflet_Actions class attributes and methods

# selflet_Action class attributes and methods
selflet_Action_file: Property = Property(name="file", type=StringType)
selflet_Action.attributes={selflet_Action_file}

# selflet_CPUUtilization class attributes and methods
selflet_CPUUtilization_lowerBound: Property = Property(name="lowerBound", type=StringType)
selflet_CPUUtilization_upperBound: Property = Property(name="upperBound", type=StringType)
selflet_CPUUtilization.attributes={selflet_CPUUtilization_lowerBound, selflet_CPUUtilization_upperBound}

# selflet_Empty class attributes and methods

# selflet_GeneralKnowledge class attributes and methods

# selflet_Service class attributes and methods
selflet_Service_active: Property = Property(name="active", type=StringType)
selflet_Service_revenue: Property = Property(name="revenue", type=StringType)
selflet_Service_maxResponseTime: Property = Property(name="maxResponseTime", type=StringType)
selflet_Service_name: Property = Property(name="name", type=StringType)
selflet_Service.attributes={selflet_Service_name, selflet_Service_active, selflet_Service_maxResponseTime, selflet_Service_revenue}

# selflet_Conditions class attributes and methods

# selflet_Condition class attributes and methods
selflet_Condition_file: Property = Property(name="file", type=StringType)
selflet_Condition.attributes={selflet_Condition_file}

# selflet_SelfLetProperty class attributes and methods
selflet_SelfLetProperty_name: Property = Property(name="name", type=StringType)
selflet_SelfLetProperty_type: Property = Property(name="type", type=StringType)
selflet_SelfLetProperty_value: Property = Property(name="value", type=StringType)
selflet_SelfLetProperty.attributes={selflet_SelfLetProperty_value, selflet_SelfLetProperty_type, selflet_SelfLetProperty_name}

# selflet_Input class attributes and methods

# selflet_Parameter class attributes and methods
selflet_Parameter_name: Property = Property(name="name", type=StringType)
selflet_Parameter_type: Property = Property(name="type", type=StringType)
selflet_Parameter.attributes={selflet_Parameter_name, selflet_Parameter_type}

# selflet_Method class attributes and methods
selflet_Method_name: Property = Property(name="name", type=StringType)
selflet_Method_paramType: Property = Property(name="paramType", type=StringType)
selflet_Method.attributes={selflet_Method_paramType, selflet_Method_name}

# selflet_Reds class attributes and methods
selflet_Reds_ipAddress: Property = Property(name="ipAddress", type=StringType)
selflet_Reds_port: Property = Property(name="port", type=StringType)
selflet_Reds.attributes={selflet_Reds_ipAddress, selflet_Reds_port}

# selflet_OfferMode class attributes and methods
selflet_OfferMode_mode: Property = Property(name="mode", type=StringType)
selflet_OfferMode.attributes={selflet_OfferMode_mode}

# selflet_Output class attributes and methods

# selflet_Rules class attributes and methods

# selflet_Rule class attributes and methods
selflet_Rule_file: Property = Property(name="file", type=StringType)
selflet_Rule.attributes={selflet_Rule_file}

# selflet_Selflet class attributes and methods
selflet_Selflet_name: Property = Property(name="name", type=StringType)
selflet_Selflet.attributes={selflet_Selflet_name}

# selflet_SelfletProperties class attributes and methods
selflet_SelfletProperties_author: Property = Property(name="author", type=StringType)
selflet_SelfletProperties_description: Property = Property(name="description", type=StringType)
selflet_SelfletProperties_enableOptimizationPolicy: Property = Property(name="enableOptimizationPolicy", type=StringType)
selflet_SelfletProperties_enableCloudOptimizationPolicy: Property = Property(name="enableCloudOptimizationPolicy", type=StringType)
selflet_SelfletProperties_limePort: Property = Property(name="limePort", type=StringType)
selflet_SelfletProperties.attributes={selflet_SelfletProperties_limePort, selflet_SelfletProperties_description, selflet_SelfletProperties_enableOptimizationPolicy, selflet_SelfletProperties_author, selflet_SelfletProperties_enableCloudOptimizationPolicy}

# selflet_SelfletResources class attributes and methods

# selflet_TypeKnowledge class attributes and methods

# selflet_Services class attributes and methods

# selflet_ElementaryBehavior class attributes and methods

# Behavior class attributes and methods

# selflet_State class attributes and methods
selflet_State_name: Property = Property(name="name", type=StringType)
selflet_State.attributes={selflet_State_name}

# selflet_ComplexBehavior class attributes and methods

# selflet_InitialState class attributes and methods

# State class attributes and methods

# selflet_FinalState class attributes and methods

# selflet_AbilityState class attributes and methods

# selflet_IntermediateState class attributes and methods

# Relationships
ability0: BinaryAssociation = BinaryAssociation(
    name="ability0",
    ends={
        Property(name="selflet_Ability", type=selflet_Abilities, multiplicity=Multiplicity(1, 1)),
        Property(name="selflet_Abilities", type=selflet_Ability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods1: BinaryAssociation = BinaryAssociation(
    name="methods1",
    ends={
        Property(name="selflet_Methods", type=selflet_Ability, multiplicity=Multiplicity(1, 1)),
        Property(name="selflet_Ability2", type=selflet_Methods, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
action3: BinaryAssociation = BinaryAssociation(
    name="action3",
    ends={
        Property(name="selflet_Action", type=selflet_Actions, multiplicity=Multiplicity(1, 1)),
        Property(name="selflet_Actions", type=selflet_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implements4: BinaryAssociation = BinaryAssociation(
    name="implements4",
    ends={
        Property(name="selflet_Service", type=selflet_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="selflet_Behavior", type=selflet_Service, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition5: BinaryAssociation = BinaryAssociation(
    name="condition5",
    ends={
        Property(name="selflet_Condition", type=selflet_Conditions, multiplicity=Multiplicity(1, 1)),
        Property(name="selflet_Conditions", type=selflet_Condition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method8: BinaryAssociation = BinaryAssociation(
    name="method8",
    ends={
        Property(name="selflet_Method", type=selflet_Methods, multiplicity=Multiplicity(1, 1)),
        Property(name="selflet_Methods9", type=selflet_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
selfLetProperty6: BinaryAssociation = BinaryAssociation(
    name="selfLetProperty6",
    ends={
        Property(name="selflet_SelfLetProperty", type=selflet_GeneralKnowledge, multiplicity=Multiplicity(1, 1)),
        Property(name="selflet_GeneralKnowledge", type=selflet_SelfLetProperty, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
parameter7: BinaryAssociation = BinaryAssociation(
    name="parameter7",
    ends={
        Property(name="selflet_Parameter", type=selflet_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="selflet_Input", type=selflet_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter10: BinaryAssociation = BinaryAssociation(
    name="parameter10",
    ends={
        Property(name="selflet_Parameter11", type=selflet_Output, multiplicity=Multiplicity(1, 1)),
        Property(name="selflet_Output", type=selflet_Parameter, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
passive16: BinaryAssociation = BinaryAssociation(
    name="passive16",
    ends={
        Property(name="selflet_Empty", type=selflet_SelfletProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="selflet_SelfletProperties17", type=selflet_Empty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
active18: BinaryAssociation = BinaryAssociation(
    name="active18",
    ends={
        Property(name="selflet_Active", type=selflet_SelfletProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="selflet_SelfletProperties19", type=selflet_Active, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rule12: BinaryAssociation = BinaryAssociation(
    name="rule12",
    ends={
        Property(name="selflet_Rule", type=selflet_Rules, multiplicity=Multiplicity(1, 1)),
        Property(name="selflet_Rules", type=selflet_Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
selfletProperties13: BinaryAssociation = BinaryAssociation(
    name="selfletProperties13",
    ends={
        Property(name="selflet_SelfletProperties", type=selflet_Selflet, multiplicity=Multiplicity(1, 1)),
        Property(name="selflet_Selflet", type=selflet_SelfletProperties, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
selfletResources14: BinaryAssociation = BinaryAssociation(
    name="selfletResources14",
    ends={
        Property(name="selflet_SelfletResources", type=selflet_Selflet, multiplicity=Multiplicity(1, 1)),
        Property(name="selflet_Selflet15", type=selflet_SelfletResources, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reds20: BinaryAssociation = BinaryAssociation(
    name="reds20",
    ends={
        Property(name="selflet_Reds", type=selflet_SelfletProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="selflet_SelfletProperties21", type=selflet_Reds, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
abilities27: BinaryAssociation = BinaryAssociation(
    name="abilities27",
    ends={
        Property(name="selflet_Abilities29", type=selflet_SelfletResources, multiplicity=Multiplicity(1, 1)),
        Property(name="selflet_SelfletResources28", type=selflet_Abilities, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
actions30: BinaryAssociation = BinaryAssociation(
    name="actions30",
    ends={
        Property(name="selflet_Actions32", type=selflet_SelfletResources, multiplicity=Multiplicity(1, 1)),
        Property(name="selflet_SelfletResources31", type=selflet_Actions, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
generalknowledge22: BinaryAssociation = BinaryAssociation(
    name="generalknowledge22",
    ends={
        Property(name="selflet_GeneralKnowledge24", type=selflet_SelfletProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="selflet_SelfletProperties23", type=selflet_GeneralKnowledge, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeKnowledge25: BinaryAssociation = BinaryAssociation(
    name="typeKnowledge25",
    ends={
        Property(name="selflet_TypeKnowledge", type=selflet_SelfletProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="selflet_SelfletProperties26", type=selflet_TypeKnowledge, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
service41: BinaryAssociation = BinaryAssociation(
    name="service41",
    ends={
        Property(name="selflet_Service43", type=selflet_Services, multiplicity=Multiplicity(1, 1)),
        Property(name="selflet_Services42", type=selflet_Service, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
input44: BinaryAssociation = BinaryAssociation(
    name="input44",
    ends={
        Property(name="selflet_Input46", type=selflet_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="selflet_Service45", type=selflet_Input, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
output47: BinaryAssociation = BinaryAssociation(
    name="output47",
    ends={
        Property(name="selflet_Output49", type=selflet_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="selflet_Service48", type=selflet_Output, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
offermode50: BinaryAssociation = BinaryAssociation(
    name="offermode50",
    ends={
        Property(name="selflet_OfferMode", type=selflet_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="selflet_Service51", type=selflet_OfferMode, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
conditions33: BinaryAssociation = BinaryAssociation(
    name="conditions33",
    ends={
        Property(name="selflet_Conditions35", type=selflet_SelfletResources, multiplicity=Multiplicity(1, 1)),
        Property(name="selflet_SelfletResources34", type=selflet_Conditions, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
services36: BinaryAssociation = BinaryAssociation(
    name="services36",
    ends={
        Property(name="selflet_Services", type=selflet_SelfletResources, multiplicity=Multiplicity(1, 1)),
        Property(name="selflet_SelfletResources37", type=selflet_Services, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rules38: BinaryAssociation = BinaryAssociation(
    name="rules38",
    ends={
        Property(name="selflet_Rules40", type=selflet_SelfletResources, multiplicity=Multiplicity(1, 1)),
        Property(name="selflet_SelfletResources39", type=selflet_Rules, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
selfLetProperty55: BinaryAssociation = BinaryAssociation(
    name="selfLetProperty55",
    ends={
        Property(name="selflet_SelfLetProperty57", type=selflet_TypeKnowledge, multiplicity=Multiplicity(1, 1)),
        Property(name="selflet_TypeKnowledge56", type=selflet_SelfLetProperty, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
states58: BinaryAssociation = BinaryAssociation(
    name="states58",
    ends={
        Property(name="selflet_State", type=selflet_ElementaryBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="selflet_ElementaryBehavior", type=selflet_State, multiplicity=Multiplicity(3, 3), is_composite=True)
    }
)
states59: BinaryAssociation = BinaryAssociation(
    name="states59",
    ends={
        Property(name="selflet_State60", type=selflet_ComplexBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="selflet_ComplexBehavior", type=selflet_State, multiplicity=Multiplicity(3, 9999), is_composite=True)
    }
)
next62: BinaryAssociation = BinaryAssociation(
    name="next62",
    ends={
        Property(name="selflet_State63", type=selflet_State, multiplicity=Multiplicity(1, 1)),
        Property(name="selflet_State61", type=selflet_State, multiplicity=Multiplicity(0, 9999))
    }
)
implementations52: BinaryAssociation = BinaryAssociation(
    name="implementations52",
    ends={
        Property(name="selflet_Behavior54", type=selflet_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="selflet_Service53", type=selflet_Behavior, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
do64: BinaryAssociation = BinaryAssociation(
    name="do64",
    ends={
        Property(name="selflet_Action65", type=selflet_AbilityState, multiplicity=Multiplicity(1, 1)),
        Property(name="selflet_AbilityState", type=selflet_Action, multiplicity=Multiplicity(1, 1))
    }
)
invoke66: BinaryAssociation = BinaryAssociation(
    name="invoke66",
    ends={
        Property(name="selflet_Service67", type=selflet_IntermediateState, multiplicity=Multiplicity(1, 1)),
        Property(name="selflet_IntermediateState", type=selflet_Service, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_selflet_ElementaryBehavior_Behavior = Generalization(general=Behavior, specific=selflet_ElementaryBehavior)
gen_selflet_ComplexBehavior_Behavior = Generalization(general=Behavior, specific=selflet_ComplexBehavior)
gen_selflet_InitialState_State = Generalization(general=State, specific=selflet_InitialState)
gen_selflet_FinalState_State = Generalization(general=State, specific=selflet_FinalState)
gen_selflet_AbilityState_State = Generalization(general=State, specific=selflet_AbilityState)
gen_selflet_IntermediateState_State = Generalization(general=State, specific=selflet_IntermediateState)

# Domain Model
domain_model = DomainModel(
    name="selflet",
    types={selflet_Active, selflet_Behavior, selflet_Abilities, selflet_Ability, selflet_Methods, selflet_Actions, selflet_Action, selflet_CPUUtilization, selflet_Empty, selflet_GeneralKnowledge, selflet_Service, selflet_Conditions, selflet_Condition, selflet_SelfLetProperty, selflet_Input, selflet_Parameter, selflet_Method, selflet_Reds, selflet_OfferMode, selflet_Output, selflet_Rules, selflet_Rule, selflet_Selflet, selflet_SelfletProperties, selflet_SelfletResources, selflet_TypeKnowledge, selflet_Services, selflet_ElementaryBehavior, Behavior, selflet_State, selflet_ComplexBehavior, selflet_InitialState, State, selflet_FinalState, selflet_AbilityState, selflet_IntermediateState, Mode, Type},
    associations={ability0, methods1, action3, implements4, condition5, method8, selfLetProperty6, parameter7, parameter10, passive16, active18, rule12, selfletProperties13, selfletResources14, reds20, abilities27, actions30, generalknowledge22, typeKnowledge25, service41, input44, output47, offermode50, conditions33, services36, rules38, selfLetProperty55, states58, states59, next62, implementations52, do64, invoke66},
    generalizations={gen_selflet_ElementaryBehavior_Behavior, gen_selflet_ComplexBehavior_Behavior, gen_selflet_InitialState_State, gen_selflet_FinalState_State, gen_selflet_AbilityState_State, gen_selflet_IntermediateState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)