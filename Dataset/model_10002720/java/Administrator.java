





import java.util.List;
import java.util.ArrayList;

public class Administrator  {

    private String admin_name;
    private String password;





    private List<Users> userss;


    public Administrator(
        String admin_name,        String password    ) {
        this.admin_name = admin_name;
        this.password = password;
        this.userss = new ArrayList<>();
    }

    public Administrator(
        String admin_name,        String password        ArrayList<Users> userss    ) {
        this.admin_name = admin_name;
        this.password = password;
        this.userss = userss;
    }

    public String getAdmin_name() {
        return admin_name;
    }

    public void setAdmin_name(String admin_name) {
        this.admin_name = admin_name;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public List<Users> getUserss() {
        return userss;
    }

    public void addUsers(Users users) {
        this.userss.add(users);
    }

}