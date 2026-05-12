





import java.util.List;
import java.util.ArrayList;

public class Interest  {

    private String discription;
    private String name;





    private User user;




    private List<Post> posts;


    public Interest(
        String discription,        String name    ) {
        this.discription = discription;
        this.name = name;
        this.posts = new ArrayList<>();
    }

    public Interest(
        String discription,        String name        ArrayList<Post> posts    ) {
        this.discription = discription;
        this.name = name;
        this.posts = posts;
    }

    public String getDiscription() {
        return discription;
    }

    public void setDiscription(String discription) {
        this.discription = discription;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }
    public List<Post> getPosts() {
        return posts;
    }

    public void addPost(Post post) {
        this.posts.add(post);
    }

}