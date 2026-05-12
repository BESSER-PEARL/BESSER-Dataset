





import java.util.List;
import java.util.ArrayList;

public class Profile  {

    private String user_Name;
    private String password;
    private String l_Name;
    private String f_Name;





    private Attendance attendance;


    public Profile(
        String user_Name,        String password,        String l_Name,        String f_Name    ) {
        this.user_Name = user_Name;
        this.password = password;
        this.l_Name = l_Name;
        this.f_Name = f_Name;
    }


    public String getUser_name() {
        return user_Name;
    }

    public void setUser_name(String user_Name) {
        this.user_Name = user_Name;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getL_name() {
        return l_Name;
    }

    public void setL_name(String l_Name) {
        this.l_Name = l_Name;
    }
    public String getF_name() {
        return f_Name;
    }

    public void setF_name(String f_Name) {
        this.f_Name = f_Name;
    }

    public Attendance getAttendance() {
        return attendance;
    }

    public void setAttendance(Attendance attendance) {
        this.attendance = attendance;
    }

}