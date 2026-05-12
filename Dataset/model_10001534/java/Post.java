





import java.util.List;
import java.util.ArrayList;

public class Post  {

    private int nShares;
    private int nComments;
    private None owner;
    private int nLikes;
    private boolean privateMode;





    private User user;




    private Group group;


    public Post(
        int nShares,        int nComments,        None owner,        int nLikes,        boolean privateMode    ) {
        this.nShares = nShares;
        this.nComments = nComments;
        this.owner = owner;
        this.nLikes = nLikes;
        this.privateMode = privateMode;
    }


    public int getNshares() {
        return nShares;
    }

    public void setNshares(int nShares) {
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