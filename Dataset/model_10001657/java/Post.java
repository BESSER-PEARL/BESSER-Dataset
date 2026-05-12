





import java.util.List;
import java.util.ArrayList;

public class Post  {

    private int nComments;
    private boolean privateMode;
    private int nLikes;
    private int nShares;
    private None owner;





    private Team team;




    private User user;


    public Post(
        int nComments,        boolean privateMode,        int nLikes,        int nShares,        None owner    ) {
        this.nComments = nComments;
        this.privateMode = privateMode;
        this.nLikes = nLikes;
        this.nShares = nShares;
        this.owner = owner;
    }


    public int getNcomments() {
        return nComments;
    }

    public void setNcomments(int nComments) {
        this.nComments = nComments;
    }
    public boolean getPrivatemode() {
        return privateMode;
    }

    public void setPrivatemode(boolean privateMode) {
        this.privateMode = privateMode;
    }
    public int getNlikes() {
        return nLikes;
    }

    public void setNlikes(int nLikes) {
        this.nLikes = nLikes;
    }
    public int getNshares() {
        return nShares;
    }

    public void setNshares(int nShares) {
        this.nShares = nShares;
    }
    public None getOwner() {
        return owner;
    }

    public void setOwner(None owner) {
        this.owner = owner;
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