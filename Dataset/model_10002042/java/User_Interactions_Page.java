





import java.util.List;
import java.util.ArrayList;

public class User_Interactions_Page  {

    private String description;
    private None fans;
    private String name;
    private None admin;
    private String posts;
    private int nFans;





    private List<Users_User> users_users;


    public User_Interactions_Page(
        String description,        None fans,        String name,        None admin,        String posts,        int nFans    ) {
        this.description = description;
        this.fans = fans;
        this.name = name;
        this.admin = admin;
        this.posts = posts;
        this.nFans = nFans;
        this.users_users = new ArrayList<>();
    }

    public User_Interactions_Page(
        String description,        None fans,        String name,        None admin,        String posts,        int nFans        ArrayList<Users_User> users_users    ) {
        this.description = description;
        this.fans = fans;
        this.name = name;
        this.admin = admin;
        this.posts = posts;
        this.nFans = nFans;
        this.users_users = users_users;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public None getFans() {
        return fans;
    }

    public void setFans(None fans) {
        this.fans = fans;
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
    public String getPosts() {
        return posts;
    }

    public void setPosts(String posts) {
        this.posts = posts;
    }
    public int getNfans() {
        return nFans;
    }

    public void setNfans(int nFans) {
        this.nFans = nFans;
    }

    public List<Users_User> getUsers_users() {
        return users_users;
    }

    public void addUsers_user(Users_user users_user) {
        this.users_users.add(users_user);
    }

}