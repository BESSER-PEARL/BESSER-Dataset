





import java.util.List;
import java.util.ArrayList;

public class Leave  {

    private String leave_type;
    private String from;
    private String leave_id;
    private String to;
    private String date;





    private Employee employee;


    public Leave(
        String leave_type,        String from,        String leave_id,        String to,        String date    ) {
        this.leave_type = leave_type;
        this.from = from;
        this.leave_id = leave_id;
        this.to = to;
        this.date = date;
    }


    public String getLeave_type() {
        return leave_type;
    }

    public void setLeave_type(String leave_type) {
        this.leave_type = leave_type;
    }
    public String getFrom() {
        return from;
    }

    public void setFrom(String from) {
        this.from = from;
    }
    public String getLeave_id() {
        return leave_id;
    }

    public void setLeave_id(String leave_id) {
        this.leave_id = leave_id;
    }
    public String getTo() {
        return to;
    }

    public void setTo(String to) {
        this.to = to;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public Employee getEmployee() {
        return employee;
    }

    public void setEmployee(Employee employee) {
        this.employee = employee;
    }

}