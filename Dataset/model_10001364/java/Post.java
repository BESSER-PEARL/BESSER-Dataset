





import java.util.List;
import java.util.ArrayList;

public class Post  {

    private int likes;
    private String info;





    private User user;


    public Post(
        int likes,        String info    ) {
        this.likes = likes;
        this.info = info;
    }


    public int getLikes() {
        return likes;
    }

    public void setLikes(int likes) {
        this.likes = likes;
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