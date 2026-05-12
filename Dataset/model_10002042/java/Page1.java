





import java.util.List;
import java.util.ArrayList;

public class Page1  {

    private None fans;
    private None admin;
    private String name;
    private String description;
    private int nFans;
    private String posts;





    private System_Controller system_controller;


    public Page1(
        None fans,        None admin,        String name,        String description,        int nFans,        String posts    ) {
        this.fans = fans;
        this.admin = admin;
        this.name = name;
        this.description = description;
        this.nFans = nFans;
        this.posts = posts;
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

    public System_Controller getSystem_controller() {
        return system_controller;
    }

    public void setSystem_controller(System_Controller system_controller) {
        this.system_controller = system_controller;
    }

}