





import java.util.List;
import java.util.ArrayList;

public class Hashtag  {

    private int id;
    private String tag;





    private List<Post> posts;


    public Hashtag(
        int id,        String tag    ) {
        this.id = id;
        this.tag = tag;
        this.posts = new ArrayList<>();
    }

    public Hashtag(
        int id,        String tag        ArrayList<Post> posts    ) {
        this.id = id;
        this.tag = tag;
        this.posts = posts;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getTag() {
        return tag;
    }

    public void setTag(String tag) {
        this.tag = tag;
    }

    public List<Post> getPosts() {
        return posts;
    }

    public void addPost(Post post) {
        this.posts.add(post);
    }

}