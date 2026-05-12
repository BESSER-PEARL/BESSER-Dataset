





import java.util.List;
import java.util.ArrayList;

public class Provider  {

    private None email;
    private None providerId;
    private String uid;
    private None photoURL;
    private None displayName;



    public Provider(
        None email,        None providerId,        String uid,        None photoURL,        None displayName    ) {
        this.email = email;
        this.providerId = providerId;
        this.uid = uid;
        this.photoURL = photoURL;
        this.displayName = displayName;
    }


    public None getEmail() {
        return email;
    }

    public void setEmail(None email) {
        this.email = email;
    }
    public None getProviderid() {
        return providerId;
    }

    public void setProviderid(None providerId) {
        this.providerId = providerId;
    }
    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }
    public None getPhotourl() {
        return photoURL;
    }

    public void setPhotourl(None photoURL) {
        this.photoURL = photoURL;
    }
    public None getDisplayname() {
        return displayName;
    }

    public void setDisplayname(None displayName) {
        this.displayName = displayName;
    }


}