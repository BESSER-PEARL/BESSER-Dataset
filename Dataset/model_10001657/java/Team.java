





import java.util.List;
import java.util.ArrayList;

public class Team  {

    private int nMembers;
    private String name;
    private None admins;
    private String description;
    private String posts;
    private None members;





    private List<User> users;


    public Team(
        int nMembers,        String name,        None admins,        String description,        String posts,        None members    ) {
        this.nMembers = nMembers;
        this.name = name;
        this.admins = admins;
        this.description = description;
        this.posts = posts;
        this.members = members;
        this.users = new ArrayList<>();
    }

    public Team(
        int nMembers,        String name,        None admins,        String description,        String posts,        None members        ArrayList<User> users    ) {
        this.nMembers = nMembers;
        this.name = name;
        this.admins = admins;
        this.description = description;
        this.posts = posts;
        this.members = members;
        this.users = users;
    }

    public int getNmembers() {
        return nMembers;
    }

    public void setNmembers(int nMembers) {
        this.nMembers = nMembers;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public None getAdmins() {
        return admins;
    }

    public void setAdmins(None admins) {
        this.admins = admins;
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
    public None getMembers() {
        return members;
    }

    public void setMembers(None members) {
        this.members = members;
    }

    public List<User> getUsers() {
        return users;
    }

    public void addUser(User user) {
        this.users.add(user);
    }

}