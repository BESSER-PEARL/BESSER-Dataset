





import java.util.List;
import java.util.ArrayList;

public class User_Admin_Module  {

    private None View_User;
    private None Delete_User;
    private None Generate_User;





    private List<System_User> system_users;


    public User_Admin_Module(
        None View_User,        None Delete_User,        None Generate_User    ) {
        this.View_User = View_User;
        this.Delete_User = Delete_User;
        this.Generate_User = Generate_User;
        this.system_users = new ArrayList<>();
    }

    public User_Admin_Module(
        None View_User,        None Delete_User,        None Generate_User        ArrayList<System_User> system_users    ) {
        this.View_User = View_User;
        this.Delete_User = Delete_User;
        this.Generate_User = Generate_User;
        this.system_users = system_users;
    }

    public None getView_user() {
        return View_User;
    }

    public void setView_user(None View_User) {
        this.View_User = View_User;
    }
    public None getDelete_user() {
        return Delete_User;
    }

    public void setDelete_user(None Delete_User) {
        this.Delete_User = Delete_User;
    }
    public None getGenerate_user() {
        return Generate_User;
    }

    public void setGenerate_user(None Generate_User) {
        this.Generate_User = Generate_User;
    }

    public List<System_User> getSystem_users() {
        return system_users;
    }

    public void addSystem_user(System_user system_user) {
        this.system_users.add(system_user);
    }

}