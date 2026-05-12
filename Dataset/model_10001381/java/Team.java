





import java.util.List;
import java.util.ArrayList;

public class Team  {

    private int nMembers;
    private None members;
    private String posts;
    private String name;
    private String description;
    private None admins;





    private List<User> users;


    public Team(
        int nMembers,        None members,        String posts,        String name,        String description,        None admins    ) {
        this.nMembers = nMembers;
        this.members = members;
        this.posts = posts;
        this.name = name;
        this.description = description;
        this.admins = admins;
        this.users = new ArrayList<>();
    }

    public Team(
        int nMembers,        None members,        String posts,        String name,        String description,        None admins        ArrayList<User> users    ) {
        this.nMembers = nMembers;
        this.members = members;
        this.posts = posts;
        this.name = name;
        this.description = description;
        this.admins = admins;
        this.users = users;
    }

    public int getNmembers() {
        return nMembers;
    }

    public void setNmembers(int nMembers) {
        this.nMembers = nMembers;
    }
    public None getMembers() {
        return members;
    }

    public void setMembers(None members) {
        this.members = members;
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
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public None getAdmins() {
        return admins;
    }

    public void setAdmins(None admins) {
        this.admins = admins;
    }

    public List<User> getUsers() {
        return users;
    }

    public void addUser(User user) {
        this.users.add(user);
    }

}