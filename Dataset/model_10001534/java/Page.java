





import java.util.List;
import java.util.ArrayList;

public class Page  {

    private String name;
    private None fans;
    private String posts;
    private None admin;
    private String description;
    private int nFans;





    private List<User> users;




    private Post post;


    public Page(
        String name,        None fans,        String posts,        None admin,        String description,        int nFans    ) {
        this.name = name;
        this.fans = fans;
        this.posts = posts;
        this.admin = admin;
        this.description = description;
        this.nFans = nFans;
        this.users = new ArrayList<>();
    }

    public Page(
        String name,        None fans,        String posts,        None admin,        String description,        int nFans        ArrayList<User> users    ) {
        this.name = name;
        this.fans = fans;
        this.posts = posts;
        this.admin = admin;
        this.description = description;
        this.nFans = nFans;
        this.users = users;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public None getFans() {
        return fans;
    }

    public void setFans(None fans) {
        this.fans = fans;
    }
    public String getPosts() {
        return posts;
    }

    public void setPosts(String posts) {
        this.posts = posts;
    }
    public None getAdmin() {
        return admin;
    }

    public void setAdmin(None admin) {
        this.admin = admin;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public int getNfans() {
        return nFans;
    }

    public void setNfans(int nFans) {
        this.nFans = nFans;
    }

    public List<User> getUsers() {
        return users;
    }

    public void addUser(User user) {
        this.users.add(user);
    }
    public Post getPost() {
        return post;
    }

    public void setPost(Post post) {
        this.post = post;
    }

}