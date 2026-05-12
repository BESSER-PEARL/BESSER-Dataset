





import java.util.List;
import java.util.ArrayList;

public class Admin  {

    private String AminName;
    private int AdminID;
    private int UserLogin;





    private Candidate candidate;




    private Voter voter;




    private Election election;




    private BallotInformation ballotinformation;


    public Admin(
        String AminName,        int AdminID,        int UserLogin    ) {
        this.AminName = AminName;
        this.AdminID = AdminID;
        this.UserLogin = UserLogin;
    }


    public String getAminname() {
        return AminName;
    }

    public void setAminname(String AminName) {
        this.AminName = AminName;
    }
    public int getAdminid() {
        return AdminID;
    }

    public void setAdminid(int AdminID) {
        this.AdminID = AdminID;
    }
    public int getUserlogin() {
        return UserLogin;
    }

    public void setUserlogin(int UserLogin) {
        this.UserLogin = UserLogin;
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
    public Election getElection() {
        return election;
    }

    public void setElection(Election election) {
        this.election = election;
    }
    public BallotInformation getBallotinformation() {
        return ballotinformation;
    }

    public void setBallotinformation(BallotInformation ballotinformation) {
        this.ballotinformation = ballotinformation;
    }

}