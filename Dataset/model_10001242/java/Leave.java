




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Leave  {

    private String Leave_detail;
    private int Leave_NoOfDays;
    private String Leave_Title;
    private LocalDate Leave_ApplyDate;
    private int Emp_Id;
    private LocalDate Leave_StartDate;
    private String Leave_Status;
    private int leave_id;
    private LocalDate Leave_EndDate;





    private Employee employee;


    public Leave(
        String Leave_detail,        int Leave_NoOfDays,        String Leave_Title,        LocalDate Leave_ApplyDate,        int Emp_Id,        LocalDate Leave_StartDate,        String Leave_Status,        int leave_id,        LocalDate Leave_EndDate    ) {
        this.Leave_detail = Leave_detail;
        this.Leave_NoOfDays = Leave_NoOfDays;
        this.Leave_Title = Leave_Title;
        this.Leave_ApplyDate = Leave_ApplyDate;
        this.Emp_Id = Emp_Id;
        this.Leave_StartDate = Leave_StartDate;
        this.Leave_Status = Leave_Status;
        this.leave_id = leave_id;
        this.Leave_EndDate = Leave_EndDate;
    }


    public String getLeave_detail() {
        return Leave_detail;
    }

    public void setLeave_detail(String Leave_detail) {
        this.Leave_detail = Leave_detail;
    }
    public int getLeave_noofdays() {
        return Leave_NoOfDays;
    }

    public void setLeave_noofdays(int Leave_NoOfDays) {
        this.Leave_NoOfDays = Leave_NoOfDays;
    }
    public String getLeave_title() {
        return Leave_Title;
    }

    public void setLeave_title(String Leave_Title) {
        this.Leave_Title = Leave_Title;
    }
    public LocalDate getLeave_applydate() {
        return Leave_ApplyDate;
    }

    public void setLeave_applydate(LocalDate Leave_ApplyDate) {
        this.Leave_ApplyDate = Leave_ApplyDate;
    }
    public int getEmp_id() {
        return Emp_Id;
    }

    public void setEmp_id(int Emp_Id) {
        this.Emp_Id = Emp_Id;
    }
    public LocalDate getLeave_startdate() {
        return Leave_StartDate;
    }

    public void setLeave_startdate(LocalDate Leave_StartDate) {
        this.Leave_StartDate = Leave_StartDate;
    }
    public String getLeave_status() {
        return Leave_Status;
    }

    public void setLeave_status(String Leave_Status) {
        this.Leave_Status = Leave_Status;
    }
    public int getLeave_id() {
        return leave_id;
    }

    public void setLeave_id(int leave_id) {
        this.leave_id = leave_id;
    }
    public LocalDate getLeave_enddate() {
        return Leave_EndDate;
    }

    public void setLeave_enddate(LocalDate Leave_EndDate) {
        this.Leave_EndDate = Leave_EndDate;
    }

    public Employee getEmployee() {
        return employee;
    }

    public void setEmployee(Employee employee) {
        this.employee = employee;
    }

}