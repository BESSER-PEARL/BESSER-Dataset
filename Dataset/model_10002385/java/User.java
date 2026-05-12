





import java.util.List;
import java.util.ArrayList;

public class User  {

    private int userId;
    private String password;





    private List<Admin> admins;


    public User(
        int userId,        String password    ) {
        this.userId = userId;
        this.password = password;
        this.admins = new ArrayList<>();
    }

    public User(
        int userId,        String password        ArrayList<Admin> admins    ) {
        this.userId = userId;
        this.password = password;
        this.admins = admins;
    }

    public int getUserid() {
        return userId;
    }

    public void setUserid(int userId) {
        this.userId = userId;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public List<Admin> getAdmins() {
        return admins;
    }

    public void addAdmin(Admin admin) {
        this.admins.add(admin);
    }

}