





import java.util.List;
import java.util.ArrayList;

public class SessionManager  {

    private String userid;
    private String departmentName;





    private User user;


    public SessionManager(
        String userid,        String departmentName    ) {
        this.userid = userid;
        this.departmentName = departmentName;
    }


    public String getUserid() {
        return userid;
    }

    public void setUserid(String userid) {
        this.userid = userid;
    }
    public String getDepartmentname() {
        return departmentName;
    }

    public void setDepartmentname(String departmentName) {
        this.departmentName = departmentName;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}