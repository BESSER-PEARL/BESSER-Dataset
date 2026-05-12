





import java.util.List;
import java.util.ArrayList;

public class Comment  {






    private Post post;




    private User user;


    public Comment(
    ) {
    }



    public Post getPost() {
        return post;
    }

    public void setPost(Post post) {
        this.post = post;
    }
    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}