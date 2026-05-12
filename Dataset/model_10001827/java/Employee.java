





import java.util.List;
import java.util.ArrayList;

public class Employee  {

    private String employeeID;
    private String salary;



    public Employee(
        String employeeID,        String salary    ) {
        this.employeeID = employeeID;
        this.salary = salary;
    }


    public String getEmployeeid() {
        return employeeID;
    }

    public void setEmployeeid(String employeeID) {
        this.employeeID = employeeID;
    }
    public String getSalary() {
        return salary;
    }

    public void setSalary(String salary) {
        this.salary = salary;
    }


}