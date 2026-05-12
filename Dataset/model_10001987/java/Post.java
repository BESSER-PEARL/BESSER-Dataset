





import java.util.List;
import java.util.ArrayList;

public class Post  {

    private String PostDesc;
    private int PostId;
    private int PostElectionId;





    private Voter voter;




    private BallotInformation ballotinformation;


    public Post(
        String PostDesc,        int PostId,        int PostElectionId    ) {
        this.PostDesc = PostDesc;
        this.PostId = PostId;
        this.PostElectionId = PostElectionId;
    }


    public String getPostdesc() {
        return PostDesc;
    }

    public void setPostdesc(String PostDesc) {
        this.PostDesc = PostDesc;
    }
    public int getPostid() {
        return PostId;
    }

    public void setPostid(int PostId) {
        this.PostId = PostId;
    }
    public int getPostelectionid() {
        return PostElectionId;
    }

    public void setPostelectionid(int PostElectionId) {
        this.PostElectionId = PostElectionId;
    }

    public Voter getVoter() {
        return voter;
    }

    public void setVoter(Voter voter) {
        this.voter = voter;
    }
    public BallotInformation getBallotinformation() {
        return ballotinformation;
    }

    public void setBallotinformation(BallotInformation ballotinformation) {
        this.ballotinformation = ballotinformation;
    }

}