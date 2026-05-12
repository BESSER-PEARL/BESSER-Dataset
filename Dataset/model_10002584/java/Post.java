





import java.util.List;
import java.util.ArrayList;

public class Post  {

    private String PostContent;





    private User user;


    public Post(
        String PostContent    ) {
        this.PostContent = PostContent;
    }


    public String getPostcontent() {
        return PostContent;
    }

    public void setPostcontent(String PostContent) {
        this.PostContent = PostContent;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}