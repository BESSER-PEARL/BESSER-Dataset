





import java.util.List;
import java.util.ArrayList;

public class Page  {

    private None admin;
    private String description;
    private String posts;
    private String name;
    private None fans;
    private int nFans;





    private Post post;




    private List<User> users;


    public Page(
        None admin,        String description,        String posts,        String name,        None fans,        int nFans    ) {
        this.admin = admin;
        this.description = description;
        this.posts = posts;
        this.name = name;
        this.fans = fans;
        this.nFans = nFans;
        this.users = new ArrayList<>();
    }

    public Page(
        None admin,        String description,        String posts,        String name,        None fans,        int nFans        ArrayList<User> users    ) {
        this.admin = admin;
        this.description = description;
        this.posts = posts;
        this.name = name;
        this.fans = fans;
        this.nFans = nFans;
        this.users = users;
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
    public String getPosts() {
        return posts;
    }

    public void setPosts(String posts) {
        this.posts = posts;
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