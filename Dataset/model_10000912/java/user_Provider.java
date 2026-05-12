





import java.util.List;
import java.util.ArrayList;

public class user_Provider  {

    private String displayName;
    private String email;
    private String providerId;
    private String uid;
    private String photoURL;



    public user_Provider(
        String displayName,        String email,        String providerId,        String uid,        String photoURL    ) {
        this.displayName = displayName;
        this.email = email;
        this.providerId = providerId;
        this.uid = uid;
        this.photoURL = photoURL;
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
    public String getPhotourl() {
        return photoURL;
    }

    public void setPhotourl(String photoURL) {
        this.photoURL = photoURL;
    }


}