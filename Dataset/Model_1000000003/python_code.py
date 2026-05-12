from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class TagsSector(Enum):
    Agriculture = "Agriculture"
    Defence = "Defence"
    Health = "Health"
    Competition = "Competition"
    Environment = "Environment"
    Economz = "Economz"
    Education = "Education"
    Trade = "Trade"
    Innovation = "Innovation"
    Inclusive_development = "Inclusive_development"
    Investment = "Investment"
class LicensingType(Enum):
    Open_Source = "Open_Source"
    Proprietary = "Proprietary"
class ProjectStatus(Enum):
    Archived = "Archived"
    Created = "Created"
    Pending = "Pending"
    Ready = "Ready"
    Closed = "Closed"
class DatasetType(Enum):
    Training = "Training"
    Test = "Test"
    Validation = "Validation"
class TagsVerificationTarget(Enum):
    Transparency = "Transparency"
    Accountability = "Accountability"
    Risk_management = "Risk_management"
    Human_Agency_and_Oversight = "Human_Agency_and_Oversight"
    Technical_Robustness__and_Saftey = "Technical_Robustness__and_Saftey"
    Privacy_and_Data_Governance = "Privacy_and_Data_Governance"
    Diversity_Nondiscrimination_and_Fairness = "Diversity_Nondiscrimination_and_Fairness"
    Societal_and_enviornmanetal_wellbeing = "Societal_and_enviornmanetal_wellbeing"
class EvaluationStatus(Enum):
    Archived = "Archived"
    Pending = "Pending"
    Processing = "Processing"
    Custom = "Custom"
    Done = "Done"
class VerificationType(Enum):
    Case_1 = "Case_1"
    Case_2 = "Case_2"
    Case_3 = "Case_3"
class TagsTargetSystem(Enum):
    Computer_Vision = "Computer_Vision"
    Natural_Language_Processing = "Natural_Language_Processing"
    Audio = "Audio"
    Multimodal = "Multimodal"
    Knowledge_and_Retrival = "Knowledge_and_Retrival"
    Decision_and_Optimization = "Decision_and_Optimization"
    Recommendation_and_Personalization = "Recommendation_and_Personalization"
    Predictive_and_Analytical_AI = "Predictive_and_Analytical_AI"
    Tabular_and_Structured_Data = "Tabular_and_Structured_Data"
    Reinforcement_Learning_and_Control = "Reinforcement_Learning_and_Control"
    Agents_and_Agentic_Systems = "Agents_and_Agentic_Systems"
    AI_Safety_and_Governance = "AI_Safety_and_Governance"
    Emerging_Other = "Emerging_Other"

############################################
# Definition of Classes
############################################










class Evaluation:

    def __init__(self, status: EvaluationStatus, observations: set["Observation"] = None, config: "Configuration" = None, project: "Project" = None, evaluates: "Element" = None, ref: set["Element"] = None):
        self.status = status
        self.observations = observations if observations is not None else set()
        self.config = config
        self.project = project
        self.evaluates = evaluates
        self.ref = ref if ref is not None else set()
        
        pass
    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: EvaluationStatus):
        self.__status = status

    @property
    def observations(self):
        return self.__observations
    @observations.setter
    def observations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Evaluation__observations", None)
        self.__observations = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eval"):
                    opp_val = getattr(item, "eval", None)
                    
                    if opp_val == self:
                        setattr(item, "eval", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eval"):
                    opp_val = getattr(item, "eval", None)
                    
                    setattr(item, "eval", self)
                    

    @property
    def config(self):
        return self.__config
    @config.setter
    def config(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Evaluation__config", None)
        self.__config = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eval"):
                opp_val = getattr(old_value, "eval", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eval"):
                opp_val = getattr(value, "eval", None)
                if opp_val is None:
                    setattr(value, "eval", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def project(self):
        return self.__project
    @project.setter
    def project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Evaluation__project", None)
        self.__project = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eval"):
                opp_val = getattr(old_value, "eval", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eval"):
                opp_val = getattr(value, "eval", None)
                if opp_val is None:
                    setattr(value, "eval", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def evaluates(self):
        return self.__evaluates
    @evaluates.setter
    def evaluates(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Evaluation__evaluates", None)
        self.__evaluates = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "evalu"):
                opp_val = getattr(old_value, "evalu", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "evalu"):
                opp_val = getattr(value, "evalu", None)
                if opp_val is None:
                    setattr(value, "evalu", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ref(self):
        return self.__ref
    @ref.setter
    def ref(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Evaluation__ref", None)
        self.__ref = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eval"):
                    opp_val = getattr(item, "eval", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eval"):
                    opp_val = getattr(item, "eval", None)
                    
                    if opp_val is None:
                        setattr(item, "eval", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Measure:

    def __init__(self, value: str, error: str, uncertainty: float, unit: str, measurand: "Element" = None, metric: "Metric" = None, observation: "Observation" = None):
        self.value = value
        self.error = error
        self.uncertainty = uncertainty
        self.unit = unit
        self.measurand = measurand
        self.metric = metric
        self.observation = observation
        
        pass
    @property
    def error(self):
        return self.__error
    @error.setter
    def error(self, error: str):
        self.__error = error

    @property
    def uncertainty(self):
        return self.__uncertainty
    @uncertainty.setter
    def uncertainty(self, uncertainty: float):
        self.__uncertainty = uncertainty

    @property
    def unit(self):
        return self.__unit
    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def measurand(self):
        return self.__measurand
    @measurand.setter
    def measurand(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Measure__measurand", None)
        self.__measurand = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "measure"):
                opp_val = getattr(old_value, "measure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "measure"):
                opp_val = getattr(value, "measure", None)
                if opp_val is None:
                    setattr(value, "measure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def observation(self):
        return self.__observation
    @observation.setter
    def observation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Measure__observation", None)
        self.__observation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "measures"):
                opp_val = getattr(old_value, "measures", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "measures"):
                opp_val = getattr(value, "measures", None)
                if opp_val is None:
                    setattr(value, "measures", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metric(self):
        return self.__metric
    @metric.setter
    def metric(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Measure__metric", None)
        self.__metric = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "measures"):
                opp_val = getattr(old_value, "measures", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "measures"):
                opp_val = getattr(value, "measures", None)
                if opp_val is None:
                    setattr(value, "measures", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class LegalRequirement:

    def __init__(self, legal_ref: str, standard: str, principle: str, project_1: "Project" = None):
        self.legal_ref = legal_ref
        self.standard = standard
        self.principle = principle
        self.project_1 = project_1
        
        pass
    @property
    def standard(self):
        return self.__standard
    @standard.setter
    def standard(self, standard: str):
        self.__standard = standard

    @property
    def principle(self):
        return self.__principle
    @principle.setter
    def principle(self, principle: str):
        self.__principle = principle

    @property
    def legal_ref(self):
        return self.__legal_ref
    @legal_ref.setter
    def legal_ref(self, legal_ref: str):
        self.__legal_ref = legal_ref

    @property
    def project_1(self):
        return self.__project_1
    @project_1.setter
    def project_1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LegalRequirement__project_1", None)
        self.__project_1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "legal_requirements"):
                opp_val = getattr(old_value, "legal_requirements", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "legal_requirements"):
                opp_val = getattr(value, "legal_requirements", None)
                if opp_val is None:
                    setattr(value, "legal_requirements", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class AssessmentElement(ABC):

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description



class Tool(AssessmentElement):

    def __init__(self, name: str, description: str, licensing: LicensingType, verification_type: VerificationType, provider: str, project: str, branch: str, version: str, project_maturity: str, scientific_reference: str, verification_targets: TagsVerificationTarget, sector: TagsSector, target_system: TagsTargetSystem, target_legal_requirements: str, observation_1: set["Observation"] = None):
        super().__init__(name, description)
        self.licensing = licensing
        self.verification_type = verification_type
        self.provider = provider
        self.project = project
        self.branch = branch
        self.version = version
        self.project_maturity = project_maturity
        self.scientific_reference = scientific_reference
        self.verification_targets = verification_targets
        self.sector = sector
        self.target_system = target_system
        self.target_legal_requirements = target_legal_requirements
        self.observation_1 = observation_1 if observation_1 is not None else set()
        
        pass
    @property
    def branch(self):
        return self.__branch
    @branch.setter
    def branch(self, branch: str):
        self.__branch = branch

    @property
    def sector(self):
        return self.__sector
    @sector.setter
    def sector(self, sector: TagsSector):
        self.__sector = sector

    @property
    def target_legal_requirements(self):
        return self.__target_legal_requirements
    @target_legal_requirements.setter
    def target_legal_requirements(self, target_legal_requirements: str):
        self.__target_legal_requirements = target_legal_requirements

    @property
    def version(self):
        return self.__version
    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def project(self):
        return self.__project
    @project.setter
    def project(self, project: str):
        self.__project = project

    @property
    def scientific_reference(self):
        return self.__scientific_reference
    @scientific_reference.setter
    def scientific_reference(self, scientific_reference: str):
        self.__scientific_reference = scientific_reference

    @property
    def verification_type(self):
        return self.__verification_type
    @verification_type.setter
    def verification_type(self, verification_type: VerificationType):
        self.__verification_type = verification_type

    @property
    def licensing(self):
        return self.__licensing
    @licensing.setter
    def licensing(self, licensing: LicensingType):
        self.__licensing = licensing

    @property
    def provider(self):
        return self.__provider
    @provider.setter
    def provider(self, provider: str):
        self.__provider = provider

    @property
    def project_maturity(self):
        return self.__project_maturity
    @project_maturity.setter
    def project_maturity(self, project_maturity: str):
        self.__project_maturity = project_maturity

    @property
    def verification_targets(self):
        return self.__verification_targets
    @verification_targets.setter
    def verification_targets(self, verification_targets: TagsVerificationTarget):
        self.__verification_targets = verification_targets

    @property
    def target_system(self):
        return self.__target_system
    @target_system.setter
    def target_system(self, target_system: TagsTargetSystem):
        self.__target_system = target_system

    @property
    def observation_1(self):
        return self.__observation_1
    @observation_1.setter
    def observation_1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Tool__observation_1", None)
        self.__observation_1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool"):
                    opp_val = getattr(item, "tool", None)
                    
                    if opp_val == self:
                        setattr(item, "tool", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool"):
                    opp_val = getattr(item, "tool", None)
                    
                    setattr(item, "tool", self)
                    



class Observation(AssessmentElement):

    def __init__(self, observer: str, whenObserved: datetime, name: str, description: str, measures: set["Measure"] = None, eval: "Evaluation" = None, tool: "Tool" = None, dataset: "Dataset" = None):
        super().__init__(name, description)
        self.observer = observer
        self.whenObserved = whenObserved
        self.measures = measures if measures is not None else set()
        self.eval = eval
        self.tool = tool
        self.dataset = dataset
        
        pass
    @property
    def whenObserved(self):
        return self.__whenObserved
    @whenObserved.setter
    def whenObserved(self, whenObserved: datetime):
        self.__whenObserved = whenObserved

    @property
    def observer(self):
        return self.__observer
    @observer.setter
    def observer(self, observer: str):
        self.__observer = observer

    @property
    def eval(self):
        return self.__eval
    @eval.setter
    def eval(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Observation__eval", None)
        self.__eval = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "observations"):
                opp_val = getattr(old_value, "observations", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "observations"):
                opp_val = getattr(value, "observations", None)
                if opp_val is None:
                    setattr(value, "observations", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tool(self):
        return self.__tool
    @tool.setter
    def tool(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Observation__tool", None)
        self.__tool = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "observation_1"):
                opp_val = getattr(old_value, "observation_1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "observation_1"):
                opp_val = getattr(value, "observation_1", None)
                if opp_val is None:
                    setattr(value, "observation_1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dataset(self):
        return self.__dataset
    @dataset.setter
    def dataset(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Observation__dataset", None)
        self.__dataset = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "observation_2"):
                opp_val = getattr(old_value, "observation_2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "observation_2"):
                opp_val = getattr(value, "observation_2", None)
                if opp_val is None:
                    setattr(value, "observation_2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def measures(self):
        return self.__measures
    @measures.setter
    def measures(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Observation__measures", None)
        self.__measures = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "observation"):
                    opp_val = getattr(item, "observation", None)
                    
                    if opp_val == self:
                        setattr(item, "observation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "observation"):
                    opp_val = getattr(item, "observation", None)
                    
                    setattr(item, "observation", self)
                    



class Element(AssessmentElement):

    def __init__(self, name: str, description: str, measure: set["Measure"] = None, project: "Project" = None, evalu: set["Evaluation"] = None, eval: set["Evaluation"] = None):
        super().__init__(name, description)
        self.measure = measure if measure is not None else set()
        self.project = project
        self.evalu = evalu if evalu is not None else set()
        self.eval = eval if eval is not None else set()
        
        pass
    @property
    def project(self):
        return self.__project
    @project.setter
    def project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Element__project", None)
        self.__project = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "involves"):
                opp_val = getattr(old_value, "involves", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "involves"):
                opp_val = getattr(value, "involves", None)
                if opp_val is None:
                    setattr(value, "involves", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eval(self):
        return self.__eval
    @eval.setter
    def eval(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Element__eval", None)
        self.__eval = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ref"):
                    opp_val = getattr(item, "ref", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ref"):
                    opp_val = getattr(item, "ref", None)
                    
                    if opp_val is None:
                        setattr(item, "ref", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def measure(self):
        return self.__measure
    @measure.setter
    def measure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Element__measure", None)
        self.__measure = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "measurand"):
                    opp_val = getattr(item, "measurand", None)
                    
                    if opp_val == self:
                        setattr(item, "measurand", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "measurand"):
                    opp_val = getattr(item, "measurand", None)
                    
                    setattr(item, "measurand", self)
                    

    @property
    def evalu(self):
        return self.__evalu
    @evalu.setter
    def evalu(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Element__evalu", None)
        self.__evalu = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "evaluates"):
                    opp_val = getattr(item, "evaluates", None)
                    
                    if opp_val == self:
                        setattr(item, "evaluates", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "evaluates"):
                    opp_val = getattr(item, "evaluates", None)
                    
                    setattr(item, "evaluates", self)
                    



class AISystem(Element):

    def __init__(self, settings: str, data: str, source: str, licensing: LicensingType, version: str, name: str, description: str, dataset: set["Dataset"] = None, project: "Project" = None, eval: set["Evaluation"] = None, measure: set["Measure"] = None, evalu: set["Evaluation"] = None):
        super().__init__(name, description, project, eval, measure, evalu)
        self.settings = settings
        self.data = data
        self.source = source
        self.licensing = licensing
        self.version = version
        self.dataset = dataset if dataset is not None else set()
        
        pass
    @property
    def version(self):
        return self.__version
    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def source(self):
        return self.__source
    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def licensing(self):
        return self.__licensing
    @licensing.setter
    def licensing(self, licensing: LicensingType):
        self.__licensing = licensing

    @property
    def settings(self):
        return self.__settings
    @settings.setter
    def settings(self, settings: str):
        self.__settings = settings

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data: str):
        self.__data = data

    @property
    def dataset(self):
        return self.__dataset
    @dataset.setter
    def dataset(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AISystem__dataset", None)
        self.__dataset = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "models"):
                    opp_val = getattr(item, "models", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "models"):
                    opp_val = getattr(item, "models", None)
                    
                    if opp_val is None:
                        setattr(item, "models", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class ConfParam(AssessmentElement):

    def __init__(self, param_type: str, value: str, name: str, description: str, conf: "Configuration" = None):
        super().__init__(name, description)
        self.param_type = param_type
        self.value = value
        self.conf = conf
        
        pass
    @property
    def param_type(self):
        return self.__param_type
    @param_type.setter
    def param_type(self, param_type: str):
        self.__param_type = param_type

    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def conf(self):
        return self.__conf
    @conf.setter
    def conf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ConfParam__conf", None)
        self.__conf = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "params"):
                opp_val = getattr(old_value, "params", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "params"):
                opp_val = getattr(value, "params", None)
                if opp_val is None:
                    setattr(value, "params", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Metric(AssessmentElement):

    def __init__(self, name: str, description: str, category: set["MetricCategory"] = None, measures: set["Measure"] = None, derivedBy: set["Derived"] = None):
        super().__init__(name, description)
        self.category = category if category is not None else set()
        self.measures = measures if measures is not None else set()
        self.derivedBy = derivedBy if derivedBy is not None else set()
        
        pass
    @property
    def measures(self):
        return self.__measures
    @measures.setter
    def measures(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Metric__measures", None)
        self.__measures = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metric"):
                    opp_val = getattr(item, "metric", None)
                    
                    if opp_val == self:
                        setattr(item, "metric", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metric"):
                    opp_val = getattr(item, "metric", None)
                    
                    setattr(item, "metric", self)
                    

    @property
    def category(self):
        return self.__category
    @category.setter
    def category(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Metric__category", None)
        self.__category = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metrics"):
                    opp_val = getattr(item, "metrics", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metrics"):
                    opp_val = getattr(item, "metrics", None)
                    
                    if opp_val is None:
                        setattr(item, "metrics", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def derivedBy(self):
        return self.__derivedBy
    @derivedBy.setter
    def derivedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Metric__derivedBy", None)
        self.__derivedBy = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "baseMetric"):
                    opp_val = getattr(item, "baseMetric", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "baseMetric"):
                    opp_val = getattr(item, "baseMetric", None)
                    
                    if opp_val is None:
                        setattr(item, "baseMetric", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Derived(Metric):

    def __init__(self, expression: str, name: str, description: str, baseMetric: set["Metric"] = None, measures: set["Measure"] = None, category: set["MetricCategory"] = None, derivedBy: set["Derived"] = None):
        super().__init__(name, description, measures, category, derivedBy)
        self.expression = expression
        self.baseMetric = baseMetric if baseMetric is not None else set()
        
        pass
    @property
    def expression(self):
        return self.__expression
    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def baseMetric(self):
        return self.__baseMetric
    @baseMetric.setter
    def baseMetric(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Derived__baseMetric", None)
        self.__baseMetric = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "derivedBy"):
                    opp_val = getattr(item, "derivedBy", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "derivedBy"):
                    opp_val = getattr(item, "derivedBy", None)
                    
                    if opp_val is None:
                        setattr(item, "derivedBy", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Direct(Metric):

    def __init__(self, name: str, description: str, measures: set["Measure"] = None, category: set["MetricCategory"] = None, derivedBy: set["Derived"] = None):
        super().__init__(name, description, measures, category, derivedBy)
        
        pass


class Configuration(AssessmentElement):

    def __init__(self, name: str, description: str, params: set["ConfParam"] = None, eval: set["Evaluation"] = None):
        super().__init__(name, description)
        self.params = params if params is not None else set()
        self.eval = eval if eval is not None else set()
        
        pass
    @property
    def params(self):
        return self.__params
    @params.setter
    def params(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Configuration__params", None)
        self.__params = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "conf"):
                    opp_val = getattr(item, "conf", None)
                    
                    if opp_val == self:
                        setattr(item, "conf", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "conf"):
                    opp_val = getattr(item, "conf", None)
                    
                    setattr(item, "conf", self)
                    

    @property
    def eval(self):
        return self.__eval
    @eval.setter
    def eval(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Configuration__eval", None)
        self.__eval = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "config"):
                    opp_val = getattr(item, "config", None)
                    
                    if opp_val == self:
                        setattr(item, "config", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "config"):
                    opp_val = getattr(item, "config", None)
                    
                    setattr(item, "config", self)
                    



class MetricCategory(AssessmentElement):

    def __init__(self, name: str, description: str, metrics: set["Metric"] = None):
        super().__init__(name, description)
        self.metrics = metrics if metrics is not None else set()
        
        pass
    @property
    def metrics(self):
        return self.__metrics
    @metrics.setter
    def metrics(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MetricCategory__metrics", None)
        self.__metrics = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "category"):
                    opp_val = getattr(item, "category", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "category"):
                    opp_val = getattr(item, "category", None)
                    
                    if opp_val is None:
                        setattr(item, "category", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Feature(Element):

    def __init__(self, feature_type: str, min_value: float, max_value: float, name: str, description: str, date: set["Datashape"] = None, features: "Datashape" = None, project: "Project" = None, eval: set["Evaluation"] = None, measure: set["Measure"] = None, evalu: set["Evaluation"] = None):
        super().__init__(name, description, project, eval, measure, evalu)
        self.feature_type = feature_type
        self.min_value = min_value
        self.max_value = max_value
        self.date = date if date is not None else set()
        self.features = features
        
        pass
    @property
    def feature_type(self):
        return self.__feature_type
    @feature_type.setter
    def feature_type(self, feature_type: str):
        self.__feature_type = feature_type

    @property
    def min_value(self):
        return self.__min_value
    @min_value.setter
    def min_value(self, min_value: float):
        self.__min_value = min_value

    @property
    def max_value(self):
        return self.__max_value
    @max_value.setter
    def max_value(self, max_value: float):
        self.__max_value = max_value

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Feature__date", None)
        self.__date = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "f_date"):
                    opp_val = getattr(item, "f_date", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "f_date"):
                    opp_val = getattr(item, "f_date", None)
                    
                    if opp_val is None:
                        setattr(item, "f_date", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def features(self):
        return self.__features
    @features.setter
    def features(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Feature__features", None)
        self.__features = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "f_features"):
                opp_val = getattr(old_value, "f_features", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "f_features"):
                opp_val = getattr(value, "f_features", None)
                if opp_val is None:
                    setattr(value, "f_features", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Datashape:

    def __init__(self, accepted_target_values: str, f_date: set["Feature"] = None, f_features: set["Feature"] = None, dataset_1: set["Dataset"] = None):
        self.accepted_target_values = accepted_target_values
        self.f_date = f_date if f_date is not None else set()
        self.f_features = f_features if f_features is not None else set()
        self.dataset_1 = dataset_1 if dataset_1 is not None else set()
        
        pass
    @property
    def accepted_target_values(self):
        return self.__accepted_target_values
    @accepted_target_values.setter
    def accepted_target_values(self, accepted_target_values: str):
        self.__accepted_target_values = accepted_target_values

    @property
    def f_date(self):
        return self.__f_date
    @f_date.setter
    def f_date(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Datashape__f_date", None)
        self.__f_date = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "date"):
                    opp_val = getattr(item, "date", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "date"):
                    opp_val = getattr(item, "date", None)
                    
                    if opp_val is None:
                        setattr(item, "date", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def f_features(self):
        return self.__f_features
    @f_features.setter
    def f_features(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Datashape__f_features", None)
        self.__f_features = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "features"):
                    opp_val = getattr(item, "features", None)
                    
                    if opp_val == self:
                        setattr(item, "features", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "features"):
                    opp_val = getattr(item, "features", None)
                    
                    setattr(item, "features", self)
                    

    @property
    def dataset_1(self):
        return self.__dataset_1
    @dataset_1.setter
    def dataset_1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Datashape__dataset_1", None)
        self.__dataset_1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datashape"):
                    opp_val = getattr(item, "datashape", None)
                    
                    if opp_val == self:
                        setattr(item, "datashape", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datashape"):
                    opp_val = getattr(item, "datashape", None)
                    
                    setattr(item, "datashape", self)
                    



class Dataset(Element):

    def __init__(self, source: str, version: str, licensing: LicensingType, dataset_type: DatasetType, name: str, description: str, models: set["AISystem"] = None, datashape: "Datashape" = None, observation_2: set["Observation"] = None, project: "Project" = None, eval: set["Evaluation"] = None, measure: set["Measure"] = None, evalu: set["Evaluation"] = None):
        super().__init__(name, description, project, eval, measure, evalu)
        self.source = source
        self.version = version
        self.licensing = licensing
        self.dataset_type = dataset_type
        self.models = models if models is not None else set()
        self.datashape = datashape
        self.observation_2 = observation_2 if observation_2 is not None else set()
        
        pass
    @property
    def licensing(self):
        return self.__licensing
    @licensing.setter
    def licensing(self, licensing: LicensingType):
        self.__licensing = licensing

    @property
    def source(self):
        return self.__source
    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def dataset_type(self):
        return self.__dataset_type
    @dataset_type.setter
    def dataset_type(self, dataset_type: DatasetType):
        self.__dataset_type = dataset_type

    @property
    def version(self):
        return self.__version
    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def datashape(self):
        return self.__datashape
    @datashape.setter
    def datashape(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dataset__datashape", None)
        self.__datashape = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dataset_1"):
                opp_val = getattr(old_value, "dataset_1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dataset_1"):
                opp_val = getattr(value, "dataset_1", None)
                if opp_val is None:
                    setattr(value, "dataset_1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def models(self):
        return self.__models
    @models.setter
    def models(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dataset__models", None)
        self.__models = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dataset"):
                    opp_val = getattr(item, "dataset", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dataset"):
                    opp_val = getattr(item, "dataset", None)
                    
                    if opp_val is None:
                        setattr(item, "dataset", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def observation_2(self):
        return self.__observation_2
    @observation_2.setter
    def observation_2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dataset__observation_2", None)
        self.__observation_2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dataset"):
                    opp_val = getattr(item, "dataset", None)
                    
                    if opp_val == self:
                        setattr(item, "dataset", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dataset"):
                    opp_val = getattr(item, "dataset", None)
                    
                    setattr(item, "dataset", self)
                    



class Project:

    def __init__(self, name: str, status: ProjectStatus, eval: set["Evaluation"] = None, involves: set["Element"] = None, legal_requirements: set["LegalRequirement"] = None):
        self.name = name
        self.status = status
        self.eval = eval if eval is not None else set()
        self.involves = involves if involves is not None else set()
        self.legal_requirements = legal_requirements if legal_requirements is not None else set()
        
        pass
    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: ProjectStatus):
        self.__status = status

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eval(self):
        return self.__eval
    @eval.setter
    def eval(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Project__eval", None)
        self.__eval = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "project"):
                    opp_val = getattr(item, "project", None)
                    
                    if opp_val == self:
                        setattr(item, "project", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "project"):
                    opp_val = getattr(item, "project", None)
                    
                    setattr(item, "project", self)
                    

    @property
    def legal_requirements(self):
        return self.__legal_requirements
    @legal_requirements.setter
    def legal_requirements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Project__legal_requirements", None)
        self.__legal_requirements = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "project_1"):
                    opp_val = getattr(item, "project_1", None)
                    
                    if opp_val == self:
                        setattr(item, "project_1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "project_1"):
                    opp_val = getattr(item, "project_1", None)
                    
                    setattr(item, "project_1", self)
                    

    @property
    def involves(self):
        return self.__involves
    @involves.setter
    def involves(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Project__involves", None)
        self.__involves = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "project"):
                    opp_val = getattr(item, "project", None)
                    
                    if opp_val == self:
                        setattr(item, "project", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "project"):
                    opp_val = getattr(item, "project", None)
                    
                    setattr(item, "project", self)
                    

