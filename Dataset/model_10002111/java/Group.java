





import java.util.List;
import java.util.ArrayList;

public class Group  {

    private String description;
    private None members;
    private int nMembers;
    private String name;
    private String posts;
    private None admins;





    private List<User> users;


    public Group(
        String description,        None members,        int nMembers,        String name,        String posts,        None admins    ) {
        this.description = description;
        this.members = members;
        this.nMembers = nMembers;
        this.name = name;
        this.posts = posts;
        this.admins = admins;
        this.users = new ArrayList<>();
    }

    public Group(
        String description,        None members,        int nMembers,        String name,        String posts,        None admins        ArrayList<User> users    ) {
        this.description = description;
        this.members = members;
        this.nMembers = nMembers;
        this.name = name;
        this.posts = posts;
        this.admins = admins;
        this.users = users;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public None getMembers() {
        return members;
    }

    public void setMembers(None members) {
        this.members = members;
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
    public String getPosts() {
        return posts;
    }

    public void setPosts(String posts) {
        this.posts = posts;
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