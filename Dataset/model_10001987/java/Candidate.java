





import java.util.List;
import java.util.ArrayList;

public class Candidate  {

    private int Candidate_PostID;
    private String Candidate_Name;
    private int candidate_ID;
    private String CandidatePartyName;



    public Candidate(
        int Candidate_PostID,        String Candidate_Name,        int candidate_ID,        String CandidatePartyName    ) {
        this.Candidate_PostID = Candidate_PostID;
        this.Candidate_Name = Candidate_Name;
        this.candidate_ID = candidate_ID;
        this.CandidatePartyName = CandidatePartyName;
    }


    public int getCandidate_postid() {
        return Candidate_PostID;
    }

    public void setCandidate_postid(int Candidate_PostID) {
        this.Candidate_PostID = Candidate_PostID;
    }
    public String getCandidate_name() {
        return Candidate_Name;
    }

    public void setCandidate_name(String Candidate_Name) {
        this.Candidate_Name = Candidate_Name;
    }
    public int getCandidate_id() {
        return candidate_ID;
    }

    public void setCandidate_id(int candidate_ID) {
        this.candidate_ID = candidate_ID;
    }
    public String getCandidatepartyname() {
        return CandidatePartyName;
    }

    public void setCandidatepartyname(String CandidatePartyName) {
        this.CandidatePartyName = CandidatePartyName;
    }


}