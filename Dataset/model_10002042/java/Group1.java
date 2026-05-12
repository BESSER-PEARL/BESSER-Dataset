





import java.util.List;
import java.util.ArrayList;

public class Group1  {

    private String name;
    private int nMembers;
    private None members;
    private None admins;
    private String description;
    private String posts;





    private System_Controller system_controller;


    public Group1(
        String name,        int nMembers,        None members,        None admins,        String description,        String posts    ) {
        this.name = name;
        this.nMembers = nMembers;
        this.members = members;
        this.admins = admins;
        this.description = description;
        this.posts = posts;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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

    public System_Controller getSystem_controller() {
        return system_controller;
    }

    public void setSystem_controller(System_Controller system_controller) {
        this.system_controller = system_controller;
    }

}