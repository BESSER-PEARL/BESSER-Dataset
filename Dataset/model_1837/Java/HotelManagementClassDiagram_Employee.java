





import java.util.List;
import java.util.ArrayList;

public class HotelManagementClassDiagram_Employee extends Person {

    private float workRate;
    private String password;
    private int employeeID;
    private float salary;



    public HotelManagementClassDiagram_Employee(
        float workRate,        String password,        int employeeID,        float salary    ) {
        super(
        );
        this.workRate = workRate;
        this.password = password;
        this.employeeID = employeeID;
        this.salary = salary;
    }


    public float getWorkrate() {
        return workRate;
    }

    public void setWorkrate(float workRate) {
        this.workRate = workRate;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public int getEmployeeid() {
        return employeeID;
    }

    public void setEmployeeid(int employeeID) {
        this.employeeID = employeeID;
    }
    public float getSalary() {
        return salary;
    }

    public void setSalary(float salary) {
        this.salary = salary;
    }


}