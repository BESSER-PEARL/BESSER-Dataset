





import java.util.List;
import java.util.ArrayList;

public class user_Provider  {

    private String displayName;
    private String email;
    private String photoURL;
    private String providerId;
    private String uid;



    public user_Provider(
        String displayName,        String email,        String photoURL,        String providerId,        String uid    ) {
        this.displayName = displayName;
        this.email = email;
        this.photoURL = photoURL;
        this.providerId = providerId;
        this.uid = uid;
    }


    public String getDisplayname() {
        return displayName;
    }

    public void setDisplayname(String displayName) {
        this.displayName = displayName;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getPhotourl() {
        return photoURL;
    }

    public void setPhotourl(String photoURL) {
        this.photoURL = photoURL;
    }
    public String getProviderid() {
        return providerId;
    }

    public void setProviderid(String providerId) {
        this.providerId = providerId;
    }
    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }


}