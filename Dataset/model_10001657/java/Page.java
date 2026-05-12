





import java.util.List;
import java.util.ArrayList;

public class Page  {

    private String posts;
    private String description;
    private int nFans;
    private String name;
    private None admin;
    private None fans;





    private List<User> users;




    private Post post;


    public Page(
        String posts,        String description,        int nFans,        String name,        None admin,        None fans    ) {
        this.posts = posts;
        this.description = description;
        this.nFans = nFans;
        this.name = name;
        this.admin = admin;
        this.fans = fans;
        this.users = new ArrayList<>();
    }

    public Page(
        String posts,        String description,        int nFans,        String name,        None admin,        None fans        ArrayList<User> users    ) {
        this.posts = posts;
        this.description = description;
        this.nFans = nFans;
        this.name = name;
        this.admin = admin;
        this.fans = fans;
        this.users = users;
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
    public int getNfans() {
        return nFans;
    }

    public void setNfans(int nFans) {
        this.nFans = nFans;
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
    public None getFans() {
        return fans;
    }

    public void setFans(None fans) {
        this.fans = fans;
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