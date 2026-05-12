





import java.util.List;
import java.util.ArrayList;

public class Attendance  {

    private String Attend_date;
    private String Leaving_Time;
    private String Emp_id;
    private String AttendTime;





    private User user;


    public Attendance(
        String Attend_date,        String Leaving_Time,        String Emp_id,        String AttendTime    ) {
        this.Attend_date = Attend_date;
        this.Leaving_Time = Leaving_Time;
        this.Emp_id = Emp_id;
        this.AttendTime = AttendTime;
    }


    public String getAttend_date() {
        return Attend_date;
    }

    public void setAttend_date(String Attend_date) {
        this.Attend_date = Attend_date;
    }
    public String getLeaving_time() {
        return Leaving_Time;
    }

    public void setLeaving_time(String Leaving_Time) {
        this.Leaving_Time = Leaving_Time;
    }
    public String getEmp_id() {
        return Emp_id;
    }

    public void setEmp_id(String Emp_id) {
        this.Emp_id = Emp_id;
    }
    public String getAttendtime() {
        return AttendTime;
    }

    public void setAttendtime(String AttendTime) {
        this.AttendTime = AttendTime;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}