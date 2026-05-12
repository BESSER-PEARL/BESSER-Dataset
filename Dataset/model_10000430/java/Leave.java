




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Leave  {

    private LocalDate Leave_EndDate;
    private String Leave_detail;
    private int leave_id;
    private String Leave_Status;
    private String Leave_Title;
    private int Emp_Id;





    private Employee employee;


    public Leave(
        LocalDate Leave_EndDate,        String Leave_detail,        int leave_id,        String Leave_Status,        String Leave_Title,        int Emp_Id    ) {
        this.Leave_EndDate = Leave_EndDate;
        this.Leave_detail = Leave_detail;
        this.leave_id = leave_id;
        this.Leave_Status = Leave_Status;
        this.Leave_Title = Leave_Title;
        this.Emp_Id = Emp_Id;
    }


    public LocalDate getLeave_enddate() {
        return Leave_EndDate;
    }

    public void setLeave_enddate(LocalDate Leave_EndDate) {
        this.Leave_EndDate = Leave_EndDate;
    }
    public String getLeave_detail() {
        return Leave_detail;
    }

    public void setLeave_detail(String Leave_detail) {
        this.Leave_detail = Leave_detail;
    }
    public int getLeave_id() {
        return leave_id;
    }

    public void setLeave_id(int leave_id) {
        this.leave_id = leave_id;
    }
    public String getLeave_status() {
        return Leave_Status;
    }

    public void setLeave_status(String Leave_Status) {
        this.Leave_Status = Leave_Status;
    }
    public String getLeave_title() {
        return Leave_Title;
    }

    public void setLeave_title(String Leave_Title) {
        this.Leave_Title = Leave_Title;
    }
    public int getEmp_id() {
        return Emp_Id;
    }

    public void setEmp_id(int Emp_Id) {
        this.Emp_Id = Emp_Id;
    }

    public Employee getEmployee() {
        return employee;
    }

    public void setEmployee(Employee employee) {
        this.employee = employee;
    }

}