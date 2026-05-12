





import java.util.List;
import java.util.ArrayList;

public class user_Provider  {

    private String email;
    private String uid;
    private String displayName;
    private String providerId;
    private String photoURL;





    private List<user_User> user_users;


    public user_Provider(
        String email,        String uid,        String displayName,        String providerId,        String photoURL    ) {
        this.email = email;
        this.uid = uid;
        this.displayName = displayName;
        this.providerId = providerId;
        this.photoURL = photoURL;
        this.user_users = new ArrayList<>();
    }

    public user_Provider(
        String email,        String uid,        String displayName,        String providerId,        String photoURL        ArrayList<user_User> user_users    ) {
        this.email = email;
        this.uid = uid;
        this.displayName = displayName;
        this.providerId = providerId;
        this.photoURL = photoURL;
        this.user_users = user_users;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }
    public String getDisplayname() {
        return displayName;
    }

    public void setDisplayname(String displayName) {
        this.displayName = displayName;
    }
    public String getProviderid() {
        return providerId;
    }

    public void setProviderid(String providerId) {
        this.providerId = providerId;
    }
    public String getPhotourl() {
        return photoURL;
    }

    public void setPhotourl(String photoURL) {
        this.photoURL = photoURL;
    }

    public List<user_User> getUser_users() {
        return user_users;
    }

    public void addUser_user(User_user user_user) {
        this.user_users.add(user_user);
    }

}