




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Attendance  {

    private LocalDate Attend_date;
    private String AttendTime;
    private String Leaving_Time;
    private String Emp_id;





    private Manager manager;


    public Attendance(
        LocalDate Attend_date,        String AttendTime,        String Leaving_Time,        String Emp_id    ) {
        this.Attend_date = Attend_date;
        this.AttendTime = AttendTime;
        this.Leaving_Time = Leaving_Time;
        this.Emp_id = Emp_id;
    }


    public LocalDate getAttend_date() {
        return Attend_date;
    }

    public void setAttend_date(LocalDate Attend_date) {
        this.Attend_date = Attend_date;
    }
    public String getAttendtime() {
        return AttendTime;
    }

    public void setAttendtime(String AttendTime) {
        this.AttendTime = AttendTime;
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

    public Manager getManager() {
        return manager;
    }

    public void setManager(Manager manager) {
        this.manager = manager;
    }

}