





import java.util.List;
import java.util.ArrayList;

public class Provider  {

    private None displayName;
    private None providerId;
    private None email;
    private None photoURL;
    private String uid;



    public Provider(
        None displayName,        None providerId,        None email,        None photoURL,        String uid    ) {
        this.displayName = displayName;
        this.providerId = providerId;
        this.email = email;
        this.photoURL = photoURL;
        this.uid = uid;
    }


    public None getDisplayname() {
        return displayName;
    }

    public void setDisplayname(None displayName) {
        this.displayName = displayName;
    }
    public None getProviderid() {
        return providerId;
    }

    public void setProviderid(None providerId) {
        this.providerId = providerId;
    }
    public None getEmail() {
        return email;
    }

    public void setEmail(None email) {
        this.email = email;
    }
    public None getPhotourl() {
        return photoURL;
    }

    public void setPhotourl(None photoURL) {
        this.photoURL = photoURL;
    }
    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }


}