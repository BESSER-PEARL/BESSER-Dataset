




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Leave  {

    private int Leave_NoOfDays;
    private LocalDate Leave_StartDate;
    private LocalDate Leave_ApplyDate;
    private String Leave_Status;
    private String Leave_detail;
    private String Leave_Title;
    private int Emp_Id;
    private LocalDate Leave_EndDate;
    private int leave_id;



    public Leave(
        int Leave_NoOfDays,        LocalDate Leave_StartDate,        LocalDate Leave_ApplyDate,        String Leave_Status,        String Leave_detail,        String Leave_Title,        int Emp_Id,        LocalDate Leave_EndDate,        int leave_id    ) {
        this.Leave_NoOfDays = Leave_NoOfDays;
        this.Leave_StartDate = Leave_StartDate;
        this.Leave_ApplyDate = Leave_ApplyDate;
        this.Leave_Status = Leave_Status;
        this.Leave_detail = Leave_detail;
        this.Leave_Title = Leave_Title;
        this.Emp_Id = Emp_Id;
        this.Leave_EndDate = Leave_EndDate;
        this.leave_id = leave_id;
    }


    public int getLeave_noofdays() {
        return Leave_NoOfDays;
    }

    public void setLeave_noofdays(int Leave_NoOfDays) {
        this.Leave_NoOfDays = Leave_NoOfDays;
    }
    public LocalDate getLeave_startdate() {
        return Leave_StartDate;
    }

    public void setLeave_startdate(LocalDate Leave_StartDate) {
        this.Leave_StartDate = Leave_StartDate;
    }
    public LocalDate getLeave_applydate() {
        return Leave_ApplyDate;
    }

    public void setLeave_applydate(LocalDate Leave_ApplyDate) {
        this.Leave_ApplyDate = Leave_ApplyDate;
    }
    public String getLeave_status() {
        return Leave_Status;
    }

    public void setLeave_status(String Leave_Status) {
        this.Leave_Status = Leave_Status;
    }
    public String getLeave_detail() {
        return Leave_detail;
    }

    public void setLeave_detail(String Leave_detail) {
        this.Leave_detail = Leave_detail;
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
    public LocalDate getLeave_enddate() {
        return Leave_EndDate;
    }

    public void setLeave_enddate(LocalDate Leave_EndDate) {
        this.Leave_EndDate = Leave_EndDate;
    }
    public int getLeave_id() {
        return leave_id;
    }

    public void setLeave_id(int leave_id) {
        this.leave_id = leave_id;
    }


}