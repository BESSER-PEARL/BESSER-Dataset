





import java.util.List;
import java.util.ArrayList;

public class Provider  {

    private None email;
    private None displayName;
    private None providerId;
    private String uid;
    private None photoURL;



    public Provider(
        None email,        None displayName,        None providerId,        String uid,        None photoURL    ) {
        this.email = email;
        this.displayName = displayName;
        this.providerId = providerId;
        this.uid = uid;
        this.photoURL = photoURL;
    }


    public None getEmail() {
        return email;
    }

    public void setEmail(None email) {
        this.email = email;
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


}