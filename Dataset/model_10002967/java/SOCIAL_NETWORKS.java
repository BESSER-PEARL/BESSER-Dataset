





import java.util.List;
import java.util.ArrayList;

public class SOCIAL_NETWORKS  {

    private String _id;
    private String instagram;
    private String twitter;
    private String facebook;
    private String updateAt;





    private USER user;


    public SOCIAL_NETWORKS(
        String _id,        String instagram,        String twitter,        String facebook,        String updateAt    ) {
        this._id = _id;
        this.instagram = instagram;
        this.twitter = twitter;
        this.facebook = facebook;
        this.updateAt = updateAt;
    }


    public String get_id() {
        return _id;
    }

    public void set_id(String _id) {
        this._id = _id;
    }
    public String getInstagram() {
        return instagram;
    }

    public void setInstagram(String instagram) {
        this.instagram = instagram;
    }
    public String getTwitter() {
        return twitter;
    }

    public void setTwitter(String twitter) {
        this.twitter = twitter;
    }
    public String getFacebook() {
        return facebook;
    }

    public void setFacebook(String facebook) {
        this.facebook = facebook;
    }
    public String getUpdateat() {
        return updateAt;
    }

    public void setUpdateat(String updateAt) {
        this.updateAt = updateAt;
    }

    public USER getUser() {
        return user;
    }

    public void setUser(USER user) {
        this.user = user;
    }

}