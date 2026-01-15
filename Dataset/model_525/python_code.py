from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Gender(Enum):
    UNKNOWN = "UNKNOWN"
    MALE = "MALE"
    FEMALE = "FEMALE"


############################################
# Definition of Classes
############################################

class Lims_Sequenced:

    pass
class Lims_Sequencer:

    def __init__(self, name: str, sequencer: set["Lims_Run"] = None, Sequencer: "Lims_Laboratory" = None, Sequencer18: "Lims_Run" = None, sequencers: "Lims_Laboratory" = None):
        self.name = name
        self.sequencer = sequencer if sequencer is not None else set()
        self.Sequencer = Sequencer
        self.Sequencer18 = Sequencer18
        self.sequencers = sequencers
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Sequencer(self):
        return self.__Sequencer

    @Sequencer.setter
    def Sequencer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Lims_Sequencer__Sequencer", None)
        self.__Sequencer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "laboratory4"):
                opp_val = getattr(old_value, "laboratory4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "laboratory4"):
                opp_val = getattr(value, "laboratory4", None)
                if opp_val is None:
                    setattr(value, "laboratory4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Sequencer18(self):
        return self.__Sequencer18

    @Sequencer18.setter
    def Sequencer18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Lims_Sequencer__Sequencer18", None)
        self.__Sequencer18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "runs"):
                opp_val = getattr(old_value, "runs", None)
                if opp_val == self:
                    setattr(old_value, "runs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "runs"):
                opp_val = getattr(value, "runs", None)
                setattr(value, "runs", self)

    @property
    def sequencer(self):
        return self.__sequencer

    @sequencer.setter
    def sequencer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Lims_Sequencer__sequencer", None)
        self.__sequencer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Run"):
                    opp_val = getattr(item, "Run", None)
                    
                    if opp_val == self:
                        setattr(item, "Run", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Run"):
                    opp_val = getattr(item, "Run", None)
                    
                    setattr(item, "Run", self)
                    

    @property
    def sequencers(self):
        return self.__sequencers

    @sequencers.setter
    def sequencers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Lims_Sequencer__sequencers", None)
        self.__sequencers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Laboratory15"):
                opp_val = getattr(old_value, "Laboratory15", None)
                if opp_val == self:
                    setattr(old_value, "Laboratory15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Laboratory15"):
                opp_val = getattr(value, "Laboratory15", None)
                setattr(value, "Laboratory15", self)

class Lims_Run:

    def __init__(self, name: str, date: date, Run: "Lims_Sequencer" = None, runs: "Lims_Sequencer" = None, Run22: "Lims_Sequenced" = None, run: set["Lims_Sequenced"] = None):
        self.name = name
        self.date = date
        self.Run = Run
        self.runs = runs
        self.Run22 = Run22
        self.run = run if run is not None else set()
        
    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Run22(self):
        return self.__Run22

    @Run22.setter
    def Run22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Lims_Run__Run22", None)
        self.__Run22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sequenced"):
                opp_val = getattr(old_value, "sequenced", None)
                if opp_val == self:
                    setattr(old_value, "sequenced", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sequenced"):
                opp_val = getattr(value, "sequenced", None)
                setattr(value, "sequenced", self)

    @property
    def run(self):
        return self.__run

    @run.setter
    def run(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Lims_Run__run", None)
        self.__run = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Sequenced"):
                    opp_val = getattr(item, "Sequenced", None)
                    
                    if opp_val == self:
                        setattr(item, "Sequenced", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Sequenced"):
                    opp_val = getattr(item, "Sequenced", None)
                    
                    setattr(item, "Sequenced", self)
                    

    @property
    def runs(self):
        return self.__runs

    @runs.setter
    def runs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Lims_Run__runs", None)
        self.__runs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Sequencer18"):
                opp_val = getattr(old_value, "Sequencer18", None)
                if opp_val == self:
                    setattr(old_value, "Sequencer18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Sequencer18"):
                opp_val = getattr(value, "Sequencer18", None)
                setattr(value, "Sequencer18", self)

    @property
    def Run(self):
        return self.__Run

    @Run.setter
    def Run(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Lims_Run__Run", None)
        self.__Run = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sequencer"):
                opp_val = getattr(old_value, "sequencer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sequencer"):
                opp_val = getattr(value, "sequencer", None)
                if opp_val is None:
                    setattr(value, "sequencer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Lims_Sample:

    def __init__(self, id: str, Sample: "Lims_Individual" = None, samples: "Lims_Individual" = None, Lims_Sample: "Lims_Sequenced" = None):
        self.id = id
        self.Sample = Sample
        self.samples = samples
        self.Lims_Sample = Lims_Sample
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def Sample(self):
        return self.__Sample

    @Sample.setter
    def Sample(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Lims_Sample__Sample", None)
        self.__Sample = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "individual"):
                opp_val = getattr(old_value, "individual", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "individual"):
                opp_val = getattr(value, "individual", None)
                if opp_val is None:
                    setattr(value, "individual", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Lims_Sample(self):
        return self.__Lims_Sample

    @Lims_Sample.setter
    def Lims_Sample(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Lims_Sample__Lims_Sample", None)
        self.__Lims_Sample = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Lims_Sequenced"):
                opp_val = getattr(old_value, "Lims_Sequenced", None)
                if opp_val == self:
                    setattr(old_value, "Lims_Sequenced", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Lims_Sequenced"):
                opp_val = getattr(value, "Lims_Sequenced", None)
                setattr(value, "Lims_Sequenced", self)

    @property
    def samples(self):
        return self.__samples

    @samples.setter
    def samples(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Lims_Sample__samples", None)
        self.__samples = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Individual20"):
                opp_val = getattr(old_value, "Individual20", None)
                if opp_val == self:
                    setattr(old_value, "Individual20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Individual20"):
                opp_val = getattr(value, "Individual20", None)
                setattr(value, "Individual20", self)

class Lims_Laboratory:

    pass
class Lims_Individual:

    def __init__(self, gender: str, name: str, Individual: "Lims_Family" = None, individuals: "Lims_Family" = None, Lims_Individual: "Lims_Individual" = None, Lims_Individual7: "Lims_Individual" = None, Lims_Individual11: "Lims_Individual" = None, Lims_Individual9: "Lims_Individual" = None, individual: set["Lims_Sample"] = None, Individual20: "Lims_Sample" = None):
        self.gender = gender
        self.name = name
        self.Individual = Individual
        self.individuals = individuals
        self.Lims_Individual = Lims_Individual
        self.Lims_Individual7 = Lims_Individual7
        self.Lims_Individual11 = Lims_Individual11
        self.Lims_Individual9 = Lims_Individual9
        self.individual = individual if individual is not None else set()
        self.Individual20 = Individual20
        
    @property
    def gender(self) -> str:
        return self.__gender

    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def individual(self):
        return self.__individual

    @individual.setter
    def individual(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Lims_Individual__individual", None)
        self.__individual = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Sample"):
                    opp_val = getattr(item, "Sample", None)
                    
                    if opp_val == self:
                        setattr(item, "Sample", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Sample"):
                    opp_val = getattr(item, "Sample", None)
                    
                    setattr(item, "Sample", self)
                    

    @property
    def individuals(self):
        return self.__individuals

    @individuals.setter
    def individuals(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Lims_Individual__individuals", None)
        self.__individuals = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Family6"):
                opp_val = getattr(old_value, "Family6", None)
                if opp_val == self:
                    setattr(old_value, "Family6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Family6"):
                opp_val = getattr(value, "Family6", None)
                setattr(value, "Family6", self)

    @property
    def Lims_Individual7(self):
        return self.__Lims_Individual7

    @Lims_Individual7.setter
    def Lims_Individual7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Lims_Individual__Lims_Individual7", None)
        self.__Lims_Individual7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Lims_Individual"):
                opp_val = getattr(old_value, "Lims_Individual", None)
                if opp_val == self:
                    setattr(old_value, "Lims_Individual", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Lims_Individual"):
                opp_val = getattr(value, "Lims_Individual", None)
                setattr(value, "Lims_Individual", self)

    @property
    def Lims_Individual(self):
        return self.__Lims_Individual

    @Lims_Individual.setter
    def Lims_Individual(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Lims_Individual__Lims_Individual", None)
        self.__Lims_Individual = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Lims_Individual7"):
                opp_val = getattr(old_value, "Lims_Individual7", None)
                if opp_val == self:
                    setattr(old_value, "Lims_Individual7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Lims_Individual7"):
                opp_val = getattr(value, "Lims_Individual7", None)
                setattr(value, "Lims_Individual7", self)

    @property
    def Individual(self):
        return self.__Individual

    @Individual.setter
    def Individual(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Lims_Individual__Individual", None)
        self.__Individual = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family"):
                opp_val = getattr(old_value, "family", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family"):
                opp_val = getattr(value, "family", None)
                if opp_val is None:
                    setattr(value, "family", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Lims_Individual9(self):
        return self.__Lims_Individual9

    @Lims_Individual9.setter
    def Lims_Individual9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Lims_Individual__Lims_Individual9", None)
        self.__Lims_Individual9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Lims_Individual11"):
                opp_val = getattr(old_value, "Lims_Individual11", None)
                if opp_val == self:
                    setattr(old_value, "Lims_Individual11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Lims_Individual11"):
                opp_val = getattr(value, "Lims_Individual11", None)
                setattr(value, "Lims_Individual11", self)

    @property
    def Individual20(self):
        return self.__Individual20

    @Individual20.setter
    def Individual20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Lims_Individual__Individual20", None)
        self.__Individual20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "samples"):
                opp_val = getattr(old_value, "samples", None)
                if opp_val == self:
                    setattr(old_value, "samples", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "samples"):
                opp_val = getattr(value, "samples", None)
                setattr(value, "samples", self)

    @property
    def Lims_Individual11(self):
        return self.__Lims_Individual11

    @Lims_Individual11.setter
    def Lims_Individual11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Lims_Individual__Lims_Individual11", None)
        self.__Lims_Individual11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Lims_Individual9"):
                opp_val = getattr(old_value, "Lims_Individual9", None)
                if opp_val == self:
                    setattr(old_value, "Lims_Individual9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Lims_Individual9"):
                opp_val = getattr(value, "Lims_Individual9", None)
                setattr(value, "Lims_Individual9", self)

class Lims_Family:

    def __init__(self, name: str, family: set["Lims_Individual"] = None, families: "Lims_Laboratory" = None, Family6: "Lims_Individual" = None, Family: "Lims_Laboratory" = None):
        self.name = name
        self.family = family if family is not None else set()
        self.families = families
        self.Family6 = Family6
        self.Family = Family
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def family(self):
        return self.__family

    @family.setter
    def family(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Lims_Family__family", None)
        self.__family = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Individual"):
                    opp_val = getattr(item, "Individual", None)
                    
                    if opp_val == self:
                        setattr(item, "Individual", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Individual"):
                    opp_val = getattr(item, "Individual", None)
                    
                    setattr(item, "Individual", self)
                    

    @property
    def families(self):
        return self.__families

    @families.setter
    def families(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Lims_Family__families", None)
        self.__families = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Laboratory"):
                opp_val = getattr(old_value, "Laboratory", None)
                if opp_val == self:
                    setattr(old_value, "Laboratory", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Laboratory"):
                opp_val = getattr(value, "Laboratory", None)
                setattr(value, "Laboratory", self)

    @property
    def Family6(self):
        return self.__Family6

    @Family6.setter
    def Family6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Lims_Family__Family6", None)
        self.__Family6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "individuals"):
                opp_val = getattr(old_value, "individuals", None)
                if opp_val == self:
                    setattr(old_value, "individuals", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "individuals"):
                opp_val = getattr(value, "individuals", None)
                setattr(value, "individuals", self)

    @property
    def Family(self):
        return self.__Family

    @Family.setter
    def Family(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Lims_Family__Family", None)
        self.__Family = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "laboratory"):
                opp_val = getattr(old_value, "laboratory", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "laboratory"):
                opp_val = getattr(value, "laboratory", None)
                if opp_val is None:
                    setattr(value, "laboratory", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
