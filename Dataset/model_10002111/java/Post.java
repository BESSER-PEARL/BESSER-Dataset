





import java.util.List;
import java.util.ArrayList;

public class Post  {

    private int nComments;
    private None owner;
    private boolean privateMode;
    private int nLikes;
    private int nShares;





    private User user;




    private Group group;


    public Post(
        int nComments,        None owner,        boolean privateMode,        int nLikes,        int nShares    ) {
        this.nComments = nComments;
        this.owner = owner;
        this.privateMode = privateMode;
        this.nLikes = nLikes;
        this.nShares = nShares;
    }


    public int getNcomments() {
        return nComments;
    }

    public void setNcomments(int nComments) {
        this.nComments = nComments;
    }
    public None getOwner() {
        return owner;
    }

    public void setOwner(None owner) {
        this.owner = owner;
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