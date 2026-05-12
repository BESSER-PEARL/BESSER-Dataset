





import java.util.List;
import java.util.ArrayList;

public class Vacation  {

    private int Employee_ID;
    private String Expiry_date;
    private String Beginning_date;





    private Employee employee;


    public Vacation(
        int Employee_ID,        String Expiry_date,        String Beginning_date    ) {
        this.Employee_ID = Employee_ID;
        this.Expiry_date = Expiry_date;
        this.Beginning_date = Beginning_date;
    }


    public int getEmployee_id() {
        return Employee_ID;
    }

    public void setEmployee_id(int Employee_ID) {
        this.Employee_ID = Employee_ID;
    }
    public String getExpiry_date() {
        return Expiry_date;
    }

    public void setExpiry_date(String Expiry_date) {
        this.Expiry_date = Expiry_date;
    }
    public String getBeginning_date() {
        return Beginning_date;
    }

    public void setBeginning_date(String Beginning_date) {
        this.Beginning_date = Beginning_date;
    }

    public Employee getEmployee() {
        return employee;
    }

    public void setEmployee(Employee employee) {
        this.employee = employee;
    }

}