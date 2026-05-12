




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Attendance  {

    private String endTime;
    private LocalDate Date;
    private String Emp_id;
    private String startTime;





    private Employee employee;


    public Attendance(
        String endTime,        LocalDate Date,        String Emp_id,        String startTime    ) {
        this.endTime = endTime;
        this.Date = Date;
        this.Emp_id = Emp_id;
        this.startTime = startTime;
    }


    public String getEndtime() {
        return endTime;
    }

    public void setEndtime(String endTime) {
        this.endTime = endTime;
    }
    public LocalDate getDate() {
        return Date;
    }

    public void setDate(LocalDate Date) {
        this.Date = Date;
    }
    public String getEmp_id() {
        return Emp_id;
    }

    public void setEmp_id(String Emp_id) {
        this.Emp_id = Emp_id;
    }
    public String getStarttime() {
        return startTime;
    }

    public void setStarttime(String startTime) {
        this.startTime = startTime;
    }

    public Employee getEmployee() {
        return employee;
    }

    public void setEmployee(Employee employee) {
        this.employee = employee;
    }

}