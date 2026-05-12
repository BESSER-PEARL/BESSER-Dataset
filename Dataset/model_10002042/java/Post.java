





import java.util.List;
import java.util.ArrayList;

public class Post  {

    private None owner;
    private int nLikes;
    private int nComments;
    private boolean privateMode;
    private int nShares;





    private User user;




    private Group group;


    public Post(
        None owner,        int nLikes,        int nComments,        boolean privateMode,        int nShares    ) {
        this.owner = owner;
        this.nLikes = nLikes;
        this.nComments = nComments;
        this.privateMode = privateMode;
        this.nShares = nShares;
    }


    public None getOwner() {
        return owner;
    }

    public void setOwner(None owner) {
        this.owner = owner;
    }
    public int getNlikes() {
        return nLikes;
    }

    public void setNlikes(int nLikes) {
        this.nLikes = nLikes;
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
    public int getNshares() {
        return nShares;
    }

    public void setNshares(int nShares) {
        this.nShares = nShares;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }
    public Group getGroup() {
        return group;
    }

    public void setGroup(Group group) {
        this.group = group;
    }

}