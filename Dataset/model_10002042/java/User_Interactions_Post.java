





import java.util.List;
import java.util.ArrayList;

public class User_Interactions_Post  {

    private None owner;
    private int nComments;
    private int nLikes;
    private int nShares;
    private boolean privateMode;





    private User_Interactions_Group user_interactions_group;




    private User_Interactions_Page user_interactions_page;




    private Users_User users_user;


    public User_Interactions_Post(
        None owner,        int nComments,        int nLikes,        int nShares,        boolean privateMode    ) {
        this.owner = owner;
        this.nComments = nComments;
        this.nLikes = nLikes;
        this.nShares = nShares;
        this.privateMode = privateMode;
    }


    public None getOwner() {
        return owner;
    }

    public void setOwner(None owner) {
        this.owner = owner;
    }
    public int getNcomments() {
        return nComments;
    }

    public void setNcomments(int nComments) {
        this.nComments = nComments;
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
    public boolean getPrivatemode() {
        return privateMode;
    }

    public void setPrivatemode(boolean privateMode) {
        this.privateMode = privateMode;
    }

    public User_Interactions_Group getUser_interactions_group() {
        return user_interactions_group;
    }

    public void setUser_interactions_group(User_Interactions_Group user_interactions_group) {
        this.user_interactions_group = user_interactions_group;
    }
    public User_Interactions_Page getUser_interactions_page() {
        return user_interactions_page;
    }

    public void setUser_interactions_page(User_Interactions_Page user_interactions_page) {
        this.user_interactions_page = user_interactions_page;
    }
    public Users_User getUsers_user() {
        return users_user;
    }

    public void setUsers_user(Users_User users_user) {
        this.users_user = users_user;
    }

}