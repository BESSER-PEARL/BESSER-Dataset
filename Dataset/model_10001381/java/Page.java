





import java.util.List;
import java.util.ArrayList;

public class Page  {

    private None fans;
    private String posts;
    private String description;
    private String name;
    private None admin;
    private int nFans;





    private Post post;




    private List<User> users;


    public Page(
        None fans,        String posts,        String description,        String name,        None admin,        int nFans    ) {
        this.fans = fans;
        this.posts = posts;
        this.description = description;
        this.name = name;
        this.admin = admin;
        this.nFans = nFans;
        this.users = new ArrayList<>();
    }

    public Page(
        None fans,        String posts,        String description,        String name,        None admin,        int nFans        ArrayList<User> users    ) {
        this.fans = fans;
        this.posts = posts;
        this.description = description;
        this.name = name;
        this.admin = admin;
        this.nFans = nFans;
        this.users = users;
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
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public None getAdmin() {
        return admin;
    }

    public void setAdmin(None admin) {
        this.admin = admin;
    }
    public int getNfans() {
        return nFans;
    }

    public void setNfans(int nFans) {
        this.nFans = nFans;
    }

    public Post getPost() {
        return post;
    }

    public void setPost(Post post) {
        this.post = post;
    }
    public List<User> getUsers() {
        return users;
    }

    public void addUser(User user) {
        this.users.add(user);
    }

}