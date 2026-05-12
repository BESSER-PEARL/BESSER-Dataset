





import java.util.List;
import java.util.ArrayList;

public class Leave  {

    private int Leave_NoOfDays;
    private String Leave_Detail;
    private String attribute;





    private Employee employee;


    public Leave(
        int Leave_NoOfDays,        String Leave_Detail,        String attribute    ) {
        this.Leave_NoOfDays = Leave_NoOfDays;
        this.Leave_Detail = Leave_Detail;
        this.attribute = attribute;
    }


    public int getLeave_noofdays() {
        return Leave_NoOfDays;
    }

    public void setLeave_noofdays(int Leave_NoOfDays) {
        this.Leave_NoOfDays = Leave_NoOfDays;
    }
    public String getLeave_detail() {
        return Leave_Detail;
    }

    public void setLeave_detail(String Leave_Detail) {
        this.Leave_Detail = Leave_Detail;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }

    public Employee getEmployee() {
        return employee;
    }

    public void setEmployee(Employee employee) {
        this.employee = employee;
    }

}