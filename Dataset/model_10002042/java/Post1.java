





import java.util.List;
import java.util.ArrayList;

public class Post1  {

    private None owner;
    private String LikeContainer_int_;
    private int nShares;
    private boolean privateMode;
    private String CommentContainer;
    private int nLikes;
    private int nComments;





    private System_Controller system_controller;


    public Post1(
        None owner,        String LikeContainer_int_,        int nShares,        boolean privateMode,        String CommentContainer,        int nLikes,        int nComments    ) {
        this.owner = owner;
        this.LikeContainer_int_ = LikeContainer_int_;
        this.nShares = nShares;
        this.privateMode = privateMode;
        this.CommentContainer = CommentContainer;
        this.nLikes = nLikes;
        this.nComments = nComments;
    }


    public None getOwner() {
        return owner;
    }

    public void setOwner(None owner) {
        this.owner = owner;
    }
    public String getLikecontainer_int_() {
        return LikeContainer_int_;
    }

    public void setLikecontainer_int_(String LikeContainer_int_) {
        this.LikeContainer_int_ = LikeContainer_int_;
    }
    public int getNshares() {
        return nShares;
    }

    public void setNshares(int nShares) {
        this.nShares = nShares;
    }
    public boolean getPrivatemode() {
        return privateMode;
    }

    public void setPrivatemode(boolean privateMode) {
        this.privateMode = privateMode;
    }
    public String getCommentcontainer() {
        return CommentContainer;
    }

    public void setCommentcontainer(String CommentContainer) {
        this.CommentContainer = CommentContainer;
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

    public System_Controller getSystem_controller() {
        return system_controller;
    }

    public void setSystem_controller(System_Controller system_controller) {
        this.system_controller = system_controller;
    }

}