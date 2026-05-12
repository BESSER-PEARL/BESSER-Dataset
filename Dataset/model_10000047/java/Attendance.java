





import java.util.List;
import java.util.ArrayList;

public class Attendance  {

    private String OT_hours;
    private String date;
    private String work_hours;
    private String att_id;
    private String out_time;
    private String in_time;





    private Employee employee;


    public Attendance(
        String OT_hours,        String date,        String work_hours,        String att_id,        String out_time,        String in_time    ) {
        this.OT_hours = OT_hours;
        this.date = date;
        this.work_hours = work_hours;
        this.att_id = att_id;
        this.out_time = out_time;
        this.in_time = in_time;
    }


    public String getOt_hours() {
        return OT_hours;
    }

    public void setOt_hours(String OT_hours) {
        this.OT_hours = OT_hours;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getWork_hours() {
        return work_hours;
    }

    public void setWork_hours(String work_hours) {
        this.work_hours = work_hours;
    }
    public String getAtt_id() {
        return att_id;
    }

    public void setAtt_id(String att_id) {
        this.att_id = att_id;
    }
    public String getOut_time() {
        return out_time;
    }

    public void setOut_time(String out_time) {
        this.out_time = out_time;
    }
    public String getIn_time() {
        return in_time;
    }

    public void setIn_time(String in_time) {
        this.in_time = in_time;
    }

    public Employee getEmployee() {
        return employee;
    }

    public void setEmployee(Employee employee) {
        this.employee = employee;
    }

}