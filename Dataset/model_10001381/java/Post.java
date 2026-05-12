





import java.util.List;
import java.util.ArrayList;

public class Post  {

    private None owner;
    private int nShares;
    private int nLikes;
    private boolean privateMode;
    private int nComments;





    private Team team;




    private User user;


    public Post(
        None owner,        int nShares,        int nLikes,        boolean privateMode,        int nComments    ) {
        this.owner = owner;
        this.nShares = nShares;
        this.nLikes = nLikes;
        this.privateMode = privateMode;
        this.nComments = nComments;
    }


    public None getOwner() {
        return owner;
    }

    public void setOwner(None owner) {
        this.owner = owner;
    }
    public int getNshares() {
        return nShares;
    }

    public void setNshares(int nShares) {
        this.nShares = nShares;
    }
    public int getNlikes() {
        return nLikes;
    }

    public void setNlikes(int nLikes) {
        this.nLikes = nLikes;
    }
    public boolean getPrivatemode() {
        return privateMode;
    }

    public void setPrivatemode(boolean privateMode) {
        this.privateMode = privateMode;
    }
    public int getNcomments() {
        return nComments;
    }

    public void setNcomments(int nComments) {
        this.nComments = nComments;
    }

    public Team getTeam() {
        return team;
    }

    public void setTeam(Team team) {
        this.team = team;
    }
    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}