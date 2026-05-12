





import java.util.List;
import java.util.ArrayList;

public class Post  {

    private String info;
    private String privacy;





    private User user;


    public Post(
        String info,        String privacy    ) {
        this.info = info;
        this.privacy = privacy;
    }


    public String getInfo() {
        return info;
    }

    public void setInfo(String info) {
        this.info = info;
    }
    public String getPrivacy() {
        return privacy;
    }

    public void setPrivacy(String privacy) {
        this.privacy = privacy;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}