





import java.util.List;
import java.util.ArrayList;

public class Attendance  {

    private String atten_date;
    private String atten_type;
    private int atten_emp_id;
    private int atten_time;
    private int atten_id;





    private Admin admin;




    private Employee employee;




    private Employee employee;


    public Attendance(
        String atten_date,        String atten_type,        int atten_emp_id,        int atten_time,        int atten_id    ) {
        this.atten_date = atten_date;
        this.atten_type = atten_type;
        this.atten_emp_id = atten_emp_id;
        this.atten_time = atten_time;
        this.atten_id = atten_id;
    }


    public String getAtten_date() {
        return atten_date;
    }

    public void setAtten_date(String atten_date) {
        this.atten_date = atten_date;
    }
    public String getAtten_type() {
        return atten_type;
    }

    public void setAtten_type(String atten_type) {
        this.atten_type = atten_type;
    }
    public int getAtten_emp_id() {
        return atten_emp_id;
    }

    public void setAtten_emp_id(int atten_emp_id) {
        this.atten_emp_id = atten_emp_id;
    }
    public int getAtten_time() {
        return atten_time;
    }

    public void setAtten_time(int atten_time) {
        this.atten_time = atten_time;
    }
    public int getAtten_id() {
        return atten_id;
    }

    public void setAtten_id(int atten_id) {
        this.atten_id = atten_id;
    }

    public Admin getAdmin() {
        return admin;
    }

    public void setAdmin(Admin admin) {
        this.admin = admin;
    }
    public Employee getEmployee() {
        return employee;
    }

    public void setEmployee(Employee employee) {
        this.employee = employee;
    }
    public Employee getEmployee() {
        return employee;
    }

    public void setEmployee(Employee employee) {
        this.employee = employee;
    }

}