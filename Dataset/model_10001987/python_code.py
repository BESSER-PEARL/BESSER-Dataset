from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Admin:

    def __init__(self, AdminID: int, AminName: str, UserLogin: int, voter13: "Voter" = None, candidate14: "Candidate" = None, election16: "Election" = None, ballotInformation18: "BallotInformation" = None):
        self.AdminID = AdminID
        self.AminName = AminName
        self.UserLogin = UserLogin
        self.voter13 = voter13
        self.candidate14 = candidate14
        self.election16 = election16
        self.ballotInformation18 = ballotInformation18
        
        pass
    @property
    def AminName(self):
        return self.__AminName
    @AminName.setter
    def AminName(self, AminName: str):
        self.__AminName = AminName

    @property
    def AdminID(self):
        return self.__AdminID
    @AdminID.setter
    def AdminID(self, AdminID: int):
        self.__AdminID = AdminID

    @property
    def UserLogin(self):
        return self.__UserLogin
    @UserLogin.setter
    def UserLogin(self, UserLogin: int):
        self.__UserLogin = UserLogin

    @property
    def ballotInformation18(self):
        return self.__ballotInformation18
    @ballotInformation18.setter
    def ballotInformation18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__ballotInformation18", None)
        self.__ballotInformation18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "admin19"):
                opp_val = getattr(old_value, "admin19", None)
                if opp_val == self:
                    setattr(old_value, "admin19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "admin19"):
                opp_val = getattr(value, "admin19", None)
                setattr(value, "admin19", self)

    @property
    def voter13(self):
        return self.__voter13
    @voter13.setter
    def voter13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__voter13", None)
        self.__voter13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "admin12"):
                opp_val = getattr(old_value, "admin12", None)
                if opp_val == self:
                    setattr(old_value, "admin12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "admin12"):
                opp_val = getattr(value, "admin12", None)
                setattr(value, "admin12", self)

    @property
    def election16(self):
        return self.__election16
    @election16.setter
    def election16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__election16", None)
        self.__election16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "admin17"):
                opp_val = getattr(old_value, "admin17", None)
                if opp_val == self:
                    setattr(old_value, "admin17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "admin17"):
                opp_val = getattr(value, "admin17", None)
                setattr(value, "admin17", self)

    @property
    def candidate14(self):
        return self.__candidate14
    @candidate14.setter
    def candidate14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__candidate14", None)
        self.__candidate14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "admin15"):
                opp_val = getattr(old_value, "admin15", None)
                if opp_val == self:
                    setattr(old_value, "admin15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "admin15"):
                opp_val = getattr(value, "admin15", None)
                setattr(value, "admin15", self)



class Election:

    def __init__(self, ElectionID: int, ElectionDate: str, ElectionCriteria: str, ElectionName: str, ballotInformation2: "BallotInformation" = None, voter5: "Voter" = None, candidate11: "Candidate" = None, admin17: "Admin" = None):
        self.ElectionID = ElectionID
        self.ElectionDate = ElectionDate
        self.ElectionCriteria = ElectionCriteria
        self.ElectionName = ElectionName
        self.ballotInformation2 = ballotInformation2
        self.voter5 = voter5
        self.candidate11 = candidate11
        self.admin17 = admin17
        
        pass
    @property
    def ElectionID(self):
        return self.__ElectionID
    @ElectionID.setter
    def ElectionID(self, ElectionID: int):
        self.__ElectionID = ElectionID

    @property
    def ElectionDate(self):
        return self.__ElectionDate
    @ElectionDate.setter
    def ElectionDate(self, ElectionDate: str):
        self.__ElectionDate = ElectionDate

    @property
    def ElectionName(self):
        return self.__ElectionName
    @ElectionName.setter
    def ElectionName(self, ElectionName: str):
        self.__ElectionName = ElectionName

    @property
    def ElectionCriteria(self):
        return self.__ElectionCriteria
    @ElectionCriteria.setter
    def ElectionCriteria(self, ElectionCriteria: str):
        self.__ElectionCriteria = ElectionCriteria

    @property
    def admin17(self):
        return self.__admin17
    @admin17.setter
    def admin17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Election__admin17", None)
        self.__admin17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "election16"):
                opp_val = getattr(old_value, "election16", None)
                if opp_val == self:
                    setattr(old_value, "election16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "election16"):
                opp_val = getattr(value, "election16", None)
                setattr(value, "election16", self)

    @property
    def ballotInformation2(self):
        return self.__ballotInformation2
    @ballotInformation2.setter
    def ballotInformation2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Election__ballotInformation2", None)
        self.__ballotInformation2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "election3"):
                opp_val = getattr(old_value, "election3", None)
                if opp_val == self:
                    setattr(old_value, "election3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "election3"):
                opp_val = getattr(value, "election3", None)
                setattr(value, "election3", self)

    @property
    def voter5(self):
        return self.__voter5
    @voter5.setter
    def voter5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Election__voter5", None)
        self.__voter5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "election4"):
                opp_val = getattr(old_value, "election4", None)
                if opp_val == self:
                    setattr(old_value, "election4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "election4"):
                opp_val = getattr(value, "election4", None)
                setattr(value, "election4", self)

    @property
    def candidate11(self):
        return self.__candidate11
    @candidate11.setter
    def candidate11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Election__candidate11", None)
        self.__candidate11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "election10"):
                opp_val = getattr(old_value, "election10", None)
                if opp_val == self:
                    setattr(old_value, "election10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "election10"):
                opp_val = getattr(value, "election10", None)
                setattr(value, "election10", self)



class Post:

    def __init__(self, PostId: int, PostElectionId: int, PostDesc: str, voter7: "Voter" = None, ballotInformation8: "BallotInformation" = None):
        self.PostId = PostId
        self.PostElectionId = PostElectionId
        self.PostDesc = PostDesc
        self.voter7 = voter7
        self.ballotInformation8 = ballotInformation8
        
        pass
    @property
    def PostElectionId(self):
        return self.__PostElectionId
    @PostElectionId.setter
    def PostElectionId(self, PostElectionId: int):
        self.__PostElectionId = PostElectionId

    @property
    def PostDesc(self):
        return self.__PostDesc
    @PostDesc.setter
    def PostDesc(self, PostDesc: str):
        self.__PostDesc = PostDesc

    @property
    def PostId(self):
        return self.__PostId
    @PostId.setter
    def PostId(self, PostId: int):
        self.__PostId = PostId

    @property
    def ballotInformation8(self):
        return self.__ballotInformation8
    @ballotInformation8.setter
    def ballotInformation8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Post__ballotInformation8", None)
        self.__ballotInformation8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "post9"):
                opp_val = getattr(old_value, "post9", None)
                if opp_val == self:
                    setattr(old_value, "post9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "post9"):
                opp_val = getattr(value, "post9", None)
                setattr(value, "post9", self)

    @property
    def voter7(self):
        return self.__voter7
    @voter7.setter
    def voter7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Post__voter7", None)
        self.__voter7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "post6"):
                opp_val = getattr(old_value, "post6", None)
                if opp_val == self:
                    setattr(old_value, "post6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "post6"):
                opp_val = getattr(value, "post6", None)
                setattr(value, "post6", self)



class BallotInformation:

    def __init__(self, BallotID: int, BallotElectionID: int, BallotVotersID: int, BallotPropID: int, BallotPropBallotID: int, BallotPropResults: int, candidate1: "Candidate" = None, election3: "Election" = None, post9: "Post" = None, admin19: "Admin" = None):
        self.BallotID = BallotID
        self.BallotElectionID = BallotElectionID
        self.BallotVotersID = BallotVotersID
        self.BallotPropID = BallotPropID
        self.BallotPropBallotID = BallotPropBallotID
        self.BallotPropResults = BallotPropResults
        self.candidate1 = candidate1
        self.election3 = election3
        self.post9 = post9
        self.admin19 = admin19
        
        pass
    @property
    def BallotPropID(self):
        return self.__BallotPropID
    @BallotPropID.setter
    def BallotPropID(self, BallotPropID: int):
        self.__BallotPropID = BallotPropID

    @property
    def BallotID(self):
        return self.__BallotID
    @BallotID.setter
    def BallotID(self, BallotID: int):
        self.__BallotID = BallotID

    @property
    def BallotPropResults(self):
        return self.__BallotPropResults
    @BallotPropResults.setter
    def BallotPropResults(self, BallotPropResults: int):
        self.__BallotPropResults = BallotPropResults

    @property
    def BallotPropBallotID(self):
        return self.__BallotPropBallotID
    @BallotPropBallotID.setter
    def BallotPropBallotID(self, BallotPropBallotID: int):
        self.__BallotPropBallotID = BallotPropBallotID

    @property
    def BallotVotersID(self):
        return self.__BallotVotersID
    @BallotVotersID.setter
    def BallotVotersID(self, BallotVotersID: int):
        self.__BallotVotersID = BallotVotersID

    @property
    def BallotElectionID(self):
        return self.__BallotElectionID
    @BallotElectionID.setter
    def BallotElectionID(self, BallotElectionID: int):
        self.__BallotElectionID = BallotElectionID

    @property
    def post9(self):
        return self.__post9
    @post9.setter
    def post9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BallotInformation__post9", None)
        self.__post9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ballotInformation8"):
                opp_val = getattr(old_value, "ballotInformation8", None)
                if opp_val == self:
                    setattr(old_value, "ballotInformation8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ballotInformation8"):
                opp_val = getattr(value, "ballotInformation8", None)
                setattr(value, "ballotInformation8", self)

    @property
    def election3(self):
        return self.__election3
    @election3.setter
    def election3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BallotInformation__election3", None)
        self.__election3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ballotInformation2"):
                opp_val = getattr(old_value, "ballotInformation2", None)
                if opp_val == self:
                    setattr(old_value, "ballotInformation2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ballotInformation2"):
                opp_val = getattr(value, "ballotInformation2", None)
                setattr(value, "ballotInformation2", self)

    @property
    def admin19(self):
        return self.__admin19
    @admin19.setter
    def admin19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BallotInformation__admin19", None)
        self.__admin19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ballotInformation18"):
                opp_val = getattr(old_value, "ballotInformation18", None)
                if opp_val == self:
                    setattr(old_value, "ballotInformation18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ballotInformation18"):
                opp_val = getattr(value, "ballotInformation18", None)
                setattr(value, "ballotInformation18", self)

    @property
    def candidate1(self):
        return self.__candidate1
    @candidate1.setter
    def candidate1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BallotInformation__candidate1", None)
        self.__candidate1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ballotInformation0"):
                opp_val = getattr(old_value, "ballotInformation0", None)
                if opp_val == self:
                    setattr(old_value, "ballotInformation0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ballotInformation0"):
                opp_val = getattr(value, "ballotInformation0", None)
                setattr(value, "ballotInformation0", self)



class Voter:

    def __init__(self, student_faculty_ID: int, Name: str, Address: str, Age: int, Eligibilty: bool, election4: "Election" = None, post6: "Post" = None, admin12: "Admin" = None):
        self.student_faculty_ID = student_faculty_ID
        self.Name = Name
        self.Address = Address
        self.Age = Age
        self.Eligibilty = Eligibilty
        self.election4 = election4
        self.post6 = post6
        self.admin12 = admin12
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Age(self):
        return self.__Age
    @Age.setter
    def Age(self, Age: int):
        self.__Age = Age

    @property
    def Eligibilty(self):
        return self.__Eligibilty
    @Eligibilty.setter
    def Eligibilty(self, Eligibilty: bool):
        self.__Eligibilty = Eligibilty

    @property
    def student_faculty_ID(self):
        return self.__student_faculty_ID
    @student_faculty_ID.setter
    def student_faculty_ID(self, student_faculty_ID: int):
        self.__student_faculty_ID = student_faculty_ID

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def admin12(self):
        return self.__admin12
    @admin12.setter
    def admin12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Voter__admin12", None)
        self.__admin12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "voter13"):
                opp_val = getattr(old_value, "voter13", None)
                if opp_val == self:
                    setattr(old_value, "voter13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "voter13"):
                opp_val = getattr(value, "voter13", None)
                setattr(value, "voter13", self)

    @property
    def election4(self):
        return self.__election4
    @election4.setter
    def election4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Voter__election4", None)
        self.__election4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "voter5"):
                opp_val = getattr(old_value, "voter5", None)
                if opp_val == self:
                    setattr(old_value, "voter5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "voter5"):
                opp_val = getattr(value, "voter5", None)
                setattr(value, "voter5", self)

    @property
    def post6(self):
        return self.__post6
    @post6.setter
    def post6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Voter__post6", None)
        self.__post6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "voter7"):
                opp_val = getattr(old_value, "voter7", None)
                if opp_val == self:
                    setattr(old_value, "voter7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "voter7"):
                opp_val = getattr(value, "voter7", None)
                setattr(value, "voter7", self)



class Candidate:

    def __init__(self, candidate_ID: int, Candidate_PostID: int, Candidate_Name: str, CandidatePartyName: str, ballotInformation0: "BallotInformation" = None, election10: "Election" = None, admin15: "Admin" = None):
        self.candidate_ID = candidate_ID
        self.Candidate_PostID = Candidate_PostID
        self.Candidate_Name = Candidate_Name
        self.CandidatePartyName = CandidatePartyName
        self.ballotInformation0 = ballotInformation0
        self.election10 = election10
        self.admin15 = admin15
        
        pass
    @property
    def CandidatePartyName(self):
        return self.__CandidatePartyName
    @CandidatePartyName.setter
    def CandidatePartyName(self, CandidatePartyName: str):
        self.__CandidatePartyName = CandidatePartyName

    @property
    def candidate_ID(self):
        return self.__candidate_ID
    @candidate_ID.setter
    def candidate_ID(self, candidate_ID: int):
        self.__candidate_ID = candidate_ID

    @property
    def Candidate_Name(self):
        return self.__Candidate_Name
    @Candidate_Name.setter
    def Candidate_Name(self, Candidate_Name: str):
        self.__Candidate_Name = Candidate_Name

    @property
    def Candidate_PostID(self):
        return self.__Candidate_PostID
    @Candidate_PostID.setter
    def Candidate_PostID(self, Candidate_PostID: int):
        self.__Candidate_PostID = Candidate_PostID

    @property
    def admin15(self):
        return self.__admin15
    @admin15.setter
    def admin15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Candidate__admin15", None)
        self.__admin15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "candidate14"):
                opp_val = getattr(old_value, "candidate14", None)
                if opp_val == self:
                    setattr(old_value, "candidate14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "candidate14"):
                opp_val = getattr(value, "candidate14", None)
                setattr(value, "candidate14", self)

    @property
    def ballotInformation0(self):
        return self.__ballotInformation0
    @ballotInformation0.setter
    def ballotInformation0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Candidate__ballotInformation0", None)
        self.__ballotInformation0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "candidate1"):
                opp_val = getattr(old_value, "candidate1", None)
                if opp_val == self:
                    setattr(old_value, "candidate1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "candidate1"):
                opp_val = getattr(value, "candidate1", None)
                setattr(value, "candidate1", self)

    @property
    def election10(self):
        return self.__election10
    @election10.setter
    def election10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Candidate__election10", None)
        self.__election10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "candidate11"):
                opp_val = getattr(old_value, "candidate11", None)
                if opp_val == self:
                    setattr(old_value, "candidate11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "candidate11"):
                opp_val = getattr(value, "candidate11", None)
                setattr(value, "candidate11", self)

