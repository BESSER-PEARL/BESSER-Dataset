





import java.util.List;
import java.util.ArrayList;

public class Page  {

    private None fans;
    private None admin;
    private String name;
    private String description;
    private int nFans;
    private String posts;





    private Post post;




    private List<User> users;


    public Page(
        None fans,        None admin,        String name,        String description,        int nFans,        String posts    ) {
        this.fans = fans;
        this.admin = admin;
        this.name = name;
        this.description = description;
        this.nFans = nFans;
        this.posts = posts;
        this.users = new ArrayList<>();
    }

    public Page(
        None fans,        None admin,        String name,        String description,        int nFans,        String posts        ArrayList<User> users    ) {
        this.fans = fans;
        this.admin = admin;
        this.name = name;
        this.description = description;
        this.nFans = nFans;
        this.posts = posts;
        this.users = users;
    }

    public None getFans() {
        return fans;
    }

    public void setFans(None fans) {
        this.fans = fans;
    }
    public None getAdmin() {
        return admin;
    }

    public void setAdmin(None admin) {
        this.admin = admin;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public String getPosts() {
        return posts;
    }

    public void setPosts(String posts) {
        this.posts = posts;
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