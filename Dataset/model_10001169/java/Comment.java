





import java.util.List;
import java.util.ArrayList;

public class Comment  {






    private User user;




    private Post post;


    public Comment(
    ) {
    }



    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }
    public Post getPost() {
        return post;
    }

    public void setPost(Post post) {
        this.post = post;
    }

}