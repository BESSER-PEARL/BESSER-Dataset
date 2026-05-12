





import java.util.List;
import java.util.ArrayList;

public class DaysAttended  {

    private String Emp_Id;
    private String Emp_BasicSalary;
    private String Additional_hours__;





    private Employee employee;


    public DaysAttended(
        String Emp_Id,        String Emp_BasicSalary,        String Additional_hours__    ) {
        this.Emp_Id = Emp_Id;
        this.Emp_BasicSalary = Emp_BasicSalary;
        this.Additional_hours__ = Additional_hours__;
    }


    public String getEmp_id() {
        return Emp_Id;
    }

    public void setEmp_id(String Emp_Id) {
        this.Emp_Id = Emp_Id;
    }
    public String getEmp_basicsalary() {
        return Emp_BasicSalary;
    }

    public void setEmp_basicsalary(String Emp_BasicSalary) {
        this.Emp_BasicSalary = Emp_BasicSalary;
    }
    public String getAdditional_hours__() {
        return Additional_hours__;
    }

    public void setAdditional_hours__(String Additional_hours__) {
        this.Additional_hours__ = Additional_hours__;
    }

    public Employee getEmployee() {
        return employee;
    }

    public void setEmployee(Employee employee) {
        this.employee = employee;
    }

}