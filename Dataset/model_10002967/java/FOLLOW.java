





import java.util.List;
import java.util.ArrayList;

public class FOLLOW  {

    private String followers;
    private String following;
    private String followingGroup;
    private String userId;
    private String createdAt;
    private String _id;





    private USER user;


    public FOLLOW(
        String followers,        String following,        String followingGroup,        String userId,        String createdAt,        String _id    ) {
        this.followers = followers;
        this.following = following;
        this.followingGroup = followingGroup;
        this.userId = userId;
        this.createdAt = createdAt;
        this._id = _id;
    }


    public String getFollowers() {
        return followers;
    }

    public void setFollowers(String followers) {
        this.followers = followers;
    }
    public String getFollowing() {
        return following;
    }

    public void setFollowing(String following) {
        this.following = following;
    }
    public String getFollowinggroup() {
        return followingGroup;
    }

    public void setFollowinggroup(String followingGroup) {
        this.followingGroup = followingGroup;
    }
    public String getUserid() {
        return userId;
    }

    public void setUserid(String userId) {
        this.userId = userId;
    }
    public String getCreatedat() {
        return createdAt;
    }

    public void setCreatedat(String createdAt) {
        this.createdAt = createdAt;
    }
    public String get_id() {
        return _id;
    }

    public void set_id(String _id) {
        this._id = _id;
    }

    public USER getUser() {
        return user;
    }

    public void setUser(USER user) {
        this.user = user;
    }

}