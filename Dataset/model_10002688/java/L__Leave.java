





import java.util.List;
import java.util.ArrayList;

public class L__Leave  {

    private String leave_id;
    private String Leave_NoOfDays;
    private String Leave_EndDate;
    private String Leave_detail;
    private String Leave_ApplyDate;
    private String Leave_Status;
    private String Leave_StartDate;
    private String Emp_Id;
    private String Leave_Title;





    private User user;


    public L__Leave(
        String leave_id,        String Leave_NoOfDays,        String Leave_EndDate,        String Leave_detail,        String Leave_ApplyDate,        String Leave_Status,        String Leave_StartDate,        String Emp_Id,        String Leave_Title    ) {
        this.leave_id = leave_id;
        this.Leave_NoOfDays = Leave_NoOfDays;
        this.Leave_EndDate = Leave_EndDate;
        this.Leave_detail = Leave_detail;
        this.Leave_ApplyDate = Leave_ApplyDate;
        this.Leave_Status = Leave_Status;
        this.Leave_StartDate = Leave_StartDate;
        this.Emp_Id = Emp_Id;
        this.Leave_Title = Leave_Title;
    }


    public String getLeave_id() {
        return leave_id;
    }

    public void setLeave_id(String leave_id) {
        this.leave_id = leave_id;
    }
    public String getLeave_noofdays() {
        return Leave_NoOfDays;
    }

    public void setLeave_noofdays(String Leave_NoOfDays) {
        this.Leave_NoOfDays = Leave_NoOfDays;
    }
    public String getLeave_enddate() {
        return Leave_EndDate;
    }

    public void setLeave_enddate(String Leave_EndDate) {
        this.Leave_EndDate = Leave_EndDate;
    }
    public String getLeave_detail() {
        return Leave_detail;
    }

    public void setLeave_detail(String Leave_detail) {
        this.Leave_detail = Leave_detail;
    }
    public String getLeave_applydate() {
        return Leave_ApplyDate;
    }

    public void setLeave_applydate(String Leave_ApplyDate) {
        this.Leave_ApplyDate = Leave_ApplyDate;
    }
    public String getLeave_status() {
        return Leave_Status;
    }

    public void setLeave_status(String Leave_Status) {
        this.Leave_Status = Leave_Status;
    }
    public String getLeave_startdate() {
        return Leave_StartDate;
    }

    public void setLeave_startdate(String Leave_StartDate) {
        this.Leave_StartDate = Leave_StartDate;
    }
    public String getEmp_id() {
        return Emp_Id;
    }

    public void setEmp_id(String Emp_Id) {
        this.Emp_Id = Emp_Id;
    }
    public String getLeave_title() {
        return Leave_Title;
    }

    public void setLeave_title(String Leave_Title) {
        this.Leave_Title = Leave_Title;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}