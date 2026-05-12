





import java.util.List;
import java.util.ArrayList;

public class User_Interactions_Group  {

    private String name;
    private None members;
    private String description;
    private None admins;
    private String posts;
    private int nMembers;





    private List<Users_User> users_users;


    public User_Interactions_Group(
        String name,        None members,        String description,        None admins,        String posts,        int nMembers    ) {
        this.name = name;
        this.members = members;
        this.description = description;
        this.admins = admins;
        this.posts = posts;
        this.nMembers = nMembers;
        this.users_users = new ArrayList<>();
    }

    public User_Interactions_Group(
        String name,        None members,        String description,        None admins,        String posts,        int nMembers        ArrayList<Users_User> users_users    ) {
        this.name = name;
        this.members = members;
        this.description = description;
        this.admins = admins;
        this.posts = posts;
        this.nMembers = nMembers;
        this.users_users = users_users;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public None getMembers() {
        return members;
    }

    public void setMembers(None members) {
        this.members = members;
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

    public List<Users_User> getUsers_users() {
        return users_users;
    }

    public void addUsers_user(Users_user users_user) {
        this.users_users.add(users_user);
    }

}