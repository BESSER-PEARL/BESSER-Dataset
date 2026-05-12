





import java.util.List;
import java.util.ArrayList;

public class Group  {

    private String posts;
    private int nMembers;
    private None admins;
    private None members;
    private String name;
    private String description;





    private List<User> users;


    public Group(
        String posts,        int nMembers,        None admins,        None members,        String name,        String description    ) {
        this.posts = posts;
        this.nMembers = nMembers;
        this.admins = admins;
        this.members = members;
        this.name = name;
        this.description = description;
        this.users = new ArrayList<>();
    }

    public Group(
        String posts,        int nMembers,        None admins,        None members,        String name,        String description        ArrayList<User> users    ) {
        this.posts = posts;
        this.nMembers = nMembers;
        this.admins = admins;
        this.members = members;
        this.name = name;
        this.description = description;
        this.users = users;
    }

    public String getPosts() {
        return posts;
    }

    public void setPosts(String posts) {
        this.posts = posts;
    }
    public int getNmembers() {
        return nMembers;
    }

    public void setNmembers(int nMembers) {
        this.nMembers = nMembers;
    }
    public None getAdmins() {
        return admins;
    }

    public void setAdmins(None admins) {
        this.admins = admins;
    }
    public None getMembers() {
        return members;
    }

    public void setMembers(None members) {
        this.members = members;
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

    public List<User> getUsers() {
        return users;
    }

    public void addUser(User user) {
        this.users.add(user);
    }

}