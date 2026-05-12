





import java.util.List;
import java.util.ArrayList;

public class Election  {

    private int ElectionID;
    private String ElectionDate;
    private String ElectionName;
    private String ElectionCriteria;





    private BallotInformation ballotinformation;




    private Candidate candidate;




    private Voter voter;


    public Election(
        int ElectionID,        String ElectionDate,        String ElectionName,        String ElectionCriteria    ) {
        this.ElectionID = ElectionID;
        this.ElectionDate = ElectionDate;
        this.ElectionName = ElectionName;
        this.ElectionCriteria = ElectionCriteria;
    }


    public int getElectionid() {
        return ElectionID;
    }

    public void setElectionid(int ElectionID) {
        this.ElectionID = ElectionID;
    }
    public String getElectiondate() {
        return ElectionDate;
    }

    public void setElectiondate(String ElectionDate) {
        this.ElectionDate = ElectionDate;
    }
    public String getElectionname() {
        return ElectionName;
    }

    public void setElectionname(String ElectionName) {
        this.ElectionName = ElectionName;
    }
    public String getElectioncriteria() {
        return ElectionCriteria;
    }

    public void setElectioncriteria(String ElectionCriteria) {
        this.ElectionCriteria = ElectionCriteria;
    }

    public BallotInformation getBallotinformation() {
        return ballotinformation;
    }

    public void setBallotinformation(BallotInformation ballotinformation) {
        this.ballotinformation = ballotinformation;
    }
    public Candidate getCandidate() {
        return candidate;
    }

    public void setCandidate(Candidate candidate) {
        this.candidate = candidate;
    }
    public Voter getVoter() {
        return voter;
    }

    public void setVoter(Voter voter) {
        this.voter = voter;
    }

}