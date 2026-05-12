





import java.util.List;
import java.util.ArrayList;

public class Post  {

    private String privacy;
    private String info;





    private User user;


    public Post(
        String privacy,        String info    ) {
        this.privacy = privacy;
        this.info = info;
    }


    public String getPrivacy() {
        return privacy;
    }

    public void setPrivacy(String privacy) {
        this.privacy = privacy;
    }
    public String getInfo() {
        return info;
    }

    public void setInfo(String info) {
        this.info = info;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}