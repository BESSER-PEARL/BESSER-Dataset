





import java.util.List;
import java.util.ArrayList;

public class login  {

    private String loginUsername;
    private String loginStatus;
    private int login_id;
    private String loginpassword;





    private Admin admin;




    private Employee employee;


    public login(
        String loginUsername,        String loginStatus,        int login_id,        String loginpassword    ) {
        this.loginUsername = loginUsername;
        this.loginStatus = loginStatus;
        this.login_id = login_id;
        this.loginpassword = loginpassword;
    }


    public String getLoginusername() {
        return loginUsername;
    }

    public void setLoginusername(String loginUsername) {
        this.loginUsername = loginUsername;
    }
    public String getLoginstatus() {
        return loginStatus;
    }

    public void setLoginstatus(String loginStatus) {
        this.loginStatus = loginStatus;
    }
    public int getLogin_id() {
        return login_id;
    }

    public void setLogin_id(int login_id) {
        this.login_id = login_id;
    }
    public String getLoginpassword() {
        return loginpassword;
    }

    public void setLoginpassword(String loginpassword) {
        this.loginpassword = loginpassword;
    }

    public Admin getAdmin() {
        return admin;
    }

    public void setAdmin(Admin admin) {
        this.admin = admin;
    }
    public Employee getEmployee() {
        return employee;
    }

    public void setEmployee(Employee employee) {
        this.employee = employee;
    }

}