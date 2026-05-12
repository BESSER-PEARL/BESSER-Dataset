





import java.util.List;
import java.util.ArrayList;

public class BallotInformation  {

    private int BallotPropBallotID;
    private int BallotPropResults;
    private int BallotElectionID;
    private int BallotID;
    private int BallotPropID;
    private int BallotVotersID;





    private Candidate candidate;


    public BallotInformation(
        int BallotPropBallotID,        int BallotPropResults,        int BallotElectionID,        int BallotID,        int BallotPropID,        int BallotVotersID    ) {
        this.BallotPropBallotID = BallotPropBallotID;
        this.BallotPropResults = BallotPropResults;
        this.BallotElectionID = BallotElectionID;
        this.BallotID = BallotID;
        this.BallotPropID = BallotPropID;
        this.BallotVotersID = BallotVotersID;
    }


    public int getBallotpropballotid() {
        return BallotPropBallotID;
    }

    public void setBallotpropballotid(int BallotPropBallotID) {
        this.BallotPropBallotID = BallotPropBallotID;
    }
    public int getBallotpropresults() {
        return BallotPropResults;
    }

    public void setBallotpropresults(int BallotPropResults) {
        this.BallotPropResults = BallotPropResults;
    }
    public int getBallotelectionid() {
        return BallotElectionID;
    }

    public void setBallotelectionid(int BallotElectionID) {
        this.BallotElectionID = BallotElectionID;
    }
    public int getBallotid() {
        return BallotID;
    }

    public void setBallotid(int BallotID) {
        this.BallotID = BallotID;
    }
    public int getBallotpropid() {
        return BallotPropID;
    }

    public void setBallotpropid(int BallotPropID) {
        this.BallotPropID = BallotPropID;
    }
    public int getBallotvotersid() {
        return BallotVotersID;
    }

    public void setBallotvotersid(int BallotVotersID) {
        this.BallotVotersID = BallotVotersID;
    }

    public Candidate getCandidate() {
        return candidate;
    }

    public void setCandidate(Candidate candidate) {
        this.candidate = candidate;
    }

}