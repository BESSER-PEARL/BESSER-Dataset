




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Attendance  {

    private String Emp_id;
    private String Leaving_Time;
    private LocalDate Attend_date;
    private String AttendTime;





    private Employee employee;


    public Attendance(
        String Emp_id,        String Leaving_Time,        LocalDate Attend_date,        String AttendTime    ) {
        this.Emp_id = Emp_id;
        this.Leaving_Time = Leaving_Time;
        this.Attend_date = Attend_date;
        this.AttendTime = AttendTime;
    }


    public String getEmp_id() {
        return Emp_id;
    }

    public void setEmp_id(String Emp_id) {
        this.Emp_id = Emp_id;
    }
    public String getLeaving_time() {
        return Leaving_Time;
    }

    public void setLeaving_time(String Leaving_Time) {
        this.Leaving_Time = Leaving_Time;
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

    public Employee getEmployee() {
        return employee;
    }

    public void setEmployee(Employee employee) {
        this.employee = employee;
    }

}